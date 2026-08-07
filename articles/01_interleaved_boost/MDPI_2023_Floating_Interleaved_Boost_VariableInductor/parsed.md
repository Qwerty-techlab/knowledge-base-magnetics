# Type of the Paper (Article

> Автоматически извлечено из `source.pdf` скриптом `parse_pdf.py`
> Движок: pymupdf. Страниц: 16 из 16.
> Дата извлечения: 2026-08-07 06:42 UTC

Текст не редактировался. Формулы и таблицы могут быть искажены —
при сомнении сверяться с исходным PDF.

---

## [стр. 1]

Technologies 2023, 11, 21. https://doi.org/10.3390/technologies11010021
www.mdpi.com/journal/technologies
Article
Floating Interleaved Boost Converter with Zero-Ripple Input
Current Using Variable Inductor
Hector Hidalgo 1, Nimrod Vázquez 2,*, Rodolfo Orosco 2, Hector Huerta-Ávila 3, Sergio Pinto 4 and Leonel Estrada 5
1 Mechatronics Department, Technological National of Mexico/Higher Technological Institute of Villa La
Venta, Huimanguillo 86410, Mexico
2 Electronics Department, Technological National of Mexico/Technological Institute of Celaya,
Celaya 38010, Mexico
3 Department of Computational Sciences and Engineering, Universidad de Guadalajara/Centro Universitario
de los Valles, Ameca 46600, Mexico
4 The "Universidad de Panama", Faculty of Informatics, Electronics and Communications, Central Campus,
Panama 0843-03561, Panama
5 Electronics Department, Technological National of Mexico/Higher Technological Institute from South of
Guanajuato, Benito Juárez 38980, Guanajuato, Mexico
* Correspondence: n.vazquez@ieee.org
Abstract: A zero-ripple input current is known to improve the lifetime of battery sets and fuel cells
and to assure maximum power point tracking in PV panels. To perform current ripple elimination
in a floating interleaved boost converter (FIBC), one of the typical linear inductors is substituted by
a variable inductor, and phases of the converter have complementary duty cycles. This variable
inductor is controlled using a switched current-source converter, which adjusts the input current
ripple. An equivalent model for the variable inductor is presented, including uncertainties in the
component description. To achieve current stabilization, a variable inductor controller was designed
using the sliding modes approach via fixed frequency. An experimental prototype is implemented
and tested with an output voltage controller to compare with the conventional FIBC. The results
demonstrate that the input current ripple of the proposed converter is eliminated without significantly decreasing the efficiency.
Keywords: DC-DC converters; floating interleaved boost converter; zero-ripple input current; variable
inductor control

1. Introduction
Environmental pollution problems have increased the use of renewable energy and
ways of transportation that do not depend on fossil fuels. Renewable energy sources with
a long lifetime are essential for the economic viability of electric vehicles and smart grid
infrastructure. One of the causes of the renewable energy sources' degradation, such as
fuel cells (FCs) and photovoltaic panels (PVs), is the input current ripple (ICR) of the dcdc converters [1,2].
To minimize the ripple in the dc-dc converters, different techniques have been proposed, such as, for example, the use of coupled inductors in a single core [3]; however,
this method has a limited voltage gain and a complex design. An alternative option with
fewer components is based on tapped inductors with a ripple cancelation network [4],
which consists of a parallel LC network that counteracts the current in the tapped inductor, achieving optimal results in eliminating the ICR for a conventional boost converter;
the main drawback is the increase in current stress in the semiconductors and an increase
in the design complexity.
Interleaved converters (ICs) have been proposed to overcome these issues and reduce the power losses in switching devices. The ICR in IC is minimized only in certain
Citation: Hidalgo, H.; Vázquez, N.;
Orosco, R.; Huerta-Á vila, H.; Pinto,
S.; Estrada, L. Floating Interleaved
Boost Converter with Zero-Ripple
Input Current Using Variable
Inductor. Technologies 2023, 11, 21.
https://doi.org/10.3390/
technologies11010021
Academic Editor: Valeri Mladenov
Received: 30 December 2022
Revised: 17 January 2023
Accepted: 21 January 2023
Published: 28 January 2023

Copyright: © 2023 by the authors.
Licensee MDPI, Basel, Switzerland.
This article is an open access article
distributed under the terms and
conditions of the Creative Commons
Attribution
(CC
BY)
license
(https://creativecommons.org/license
s/by/4.0/).

## [стр. 2]

Technologies 2023, 11, 21
2 of 16


operating points with specific switching frequencies and phase-shift [5], which is its main
drawback. This problem may be solved by using a frequency control in discontinuous
conduction mode [6]; however, the latter technique limits the voltage ratio. Moreover, an
extra double-loop controller is required to compensate for inductance variation.
Another challenge for boost converters is to achieve high voltage gain; different alternatives may be employed, including the cascade connection [7], where the main disadvantage is the losses. Recently, a floating interleaved boost converter (FIBC) has been introduced to increase the gain of conventional converters [8]. However, the main disadvantage is the zero-ripple input current in a fixed point. In [9], a current mirror technique
between phases is proposed, achieving the total elimination of the ICR demanded from
the power supply; in this case, the condition is restricted in the vicinity of the selected
operating point for two phases.
On the other hand, the current trend to improve the characteristics of power inductors has led to exploring the use of variable inductors (VIs). In [10-16], a feasibility study
is presented to integrate a VI in a dc-dc converter with a dynamic load variation, obtaining significant results in reducing the core size and the current ripple. The VI is a currentcontrolled device with low-power consumption. Moreover, this device can operate in different conduction modes. In [17], a magnetic control is presented, which takes advantage
of the inductance variation to regulate the average current in the discontinuous conduction mode. In [18], a VI is proposed to control the switching frequency in critical conduction mode. Meanwhile, the power factor is corrected via the closed-loop main boost converter.
This paper presents a zero-ripple input current FIBC using a VI, including the output
voltage control strategy. The converter offers a high boosting gain and a zero current ripple for a wider operating region. The primary function of VI is to regulate the ripple in
one of the phases to achieve a proportional mirror current, resulting in total ICR elimination independent of the operating point for two interleaved phases, which is the main
advantage over other techniques. An auxiliary winding is introduced to the magnetic core,
which is connected to a switched current-source converter (SCC). A current controller is
proposed to lead with uncertainties and parameter variations in the VI. The reference current of the current controlled auxiliary converter is obtained from the control current estimator based on the duty cycle. An experimental implementation was conducted to evaluate
the
proposal's
effectiveness
using
the
circuit
depicted
in
Figure
1.

Figure 1. Schematic diagram of FIBC with a VI and its control structure.
+
+
+
L1
L2
S4
S3
S1
S2
is
iL1
iL2
C2
C1
io
VS
+
S6
S5
ic
Vin
Lc
R
Vo
+
-
Vref
d
Ramp
+
-
C(s)
V1
V2
dc SMC
Ramp
+ Iref
1
Estimator

## [стр. 3]

Technologies 2023, 11, 21
3 of 16


This paper is organized as follows. In Section 2, the operation and analysis are conducted, including the voltage gain, dynamic modeling, and control of the main converter.
Section 3 introduces the operation principle and design method for the VI. The equivalent
model of the VI and proposed controller with a reference current estimator are provided
in Section 4. Experimental results and the corresponding analysis are described in Section
5. Finally, the paper is concluded in Section 6.
2. Main Converter Analysis
The FIBC is shown in Figure 2a. This converter is applied in FC and PV applications
to reduce the current and voltage stress in the switching devices, which substantially increases the overall efficiency of the system by reducing the ICR [19].
To increase the voltage gain, a duty cycle different from 0.5 is required. The switches
𝑆1 and 𝑆2 operate inversely to minimize the ICR owing to the summation of the currents
through each inductor. In this case, the phases present opposite slopes and complementary duty cycles, as shown in Figure 2b.

Figure 2. Two-phase FIBC when 𝐷1 = 0.7 and 𝐷2 = 0.3: (a) schematic diagram; (b) relevant waveforms.
2.1. Steady State Analysis
The elimination of the ICR is achieved by matching the current ripple in the inductors, which can be mathematically expressed using the equation:
(
)
1
2
1
s
s
V
d
V d
L f
L f
-
=
,
(1)
where 𝑓 is the switching frequency, 𝑑 is the duty cycle for the converter, 𝐿1 and 𝐿2 are the
inductances, and 𝑉𝑠 is the source voltage. After some elementary algebraic transformations, Equation (1) yields:
(
)
2
1
1
d
L
L
d
-
=
.
(2)
It follows immediately from (2) that, in order to compensate for the change in the
duty cycle 𝑑, the inductance (𝐿2) must be a variable one. According to Kirchhoff's voltage
law, the output voltage 𝑉𝑜 is given as:
1
s
s
o
s
V
V
V
V
d
d
=
+
-
-
,
(3)
hence, the static gain of the converter is:
(
)
(
)
1
1
1
o
s
d
d
V
V
d
d
-
-
=
-
.
(4)
VS
iS
iL1
iL2
VGS1
VGS2
+
+
L1
L2
S4
S3
S1
S2
is
iL1
iL2
C2
C1
io
+
Vo
+
-
R
V1
V2
(a)
(b)

## [стр. 4]

Technologies 2023, 11, 21
4 of 16


Denoting 𝑀= 𝑉𝑜𝑉𝑠
⁄
, and assuming that ICR is completely mitigated, one obtains
from (3) the value of the duty cycle:
4
1
1
1
2
M
d
+
-
+
=
.
(5)
The voltage gain 𝑀 of Equation (4) for different values of 𝑑 is shown in Figure 3.

Figure 3. Voltage gain of FIBC for different values of 𝑑.
2.2. The Dynamic Model of FIBC
According to the model presented in [9] with complementary duty cycles, under continuous conduction mode, the averaged model of the converter is:
(
)
1 1
2
1
s
L x
V
d x
=
-
-
,
(6a)
(
)
(
)
2
4
1
2
1
1
s
x
x
V
C x
d x
R
+
-
=
-
-
,
(6b)
2
3
4
s
L x
V
dx
=
-
,
(6c)
(
)
2
4
2
4
3
s
x
x
V
C x
dx
R
+
-
=
-
,
(6d)
where the state variable 𝑥1 represents the average inductor current (𝑖𝐿1), 𝑥2 represents the
average capacitor voltage (𝑉1), 𝑥3 represents the average inductor current (𝑖𝐿2), and 𝑥4 represents the average capacitor voltage (𝑉2). The components 𝐿1, 𝐿2, 𝐶1, 𝐶2, and 𝑅 represent
the inductors, capacitors, and load resistor, respectively.
Setting to zero, the relevant derivatives in (6) yields:
(
)
(
)
2
4
1
1
s
x
x
V
x
R
d
+
-
=
-
,
(7a)
(
)
1
2
1
s
V
y
x
d
=
=
-
,
(7b)
(
)
2
4
3
s
x
x
V
x
Rd
+
-
=
,
(7c)
2
4
s
V
y
x
d
=
=
,
(7d)
from Equation (7), one may obtain the equilibrium point.
From Equation (6), the linearization of the average model, around the desired equilibrium point (𝑥̅1, 𝑥̅2, 𝑥̅3, 𝑥̅4, 𝑑̅), yields the following state equations:
𝑥̃̇ = 𝐀𝑥̃ + 𝐁𝑑̃,
𝑦̃ = 𝐂𝑥̃,
(8)

## [стр. 5]

Technologies 2023, 11, 21
5 of 16


with 𝑥̃ = [𝑥̃1 𝑥̃2 𝑥̃3 𝑥̃4]𝑇, 𝑥̃1 = 𝑥1 -𝑥̅1 , 𝑦̃1 = 𝑥̃2 = 𝑥2 -𝑥̅2 , 𝑥̃3 = 𝑥3 -𝑥̅3 , 𝑦̃2 = 𝑥̃4 = 𝑥4 -𝑥̅4 ,
𝑑̃ = 𝑑-𝑑̅ and 𝑦̃ = [𝑦̃1 𝑦̃2]𝑇= 𝑦-𝑦̅, where the superscript (~) represents the linearized
signal. The system matrix is given by:
1
1
1
1
2
2
2
2
(1
)
0
0
0
(1
)
1
1
0
0
0
0
1
1
0
d
L
d
C
RC
RC
d
L
d
RC
C
RC


-
-






-


-
-


= 



-






-
-




A
.
(9)
While the input matrix is given by:
𝐁= [𝑥2
𝐿1
-𝑥1
𝐶1
-𝑥4
𝐿2
𝑥3
𝐶2
]
𝑇
.
(10)
In the case of the output matrix:
𝐂= [0
1
0
0
0
0
0
1].
(11)
The matrix transfer function corresponding to the state Equation (8) is:
𝐺(𝑠) = 𝐂(𝑠𝑰-𝐀)-1𝐁.
(12)
Expression (12) can be developed into
[
𝐺1(𝑠) =
𝑥̃2
𝑑̃
𝐺2(𝑠) =
𝑥̃4
𝑑̃
] =
3
2
10
11
12
13
4
3
2
1
2
3
4
3
2
20
21
22
23
4
3
2
1
2
3
4
0
b s
b s
b s
b
s
a s
a s
a s
a
b s
b s
b s
b
s
a s
a s
a s
a


+
+
+


+
+
+
+






+
+
+




+
+
+
+


,
(13)
where the numerator coefficients of Equation (13) are:
𝑏10 = -𝑥̅1
𝐶1
; 𝑏11 = 𝑥̅2(1 -𝑢̅)
𝐿1𝐶1
-𝑥̅1 + 𝑥̅3
𝑅𝐶1𝐶2
;
𝑏12 = 𝑥̅4𝐿1𝑢̅ + 𝑥̅2𝐿2(1 -𝑢̅)
𝑅𝐿1𝐶1𝐿2𝐶2
-𝑥̅1𝑢̅2
𝐿2𝐶1𝐶2
; 𝑏13
= 𝑥̅2𝑢̅2(1 -𝑢̅)
𝐿1𝐶1𝐿2𝐶2
;
𝑏20 = 𝑥̅3
𝐶2
; 𝑏21 = (𝑥̅1 + 𝑥̅3)
𝑅𝐶1𝐶2
-𝑥̅4𝑢̅
𝐿2𝐶2
;
𝑏22 = -
1
𝑅𝐶1𝐶2
(𝑥̅4𝑢̅
𝐿2
+ 𝑥̅2(1 -𝑢̅)
𝐿1
) + 𝑥̅3(𝑢̅2 -2𝑢̅ + 1)
𝐿1𝐶1𝐶2
;
𝑏23 = 𝑥̅4(𝑢̅3 -2𝑢̅2 + 𝑢̅)
𝐿1𝐶1𝐿2𝐶2
.
and the denominator coefficients of Equation (13) are:
𝑎1 = 𝐶1 + 𝐶2
𝑅𝐶1𝐶2
; 𝑎2 = 𝐿1𝐶1𝑢̅2 + 𝐿2𝐶2(1 -𝑢̅)2
𝐿1𝐶1𝐿2𝐶2
;
𝑎3 = 𝐿1𝑢̅2 + 𝐿2(1 -𝑢̅)2
𝑅𝐿1𝐶1𝐿2𝐶2
; 𝑎4 = 𝑢̅2(1 -𝑢̅)2
𝐿1𝐶1𝐿2𝐶2
.

## [стр. 6]

Technologies 2023, 11, 21
6 of 16


2.3. Output Voltage Control
In this system, it is possible to control both capacitor voltages with only one controller. The different dynamic transfer functions from (13) are added to obtain the relation
between the input 𝑑̃ and output 𝑉̃𝑜. Considering 𝑉𝑠 as a perturbation, this yields:
𝐺𝑣(𝑠) = 𝑉̃𝑜
𝑑̃ =
𝑏1𝑠3 + 𝑏2𝑠2 + 𝑏3𝑠+ 𝑏4
𝑠4 + 𝑎1𝑠3 + 𝑎2𝑠2 + 𝑎3𝑠+ 𝑎4
,
(14)
where 𝑏1 = 𝑏10 + 𝑏20, 𝑏2 = 𝑏11 + 𝑏21, 𝑏3 = 𝑏12 + 𝑏22 and 𝑏4 = 𝑏13 + 𝑏23.
The inductance variation of 𝐿2 produces an interval plant and is considered for controller design, with 𝐿2
- as a minimum inductance and 𝐿2
+ as a maximum inductance. Expression (14) is defined as a set of transfer functions achieved using:
𝐺𝑣(𝑠, 𝑏, 𝑎) = 𝑁(𝑠, 𝑏)
𝐷(𝑠, 𝑎) = ∑
𝑏𝑖𝑠𝑖
𝑚
𝑖=0
∑
𝑎𝑖𝑠𝑖
𝑛
𝑖=0
,
(15)
and coefficients are supposed to vary within the following bounds:
𝑏𝑖
-≤𝑏𝑖≤𝑏𝑖
+, 𝑖= 0, 1, … , 𝑚,
𝑎𝑖
-≤𝑎𝑖≤𝑎𝑖
+, 𝑖= 0, 1, … , 𝑛,
(16)
where 𝑏𝑖
- represents the minimum numerator coefficient, 𝑏𝑖
+ represents the maximum
numerator coefficient, 𝑎𝑖
- represents the minimum denominator coefficient, and 𝑎𝑖
+ represents the maximum denominator coefficient.
A first-order controller is needed with an acceptable range, which robustly stabilizes
the trajectories of the closed-loop system, under parameter variations, around a region
defined by the interval plant. The output voltage controller is chosen as a proportionalintegral controller as follows:
( )
i
p
K
K s
C s
s
+
=
,
(17)
where 𝐾𝑝 is the proportional gain and 𝐾𝑖 is the integral gain.
The characteristic equation for a closed-loop system is expressed as follows:
𝑃(𝑠, 𝐶) = 1 + C(𝑠)𝐺𝑣(𝑠, 𝑏, 𝑎).
(18)
Using (18), the transfer function (15) is evaluated with a uniform distribution of interval 𝐿2ϵ[𝐿2
-, 𝐿2
+]. The stability of these polynomials can be tested via Routh-Hurwitz
test. The stability condition must be fulfilled for all transfer functions-in this case, the
number selected is ten. This proof generates an area of the acceptable range of controller
parameters (𝐾𝑝, 𝐾𝑖> 0) that robustly stabilize the interval plant, as depicted in Figure 4.
The closed-loop Bode diagram for the linear control system of the plant model (15)
with the controller designed is shown in Figure 5. The crossover frequency is 561 Hz. The
phase margin is ranged from 37.6° to 40.1° and the gain margin ranged from 7.73 dB to
9.11 dB.

Figure 4. Acceptable proportional and integral gains; the red dot represents the selected controller
parameters.

## [стр. 7]

Technologies 2023, 11, 21
7 of 16



Figure 5. Bode diagram of closed-loop transfer functions for uniform distributed parameter 𝐿2.
3. Variable Inductor Operation and Design
The VI based on a double E-core contains a control winding and the main winding.
The principle of operation is based on the variation of the main winding inductance
through the control of the flux created by the control winding. The reluctance model and
design algorithms have been reported in the literature [20,21].
Figure 6a shows a schematic representation of the windings for practical implementation. Figure 6b illustrates the operating points on the B-H curve.

Figure 6. Complete VI model: (a) winding distribution; (b) operating points on B-H curve.
The reluctance model depicted in Figure 7 is required to determine the appropriate
characteristics and paths of VI.
The inductance will vary between points A and B, according to Figure 5. Point A
starts after the linear region; point B reaches the value before the core saturation. Point A
has the minimum current ripple when ΔiL2 = ΔiL2_min, having a control current ic = 0; thus,
the main inductance is maximum L2 = Lmax.
Nc
Linear
Transition
Saturation
H
B
ic=0
ic_max
ΔiL2_min
ΔiL2_max
ic
NL2
Nc
L2
iL2
Air gap
A
B
(a)
(b)

## [стр. 8]

Technologies 2023, 11, 21
8 of 16



Figure 7. Reluctance model of VI.
The maximum inductance can be obtained with [21]:
(
)
2
2
1
2
3
2
L
max
g
N
L
=
+
+
+
,
(19)
where ℛ𝑔, ℛ1, ℛ2, and ℛ3 are the equivalent reluctances values of the gap, center arm, left
arm, and right arm, respectively, and 𝑁𝐿2 is the main winding number of turns.
The final state reaches point B when the current ripple is maximum ΔiL2 = ΔiL2_max, and
the current is maximum ic = ic_max; therefore, the main inductance is minimum L2 = Lmin.
Control winding 𝑁𝑐 creates a magnetic saturation along the flux path of the left and right
arms. Then, the reluctance ℛ2 and ℛ3 must be replaced with ℛ2𝑠𝑎𝑡 and ℛ3𝑠𝑎𝑡. The length
of the saturated area in the core is associated with the values provided by the manufacturer, as shown in Figure 8.

Figure 8. Dimensions of magnetic E-core for modified reluctance calculation.
The calculation of the equivalent reluctance for the saturated condition is necessary
to determine the length of the saturated region, as follows [21]:
3
2
3
1
2
2
16
2
8
sat
w
w
w
w
w
L
-
-
=
+
+
,
(20)
1
2
3
2
4
sat
a
a
L
a
-
=
+
,
(21)
where 𝑤𝑖 and 𝑎𝑖 are the length values provided by the manufacturer. The equivalent reluctance for saturation condition ℛ2𝑠𝑎𝑡 and ℛ3𝑠𝑎𝑡 can be calculated as:
,
2, 3
isat
isat
ds
i
l
i
A

=
=

(22)
where 𝑙𝑖𝑠𝑎𝑡 is the length of the magnetic path 𝑖, 𝜇𝑑𝑠 is the value of the differential permeability for the saturation condition, and 𝐴𝑖 is the cross-section of the path. The properties of






 g
NL2iL2




a1
a2
w1
w3w2

## [стр. 9]

Technologies 2023, 11, 21
9 of 16


the magnetic materials are illustrated in B-H curves, where the permeability for each reluctance is obtained; then, the equations are achieved using:
𝜇𝑑= lim
𝐻→0
𝐵
𝐻,
(23)
𝜇𝑑𝑠= 𝑑𝐵𝑠𝑎𝑡
𝑑𝐻𝑠𝑎𝑡
.
(24)
Equation (23) is the slope of the linear region, which is required to estimate the reluctance in (19). Considering (20)-(24), the minimum inductance can be obtained as:
(
)
2
2
1
2
3
2
L
min
g
sat
sat
N
L
=
+
+
+
,
(25)
Flux density must be limited to guarantee that the VI does not operate in the saturation region. Thus, the following condition must be fulfilled [22]:
𝐵𝑚𝑎𝑥≤𝐵𝑠𝑎𝑡.
(26)
From (26), the maximum peak current iL2_max can be calculated as:
2
2
0.3
m
total
c
sat
L
ax
L
A B
i
N

,
(27)
where ℛ𝑡𝑜𝑡𝑎𝑙 is the denominator of (19), 𝐴𝑐 is the cross-section of the center arm, and 𝐵𝑠𝑎𝑡
is the saturation flux density. If Equation (27) cannot be fulfilled, a bigger core must be
selected. Furthermore, the control winding number of turns is achieved using:
𝑁𝑐= 2𝐻𝑠𝑎𝑡(𝑙2 + 𝑙3)
𝑖𝑐𝑚𝑎𝑥
,
(28)
where 𝐻𝑠𝑎𝑡 is the saturation magnetic field and 𝑙2 and 𝑙3 are the magnetic paths of the right
arm and left arm, respectively.
4. Current Controller and Reference Estimator
4.1. Current Controller for VI
The VI, in general, suffers from two main uncertainties. The first is the parameter
variations, where the inductance changes due to the current of the main converter and
auxiliary SCC. The temperature effect is the second important source of uncertainty and
is typically unknown.
The dynamic model of VI with uncertainties is written as:
𝑑𝑖𝑐
𝑑𝑡= -𝑅𝑐
𝐿𝑐
𝑖𝑐+ 𝑉𝑖𝑛
𝐿𝑐
𝑑𝑐+ 𝑔(𝑖𝑐, 𝑡),
(29)
where 𝑖𝑐, 𝐿𝑐, and 𝑅𝑐 are the control current, inductance, and resistance of the control inductor, respectively, 𝑔(𝑖𝑐, 𝑡) is the perturbation term that contains parameter variations
and external disturbances, 𝑉𝑖𝑛 is the voltage input of switching current-source converter,
and 𝑑𝑐 is the control input.
The perturbation term 𝑔(𝑖𝑐, 𝑡) is unknown but bounded. Moreover, consider that
𝑔(𝑖𝑐, 𝑡) satisfies the matching condition [23], that is:
𝑔(𝑖𝑐, 𝑡) = 𝑉𝑖𝑛
𝐿𝑐
𝑔̅(𝑖𝑐, 𝑡).
(30)
From (29) and (30), the dynamic model of VI can be expressed as follows:
𝑑𝑖𝑐
𝑑𝑡= -𝑅𝑐
𝐿𝑐
𝑖𝑐+ 𝑉𝑖𝑛
𝐿𝑐
(𝑑𝑐+ 𝑔̅(𝑖𝑐, 𝑡)).
(31)
The norm of perturbation term 𝑔(𝑖𝑐, 𝑡) is calculated considering a Lipschitz condition, that is:
‖ 𝑔(𝑖𝑐, 𝑡)‖ ≤𝑅𝑐
𝐿𝑐
.
(32)
A sliding mode controller (SMC) via fixed-frequency 𝑓𝑐 is proposed to add robustness under uncertainties. Considering 𝑖𝑟𝑒𝑓 as the current reference, a sliding surface can
be written as:
𝑠= 𝑖𝑐-𝑖𝑟𝑒𝑓.
(33)

## [стр. 10]

Technologies 2023, 11, 21
10 of 16


In order to drive the sliding surface (33) to zero, the following reaching law is proposed:
𝑠𝑠̇ = -η|𝑠|,
η > 0.
(34)
Substituting the time derivative of (33) into (34) to stabilize the system (31) and regulate the current 𝑖𝑐= 𝑖𝑟𝑒𝑓, the control input is selected as:
𝑑𝑐= 𝐿𝑐
𝑉𝑖𝑛
(𝑅𝑐
𝐿𝑐
𝑖𝑐-η𝑠𝑖𝑔𝑛(𝑠)).
(35)
Under the condition η > 𝑔(𝑖𝑐, 𝑡), Equation (34) is negative and the surface (33) converges to zero in a finite time [23].
4.2. Reference Estimator
The current reference estimator is determined from a series of tests. For several average current levels of 𝑖𝐿2 in the main winding, the control current 𝑖𝑐 is varied in steps of 5
mA until a minimum ICR in 𝑖𝑠 is noticed for each duty cycle. The effect of 𝑖𝐿2 on inductance is not significant for this converter since the current variation of the variable inductor
phase is less than 500 mA.
Figure 9 demonstrates the characteristics of the inductance curve as a function of the
DC control current. As can be observed, the inductance value is inversely proportional to
the control current.
A linear approximation can be used to relate the control current and inductance 𝐿2
over a specified span as follows:
𝐿2 = 𝐿1 -∆𝐿2
∆𝑖𝑐
(𝑖𝑐-𝑖𝑐_𝑚𝑖𝑛).
(36)
where ∆𝐿2 is the change in the value of 𝐿2, ∆𝑖𝑐 is the change in the value of 𝑖𝑐, and 𝑖𝑐_𝑚𝑖𝑛 is
the minimum control current. Considering Equation (2), when 𝑖𝑐= 𝑖𝑟𝑒𝑓 with 𝑖𝑟𝑒𝑓 as the
reference current, that is:
𝑖𝑟𝑒𝑓= 𝑖𝑐_𝑚𝑖𝑛-∆𝑖𝑐
∆𝐿2
𝐿1 (1 -2𝑑
𝑑
).
(37)

Figure 9. Characteristic inductance curve.
5. Experimental Results
A prototype of FIBC and VI was implemented to validate the proposed zero-ripple
input current method (Figure 10). The specifications of the prototype are shown in Table
1. The controllers were implemented using a CompactRIO embedded system with an NI
cRIO-9067 chassis, NI 9223 analog input module, and NI 9401 digital output module.


∆𝐿2
∆𝑖𝑐

## [стр. 11]

Technologies 2023, 11, 21
11 of 16


Table 1. Specifications of the prototype.
Parameter-Component
Value and Information
Rated power
100 W
FIBC frequency 𝑓
SCC frequency 𝑓𝑐
Input voltage 𝑉𝑠/𝑉𝑖𝑛
MOSFET 𝑆1
MOSFET 𝑆2
MOSFET 𝑆5
Diode 𝑆3, 𝑆4 and 𝑆6
Film capacitor 𝐶1
Film capacitor 𝐶2
Inductor 𝐿1
Variable inductor 𝐿2
40 kHz
20 kHz
48 V/12V
C3M0065090D
C2M0160120D
IRF640
MUR1560G
15 μF, 600 V, ESR 4 mΩ
15 μF, 600 V, ESR 4 mΩ
860 μH, 6A, ESR 215 mΩ
200-860 μH, 2.6A, ESR 175 mΩ
The VI was implemented in an ETD 59/31/22 E-core with 3C90 magnetic material,
𝑁𝐿2 = 43, 𝑁𝑐 = 185. A first test was performed to measure the control inductance 𝐿𝑐 using a
Hewlett Packard 4263B LCR meter. In this case, the main current 𝑖𝐿2 = 0, for which 𝐿𝑐 presents an average value of 120 mH and ESR of 3.2 Ω. The current controller was set up and
incorporated these parameters and the controller gain η = 15.
Once the VI controller was finished, the test was carried out with the main converter
in an open/closed loop. Two tests are made in an open loop: 300 Ω constant output load
and 150 V constant output voltage 𝑉𝑜. In the case of a closed loop, two types of tests are
made: change of load from half load to full load and change of input voltage 𝑉𝑠.

Figure 10. Experimental prototype.
5.1. Main Converter Open-Loop Test
Figure 11 shows the current of inductors in the traditional duty cycle 𝑑=0.5 for twophase interleaved converters when the output load was 300 Ω and zero-ripple input current occurs naturally. It can be observed that the current ripple ∆𝑖𝐿2 of the VI is distorted
due to many reasons: the core is forced to operate within the limits of the linear and transitions regions when 𝑖𝑐 = 0, but also within the unbalance of the winding arms, which has
an impact on the magnetic reluctance and parasites and the parasitic capacitance of the
windings in high frequency [24]. A small film capacitor can be added to remove the residual ICR in the case of L_1 parameter deviation.

## [стр. 12]

Technologies 2023, 11, 21
12 of 16



Figure 11. Traditional duty cycle 𝑑 = 0.5.
In Figure 12a, the duty cycle is set to d = 0.7; the ICR presents a deviation compared
to the operation with d = 0.5. There is a high ICR, in this case, since the inductances are
different. The average currents of the inductors are i_L1 = 2 A and i_L2 = 1 A, and the
current ripple distortion is maintained.
Figure 12b shows that the ICR for both inductors are now different; however, the
current ripple with the same magnitude, and then a zero-ripple input current, occurs with
the corresponding control current (𝑖𝑐 = 395 mA). The signal waveform behavior depicted
in Figure 2 is therefore confirmed. The current ripple distortion is slightly noticeable, and
the duty cycle is kept.

Figure 12. Waveforms of currents/voltage of open loop tests: (a) ICR presence at 𝑑 = 0.7; (b) zeroripple input current at 𝑑 = 0.7.
The transient state waveform of the VI current ripple is shown in Figure 13. The control current of the inductor 𝑖𝑐 is changed from 0 to 395 mA. The ICR changes from ∆𝑖𝐿2 =
0.7 A to zero-ripple, and the transient response is about 8 ms with asymptotic behavior.
This characteristic behavior is required with the closed-loop main converter when this
variation represents a negligible disturbance. As observed, the inductor current ∆𝑖𝐿1 and
output voltage 𝑉𝑜 are not affected by increased ∆𝑖𝐿2. Larger the value of η the faster the

## [стр. 13]

Technologies 2023, 11, 21
13 of 16


trajectory converges to the sliding surface. The closed-loop response of VI should be faster
than the transient response of the main converter to guarantee stability.

Figure 13. Ripple current in a steady state.
A comparison of the measured efficiency with different output powers is depicted in
Figure 14. The efficiency values presented were all measured using the Chroma 62204
power meter, 48 V nominal input voltage 𝑉𝑠, and 150 V nominal output voltage 𝑉𝑜. The
converter efficiency with the zero-ripple input current presents a similar trajectory with a
maximum difference of 0.92 %, including the VI power consumption. The efficiency of the
proposed converter-rated power is 94.47%, which is 0.24% less than conventional. The
maximum control current in this test is 𝑖𝑐 = 280 mA at 50W. The efficiency decrease is due
to power losses in the SCC and conduction loss in the auxiliary winding of the VI.
Knowledge of these power losses is necessary to evaluate the conversion efficiency of the
system. The losses of the inductor 𝐿2 and the diodes strongly influence the total efficiency
of the converter. The effect of the capacitor series resistance is negligible for the voltage
gain factor. The efficiency of the phases is expected to be different compared to the conventional FIBC.

Figure 14. Efficiency comparison.
87
88
89
90
91
92
93
94
95
96
0
20
40
60
80
100
120
Efficiency (%)
Output  Power (W)
Conventional
Proposed

## [стр. 14]

Technologies 2023, 11, 21
14 of 16


5.2. Main Converter Closed-Loop Test
The dynamic response of FIBC under the action of a robust PI controller is shown in
Figure 15 when the output load is changed from half load to full load and the reference
voltage is 150 V. As can be observed, variation in the inductance parameter value 𝐿2 does
not cause a significant change in performance or stability. Additionally, according to the
load step test, one can conclude that the zero-ripple input current in the transient response
is maintained. The settling time is about 2 ms, which is a good response for boosting converters with high gain, and the voltage overshoot is 8 V.

Figure 15. Transient response under load changes.
The controller is tested under input voltage change from 48 V to 43 V and vice versa
(Figure 16). A fast dynamic response is observed, and the zero-current ripple is maintained all the time, even at different operating points, which is the main advantage of the
proposal. The dynamic response is about 60 ms, and the voltage overshoot and voltage
drop are within 13 V. In summary, the dynamic experiment shows that the proposed converter has strong robustness under the PI control strategy, which is beneficial to ensure
the stable output of the power source.

Figure 16. Transient response under input voltage change.

## [стр. 15]

Technologies 2023, 11, 21
15 of 16


6. Conclusions
In this paper, a zero-ripple input current FIBC using a VI has been introduced. The
inductance variation is fast and its effect is reflected in the main converter as a negligible
disturbance. The converter presents a wide operating region without affecting the zeroripple condition. The interval plant model stability is verified via Routh-Hurwitz. The PI
controller is designed under parameter variation of inductance. The dynamical behavior
of the converter permits the use of only one voltage controller. Only one magnetic component is used to achieve the power transfer and zero-ripple. The main converter and the
SCC are galvanically isolated. Different voltage supplies can be used for the current regulation of the VI. A dynamic model has been developed which describes the behavior of
a VI, including uncertainties. Experimental results of the proposed SCC revealed that a
simple current control loop is employed to adjust the inductance, and that the efficiency
of the main converter is not significantly decreased. Operating at the rated 100 W power,
the proposed converter achieved 94.47% efficiency. The current controller offers remarkable accuracy, robustness, low computational load, and easy tuning for implementation.
The proposed reference estimator determines the amount of auxiliary winding current
based on the main duty cycle levels. The introduced converter is suitable for renewable
sources where a lower ripple is demanded. Future research will focus on the experimental
validation of the proposed estimator with a large‐scale VI‐based DC-DC converter with
variable load.
Author Contributions: Conceptualization, H.H. and N.V.; Investigation, H.H.; Methodology, N.V.
and H.H.; Supervision, N.V., R.O., H.H.Á . and S.P.; Writing-original draft, H.H.; Writing-review
and editing, N.V., S.P. and L.E. All authors have read and agreed to the published version of the
manuscript.
Funding: This work was sponsored by TecNM.
Data Availability Statement: Data is contained in the paper.
Conflicts of Interest: The authors declare no conflict of interest.
References
1.
Elkhateb, A.; Rahim, N.A.; Selvaraj, J.; Williams, B.W. DC-to-DC Converter With Low Input Current Ripple for Maximum Photovoltaic Power Extraction. IEEE Trans. Ind. Electron. 2015, 62, 2246-2256. https://doi.org/10.1109/TIE.2014.2383999.
2.
Lu, N.; Yang, S.; Tang, Y. Ripple Current Reduction for Fuel-Cell-Powered Single-Phase Uninterruptible Power Supplies. IEEE
Trans. Ind. Electron. 2017, 64, 6607-6617. https://doi.org/10.1109/TIE.2017.2677329.
3.
Gu, Y.; Zhang, D.; Zhao, Z. Input/Output Current Ripple Cancellation and RHP Zero Elimination in a Boost Converter Using
an Integrated Magnetic Technique. IEEE Trans. Power Electron. 2015, 30, 747-756. https://doi.org/10.1109/TPEL.2014.2307571.
4.
Yu Gu; Donglai Zhang; Zhongyang Zhao Input Current Ripple Cancellation Technique for Boost Converter Using Tapped
Inductor. IEEE Trans. Ind. Electron. 2014, 61, 5323-5333. https://doi.org/10.1109/TIE.2014.2300045.
5.
Nandankar, P.; Rothe, J.P. Design and Implementation of Efficient Three-Phase Interleaved DC-DC Converter. In Proceedings
of the 2016 International Conference on Electrical, Electronics, and Optimization Techniques (ICEEOT), Mumbai, India, 26-27
February 2016; pp. 1632-1637.
6.
Joo, D.-M.; Kim, D.-H.; Lee, B.-K. DCM Frequency Control Algorithm for Multi-Phase DC-DC Boost Converters for Input Current Ripple Reduction. J. Electr. Eng. Technol. 2015, 10, 2307-2314. https://doi.org/10.5370/JEET.2015.10.6.2307.
7.
Antares, B.; Makarim, F.H.; Ilman, S.M.; Rizqiawan, A.; Dahono, P.A. Analysis and Control of Cascade Multiphase DC-DC
Boost Converters with Very Low Input Current Ripple. In Proceedings of the 2019 2nd International Conference on High Voltage Engineering and Power Systems (ICHVEPS), Denpasar, Indonesia, 1-4 October 2019; pp. 1-6.
8.
Huangfu, Y.; Zhuo, S.; Chen, F.; Pang, S.; Zhao, D.; Gao, F. Robust Voltage Control of Floating Interleaved Boost Converter for
Fuel Cell Systems. IEEE Trans. Ind. Appl. 2018, 54, 665-674. https://doi.org/10.1109/TIA.2017.2752686.
9.
Villarreal-Hernandez, C.A.; Mayo-Maldonado, J.C.; Escobar, G.; Loranca-Coutino, J.; Valdez-Resendiz, J.E.; Rosas-Caro, J.C.
Discrete-Time Modeling and Control of Double Dual Boost Converters With Implicit Current Ripple Cancellation Over a Wide
Operating Range. IEEE Trans. Ind. Electron. 2021, 68, 5966-5977. https://doi.org/10.1109/TIE.2020.2996149.
10.
Beraki, M.; Perdigao, M.; Machado, F.; Trovao, J.P. Auxiliary Converter for Variable Inductor Control in a DC-DC Converter
Application. In Proceedings of the 2016 51st International Universities Power Engineering Conference (UPEC), Coimbra, Portugal, 6-9 September 2016; pp. 1-6.
11.
Beraki, M.W.; Trovao, J.P.F.; Perdigao, M.S.; Dubois, M.R. Variable Inductor Based Bidirectional DC-DC Converter for Electric
Vehicles. IEEE Trans. Veh. Technol. 2017, 66, 8764-8772. https://doi.org/10.1109/TVT.2017.2710262.

## [стр. 16]

Technologies 2023, 11, 21
16 of 16


12.
Beraki, M.; Trovao, J.P.; Perdigao, M. Design of Variable Inductor for Powertrain DC-DC Converter. In Proceedings of the 2019
IEEE 28th International Symposium on Industrial Electronics (ISIE), Vancouver, BC, Canada, 12-14 June 2019; pp. 822-827.
13.
Wei, Y.; Luo, Q.; Du, X.; Altin, N.; Alonso, J.M.; Mantooth, H.A. Analysis and Design of the LLC Resonant Converter With
Variable Inductor Control Based on Time-Domain Analysis. IEEE Trans. Ind. Electron. 2020, 67, 5432-5443.
https://doi.org/10.1109/TIE.2019.2934085.
14.
Babaiahgari, B.; Jeong, Y.; Park, J.-D. Stability Enhancement Method for DC Microgrids with Constant Power Loads Using
Variable Inductor. In Proceedings of the 2020 IEEE Applied Power Electronics Conference and Exposition (APEC), New Orleans, LA, USA, 15-19 March 2020; pp. 2236-2240.
15.
Mendes, A.P.; Baptista, B.; Perdigao, M.S.; Mendes, A.M.S. Experimental Analysis of a DC Current-Controlled Variable Inductor
in a DC-DC Converter. In Proceedings of the 2019 IEEE International Conference on Industrial Technology (ICIT), Melbourne,
Australia, 13-15 February 2019; pp. 440-445.
16.
Alonso, J.M.; Perdigao, M.S.; Abdelmessih, G.Z.; Dalla Costa, M.A.; Wang, Y. SPICE Modeling of Variable Inductors and Its
Application
to
Single
Inductor
LED
Driver
Design.
IEEE
Trans.
Ind.
Electron.
2017,
64,
5894-5903.
https://doi.org/10.1109/TIE.2016.2638803.
17.
Chinchero, H.; Alonso, M. Using Magnetic Control of DC-DC Converters in LED Driver Applications. IEEE Lat. Am. Trans. 2021,
19, 297-305. https://doi.org/10.1109/TLA.2021.9443072.
18.
Yao, K.; Zhang, Z.; Yang, J.; Liu, J.; Li, J.; Shao, F. Quasi-Fixed Switching Frequency Control of CRM Boost PFC Converter Based
on
Variable
Inductor
in
Wide
Input
Voltage
Range.
IEEE
Trans.
Power
Electron.
2021,
36,
1814-1827.
https://doi.org/10.1109/TPEL.2020.3007601.
19.
Zhuo, S.; Gaillard, A.; Paire, D.; Breaz, E.; Gao, F. Design and Control of a Floating Interleaved Boost DC-DC Converter for Fuel
Cell Applications. In Proceedings of the IECON 2018-44th Annual Conference of the IEEE Industrial Electronics Society, Washington, DC, USA, 21-23 October 2018; pp. 2026-2031.
20.
Alonso, J.M.; Perdigao, M.; Dalla Costa, M.A.; Zhang, S.; Wang, Y. Variable Inductor Modeling Revisited: The Analytical Approach. In Proceedings of the 2017 IEEE Energy Conversion Congress and Exposition (ECCE), Cincinnati, OH, USA, 1-5 October
2017; pp. 895-902.
21.
Saeed, S.; Garcia, J.; Perdigao, M.S.; Costa, V.S.; Baptista, B.; Mendes, A.M.S. Improved Inductance Calculation in Variable
Power Inductors by Adjustment of the Reluctance Model Through Magnetic Path Analysis. IEEE Trans. Ind. Appl. 2021, 57,
1572-1587. https://doi.org/10.1109/TIA.2020.3047593.
22.
Ferreira, S.F.S. Electromagnetic Study of a Variable Inductor Controlled by a DC Current. Master's Thesis, Universidade de
Coimbra: Coimbra, Portugal, 2016.
23.
Utkin, V.; Guldner, J.; Shi, J. Sliding Mode Control in Electro-Mechanical Systems; CRC Press: Boca Raton, FL, USA, 2017; ISBN
9781315218977.
24.
Saeed, S.; Georgious, R.; Garcia, J. Modeling of Magnetic Elements Including Losses-Application to Variable Inductor. Energies
2020, 13, 1865. https://doi.org/10.3390/en13081865.
Disclaimer/Publisher's Note: The statements, opinions and data contained in all publications are solely those of the individual author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to
people or property resulting from any ideas, methods, instructions or products referred to in the content.
