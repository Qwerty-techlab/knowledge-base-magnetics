# Microsoft Word - 2_JPE-16-08-060

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

590                    Journal of Power Electronics, Vol. 17, No. 3, pp. 590-600, May 2017

 https://doi.org/10.6113/JPE.2017.17.3.590
ISSN(Print): 1598-2092 / ISSN(Online): 2093-4718

JPE 17-3-2
A Ripple-free Input Current Interleaved Converter
with Dual Coupled Inductors for High Step-up
Applications

Xuefeng Hu*, Meng Zhang*, Yongchao Li†, Linpeng Li*, and Guiyang Wu*

*,†School of Electrical Engineering, Anhui University of Technology, Ma'anshan, China


Abstract

This paper presents a ripple-free input current modified interleaved boost converter for high step-up applications. By integrating
dual coupled inductors and voltage multiplier techniques, the proposed converter can reach a high step-up gain without an extremely
high turn-ON period. In addition, a very small auxiliary inductor employed in series to the input dc source makes the input current
ripple theoretically decreased to zero, which simplifies the design of the electromagnetic interference (EMI) filter. In addition, the
voltage stresses on the semiconductor devices of the proposed converter are efficiently reduced, which makes high performance
MOSFETs with low voltage rated and low resistance rDS(ON) available to reduce the cost and conduction loss. The operating
principles and steady-state analyses of the proposed converter are introduced in detail. Finally, a prototype circuit rated at 400W with
a 42-50V input voltage and a 400V output voltage is built and tested to verify the effectiveness of theoretical analysis. Experimental
results show that an efficiency of 95.3% can be achieved.

Key words: Dual coupled inductors, High step-up, Modified interleaved boost converter, Ripple-free input current

I. INTRODUCTION
Recently, photovoltaic and fuel cells have become
increasingly important and widely used in distribution power
generation systems in order to alleviate the problems of
environmental pollution and depletion of fossil energy reserves
[1]-[7]. However, the main characteristic of these energies is a
low-output voltage. Hence, a DC-DC converter with a large
voltage conversion ratio, to boost low voltage (15-50V) to high
voltage (380-400V), is required as an interface to the main
electricity source through a DC-AC inverter. Although some
single switch boost converters with a high voltage gain have
been proposed [8]-[13], these single switch topologies suffer
from large input currents and current ripples for high power
applications.
Moreover,
for
renewable
energy
source
applications, a large input pulsating current reduces their
lifetime and even damage the power generation equipment.
The interleaved boost structure is a solution for high power
conversion and low input current ripple applications [14], [15].
However, the voltage gain of the conventional interleaved
boost converter is only determined by the duty ratio. In
practical application, the voltage gain is limited to five times
due to the influence of the parasitic parameters of the power
devices, inductors and capacitors. In addition, the voltage
stresses on the power devices are still equal to the high output
voltage, and an extreme duty ratio will result in a serious
reverse recovery problem of the output diodes [16]. Authors
have proposed several high step-up interleaved boost
converters by inserting switched capacitor cells into
conventional interleaved boost converters [17]-[19]. However,
massive switched capacitor cells are required to reach a very
high voltage gain, which increases the circuit complexity. In
addition, several high step-up interleaved boost converters with
coupled inductors were introduced in [20], [21]. However, the
voltage step-up capability is ordinary. In [22]-[26], some
interleaved boost converters combined coupled inductors with
switched capacitors for high step up and high power
applications.
This paper presents a modified interleaved boost converter
integrating dual coupled inductors and voltage multiplier
techniques for a high step-up gain. The proposed converter
inherits the merit of a ripple-free input current, which greatly
Manuscript received Aug. 9, 2016; accepted Jan. 23, 2017
Recommended for publication by Associate Editor Il-Oun Lee.
†Corresponding Author: chao1991_ly@foxmail.com
Tel: +86-15551783680, Anhui University of Technology
*School of Electrical Engineering, Anhui Univ. of Tech., China
© 2017 KIPE

## [стр. 2]

A Ripple-free Input Current Interleaved Converter with Dual Coupled Inductors for …              591

+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+

Fig. 1. Deduction process for the proposed topology. (a) Conventional boost converter. (b) Other boost converter structure. (c) Other
boost converter structure. (d) Modified interleaved boost converter. (e) The proposed converter.

suppress electromagnetic interference problem. At the same
time, the low voltages stress across the power switches is
conducive to improving the efficiency of power conversion.

II. OPERATIONAL PRINCIPLE OF THE PROPOSED
CONVERTER
The deduction process for the proposed converter topology
is shown in Fig. 1. It can be seen that this converter consists of
two parts: a modified interleaved boost converter in the left
dotted box and a voltage multiplier cell in the right dotted box.
The conventional boost converter is shown in Fig. 1(a). Fig.
1(b) and (c) show other boost converter versions, whose output
voltages are stacked by the capacitor C and the dc-source Vin,
and the voltage gains are equal to that of the conventional boost
converter. Fig. 1(d) is the modified interleaved boost converter,
which is achieved by the integration of the converters in Fig.1
(b) and (c). Then, the two inductors L1 and L2 in the modified
interleaved boost converter are separately substituted by the
primary windings of the coupled inductors Np1 and Np2, which
are adopted as energy storage and filter inductors. In addition,
the secondary windings of the two coupled inductors Ns1 and
Ns2 are connected in series for a voltage multiplier cell to obtain
a high voltage gain, as shown in Fig. 1(e).

The coupled inductor can be modeled as a magnetizing
inductor, a leakage inductance in series with the magnetizing
inductor and an ideal transformer with a corresponding turns
ratio. The coupling references of the coupled inductors are
indicated by the marks "*" and "·". Fig. 2 shows an equivalent

## [стр. 3]

592                          Journal of Power Electronics, Vol. 17, No. 3, May 2017


Fig. 2. Equivalent circuit of the proposed converter.

circuit of the proposed converter, in which:

1)
Lm1, Lm2: magnetizing inductors
2)
Lk1, Lk2: leakage inductances
3)
LS: a very small auxiliary inductor
4)
C1, C2, C3: intermediate storage capacitors
5)
CO: an output capacitor
6)
S1, S2: power switches
7)
D1, D2: clamp diodes
8)
Dr, Cm: a regenerative diode and a capacitor
9)
D3: an output diode
10)
N: the turns ratio of Ns/Np

It is worth pointing out that the duty ratios of the power
switches during steady operation are interleaved with a 180o
phase shift and higher than 0.5. The voltage step-up capability
is ordinary when the proposed converter is operating at a duty
ratio less than 0.5. Thus, the steady state analysis is made only
for this condition. To simplify the analysis, the very small
auxiliary inductor is not considered. The key theoretical
waveforms of the proposed converter are plotted in Fig. 3.
Considering the effect of the leakage inductance, there are
eight stages in one switching period, and the corresponding
equivalent circuits for each operational stage are depicted in
Fig. 4.
Stage I [t0-t1]: At t=t0, S1 begins to turn on, while S2 remains
conducting. Diodes D1, D2 and Dr are turned off, while diode
D3 is turned on. The current-flow path is shown in Fig. 4(a).
The capacitor Cm is discharging its energy to the capacitor C3
and the load RL through the output diode D3. The current
falling rate through the diode D3 is restrained by the leakage
inductances Lk1 and Lk2. Therefore, the reverse recovery
problem of the diode D3 is effectively alleviated. When the
current through the diode D3 becomes zero at t=t1, D3 switches
off and this mode ends.
3
3
3
0
0
2
1
2
( )
( )
(
)
(
)
C
Cm
D
D
k
k
V
V
i
t
i
t
t
t
N
L
L





    (1)
Stage II [t1-t2]: In this mode, S1 and S2 remain conducting,
and all of the diodes D1, D2, D3 and Dr are turned off. The
S1
S2
VD3
iD3
t0
t2
t3
t4
t5
t6
t0'
VDr
iDr
VD2
iD2
VD1
iD1
VDS2
iDS2
iLk1
iLk2
Iin
VDS1
t7
t8
t1
iDS1
TS
DTS


Fig. 3. Key theoretical waveforms of the proposed converter.

current-flow path is shown in Fig. 4(b). The magnetizing
inductors Lm1, Lm2 and the leakage inductances Lk1, Lk2 are
charged linearly by the dc power source Vin. There is no current
flowing through the primary or secondary windings. This
operating mode ends at t=t2 when S2 is turned off.
1
1
1
1
1
1
( )
( )
(
)
(
)
in
Lk
Lk
m
k
V
i
t
i
t
t
t
L
L




     (2)
2
2
1
1
2
2
( )
( )
(
)
(
)
in
Lk
Lk
m
k
V
i
t
i
t
t
t
L
L




    (3)
Stage III [t2-t3]: During this time interval, S1 remains
conducting, while S2 is turned off. The diodes D2 and Dr are
turned on, while the diodes D1 and D3 are turned off. Fig. 4(c)
depicts the current-flow path of this mode. The currents iLk2
and iLm2 decrease linearly, and the energy stored in the
leakage inductance Lk2 and the magnetizing inductor Lm2 are
released to the capacitor C2 through D2. Thus, the voltage
across the switch S2 is clamped at Vin+VC2. In addition, a part

## [стр. 4]

A Ripple-free Input Current Interleaved Converter with Dual Coupled Inductors for …              593

of the energy stored in the magnetizing inductor Lm2 is
transferred to the secondary side, which charges the capacitor
Cm via Dr. When the current iLk2 drops to zero at t=t3, this
mode is ends.
1
1
2
2
1
1
( )
( )
(
)
(
)
in
Lk
Lk
m
k
V
i
t
i
t
t
t
L
L




     (4)
2
2
2
2
2
2
2
( )
( )
(
)
(
)
C
Lk
Lk
m
k
V
i
t
i
t
t
t
L
L




    (5)
Stage Ⅳ [t3-t4]: During this time interval, S1 remains
conducting and S2 is still turned off. Diode Dr is turned on, D1
and D3 are turned off, while D2 turns off naturally since the
energy stored in the leakage inductance Lk2 has been released
completely to the capacitor C2. Fig. 4(d) illustrates the
current-flow path of this mode. The energy of the magnetizing
inductor Lm2 is transferred to the secondary side to
continuously charge the capacitor Cm. This mode ends when S2
begins to turn on at t=t4.
3
3
2
1
2
( )
( )
(
)
(
)
Cm
Dr
Dr
k
k
V
i
t
i
t
t
t
N
L
L




    (6)
Stage V [t4-t5]: During this transition interval, S1 remains
conducting, while S2 is turned on. Only diode Dr is turned on,
while D1, D2 and D3 are turned off. Fig. 4(e) depicts the
current-flow path of this mode. The current through the diode
Dr decreases linearly. The current falling rate through the diode
Dr is limited due to the leakage inductances Lk1 and Lk2. This
mode ends when the current through the diode Dr becomes
zero at t=t5.
4
4
2
1
2
( )
( )
(
)
(
)
Cm
Dr
Dr
k
k
V
i
t
i
t
t
t
N
L
L





(7)
Stage VI [t5-t6]: In this mode, both S1 and S2 are still turned
on. All of the diodes D1, D2, D3 and Dr are in the turn-off state.
The operating mode of this stage is the same as that of Stage
Ⅱ. The current-flow path is shown in Fig. 4(f). This mode ends
when S1 is turned off at t=t6.
Stage VII [t6-t7]: At t6, S1 is turned off, while S2 is still
turned on. Diodes D1 and D3 are turned on, while D2 and Dr
are turned off. The current-flow path is shown in Fig. 4(f).
The energy stored in the leakage inductance Lk1 and the
magnetizing inductor Lm1 are released to the capacitor C1
through the diode D1. Thus, the voltage across the switch S1 is
clamped at Vin+VC1. Meanwhile, the secondary windings of
the coupled inductors are series connected with the capacitor
Cm to charge the capacitor CO and to provide energy to the
load RL. This mode ends when the current through the
leakage inductance Lk1 decreases to zero at t=t7.
3
3
3
6
6
2
1
2
( )
( )
(
)
(
)
C
Cm
D
D
k
k
V
V
i
t
i
t
t
t
N
L
L






(8)
Stage VIII [t7-t8]: During this transition interval, S1 is turned
off, while S2 remains conducting. The diodes D1 and D3 are
turned on, while D2 and Dr are turned off. The current-flow
path of this mode is shown in Fig. 4(g). The energy stored in
the leakage inductance Lk1 has been completely released to the
capacitor C1, while the magnetizing inductor Lm1 continuously
delivers energy to the output via the secondary side of the
coupled inductor N1. This mode is ends when S1 is turned
onagain at t=t8.
3
3
3
7
7
2
1
2
( )
( )
(
)
(
)
C
Cm
D
D
k
k
V
V
i
t
i
t
t
t
N
L
L





    (9)

III. STEADY-STATE PERFORMANCE ANALYSIS OF
THE PROPOSED CONVERTER
To simplify the circuit analysis, the following assumptions
have been taken into account:
(1) The active switches and diodes are ideal, and the
equivalent series resistances (ESR) of all the
components including the inductor and capacitor are
ignored.
(2) Capacitor C1, C2, C3, Cm, and CO are large enough. Thus,
the voltages across them can be considered to be
constant in one switching cycle.
(3) The coupling-coefficient of the coupled inductor k is
equal to Lm/(Lm+Lk) and the turns ratio of the coupled
inductor N is equal to Ns/Np.
(4) The parameters of two coupled inductors are completely
symmetrical, that is to say, Lm1=Lm2=Lm, Lk1=Lk2=Lk,
Ns1/Np1=Ns2/Np2=N,k1=Lm1/(Lm1+Lk1)=k2=Lm2/(Lm2+Lk2)=
k.
A. Voltage Gain Express
To simplify the analysis, the very small auxiliary inductor LS
is not considered, and only stages Ⅱ, Ⅲ and Ⅶ are taken
into consideration for the CCM operation. According to the
topology structure, the output voltage can be expressed as:
1
2
3
O
in
C
C
C
V
V
V
V
V




      (10)
The following equations can be obtained from Fig. 4 (b)
and (c):
1
2
Lm
Lm
in
V
V
kV


Ⅱ
Ⅱ
             (11)
1
Lm
in
V
kV

Ⅲ
                (12)
2
2
Lm
C
V
kV

Ⅲ
              (13)
m
2
C
in
C
V
NkV
NkV


          (14)
During Stage Ⅶ, the following equations can be obtained
based on Fig. 4 (g):
1
1
Lm
C
V
kV

Ⅶ
              (15)
3
1
2
2
C
in
C
C
V
NkV
NkV
NkV



      (16)
Applying the volt-second balance principle on the
magnetizing inductors Lm1 and Lm2 yields:

## [стр. 5]

594                          Journal of Power Electronics, Vol. 17, No. 3, May 2017


(a) Stage Ⅰ.                                    (b) Stage Ⅱ.
RL
+
C1
D1
S1
+
+
+
C2
D2
S2
Np1
Np2
Lm1
Lm2
Lk1
Lk2
Co
D3
Ns2
Ns1
Cm
Dr
+
C3
Ls
+
Vin
iDS2
iDS1
iDr
iD3
iD1
iD2
iLk1
iLk2
iLs
RL
+
C1
D1
S1
+
+
+
C2
D2
S2
Np1
Np2
Lm1
Lm2
Lk1
Lk2
Co
D3
Ns2
Ns1
Cm
Dr
+
C3
Ls
+
Vin
iLk1
iDr
iD3
iD1
iD2
iLs
iDS1
iDS2
iLk2

                            (c) Stage Ⅲ.                                    (d) Stage Ⅳ.

                           (e) Stage Ⅴ.                                     (f) Stage Ⅵ.
RL
C1
D1
S1
C2
D2
S2
Np1
Np2
Lm1
Lm2
Lk1
Lk2
Co
D3
Ns2
Ns1
Cm
Dr
C3
Ls
Vin
iLk1
iLk2
iD2
iDS2
iDS1
iD1
iDr
iD3
iLs
RL
C1
D1
S1
C2
D2
S2
Np1
Np2
Lm1
Lm2
Lk1
Lk2
Co
D3
Ns2
Ns1
Cm
Dr
C3
Ls
Vin
iD2
iDS2
iD1
iDS1
iDr
iD3
iLk1
iLk2
iLs

                        (g) Stage Ⅶ                                            (h) Stage Ⅷ
Fig. 4. Operating modes of the proposed converter.

## [стр. 6]

A Ripple-free Input Current Interleaved Converter with Dual Coupled Inductors for …              595

Voltage gain MCCM
Turns ratio N

Fig. 5. Voltage gain MCCM as a function of the duty ratio D with
various turns ratios, the turns ratios versus the duty ratio under a
voltage conversion of 9, and the basic boost converter gain
curve.

1
0
(
)
0
S
S
S
DT
T
in
C
DT
kV dt
kV
dt





      (17)
2
0
(
)
0
S
S
S
DT
T
in
C
DT
kV dt
kV
dt





     (18)
The voltages across the capacitor C1 and C2 are derived as:
1
2
1
C
C
in
D
V
V
V
D


         (19)
Substituting (16) and (19) into (10), the output voltage can
be derived by:
1
2
3
1
2
1
O
in
C
C
C
in
D
Nk
V
V
V
V
V
V
D








 (20)
Thus, the voltage gain MCCM can be expressed as follows:
1+
2
1
O
CCM
in
V
D
Nk
M
V
D




        (21)
The characteristic curve of the voltage gain MCCM as a
function of the duty ratio D by various turns ratios, the plot of
the turns ratio N versus the duty ratio under a voltage gain of
MCCM = 9, and the gain curve of the basic boost converter are
shown in Fig. 5.
Fig. 6 shows the voltage gain MCCM versus the duty ratio
under different coupling coefficients and turns ratios of the
coupled inductor. It indicates that the coupling coefficient k has
a minimal impact on the voltage gain, especially with a turns
ratio of N=1. Thus, if the influence of the leakage inductances
is ignored, namely k=1, the ideal voltage gain can be derived
by:
1+
2
1
O
CCM
in
V
D
N
M
V
D




        (22)
B. Ripple-free Current Ripple Performance Analysis
It can be seen from Fig. 4 that in one switching period the dc
source Vin, the auxiliary inductor LS, the intermediate storage
capacitors C1, C2 and C3, and the output capacitor CO
constitute a voltage loop. Therefore, the voltage across the

Fig. 6. Voltage gain versus the duty ratio under different turns
ratios and coupling coefficients.

auxiliary inductor LS can be expressed as:
1
2
3
( )
S
S
L
L
S
in
C
C
C
CO
di
t
V
L
V
V
V
V
V
dt






(23)
Since the capacitors C1, C2, C3 and CO are assumed to be
large enough, their voltage ripples can be neglected and the
voltages across them can be considered to be approximately
constant in one switching period. As a result, there is an
extremely small voltage drop across the auxiliary inductor LS.
Therefore, the voltage VLS can be considered as a constant of
zero.
According to VLS/LS=diLS/dt=0, the auxiliary inductor
current iLS remains constant during one switching period.
Thus, the ripple-free input current characteristic of the
proposed converter can be achieved. It can be concluded that
the realization of ripple-free input current is not dependent on
other circuit parameters such as the duty ratio and turns ratio,
and that only a very small auxiliary inductor LS is needed,
without increasing the control complexity of the circuit.
C. Voltage Stress Analysis
On the basis of the steady operating principle, the voltage
stresses on the power components of the proposed converter
are formulated as follows. In order to simplify the voltage
stress analysis, the leakage inductances of the coupled
inductors and the voltage ripples on the capacitors are
neglected. The voltage stresses on the switches S1 and S2 can be
derived by:
1
2
1
1
1
2
O
DS
DS
in
V
V
V
V
D
D
N






    (24)
The voltage stresses of the diodes D1, D2, D3 and Dr are
expressed as:
1
2
1
1
1
2
O
D
D
in
V
V
V
V
D
D
N






    (25)
3
2
2
1
1
2
O
D
Dr
in
NV
N
V
V
V
D
D
N






    (26)
Fig. 7 shows the relationship between the normalized

## [стр. 7]

596                          Journal of Power Electronics, Vol. 17, No. 3, May 2017

.

Fig. 7. Relationship between the normalized voltage stresses and
turns ratios under D=0.6.

TABLE I
PERFORMANCE COMPARISON OF SIMILAR PROTOTYPES
Similar
prototypes
Converter[25]
Converter[26]
The proposed
converter
Number of
switches
2
2
2
Number of
diodes
4
4
4
Number of
cores
2
2
2
Number of
secondary
side
windings
1
1
1
Voltage
gain
2
1
ND
D



2
1
1
N
D



1
2
1
D
N
D




Voltage
stress on
the active
switches
2
(1
)
O
V
ND
D



2
1
O
V
N 

1
2
O
V
D
N



Input
current
ripple
Medium
Large
Close to zero

voltage stresses on the power components and the turns ratio
N under D=0.6. It can be concluded that when N=1, the
voltage stresses on the switches S1, S2 and the diodes D1, D2
are approximately 1/4 of the output voltage, and the voltage
stresses on the diodes D3, Dr are equal to 5/9 of the output
voltage
D. Key Performance Comparison
To demonstrate the performance of the proposed converter,
the key component quantities, the voltage gain, the
normalized voltages stress of the active switches, and the
input current ripple performance of the proposed converter
and other similar high step-up interleaved converters are
displayed in Table I.
It can be seen that the voltage gain of the proposed converter
is higher than that of the converters in [25] and [26]. In
addition, the proposed converter has the lowest voltage stresses
on the active switches. Moreover, the input current ripple of the
proposed converter is close to zero, which simplifies the
electromagnetic interference (EMI) filter design and helps to
extend the lifetime of power generation equipment.

IV. DESIGN CONSIDERATIONS
A. Design Consideration of Coupled Inductors
The turns ratio is one of the key parameters of the
suggested converter since it determines the voltage gain and
voltage stresses on the power devices. In general, in order to
reduce the conduction loss of the main switches, the duty
ratio should be no higher than 0.8. The turns ratio of the
coupled inductor can be calculated by:


1
(1
) 1
2
CCM
N
M
D
D



       (27)
The voltage gain of the proposed converter is designed as
ninefold, and the duty ratios of the switches are chosen as 0.6.
Once the duty ratios of the switches and the voltage gain are
chosen, according to the above equation, N=1 will be the
proper choice.
Based on the aforementioned analysis, the voltage gain is
less sensitive to the coupling coefficient k. However, the
leakage inductances of the coupled inductors can be designed
to restrain the current falling rate and to alleviate the reverse
recovery problem of the diode. In addition, the leakage
inductances Lk1 and Lk2 should be designed to be as consistent
as possible. The relationship of the leakage inductance, the
diode current falling rate, and the turns ratio is given by:
3
1
2
(1
2
)(
)
D
O
Dr
k
k
di
V
di
dt
dt
N
D
N
L
L





  (28)
When the leakage inductances Lk1 and Lk2 are equal to 1.8μH,
the current falling rate of the diodes Dr and D3 can be
decreased at approximately 30A/us, which alleviates the diode
reverse-recovery problem. It can be concluded that a small
leakage inductance can limit the diode current falling rate to a
low level. The actual inductance of the magnetizing inductors
Lk1 and Lk2 is measured as 2.1uH.
The value of the magnetizing inductors Lm1 and Lm2 can be
designed based on the foundation of the boundary operating
condition, which is derived from:
2
(1
)
66.7
2
(1
)(1
2
)
mB
S
R D
D
L
uH
f
N
D
N








To ensure the CCM operation of the proposed converter, the
actual inductance of the magnetizing inductors Lm1 and Lm2 is
designed as 80uH.
B. Design Consideration of the Capacitors
 Energy transfers from the input dc source to the load
through the auxiliary inductor LS, and the capacitors C1, C2, C3,
CO and Cm. According to ∆Q=C·∆VC =IC·∆T, the relationship
between the voltage ripple and the output power is derived as
follows:

## [стр. 8]

A Ripple-free Input Current Interleaved Converter with Dual Coupled Inductors for …              597

O
O
C
S
P
C
V
V f


              (29)
Where PO is the output power, VO is the output voltage, ∆VC
is the maximum tolerant voltage ripple on the capacitors C1,
C2, C3, CO and Cm, and fS is the switching frequency [26]. It
can be seen that the voltage ripple on capacitors can be
suppressed by a large capacitor. However, large capacitors
have a bulky volume, high cost and short life. On the other
hand, to realize ripple-free input current, the capacitances of
the capacitors C1, C2, C3 and CO should be large enough to
ensure that the voltages across C1, C2, C3 and CO are constant
in one switching period. In addition, when the capacitance of
an aluminum electrolytic capacitor increases, the ESR
becomes smaller, which reduces the power losses. Therefore,
a compromise should be made in the selection of a capacitor
among the input current ripple performance, converter
efficiency, converter lifetime, and cost.

V. EXPERIMENTAL VERIFICATIONS
In order to verify the performance of the proposed
converter, an experimental prototype has been built and
tested with the specifications in Table II.
Some key experimental waveforms of the proposed
converter are shown in Figs. 8-15. Fig. 8 displays the
performance of the currents through the primary side leakage
inductances iLk1 and Lk2 of the coupled inductors. It can be
TABLE Ⅱ
UTILIZED COMPONENTS AND PARAMETERS OF THE PROTOTYPE
Components
Parameters
Input voltage Vin
42V-50V
Output voltage VO
400V
Maximum output
power PO
400W
Switching
frequency fS
40kHz
Coupled inductors
N1,N2
N1=N2: 14T:14T
Lm1=Lm2=80uH
Lk1=Lk2=2.1uH
Core:EE55 PC40
Auxiliary
inductor LS
20uH
Power switches
S1, S2
IRFP260N(VDSS=200V,RDS(on)=0.04Ω)
Diodes D1, D2
MBR20200
Diodes D3, Dr
MUR2040
Capacitors C1, C2,
Cm
100uF/160V
Capacitor C3
100uF/250V
Capacitor CO
330uF/450V

Fig. 8. Experimental results of iLk1 and iLk2.


Fig. 9. Experimental comparison between input currents iin with
and without the auxiliary inductor Ls.


Fig. 10. Experimental results of VDS1 and iDS1.


Fig. 11. Experimental results of VDS2 and iDS2.


Fig. 12. Experimental results of VD1 and iD1.

## [стр. 9]

598                          Journal of Power Electronics, Vol. 17, No. 3, May 2017


Fig. 13. Experimental results of VD2 and iD2.


Fig. 14. Experimental results of VDr and iDr.


Fig. 15. Experimental results of VD3 and iD3.

seen that the currents iLk1 and iLk2 are interleaving and
approximately the same. This is in agreement with the
theoretical analysis.
To demonstrate the influence of the auxiliary inductor Ls, an
experimental waveform comparison between the input current
iin with Ls and the input current iin without Ls is made in Fig. 9.
It can be seen that the input current ripple is approximately
zero when the auxiliary inductor Ls exists, while the input
current ripple is relatively large when the auxiliary inductor Ls
is removed. This is in agreement with the theoretical analysis.
Experimental results of the voltage stresses of S1 and S2
and the current waveforms passing through them are shown
in Fig. 10 and Fig. 11. It can be seen that the voltage stresses
on the switches S1 and S2 are clamped at approximately 100V
and that there are voltage spikes across switches S1 and S2 due
to the leakage inductances of the coupled inductors.
Fig. 12 and Fig. 13 show the voltage and current stresses
on the diodes D1 and D2. It can be seen that the voltage
stresses on the diodes D1 and D2 are about 100V. This is in
agreement with the theoretical analysis. Thus, low-voltage

Fig. 16. Dynamic response waveforms from 400W to 550W.


Fig. 17. Measured efficiency of the proposed converter.


Fig. 18. Photo of the experimental system.

rated diodes with high performance can be adopted for the
proposed converter. In addition, the diodes D1 and D2 can be
turned off naturally.
Fig. 14 and Fig. 15 display the voltage and current stresses
on the diodes Dr and D3. It can be seen that the voltage stress
on diode Dr is approximately 180V, which is equal to the
voltage stress on diode D3. These results are in agreement
with the steady-state analysis and operating principle.
Fig. 16 shows the dynamic response between 550W and
400W because of a step load variation. It can be seen that the
output voltage is maintained at 400V.
A measured efficiency comparison according to the power
variation between the conventional interleaved boost
converter and the proposed converter is sketched in Fig. 17.
The maximum efficiency of the proposed converter is about
95.3% at Pout=200W, while the efficiency is approximately
91.2% at a full load. Fig. 18 shows a photograph of the
experimental system for the proposed converter.

## [стр. 10]

A Ripple-free Input Current Interleaved Converter with Dual Coupled Inductors for …              599

VI. CONCLUSION
In this paper, a modified interleaved boost converter for high
step-up applications is presented. The proposed converter can
reach a high step-up gain without an extreme duty ratio.
Meanwhile, the input current ripple of the proposed converter
can be decreased to zero by employing a small auxiliary
inductor, which simplifies the EMI filter design. Moreover, the
voltage stresses on the power switches are very low. As a result,
high performance MOSFETs with low voltage rated and low
resistance rDS(ON) can be selected to reduce the conduction
losses and cost. In addition, the reverse recovery problem of
the diodes is alleviated due to appropriate leakage inductances
of the coupled inductors. Furthermore, the energy of the
leakage inductances can be recycled to the output through the
capacitors C1 and C2. All of these features make this converter
suitable for high power applications where a large voltage gain
is demanded. The steady-state characteristics and the main
circuit performance are investigated minutely to explore the
advantages of the proposed converter. An experimental
prototype was developed with an input voltage source from
42V to 50V and a 400V output voltage. The results verified the
correction of the theoretical analysis.

ACKNOWLEDGMENT
The authors gratefully acknowledge the Natural Science
Foundation of Anhui Province of China (1408085ME80), the
Natural Science Foundation of Anhui Education Committee
(KJ2012A048), and the National Natural Science Foundation
(51577002) for its financial support.

REFERENCES
[1]
S. K. Changchien, T. J. Liang, J. F. Chen, and L. S. Yang,
"Novel high step-up DC-DC converter for fuel cell energy
conversion system," IEEE Trans. Ind. Electron., Vol. 57,
No. 6, pp. 2007-2017, Jun. 2010.
[2]
S. M. Chen, T. J. Liang, L. S. Yang, and J. F. Chen, "A
cascaded high step-up DC-DC converter with single
switch for microsource applications," IEEE Trans. Power
Electron., Vol. 26, No. 4, pp. 1146-1153, Apr. 2011.
[3]
Ling, Rui, G. Zhao, and Q. Huang. "High step-up
interleaved boost converter with low switch voltage
stress," Electric Power Systems Research, Vol. 128, pp.
11-18, Nov. 2015.
[4]
M. Prudente, L. L. Pfitscher, G. Emmendoerfer, and E. F.
Romaneli, "Voltage multiplier cells applied to non-isolated
DC-DC converters," IEEE Trans. Power Electron., Vol.
23, No. 2, pp. 871-887, Mar. 2008.
[5]
X. Yu, C. Cecati, T. Dillon, and M. G. Simões, "The new
frontier of smart grids," IEEE Ind. Electron. Mag., Vol. 5,
No. 3, pp. 49-63, Sep. 2011.
[6]
Q. Luo, Y. Zhang, P. Sun, and L. Zhou, "An active clamp
high step-up boost converter with a coupled inductor,"
Journal of Power Electronics, Vol. 15, No. 1, pp. 86-95,
Jan. 2015.
[7]
B. Yang, W. Li, Y. Zhao, and X. He, "Design and analysis
of a grid-connected photovoltaic power system," IEEE
Trans. Power Electron., Vol. 25, No. 4, pp. 992-1000, Apr.
2010.
[8]
T. F. Wu, Y. S. Lai, J. C. Hung, and Y. M. Chen, "Boost
converter with coupled inductors and buck-boost type of
active clamp," Industry Applications Conference, Vol. 1,
pp. 639-644, 2005.
[9]
Q. Zhao, and F. C. Lee, "High-efficiency, high step-up
DC-DC converters," IEEE Trans. Power Electron., Vol.
18, No. 1, pp. 65-73, Jan. 2003.
[10] R.-J. Wai, and R.-Y. Duan, "High-efficiency DC/DC
converter with high voltage gain," IEE Proceedings
Electric Power Applications, Vol. 152, No. 4, pp. 793-802,
Jul. 2005.
[11] T. J. Liang, and K. C. Tseng, "Analysis of integrated
boost-flyback step-up
converter,"
IEE
Proceedings
Electric Power Applications, Vol. 152, No. 2, pp. 217-225,
Mar. 2005.
[12] Y. P. Hsieh, J. F. Chen, T. J. Liang, and L. S. Yang,
"Novel
high
step-up
DC-DC
converter
with
coupled-inductor and switched-capacitor techniques,"
IEEE Trans. Ind. Electron., Vol. 59, No. 2, pp. 998-1007,
Feb. 2012.
[13] C. Y. Inaba, Y. Konishi, and M. Nakaoka, "High
frequency PWM controlled step-up chopper type DC-DC
power converters with reduced peak switch voltage
stress," IEE Proceedings Electric Power Applications, Vol.
151, No. 1, pp. 47-52, Jan. 2004.
[14] D. Y. Jung, Y. H. Ji, S. H. Park, and Y. C. Jung,
"Interleaved
soft-switching
boost
converter
for
photovoltaic power-generation system," IEEE Trans.
Power Electron., Vol. 26, No. 4, pp. 1137-1145, Apr.
2011.
[15] P. W. Lee, Y. S. Lee, D. K. W. Cheng, and X. C. Liu,
"Steady-state analysis of an interleaved boost converter
with coupled inductors," IEEE Trans. Ind. Electron., Vol.
47, No. 4, pp. 787-795, Aug. 2000.
[16] Wuhua Li, and Xiangning "A family of interleaved
DC-DC converters deduced from a basic cell with
winding-cross-coupled inductors (WCCIs) for high step-up
or step-down conversions," IEEE Trans. Power Electron.,
Vol. 23, No. 4, pp. 1791-1801, Jul. 2008.
[17] R. Giral, L. Martinez-Salamero, R. Leyva, and J. Maixe,
"Sliding-mode control of interleaved boost converters,"
IEEE Trans. Circuits Syst. I, Fundam. Theory Appl., Vol.
47, No. 9, pp. 1330-1339, Sep. 2000.
[18] L. S. Yang, T. J. Liang, and J. F. Chen, "Transformerless
DC-DC converters with high step-up voltage gain," IEEE
Trans. Ind. Electron., Vol. 56, No. 8, pp. 3144-3152, Aug.
2009.
[19] M. Prudente, L. L. Pfitscher, G. Emmendoerfer, and E. F.
Romaneli, "Voltage multiplier cells applied to non-isolated
DC-DC converters," IEEE Trans. Power Electron., Vol.
23, No. 2, pp. 871-887, Mar. 2008.
[20] Dwari, Suman, and L. Parsa, "An efficient high-step-up
interleaved DC-DC converter with a common active
clamp," IEEE Trans. Power Electron., Vol. 26, No. 1, pp.
66-78, Jan. 2014.
[21] G. A. L. Henn, R. N. A. L. Silva, P. P. Praça, and L. H. S.
C. Barreto, "Interleaved-boost converter with high voltage
gain," IEEE Trans. Power Electron., Vol. 25, No. 11, pp.
2753-2761, Nov. 2010.
[22] K. C. Tseng, C. T. Chen, and C. A. Cheng, "A
high-efficiency high step-up interleaved converter with a

## [стр. 11]

600                          Journal of Power Electronics, Vol. 17, No. 3, May 2017

voltage multiplier for electric vehicle power management
applications," Journal of Power Electronics, Vol. 16, No.
2, pp. 414-424, Jan. 2016.
[23] X. F. Hu, and C. Gong, "A high gain input-parallel
output-series DC/DC converter with dual coupled
inductors," IEEE Trans. Power Electron., Vol. 30, No. 3,
pp. 1306-1317, Mar. 2015.
[24] K. C. Tseng, C. C. Huang, and W. Y. Shih, "A high
step-up converter with a voltage multiplier module for a
photovoltaic system," IEEE Trans. Power Electron., Vol.
28, No. 6, pp. 3047-3057, Jun. 2013.
[25] C. M. Lai, C. T. Pan, and M. C. Cheng, "High-efficiency
modular high step-up interleaved boost converter for
DC-microgrid applications," IEEE Trans. Ind. Appl., Vol.
48, No. 1, pp. 161-171, Jan/Feb. 2012.
[26] W. Li, Y. Zhao, Y. Deng, and X. He, "Interleaved
converter with voltage multiplier cell for high step-up and
high-efficiency conversion," IEEE Trans. Power Electron.,
Vol. 25, No. 9, pp. 2397-2408, Sep. 2010.





Xuefeng Hu was born in Jiangsu Province,
China. He received his M.S. degree in
Electronic Engineering from the China
University of Mining and Technology,
Xuzhou, China, in 2001; and his Ph.D.
degree in Electrical Engineering from the
Nanjing University of Aeronautics and
Astronautics (NUAA), Nanjing, China, in
2014. He is presently working as a Professor in the Anhui Key
Laboratory
of
Power
Electronics
and
Motion
Control
Technology,
College
of
Electronic
Engineering,
Anhui
University of Technology, Ma'anshan, China. He is the author or
coauthor of more than 30 technical papers. His current research
interests include renewable energy systems, dc-dc power
conversion, the modeling and control of converters, flexible ac
transmission systems and distributed power systems.

















Meng Zhang was born in Anhui, China, in
1993. She received her B.S. degree from the
Jilin Jianzhu University, Changchun, China, in
2015. She is presently working towards her
M.S. degree in the College of Electrical
Engineering, Anhui University of Technology,
Ma'anshan, China. Her current research
interests include power electronics, and solar
and wind power generation.

Yongchao Li was born in Henan, China, in
1991. He received his B.S. degree from the
Henan University of Science and Technology,
Luoyang, China, in 2013. He is presently
working towards his M.S. degree in the
College of Electrical Engineering, Anhui
University of Technology, Ma'anshan, China.
His current research interests include power
electronics, distributed power system, and solar and wind power
generation.

Linpeng Li was born in Henan, China, in
1990. He received his B.S. degree from
Xuchang University, Xuchang, China, in 2014.
He is presently working towards his M.S.
degree in the College of Electrical Engineering,
Anhui University of Technology, Ma'anshan,
China. His current research interests include
power electronics, dc-dc power conversion,
and solar and wind power generation.

Guiyang Wu was born in Anhui, China, in
1991. He received his B.S. degree from the
Industrial and Commercial College, Anhui
University of Technology, Ma'anshan, China,
in 2015. He is presently working towards his
M.S. degree in the College of Electrical
Engineering,
Anhui
University
of
Technology, Ma'anshan, China. His current
research interests include power electronics and dc-dc power
conversion.
