# Design guide PFC CCM boost converter

<!-- FORMULA-WARNING -->
> **Формулы в этом файле недостоверны.** Текстовый слой PDF теряет дробные черты, радикалы и группировку степеней; знак интеграла приходит как `Z` или `R`, знак суммы -- как `P`. Формул вырезано: **17**, читать их в `formulas/` (картинки 300 dpi, перечень в `formulas/INDEX.md`).
<!-- /FORMULA-WARNING -->

> Автоматически извлечено из `source.pdf` скриптом `parse_pdf.py`
> Движок: pymupdf. Страниц: 30 из 30.
> Дата извлечения: 2026-08-07 06:42 UTC

Текст не редактировался. Формулы и таблицы могут быть искажены —
при сомнении сверяться с исходным PDF.

---

## [стр. 1]

Application Note
1
Revision1.1, 2016-02-22




About this document
Scope and purpose
This document introduces a design methodology for a Power Factor Correction (PFC) Continuous
Conduction Mode (CCM) boost converter, including:
 Equations for design and power losses
 Selection guide of semiconductor devices and passive components
 Charts for CoolMOS™  optimum RDS(ON)  selection
 1200 W design example with calculated and experimental results.
 Schematics, layout and bill of material
Intended audience
This document is intended for design engineers who want to design CCM PFC boost converter.
Table of contents

Introduction ................................................................................................................................... 2
1

Power stage design ........................................................................................................................ 4
2

ICE3PCS01G PFC boost controller ................................................................................................ 17
3

Efficiency and power losses modeling ......................................................................................... 19
4

Experimental results .................................................................................................................... 20
5

Board design ................................................................................................................................ 23
6

References ................................................................................................................................... 27
7

Symbols used in formulas ............................................................................................................ 28
8

PFC boost converter design guide
1200 W design example
Sam Abdel-Rahman
Franz Stückler
Ken Siu

Application Note

## [стр. 2]

PFC  boost converter design guide
Application Note
2
Revision1.1, 2016-02-22
Design Note DN 2013-01
V1.0 January 2013

Introduction
1
Power Factor Correction (PFC) shapes the input current of the power supply to be in synchronization with
the mains voltage, in order to maximize the real power drawn from the mains. In a perfect PFC circuit, the
input current follows the input voltage as a pure resistor, without any input current harmonics. This
document is to introduce a design methodology for the CCM PFC Boost converter, including equations for
power losses estimation, selection guide of semiconductor devices and passive components, and a design
example with experimental results.
1.1
Boost topology
Although active PFC can be achieved by several topologies, the boost converter (Figure 1) is the most
popular topology used in PFC applications, for the following reasons:
 The line voltage varies from zero to some peak value typically 375 V; hence a step up converter is needed
to output a DC bus voltage of 380 V or more. For that reason the buck converter is eliminated, and the
buck-boost converter has high switch voltage stress (Vin+Vo), therefore it is also not the popular one.
 The boost converter has the filter inductor on the input side, which provides a smooth continuous input
current waveform as opposed to the discontinuous input current of the buck or buck-boost topology.
The continuous input current is much easier to filter, which is a major advantage of this design because
any additional filtering needed on the converter input will increase the cost and reduces the power
factor due to capacitive loading of the line.


Boost Key Waveforms

 𝑉𝑜
𝑉in
=
1
1 -D    (CCM operation)
Figure 1
 Structure and key waveforms of a boost converter
1.2
PFC modes of operation
The boost converter can operate in three modes: continuous conduction mode (CCM), discontinuous
conduction mode (DCM), and critical conduction mode (CrCM). Figure 2 shows modeled waveforms to
illustrate the inductor and input currents in the three operating modes, for the same exact voltage and
power conditions.
By comparing DCM among the others, DCM operation seems simpler than CrCM, since it may operate in
constant frequency operation; however DCM has the disadvantage that it has the highest peak current
compared to CrCM and also to CCM, without any performance advantage compared to CrCM. For that
reason, CrCM is a more common practice design than DCM, therefore, this document will exclude the DCM
design.
AC
PFC
Converter
DC/DC
Converter
Load
DC Bus
Vac
AC
L
D
Ro
Vac
Co
S
+
Vo
-
DC Bus
S
V_L
I_L
I_S
I_D
T=1/f
DT
Vin
Vin-Vo
I_Lmax
I_Lmin
I_Lmax
I_Lmax
I_Lmin

## [стр. 3]

PFC  boost converter design guide
Application Note
3
Revision1.1, 2016-02-22
Design Note DN 2013-01
V1.0 January 2013
CrCM may be considered a special case of CCM, where the operation is controlled to stay at the boundary
between CCM and DCM. CrCM usually uses constant on-time control; the line voltage is changing across the
60 Hz line cycle, the reset time for the boost inductor is varying, and the operating frequency will change as
well in order to maintain the boundary mode operation. CrCM dictates the controller to sense the inductor
current zero crossing in order to trigger the start of the next switching cycle.
The inductor current ripple (or the peak current) in CrCM is twice of the average value, which greatly
increases the MOSFET RMS currents and turn-off current. But since every switching cycle starts at zero
current, and usually with ZVS operation, turn-on loss of MOSFET is usually eliminated. Also, since the boost
rectifier diode turns off at zero current as well, reverse recovery losses and noise in the boost diode are
eliminated too, another major advantage of CrCM mode. Still, on the balance, the high input ripple current
and its impact on the input EMI filter tends to eliminate CrCM mode for high power designs unless
interleaved stages are used to reduce the input HF current ripple. A high efficiency design can be realized
that way, but at substantially higher cost. That discussion is beyond the scope of this application note.
The power stage equations and transfer functions for CrCM are the same as CCM. The main differences
relate to the current ripple profile and switching frequency, which affects RMS current and switching power
losses and filter design.
CCM operation requires a larger filter inductor compared to CrCM.  While the main design concerns for a
CrCM inductor are low HF core loss, low HF winding loss, and the stable value over the operating range (the
inductor is essentially part of the timing circuit), the CCM mode inductor takes a different approach. For the
CCM PFC, the full load inductor current ripple is typically designed to be 20-40% of the average input
current. This has several advantages:
 Peak current is lower, and the RMS current factor with a trapezoidal waveform is reduced compared to a
triangular waveform, reducing device conduction losses.
 Turn-off losses are lower due to switch off at much lower maximum current.
 The HF ripple current to be smoothed by the EMI filter is much lower in amplitude.
On the other side, CCM encounters the turn-on losses in the MOSFET, which can be exacerbated by the boost
rectifier reverse recovery loss due to reverse recovery charge, Qrr. For this reason, ultra-fast recovery diodes
or silicon carbide Schottky Diodes with extreme low Qrr are needed for CCM mode.
In conclusion, we can say that for low power applications, the CrCM boost has the advantages in power
saving and improving power density. This advantage may extend to medium power ranges, however at
some medium power level the low filtering ability and the high peak current starts to become severe
disadvantages. At this point the CCM boost starts being a better choice for high power applications.
Since this document is intended to support high power PFC applications, therefore a CCM PFC boost
converter has been chosen in the application note with detailed design discussions and design examples for
demonstration.

0
1
10 4
-

2
10 4
-

3
10 4
-

4
10 4
-

0
5
10
15
Iin t( )
IL t( )
t
Continuous Conduction Mode (CCM)

0
1 10 4
-

2 10 4
-

3 10 4
-

4 10 4
-

0
5
10
15
Iin t( )
IL t( )
t
Discontinuous Conduction Mode (DCM)

Figure 2
 PFC Inductor and input line current waveforms in the three different operating modes
0
1 10 4
-

2 10 4
-

3 10 4
-

4 10 4
-

0
5
10
15
Iin t( )
IL t( )
t
Critical Conduction Mode (CrCM)

## [стр. 4]

PFC  boost converter design guide
Application Note
4
Revision1.1, 2016-02-22
Design Note DN 2013-01
V1.0 January 2013

Power stage design
2
The following are the converter design and power losses equations for the CCM operated boost. The design
example specifications listed in Table 1 will be used for all of the equations calculations. Also the boost
converter encounters the maximum current stress and power losses at the minimum line voltage condition
(𝑉𝑎𝑐.𝑚𝑖𝑛 ); hence, all design equations and power losses will be calculated using the low-line voltage
condition as an extreme case.

Specifications of the power stage
Table 1
Input voltage
85-265 VAC  60 Hz
Output voltage
400 V
Maximum power steady state
1200 W
Switching frequency
100 kHz
Inductor current ripple
25% @ low line/full load
Output voltage 120Hz ripple
10 Vp-p
Hold-up time
16.6 ms @ VO,min=340 V


Figure 3
Block schematic for boost power stage with input rectifier
2.1
Main PFC inductor
Off-the-shelf inductors are available and usable for a first pass design, typically with single layer windings
and a permeability drop of 30% or less.
In some circumstances it may be desirable to further optimize the inductor configuration in order to meet
the requirements for high power factor over a wide input line current range. Many popular PFC controllers
use single cycle current loop control, which can provide good performance provided that the inductor
remains in CCM operation. At low-line this is no problem, but for the operation in the high-line band (176 VAC
to 265 VAC), the operating current will be much lower.  If an inductor is used with a nominal "stable" value of
inductance, it works well at low-line but results in DCM mode operation for a significant part of the load
range at high-line, with poorer power factor, THDi and higher EMI. A swinging choke (also called powder
core), such as Arnold/Micrometals Sendust or Magnetics Inc Kool Mu, can address this if designed with the

## [стр. 5]

PFC  boost converter design guide
Application Note
5
Revision1.1, 2016-02-22
Design Note DN 2013-01
V1.0 January 2013
right energy capability and with full load permeability drop by 75-80%, so that at lighter load the inductance
swings up.
The filter inductor value and its maximum current are determined based on the specified maximum
inductor current ripple as shown below:
𝐿=
1
%𝑅𝑖𝑝𝑝𝑙𝑒 ∙𝑉𝑎𝑐.𝑚𝑖𝑛
2
𝑃𝑜
(1 -√2 ∙𝑉𝑎𝑐 .𝑚𝑖𝑛
𝑉𝑜
) ∙𝑇=
1
0.25 ∙
(85 𝑉)2
1200 𝑊(1 -√2 ∙85 𝑉
400 𝑉) ∙
1
100 ∙103𝐻𝑧 = 168.5 𝜇𝐻
Eq. 1

𝐼𝐿.𝑚𝑎𝑥= √2 ∙𝑃𝑜
𝑉𝑎𝑐.𝑚𝑖𝑛
∙(1 + %𝑅𝑖𝑝𝑝𝑙𝑒
2
) = √2 ∙1200 𝑊
85 𝑉
∙(1 + 0.25
2 ) = 22.5 𝐴
Eq. 2

Note: Inductor saturation current must be rated at > 22.5 A.
In this evaluation board design, a 60 μ permeability Kool Mu core from Magnetics Inc. is used. It consists of
two stacked of "Kool Mμ" 77083A7 toroids cores from Magnetics Inc., with 64 turns of 1.15 mm copper wire,
the DC resistance is about 70 mΩ, and the inductance ranges from 680 µH at no load dropping to about 165
µH at low-line full load, which is very close to the desired value calculated above.

Figure 4
Main PFC inductor
Since the inductance value is varying across the line and load range, and also across the line cycle, it would
be more accurate to model the inductance value as a function of Vin, Po and t. in order to obtain better
estimation of the switching currents and losses. This specific inductor value was modeled as shown in Figure
5.

Figure 5
Swinging inductance accros load/line range

L (Henry)
Po (W)
230Vac  @
85Vac   @
85Vac    @
230Vac  @

## [стр. 6]

PFC  boost converter design guide
Application Note
6
Revision1.1, 2016-02-22
Design Note DN 2013-01
V1.0 January 2013
Inductor copper loss:
The inductor RMS current and the corresponding copper loss are:
𝐼𝐿.𝑟𝑚𝑠≅𝐼𝑖𝑛.𝑟𝑚𝑠=
𝑃𝑜
𝑉𝑎𝑐.𝑚𝑖𝑛
= 1200 𝑊
85 𝑉
= 14.12 𝐴
Eq. 3
𝑃𝐿.𝑐𝑜𝑛𝑑= 𝐼𝐿.𝑟𝑚𝑠
2 ∙𝐷𝐶𝑅= (14.12 𝐴)2 ∙0.07 Ω= 13.95 𝑊
Eq. 4
Inductor core losses:
At low-line, core loss across the line cycle is found to be close to a sinusoidal shape (Figure 6, left).  Therefore
a simple and accurate enough method to estimate the average core loss is to calculate the peak core loss at
the peak of the line cycle point, then multiply by 2/π. However, at high line, core losses are far from the
sinusoidal shape (Figure 6, right), so the aforementioned method is not valid anymore, so it is necessary to
model the core loss across the line cycle as a function of time, and then integrate it to obtain the average
loss.

Figure 6
Inductor core loss across the line cycle: low-line (left) , high-line (right)
Since in this document we are calculating losses at the minimum line voltage, as the worst case scenario,
thus we will use the first method discussed above to obtain the average core loss in the low-line, as detailed
below:
In order to calculate the core loss, we must calculate the minimum and maximum inductor current and the
associated minimum and maximum magnetic force (H), then we can use the fitted equation of that
magnetic material to calculate the minimum and maximum magnetic flux (B). Then the AC flux swing can be
used to calculate the core loss by using another fitted equation.
For 2 stacked Kool Mμ 77083A7 toroids, we get:
𝑃𝑎𝑡ℎ 𝑙𝑒𝑛𝑔𝑡ℎ  𝑙𝑒= 98.4 𝑚𝑚        𝐶𝑟𝑜𝑠𝑠 𝑠𝑒𝑐𝑡𝑖𝑜𝑛 𝑎𝑟𝑒𝑎  𝐴𝑒= 2 ∙107 𝑚𝑚2       𝑉𝑜𝑙𝑢𝑚𝑒  𝑉𝑒= 2 ∙10600 𝑚𝑚3
Using the maximum inductor current calculated in Eq. 2, the magnetic force at the peak of the line cycle can
be found as:
𝐻𝑚𝑎𝑥= 0.4 ∙𝜋∙𝑁∙𝐼𝐿.𝑚𝑎𝑥
𝑙𝑒 (𝑖𝑛 𝑐𝑚)
= 0.4 ∙𝜋∙64 𝑡𝑢𝑟𝑛𝑠∙22.51𝐴
98.4 𝑚𝑚/10
= 184 𝑂𝑒𝑟𝑠𝑡𝑒𝑑𝑠
Eq. 5
The minimum inductor current and magnetic force at the peak of the line cycle are:
𝐼𝐿.𝑚𝑖𝑛= 𝑃𝑜∙√2
𝑉𝑎𝑐.𝑚𝑖𝑛
(1 -%𝑅𝑖𝑝𝑝𝑙𝑒
2
) = 1200 𝑊∙√2
85 𝑉
(1 -25%
2 ) = 17.42 𝐴
Eq. 6
𝐻𝑚𝑖𝑛= 0.4 ∙𝜋∙𝑁∙𝐼𝐿.𝑚𝑖𝑛
𝑙𝑒 (𝑖𝑛 𝑐𝑚)
= 0.4 ∙𝜋∙64𝑡𝑢𝑟𝑛𝑠∙17.42 𝐴
98.4𝑚𝑚/10
= 142.37 𝑂𝑒𝑟𝑠𝑡𝑒𝑑𝑠
Eq. 7

## [стр. 7]

PFC  boost converter design guide
Application Note
7
Revision1.1, 2016-02-22
Design Note DN 2013-01
V1.0 January 2013
Flux density for 60 Koolu material is:
𝐵= (𝑎+ 𝑏∙𝐻+ 𝑐∙𝐻2
𝑎+ 𝑑∙𝐻+ 𝑒∙𝐻2)
𝑥

Eq. 8
where a = 1.658e-2   b = 1.831e-3   c = 4.621e-3   d = 4.7e-3   e = 3.833e-5   x = 0.5
The minimum and maximum flux densities at the peak of the line cycle are:
𝐵𝑚𝑎𝑥= (𝑎+ 𝑏∙𝐻𝑚𝑎𝑥+ 𝑐∙𝐻𝑚𝑎𝑥
2
𝑎+ 𝑑∙𝐻𝑚𝑎𝑥+ 𝑒∙𝐻𝑚𝑎𝑥
2)
𝑥
= 8.483 𝑘𝐺𝑎𝑢𝑠𝑠
Eq. 9
𝐵𝑚𝑖𝑛= (𝑎+ 𝑏∙𝐻𝑚𝑖𝑛+ 𝑐∙𝐻𝑚𝑖𝑛
2
𝑎+ 𝑑∙𝐻𝑚𝑖𝑛+ 𝑒∙𝐻𝑚𝑖𝑛
2)
𝑥
= 8.014 𝑘𝐺𝑎𝑢𝑠𝑠
Eq. 10
The AC flux swing at the peak of the line cycle is:
∆𝐵= 𝐵𝑚𝑎𝑥-𝐵𝑚𝑖𝑛
2
= 0.234 𝑘𝐺𝑎𝑢𝑠
Eq. 11
Peak core loss at the peak of the line cycle is:
𝑃𝑐𝑜𝑟𝑒.𝑝𝑘= ∆𝐵2 ∙( 𝑓
103)
1.46
∙𝑉𝑒∙10-6 = 0.2342 ∙(100 ∙103
103
)
1.46
∙2 ∙10600 ∙10-6 = 0.97 𝑊
Eq. 12
Average core loss across the line cycle is:
𝑃𝑐𝑜𝑟𝑒.𝑎𝑣= 𝑃𝑐𝑜𝑟𝑒.𝑝𝑘∙2
𝜋= 0.968 𝑊∙2
𝜋= 0.62 𝑊
Eq. 13
2.2
Rectifier bridge
Using a higher rated current bridge can reduce the forward voltage drop Vf, which reduces the total power
dissipation at a small incremental cost. Also using two parallel bridges is another approach to distribute the
thermal dissipation.  This is often a sound strategy, as with modern components, the bridge rectifier usually
has the highest semiconductor loss for the PFC stage. In this evaluation board design, 2 parallel GSIB2580
are used.
The bridge total power loss is calculated using the average input current flowing through two of the bridge
rectifying diodes and is shown as:
𝐼𝑎𝑣𝑒𝑟𝑎𝑔𝑒= 2
𝜋∙√2 ∙𝑃𝑜
𝑉𝑎𝑐.𝑚𝑖𝑛
= 2
𝜋∙√2 ∙1200 𝑊
85 𝑉
= 12.71 𝐴
Eq. 14
𝑃𝑏𝑟𝑖𝑑𝑔𝑒= 2 ∙𝐼𝑎𝑣𝑒𝑟𝑎𝑔𝑒∙𝑉𝑓.𝑏𝑟𝑖𝑑𝑔𝑒 = 2 ∙12.71 𝐴∙1 𝑉= 25.4 𝑊
Eq. 15
The selection on the heat sink is based on the process discussed in chapter 2.6 Heat sink design.

2.3
MOSFET
In order to select the optimum MOSFET, one must understand the MOSFET requirements in a CCM boost
converter. High voltage MOSFETS have several families based on different technologies. For a boost
converter, the following are some major MOSFET selection considerations for high efficiency application
design:
 Low figure-of merits - RDS(ON)*Qg and RDS(ON)*Eoss

## [стр. 8]

PFC  boost converter design guide
Application Note
8
Revision1.1, 2016-02-22
Design Note DN 2013-01
V1.0 January 2013
 Fast turn-on/off switching to reduce the device switching losses
 Gate plateau near middle of gate drive range to balance turn-on/off losses
 Low output capacitance Coss for low switching energy and to increase light load efficiency
 Drain-source breakdown voltage VBR(DSS) to handle spikes/overshoots
 Low thermal resistance RthJC. Package selection must consider the resulting total thermal resistance from
junction to ambient, and the worst case surge dissipation, typically under low-line cycle skipping and
recovery into highline while ramping the bulk voltage back up.
 The body diode commutation speed and reverse recovery charge are not important, since body diode
never conducts in the CCM boost converter.
Several CoolMOS™  series can be used for boost applications. C7 followed by CP provides the fastest
switching (Figure 7) and best performance, but require careful design in terms of gate driving circuit and
PCB layout. The P6/C6/E6 series provides a cost advantage, with easier design. The P6 series approaches CP
performance closely at a better price point, and is recommended for new designs that are cost sensitive. In
this Evaluation board C7 is used to reach the best efficiency.
Figure 7 shows that CoolMOS™ C7 total gate charge Qg is less than one third of the C6 charge, and less than
two thirds of the CP charge. Moreover, it shows gate-drain charge Qgd reduction in the much shorter length
of the Miller Plateau compared to previous generations. These improvements in the gate charge profile are
an indication of the improvement of the gate driving related losses as well as of the MOSFET switching times
and losses.

Figure 7
 Gate charge and Eoss comparision for 41-45 mΩ CoolMOS™ C6, CP, C7
2.3.1
CoolMOS™  optimum RDS(ON) selection charts
Selection of the optimum on-state resistance of a specific CoolMOS™  series is based on the balancing
between switching losses and conduction losses of the device at a targeted load point. This can be done by
modeling all losses in software tool such as Mathcad® by evaluating different technologies and different
values of the on-state resistance. This requires few iterations and entry of several parameters from the
datasheet of each part.
An alternative way is using the CoolMOS™ selection charts shown in Figure 9 to Figure 12, specific charts
exist for each CoolMOS™ family, optimized at half load or full load. The following is a guide on how to use
these CoolMOS™ RDS(ON) selection charts.
Let's use the specifications in Table 1 as our design example:
Po= 1200 W, f=100 kHz; full load efficiency is critical; CoolMOS™ C7 is preferred for best performance.

## [стр. 9]

PFC  boost converter design guide
Application Note
9
Revision1.1, 2016-02-22
Design Note DN 2013-01
V1.0 January 2013
 Step 1: Find the correct chart, Figure 8 shows the chart for CoolMOS™ C7 optimized at full load.
 Step 2: Find the 100 kHz curves (blue curves in this example)
 Step3: Mark the 1200 W on the x-axis
 Step 3: Find the 1200 W intersection with the solid blue line for the 100 kHz, read the left side y-axis, we
find that 0.055 Ohm is the optimum for CoolMOS™ C7, then we may choose 045C7.
 Step 4: Find the 1200 W intersection with the dashed blue line for the 100 kHz, read the right side y-axis,
we find that the 0.055 Ω will result in 13.9 W power loss at full load and low line 115 VAC.


Figure 8
Example on how to use the CoolMOS™  optimum RDS(on)  selection charts.
45kHz
65kHz
0.01
1
0.1
1
100
10
100
10,000
Output Power (W)
Optimum FET On-Resistance (ohm)
Max Power Loss (W) for Optimum FET @ 115 Vac
045C7
065C7
095C7
125C7
190C7
225C7
019C7
100kHz
150kHz
200kHz
400kHz
Ron optimized at full load
Best thermal performance
1200W
13.9W
0.055ohm
45kHz
65kHz
100kHz
150kHz
200kHz
400kHz

## [стр. 10]

PFC  boost converter design guide
Application Note
10
Revision1.1, 2016-02-22
Design Note DN 2013-01
V1.0 January 2013


Figure 9
CoolMOS™  C7 optimum RDS(on) selection charts


Figure 10
CoolMOS™  CP optimum RDS(on) selection charts
1000
10,000
45kHz
65kHz
0.01
1
0.1
1
100
10
100
Output Power (W)
Optimum FET On-Resistance (ohm)
Max Power Loss (W) for Optimum FET @ 115 Vac
045C7
065C7
095C7
125C7
190C7
225C7
019C7
100kHz
150kHz
200kHz
400kHz
Ron optimized at full load
Best thermal performance
45kHz
65kHz
100kHz
150kHz
200kHz
400kHz
0.01
1
0.1
1
100
10
100
10,000
Output Power (W)
Optimum FET On-Resistance (ohm)
Max Power Loss (W) for Optimum FET @ 115 Vac
045C7
065C7
095C7
125C7
190C7
225C7
019C7
Ron optimized at 50% load
Balanced light/full load efficiency
45kHz
65kHz
100kHz
150kHz
200kHz
400kHz
45kHz
65kHz
100kHz
150kHz
200kHz
400kHz
1000
0.01
1
0.1
1
100
10
100
10,000
Output Power (W)
Optimum FET On-Resistance (ohm)
Max Power Loss (W) for Optimum FET @ 115 Vac
045CP
075CP
099CP
125CP
165CP
199CP
250CP
299CP
385CP
600CP
520CP
Ron optimized at full load
Best thermal performance
0.01
1
0.1
1
100
10
100
10,000
Output Power (W)
Optimum FET On-Resistance (ohm)
Max Power Loss (W) for Optimum FET @ 115 Vac
045CP
075CP
099CP
125CP
165CP
199CP
250CP
299CP
385CP
600CP
520CP
Ron optimized at 50% load
Balanced light/full load efficiency
45kHz
65kHz
100kHz
150kHz
200kHz
400kHz
45kHz
65kHz
100kHz
150kHz
200kHz
400kHz
45kHz
65kHz
100kHz
150kHz
200kHz
400kHz
45kHz
65kHz
100kHz
150kHz
200kHz
400kHz
1000
1000

## [стр. 11]

PFC  boost converter design guide
Application Note
11
Revision1.1, 2016-02-22
Design Note DN 2013-01
V1.0 January 2013


Figure 11
CoolMOS™  P6 Optimum RDS(on) selection charts


Figure 12
CoolMOS™  C6 optimum RDS(on) selection charts
Since we found that 45 mΩ CoolMOS™ C7 "IPW65R045C7" is the optimum device for our design, we can base
on it to calculate different power losses at the worst case of 85 Vac full load condition, as follows:
The MOSFET RMS current across the 60 Hz line cycle can be calculated by the following equation, and
consequently the MOSFET conduction loss can be obtained as:
0.01
1
100
10
100
10,000
Output Power (W)
Optimum FET On-Resistance (ohm)
Max Power Loss (W) for Optimum FET @ 115 Vac
1
0.1
041P6
070P6
099P6
125P6
160P6
190P6
230P6
280P6
330P6
380P6
600P6
Ron optimized at full load
Best thermal performance
0.01
1
0.1
1
100
10
100
10,000
Output Power (W)
Optimum FET On-Resistance (ohm)
Max Power Loss (W) for Optimum FET @ 115 Vac
041P6
070P6
099P6
125P6
160P6
190P6
230P6
280P6
330P6
380P6
600P6
Ron optimized at 50% load
Balanced light/full load efficiency
45kHz
65kHz
100kHz
150kHz
200kHz
400kHz
45kHz
65kHz
100kHz
150kHz
200kHz
400kHz
45kHz
65kHz
100kHz
150kHz
200kHz
400kHz
45kHz
65kHz
100kHz
150kHz
200kHz
400kHz
1000
1000
100kHz
150kHz
200kHz
400kHz
45kHz
65kHz
0.01
1
100
10
100
10,000
Output Power (W)
Optimum FET On-Resistance (ohm)
Max Power Loss (W) for Optimum FET @ 115 Vac
1
0.1
041C6
070C6
099C6
125C6
160C6
190C6
280C6
380C6
600C6
520C6
950C6
Ron optimized at full load
Best thermal performance
0.01
1
100
10
100
10,000
Output Power (W)
Optimum FET On-Resistance (ohm)
Max Power Loss (W) for Optimum FET @ 115 Vac
1
0.1
041C6
070C6
099C6
125C6
160C6
190C6
280C6
380C6
600C6
520C6
950C6
Ron optimized at 50% load
Balanced light/full load efficiency
45kHz
65kHz
100kHz
150kHz
200kHz
400kHz
45kHz
65kHz
100kHz
150kHz
200kHz
400kHz
45kHz
400kHz
45kHz
400kHz
1000
1000

## [стр. 12]

PFC  boost converter design guide
Application Note
12
Revision1.1, 2016-02-22
Design Note DN 2013-01
V1.0 January 2013
𝐼𝑆.𝑟𝑚𝑠=
𝑃𝑜
𝑉𝑎𝑐.𝑚𝑖𝑛
∙√1 -8 ∙√2 ∙𝑉𝑎𝑐.𝑚𝑖𝑛
3 ∙𝜋∙𝑉𝑜
= 1200 𝑊
85 𝑉
∙√1 -8 ∙√2 ∙85 𝑉
3 ∙𝜋∙400 𝑉= 12.2 𝐴
Eq. 16
𝑃𝑆.𝑐𝑜𝑛𝑑= 𝐼𝑆.𝑟𝑚𝑠
2 ∙𝑅𝑜𝑛(100℃) = 12.2 2 ∙(0.045 ∙1.8) = 12 𝑊
(𝐴𝑠𝑠𝑢𝑚𝑖𝑛𝑔 𝑅𝑜𝑛(100℃) = 1.8 ∙𝑅𝑜𝑛(25℃) )
Eq. 17
For switching losses calculation, the average input current is used to estimate the losses over the line cycle.
The calculation is based on the switching time consideration, where the triangular area between current
and voltage changing references to the switching losses.


Figure 13
Simplified turn-on and turn-off waveforms
The average input current is given as:
𝐼𝐿.𝑎𝑣𝑔=
𝑃𝑜
𝑉𝑎𝑐.𝑚𝑖𝑛
∙2 ∙√2
𝜋
=   = 1200 𝑊
85 𝑉
∙2 ∙√2
𝜋
= 12.71 𝐴
Eq. 18
Turn-on time and loss are:
𝑡𝑜𝑛= 𝐶𝑖𝑠𝑠∗𝑅𝑔∙𝑙𝑛(
𝑉𝑔-𝑉𝑡ℎ
𝑉𝑔-𝑉𝑝𝑙
) + 𝐶𝑟𝑠𝑠∙𝑅𝑔∙(
𝑉𝑑𝑠-𝑉𝑝𝑙
𝑉𝑔-𝑉𝑝𝑙
)
      = 4340 ∙10-12𝐹∙1.8 Ω∙𝑙𝑛(12 𝑉-3.5 𝑉
12 𝑉-5.4 𝑉) + 75 ∙10-12𝐹∙1.8Ω∙(400 𝑉-5.4 𝑉
12 𝑉-5.4 𝑉)
= 10 ∙10-9 𝑠
Eq. 19
(𝑉𝑑𝑠= 𝑉𝑜= 400 𝑉    ,    𝐶𝑟𝑠𝑠= 𝑄𝑔𝑑
𝑉𝑑𝑠
= 93 ∙10-9𝑛𝐶
400 𝑉
= 75 ∙10-12𝐹)
𝑃𝑆.𝑜𝑛= 0.5 ∙𝐼𝐿.𝑎𝑣𝑔∙𝑉𝑜∙𝑡𝑜𝑛∙𝑓= 0.5 ∙12.71𝐴∙400 𝑉∙10 ∙10-9𝑠∙100 ∙103𝐻𝑧= 2.5 𝑊
Eq. 20
Turn-off time and loss are:
𝑡𝑜𝑓𝑓= 𝐶𝑟𝑠𝑠∗𝑅𝑔∙(
𝑉𝑑𝑠-𝑉𝑝𝑙
𝑉𝑝𝑙
) + 𝐶𝑖𝑠𝑠∙𝑅𝑔∙𝑙𝑛(
𝑉𝑝𝑙
𝑉𝑡ℎ
)
        = 75 ∙10-12𝐶∙1.8Ω∙(400 𝑉-5.4 𝑉
5.4 𝑉
) + 4340 ∙10-12𝐶∙1.8Ω∙𝑙𝑛(5.4 𝑉
3.5 𝑉) = 13.3 ∙10-9 𝑠
Eq. 21
𝑃𝑆.𝑜𝑓𝑓= 0.5 ∙𝐼𝐿.𝑎𝑣𝑔∙𝑉𝑜∙𝑡𝑜𝑓𝑓∙𝑓= 0.5 ∙12.71𝐴∙400𝑉∙13.25 ∙10-9𝑠∙100 ∙103𝐻𝑧= 3.4 𝑊
Eq. 22
The above is the "classic" format for calculating turn-off time and loss; due to the high Qoss of Super Junction
MOSFETs, the Coss acts like a nonlinear capacitive snubber, and actual turn-off losses with fast switching can

## [стр. 13]

PFC  boost converter design guide
Application Note
13
Revision1.1, 2016-02-22
Design Note DN 2013-01
V1.0 January 2013
be up to 50% lower than calculated. The current flow through the drain during turn-off under these
conditions is non-dissipative capacitive current, and with fast drive, the channel may be completely turned
off by the onset of drain voltage rise.
Output capacitance Coss switching loss are:
𝑃𝑆.𝑜𝑠𝑠= 𝐸𝑜𝑠𝑠∙𝑓    = 11.7 ∙10-6 𝐽𝑜𝑢𝑙𝑒∙100 ∙103 𝐻𝑧= 1.17 𝑊
Eq. 23
Gate drive loss is defined as:
𝑃𝑆.𝑔𝑎𝑡𝑒= 𝑉𝑔∙𝑄𝑔∙𝑓  = 12 𝑉∙93 ∙10-9 𝑛𝐶∙100 ∙103𝐻𝑧= 0.11 𝑊
Eq. 24
Total MOSFET loss is defined as:
𝑃𝑆.𝑡𝑜𝑡𝑎𝑙= 𝑃𝑆.𝑐𝑜𝑛𝑑+ 𝑃𝑆.𝑜𝑛 + 𝑃𝑆.𝑜𝑓𝑓+ 𝑃𝑆.𝑜𝑠𝑠= 19.2 𝑊
Eq. 25
2.3.2
TO-247 4-pin package with Kelvin source connection
In common gate drive arrangements, the fast current transient causes a voltage drop VLS across the parasitic
inductance of the source of the MOSFET that can counteracts the driving voltage. The induced source
voltage, VLS = L*di/dt, can reduce the gate current (Figure 14), therefore lead to slowing down the switching
transient and increasing the associated energy loss. On the other hand, the kelvin-source package concept
is to exclude the package source inductance and layout inductance from the driving loop, so that the L*di/dt
induced voltage is outside the gate drive loop and not affecting the gate current and switching losses. The
4pin MOSFET recommended for this design would be IPZ65R045C7.


Figure 14
a) Conventional package
b) TO-247 4pin package
2.4
Boost diode
Selection of the boost diode is a major design decision in CCM boost converter. Since the diode is hard
commutated at a high current, and the reverse recovery can cause significant power loss, noise and current
spikes. Reverse recovery can be a bottle neck for high switching frequency and high power density power
supplies. Additionally, at low line, the available diode conduction duty cycle is quite low, and the forward
current quite high in proportion to the average current. For that reason, the first criteria for selecting a diode
in CCM boost are fast recovery with low reverse recovery charge, followed by Vf operating at high forward
current.
Since Silicon Carbide (SiC) Schottky Diodes have capacitive charge ,Qc, rather than reverse recovery charge,
Qrr. Their switching loss and recovery time are much lower compared to silicon ultrafast diode, and will
show an enhanced performance. Moreover, SiC diodes allow higher switching frequency designs, hence,
higher power density converters is achieved.

## [стр. 14]

PFC  boost converter design guide
Application Note
14
Revision1.1, 2016-02-22
Design Note DN 2013-01
V1.0 January 2013
The capacitive charge for SiC diodes are not only low, but also independent on di/dt, current level, and
temperature; which is different from Si diodes that have strong dependency on these conditions, as shown
in Figure 15.


Figure 15
Capacitive charge as a function of di/dt for Si pin double diode and SiC diode
The newer generations of SiC diodes are not just Schottky devices, but are merged structure diodes known
as MPS diodes - Merged PN/Schottky (Figure 16).  They combine the relatively low Vf and capacitive charge
characteristics of Schottky Diodes with the high peak current capability of PN diodes, while avoiding the
high junction voltage penalty (typically 2.5-3 V at room temperature) of a pure PN wide bandgap diode.


Figure 16
Schottky and Merged PN/Schottky compared
The recommended diode for CCM boost applications is the 650 V CoolSiC™ Schottky Diode Generation 5,
which include Infineon's leading edge technologies, such as diffusion soldering process and wafer thinning
technology. The result is a new family of products showing improved efficiency over all load conditions,
coming from both the improved thermal characteristics and an improved figure-of-merit (Qc x Vf).
With the high surge current capability of the MPS diode, there is some latitude for the selection of the boost
diode. A simple rule of thumb that works well for a wide input range PFC is 1 A diode rating for each 150 W of
output power for good cost/performance tradeoffs, or 1 A diode rating for each 75 W for a premium
performance. For example, a 600 W application will only need a 4 A rated diode, but an 8 A diode would
perform better at full load. Especially at low-line operation, where the input current is quite high with a

## [стр. 15]

PFC  boost converter design guide
Application Note
15
Revision1.1, 2016-02-22
Design Note DN 2013-01
V1.0 January 2013
short duty cycle, the higher rated diode will have a much lower Vf at the actual operating current, reducing
the conduction losses.
Note that even when using the MPS type SiC diode, it is still preferred to use a bulk pre-charge diode as
shown earlier in Figure 3.  This is a low frequency standard diode with high I2t rating to support pre-charging
the bulk capacitor to the peak of the AC line voltage; this is a high initial surge current stress (which should
be limited by a series NTC) that is best avoided for the HF boost rectifier diode.
In this design example, we are using the 1 A/75 W rule, so for a 1200 W we require a 16 A diode, therefore SiC
diode IDH16G65C5 is selected.
The boost diode average current and conduction loss are:
𝐼𝐷.𝑎𝑣𝑔= 𝑃𝑜
𝑉𝑜
= 1200 𝑊
400 𝑉= 3 𝐴
Eq. 26
𝑃𝐷.𝑐𝑜𝑛𝑑= 𝐼𝐷.𝑎𝑣𝑔∙𝑉𝑓.𝑑𝑖𝑜𝑑𝑒= 3 𝐴∙1.5 𝑉= 4.5 𝑊
Eq. 27
Diode switching loss, which is carried by the boost MOSFET is:
𝑃𝐷.𝑠𝑤𝑖𝑡= 0.5 ∙𝑉𝑜∙𝑄𝐶∙𝑓= 0.5 ∙400𝑉∙23 ∙10-9𝑛𝐶∙100 ∙103𝐻𝑧= 0.46 𝑊
Eq. 28
Diode total loss is:
𝑃𝐷.𝑡𝑜𝑡𝑎𝑙= 𝑃𝐷.𝑐𝑜𝑛𝑑+ 𝑃𝐷.𝑠𝑤𝑖𝑡= 4.5 𝑊+ 0.46 𝑊= 4.96 𝑊
Eq. 29
2.5
Output capacitor
The output capacitor is sized to meet both of the hold-up time (16.6 ms) and the low frequency voltage
ripple (10 V) requirements. The capacitor value is selected to have the larger value among the two equations
in below:
𝐶𝑜≥2 ∙𝑃𝑜∙𝑡ℎ𝑜𝑙𝑑
𝑉𝑜
2 -𝑉𝑜.𝑚𝑖𝑛
2 = 2 ∙1200 𝑊∙16.6 ∙10-3𝑠𝑒𝑐
(400 𝑉)2 -(340 𝑉)2
= 900.9 𝜇𝐹
Eq. 30
𝐶𝑜≥
𝑃𝑜
2 ∙𝜋∙𝑓𝑙𝑖𝑛𝑒 ∙∆𝑉𝑜∙𝑉𝑜
=
1200 𝑊
2 ∙𝜋∙60 𝐻𝑧∙10 𝑉∙400 𝑉= 795.8 𝜇𝐹
Eq. 31
→  𝐶𝑜= 𝑚𝑎𝑥 (900.9 𝜇𝐹 , 795.8 𝜇𝐹) = 900.9 𝜇𝐹
In this design we use two parallel 560 μF , 450 V, with dissipation factor DF=0.2, consequently the capacitor
ESR loss is obtained as below:
𝐸𝑆𝑅=
𝐷𝐹
2 ∙𝜋∙𝑓∙𝐶𝑜
=
0.2
2 ∙𝜋∙120𝐻𝑧∙(2 ∙560 𝜇𝐹) = 0.237 Ω
Eq. 32
The capacitor RMS current across the 60Hz line cycle can be calculated by the following equation.
𝐼𝐶𝑜.𝑟𝑚𝑠= √
8 ∙√2 ∙𝑃𝑜
2
3 ∙𝜋∙𝑉𝑎𝑐.𝑚𝑖𝑛 ∙𝑉𝑜
-𝑃𝑜
2
𝑉𝑜
2 = √8 ∙√2 ∙(1200 𝑊)2
3 ∙𝜋∙85 𝑉 ∙400 𝑉-(1200 𝑊)2
(400 𝑉)2 = 6.47 𝐴
Eq. 33
𝑃𝐶𝑜= 𝐼𝐶𝑜.𝑟𝑚𝑠
2 ∙𝐸𝑆𝑅= (6.47𝐴)2 ∙0.237 Ω= 9.91 𝑊
Eq. 34

## [стр. 16]

PFC  boost converter design guide
Application Note
16
Revision1.1, 2016-02-22
Design Note DN 2013-01
V1.0 January 2013
2.6
Heat sink design
The MOSFET and boost diode share the same heat sink, thermal resistors are modeled as in Figure 17.
In this evaluation board the maximum heat sink temperature 𝑇𝑆 is regulated to 60°C, so we can calculate the
average junction temperature for the MOSFET and diode as follows:
𝑇𝐽.𝑑𝑖𝑜𝑑𝑒= 𝑇𝑆+ 𝑃𝑑𝑖𝑜𝑑𝑒∙(𝑅𝑡ℎ𝐶𝑆.𝑑𝑖𝑜𝑑𝑒+ 𝑅𝑡ℎ𝐽𝐶.𝑑𝑖𝑜𝑑𝑒)
Eq. 35
𝑇𝐽.𝐹𝐸𝑇= 𝑇𝑆+ 𝑃𝐹𝐸𝑇∙(𝑅𝑡ℎ𝐶𝑆.𝐹𝐸𝑇+ 𝑅𝑡ℎ𝐽𝐶.𝐹𝐸𝑇)
Eq. 36
The 𝑇𝑆 can be regulated by choosing a heatsink that with certain airflow can reach the thermal resistance
(𝑅𝑡ℎ𝑆𝐴) calculated below:
𝑅𝑡ℎ𝑆𝐴=
𝑇𝑆-𝑇𝐴
𝑃𝐹𝐸𝑇+ 𝑃𝑑𝑖𝑜𝑑𝑒

Eq. 37
Where:
𝑅𝑡ℎ𝐽𝐶 : Thermal resistance from junction to case, this is specified in the MOSFET and Diode datasheets.
𝑅𝑡ℎ𝐶𝑆 : Thermal resistace from case to heatsink, typically low compared to the overall thermal resistance, its
value depends on the the interface material, for example, thermal grease and thermal pad.
𝑅𝑡ℎ𝑆𝐴 : Thermal resistance from heatsink to ambient, this is specified in the heatsink datasheets, it depends
on the heatsink size and design, and is a function of the surroundings, for example, a heat sink could
have difference values for RthSA for different airflow conditions.
𝑇𝑆 :  Heatsink temperature.
𝑇𝐶 : Case temperature.
𝑇𝐴 : Ambient temperature.
𝑃𝐹𝐸𝑇 : FET total power loss.
𝑃𝑑𝑖𝑜𝑑𝑒 : Diode total power loss.

PFET
RthJC.FET
RthCS.FET
RthJC.diode
RthCS.diode
RthSA


TJ.FET
TJ.diode
TS
TA
TC.FET
TC.diode
Pdiode
PFET+Pdiode

Figure 17
Schematic of thermal network

## [стр. 17]

PFC  boost converter design guide
Application Note
17
Revision1.1, 2016-02-22
Design Note DN 2013-01
V1.0 January 2013

ICE3PCS01G PFC boost controller
3
The ICE3PCS01G is a 14pins controller IC for power factor correction converters. It is suitable for wide range
line input applications from 85 to 265 VAC and with overall efficiency above 97%. The IC supports the
converters in boost topology and operates in continuous conduction mode (CCM) with average current
control.
The IC operates with a cascaded control; the inner current loop and the outer voltage loop. The inner
current loop of the IC controls the sinusoidal profile for the average input current. It uses the dependency of
the PWM duty cycle on the line input voltage to determine the corresponding input current. This means the
average input current follows the input voltage as long as the device operates in CCM. Under light load
condition, depending on the choke inductance, the system may enter into discontinuous conduction mode
(DCM) resulting in a higher harmonics but still meeting the Class D requirement of IEC 1000-3-2.
The outer voltage loop of the IC controls the output bulk voltage and is integrated digitally within the IC.
Depending on the load condition, internal PI compensation output is converted to an appropriate DC
voltage which controls the amplitude of the average input current.
The IC is equipped with various protection features to ensure safe operating for the system and the device.
3.1
Soft startup
During power up when the VOUT is less than 96% of the rated level, internal voltage loop output increases
from initial voltage under the soft-start control. This results in a controlled linear increase of the input
current from 0 A as can be seen in Figure 17.  This helps to reduce the current stress in power components.
Once VOUT has reached 96% of the rated level, the soft-start control is released to achieve good regulation
and dynamic response and VB_OK pin outputs 5 V indicating PFC output voltage in normal range.
3.2
Gate switching frequency
The switching frequency of the PFC converter can be set with an external resistor RFREQ at pin FREQ with
reference to pin SGND. The voltage at pin FREQ is typical 1V. The corresponding capacitor for the oscillator is
integrated in the device and the RFREQ/frequency is given in Figure 18. The recommended operating
frequency range is from 21 kHz to 250 kHz. As an example, a RFREQ of 43 kΩ at pin FREQ will set a switching
frequency fSW of 100 kHz typically.


Figure 18
Frequency setting
Frequency vs Resistance
0
20
40
60
80
100
120
140
160
180
200
220
240
260
10
20
30
40
50
60
70
80
90 100 110 120 130 140 150 160 170 180 190 200 210 220 230 240 250
Resistance/kohm
Frequency/kHz
19.2
232
43
100
20.2
221
49
90
21.2
210
55
80
23
200
62
70
25
191
74
60
26.2
169
86
50
29.5
150
106
40
31.5
140
141
30
34
130
211
20
36
120
249
17
40
110
278
15
Frequency
/kHz
Resistance
/kohm
Frequency
/kHz
Resistance
/kohm

## [стр. 18]

PFC  boost converter design guide
Application Note
18
Revision1.1, 2016-02-22
Design Note DN 2013-01
V1.0 January 2013
3.3
Protection features
3.3.1
Open loop protection (OLP)
The open loop protection is available for this IC to safe-guard the output. Whenever voltage at pin VSENSE falls
below 0.5 V, or equivalently VOUT falls below 20% of its rated value, it indicates an open loop condition (i.e.
VSENSE pin not connected). In this case, most of the blocks within the IC will be shutdown. It is implemented
using a comparator with a threshold of 0.5 V.
3.3.2
First over-voltage protection (OVP1)
Whenever VOUT exceeds the rated value by 8%, the first over-voltage protection OVP1 is active. This is
implemented by sensing the voltage at pin VSENSE with respect to a reference voltage of 2.7 V. A VSENSE
voltage higher than 2.7 V will immediately block the gate signal. After bulk voltage falls below the rated
value, gate drive resumes switching again.
3.3.3
Peak current limit
The IC provides a cycle by cycle peak current limitation (PCL). It is active when the voltage at pin ISENSE
reaches -0.2 V. This voltage is amplified by a factor of -5 and connected to comparator with a reference
voltage of 1.0 V. A deglitcher with 200 ns after the comparator improves noise immunity to the activation of
this protection. In other words, the current sense resistor should be designed lower than -0.2 V PCL for
normal operation.
3.3.4
IC supply under voltage lockout
When VCC voltage is below the under voltage lockout threshold VCC,UVLO, typical 11 V, IC is off and the gate
drive is internally pull low to maintain the off state. The current consumption is down to 1.4 mA only.
3.3.5
Bulk voltage monitor and enable function (VBTHL_EN)
The IC monitors the bulk voltage status through VSENSE pin and output a TTL signal to enable PWM IC or
control inrush relay. During soft-start once the bulk voltage is higher than 95% rated value, pin VB_OK
outputs a high level. The threshold to trigger the low level is decided by the pin VBTHL voltage adjustable
externally.
When pin VBTHL is pulled down externally lower than 0.5 V most function blocks are turned off and the IC
enters into standby mode for low power consumption. When the disable signal is released the IC recovers by
soft-start.

## [стр. 19]

PFC  boost converter design guide
Application Note
19
Revision1.1, 2016-02-22
Design Note DN 2013-01
V1.0 January 2013

Efficiency and power losses modeling
4
The design example discussed in this document was modeled in Mathcad®. All of the power losses equations
were written as a function of the output power in order to be able to plot an estimated efficiency curve
across the output power range as shown in Figure 19.

Figure 19
Calculated efficiency @ 85VAC  vs experimental efficiency @ 90VAC
Figure 20 shows a breakdown of main power losses at the full load of both low and high line conditions.


Figure 20
Breakdown of main power losses
Figure 21 shows the simulated and experimental inductor current at the low line full load condition.
Figure 21
Simulated and experimental Inductor current waveforms at low-line full load condition
MOSFET
losses
26%
Boost
diode
losses
7%
Inductor
losses
20%
Rectifier
bridge loss
34%
Output
capacitor
loss
13%
85Vac 100% load
Total power loss = 74.1W
MOSFET
losses
16%
Boost
diode
losses
20%
Inductor
losses
18%
Rectifier
bridge
loss
37%
Output
capacitor
loss
9%
230Vac 100% load
Total power loss = 25.3W

## [стр. 20]

PFC  boost converter design guide
Application Note
20
Revision1.1, 2016-02-22
Design Note DN 2013-01
V1.0 January 2013

Experimental results
5


Figure 22
Evaluation board
All test conditions are based on 60°C heat sink temperature.
5.1
Load and line measurement data
The test data of the evaluation board under different test conditions are listed in Table 2. The corresponding
efficiency waveforms are shown in Figure 23 and Figure 24.

Efficiency test data with IPZ65R045C7 & IDH12G65C5 @ 100kHz , Rg= 1.8 Ω
Table 2
Input
VIN
[V]
IIN
[A]
PIN
[W]
UOUT
[V]
IOUT
[A]
POUT
[W]
Efficiency
[%]
Power
factor
90 VAC
88.88
14.3962
1278.5
402.05
2.984
1200.02
93.829
0.9996
89.11
10.8743
968.8
402.09
2.282
917.68
94.719
0.9997
89.33
8.0877
722.4
402.12
1.711
688.38
95.290
0.9998
89.51
5.3667
480.2
402.15
1.141
459.05
95.597
0.9996
89.74
2.6953
241.5
402.18
0.571
229.82
95.161
0.9984
230 VAC
229.5
5.3365
1222.1
402.03
2.985
1200.01
98.186
0.9976
229.6
4.431
1014.9
402.06
2.479
996.66
98.198
0.9975
229.7
3.3171
758.7
402.10
1.852
744.59
98.138
0.9956
229.8
2.2298
508.8
402.12
1.239
498.18
97.910
0.9929
229.9
1.1304
253.4
402.16
0.612
246.15
97.120
0.9752

## [стр. 21]

PFC  boost converter design guide
Application Note
21
Revision1.1, 2016-02-22
Design Note DN 2013-01
V1.0 January 2013

Figure 23
High-line efficiency with IPZ65R045C7 & IDH12G65C5 @ 100kHz, Rg= 1.8 Ω

Figure 24
Low-line efficiency with IPZ65R045C7 & IDH12G65C5 @ 100kHz, Rg= 1.8 Ω
5.2
Conductive EMI test
Compliance with EN55022 standard is a very important quality factor for a power supply. The EMI has to
consider the whole SMPS and is split into radiated and conductive EMI consideration. For the described
evaluation PFC board it is most important to investigate on the conducted EMI-behavior since it is the input
stage of any SMPS below a certain power range, as shown in Figure 25.

## [стр. 22]

PFC  boost converter design guide
Application Note
22
Revision1.1, 2016-02-22
Design Note DN 2013-01
V1.0 January 2013

Figure 25
Conductive EMI  measurement of the board with resistive load
5.3
Startup behavior
During power up when the VOUT is less than 96% of the rated level, internal voltage loop output increases
from initial voltage under the soft-start control. This results in a controlled linear increase of the input
current from 0 A thus reducing the current stress in the power components as can be seen on the yellow
waveform in Figure 26.

Figure 26
Waveform capture during low-line startup

## [стр. 23]

PFC  boost converter design guide
Application Note
23
Revision1.1, 2016-02-22
Design Note DN 2013-01
V1.0 January 2013

Board design
6
6.1
Schematics


Figure 27
Evaluation board schematic

## [стр. 24]

PFC  boost converter design guide
Application Note
24
Revision1.1, 2016-02-22
Design Note DN 2013-01
V1.0 January 2013
6.2
PCB layout


Figure 28
PCB top layer view


Figure 29
PCB bottom layer view

## [стр. 25]

PFC  boost converter design guide
Application Note
25
Revision1.1, 2016-02-22
Design Note DN 2013-01
V1.0 January 2013
6.3
Bill of material
Table 3
Bill of material
Designator
Value
Description
B1, B2
closed with 0 Ω
Placeholder for Ferrite Bead, 0 Ω resistor
Bias1
12 V Bias
Bias adapter
C1
10 µ
25 V
C2
4n7
25 V
C3
10 n
25 V
C4, C5
1 µ
x-capacitor
C6
4.7 n
25 V
C7
10 n
25 V
C8, C30
100n500 V
VJ1825Y104KXEAT
C10, C31
1 n
25 V
C11
10 µ
25 V
C12, C25, C32
100 n
25 V
C13
100 n
25 V
C14, C15
1 µ
25 V
C16
100 µ
25 V
C17, C18
1.1 n
Y-capacitor
C19, C20
3.3 n
Y-capacitor
C21, C24
560 µ
EETHC2G561KA or EKMR421VSN561MR50S
C22
1u_400 V
BFC237351105; Farnel 1215540
C23
1.5u_400 V

C26
220 n
25 V
C27
10 µ
25 V
C28
470p
25 V
C29
22n
25 V
D1
SS26

D2, D3
1N4148

D4
1N5408

D6
short
0 Ω
D10
ES1C
1 A 150 V fast diode
DUT1
IPZ65R045C7

D_Z3
ZMM15
1N4734A
EMI_1
not placed
EMI Adapter
GL1, GL2
GSIB2580
GSIB2580
IC1
TDA2030
Mount with M2.5x6
IC2
LM4040
LM4040D20IDBZRG4
IC3
ICE3PCS01G
PFC_CCM_Controller
IC4
1EDI60N12AF
6 A_isolated_MOSdriver
IC5
IFX91041
1.8A Step down switching regulator
J1, J11
Jumper_3Pin
SPC20486
J2
Current measure bridge
1.25 mm isolated copper wire
J3
Current measure bridge
U-shape-Cu-wire 1.25 mm 2 cm distance
J6
open
Solder jumper; 4 pin as 3 pin
J7, J12
close with solder
Solder jumper; driver ground to SS, Solder jumper; isolated driver power
J8, J10
open
Solder jumper; 3pin ground, Solder jumper; driver power none isolated
J9
close with solder
Solder jumper; isolated driver power
K1
SK426
100 mm long; mound with 2xM4x15
K2
KM75-1
KM75-1 +4clip 4597; Fischer
KL1
BNC
Oscilloscope_ Funtion generator
KL01
HV in
GMSTBVA 2,5 HC/ 3-G-7,62
KL01-S
Complement
GMSTB 2,5 HCV/ 3-ST-7,62
KL02
Vin_sense
GMSTBVA 2,5 HC/ 2-G-7,62
KL02-S
Complement
GMSTB 2,5 HCV/ 2-ST-7,62

## [стр. 26]

PFC  boost converter design guide
Application Note
26
Revision1.1, 2016-02-22
Design Note DN 2013-01
V1.0 January 2013
L1
L_PFC
2times 77083A7 64wind_1.15 mm
L2
10 A 100 µH
Würth 744824101
L3
8120-RC
BOURNS_8120-RC_2m4H_17 A
L4
33 µH
74454133
LED1
red
Power on LED
LED2, LED3, LED4,
LED5
blue
Power on LED
M1, M2
Fan 60mm
PMD1206PTB1-A
M1, M2
finger guard for Fan 60mm
LZ28CP
PWM-Signal
SMA
Oscilloscope_ Function generator
R1, R3, R13, R20, R56
1 k
5%
R2, R8, R15, R44
10 k
5%
R4
5 k
67WR20KLF
R5
680
5%
R6
220R
5%
R7, R11
10R
5%
R9, R16
20R
3314G-1-200E
R10, R25
47R
5%
R12, R42
330 k
5%
R14, R19
2M
5%
R17
27 k
5%
R18
36 k
5%
R21
LTO100 4R7
include two 20F2617 Bürklin connector
R22, R23
500 k
10%
R24
0R005
FCSL90R005FE
R27
np

R28
20 k
23AR20KLFTR
R29
22 k
5%
R30
1 k
10 V
R31
100 k
67WR100KLF
R35
2R
5%
R36
np

R37
np 500 k
5%
R45
200 k
5%
REL1
AZ762
12 V
REL2
G6D_1A_ASI
12 V
R_NTC1
5k
B57560G502F mound in K1 under MOS
R_NTC2
3R3
R_SL22
S1, S2, S3, S4, S5, S6
SCREW_M4
3 cm Distance holder
S1, S2, S3, S4, S5, S6
M4 Screw nut
M4 Screw nut
S1, S2, S3, S4, S5, S6
washer M4
washer M4
Vin
HV_in
GMSTBA_2.5HC_3G7.62
Vout
Vout
GMSTBA_2.5HC_2G7.62
Vout_sense
Vout_sense
GMSTBVA_2.5HC_2G7.62
X1
np (Heat sink)
thermocouple plug
X2
np (MOS1)
thermocouple plug
X3
np (Diode)
thermocouple plug
X4
np (Choke)
thermocouple plug
X5
np (MOS2)
thermocouple plug
X6
Rg_4pin
SPC20485
X7
Rg_3pin
SPC20485
X8, X9
KL_STANDARD_2
SPC20485
X12
Np
for adapter power supply

## [стр. 27]

PFC  boost converter design guide
Application Note
27
Revision1.1, 2016-02-22
Design Note DN 2013-01
V1.0 January 2013

References
7
 F. Stueckler, E. Vecino, Infineon Technologies Application Note: "Coo lMOSTM C7 650V Switch in a Kelvin
[1]
Source Configuration". May 2013.
http://www.infineon.com/dgdl/Infineon+-+Application+Note+-+TO-247-4pin+-+650V+CoolMOS™
+C7+Switch+in+a+Kelvin+Source+Configuration.pdf?folderId=db3a304333b8a7ca0133c6bec0956188&fi
leId=db3a30433e5a5024013e6a9908a26410
 J. Hancock, F. Stueckler, E. Vecino, Infineon Technologies Application Note: "CoolMOS™ C7 : Mastering
[2]
the Art of Quickness". April 2013.
http://www.infineon.com/dgdl/Infineon+-+Application+Note+-+650V+CoolMOS™ +C7+-
+Mastering+the+Art+of+Quickness.pdf?folderId=db3a304333b8a7ca0133c6bec0956188&fileId=db3a30
433e5a5024013e6a966779640b
 ICE3PCS01G controller datasheet.
[3]
http://www.infineon.com/dgdl/Infineon-ICE3PCS01-DS-v02_00en.pdf?folderId=5546d4694909da4801490a07012f053b&fileId=db3a304329a0f6ee0129a67ae8c02b46
 Power Factor Correction (PFC) Parts Selection Guide
[4]
http://www.infineon.com/dgdl/Infineon+-+Selection+Guide+-+PFC+-+Power+Factor+Correction+-
+CoolMOS™ +-+SiC+Diodes+-
+Controllers.pdf?folderId=db3a30433e5a5024013e6a288c8f6352&fileId=db3a30433e5a5024013e6a35c
b806364

## [стр. 28]

PFC  boost converter design guide
Application Note
28
Revision1.1, 2016-02-22
Design Note DN 2013-01
V1.0 January 2013

Symbols used in formulas
8
Table 4
Symbols used in formulas
Vac
Input voltage
Vac.min
Minimum input voltage
Vo
Output voltage
Po
Output power
f
Switching frequency
T
Switching time period
fline
line frequency
L
Filter inductor
%Ripple
Inductor current ripple percentage to input current
DCR
Inductor DC resistance
Iin.rms
Input rms current
IL.rms
Inductor rms current
IL.avg
Inductor average current across the line cycle
IL.pk
Inductor peak current
PL.cond
Inductor conduction loss
Vf.bridge
Bridge diode forward voltage drop
Pbridge
Bridge power loss
Ron(100C)
MOSFET on-resistance at 100oC
Qgs
MOSFET gate-source charge
Qgd
MOSFET gate-drain charge
Qg
MOSFET total gate charge
Rg
MOSFET gate resistance
Vpl
MOSFET gate plateau voltage
Vth
MOSFET gate threshold voltage
ton
MOSFET turn-on time
toff
MOSFET turn-off time
Eoss
MOSFET output capacitance switching energy
IS.rms
MOSFET rms current over the line cycle
PS.cond
MOSFET conduction loss
PS.on
MOSFET turn-on power loss
PS.off
MOSFET turn-off power loss
PS.oss
MOSFET output capacitance switching loss
PS.gate
MOSFET gate drive loss
ID.avg
Boost diode average current
Vf.diode
Boost diode forward voltage drop
Qrr
Boost diode reverse recovery charge

## [стр. 29]

PFC  boost converter design guide
Application Note
29
Revision1.1, 2016-02-22
Design Note DN 2013-01
V1.0 January 2013
Vac
Input voltage
PDcond
Boost diode conduction loss
PD.sw
Boost diode switching loss
Co
Output capacitor
ESR
Output capacitor resistance
thold
Hold-up time
Vo.mi
Hold up minimum output voltage
∆Vo
Output voltage ripple
ICo.rms
Output capacitor rms current
PCo
Output capacitor conduction loss

Revision history
Major changes since the last revision
Page or reference
Description of change
--
First release (Revision 1.0)
Figure 8-12
Corrected output power on y-Axis: 10,000(Revision 1.1.)

## [стр. 30]

Published by
Infineon Technologies AG
81726 Munich, Germany

© 2016 Infineon Technologies AG.
All Rights Reserved.

Do you have a question about any
aspect of this document?
Email: erratum@infineon.com

Document reference

Legal Disclaimer
THE INFORMATION GIVEN IN THIS APPLICATION
NOTE
(INCLUDING
BUT
NOT
LIMITED
TO
CONTENTS OF REFERENCED WEBSITES) IS GIVEN
AS A HINT FOR THE IMPLEMENTATION OF THE
INFINEON TECHNOLOGIES COMPONENT ONLY
AND SHALL NOT
BE REGARDED AS ANY
DESCRIPTION OR WARRANTY OF A CERTAIN
FUNCTIONALITY, CONDITION OR QUALITY OF THE
INFINEON TECHNOLOGIES COMPONENT. THE
RECIPIENT OF THIS APPLICATION NOTE MUST
VERIFY ANY FUNCTION DESCRIBED HEREIN IN THE
REAL APPLICATION. INFINEON TECHNOLOGIES
HEREBY DISCLAIMS ANY AND ALL WARRANTIES
AND LIABILITIES OF ANY KIND (INCLUDING
WITHOUT LIMITATION WARRANTIES OF NONINFRINGEMENT OF INTELLECTUAL PROPERTY
RIGHTS OF ANY THIRD PARTY) WITH RESPECT TO
ANY AND ALL INFORMATION GIVEN IN THIS
APPLICATION NOTE.

Information
For further information on technology, delivery terms
and conditions and prices, please contact the nearest
Infineon Technologies Office (www.infineon.com).
Warnings
Due to technical requirements, components may
contain dangerous substances. For information on
the types in question, please contact the nearest
Infineon Technologies Office. Infineon Technologies
components may be used in life-support devices or
systems only with the express written approval of
Infineon Technologies, if a failure of such components
can reasonably be expected to cause the failure of
that life-support device or system or to affect the
safety or effectiveness of that device or system. Life
support devices or systems are intended to be
implanted in the human body or to support and/or
maintain and sustain and/or protect human life. If
they fail, it is reasonable to assume that the health of
the user or other persons may be endangered.





www.infineon.com
Trademarks of Infineon Technologies AG
AURIX™, C166™, CanPAK™, CIPOS™, CoolGaN™, CoolMOS™, CoolSET™, CoolSiC™, CORECONTROL™, CROSSAVE™, DAVE™, DI-POL™, DrBlade™, EasyPIM™,
EconoBRIDGE™, EconoDUAL™, EconoPACK™, EconoPIM™, EiceDRIVER™, eupec™, FCOS™, HITFET™, HybridPACK™, Infineon™, ISOFACE™, IsoPACK™,
i-Wafer™, MIPAQ™, ModSTACK™, my-d™, NovalithIC™, OmniTune™, OPTIGA™, OptiMOS™, ORIGA™, POWERCODE™, PRIMARION™, PrimePACK™,
PrimeSTACK™, PROFET™, PRO-SIL™, RASIC™, REAL3™, ReverSave™, SatRIC™, SIEGET™, SIPMOS™, SmartLEWIS™, SOLID FLASH™, SPOC™, TEMPFET™,
thinQ!™, TRENCHSTOP™, TriCore™.
Trademarks updated August 2015
Other Trademarks
All referenced product or service names and trademarks are the property of their respective owners.
Edition 2014-11-01












AN_201409_PL52_009
