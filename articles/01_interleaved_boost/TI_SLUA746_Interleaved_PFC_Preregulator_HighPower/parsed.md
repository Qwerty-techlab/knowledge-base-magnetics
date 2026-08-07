# An Interleaved PFC Preregulator for High-Power Converters

<!-- FORMULA-WARNING -->
> **Формулы в этом файле недостоверны.** Текстовый слой PDF теряет дробные черты, радикалы и группировку степеней; знак интеграла приходит как `Z` или `R`, знак суммы -- как `P`. Формул вырезано: **27**, читать их в `formulas/` (картинки 300 dpi, перечень в `formulas/INDEX.md`).
<!-- /FORMULA-WARNING -->

> Автоматически извлечено из `source.pdf` скриптом `parse_pdf.py`
> Движок: pymupdf. Страниц: 17 из 17.
> Дата извлечения: 2026-08-07 06:42 UTC

Текст не редактировался. Формулы и таблицы могут быть искажены —
при сомнении сверяться с исходным PDF.

---

## [стр. 1]

Topic 5
An Interleaved PFC Preregulator for
High-Power Converters
SLUA746

## [стр. 2]

SLUA746

## [стр. 3]

5-1
An Interleaving PFC Pre-Regulator
for High-Power Converters
Michael O'Loughlin, Texas Instruments
ABSTRACT
In higher power applications, to fully utilize the line, power factor correction (PFC) is a necessity.
Passive solutions were developed first, which required bulky inductors and capacitors. To reduce the
volume of these bulky solutions active PFC using a boost topology was developed. The active solutions
had higher power densities than the passive solutions. Interleaving PFC pre-regulators is the next step
in increasing PFC pre-regulator power densities, reducing the overall volume of the design.
Interleaving will reduce magnetic volume and has the added benefit of reducing RMS current in the
boost capacitor. This topic will evaluate the benefits of interleaving PFC pre-regulators.

I. SINGLE STAGE BOOST CONVERTER REVIEW
In PFC pre-regulators, the most popular
topology used is a boost converter. This is
because boost converters can have continuous
input current that can be manipulated with
average current mode control techniques to force
input current to track changes in line voltage.
Fig. 1 shows a traditional single stage boost. The
inductor ripple current (∆IL1) is directly seen at
the converter's input and will require filtering to
meet EMI specifications. The diode output
current (I1) is discontinues and needs to be
filtered out by the output capacitor (COUT). In this
topology, the output capacitor ripple current
(ICOUT) is very high and is the difference between
I1 and the dc output current ( IOUT).


I
1
L1
S1
I1
COUT
RLOAD
IIN
VIN
IOUT
ICOUT
ON
OFF
S1
∆IL1
IIN
0A
ICOUT = I1 - IOUT

Fig. 1. Traditional boost stage.
SLUA746

## [стр. 4]

5-2
II. BENEFITS OF TWO PHASE INTERLEAVING
BOOST CONVERTERS
Fig. 2 shows the functional diagram of a two
phase
interleaved
boost
converter.
The
interleaved boost converter is simply two boost
converters in parallel operating 180° out of
phase. The input current is the sum of the two
inductor currents IL1 and IL2. Because the
inductor's ripple currents are out of phase, they
tend to cancel each other and reduce the input
ripple current caused by the boost inductors.
The
best
input
inductor
ripple
current
cancellation occurs at 50 percent duty cycle.
The output capacitor current is the sum of the
two diode currents (I1 + I2) less the dc output
current.
Interleaving
reduces
the
output
capacitor ripple current ( IOUT) as a function of
duty cycle. As the duty cycle approaches 0
percent, 50 percent and 100 percent duty cycle,
the sum of the two diode currents approaches
dc. At these points, the output capacitor only has
to filter the inductor ripple current.
L1
I1
COUT
RLOAD
IIN
VIN
IOUT
ICOUT
L2
I2
S2
S1
S1
S2
ON
ON
OFF
OFF
∆IL1
∆IL1
IIN/2
IIN = IL1 + IL2
I1
I2
ICOUT = (I1 + I2) - IOUT
0 A

Fig. 2. Interleaved boost stage.

SLUA746

## [стр. 5]

5-3
III. INPUT RIPPLE CURRENT REDUCTION AS A
FUNCTION OF DUTY CYCLE
The following equations show how the ratio
of input ripple current to the inductor ripple
current (K(D)) vary with changes in duty cycle.
Fig. 3 shows how K(D) varies with changes in
duty cycle.
1
L
IN
ΔI
ΔI
K(D) =


D
1
2D
1
K(D)
-
-
=
 if D ≤ 0.5

D
1
-
2D
K(D) =
 if D > 0.5

0.0
K(D) = ∆IIN/∆IL1
0.0
1.0
D - Duty Cycle
0.4
0.4
0.6
1.0
0.1
0.3
0.5
0.8
0.9
0.2
0.6
0.8
0.1
0.3
0.5
0.7
0.9
0.2
0.7

Fig. 3. Input ripple current reduction.
In PFC pre-regulators the duty cycle (D(θ))
is not constant and will varies with changes in
line phase angle (θ) and input voltage (VIN(θ) ).
The amount of duty cycle variation for universal
applications can be quite large. This variation in
duty cycle can be observed by evaluating a
converter that was designed for a universal input
of 85 V to 265 V RMS with a regulated 385 V
dc output. At low line the duty cycle (D1(θ))
will vary from 100% to 69% and at high line the
duty cycle (D2(θ)) will vary from 100% down
to 2%. The inductor ripple current cancellation
will not be 100% throughout the line cycle.
However, it is good enough to drastically reduce
the input ripple current for a given inductance.
The highest ripple current in this example would
occur at the peak of low line with a duty cycle
of 69%. The input ripple current at this duty
cycle will be 55% of the individual inductor
ripple current. When the converter is operating
at 2% and 100% duty cycle there is very little
inductor ripple current cancellation. However, at
these duty cycles the interleaved PFC preregulator has very little inductor ripple current.
Overall, the input ripple current of the PFC
boost will be 55% of what it would have been in
a single phase PFC designed for the same power
level and inductance. This can be found by
evaluating Fig. 3.
( )
( )
θ
θ
sin
2
V
V
IN(rms)
IN
×
=


( )
( )
OUT
IN
OUT
V
V
V
D
θ
θ
-
=





SLUA746

## [стр. 6]

5-4
D - Duty Cycle
0
180
Phase Angle - O
60
30
120
150
90
0.0
0.4
0.6
1.0
0.1
0.3
0.5
0.8
0.9
0.2
0.7
D2(θ)
D1(θ)

Fig. 4. Duty cycle variation in universal PFC
pre-regulator.
IV. INPUT RIPPLE CURRENT CANCELLATION
CAN REDUCE BOOST MAGNETIC VOLUME
The inductor ripple current cancellation
allows the designer to reduce boost inductor
magnetic volume. This is due to the energy
storage requirement of the two interleaved
inductors being half that of single stage preregulator designed for the same power level,
switching frequency and inductance.
Single stage inductor energy (ESingle):
2
SINGLE
LI
2
1
E
=


Two phase total inductor energy (EInterleaved):
2
2
2
D
INTERLEAVE
LI
4
1
2
I
L
2
1
2
I
L
2
1
E
=
⎟
⎠
⎞
⎜
⎝
⎛
+
⎟
⎠
⎞
⎜
⎝
⎛
=


The reduction in energy storage does not
directly
translate
into
magnetic
volume
reduction. A designer could expect to see up to a
25% reduction in magnetic volume going from a
single phase PFC pre-regulator to a dual phase
interleaved PFC. This will be discussed later in
the paper with actual design examples.
Interleaving PFC pre-regulators if done in
this fashion will not increase the size of the EMI
filter. A common design practice is to select the
switching frequency of the power converter
below the EMI lower limit of 150 kHz. The
second harmonic of switching frequency would
be twice the fundamental and will most likely be
in the EMI band and would need to be filtered to
meet specifications. Interleaving two preregulators will cause the input to see a switching
frequency that is twice the switching frequency
of a single phase. This means the fundamental
switching frequency of the converter will most
likely be pushed into the EMI band and will be
at the second harmonic of an individual stage's
switching frequency. However, the input ripple
current at this frequency will be reduced by a
factor of two. This should not put any additional
constraints on the EMI filter.
SLUA746

## [стр. 7]

5-5
V. THE EMI FILTER CAN ALSO BE REDUCED
Depending on the design parameters just
interleaving PFC pre-regulators could reduce
the size of the EMI filter. For example in
European
designs
and
boost
follower
applications where the boost voltage is just
above the peak of the input line voltage the
highest inductor ripple current occurs at 50%
duty cycle. From the graph in Fig. 3 it can be
observed when the converter is operating at
50% duty cycle the inductor ripple currents
would cancel each other out. In this case the
EMI filter would be drastically reduced just by
interleaving.
The designer also has the option of running
the interleaved pre-regulator at a lower
switching frequency and increase the boost
inductance slightly to reduce input ripple
current. If this is done correctly the designer
could decrease the size of the EMI filter without
increasing the size of the boost inductor volume
compared to a single stage pre-regulator
approach. The designer may be able to reduce
both the EMI filter; as well as, the boost
inductor if the converter's switching frequency
is not reduced too much.
VI. OUTPUT CAPACITOR RIPPLE CURRENT
REDUCTIONS AS A FUNCTION OF DUTY CYCLE
Interleaving PFC pre-regulator stages has
the added benefit of reducing the output
capacitor RMS current. Fig. 5 shows the
normalized output capacitor RMS current in a
single stage boost (ICOUT1(D)) and in a two stage
interleaved boost converter (ICOUT2(D)) as a
function of duty cycle. Knowing that the duty
cycle
in
universal
PFC
pre-regulator
applications varies from 100% to 2% and
studying Fig. 5 it can be observed that
interleaving will drastically reduce output
capacitor RMS current. In this example the
RMS current would be cut in half. This
reduction in RMS current will reduce electrical
stress in the output capacitor and improve the
converter's reliability.
(
)
2
OUT1
C
D
1
D)
(1
(D)
I
-
×
-
=

(
)
2
OUT2
C
2D
1
2D)
(1
2
1
(D)
I
-
×
-
=
 if D ≤ 0.5
(
)
2
OUT12
C
2D
2
2D)
(2
2
1
(D)
I
-
×
-
=
 if D > 0.5
0.0
ICOUT - Output Capacitor Current - A
0.24
0.36
0.60
0.06
0.18
0.30
0.48
0.54
Single Stage ICOUT1(D)
RMS Current
Interleaved ICOUT2(D)
RMS Current
0.0
1.0
D - Duty Cycle - C
0.4
0.2
0.6
0.8
0.1
0.3
0.5
0.7
0.9
0.12
0.42

Fig. 5. Normalized output capacitor RMS
currents as a function of D.
SLUA746

## [стр. 8]

5-6
VII. 350-W, TWO PHASE INTERLEAVE PFC
PROTOTYPE
To evaluate some of the benefits of
interleaving a 350-W two phase interleaved PFC
pre-regulator was constructed. This prototype
was designed for a universal input of 85 V to
265 V RMS. The boost output voltage (VOUT)
for the design was 385 VDC. The circuit was
designed for a switching frequency (fS) of
100 kHz to limit switching losses. The prototype
used 600-μH inductors for L1 and L2. The
output capacitor (COUT) needed for the design
was
a
220-μF
electrolytic
capacitor.
A
functional schematic of the circuit is presented
in Fig. 6.

VIII. LAB RESULTS
The largest inductor ripple current occurs
when the converter operates at low line input at
the peak of line. The oscilloscope plot in Fig. 7
shows the inductor ripple current cancellation at
the peak of line when the input is 85 VRMS. CH1
is L1 inductor current, CH2 is L2 inductor
current. M1 is the input current which is the sum
of inductor currents L1 and L2. The current
probes were set with 2 A/Div. ratio. From this
plot it can observed that the input ripple current
is 55% of the individual inductor current. The
reduction in input ripple current agrees with the
graph of Fig. 3 for 69% duty cycle.
Input Current IIN
IL2
IL1
CH2
CH1
M1

Fig. 7. Inductor ripple current, POUT = 350 W.
UCC28220
Interleaved
PWM
Controller
VLINE
L1
D1
COUT
VOUT
L2
D2
UCC28528 PFC
Controller
Q2
Q1

Fig. 6. Dual interleaved PFC.


SLUA746

## [стр. 9]

5-7
Figs. 8 and 9 show the input and inductor
ripple currents at maximum load at minimum
and maximum line voltage. CH1 and CH2 are
inductor current L1 and L2. M1 is the input
current to the converter and is the sum of L1 and
L2. The current probe was set with 2 A/Div.
ratio. From these waveforms, it can be observed
that high frequency input ripple current is much
less than the individual phase's boost inductor
current. If this was a single stage topology the
full inductor ripple current would be seen at the
input of the converter.

Input Current IIN
IL2
IL1
CH2
CH1
M1

Fig. 8. Input current at VIN = 85 V, 2 A/Div.
Input Current IIN
IL2
IL1
CH2
CH1
M1

Fig. 9. Input current at VIN = 265 V, 2 A/Div.
The following equations was used to
calculate the highest RMS current in the output
capacitor. The highest ripple current occurs at
the minimum input (VIN(min)) of 85 V RMS. The
calculation is based on half a line cycle of the
50 Hz line (fLINE). The duty cycle of each boost
stage (D1(t)) at low line varies from 100% to
69%. The estimated output capacitor RMS
current (ICOUT(rms)) was 1 A.
LINE
S
f
2
f
terations
I
×
=


Iterations
f
2
1
Step
LINE
×
=


)
t
sin(ω
V
2
P
(t)
I
IN(min)
OUT
IN
×
×
×
=


The RMS current in the boost capacitor was
measured at 1 A, which is less than half of what
it would be in a single stage PFC pre-regulator
with the same power requirements.

(
)
(
)
A
 1
Iterations
Step)
n
2D1(ω
2
Step))
n
2D1(ω
(2
2
1
Step
n
I
I
Iterations
1
n
2
2
IN
Cout_rms
≈
×
×
-
×
×
×
-
×
×
=
∑
=



SLUA746

## [стр. 10]

5-8
IX. EVALUATE INDUCTOR RIPPLE CURRENT
CANCELLATION IN THREE AND FOUR PHASE
INTERLEAVED PFC PRE-REGULATORS
The following equations and the graph in
Fig. 10 show how the ratio of input ripple
current to inductor ripple current vary with
changes in duty cycle for two, three and four
phase interleaved PFC pre-regulators. Note
these equations are based on the boost
converters operating in continues conduction
mode (CCM).
Two phase input current to inductor current
ratio as a function of D (K2(D)):
(
)
(
)
2
1
1
1
1
2
1
2
1
1
2
1
2
>
-
-
-
×
-
≤
-
-
=
D
if
D
D
D
if
D
D
)
D
(
k


Three phase input current to inductor current
ratio as a function of D (K3(D)):
(
)
3
2
3
1
3
2
2
3
1
2
9
9
3
1
3
1
1
3
1
3
2
<
<
≥
-
×
×
+
-
+
×
+
×
-
×
≤
-
-
=
D
if
D
if
D
D
D
D
D
D
D
if
D
D
)
D
(
k

Four phase input current to inductor current
ratio as a function of D (K4(D)):
(
)
(
)
4
3
3
4
4
3
4
2
1
3
8
10
2
1
4
2
4
1
1
1
8
6
2
1
4
1
1
4
1
4
2
2
≥
-
×
<
<
×
+
-
+
×
+
×
-
×
<
<
×
+
-
+
×
+
×
-
×
≤
-
×
-
=
D
if
D
D
D
if
D
D
D
D
D
if
D
D
D
D
D
if
D
D
)
D
(
k

0.0
∆IIN/∆IL1
0.0
1.0
D - Duty Cycle
0.4
0.4
0.6
1.0
0.1
0.2
0.5
0.8
0.9
0.2
0.6
0.8
0.1
0.3
0.5
0.7
0.9
0.7
0.3
K2(D)
K3(D)
K4(D)

Fig. 10. Ratio of input ripple current/inductor
ripple vs. duty cycle (D).

SLUA746

## [стр. 11]

5-9
X. THE TOTAL INDUCTOR ENERGY IS
REDUCED FOR EACH ADDITIONAL PHASE
For each additional interleaved phase added
will reduce the total inductor energy required by
the design, when compared to a single stage
PFC pre-regulator and a n phase interleaved preregulator. The graph in Fig. 11 shows the
percent reduction in total inductor energy
(%_Energy_Reduction) required in the design
going from a single phase boost to 4 phase
interleaved pre-regulator. From this graph it can
be observed that the total energy going from a
single phase to a two phase interleaved power
converter will be reduced by 50%. A three
phase
interleaved
pre-regulator
will
take
roughly 67% less total inductor energy
compared to a single phase approach. A four
phase interleaved PFC pre-regulator will reduce
the total inductor energy required by the design
by 75%. Interleaving reduces the total energy
required by the design which will allow the total
boost inductor volume to be reduced. However,
there is not an easy mathematical calculation to
show the reduction in boost magnetic volume by
interleaving. The reduction in magnetic volume
will vary depending on the magnetic cores that
are selected. The best way to evaluate the
reduction in boost magnetic volume is by going
through a theoretical design using similar
magnetic cores.
In the following equations that calculate
energy and energy reduction n represents the
total number of interleaved phases in the preregulator.
Total
multiple
phase
inductor
energy
(EInterleaved(n)).
2
1 2
1
⎟
⎠
⎞
⎜
⎝
⎛
= ∑
=
n
I
L
)
n
(
E
n
k
d
Interleave


100
×
⎟⎟
⎟
⎟
⎟
⎠
⎞
⎜⎜
⎜
⎜
⎜
⎝
⎛
⎟
⎠
⎞
⎜
⎝
⎛
=
∑
=
1
n
1
-
1
)
eduction(n
%_Energy_R
n
1
k
2

20
Energy Reduction - %
1
Interleaved Phase - n
2
50
70
100
30
40
60
80
90
3
4
10
0

Fig. 11. Percent of total inductor energy
reduction.


SLUA746

## [стр. 12]

5-10
XI. MAGNETIC VOLUME REDUCTION
To show how interleaving PFC preregulators can reduce magnetic volume a
theoretical design of boost inductors was
conducted for a universal 500-W PFC preregulator for a single phase to a four phase PFC
pre-regulator.  The output of the converters was
set at 385 V.  The inductance (L) was chosen
based on the inductance for a four phase design.
This would ensure the inductance would work
for 1- through 4-phase interleaved PFC
applications. Also the amount of boost inductor
ripple chosen was small enough that the ac
portion of the inductor ripple current would be
negligible. The following equations were used
to select the area products required for the
inductors for the four different designs. In the
following equations n represents the number of
interleaved phases in the pre-regulators.
IN(min)
OUT(max)
PEAK
V
2
P
I
×
=
, peak input current

kHz
.
I
.
V
L
PEAK
OUT
100
3
0
4
5
0
2
×
×
×
=

∆B = 0.2 T, change in flux density

2
6
m
A

10

3.95
Cd
×
=
, current density

Ku = 0.4, winding factor

Cd
u
K
I
ΔB
n
I
L
)
n
WaAc(
RMS
PEAK
×
×
×
=


Cd
u
K
2
n
I
ΔB
n
I
L
)
n
WaAc(
PEAK
PEAK
×
×
×
×
=


To do a true comparison of inductor volume
reduction required using the same magnetic core
type. One of the more efficient core sets to wind
is an EE core set. For this example EE cores
from Mag-Inc were selected for the individual
designs. Fig. 12 shows the mechanical drawing
of the EE cores used for this example.
B
A
D
M
F
E
L
C

Fig. 12. Mechanical drawing of Mag-Inc EE
core.
The estimated volume of the boost inductor
(VINDUCTOR) will be based on magnetic core
(VCORE) volume and exposed copper winding
volume (VCOPPER.) This evaluation will not take
into account bobbin size and was also based on
dimension B of the E core being trimmed to get
the area product as close to calculated as
possible.
(
) C
B
2
A
VCORE
×
×
×
=


(
) (
)
L
2
A
M
D
2
2
VCOPPER
×
-
×
×
×
×
=


COPPER
CORE
INDUCTOR
V
V
V
+
=




SLUA746

## [стр. 13]

5-11
To show the reduction in boost inductor
volume Table I. was constructed for a single
phase through a four phase interleaved PFC preregulator. The following equation was used to
calculate the reduction in total inductor
magnetic volume (% Reduction in Inductor
Volume) as compared to a single phase PFC
inductor. VINDUCTOR (1) is the volume of a
tradition single phase pre-regulators boost
inductor. Variable VINDUCTOR(n) is the volume
of a single inductor in a multiphase boost preregulator where n is the total number of phases
in the pre-regulator used in the reduction
comparison. This exercise showed that the
reduction in total magnetic volume was much
less than the total energy reduction that was
calculated previously. However, interleaving
reduced the magnetic volume by 32% to 51%
depending on the number of phases that were
used in the design.
XII. EMI FILTER REDUCTION FOR 3
RD AND 4
TH
PHASE
Form Fig. 10 it can be observed that the
three phase inductor ripple current is completely
cancelled at 33% and 66% duty cycle. In
universal designs a three phase system would
reduce the size of the EMI filter. This is because
the inductor ripple current in a universal design
is at its maximum at the peak of low line which
has a duty cycle around 69%. At this point the
input ripple current would be 10% of the
inductor ripple current. The reduction in input
ripple current should result in a reduction of the
size of the EMI filter.
The four phase system has almost no ripple
current when the converter is operating at 25%,
50%, 75% duty cycle. In European and boost
follower pre-regulators interleaving with four
phases will also reduce the size of the EMI filter
just by interleaving. This is due to the maximum
inductor ripple that occurs at 50% duty cycle
being 100% cancelled at the input of the
converter. Also the 4-phase inductor ripple
current cancellation curves show that overall
input ripple current should be much less than a
two phase interleaved converter for these
applications.

100
(1)
V
)
n
(
V
n
(1)
V
volume

inductor

in

reduction

%
INDUCTOR
INDUCTOR
INDUCTOR
×
⎟⎟
⎠
⎞
⎜⎜
⎝
⎛
×
-
=


TABLE I. BOOST INDUCTOR MAGNETIC VOLUME REDUCTION

WaAc
Mag-Inc.
EE Core
Set
A
B
C
D
E
F
L
M
AC
VINDUCTOR
(h)
% Reduction
In Inductor
Volume
Units
cm4

mm
mm
mm
mm
mm
mm
mm
mm
cm2
cm3
%
# of
Phases













1
23.228
48020-EC
80.00
24.862
19.80
14.962
59.30
19.80
9.90
19.80
3.920
150.099
0
2
5.807
45528-EC
54.90
16.941
20.60
7.841
37.50
16.80
8.38
10.70
3.461
51.118
32
3
2.581
44020-EC
42.80
13.481
15.40
7.381
30.40
11.90
5.94
9.54
1.833
26.480
47
4
1.452
44016-EC
42.80
13.204
9.00
7.104
30.40
11.90
5.94
9.54
1.071
18.554
51
SLUA746

## [стр. 14]

5-12
XIII. OUTPUT CAPACITOR RIPPLE CURRENT
CANCELLATION IN THREE AND FOUR PHASE
INTERLEAVED PFC PRE-REGULATORS
Each individual added phase will continue to
reduce the RMS current in the boost capacitor.
However, the amount of reduction decreases
with each additional phase. Please refer to
Fig. 13 for a normalized output capacitor RMS
current for a single phase boost through 4 phase
interleaved boost converter.
The equations below gives the normalized
output capacitor RMS current (ICOUT1(D))
converter in a single stage PFC pre-regulator as
a function of duty cycle (D).
ICOUT1(D) is the normalized output capacitor
RMS current as a function of D.
(
) (
)
2
1
1
1
1
D
D
)
D
(
ICOUT
-
-
-
=


ICOUT2(D) is the normalized output capacitor
RMS current as a function of D.
(
) (
)
(
) (
)
2
1
2
2
2
2
2
1
2
1
2
1
2
1
2
1
2
2
≥
-
-
-
<
-
-
-
=
D
if
D
D
D
if
D
D

(D)
I COUT2

ICOUT3(D) is the normalized output capacitor
RMS current as a function of D.
(
) (
)
(
) (
)
(
) (
)
3
2
3
3
2
3
3
1
3
2
3
1
3
2
2
2
3
1
3
1
3
1
2
1
3
1
2
2
2
≥
-
-
-
<
<
-
-
-
≤
-
-
-
=
D
if
D
D
D
if
D
D
D
if
D
D
(D)
ICOUT3

ICOUT4(D) is the normalized output capacitor
RMS current as a function of D.
(
) (
)
(
) (
)
(
) (
)
(
) (
)
4
3
4
4
4
4
4
1
4
3
4
2
4
3
4
3
4
1
4
2
4
1
4
2
4
2
4
1
4
1
4
1
4
1
4
1
2
2
2
2
≥
-
-
-
<
<
-
-
-
<
<
-
-
-
≤
-
-
-
=
D
if
D
D
D
if
D
D
D
if
D
D
D
if
D
D

(D)
I COUT4

0.00
ICOUT - Output Current -  A
0.0
1.0
D - Duty Cycle - %
0.4
0.20
0.30
0.50
0.05
0.15
0.25
0.40
0.45
0.2
0.6
0.8
0.1
0.3
0.5
0.7
0.9
0.10
0.35
ICOUT1(D)
ICOUT2(D)
ICOUT4(D)
ICOUT3(D)

Fig. 13. Output capacitor RMS current.





SLUA746

## [стр. 15]

5-13
XIV. EFFICIENCY
Interleaving
and
paralleling
power
converters can increase the efficiency of the
power converter; as long as, the inductor ripple
currents
are
kept
within
reason.
The
semiconductor switching losses will remain
roughly the same. The I2R losses should be
reduced with each additional phase. However, if
the inductor currents have excessive inductor
ripple the higher RMS currents will cause
greater
conduction
losses
driving
down
efficiency. Also at lower power levels where the
switching losses dominate interleaving will not
show a drastic improvement in efficiency.

Single phase conduction losses:
R
I
P
2
SINGLE =

Two phase conduction losses:
R
2
I
R
2
I
R
2
I
P
2
2
2
2_PHASE
=
⎟
⎠
⎞
⎜
⎝
⎛
+
⎟
⎠
⎞
⎜
⎝
⎛
=


Three phase conduction losses:
R
3
I
R
3
I
R
3
I
R
3
I
P
2
2
2
2
3_PHASE
=
⎟
⎠
⎞
⎜
⎝
⎛
+
⎟
⎠
⎞
⎜
⎝
⎛
+
⎟
⎠
⎞
⎜
⎝
⎛
=


Four phase conduction losses:
R
4
I
R
4
I
R
4
I
R
4
I
R
4
I
P
2
2
2
2
2
4_PHASE
=
⎟
⎠
⎞
⎜
⎝
⎛
+
⎟
⎠
⎞
⎜
⎝
⎛
+
⎟
⎠
⎞
⎜
⎝
⎛
+
⎟
⎠
⎞
⎜
⎝
⎛
=

The 350-W prototype had greater than 91%
efficiency over line and load.
89
Efficiency - %
20
100
VOUT - Output Power - %
50
92
94
97
90
91
93
95
96
30
70
80
90
60
40
VIN = 85 V
VIN = 265 V

Fig. 14. Prototype efficiency.
SLUA746

## [стр. 16]

5-14
XV. CONCLUSION
Interleaving PFC pre-regulators has many
benefits. It can reduce EMI and boost inductor
magnetic volume. The amount of reduction
varies and depends on the design requirements
and design tradeoffs. The designer may choose
to reduce either the boost inductor magnetic
volume or cut back the switching frequency to
reduce the size of the EMI filter. In some cases
just adding an additional phase will reduce the
size of the EMI filter. Interleaving also reduces
the RMS current in the boost capacitor greatly
reducing electrical over stress on the capacitor.
However, the complexity and cost of the design
will increase with each additional phase.
XVI. ACKNOWLEDGEMENTS
I would like to thank Isaac Cohen for his
contributions to this article. His consolation and
advice greatly contributed to the quality of this
seminar paper.
REFERENCES
[1] Lazlo Balogh and Richard Redi, "Power
Factor
Correction
with
Interleaved
Boost," APEC 1993, pp. 168-174
[2] Lloyd
Dixon,
"High
Power
Factor
Switching
Pre-regulator
Design
Optimization," Unitrode Power Supply
Design Seminar SEM-700, 1990, Topic 7
[3] Brett Miwa, David Otten, Martin F.
Schlecht, "High Efficiency Power Factor
Correction Using Interleaved Techniques"
IEEE 1992, pp. 557 to 568
[4] Michael O'Loughlin, "350W, Two Phase
Interleaved PFC Pre-regulator Design
Review," Texas Instrument Literature
Number SLUA369, 2006
[5] Michael
O'Loughlin,"HPA117
350W
Interleaved PFC Pre-Regulator User's
Guide," TI Literature Number SLUU228,
2005
[6] Brian Shafer, "Interleaving Contributes
Unique Benefits to Forward Converters
and
Flyback
Converters,"
Texas
Instrument Power Supply Design Seminar,
Topic 4, SEM 1600, 2004
[7] P. Zumel, O. Garcia, J. A. Cobos, J.
Uceda, "EMI Reduction by Interleaving of
Power Converters Presentation," APEC
2004
[8] "UCC28220/1
Dual
Interleave
PWM
Controller,"
Data
Sheet,
Instruments
Literature Number SLUS544, September
2003
[9] "UCC28521/8
Advanced
PFC/PWM
Controller Data Sheet," Texas Instruments
Literature Number SLUS608
SLUA746

## [стр. 17]

IMPORTANT NOTICE
Texas Instruments Incorporated and its subsidiaries (TI) reserve the right to make corrections, enhancements, improvements and other
changes to its semiconductor products and services per JESD46, latest issue, and to discontinue any product or service per JESD48, latest
issue. Buyers should obtain the latest relevant information before placing orders and should verify that such information is current and
complete. All semiconductor products (also referred to herein as "components") are sold subject to TI's terms and conditions of sale
supplied at the time of order acknowledgment.
TI warrants performance of its components to the specifications applicable at the time of sale, in accordance with the warranty in TI's terms
and conditions of sale of semiconductor products. Testing and other quality control techniques are used to the extent TI deems necessary
to support this warranty. Except where mandated by applicable law, testing of all parameters of each component is not necessarily
performed.
TI assumes no liability for applications assistance or the design of Buyers' products. Buyers are responsible for their products and
applications using TI components. To minimize the risks associated with Buyers' products and applications, Buyers should provide
adequate design and operating safeguards.
TI does not warrant or represent that any license, either express or implied, is granted under any patent right, copyright, mask work right, or
other intellectual property right relating to any combination, machine, or process in which TI components or services are used. Information
published by TI regarding third-party products or services does not constitute a license to use such products or services or a warranty or
endorsement thereof. Use of such information may require a license from a third party under the patents or other intellectual property of the
third party, or a license from TI under the patents or other intellectual property of TI.
Reproduction of significant portions of TI information in TI data books or data sheets is permissible only if reproduction is without alteration
and is accompanied by all associated warranties, conditions, limitations, and notices. TI is not responsible or liable for such altered
documentation. Information of third parties may be subject to additional restrictions.
Resale of TI components or services with statements different from or beyond the parameters stated by TI for that component or service
voids all express and any implied warranties for the associated TI component or service and is an unfair and deceptive business practice.
TI is not responsible or liable for any such statements.
Buyer acknowledges and agrees that it is solely responsible for compliance with all legal, regulatory and safety-related requirements
concerning its products, and any use of TI components in its applications, notwithstanding any applications-related information or support
that may be provided by TI. Buyer represents and agrees that it has all the necessary expertise to create and implement safeguards which
anticipate dangerous consequences of failures, monitor failures and their consequences, lessen the likelihood of failures that might cause
harm and take appropriate remedial actions. Buyer will fully indemnify TI and its representatives against any damages arising out of the use
of any TI components in safety-critical applications.
In some cases, TI components may be promoted specifically to facilitate safety-related applications. With such components, TI's goal is to
help enable customers to design and create their own end-product solutions that meet applicable functional safety standards and
requirements. Nonetheless, such components are subject to these terms.
No TI components are authorized for use in FDA Class III (or similar life-critical medical equipment) unless authorized officers of the parties
have executed a special agreement specifically governing such use.
Only those TI components which TI has specifically designated as military grade or "enhanced plastic" are designed and intended for use in
military/aerospace applications or environments. Buyer acknowledges and agrees that any military or aerospace use of TI components
which have not been so designated is solely at the Buyer's risk, and that Buyer is solely responsible for compliance with all legal and
regulatory requirements in connection with such use.
TI has specifically designated certain components as meeting ISO/TS16949 requirements, mainly for automotive use. In any case of use of
non-designated products, TI will not be responsible for any failure to meet ISO/TS16949.
Products
Applications
Audio
www.ti.com/audio
Automotive and Transportation
www.ti.com/automotive
Amplifiers
amplifier.ti.com
Communications and Telecom
www.ti.com/communications
Data Converters
dataconverter.ti.com
Computers and Peripherals
www.ti.com/computers
DLP® Products
www.dlp.com
Consumer Electronics
www.ti.com/consumer-apps
DSP
dsp.ti.com
Energy and Lighting
www.ti.com/energy
Clocks and Timers
www.ti.com/clocks
Industrial
www.ti.com/industrial
Interface
interface.ti.com
Medical
www.ti.com/medical
Logic
logic.ti.com
Security
www.ti.com/security
Power Mgmt
power.ti.com
Space, Avionics and Defense
www.ti.com/space-avionics-defense
Microcontrollers
microcontroller.ti.com
Video and Imaging
www.ti.com/video
RFID
www.ti-rfid.com
OMAP Applications Processors
www.ti.com/omap
TI E2E Community
e2e.ti.com
Wireless Connectivity
www.ti.com/wirelessconnectivity
Mailing Address: Texas Instruments, Post Office Box 655303, Dallas, Texas 75265
Copyright © 2015, Texas Instruments Incorporated
