# Шаблоны PyAEDT

Код для `run_python_code`. Проверяйте под свою задачу — это каркасы, не готовые решения.

Установка: AEDT 2024 R2, `version="2024.2"`. Указывайте версию всегда.

## Общее

```python
from ansys.aedt.core import Desktop, Maxwell3d, Maxwell2d, Hfss, Q3d, Icepak, Circuit, Hfss3dLayout

# Сессия persistent — переменные живут между вызовами run_python_code.
# Проект открыт один раз, дальше работаем в нём.
```

Единицы задаются явно, иначе легко получить метры вместо миллиметров:

```python
m3d.modeler.model_units = "mm"
```

## Maxwell 3D — магнитостатика

```python
from ansys.aedt.core import Maxwell3d

m3d = Maxwell3d(project="Motor", design="Static", solution_type="Magnetostatic", version="2024.2")
m3d.modeler.model_units = "mm"

# Геометрия
core = m3d.modeler.create_box([0, 0, 0], [50, 50, 20], name="Core", material="steel_1008")
coil = m3d.modeler.create_box([10, 10, 5], [10, 30, 10], name="Coil", material="copper")

# Материал с нелинейной BH-кривой задаётся до назначения
# m3d.materials["steel_1008"].permeability.value = ...

# Возбуждение: ток через обмотку
m3d.assign_coil(assignment=["Coil"], conductors_number=100, name="CoilTerm")
wdg = m3d.assign_winding(assignment=["CoilTerm"], winding_type="Current", current=5, name="Winding1")

# Область расчёта — без неё задача незамкнута
m3d.modeler.create_region(pad_percent=200)

# Сетка: уплотнение по интересующим телам
m3d.mesh.assign_length_mesh(["Core"], maximum_length=2, name="CoreMesh")

setup = m3d.create_setup(name="Setup1")
setup.props["MaximumPasses"] = 10
setup.props["PercentError"] = 1
m3d.save_project()
```

Расчёт сил и момента:

```python
m3d.assign_force(["Rotor"], force_name="ForceRotor")
m3d.assign_torque(["Rotor"], axis="Z", torque_name="TorqueRotor")
```

## Maxwell 2D — вихревые токи

```python
from ansys.aedt.core import Maxwell2d

m2d = Maxwell2d(project="Eddy", design="EddyCurrent",
                solution_type="EddyCurrent", version="2024.2")
m2d.modeler.model_units = "mm"

# 2D работает в плоскости XY (или осесимметрия RZ)
rect = m2d.modeler.create_rectangle([0, 0, 0], [20, 10], name="Conductor", material="copper")
m2d.assign_current([rect.name], amplitude="10A", name="I1")
m2d.modeler.create_region(pad_percent=300)

setup = m2d.create_setup(name="Setup1")
setup.props["Frequency"] = "50Hz"
```

## Движение — вращение ротора

```python
m3d.assign_rotate_motion(
    assignment="Band",           # тело-band вокруг ротора
    coordinate_system="Global",
    axis="Z",
    positive_movement=True,
    start_position=0,
    angular_velocity="1000rpm",
)
```

Требует `solution_type="Transient"` и корректно построенного band-объекта, охватывающего вращающуюся часть.

## HFSS — S-параметры

```python
from ansys.aedt.core import Hfss

hfss = Hfss(project="Filter", design="SParam", solution_type="DrivenModal", version="2024.2")
hfss.modeler.model_units = "mm"

# Волновой порт на прямоугольнике
hfss.wave_port(assignment="PortSheet", name="P1", renormalize=True, impedance=50)

# Или сосредоточенный порт
# hfss.lumped_port(assignment="Sheet", integration_line=..., impedance=50, name="P1")

hfss.assign_radiation_boundary_to_objects("Airbox")

setup = hfss.create_setup(name="Setup1")
setup.props["Frequency"] = "10GHz"
setup.props["MaximumPasses"] = 15
setup.props["MaxDeltaS"] = 0.02

sweep = setup.create_frequency_sweep(unit="GHz", start_frequency=1, stop_frequency=20,
                                     num_of_freq_points=401, sweep_type="Interpolating")
```

## Q3D — паразитные параметры

```python
from ansys.aedt.core import Q3d

q3d = Q3d(project="Parasitics", version="2024.2")
q3d.auto_identify_nets()
q3d.assign_source_to_objectface("Trace", axisdir=0, source_name="Src1")
q3d.assign_sink_to_objectface("Trace", axisdir=3, sink_name="Snk1")
setup = q3d.create_setup()
setup.props["AdaptiveFreq"] = "1GHz"
```

## Icepak — тепловой расчёт

```python
from ansys.aedt.core import Icepak

ipk = Icepak(project="Thermal", version="2024.2")
ipk.modeler.model_units = "mm"

ipk.assign_source("Chip", thermal_condition="Total Power", assignment_value="5W", boundary_name="ChipPower")
ipk.create_openregion(pad_percent=50)
ipk.assign_free_opening(ipk.modeler.get_object_faces("Region"), flow_type="Pressure")

setup = ipk.create_setup()
setup.props["Convergence Criteria - Max Iterations"] = 250
```

Связка EM → тепло: результат Maxwell/HFSS как источник тепла в Icepak через `ipk.assign_em_losses(...)`.

## EDB / SIwave — layout без GUI

Для PCB-задач это основной путь. EDB работает с базой layout напрямую, GUI не запускается — быстро и скриптуемо.

```python
from pyedb import Edb

edb = Edb(edbpath=r"C:\path\board.aedb", edbversion="2024.2")

# Инспекция
print("Nets:", len(edb.nets.nets))
print("Components:", len(edb.components.components))
print("Stackup:", list(edb.stackup.layers.keys()))

# Питание: найти PWR/GND
power_nets = [n for n in edb.nets.nets if n.upper().startswith(("VCC", "VDD", "PWR"))]

# Вырезать участок вокруг сигнальной цепи (ускоряет расчёт в разы)
edb.cutout(signal_list=["DDR_DQ0"], reference_list=["GND"], expansion_size=0.005)

edb.save_edb()
edb.close_edb()
```

Обязательно `close_edb()` — иначе база остаётся заблокированной.

Запуск расчёта SIwave по подготовленной базе:

```python
from ansys.aedt.core import Siwave

siw = Siwave(specified_version="2024.2")
siw.open_project(r"C:\path\board.siw")
siw.run_dc_simulation()          # DC IR-drop
siw.export_element_data(r"C:\out\dc_results.txt")
siw.save_project()
siw.close_project()
siw.quit_application()
```

SI/PI-анализ через SIwave часто удобнее готовить в EDB (`edb.siwave.create_exec_file()`), затем запускать `siwave_ng.exe` в batch.

## HFSS 3D Layout

```python
from ansys.aedt.core import Hfss3dLayout

h3d = Hfss3dLayout(project=r"C:\path\board.aedt", version="2024.2")
setup = h3d.create_setup("Setup1")
setup.props["Frequency"] = "5GHz"
```

## Параметрика и Optimetrics

```python
# Переменные проекта ($ — глобальная, без $ — на дизайн)
m3d["gap"] = "1mm"
m3d["turns"] = 100
m3d["$global_temp"] = "25cel"

# Параметрический свип
sweep = m3d.parametrics.add(variable="gap", start_point=0.5, end_point=3,
                            step=0.5, variation_type="LinearStep")

# Оптимизация
opt = m3d.optimizations.add(calculation="Torque", ranges={}, optimization_type="Optimization")
opt.add_variation("gap", 0.5, 3, 0.1)
```

## Экспорт результатов

```python
# Отчёт по решению
report = m3d.post.create_report("Torque")
report.export_to_file(r"C:\out\torque.csv")

# Данные решения в Python
sol = m3d.post.get_solution_data(expressions="Torque")
print(sol.primary_sweep_values)
print(sol.data_real())

# S-параметры Touchstone из HFSS
hfss.export_touchstone(output_file=r"C:\out\filter.s2p")

# Поля
m3d.post.export_field_file(quantity="Mag_B", output_file=r"C:\out\B.fld")

# Картинка модели
m3d.plot(show=False, output_file=r"C:\out\model.png")
```

## Типовые ошибки

**Забыли область расчёта.** Без `create_region` / `create_openregion` задача не замкнута — решатель либо падает, либо считает бессмыслицу.

**Единицы.** `model_units` по умолчанию может быть не тем, что вы ждёте. Задавайте явно. Числа без единиц трактуются в текущих `model_units`, строки (`"5mm"`) — явно.

**Имена объектов.** PyAEDT молча переименует при коллизии (`Box1` → `Box1_1`), и дальнейшие ссылки по старому имени не найдут объект. Проверяйте `obj.name` после создания.

**Материал не назначен.** `create_box` без `material` даёт вакуум. Для магнитных задач это тихо ломает результат.

**`solution_type` задаётся при создании** дизайна и потом меняется тяжело. Магнитостатика, вихревые токи, transient — разные типы.

**Сессия persistent.** Старая переменная из предыдущего вызова `run_python_code` может указывать на закрытый проект. При странных ошибках проверьте namespace.

**Сохранение не автоматическое.** `save_project()` явно, иначе работа потеряется.

**Осесимметрия в 2D.** Maxwell 2D в режиме RZ считает на радиан или на полный оборот в зависимости от настройки — проверяйте нормировку результата.
