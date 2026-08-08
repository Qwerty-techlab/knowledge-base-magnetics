# Библиография базы знаний

Файл сгенерирован автоматически из `bibliography.json` скриптом
`skills/make_bibliography.py`. **Правьте `bibliography.json`, не этот файл.**

Обновлено: 2026-08-07. Записей: 37, из них с DOI: 13.

> 10 записей помечены `derived_from_filename` — заголовок восстановлен по имени файла,
> точная библиографическая запись не выверена. Перед цитированием в отчёте сверяйте с PDF.

У каждой статьи в её папке лежат: `source.pdf` (исходник, **не** в git), `parsed.md` (извлечённый
текст — читайте его, а не PDF) и `metadata.json` (метаданные и оценка качества извлечения).

---

## Interleaved boost и многофазные преобразователи

Папка: `articles/01_interleaved_boost/`

**1. Fairchild Semiconductor, *AN-6086 Design Consideration for Interleaved Boundary Conduction Mode PFC Using FAN9611/12*, Fairchild Application Note AN-6086.**

- Папка: `01_interleaved_boost/Fairchild_AN6086_Interleaved_BCM_PFC_FAN9611/`, 18 стр.
- Применение: Граничный режим (BCM) в interleaved PFC — для сопоставления с выбранным CCM.
- Ключевые слова: interleaved, BCM, граничный режим, PFC

**2. *Multiphase Boost Converter with Coupled Inductor for Ripple Reduction*, IJERA.**  ⚠ запись не выверена

- Папка: `01_interleaved_boost/IJERA_Multiphase_Boost_Coupled_Inductor_Ripple/`, 6 стр.
- Применение: Обзорный источник по снижению пульсации в многофазном boost.
- Ключевые слова: многофазный boost, снижение пульсации

**3. *Interleaved Boost Converter with Zero Ripple and Integrated EMI Filter*, Journal of Power Electronics (JPE), 2016.**  ⚠ запись не выверена

- Папка: `01_interleaved_boost/JPE_2016_Interleaved_Boost_ZeroRipple_EMI_Filter/`, 11 стр.
- Применение: Совмещение подавления пульсации с ЭМС-фильтром.
- Ключевые слова: нулевая пульсация, EMI-фильтр, ЭМС

**4. *The Study of the Operational Characteristic of Interleaved Boost Converter with Modified Coupled Inductor*, MDPI (журнал уточнить), 2019.**

- Папка: `01_interleaved_boost/MDPI_2019_Interleaved_Boost_Modified_Coupled_Inductor/`, 18 стр.
- Применение: Связанные дроссели в interleaved boost — рассмотрено и отклонено (ТЗ требует независимых дросселей).
- Ключевые слова: связанный дроссель, coupled inductor

**5. *NSGA-II Based Co-Design of Interleaved Boost Converter for Electric Vehicles*, MDPI (журнал уточнить), 2020.**  ⚠ запись не выверена

- Папка: `01_interleaved_boost/MDPI_2020_NSGA2_Codesign_Interleaved_Boost_EV/`, 35 стр.
- Применение: Многокритериальная оптимизация (NSGA-II) параметров interleaved boost.
- Ключевые слова: NSGA-II, многокритериальная оптимизация, co-design

**6. *Three-Legs Interleaved Boost PFC Converter, 3 kW*, MDPI (журнал уточнить), 2020.**  ⚠ запись не выверена

- Папка: `01_interleaved_boost/MDPI_2020_ThreeLegs_Interleaved_Boost_PFC_3kW/`, 16 стр.
- Применение: Трёхплечевой interleaved PFC на 3 кВт — близкий по мощности прототип.
- Ключевые слова: трёхфазный interleaved, PFC, 3 кВт

**7. *Differential Mode Noise Estimation and Filter Design for Interleaved Boost PFC*, MDPI (журнал уточнить), 2021.**

- Папка: `01_interleaved_boost/MDPI_2021_DM_EMI_Filter_Interleaved_Boost_PFC/`, 17 стр.
- Применение: Оценка дифференциальной помехи и синтез фильтра для interleaved boost — основа раздела ЭМС.
- Ключевые слова: ЭМС, дифференциальная помеха, EMI-фильтр, interleaved

**8. *Differential Evolution Based Algorithm for Optimal Current Ripple Cancellation in an Unequally Interleaved Converter*, MDPI (журнал уточнить), 2021.**

- Папка: `01_interleaved_boost/MDPI_2021_Optimal_Ripple_Cancellation_Unequal_Interleaved/`, 17 стр.
- Применение: Оптимизация подавления пульсации при неравномерном сдвиге фаз.
- Ключевые слова: подавление пульсации, неравномерный сдвиг, оптимизация

**9. *Efficient Multi-Phase Converter for E-Mobility*, MDPI (журнал уточнить), 2022.**

- Папка: `01_interleaved_boost/MDPI_2022_Efficient_MultiPhase_Converter_EMobility/`, 16 стр.
- Применение: Многофазный преобразователь для электротранспорта — выбор числа фаз по КПД.
- Ключевые слова: многофазный, КПД, число фаз, электротранспорт

**10. *Floating Interleaved Boost Converter with Zero Ripple Using a Variable Inductor*, MDPI (журнал уточнить), 2023.**  ⚠ запись не выверена

- Папка: `01_interleaved_boost/MDPI_2023_Floating_Interleaved_Boost_VariableInductor/`, 16 стр.
- Применение: Нулевая пульсация через управляемую индуктивность — альтернативная схема, не применена.
- Ключевые слова: нулевая пульсация, управляемая индуктивность

**11. *Design and Analysis of a Three-Phase Interleaved DC-DC Boost Converter for PV and ESS Applications*, MDPI (журнал уточнить), 2024.**

- Папка: `01_interleaved_boost/MDPI_2024_ThreePhase_Interleaved_Boost_PV_ESS/`, 14 стр.
- Применение: Ключевой источник по ТРЁХФАЗНОМУ interleaved boost: сдвиг 120°, подавление пульсации в 5,3 раза, частоты 3·f_sw.
- Ключевые слова: трёхфазный interleaved, сдвиг 120°, подавление пульсации, PV, ESS

**12. Texas Instruments, *350-W, Two Phase Interleaved PFC Pre-Regulator (Rev. C)*, TI Application Report SLUA369C.**

- Папка: `01_interleaved_boost/TI_SLUA369C_350W_TwoPhase_Interleaved_PFC/`, 22 стр.
- Применение: Полный пример расчёта двухфазного PFC с номиналами: сверка порядка величин индуктивности и токов.
- Ключевые слова: interleaved, PFC, пример расчёта

**13. Texas Instruments, *UCC28070 300W Interleaved PFC Pre-regulator Design Review*, TI Application Report SLUA479B.**

- Папка: `01_interleaved_boost/TI_SLUA479B_UCC28070_Interleaved_PFC_DesignReview/`, 27 стр.
- Применение: Разбор проекта на UCC28070: сдвиг фаз 180°, влияние на пульсации и ЭМС.
- Ключевые слова: interleaved, PFC, UCC28070, сдвиг фаз

**14. Texas Instruments, *An Interleaved PFC Preregulator for High-Power Converters*, TI Application Report SLUA746.**

- Папка: `01_interleaved_boost/TI_SLUA746_Interleaved_PFC_Preregulator_HighPower/`, 17 стр.
- Применение: Базовая методика двухфазного interleaved PFC: расчёт тока фазы, коэффициент подавления пульсации входного тока, выбор индуктивности.
- Ключевые слова: interleaved, PFC, пульсации входного тока, методика TI

**15. Texas Instruments, *AN-1820 LM5032 Interleaved Boost Converter (Rev. A)*, TI Application Note SNVA335A.**

- Папка: `01_interleaved_boost/TI_SNVA335A_AN1820_LM5032_Interleaved_Boost/`, 13 стр.
- Применение: Interleaved boost (не PFC) — режим CCM, распределение тока между фазами.
- Ключевые слова: interleaved boost, CCM, распределение тока

**16. *Analysis of a Four-Phase Interleaved DC-DC Converter in CCM*, WSEAS Transactions, 2018.**  ⚠ запись не выверена

- Папка: `01_interleaved_boost/WSEAS_2018_FourPhase_Interleaved_DCDC_CCM/`, 11 стр.
- Применение: Четырёхфазный вариант — оценка выигрыша при N>3.
- Ключевые слова: четырёхфазный, CCM, interleaved

---

## Базовый boost, CCM PFC, выбор режима

Папка: `articles/02_basic_boost_pfc/`

**1. Infineon Technologies, *Design guide PFC CCM boost converter*, Infineon Application Note.**

- Папка: `02_basic_boost_pfc/Infineon_Design_Guide_PFC_CCM_Boost/`, 30 стр.
- Применение: Проектирование CCM boost PFC: выбор индуктивности, оценка потерь, тепловой расчёт.
- Ключевые слова: CCM, PFC, boost, методика Infineon

**2. Infineon Technologies, *EVAL-PFC5KIKWWR5SYS - User Guide (5 kW CCM PFC)*, Infineon Evaluation Board User Guide.**

- Папка: `02_basic_boost_pfc/Infineon_EVAL_PFC5K_5kW_CCM_PFC_UserGuide/`, 38 стр.
- Применение: Референс-дизайн 5 кВт CCM PFC — сверка порядка величин с расчётом на 6 кВт.
- Ключевые слова: 5 кВт, референс-дизайн, CCM PFC

**3. Infineon Technologies, *High switching frequency CCM PFC operation with TRENCHSTOP 5 WR5 IGBT*, Infineon Application Note.**

- Папка: `02_basic_boost_pfc/Infineon_High_Switching_Frequency_CCM_PFC/`, 23 стр.
- Применение: Обоснование выбора частоты коммутации 100…150 кГц: баланс потерь в ключах и магнитных элементах.
- Ключевые слова: частота коммутации, CCM, PFC, выбор частоты

**4. P. Papamanolis, T. Guillod, F. Krismer, J. W. Kolar, *Minimum Loss Operation and Optimal Design of High-Frequency Inductors for Defined Core and Litz Wire*, IEEE Open Journal of Power Electronics (OJPEL), 2020. DOI: [10.1109/OJPEL.2020.3027452](https://doi.org/10.1109/OJPEL.2020.3027452)**

- Папка: `02_basic_boost_pfc/Papamanolis_2020_Minimal_Loss_Operation/`, 20 стр.
- Применение: Совместная оптимизация потерь в сердечнике и литцендрате, температурная обратная связь, выбор точки минимума суммарных потерь.
- Ключевые слова: минимум потерь, оптимальное проектирование, литцендрат, тепловая связь
- Примечание: Файл 16_Minimal-Loss-Operation_ACCEPTED-VERSION_Papamanolis_OJ-PEL.pdf в 0_references — побайтовый дубликат этого же PDF.

**5. Texas Instruments (B. Hauke), *Basic Calculation of a Boost Converter's Power Stage (Rev. D)*, TI Application Report SLVA372D.**

- Папка: `02_basic_boost_pfc/TI_SLVA372_Basic_Calculation_Boost_Power_Stage/`, 10 стр.
- Применение: ОПОРНЫЙ источник базовых формул: D, ΔI_L, I_rms, условие CCM. Указан в ТЗ как методика расчёта пульсаций.
- Ключевые слова: boost, коэффициент заполнения, пульсации тока, CCM, базовые формулы

---

## Проектирование дросселя: потери, зазор, обмотка

Папка: `articles/03_inductor_design/`

**1. T. Ewald, J. Biela, *Frequency-Dependent Inductance and Winding Loss Model for Gapped Foil Inductors*, IEEE Transactions on Power Electronics (TPEL), 2022. DOI: [10.1109/TPEL.2022.3169620](https://doi.org/10.1109/TPEL.2022.3169620)**

- Папка: `03_inductor_design/Ewald_Biela_2022_Gapped_Foil_Inductors/`, 12 стр.
- Применение: Частотно-зависимые потери и индуктивность фольговой обмотки с учётом зазора и экранирования полем проводников. Фольга рассмотрена как альтернатива литцендрату.
- Ключевые слова: фольговая обмотка, частотная зависимость, экранирование

**2. T. Ewald, J. Biela, *Analytical Winding Loss and Inductance Models for Gapped Inductors With Litz or Solid Wires*, IEEE Transactions on Power Electronics (TPEL), 2022. DOI: [10.1109/TPEL.2022.3187155](https://doi.org/10.1109/TPEL.2022.3187155)**

- Папка: `03_inductor_design/Ewald_Biela_2022_Winding_Loss_Gapped_Litz_Solid/`, 14 стр.
- Применение: Потери в обмотке и индуктивность при дискретном воздушном зазоре — влияние поля зазора на ближние витки.
- Ключевые слова: потери в обмотке, воздушный зазор, литцендрат, индуктивность

**3. H. Liao, J.-F. Chen, *Design process of high-frequency inductor with multiple air-gaps in the dimensional limitation*, The Journal of Engineering (IET), 2022. DOI: [10.1049/tje2.12087](https://doi.org/10.1049/tje2.12087)**

- Папка: `03_inductor_design/Liao_Chen_2022_Multiple_Air_Gaps/`, 18 стр.
- Применение: ОПОРНЫЙ источник магнитной цепи и выпучивания. Сопротивление физического зазора задано через A_g; A_e появляется только после частного допущения A_g=A_e. Для отдельного стержня формулу обобщать через фактическую A_g каждого зазора. Разделение зазора требует повторного расчёта F_f каждого участка.
- Ключевые слова: коэффициент выпучивания, краевой поток, воздушный зазор, разделение зазора
- Примечание: Файл 'The Journal of Engineering - 2021 - Liao - ...' в 0_references — побайтовый дубликат этого же PDF (обнаружено при миграции).

**4. Q. Meng, J. Biela, *Analytical Models for HF-Losses of Litz Wire in Inductors With Arbitrary Winding and Gap Arrangements*, IEEE Open Journal of Power Electronics (OJPEL), 2025. DOI: [10.1109/OJPEL.2025.3604564](https://doi.org/10.1109/OJPEL.2025.3604564)**

- Папка: `03_inductor_design/Meng_Biela_2025_HF_Losses_Litz_Arbitrary_Gap/`, 14 стр.
- Применение: Вихревые потери литцендрата при произвольном расположении обмотки и зазоров; содержит независимый контроль расчёта по МКЭ.
- Ключевые слова: вихревые потери, литцендрат, произвольное расположение, МКЭ

**5. J. Mühlethaler, J. Biela, J. W. Kolar, *Improved Core-Loss Calculation for Magnetic Components Employed in Power Electronic Systems*, IEEE APEC, 2011. DOI: [10.1109/APEC.2011.5744829](https://doi.org/10.1109/APEC.2011.5744829)**

- Папка: `03_inductor_design/Muehlethaler_Biela_Kolar_2011_Improved_Core_Loss_iGSE/`, 9 стр.
- Применение: ПЕРВИЧНЫЙ источник iGSE. Коэффициент k_i брать по ур. (3) с множителем (2π)^(α−1), интегралом 0…2π и 2^(β−α); эквивалентную B(t) нормировать по A_e. Указывает ограничения на интервалах постоянной индукции и при магнитной релаксации.
- Ключевые слова: iGSE, потери в сердечнике, Штейнмец, несинусоидальная индукция

**6. H. Pichon et al., *Accurate Efficiency and Power Densities Optimization of Output Inductor of Buck Derived Converters*, Applied Sciences (MDPI), 2022. DOI: [10.3390/app12189330](https://doi.org/10.3390/app12189330)**

- Папка: `03_inductor_design/Pichon_2022_Efficiency_PowerDensity_Output_Inductor/`, 31 стр.
- Применение: Многокритериальная оптимизация КПД, объёмной плотности мощности и геометрии дросселя.
- Ключевые слова: оптимизация КПД, плотность мощности, геометрия дросселя

**7. B. N. Sanusi et al., *Investigation and Modeling of DC Bias Impact on Core Losses at High Frequency*, IEEE Transactions on Power Electronics (TPEL), 2023. DOI: [10.1109/TPEL.2023.3249106](https://doi.org/10.1109/TPEL.2023.3249106)**

- Папка: `03_inductor_design/Sanusi_2023_DC_Bias_Impact_Core_Losses/`, 17 стр.
- Применение: КРИТИЧНО: показывает неприменимость модели потерь без идентификации при постоянном подмагничивании. Для дросселя boost с большим I_dc — ограничение точности iGSE.
- Ключевые слова: постоянное подмагничивание, DC bias, потери в сердечнике, ограничение модели

**8. M. Schäfer, D. Bortis, J. W. Kolar, *Optimal Design of Highly Efficient and Highly Compact PCB Winding Inductors*, IEEE IPEC (ECCE Asia), 2018. DOI: [10.23919/IPEC.2018.8507558](https://doi.org/10.23919/IPEC.2018.8507558)**

- Папка: `03_inductor_design/Schaefer_Bortis_Kolar_2018_PCB_Winding_Inductors/`, 9 стр.
- Применение: Потери печатной обмотки, влияние положения зазора, поверхностного эффекта и эффекта близости.
- Ключевые слова: печатная обмотка, положение зазора, эффект близости

---

## Литцендрат

Папка: `articles/04_litz_wire/`

**1. C. R. Sullivan, R. Y. Zhang, *Simplified Design Method for Litz Wire*, IEEE APEC, 2014. DOI: [10.1109/APEC.2014.6803671](https://doi.org/10.1109/APEC.2014.6803671)**

- Папка: `04_litz_wire/Sullivan_Zhang_2014_Simplified_Litz_Design/`, 8 стр.
- Применение: ОПОРНЫЙ источник расчёта литцендрата: выбор диаметра и числа жил по глубине проникновения, ширине секции и числу витков; проверка F_R = R_ac/R_dc.
- Ключевые слова: литцендрат, F_R, глубина проникновения, число жил, выбор провода

---

## ЭМС, паразитные ёмкости, собственный резонанс

Папка: `articles/05_emc/`

**1. M. L. Heldwein, J. W. Kolar, *Winding Capacitance Cancellation for Three-Phase EMC Input Filters*, IEEE Transactions on Power Electronics (TPEL), 2008. DOI: [10.1109/TPEL.2008.924820](https://doi.org/10.1109/TPEL.2008.924820)**

- Папка: `05_emc/Heldwein_Kolar_2008_Winding_Capacitance_Cancellation/`, 13 стр.
- Применение: Влияние паразитной ёмкости на высокочастотный импеданс и конструктивное управление ёмкостными связями.
- Ключевые слова: паразитная ёмкость, ЭМС-фильтр, трёхфазный, импеданс

**2. N. Jia et al., *Mitigating EMI Noise in Propagation Paths: Review of Parasitic and Coupling Effects in Power Electronic Packages, Filters, and Systems*, IEEE Open Journal of Power Electronics (OJPEL), 2024. DOI: [10.1109/OJPEL.2024.3357832](https://doi.org/10.1109/OJPEL.2024.3357832)**

- Папка: `05_emc/Jia_2024_Mitigating_EMI_Propagation_Paths_Review/`, 17 стр.
- Применение: Обзор путей распространения синфазных и дифференциальных помех; контроль паразитных связей.
- Ключевые слова: ЭМС, синфазная помеха, дифференциальная помеха, паразитные связи, обзор

**3. H. Zhao et al., *Parasitic Capacitance Modeling of Copper-Foiled Medium-Voltage Filter Inductors Considering Fringe Electrical Field*, IEEE Transactions on Power Electronics (TPEL), 2021. DOI: [10.1109/TPEL.2020.3048226](https://doi.org/10.1109/TPEL.2020.3048226)**

- Папка: `05_emc/Zhao_2021_Parasitic_Capacitance_Foil_Inductors_Fringe/`, 13 стр.
- Применение: Паразитные ёмкости, электрическое краевое поле и собственный резонанс обмотки — основа проверки k_f = f_res/f_треб,max; k_R оставлен для отношения магнитных сопротивлений.
- Ключевые слова: собственная ёмкость, краевое электрическое поле, собственный резонанс

---

## Отечественные учебные пособия и методики

Папка: `articles/06_textbooks_ru/`

**1. Легостаев Н. С., *Материалы и элементы электронной техники (МЭЭУ). Учебно-методическое пособие*, ТУСУР.**  ⚠ запись не выверена

- Папка: `06_textbooks_ru/Legostaev_MEEU_uchebno_metodicheskoe_posobie/`, 146 стр.
- Применение: Отечественная терминология и нормативный подход к расчёту магнитных элементов; согласование обозначений в отчёте по ГОСТ.
- Ключевые слова: учебное пособие, магнитные элементы, терминология, ГОСТ

**2. Легостаев Н. С., *Материалы и элементы электронной техники. Пособие*, ТУСУР.**  ⚠ запись не выверена  ⚠ неполно: часть страниц без текста

- Папка: `06_textbooks_ru/Legostaev_NS_MEEU_posobie/`, 186 стр.
- Применение: Дополнение к основному пособию Легостаева.
- Ключевые слова: учебное пособие, магнитные материалы

**3. Обрусник В. П., *Магнитные элементы электронных устройств. Руководство*, ТУСУР, 2019.**  ⚠ запись не выверена

- Папка: `06_textbooks_ru/Obrusnik_MEEU_rukovodstvo_2019/`, 61 стр.
- Применение: Практическое руководство к расчёту; примеры и порядок оформления.
- Ключевые слова: магнитные элементы, руководство, примеры расчёта

**4. Обрусник В. П., *Магнитные элементы электронных устройств. Учебное пособие*, ТУСУР, 2018.**  ⚠ запись не выверена

- Папка: `06_textbooks_ru/Obrusnik_VP_MEEU_posobie_2018/`, 154 стр.
- Применение: Расчёт магнитных элементов по отечественной методике: произведение площадей, коэффициент заполнения окна.
- Ключевые слова: магнитные элементы, произведение площадей, коэффициент заполнения

---
