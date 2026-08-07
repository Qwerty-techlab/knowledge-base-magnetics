# source

> Автоматически извлечено из `source.pdf` скриптом `parse_pdf.py`
> Движок: pymupdf. Страниц: 6 из 6.
> Дата извлечения: 2026-08-07 06:42 UTC

Текст не редактировался. Формулы и таблицы могут быть искажены —
при сомнении сверяться с исходным PDF.

---

## [стр. 1]

G. Kishor et al Int. Journal of Engineering Research and Applications                          www.ijera.com
ISSN : 2248-9622, Vol. 4, Issue 2( Version 1), February 2014, pp.274-279

 www.ijera.com                                                                                                                                274 | P a g e




Multiphase Boost Converter with Reduced Input Current Ripple
Using Direct Coupled Inductors

G. Kishor*, D. Subbarayudu**, S. Sivanagaraju***
*Associate Professor, Department of EEE, GPREC, Kurnool
** Retd. Professor & HOD, Department of EEE, GPREC, Kurnool
*** Professor & HOD, Department of EEE, JNTUK, Kakinada

ABSTRACT
The multi phase Boost topology is very popular in many applications. However, the current ripple in the input
inductor affects its ability to meet EM1 requirements. This paper presents the concept of overall current ripple
reduction of multiphase DC-DC converter by employing directly coupled inductors. An emphasis was also given
to calculate the generalized expression of equivalent inductance. With the help of specified parameters, the
design parameters are also determined. The proposed multi phase Boost topology retains the advantages of the
conventional Boost topology, but with ripple free input current. Detailed analysis was validated with simulation
and the results have been presented.
Keywords - Multiphase Boost Converter, Direct coupled, Ripple reduction.

I.
INTRODUCTION
Switching power converters have become
more and more important in industry today. Coupled
inductor and integrated magnetic techniques have
been widely reported since they were implemented in
the Cuk converter in 1977. The advantages of
integrated magnetic techniques are that the amount of
core material is reduced and the component count is
reduced. The significant advantage is that the ripple
in one winding can be dumped to another winding,
thus achieving a ripple free input or output current by
using coupled inductor technique. In addition to the
ripple free input current, Sepic and Cuk converters
also have the advantage of overload protection since
there is one capacitor, in the main loop to transfer the
energy. However, this capacitor has to carry large
input and output currents with a dc voltage value in
each cycle. The switch voltage stress of the Sepic and
Cuk converters is the sum of the input voltage and
the output voltage. This is a very critical condition in
some applications, especially for "boost" only
applications.
To meet the relevant EMI requirements in
power electronics a ripple free input current is very
much essential. A Boost-buck cascaded converter is
used for ripple reduction [1], however one addition
buck converter is used which increases the cost.
Several input filter designs are analyzed and
implemented [2], which increases the size of the
inductor used. However, the Cuk and Sepic
converters can easily achieve zero-ripple input
current by using coupled inductor techniques.
Therefore, the input current harmonics are much less
than the PWM Boost converter and EM1 is much
better [3].
Coupled-inductor and other integratedmagnetics techniques have existed for many years,
but
most
power
electronics
engineers
are
uncomfortable with them. This may be because of
limited experience with coupled magnetics. Or it
could be explained by the level of complexity in
many treatments of coupled magnetic devices. Unlike
most networks, coupled-inductor techniques involve
simultaneous
parallel
energy-transfer
pathways:
electrical and magnetic. Despite the difficulty, the
circuits are useful and deserve to be better
appreciated.
Multiphase
structure
with
interleaved
control is essential for the boost converter in order to
reduce the ripple current and to reduce the size of
passive component. On the other hand, although
parallel individual DC-DC converters in interleaved
structure have been demonstrated to reduce the
overall current ripple, it is still challenging to meet
today‟s requirements. In addition, the multiphase
interleaving structure has more inductors than the
single phase converters, which increases the
complexity of this converter. Solution has to be found
to reduce the core number and the complexity of
converters. This paper is aimed to improve the
performance of multiphase DC-DC converters by
employing directly coupled inductors.

II.
TWO PHASE BOOST CONVERTER
To increase the output voltage level a
multiphase boost converter is used. Fig.1 shows the
RESEARCH ARTICLE                                                                               OPEN ACCESS

## [стр. 2]

G. Kishor et al Int. Journal of Engineering Research and Applications                          www.ijera.com
ISSN : 2248-9622, Vol. 4, Issue 2( Version 1), February 2014, pp.274-279

 www.ijera.com                                                                                                                                275 | P a g e
schematic diagram of a two phase boost converter
with directly coupled inductors. The coupled
inductors are used to reduce the current ripple. In the
circuit shown switch SW1 , inductor L1 and the diode
D1 acts as one phase of boost converter. Similarly
switch SW2, inductor L2 and the diode D2 acts as the
other phase of boost converter.

Fig. 1. Two phase Boost converter

Fig. 2 shows the equivalent circuit of
directly coupled inductors

Fig. 2. Equivalent circuit of directly coupled
inductors

Where Lk1 and Lk2 are the leakage
inductances and Lm is the mutual inductance. The
coupled inductors are related with the equation (1)
Lm =
2
1L
L




         (1)
Where L1 and L2 are the inductances of the two
inductors. Let L1 = L2 = L and Lk1 = Lk2 = Lk . Also
let V1  and V2 are the voltages across the two
inductors which is given as in equation (2).
dt
dI
L
dt
dI
L
V
m
2
1
1
1




dt
dI
L
dt
dI
L
V
m
2
2
1
2




         (2)
By rearranging the equation (2)
dt
dI
L
L
L
V
L
L
V
m
m
1
2
2
1









dt
dI
L
L
L
V
L
L
V
m
m
2
2
1
2










         (3)
Consider
the
gating
signals
for
one
switching cycle with VG1 and VG2 as gating signals
of the two switches SW1 and SW2 as shown in Fig.3.


Fig.3. One switching cycle

Switch SW1 is on in the period „a‟. During
this period switch SW2 is in off position and so V1
and V2 are given as
V1 = VIN
&
V2 = VIN - V0
         (4)
In this stage the multiphase boost converter act as
single phase boost converter and so the output
voltage is given as
)
1
(
0
D
V
V
IN





         (5)
Substituting equation (5) in (4) V2 is given as
1
2
)
1
(
V
D
D
V






         (6)
Substituting equation (6) in (3) and solving for V1
which gives
dt
dI
D
D
L
L
L
L
L
V
m
m
1
2
1
)
1
(
.
1

















         (7)
Therefore the equivalent inductance during the period
„a‟ is

L
D
D
D
D
L
L
L
L
L
L
m
m
a
eq
)
1(
1
1
)
1(.
1
2
2
,











         (8)
Where α is coefficient of coupling and α = Lm/L.
Similarly during the time interval „b‟ V1 and V2 are
given as
V1 = VIN - V0  &  V2 = VIN - V0

         (9)
From equation (9) it is clear that
V1 = V2



       (10)
Substituting equation (10) in (3) , the equivalent
inductance is
Leq,b= (1+)L



       (11)
Similarly, during time interval „c‟, V1 and V2 are
V1 = VIN -V0    & V2 = VIN

       (12)
Therefore V1 and V2 are related with the equation
given in (13)
1
2
1
V
D
D
V





       (13)
VG1
VG2
a
b
c
d

## [стр. 3]

G. Kishor et al Int. Journal of Engineering Research and Applications                          www.ijera.com
ISSN : 2248-9622, Vol. 4, Issue 2( Version 1), February 2014, pp.274-279

 www.ijera.com                                                                                                                                276 | P a g e
By substituting equation (13) in equation
(3), the equivalent inductance Leq,c is
L
D
D
L
c
eq






1
.
1
1
2
,


       (14)
The interval „d‟ is same as interval „b‟ and so the
equivalent inductance is
Leq,d = (1+)L


       (15)

III.
RIPPLE CURRENT REDUCTION
For a duty cycle below 0.5 the phase current
and overall current waveforms are as shown in Fig.4.
The phase current ripples of phase 1 and phase 2 are
given as

Fig.4. Current waveforms in one switching cycle

2
,
,1
1
)
1(
).
1(
.








D
D
L
DT
V
L
DT
V
I
IN
a
eq
IN
a


(16)
2
,
0
,
2
1
)
1(
.
)
(









D
D
L
DT
V
L
DT
V
V
I
IN
a
eq
IN
a

       (17)
The overall current ripple is the sum of two phase
current ripples and for  a directly coupled inductors it
is given as
,
1,
2,
(1 2 )
1
.
.
(1
) (1
)
IN
IN dir
a
a
V DT
D
I
I
I
L
D









       (18)
Similarly the ripple current for a uncoupled inductors
is given as
)
1
(
)
2
1
(.
)
(
,
D
D
L
DT
V
L
DT
Vo
V
L
DT
V
I
IN
IN
IN
unc
IN








(19)
With this the ratio of the direct coupled to the
uncoupled is





1
1
,
,
unc
IN
dir
IN
I
I



       (20)
With the variation in duty cycle and with coefficient
of coupling = 0.61, Fig.5 shows the input current
variation of uncoupled and the directly coupled
inductors.

Fig.5. Input current reduction in uncoupled and
directly coupled inductors

From the Fig.5 it is clear that by increasing
the coupling coefficient, which effectively reduce the
input current ripple. Therefore coupling coefficient is
to be chosen carefully.

IV.
DESIGN PROCEDURE
The design procedure for the multiphase
boost converter is presented in this section. The
specifications of the boost converter are
Output Power

P   = 250W
Output Voltage
Vo = 200V
Input Voltage

VIN = 50V
Switching frequency
fs = 25kHz
Input current ripple
ΔI = 10% of phase current

The design procedure can be performed as following
Duty cycle
75
.
0
1



o
IN
V
V
D

 Input current
    =  P/VIN  = 5A

mH
I
DT
V
L
phase
IN
a
eq
23
.
0
,




With the consideration of losses and high
transient current, the inductors used are chosen with
slight changes. In the proposed converter the
maximum current that flow through the inductor in
each phase is equal to half of the total current.

V.
SIMULATION RESULTS
In order to verify the theoretical analysis of
the previous section, simulations have been carried
out.
An input voltage of 50V given to the converter circuit
and the switching pulses of duty ratio, D=0.74 and
frequency, f = 25 kHz given to the MOSFET‟s is
shown in Fig. 6, Fig.7 and Fig.8, respectively.

## [стр. 4]

G. Kishor et al Int. Journal of Engineering Research and Applications                          www.ijera.com
ISSN : 2248-9622, Vol. 4, Issue 2( Version 1), February 2014, pp.274-279

 www.ijera.com                                                                                                                                277 | P a g e

Fig.6 Input voltage to the converter


Fig.7 Driving pulses for switch S1

Fig. 9 and Fig. 10 shows the output voltages
across the switches. It can be seen that the output of
MOSFET is compliment of the input.

Fig. 8 Driving pulses for switch S2.


Fig.9 Voltage across the switch S1

Fig.10 Voltage across the switch S2

Fig.11 and 12 shows the current waveforms
of uncoupled and direct coupled. With uncoupled
inductors, the input current has risen up to 24A and
settles at 6.181A in 0.075sec whereas with direct
coupling, the input current has risen up to 18.7A and
settles at 6.07A in 0.06 seconds. Therefore the direct
coupling method attains stability at a much faster rate
compared to the converter with uncoupled inductors.
A close observation of the two current waveforms
(fig. 11 and fig.12) yields that the transient current
has reduced along with the current ripple in directly
coupled based two inductor boost converter system.
The decrease in transient current ensures less harm to
the inductor as well as the switches and moreover the
rating of the inductor can be reduced, thus decreasing
the size of the inductor. On the other hand the current
ripple has reduced from 7.16% (as in uncoupled) to

Fig.11 Input current for uncoupled system


Fig.12 Input current for directly coupled system

## [стр. 5]

G. Kishor et al Int. Journal of Engineering Research and Applications                          www.ijera.com
ISSN : 2248-9622, Vol. 4, Issue 2( Version 1), February 2014, pp.274-279

 www.ijera.com                                                                                                                                278 | P a g e
6.58% (as in direct coupling), therefore the losses due
to the ripple gets reduced, thus leading to an efficient
converter.
In Fig. 13 and Fig. 14, the input power and
output power of the system is shown. Clearly the
input power is equal to the output power.

Fig.2.13 Input power of the system



Fig. 14 Output power of the system


Fig.15 Output voltage of the system

Fig. 15 shows the output voltage which has
settled at 199.5V. The output voltage ripple is found
to be 0.76% which is clearly in the standard desired
limits of 1%.Fig. 16 shows the output current of the
system.


Fig.16 Output current of the system


Fig.17 Variation of output voltage with input voltage


Fig.18 Variation of output power with input power

Fig. 17 shows the variation of the input
voltage with the output voltage. Clearly, as desired,
the output voltage is found to be four times the input
voltage. Fig.18 shows the variation of the input
power with the output power of the system. It can be
observed that the efficiency lays around 86% for the
direct coupled converter.

VI.
CONCLUSION
A multi phase boost converter is simulated
with direct coupled inductors. The main feature of
this circuit is that the voltage stress of each switch is
one half of the voltage stresses of the switches in the
single inductor implementation. In addition, the input
current is distributed evenly through the two boost
inductors so that the current ripple in the output
capacitor is smaller than that in the single-inductor
implementation. And also, it has been found that the

## [стр. 6]

G. Kishor et al Int. Journal of Engineering Research and Applications                          www.ijera.com
ISSN : 2248-9622, Vol. 4, Issue 2( Version 1), February 2014, pp.274-279

 www.ijera.com                                                                                                                                279 | P a g e
transient current has been reduced when compared
with the uncoupled boost converter, thus minimizing
the stress on inductor and the switches during
transient period.


REFERENCES
[1]
M. Milanovic, F. Mihalic, K. Jezernik, U.
Milutinovic "Single Phase Unity Power
Factor Correction Circuits with Coupled
Inductances" , IEEE Power Electronics
Specialists Conference, 1992, pp. 1077-1082.
[2]
J. Simonelli, D. Torrey "Input Filter Design
Considerations for Boost Derived High
Power Factor Converters", IEEE Applied
Power Electronics Conference, 1992, pp.
186-192.
[3]
D. Simonetti, J. Sebastian, J. Uceda "Control
Conditions to Improve Conducted EM1 by
Switching Frequency Modulation of Basic
Discontinuous PWM Preregulators‟‟ IEEE
Power Electronics Specialists Conference,
1994, pp. 1180-1187
[4]
J. Wang, W.G. Dunford and K. Mauch,
"Analysis of a ripplefree input-current boost
converter with discontinuous conduction
characteristics",
IEEE
Trans.
Power
Electronics, vol. 12, no. 4, pp. 684-694, July
1997
[5]
J.W. Kolar, H. Sree, N. Mohan and F.C.
Zach, "Novel aspects of an application of
„zero‟-ripple techniques to basic converter
topologies", in Rec. IEEE Power Electronics
Specialists Conf., pp. 796-803, 1997
[6]
D.K.W. Cheng, X.C. Liu and Y.S. Lee, "A
new improved boost converter with ripple
free input current using coupled inductors",
Power Electronics and Variable Speed
Drives Conf., IEE conf. publ. no. 456, pp.
592-599, Sep. 1998
