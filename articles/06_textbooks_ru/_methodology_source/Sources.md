# Реестр источников для методики расчёта ВЧ дросселя

Файл фиксирует соответствие между локальными PDF, библиографическими записями
LaTeX-документа и темами методики. В основной текст включаются только
источники, для которых доступен полный текст в этой папке либо официальный
паспорт изготовителя.

| Поз. | Локальный файл | Библиографическая ссылка | Применение в методике |
|---:|---|---|---|
| 1 | `Papamanolis_2020_Minimal_Loss_Operation.pdf` | P. Papamanolis et al., *Minimum Loss Operation and Optimal Design of High-Frequency Inductors for Defined Core and Litz Wire*, IEEE OJPEL, 2020. DOI: https://doi.org/10.1109/OJPEL.2020.3027452 | Совместная оптимизация потерь в сердечнике и литцендрате, температурная обратная связь, выбор точки минимума потерь. |
| 2 | `Accurate Efficiency and Power Densities Optimization of Output Inductor of Buck Derived Converters.pdf` | H. Pichon et al., *Accurate Efficiency and Power Densities Optimization of Output Inductor of Buck Derived Converters*, Applied Sciences, 2022. DOI: https://doi.org/10.3390/app12189330 | Многокритериальная оптимизация КПД, объёмной плотности мощности и геометрии. |
| 3 | `Analytical winding loss and industance models for gapped inductors with Litz or solid wires.pdf` | T. Ewald, J. Biela, *Analytical Winding Loss and Inductance Models for Gapped Inductors With Litz or Solid Wires*, IEEE TPEL, 2022. DOI: https://doi.org/10.1109/TPEL.2022.3187155 | Потери в обмотке и индуктивность при дискретном воздушном зазоре. |
| 4 | `Analytical_Models_for_HF-Losses_of_Litz_Wire_in_Inductors_With_Arbitrary_Winding_and_Gap_Arrangements.pdf` | Q. Meng, J. Biela, *Analytical Models for HF-Losses of Litz Wire in Inductors With Arbitrary Winding and Gap Arrangements*, IEEE OJPEL, 2025. DOI: https://doi.org/10.1109/OJPEL.2025.3604564 | Вихревые потери литцендрата при произвольном расположении обмотки и зазоров; независимый контроль FEM. |
| 5 | `hkkr_Investigation_and_Modeling_of_DC_Bias_Impact_on_Core_Losses_at_High_Frequency.pdf` | B. N. Sanusi et al., *Investigation and Modeling of DC Bias Impact on Core Losses at High Frequency*, IEEE TPEL, 2023. DOI: https://doi.org/10.1109/TPEL.2023.3249106 | Неприменимость модели потерь без идентификации при постоянном подмагничивании. |
| 6 | `Liao_Chen_2022_Multiple_Air_Gaps.pdf` | H. Liao, J.-F. Chen, *Design Process of High-Frequency Inductor With Multiple Air-Gaps in the Dimensional Limitation*, The Journal of Engineering, 2022. DOI: https://doi.org/10.1049/tje2.12087 | Поправка на краевой поток, разделение зазора и конструктивные ограничения E-сердечника. |
| 7 | `Parasitic_Capacitance_Modeling_of_Copper_Foiled_Medium_Voltage_Filter_Inductors_Considering_Fringe_Electrical_Field.pdf` | H. Zhao et al., *Parasitic Capacitance Modeling of Copper-Foiled Medium-Voltage Filter Inductors Considering Fringe Electrical Field*, IEEE TPEL, 2021. DOI: https://doi.org/10.1109/TPEL.2020.3048226 | Паразитные ёмкости, электрическое краевое поле и собственный резонанс. |
| 8 | `Mitigating_EMI_Noise_in_Propagation_Paths_Review_of_Parasitic_and_Coupling_Effects_in_Power_Electronic_Packages_Filters_and_Systems.pdf` | N. Jia et al., *Mitigating EMI Noise in Propagation Paths: Review of Parasitic and Coupling Effects in Power Electronic Packages, Filters, and Systems*, IEEE OJPEL, 2024. DOI: https://doi.org/10.1109/OJPEL.2024.3357832 | Пути распространения синфазных и дифференциальных помех; контроль паразитных связей. |
| 9 | `Muehlethaler_Biela_Kolar_2011_Improved_Core_Loss.pdf` | J. Mühlethaler, J. Biela, J. W. Kolar, *Improved Core-Loss Calculation for Magnetic Components Employed in Power Electronic Systems*, APEC, 2011. DOI: https://doi.org/10.1109/APEC.2011.5744829 | Первичный источник формы iGSE; ограничение базовой модели при интервалах постоянной индукции и магнитной релаксации. |
| 10 | `Sullivan_Zhang_2014_Simplified_Litz_Design.pdf` | C. R. Sullivan, R. Y. Zhang, *Simplified Design Method for Litz Wire*, APEC, 2014. DOI: https://doi.org/10.1109/APEC.2014.6803671 | Выбор диаметра и числа жил литцендрата по глубине проникновения, ширине секции и числу витков; проверка \(R_\mathrm{AC}/R_\mathrm{DC}\). |
| 11 | `Schaefer_Bortis_Kolar_2018_PCB_Winding_Inductors.pdf` | M. Schäfer, D. Bortis, J. W. Kolar, *Optimal Design of Highly Efficient and Highly Compact PCB Winding Inductors*, IPEC, 2018. DOI: https://doi.org/10.23919/IPEC.2018.8507558 | Потери печатной обмотки, влияние положения зазора, поверхностного эффекта и эффекта близости. |
| 12 | `Ewald_Biela_2022_Gapped_Foil_Inductors.pdf` | T. Ewald, J. Biela, *Frequency-Dependent Inductance and Winding Loss Model for Gapped Foil Inductors*, IEEE TPEL, 2022. DOI: https://doi.org/10.1109/TPEL.2022.3169620 | Частотно-зависимые потери и индуктивность фольговой обмотки с учётом зазора и экранирования полем проводников. |
| 13 | `Heldwein_Kolar_2008_Winding_Capacitance_Cancellation.pdf` | M. L. Heldwein, J. W. Kolar, *Winding Capacitance Cancellation for Three-Phase EMC Input Filters*, IEEE TPEL, 2008. DOI: https://doi.org/10.1109/TPEL.2008.924820 | Влияние паразитной ёмкости на высокочастотный импеданс и конструктивное управление ёмкостными связями. |

## Найденные дополнительные источники

Следующие работы найдены в открытых каталогах, но пока не включены в основной
текст: их полный текст отсутствует в папке `references`, а происхождение
доступной сторонней копии должно быть подтверждено до использования как
источника формул.

| Работа | Проверенная карточка / доступ | Возможное применение |
|---|---|---|
| H. Li et al., *MagNet: An Open-Source Database for Data-Driven Magnetic Core Loss Modeling*, APEC 2022, DOI: https://doi.org/10.1109/APEC43599.2022.9773372 | Официальная карточка Princeton: https://collaborate.princeton.edu/en/publications/magnet-an-open-source-database-for-data-driven-magnetic-core-loss/ | Проверка модели потерь по экспериментальным волнам. Не заменяет паспортные либо собственные данные для N88 и потому не должна задавать коэффициенты модели. |
| C. R. Sullivan, *Optimal Choice for Number of Strands in a Litz-Wire Transformer Winding*, IEEE TPEL, 1999, DOI: https://doi.org/10.1109/63.750181 | Официальная карточка IEEE: https://ieeexplore.ieee.org/document/750181/ . Обнаружена PDF-копия на сайте Universidad de Buenos Aires: https://cms.fi.uba.ar/uploads/Sullivan_Optimal_choice_for_number_of_strands_in_a_litz_wire_transformer_winding_PELS_1999_26877be9ec.pdf | Уточнение оптимального сочетания диаметра и числа жил. До подтверждения правомерности копии и сохранения полного текста не используется как нормативный источник методики. |

## Необходимая редакционная проверка

Файлы `16_Minimal-Loss-Operation_ACCEPTED-VERSION_Papamanolis_OJ-PEL.pdf` и
`Papamanolis_2020_Minimal_Loss_Operation.pdf` имеют одинаковый размер и
являются дубликатами одной принятой версии статьи. Они сохранены без удаления,
поскольку удаление не требуется для расчёта.
