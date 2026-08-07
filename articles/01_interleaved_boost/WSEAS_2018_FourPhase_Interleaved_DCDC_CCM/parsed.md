# source

<!-- FORMULA-WARNING -->
> **Формулы в этом файле недостоверны.** Текстовый слой PDF теряет дробные черты, радикалы и группировку степеней; знак интеграла приходит как `Z` или `R`, знак суммы -- как `P`. Формул вырезано: **11**, читать их в `formulas/` (картинки 300 dpi, перечень в `formulas/INDEX.md`).
<!-- /FORMULA-WARNING -->

> Автоматически извлечено из `source.pdf` скриптом `parse_pdf.py`
> Движок: pymupdf. Страниц: 11 из 11.
> Дата извлечения: 2026-08-07 06:42 UTC

Текст не редактировался. Формулы и таблицы могут быть искажены —
при сомнении сверяться с исходным PDF.

---

## [стр. 1]

Four Phase Interleaved Boost Converter:  Theory and Applications

SLAVOMIR KASCAK, MICHAL PRAZENICA, MIRIAM JARABICOVA, ROMAN KONARIK
Department of Mechatronics and Electronics, Faculty of Electrical Engineering
University of Zilina
Univerzitna 1 010 26 Zilina
SLOVAK REPUBLIC
prazenica@fel.uniza.sk    https://www.uniza.sk


Abstract: - This paper deals with an analysis of four phase interleaved DC-DC converter for higher power
application in continuous conduction mode. The interleaved topology is widely used due to their advantage as
lower input current ripple which means volume reduction of input capacitor. The current ripple equations of an
input current for the boost operation mode and the ripple current in individual phases of the interleaved
converter using uncoupled inductor are shown. The theoretical equations are supplemented by the simulation
results using Spice simulator and by measurement on the interleaved converter.

Key-Words: - Interleaved boost converter, uncoupled inductor, simulation, measurement.

1 Introduction
Nowadays, the interleaved topologies are widely
used in various sectors of industry, ranging from
small output power to several hundred kilowatts for
their attractive features [1] - [6], [10], [13] - [15].
The interleaved topologies are frequently used
for following applications, such as an active PFC
filter
for
improvement
of
electromagnetic
compatibility [7]- [9]. The next advantage is present
in VRM application in the motherboard of a
personal computer, where the output voltage is
about 1 V, but output current is several tens of
amperes [10]. The high output current can be
divided into several channels of the multiphase
converter without using power devices with higher
current ratings, which leads to decreased power
losses. Another advantage is a high-frequency
operation for the input current, but the switching
frequency of power devices is n-times lower for the
n-channel interleaved converter. For achievement of
the same current ripple, it is possible to use smaller
inductors in comparison to classical converter but
the transient response of the interleaved will be
faster, and therefore the dynamics will be better.
The above-mentioned properties and many others
contribute to the increase of the power density [1],
[4].
The multiphase converter also has several
disadvantageous, such as more active and/or passive
components
and
complexity
of
the
control
algorithm. Currently, the microprocessors or digital
signal
controllers
are
powerful,
and
this
disadvantage is irrelevant.
Therefore, in this paper, the advantageous
features of the interleaved topology will be analysed
on four phase boost DC-DC converter. The
motivation for preparing this article is utilizing of
the converter as an interface between batteries or
supercapacitor and a inverter for an AC motor drive
system in Electric Vehicle (EV) [4], [6], [11] - [17].
This paper is divided as follows: Firstly, the
theoretical analysis is investigated for different
operational mode depending on the value of the duty
cycle. The switching interval is accordingly divided
into four intervals. In addition, the equation of the
inductor current ripple and input current ripple are
given in this part. Secondly, the simulation analysis
will be performed to compare current ripples with a
calculated value. And finally, the measured data of
the input current ripple and inductor ripple will be
given proportionally as a ratio of input current ripple
to inductor current ripple. The theoretical, simulated
and measured ratio will be plotted in a graph.
The purpose of the paper is to examine operating
mode of the converter with the lowest input current
ripple comparing to inductor currents and then
determine the proper range of duty cycle.


2 Interleaved Boost Converter
The inductor ripple currents of the four-phase
interleaved boost converter depicted in Fig. 1 are
analyzed in this section. Based on these currents is
calculated an input current ripple as a sum of them.
These characteristics are analyzed separately for
operation modes because the applied voltages
WSEAS TRANSACTIONS on POWER SYSTEMS
Slavomir Kascak, Michal Prazenica,
Miriam Jarabicova, Roman Konarik
E-ISSN: 2224-350X
272
Volume 13, 2018

## [стр. 2]

depend on ranges of the duty ratio D ≤ ¼, ¼ ≤ D ≤
½, ½ ≤ D ≤ ¾, ¾ ≤ D ≤ 1.


Vin
T1
CIN
L1
Vout
COUT
L2
D1
D2
T2
i1
i2
iin
ic,in
iT1
iT2
iD2
iD1
ic,out
iout
+
-
T3
T4
iT3
iT4
L3
D3
i3
iD3
L4
D4
i4
iD4

Fig. 1  Four-phase interleaved boost converter

t
t
t
S1
S2
i1
I1pp
i2
t
iin
t
I2pp
IINpp
D.TS
1/4.TS
TS
t
S3
i3
t
I3pp
t
S4
i4
t
I4pp
ON
ON
ON
ON
OFF
OFF
OFF
OFF
OFF
OFF
ΔI2p
p
ΔI3p
p
ΔI4p
p
ΔI1p
p

Fig. 2  Inductors current waveforms in range of duty ratio less than 1/4

WSEAS TRANSACTIONS on POWER SYSTEMS
Slavomir Kascak, Michal Prazenica,
Miriam Jarabicova, Roman Konarik
E-ISSN: 2224-350X
273
Volume 13, 2018

## [стр. 3]

t
t
t
S1
S2
i1
I1pp
i2
t
iin
t
I2pp
IINpp
D.TS
TS
t
S3
i3
t
I3pp
t
S4
i4
t
I4pp
ON
OFF
OFF
OFF
OFF
OFF
ON
ON
ON
ON
d.TS
ΔI1p
p
ΔI2p
p
ΔI3p
p
ΔI4p
p
1/4.TS

Fig. 3  Inductor current waveforms in range of duty ratio  ¼ ≤ D ≤ ½
WSEAS TRANSACTIONS on POWER SYSTEMS
Slavomir Kascak, Michal Prazenica,
Miriam Jarabicova, Roman Konarik
E-ISSN: 2224-350X
274
Volume 13, 2018

## [стр. 4]

t
t
t
S1
S2
i1
I1pp
i2
t
iin
t
I2pp
IINpp
D.TS
1/4.TS
TS
t
S3
i3
t
I3pp
t
S4
i4
t
I4pp
ON
OFF
OFF
d.TS
ON
ON
ON
ON
ON
OFF
OFF
ΔI1p
p
ΔI2p
p
ΔI3p
p
ΔI4p
p

Fig. 4  Inductor current waveforms in range of duty ratio ½ ≤ D ≤ ¾


Figures 2, 3, 4 and 5 show the inductor current
waveforms for duty ratio less than ¼, between ¼ and
½, ½ and ¾, and greater than ¾, respectively, where
S1, S2, S3 and S4 are switching signals; i1, i2, i3 and i4
are the inductor currents; I1pp, I2pp, I3pp, and I4pp are the
peak to peak amplitudes or current ripples of the i1, i2,
i3 and i4, respectively and iin is the input current, which
is the sum of four inductor currents.
Here, the equations for inductor current ripples are
investigated and they are given for D ≤ ¼. The
equation (1) determines an increasing character of
the inductor current i1 and on the other hand the
equations (2), (3) and (4) a decreasing character of
the inductor currents i2, i3, and i4.
S
in
pp
pp
DT
L
V
I
I
=
=
1
1
∆
,
(1)
S
in
pp
DT
)
D
(
L
V
I
-
-
=
1
1
1
2
∆
,
(2)
S
in
pp
DT
)
D
(
L
V
I
-
-
=
1
1
1
3
∆
,
(3)

S
in
pp
DT
)
D
(
L
V
I
-
-
=
1
1
1
4
∆
,
(4)
(
)
1
2
3
4
1
4
1
4
,
1
inpp
pp
pp
pp
pp
in
out
S
S
I
I
I
I
I
V
V
D
DT
DT
D
L
D
L
=
+ ∆
+ ∆
+ ∆
=
-

=
-


-



(5)
where Vin and Vout are the input and output voltages
of the interleaved converter, D is the duty ratio, and
L is the inductor value in Henrys.
As can be seen from Fig. 2 to Fig. 5 the equations
(1) - (20) are dependent on the rise time of the input
current which it expresses the value of the input
current ripple. According this statement the inductor
current ripples (I1pp - I4pp) are different from the
current ripples ( ∆I1pp - ∆I4pp), except one case of (1).


Similarly, the equations for another interval of the
duty ratio ¼ ≤ D ≤ ½ are as follows:
S
in
pp
DT
L
V
I
=
1
∆
,
(6)
WSEAS TRANSACTIONS on POWER SYSTEMS
Slavomir Kascak, Michal Prazenica,
Miriam Jarabicova, Roman Konarik
E-ISSN: 2224-350X
275
Volume 13, 2018

## [стр. 5]

S
in
pp
DT
)
D
(
L
V
I
-
-
=
1
1
1
2
∆
,
(7)
S
in
pp
DT
)
D
(
L
V
I
-
-
=
1
1
1
3
∆
,
(8)
S
in
pp
DT
L
V
I
=
4
∆
,
(9)
(
)1
6
8
2
1
1
6
8
2
2
2
4
3
2
1
+
-
-
=






-
+
-
-
=
+
+
+
=
D
D
T
L
V
D
D
D
T
L
V
I
I
I
I
I
S
out
S
in
pp
pp
pp
pp
inpp
∆
∆
∆
∆

(10)

The value of the input current is increased until
two switches in two different phases are in on-state; in
the all next states of the switches, the input current has
a decreasing character, as can be seen in Fig. 3.
In the third interval ½ ≤ D ≤ ¾, when three switches
are in on-state the inductor current is increasing and
therefore the input current is also increasing. When
only two switches are in on-state, the input current is
decreasing, which is shown in the following equations
and depicted in Fig. 4.
S
in
pp
DT
L
V
I
=
1
∆
,
(11)
S
in
pp
DT
)
D
(
L
V
I
-
-
=
1
1
1
2
∆
,
(12)
S
in
pp
DT
L
V
I
=
3
∆
,
(13)
S
in
pp
DT
L
V
I
=
4
∆
,
(14)
(
)
1
2
3
4
2
2
8
10
3
2
1
8
10
3 .
2
inpp
pp
pp
pp
pp
in
S
out
S
I
I
I
I
I
V
D
D
T
L
D
V
T
D
D
L
= ∆
+ ∆
+ ∆
+ ∆
=


-
+
-
=


-


-
-
+

(15)

In the same manner, as in previous intervals, in
the fourth interval ¾ ≤ D ≤ 1, when four switchers
are in on-state the inductor current is increasing, and
if only one switch is in off-state, the input current is
decreasing.

S
in
pp
DT
L
V
I
=
1
∆
,
(16)
S
in
pp
DT
L
V
I
=
2
∆
,
(17)
S
in
pp
DT
L
V
I
=
3
∆
,
(18)
S
in
pp
DT
L
V
I
=
4
∆
,
(19)
1
2
3
4
(3
2).
inpp
pp
pp
pp
pp
in
S
I
I
I
I
I
V T
D
L
= ∆
+ ∆
+ ∆
+ ∆
=
-

(20)
As can be seen from the previous figures the
frequency of the input current ripple is four times
higher as compared to the inductor current what yields
to reduced current ripple. If we look at equations (1) -
(20) the current ripples are dependent on the value of
Vin or Vout, duty ratio D, inductor value L and
switching period TS. However, the ratio of Iinpp and
Inpp (n = 1, 2, 3 or 4 is the number of the phase) is
only dependent on the duty ratio D. Therefore, in
the next chapter is analysed only relative value of
input current ripple and inductor current ripple.

WSEAS TRANSACTIONS on POWER SYSTEMS
Slavomir Kascak, Michal Prazenica,
Miriam Jarabicova, Roman Konarik
E-ISSN: 2224-350X
276
Volume 13, 2018

## [стр. 6]

t
t
t
S1
S2
i1
I1pp
i2
t
iin
t
I2pp
IINpp
D.TS
1/4.TS
TS
t
S3
i3
t
I3pp
t
S4
i4
t
I4pp
ON
OFF
ON
d.TS
ON
ON
ON
O
N
ON
OFF
OFF
OFF
ΔI1p
p
ΔI2p
p
ΔI3p
p
ΔI4p
p

Fig. 5  Inductor current waveforms in range of duty ratio  ¾ ≤ D ≤ 1



WSEAS TRANSACTIONS on POWER SYSTEMS
Slavomir Kascak, Michal Prazenica,
Miriam Jarabicova, Roman Konarik
E-ISSN: 2224-350X
277
Volume 13, 2018

## [стр. 7]

Fig. 6  Test stand of four phase interleaved boost converter



Fig. 7  Simulated waveforms of input current (up) and inductor current (down) with D = 0.1



Fig. 8  Measured waveforms of input current (up) and inductor current (down) with D = 0.1
99.8ms
99.9ms
100.0ms
400mA
530mA
660mA
2.020A
2.110A
2.200A
-I(L1)
-I(V1)
WSEAS TRANSACTIONS on POWER SYSTEMS
Slavomir Kascak, Michal Prazenica,
Miriam Jarabicova, Roman Konarik
E-ISSN: 2224-350X
278
Volume 13, 2018

## [стр. 8]

Fig. 9  Simulated waveforms of input current (up) and inductor current (down) with D = 0.5



Fig. 10  Measured waveforms of input current (up) and inductor current (down) with D = 0.5




99.9ms
100.0ms
1.9A
2.6A
3.2A
10.2502A
10.2512A
10.2522A
-I(L1)
-I(V1)
WSEAS TRANSACTIONS on POWER SYSTEMS
Slavomir Kascak, Michal Prazenica,
Miriam Jarabicova, Roman Konarik
E-ISSN: 2224-350X
279
Volume 13, 2018

## [стр. 9]

Fig. 11  Simulated waveforms of input current (up) and inductor current (down) with D = 0.625



Fig. 12  Measured waveforms of input current (up) and inductor current (down) with D = 0.625



Fig. 13  The ratio of input current ripple to inductor current ripple
99.90ms
99.95ms
100.00ms
2.2A
2.9A
3.5A
11.16A
11.36A
11.55A
-I(L1)
-I(V1)
0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1
D [-]
0
0.2
0.4
0.6
0.8
1
I
in/I
L [-]
theory
simulation
measurement
WSEAS TRANSACTIONS on POWER SYSTEMS
Slavomir Kascak, Michal Prazenica,
Miriam Jarabicova, Roman Konarik
E-ISSN: 2224-350X
280
Volume 13, 2018

## [стр. 10]

3 Experimental Verification
The test stand depicted in Fig. 6 consist of 8
switches converter, four non-coupled inductors,
power analyser, power supplies and electronic load.
The control algorithm of the converter was only in
open loop and PWM signals for driving transistors
was
implemented
by
the
TI
microcontroller
TMS320F28069M. The parameters of the converter
stand are given in Table 1.

Table 1  Parameters of the interleaved converter
Parameter
Value
Inductor
430 μH
Output power
according the load
Input voltage
50 V
Output voltage
According duty ratio and load

The input or output voltage of the converter was
not so important because investigating characteristic
of current ripple ratio does not depend on these
parameters. Also the converter stage was not
optimized
for
efficiency
measurement;
the
investigation was only oriented to determine a current
ripple in different conditions.  The AC components of
simulated and measured input and inductor currents
are shown in the following figures, Fig. 7 - Fig. 12.
Then, from simulation results (Fig. 9) and
measurement (Fig. 10) is seen that the ripple of the
input current is not zero, but in comparison to its dc
component as shown in Fig. 9 should be considered
as zero. Therefore, also the measured ratio around
duty cycles 0.25, 0.5 and 0.75 should be considered
as zero. Then, Fig. 13 shows the comparison of the
theoretical, simulated and measured ratio of input
current ripple to inductor current ripple within
whole range of duty cycle. From Fig. 13 is seen that
a preferable range of duty ratio is approximately
from 0.2 to 0.8, which is sufficient for almost all
areas of use of boost converter. The increasing of
duty ratio causes that the dc component of current is
also increasing, what is associated with increasing
of AC component (the ripple) of the current. Then,
in Fig. 13 states that not the ripple of the inductor
current or the input current is shown, but only the
ratio between them.


4 Conclusion
The four-phase interleaved boost converter
operated in the continuous inductor current mode
was analysed. Generalised expressions for the input
and inductor current ripple were given in the
theoretical part. Subsequently, the simulation and
experimental results in the steady-state operation
was examined. The comparison of theoretical,
simulation and measured results is plotted in a
graph. According to the graph, the optimal operation
of the converter is around the duty ratio of 0.25, 0.5,
0.75. In these time instants, the ripple of the input
current is theoretically zero, but in practice is
approximately zero. On the other side, while
maintaining operating condition of the converter,
the reduced inductor current ripple depends only on
the value of L and therefore, if the ripples should be
smaller the inductor value must be higher.
In the future work the determination of input and
output capacities, determination of the optimal
number of phases and phase shedding of the
unloaded phases will be analysed.



Acknowledgments
This work was supported by projects: ITMS
26210120021, co-funded from EU sources and
European Regional Development Fund, APVV-150571: Research of the optimum energy flow control
in the electric vehicle system, VEGA 1/0928/15 -
Research
of
electronic
control
of
power
transmission and motion of road ICE- hybrid HEV
and EV vehicles.


References:
[1] TI, Power Tips: When to choose multiphase,
https://e2e.ti.com/blogs_/b/powerhouse/archive
/2013/10/31/powerlab-notes-when-to-choosemultiphase.
[2] Bodo´s Power Systems, Multiphase Buck
Converters,
http://www.powerguru.org/multiphase-buckconverters.
[3] Ovcarcik, R. Spanik, P., Pavlanin, R., DC/DC
converters used for a high input voltage based
on a half-bridge topology, 6-th European
Conference of TRANSCOM, Žilina, ISBN 808070-417-1, pp. 57-62, 2005.
[4] Somkun, S., Sirisamphanwong, Ch., Sukchai,
S., A DSP-based interleaved boost DC-DC
converter
for
fuel
cell
applications,
International Journal of Hydrogen Energy,
Vol. 40, Iss. 19, pp 6391-6404, May 2015.
[5] Sundari, N., Jeba, D., Ramalakshmi, R.
Rajasekaran, R., A Performance Comparison of
Interleaved Boost Converter and Conventional
Boost
Converter
for
Renewable
Energy
Application,
International
Conference
on
WSEAS TRANSACTIONS on POWER SYSTEMS
Slavomir Kascak, Michal Prazenica,
Miriam Jarabicova, Roman Konarik
E-ISSN: 2224-350X
281
Volume 13, 2018

## [стр. 11]

Green High Performance Computing, IEEE,
2013, pp. 6, 2013.
[6] Lazic, M., Zivanov, N., Sasic, B., Design of
Mutiphase Boost Converter for Hybrid Fuel
Cell/Battery
Power
Sources,
Paths
to
Sustainable Energy, INTECH, pp. 359-404,
2010.
[7] ON Semiconductor, Interleaved PFC.
[8] O'Loughlin, M., An Interleaving PFC PreRegulator for High-Power Converters, Texas
Instruments.
[9] Musavi, F., Eberle, W., Dunford, W. G., A
High-Performance
Single-Phase
Bridgeless
Interleaved PFC Converter for Plug-in Hybrid
Electric Vehicle Battery Chargers, IEEE
Transaction on Industry Applications, Vol. 47,
No. 4, 2011.
[10] Wong, P.L., Xu, P., Yang, B., Lee, F.C.,
Performance Improvements of Interleaving
VRMs
with
Coupling
Inductors,
IEEE
Transaction on Power Electronics, Vol. 16,
NO. 4, 2001.
[11] Cubon,
P.,
Radvan,
R..
Evaluation
of
Propulsion System of the Electric Go-kart, 17th
International Student Scientific Conference on
Electrical
Engineering,
POSTER,
Prague,
ISBN 978-80-01-05242-6, May 2013
[12] Mazgut,
R.,
Cubon,
P.,
Radvan,
R.,
Possibilities optimizing energy consumption of
electric vehicle, 19th International Student
Scientific
Conference
on
Electrical
Engineering, POSTER, Prague, ISBN 978-8001-05728-5, 2013
[13] Shin, H. B., Park, J. G., Chung, S. K., Lee, H.
W., Generalized Steady-state Analysis of
Multiphase Interleaved Boost Converter with
Coupled Inductors, IEE Proc.-Electr. Power
Appl., Vol. 152, No. 3, 2005.
[14] Ikriannikov, A., The Benefits of the Coupled
Inductor
Technology,
Maxim
Integrated,
Tutorial.
[15] Imaoka, J., Yamamoto, M., Kawashima, T.,
High-power-density three-phase interleaved
boost converter with a novel coupled inductor,
IEEJ Journal of Industry Applications, Vol. 1,
No. 1, pp. 20-3.
[16] Frivaldsky,
M.,
Hanko,
B.,
Prazenica,
M., Morgos, J., High Gain Boost Interleaved
Converters with Coupled Inductors and with
Demagnetizing Circuits, Energies, 11(1), 130,
2018.
[17] Zdanowskim M., Rabkowski, J., Barlik, R.,
Highly-Efficient and Compact 6 kW/4x125
kHz Interleaved DC-DC Boost Converter with
SiC Devices and Low-Capacitive Inductors,
Energies, 10, 363, 2017
WSEAS TRANSACTIONS on POWER SYSTEMS
Slavomir Kascak, Michal Prazenica,
Miriam Jarabicova, Roman Konarik
E-ISSN: 2224-350X
282
Volume 13, 2018
