# Журнал проверки источников

**Промежуточная редакция: литературная проверка не завершена.**

89 позиций: 24 текста доступны локально, 65 не получены. Для 14 позиций прочитан текст с ограничениями, 10 доступных материалов ещё не прочитаны полностью. Наличие текстового слоя не подтверждает проверку всех рисунков и формул.

Полные тексты сторонних публикаций не включены: права на публичное распространение не проверены. Ссылки ведут к источникам; доступность не гарантирована.

## [1] Texas Instruments. Magnetics Design 4 - Power Transformer Design
- Источник: https://www.ti.com/lit/ml/slup126/slup126.pdf
- Получение: existing_fulltext
- Чтение: Прочитан извлечённый текст всех 13 страниц; графики и повреждённые формулы не проверены по изображениям.
- Выводы и ограничения: TI отделяет передающий трансформатор от flyback. Нужны проверка пуска при максимальных VIN и duty, различение частоты переключения и периода магнитного цикла, потери/температура в реальном монтаже. Правила распределения потерь, заполнения окна и температуры в апноте не являются нормами космического изделия. Раздел 4-8 прямо оговаривает, что специальные проблемы planar вне охвата. Пример 4-10—4-11 не переносится как готовый PCB-дизайн.

## [2] Texas Instruments. Magnetics Design 3 - Windings
- Источник: https://www.ti.com/lit/ml/slup125/slup125.pdf
- Получение: existing_fulltext
- Чтение: Файл доступен, полное содержательное чтение в этой редакции не завершено.

## [3] Texas Instruments. Magnetics Design 2 - Magnetic Core Characteristics
- Источник: https://www.ti.com/lit/ml/slup124/slup124.pdf
- Получение: existing_fulltext
- Чтение: Файл доступен, полное содержательное чтение в этой редакции не завершено.

## [4] Texas Instruments. Magnetics Design 5 - Inductor and Flyback Transformer Design
- Источник: https://www.ti.com/lit/ml/slup127/slup127.pdf
- Получение: existing_fulltext
- Чтение: Файл доступен, полное содержательное чтение в этой редакции не завершено.

## [5] Würth Elektronik. ANP151a — Mastering Galvanic Isolation: Ensuring Safety in High-Power Electronics
- Источник: https://www.we-online.com/components/media/o896744v410%20ANP151_EN.pdf
- Получение: existing_fulltext
- Чтение: Файл доступен, полное содержательное чтение в этой редакции не завершено.

## [6] Copper Layers - Eurocircuits
- Источник: https://www.eurocircuits.com/technical-guidelines/pcb-design-guidelines/copper-layers/
- Получение: existing_fulltext
- Чтение: Прочитан весь сохранённый текст веб-страницы.
- Выводы и ограничения: Gerber: flashes для площадок, полигоны вместо отрисовки мелкими линиями; обязательный порядок слоёв; нормы также для меди одной цепи. Производитель может заменить неподходящий hatch сплошной заливкой — для магнитики такое изменение опасно. Заводские размеры не универсальны.

## [7] Drilled Holes - Eurocircuits
- Источник: https://www.eurocircuits.com/technical-guidelines/pcb-design-guidelines/drilled-holes/
- Получение: existing_fulltext
- Чтение: Прочитан весь сохранённый текст веб-страницы.
- Выводы и ограничения: ENDSIZES отличаются от TOOLSIZE; PTH и NPTH лучше выдавать раздельно. Автоклассификация мелких отверстий как via допускает уменьшение готового размера. Для расчётных силовых переходов запретить несогласованные изменения и запросить PPA. Перекрывающиеся сверления не заменяют фрезерованный паз.

## [8] Track Width and Isolation Gap Tolerances - Eurocircuits
- Источник: https://www.eurocircuits.com/pcb-design-guidelines/track-width-and-isolation-gap-tolerances/
- Получение: existing_fulltext
- Чтение: Прочитан весь сохранённый текст веб-страницы.
- Выводы и ограничения: Травление идёт вниз и вбок; ширина основания отличается от верха. Толстая медь требует более грубого рисунка. Производитель применяет собственную CAM-компенсацию. Указанные им проценты со ссылкой на IPC не равны прямой проверке нормативного текста.

## [9] Tolerances on Copper Thickness - Eurocircuits
- Источник: https://www.eurocircuits.com/technical-guidelines/understanding-manufacturing-tolerances-on-a-pcb/tolerances-on-copper-thickness/
- Получение: existing_fulltext
- Чтение: Прочитан весь сохранённый текст веб-страницы.
- Выводы и ограничения: Start copper, nominal end copper и гарантированный минимум — разные величины. Внутренний print-and-etch уменьшает толщину, наружная гальваника добавляет её неравномерно. В записи сайта +/- означает приблизительно, не математический допуск. Поэтому в модели нужна гарантированная готовая медь и микрошлиф.

## [10] Layer to Layer Registration Tolerances - Eurocircuits
- Источник: https://www.eurocircuits.com/technical-guidelines/understanding-manufacturing-tolerances-on-a-pcb/layer-to-layer-registration-tolerances/
- Получение: existing_fulltext
- Чтение: Прочитан весь сохранённый текст веб-страницы.
- Выводы и ограничения: Совмещение включает core-core, рисунок-сверление и наружный-внутренний слой. DI уменьшает, но не устраняет погрешности. Нельзя объявить единый численный допуск по этой описательной странице.

## [11] Finished PCB Thickness Tolerance - Eurocircuits
- Источник: https://www.eurocircuits.com/technical-guidelines/understanding-manufacturing-tolerances-on-a-pcb/finished-pcb-thickness-tolerances/
- Получение: existing_fulltext
- Чтение: Прочитан весь сохранённый текст веб-страницы.
- Выводы и ограничения: Толщина заказа/материального пакета не всегда включает наружную гальванику, покрытие, маску и маркировку. Геометрия окна должна учитывать полный физический габарит без двойного счёта.

## [12] Copper Distribution on a Panel - Eurocircuits
- Источник: https://www.eurocircuits.com/technical-guidelines/panel-guidelines/copper-distribution-on-a-panel/
- Получение: existing_fulltext
- Чтение: Прочитан весь сохранённый текст веб-страницы.
- Выводы и ограничения: Равномерная медь уменьшает коробление и улучшает металлизацию. Предложение добавлять медь применимо к обычной панели, но требует электромагнитного ограничения в зоне обмотки.

## [13] Magnetics - Ferrite Core Inductor Design
- Источник: https://www.mag-inc.com/Design/Design-Guides/Inductor-Design-with-Magnetics-Ferrite-Cores.aspx
- Получение: existing_fulltext
- Чтение: Прочитан весь сохранённый текст; изображения формул и графики не проверены.
- Выводы и ограничения: Предварительный выбор феррита по LI² построен при заданных заполнении окна и сечении на ампер. Это не универсальная PCB-методика. LI² на диаграмме — параметр отбора, физическая энергия линейного дросселя LI²/2.

## [14] Magnetics - Ferrite Core Transformer Design
- Источник: https://www.mag-inc.com/Design/Design-Guides/Transformer-Design-with-Magnetics-Ferrite-Cores.aspx
- Получение: existing_fulltext
- Чтение: Прочитан весь сохранённый текст; изображения формул и графики не проверены.
- Выводы и ограничения: Выбор трансформатора зависит от топологии, частоты, B и нагрева; коэффициенты area-product завязаны на допущения. Не переносить типовое заполнение окна и плотность тока на печатный стек.

## [15] WE-PLN Planar Transformers | Passive Components | Würth Elektronik Product Catalog
- Источник: https://www.we-online.com/en/components/products/WE-PLN
- Получение: existing_fulltext
- Чтение: Файл доступен, полное содержательное чтение в этой редакции не завершено.

## [16] Würth Elektronik. WE-PLN 750341134 — Datasheet
- Источник: https://www.we-online.com/components/products/datasheet/750341134.pdf
- Получение: existing_fulltext
- Чтение: Файл доступен, полное содержательное чтение в этой редакции не завершено.

## [17] Products-Ferroxcube
- Источник: https://www.ferroxcube.com/en-global/products_ferroxcube/detail/shape_cores_accessories/planar_e_cores
- Получение: existing_fulltext
- Чтение: Прочитан сохранённый текст одной страницы каталога, не весь динамический каталог.
- Выводы и ограничения: Есть разные материалы и исполнения gap/AL даже одного геометрического семейства. Страница каталога — не апнот и не подтверждение конструкции; полный каталог не считался прочитанным.

## [18] Design and analysis of planar integrated L-C-T components for converters
- Источник: https://doi.org/10.1109/63.892837
- Получение: fulltext_unavailable
- Чтение: Полный текст не получен; чтение невозможно по имеющимся данным.

## [19] New method for integration of resonant inductor and transformer-design, realisation, measurements
- Источник: https://doi.org/10.1109/apec.1999.750516
- Получение: fulltext_unavailable
- Чтение: Полный текст не получен; чтение невозможно по имеющимся данным.

## [20] Electromagnetic integration of high power resonant circuits comprising high leakage inductance transformers
- Источник: https://doi.org/10.1109/pesc.2004.1354802
- Получение: fulltext_unavailable
- Чтение: Полный текст не получен; чтение невозможно по имеющимся данным.

## [21] Energy based capacitance model for magnetic devices
- Источник: https://doi.org/10.1109/apec.2001.911635
- Получение: fulltext_unavailable
- Чтение: Полный текст не получен; чтение невозможно по имеющимся данным.

## [22] Optimal air-gap design in high-frequency foil windings
- Источник: https://doi.org/10.1109/63.712317
- Получение: fulltext_unavailable
- Чтение: Полный текст не получен; чтение невозможно по имеющимся данным.

## [23] Elimination of Leakage Effects Related to the Use of Windings with Fractions of Turns
- Источник: https://doi.org/10.1109/tpel.1986.4766275
- Получение: fulltext_unavailable
- Чтение: Полный текст не получен; чтение невозможно по имеющимся данным.

## [24] Experimental determination of stray capacitances in high frequency transformers
- Источник: https://doi.org/10.1109/tpel.2003.816186
- Получение: fulltext_unavailable
- Чтение: Полный текст не получен; чтение невозможно по имеющимся данным.

## [25] A novel approach for minimizing high-frequency transformer copper losses
- Источник: https://doi.org/10.1109/63.17944
- Получение: fulltext_unavailable
- Чтение: Полный текст не получен; чтение невозможно по имеющимся данным.

## [26] Multiple Layer Series Connected Winding Design for Minimum Losses
- Источник: https://doi.org/10.1109/tpas.1979.319520
- Получение: fulltext_unavailable
- Чтение: Полный текст не получен; чтение невозможно по имеющимся данным.

## [27] Effects of eddy currents in transformer windings
- Источник: https://doi.org/10.1049/piee.1966.0236
- Получение: fulltext_unavailable
- Чтение: Полный текст не получен; чтение невозможно по имеющимся данным.

## [28] Optimal Design and Tradeoff Analysis of Planar Transformer in High-Power DC–DC Converters
- Источник: https://doi.org/10.1109/tie.2010.2046005
- Получение: fulltext_unavailable
- Чтение: Полный текст не получен; чтение невозможно по имеющимся данным.

## [29] Optimizing the AC resistance of multilayer transformer windings with arbitrary current waveforms
- Источник: https://doi.org/10.1109/63.838110
- Получение: fulltext_unavailable
- Чтение: Полный текст не получен; чтение невозможно по имеющимся данным.

## [30] Improved analytical modeling of conductive losses in magnetic components
- Источник: https://doi.org/10.1109/63.285503
- Получение: fulltext_unavailable
- Чтение: Полный текст не получен; чтение невозможно по имеющимся данным.

## [31] Model and design of PCB parallel winding for planar transformer
- Источник: https://doi.org/10.1109/tmag.2003.816147
- Получение: fulltext_unavailable
- Чтение: Полный текст не получен; чтение невозможно по имеющимся данным.

## [32] A study of volume and weight vs. frequency for high-frequency transformers
- Источник: https://doi.org/10.1109/pesc.1993.472059
- Получение: fulltext_unavailable
- Чтение: Полный текст не получен; чтение невозможно по имеющимся данным.

## [33] Current Sharing Between Parallel Turns of a Planar Transformer: Prediction and Improvement Using a Circuit Simulation Software
- Источник: https://doi.org/10.1109/07ias.2007.273
- Получение: fulltext_unavailable
- Чтение: Полный текст не получен; чтение невозможно по имеющимся данным.

## [34] Using parallel windings in planar magnetic components
- Источник: https://doi.org/10.1109/pesc.2001.954423
- Получение: fulltext_unavailable
- Чтение: Полный текст не получен; чтение невозможно по имеющимся данным.

## [35] Selection of the appropriate winding setup in planar inductors with parallel windings
- Источник: https://doi.org/10.1109/ecce.2010.5618404
- Получение: downloaded_unreviewed
- Чтение: Прочитан извлечённый текст всех 6 страниц. Часть формул/чисел разрушена раскладкой колонок, не использована как точная транскрипция.
- Адрес полного текста: https://oa.upm.es/7818/2/INVE_MEM_2010_79225.pdf
- Выводы и ограничения: При несимметричном зазоре равные DC-ветви и полное interleaving могут давать разные амплитуды и фазы. Авторы извлекают матрицу независимых слоёв и затем перебирают соединения; изменение геометрии требует новой матрицы. Равенство токов и минимум потерь — разные цели. Включён общий матричный вывод, проверенный независимо.

## [36] Opportunities and Challenges in Very High Frequency Power Conversion
- Источник: https://doi.org/10.1109/apec.2009.4802625
- Получение: fulltext_unavailable
- Чтение: Полный текст не получен; чтение невозможно по имеющимся данным.

## [37] Calculation of leakage inductance in transformer windings
- Источник: https://doi.org/10.1109/63.285502
- Получение: fulltext_unavailable
- Чтение: Полный текст не получен; чтение невозможно по имеющимся данным.

## [38] The analysis and comparison of leakage inductance in different winding arrangements for planar transformer
- Источник: https://doi.org/10.1109/peds.2009.5385844
- Получение: fulltext_unavailable
- Чтение: Полный текст не получен; чтение невозможно по имеющимся данным.

## [39] The low leakage inductance of planar transformers; fact or myth?
- Источник: https://doi.org/10.1109/apec.2001.912515
- Получение: fulltext_unavailable
- Чтение: Полный текст не получен; чтение невозможно по имеющимся данным.

## [40] Leakage inductance calculation for planar transformers with a magnetic shunt
- Источник: https://doi.org/10.1109/ecce.2013.6646762
- Получение: fulltext_unavailable
- Чтение: Полный текст не получен; чтение невозможно по имеющимся данным.

## [41] Planar inductor
- Источник: https://doi.org/10.1109/tmag.1984.1063271
- Получение: fulltext_unavailable
- Чтение: Полный текст не получен; чтение невозможно по имеющимся данным.

## [42] Planar transformer technology applied to AC/DC conversion
- Источник: https://doi.org/10.1109/intlec.1999.794113
- Получение: fulltext_unavailable
- Чтение: Полный текст не получен; чтение невозможно по имеющимся данным.

## [43] Transformers and Inductors for Power Electronics
- Источник: https://doi.org/10.1002/9781118544648
- Получение: fulltext_unavailable
- Чтение: Полный текст не получен; чтение невозможно по имеющимся данным.

## [44] A review of planar magnetic techniques and technologies
- Источник: https://doi.org/10.1109/apec.2001.912514
- Получение: fulltext_unavailable
- Чтение: Полный текст не получен; чтение невозможно по имеющимся данным.

## [45] Improving the thermal management of AC-DC converters using integration technologies
- Источник: https://doi.org/10.1109/ias.2004.1348798
- Получение: fulltext_unavailable
- Чтение: Полный текст не получен; чтение невозможно по имеющимся данным.

## [46] Embedded passives integrated circuits for power converters
- Источник: https://doi.org/10.1109/psec.2002.1023840
- Получение: fulltext_unavailable
- Чтение: Полный текст не получен; чтение невозможно по имеющимся данным.

## [47] Fabrication method for a winding assembly with a large number of planar layers
- Источник: https://doi.org/10.1109/63.208500
- Получение: fulltext_unavailable
- Чтение: Полный текст не получен; чтение невозможно по имеющимся данным.

## [48] PCB integrated inductors for low power DC/DC converter
- Источник: https://doi.org/10.1109/tpel.2003.813757
- Получение: fulltext_unavailable
- Чтение: Полный текст не получен; чтение невозможно по имеющимся данным.

## [49] Design Method and Material Technologies for Passives in Printed Circuit Board Embedded Circuits
- Источник: https://doi.org/10.1109/tpel.2005.846530
- Получение: fulltext_unavailable
- Чтение: Полный текст не получен; чтение невозможно по имеющимся данным.

## [50] Analysis of planar sandwich inductors by current images
- Источник: https://doi.org/10.1109/20.104901
- Получение: fulltext_unavailable
- Чтение: Полный текст не получен; чтение невозможно по имеющимся данным.

## [51] Effect of finite thickness of magnetic substrate on planar inductors
- Источник: https://doi.org/10.1109/20.50553
- Получение: fulltext_unavailable
- Чтение: Полный текст не получен; чтение невозможно по имеющимся данным.

## [52] Planar inductor with ferrite layers for DC-DC converter
- Источник: https://doi.org/10.1109/tmag.2003.812708
- Получение: fulltext_unavailable
- Чтение: Полный текст не получен; чтение невозможно по имеющимся данным.

## [53] Improved analytical modeling of conductive losses in gapped high-frequency inductors
- Источник: https://doi.org/10.1109/28.936395
- Получение: fulltext_unavailable
- Чтение: Полный текст не получен; чтение невозможно по имеющимся данным.

## [54] Toward the Next Level of PCB Usage in Power Electronic Converters
- Источник: https://doi.org/10.1109/tpel.2008.2004276
- Получение: downloaded_unreviewed
- Чтение: Прочитан извлечённый текст всех 13 страниц; таблицы/рисунки с отсутствующим текстовым слоем не визуально верифицированы.
- Адрес полного текста: https://repository.tudelft.nl/file/File_6faca9df-0d53-4d9d-9f87-53ac4ec4cfe7
- Выводы и ограничения: Rigid-flex позволяет не увеличивать число слоёв всей платы ради трансформатора. Важно учитывать раскрой, инверсию artwork, радиус и наложение сгибов. Стоимостные коэффициенты авторов условные и устаревшие, не цены. В разделе IV отмечены микротрещины на сгибах и разрыв microvia у шва. Измерение внутренних температур выполнялось термопарами вместе с IR. Полезно для производственного раздела; не доказывает квалификацию космического исполнения.

## [55] A Coupled Electrothermal Model for Planar Transformer Temperature Distribution Computation
- Источник: https://doi.org/10.1109/tie.2008.2003102
- Получение: fulltext_unavailable
- Чтение: Полный текст не получен; чтение невозможно по имеющимся данным.

## [56] Fabrication and modeling of a planar magnetic structure with directly etched windings
- Источник: https://doi.org/10.1109/ecce.2009.5316202
- Получение: fulltext_unavailable
- Чтение: Полный текст не получен; чтение невозможно по имеющимся данным.

## [57] Magnetic Component Model for Planar Structures Based on Transmission Lines
- Источник: https://doi.org/10.1109/tie.2009.2032434
- Получение: fulltext_unavailable
- Чтение: Полный текст не получен; чтение невозможно по имеющимся данным.

## [58] Planar LTCC Transformers for High-Voltage Flyback Converters
- Источник: https://doi.org/10.1109/tcapt.2009.2031872
- Получение: fulltext_unavailable
- Чтение: Полный текст не получен; чтение невозможно по имеющимся данным.

## [59] Printed Spiral Winding Inductor With Wide Frequency Bandwidth
- Источник: https://doi.org/10.1109/tpel.2010.2076318
- Получение: fulltext_unavailable
- Чтение: Полный текст не получен; чтение невозможно по имеющимся данным.

## [60] Using Transformer Parasitics for Resonant Converters—A Review of the Calculation of the Stray Capacitance of Transformers
- Источник: https://doi.org/10.1109/tia.2007.912722
- Получение: fulltext_unavailable
- Чтение: Полный текст не получен; чтение невозможно по имеющимся данным.

## [61] Design, Modeling, and Analysis of a Compact Planar Transformer
- Источник: https://doi.org/10.1109/tmag.2012.2202642
- Получение: fulltext_unavailable
- Чтение: Полный текст не получен; чтение невозможно по имеющимся данным.

## [62] Improving the Characteristics of Integrated EMI Filters by Embedded Conductive Layers
- Источник: https://doi.org/10.1109/tpel.2005.846526
- Получение: fulltext_unavailable
- Чтение: Полный текст не получен; чтение невозможно по имеющимся данным.

## [63] Applying Response Surface Methodology to Small Planar Transformer Winding Design
- Источник: https://doi.org/10.1109/tie.2012.2187416
- Получение: fulltext_unavailable
- Чтение: Полный текст не получен; чтение невозможно по имеющимся данным.

## [64] Characterizations of High Frequency Planar Transformer With a Novel Comb-Shaped Shield
- Источник: https://doi.org/10.1109/tmag.2011.2157664
- Получение: fulltext_unavailable
- Чтение: Полный текст не получен; чтение невозможно по имеющимся данным.

## [65] Planar magnetic component technology-a review
- Источник: https://doi.org/10.1109/33.180055
- Получение: fulltext_unavailable
- Чтение: Полный текст не получен; чтение невозможно по имеющимся данным.

## [66] Self-Capacitance of High-Voltage Transformers
- Источник: https://doi.org/10.1109/tpel.2007.904252
- Получение: fulltext_unavailable
- Чтение: Полный текст не получен; чтение невозможно по имеющимся данным.

## [67] Modelling and design of high frequency planar transformers
- Источник: https://doi.org/10.1109/pesc.1995.474888
- Получение: fulltext_unavailable
- Чтение: Полный текст не получен; чтение невозможно по имеющимся данным.

## [68] Design of a high-frequency planar power transformer in multilayer technology
- Источник: https://doi.org/10.1109/41.88907
- Получение: fulltext_unavailable
- Чтение: Полный текст не получен; чтение невозможно по имеющимся данным.

## [69] A low-profile power converter using printed-circuit board (PCB) power transformer with ferrite polymer composite
- Источник: https://doi.org/10.1109/63.931055
- Получение: fulltext_unavailable
- Чтение: Полный текст не получен; чтение невозможно по имеющимся данным.

## [70] Air-gap effects in inductive energy transfer
- Источник: https://doi.org/10.1109/pesc.2008.4592594
- Получение: fulltext_unavailable
- Чтение: Полный текст не получен; чтение невозможно по имеющимся данным.

## [71] Airgap fringing flux reduction in inductors using open-circuit copper screens
- Источник: https://doi.org/10.1049/ip-epa:20045234
- Получение: fulltext_unavailable
- Чтение: Полный текст не получен; чтение невозможно по имеющимся данным.

## [72] Orthogonal Winding Structures and Design for Planar Integrated Magnetics
- Источник: https://doi.org/10.1109/tie.2007.909754
- Получение: fulltext_unavailable
- Чтение: Полный текст не получен; чтение невозможно по имеющимся данным.

## [73] Analysis and Design of Fully Integrated Planar Magnetics for Primary–Parallel Isolated Boost Converter
- Источник: https://doi.org/10.1109/tie.2012.2186777
- Получение: fulltext_unavailable
- Чтение: Полный текст не получен; чтение невозможно по имеющимся данным.

## [74] Winding loss mechanism analysis and design for new structure high-frequency gapped inductor
- Источник: https://doi.org/10.1109/tmag.2005.854991
- Получение: fulltext_unavailable
- Чтение: Полный текст не получен; чтение невозможно по имеющимся данным.

## [75] The influence of air gap size and winding position on the proximity losses in high frequency transformers
- Источник: https://doi.org/10.1109/pesc.2001.954329
- Получение: fulltext_unavailable
- Чтение: Полный текст не получен; чтение невозможно по имеющимся данным.

## [76] High-Frequency Fringing Fields Loss in Thick Rectangular and Round Wire Windings
- Источник: https://doi.org/10.1109/tmag.2008.2002302
- Получение: fulltext_unavailable
- Чтение: Полный текст не получен; чтение невозможно по имеющимся данным.

## [77] Fringing Field Formulas and Winding Loss Due to an Air Gap
- Источник: https://doi.org/10.1109/tmag.2007.898908
- Получение: fulltext_unavailable
- Чтение: Полный текст не получен; чтение невозможно по имеющимся данным.

## [78] Overview of Planar Magnetic Technology—Fundamental Properties
- Источник: https://doi.org/10.1109/tpel.2013.2283263
- Получение: fulltext_unavailable
- Чтение: Полный текст не получен; чтение невозможно по имеющимся данным.

## [79] Optimal Design of Highly Efficient and Highly Compact PCB Winding Inductors
- Источник: https://doi.org/10.1109/compel.2018.8460166
- Получение: existing_fulltext
- Чтение: Прочитан извлечённый текст всех 9 страниц, включая выводы и библиографию. Аналитические формулы с повреждённой выгрузкой не переписаны.
- Выводы и ограничения: Компенсация fringing против skin/proximity требует конкретной геометрии; прямой и круговой проводники различаются, DC-плотность в круговом витке неравномерна. При переносе на слои нужно dL << bw. Выводы должны быть копланарными для снижения потерь, through-hole предложены по стоимости. Это аналитико-FEM работа с предложенной реализацией, не серийная квалификация.

## [80] Frequency-Dependent Inductance and Winding Loss Model for Gapped Foil Inductors
- Источник: https://doi.org/10.1109/tpel.2022.3169620
- Получение: existing_fulltext
- Чтение: Файл доступен, полное содержательное чтение в этой редакции не завершено.

## [81] Analytical Fringing Field Model for Efficient Winding Loss Calculation in Gapped Foil Inductors
- Источник: https://doi.org/10.1109/tpel.2024.3368145
- Получение: fulltext_unavailable
- Чтение: Полный текст не получен; чтение невозможно по имеющимся данным.

## [82] Novel Highly Efficient/Compact Automotive PCB Winding Inductors Based on the Compensating Air-Gap Fringing Field Concept
- Источник: https://doi.org/10.1109/tpel.2020.2969295
- Получение: fulltext_unavailable
- Чтение: Полный текст не получен; чтение невозможно по имеющимся данным.

## [83] A comprehensive design approach for a three‐winding planar transformer
- Источник: https://doi.org/10.1049/pel2.12261
- Получение: fulltext_unavailable
- Чтение: Полный текст не получен; чтение невозможно по имеющимся данным.

## [84] Transformer and Inductor Design Handbook
- Источник: https://doi.org/10.1201/b10865
- Получение: fulltext_unavailable
- Чтение: Полный текст не получен; чтение невозможно по имеющимся данным.

## [85] I-core PCB Planar Inductor Design for High Frequency and High Power Converters
- Источник: https://doi.org/10.1109/itec53557.2022.9813880
- Получение: fulltext_unavailable
- Чтение: Полный текст не получен; чтение невозможно по имеющимся данным.

## [86] Study on PCB Based Litz Wire Applications for Air-Core Inductor and Planar Transformer
- Источник: https://doi.org/10.1109/icpes47639.2019.9105549
- Получение: fulltext_unavailable
- Чтение: Полный текст не получен; чтение невозможно по имеющимся данным.

## [87] Parasitic Capacitance Modeling of Copper-Foiled Medium-Voltage Filter Inductors Considering Fringe Electrical Field
- Источник: https://doi.org/10.1109/TPEL.2020.3048226
- Получение: existing_fulltext
- Чтение: Файл доступен, полное содержательное чтение в этой редакции не завершено.

## [88] В. П. Обрусник. Магнитные элементы электронных устройств. Учебное пособие. 2018
- Источник: ../../articles/06_textbooks_ru/Obrusnik_VP_MEEU_posobie_2018/metadata.json
- Получение: existing_fulltext
- Чтение: Файл доступен, полное содержательное чтение в этой редакции не завершено.

## [89] Н. С. Легостаев. Магнитные элементы электронных устройств. Учебное пособие. 2014
- Источник: ../../articles/06_textbooks_ru/Legostaev_NS_MEEU_posobie/metadata.json
- Получение: existing_fulltext
- Чтение: Файл доступен, полное содержательное чтение в этой редакции не завершено.
