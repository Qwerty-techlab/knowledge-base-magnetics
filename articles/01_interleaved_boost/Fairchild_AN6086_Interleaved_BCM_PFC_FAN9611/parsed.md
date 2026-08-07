# AN-6086 Design Consideration for Interleaved Boundary Conduction Mode PFC Using FAN9611/12

<!-- FORMULA-WARNING -->
> **Формулы в этом файле недостоверны.** Текстовый слой PDF теряет дробные черты, радикалы и группировку степеней; знак интеграла приходит как `Z` или `R`, знак суммы -- как `P`. Формул вырезано: **39**, читать их в `formulas/` (картинки 300 dpi, перечень в `formulas/INDEX.md`).
<!-- /FORMULA-WARNING -->

> Автоматически извлечено из `source.pdf` скриптом `parse_pdf.py`
> Движок: pymupdf. Страниц: 18 из 18.
> Дата извлечения: 2026-08-07 06:42 UTC

Текст не редактировался. Формулы и таблицы могут быть искажены —
при сомнении сверяться с исходным PDF.

---

## [стр. 1]

www.fairchildsemi.com

© 2009 Fairchild Semiconductor Corporation

www.fairchildsemi.com
Rev. 1.0.4 • 4/22/10
AN-6086
Design Consideration for Interleaved Boundary
Conduction Mode PFC Using FAN9611/12

1. Introduction
This application note presents practical step-by-step design
considerations for an interleaved Boundary-ConductionMode (BCM) Power-Factor-Correction (PFC) converter
employing Fairchild PFC controllers FAN9611 and
FAN9612. It includes designing the inductor and ZeroCurrent-Detection
(ZCD)
circuit,
selecting
the
components, and closing the control loop. The design
procedure is verified through an experimental 400W
prototype converter.
The FAN9611/12 interleaved dual BCM PFC controller
operates two parallel-connected boost power trains 180º
out of phase, extending the maximum practical power level
of this control technique from 200-300W to greater than
800W. Unlike the Continuous Conduction Mode (CCM)
technique often used at this power level, BCM offers
inherent zero-current switching of the boost diodes (no
reverse-recovery losses), which permits the use of less
expensive
diodes
without
sacrificing
efficiency.
Furthermore, the input and output filters can be made
smaller due to ripple cancellation between the power
stages and the effective doubling of the switching
frequency. The advanced line feed-forward with peak
detection circuit minimizes the output voltage variation
during line transients. To guarantee stable operation with
less switching loss at light load, the maximum switching
frequency
is
clamped
at
525kHz.
Interleaved
synchronization
is maintained under all operating
conditions. Protection functions include output overvoltage,
over-current,
open-feedback,
under-voltage
lockout, brownout protection, and secondary latching
over-voltage protection.



Figure 1. Typical Application Circuit of FAN9611 or FAN9612

## [стр. 2]

AN-6086

© 2009 Fairchild Semiconductor Corporation

www.fairchildsemi.com
Rev. 1.0.4 • 4/22/10
2
2. Operation Principle of BCM
Boost PFC Converter
The most widely used operation modes for the boost
converter are the continuous conduction mode (CCM) and
the boundary conduction mode (BCM). These two
descriptive names refer to the current flowing through the
energy storage inductor of the boost converter, as depicted
in Figure 2. As the names indicate, the inductor current in
CCM is continuous; while in BCM, the new switching
period is initiated when the inductor current returns to zero,
which is at the boundary of continuous conduction and
discontinuous conduction operations. Even though the
BCM operation has higher RMS current in the inductor
and switching devices, it allows better switching condition
for the MOSFET and the diode. As shown in Figure 2, the
diode reverse recovery is eliminated and a fast recovery
diode is not needed. MOSFET is also turned on with zero
current, which reduces the switching loss.



Figure 2. CCM vs. BCM Control

The fundamental idea of BCM PFC is that the inductor
current starts from zero in each switching period, as shown
in Figure 3. When the power transistor of the boost
converter is turned on for a fixed time, the peak inductor
current is proportional to the input voltage. Furthermore,
since the current waveform is triangular, the average value
in each switching period is also proportional to the input
voltage. In the case of a sinusoidal input voltage, the input
current of the converter follows the input voltage
waveform with a very high accuracy and draws a sinusoidal
input current from the source. This behavior makes the
boost converter in BCM operation an ideal candidate for
power factor correction.
A by-product of the BCM is that the boost converter runs
with variable switching frequency that depends primarily
on the selected output voltage, the instantaneous value of
the input voltage, the boost inductor value, and the output
power delivered to the load. The operating frequency
changes as the input current follows the sinusoidal input
voltage waveform, as shown in Figure 3. The lowest
frequency occurs at the peak of sinusoidal line voltage.

Figure 3. Operation Waveforms of BCM PFC
The voltage-second balance equation for the inductor is:
( )
(
( ))
IN
ON
OUT
IN
OFF
V
t
t
V
V
t
t
⋅
=
-
⋅



(1)
where VIN(t) is the rectified line voltage.
The switching frequency of BCM boost PFC converter is
obtained as:
,
( )
1
1
| sin(2
) |
1
OUT
IN
SW
ON
OFF
ON
OUT
OUT
IN PK
LINE
ON
OUT
V
V
t
f
t
t
t
V
V
V
f
t
t
V
π
-
=
=
⋅
+
-
⋅
=
⋅


(2)
where VIN,PK is the amplitude of the line voltage and fLINE is
the line frequency.
Figure 4 shows how the MOSFET on time and switching
frequency changes as output power decreases. When the
load decreases, as shown in the right side of Figure 4, the
peak inductor current diminishes with reduced MOSFET
on time and, therefore, the switching frequency increases.
Since this can cause severe switching losses at light load
condition,
the
maximum
switching
frequency
of
FAN9611/12 is limited to 525kHz.

## [стр. 3]

AN-6086

© 2009 Fairchild Semiconductor Corporation

www.fairchildsemi.com
Rev. 1.0.4 • 4/22/10
3

Figure 4. Frequency Variation of BCM PFC

Since the design of filter and inductor for a BCM PFC
converter with variable switching frequency should be
done at minimum frequency condition, it is worthwhile to
examine how the minimum frequency of BCM PFC
converter changes with operating conditions.
Figure 5 shows the minimum switching frequency, which
occurs at the peak of line voltage, as a function of the RMS
line voltage for three output voltage settings. It is
interesting to note that, depending on where the output
voltage is set, the minimum switching frequency may occur
at the minimum or at the maximum line voltage. When the
output voltage is approximately 405V, the minimum
switching frequency is the same for both low line (85VAC)
and high line (265VAC).


Figure 5. Minimum Switching Frequency vs. RMS Line
Voltage (L = 390µH, POUT = 200W)


3. Interleaving of BCM Boost PFC
One important characteristic of a BCM boost converter is
the high ripple current of the boost inductor, which goes
from zero to a controlled peak value in every switching
period. Accordingly, the power switch is also stressed with
high peak currents. In addition, the high ripple current must
be filtered by an EMI filter to meet high-frequency noise
regulations enforced for equipment connected to the mains.
These effects usually limit the practical output power level
of the converter below 300W. However, operating two
parallel-connected boost power stages 180º out of phase, as
shown in Figure 6; the high peak current and over-sized
EMI filter problems are solved, extending the maximum
practical power level of this control technique to greater
than 800W. This technique is called interleaving.



Figure 6. Interleaving Operation of BCM Boost PFC

Interleaving operation provides many advantages over the
single BCM PFC operation. The losses are distributed in the
switching devices, which also spreads the dissipated power
and eases the thermal management of the power stage
design. Interleaving also yields great benefits on EMI filter
size reduction since the effective switching frequency seen at
the input side of the converter is doubled, while the
combined ripple current is minimized due to the ripple
current cancellation, as shown in the waveforms of Figure 6.

## [стр. 4]

AN-6086

© 2009 Fairchild Semiconductor Corporation

www.fairchildsemi.com
Rev. 1.0.4 • 4/22/10
4
4. Design Considerations
In this section, a design procedure is presented using the
schematic in Figure 7 as a reference. A 400W PFC
application with universal input range is selected as a
design example. The design specifications are as follows:
- Line voltage range: 85~265VAC (universal input),
50Hz
- Nominal output voltage and current: 400V/1A (400W)
- Holdup time requirement: Output voltage should not
drop below 330V during one line cycle
- Output voltage ripple: less than 8Vp-p
- Minimum switching frequency: higher than 50kHz
- Control Bandwidth: 5~10Hz
- Brownout protection line voltage: 70VAC
The design is for two identical converters, which deliver
half of the total output power (200W), respectively. VDD is
assumed to be supplied from auxiliary power supply.



Figure 7. Reference Circuit for Design Example of Interleaving BCM Boost PFC

[STEP-1] Boost Inductor Design
The boost inductor value is determined by the output
power and the minimum switching frequency. From
Equation 2, the minimum frequency with a given line
voltage and MOSFET on time is obtained as:
,
2
1
OUT
LINE
SW MIN
ON
OUT
V
V
f
t
V
-
=
⋅



   (3)
where:
VLINE is RMS line voltage;
tON is the MOSFET conduction time; and
VOUT is the output voltage.
The MOSFET conduction time with a given line voltage at
a nominal output power is given as:
,
2
2
OUT CH
ON
LINE
P
L
t
V
η
⋅
⋅
=
⋅




   (4)
where:
η is the efficiency;
L is the boost inductance; and
POUT,CH is the nominal output power per channel
Using Equation 4, the minimum switching frequency of
Equation 3 can be expressed as:
2
LINE
LINE
,
,
2
2
OUT
SW MIN
OUT CH
OUT
V
V
V
f
P
L
V
η ⋅
-
=
⋅
⋅
⋅

   (5)

## [стр. 5]

AN-6086

© 2009 Fairchild Semiconductor Corporation

www.fairchildsemi.com
Rev. 1.0.4 • 4/22/10
5
Therefore, once the output voltage and minimum switching
frequency are set, the inductor value is given as:
2
,
,
,
,
2
2
LINE MINF
OUT
LINE MINF
OUT CH
SW MIN
OUT
V
V
V
L
P
f
V
η ⋅
-
=
⋅
⋅
⋅

  (6)
where VLINE,MINF is the RMS line voltage that results in
minimum switching frequency.
For universal input range, VLINE,MINF is the maximum line
voltage (265VAC) when VOUT is set at lower than 405V;
while VLINE,MINF is minimum line voltage (85VAC) when
VOUT is set at higher than 405V.
As the minimum frequency decreases, the switching loss is
reduced, while the inductor size and line filter size
increase. Thus, the minimum switching frequency should
be determined by the trade-off between efficiency and the
size of magnetic components. The minimum switching
frequency must be above the minimum frequency of
FAN9611/12, which is set at 16.5kHz to prevent audible
noise.
Once the inductance value is decided, the maximum peak
inductor current at the nominal output power is obtained as:
,
.
,
2 2
OUT CH
L PK
LINE MIN
P
I
V
η
⋅
=
⋅

(7)
where VLINE,MIN is the minimum line voltage.
The number of turns of boost inductor should be
determined considering the core saturation. The minimum
number is given as:
,
L PK
BOOST
e
I
L
N
A
B
⋅
≥
⋅Δ

(8)
where is Ae is the cross-sectional area of core and ΔB is the
maximum flux swing of the core in Tesla. ΔB should be set
below the saturation flux density.
Figure 8 shows the typical B-H characteristics of ferrite
core from TDK (PC45). Since the saturation flux density
(ΔB) decreases as the temperature increases, the high
temperature characteristics should be considered.

Figure 8. Typical B-H Curves of Ferrite Core
(Design Example) Since the output voltage is 400V, the
minimum frequency occurs at high-line (265VAC) and
full-load condition. Assuming the efficiency is 95% and
selecting the minimum frequency as 52kHz, the inductor
value is obtained as:
2
,
,
,
,
2
3
2
2
0.95 265
400
2 265
202
400
2 200 52 10
LINE MINF
OUT
LINE MINF
OUT CH
SW MIN
OUT
V
V
V
L
P
f
V
H
η
μ
⋅
-
=
⋅
⋅
⋅
⋅
-
⋅
=
⋅
=
⋅
⋅
×


The maximum peak inductor current at nominal output
power is calculated as:
,
,
,
2 2
2 2 200
7
0.95 85
OUT CH
L PK
LINE MIN
P
I
A
V
η
⋅
⋅
=
=
=
⋅
⋅


Assuming PQ3230 core (PC45, Ae=161mm2) is used and
setting ΔB as 0.3T, the primary winding should be:
6
,
6
7 202 10
29
161 10
0.3
L PK
BOOST
e
I
L
N
turns
A
B
-
-
⋅
⋅
×
≥
=
=
⋅Δ
×
⋅

Thus, the number of turns (NBOOST) of boost inductor is
determined as 30 turns.

[STEP-2] Inductor Auxiliary Winding Design
Figure 9 shows the inductor current and voltage waveforms
of a BCM boost converter. FAN9611/12 indirectly detects
the inductor zero current point using an auxiliary winding
of the boost inductor. Since the zero current detection
(ZCD) circuit in FAN9611/12 is designed to turn on the
MOSFET when the slope of auxiliary winding voltage
becomes zero, no special consideration for timing delay is
required for the auxiliary winding design.
AUX
IN
BOOST
N
V
N
(
)
AUX
OUT
IN
BOOST
N
V
V
N
-

Figure 9. ZCD Detection Waveforms
The voltage of the ZCD pin is clamped near zero and the
resistor RZCD limits the current of the ZCD pin below 1mA as:

## [стр. 6]

AN-6086

© 2009 Fairchild Semiconductor Corporation

www.fairchildsemi.com
Rev. 1.0.4 • 4/22/10
6
1
OUT
AUX
ZCD
BOOST
V
N
R
mA
N
>
⋅




   (9)
For low-power applications, such as adaptors, the supply
voltage (VDD) for FAN9611/12 is supplied by auxiliary
winding of inductor, as shown in Figure 10. Since the
auxiliary winding voltage varies extensively within half of
line cycle, DC blocking capacitor (CB) is used to guarantee
stable VDD voltage.
When supplying VDD using the auxiliary winding, the turns
ratio should be determined as:
2
BOOST
OUT
AUX
Z
N
V
N
N
V
=
≅




 (10)
where VZ is the Zener diode voltage for VDD.
The reason for setting the turns ratio such that peak-to-peak
voltage of auxiliary winding is around twice of VZ is to
guarantee stable VDD supply without under-voltage lockout
(UVLO) during startup.
AUX
OUT
BOOST
N
V
N
(
( ))
AUX
OUT
IN
BOOST
N
V
V
t
N
-
( )
AUX
IN
BOOST
N
V
t N
-

Figure 10. VDD Supply Circuit using Auxiliary Winding

The average current through the startup resistor should be
larger than the startup current (100μA), determined as:
,
2 2
100
LINE MIN
START
START
V
I
A
R
μ
π
=
>



(11)
The startup resistor also should be determined by
considering the minimum startup time, which is given as:
,
2 2
(
100
)
ON
DD
START
LINE MIN
START
V
C
t
V
A
R
μ
π
=
-



 (12)
where VON is UVLO start voltage for VDD and
CDD is the total capacitance of capacitors connected to the
VDD pin.
Typically 20~50μF of electrolytic capacitor (CVDD2) is used
together with 2~4μF of bypass capacitor (CVDD1).
The power consumption in the startup resistor is obtained as:
2
,
LINE MAX
LOSS
START
V
P
R
=




 (13)
(Design Example) Selecting the turns ratio of the
inductor (NBOOST/NAUX) as 10, NAUX is obtained as 3 and
the value of RZCD is given as:
400
3
40
1
1
30
OUT
AUX
ZCD
BOOST
V
N
R
k
mA
N
mA
>
⋅
=
⋅
=
Ω
RZCD is selected as 47kΩ.
Assuming that VDD is supplied from auxiliary power
supply, VDD supply circuit using the auxiliary winding is
not included in this example.

[STEP-3] Design VIN Sense Circuit
Since the RMS value of AC line voltage is directly
proportional to the peak of the line voltage, FAN9611/12
detects the peak value of input voltage to sense the RMS
value of the line voltage, which permits a simple voltage
divider for line voltage sensing, as shown in Figure 11. The
detected line voltage information is used for line undervoltage lockout (UVLO), and line feed-forward for PWM
control.
When the peak of VIN pin voltage drops below 0.95V, the
line UVLO (brownout protection) is triggered and
FAN9611/12 stops operating. The RMS value of the line
voltage that causes line UVLO is given as:
1
2
.
2
0.95
(
)
2
IN
IN
LINE UVLO
AC
IN
R
R
V
V
R
+
=
⋅


 (14)
The internal switched current source allows UVLO
hysteresis on line voltage as:
1
1
,
2
,
(
1)
2
2
IN
IN
IN HYS
IN
LINE HYS
R
R
R
R
V
A
μ
+
+
=
⋅
 (VAC )               (15)
From Equation 15, RIN,HYS with a given hysteresis of line
voltage is obtained as:
.
2
,
1
1
2
2
(
)
2
LINE HYS
IN
IN HYS
IN
IN
IN
V
R
R
R
A
R
R
μ
=
-
⋅
+


 (16)

## [стр. 7]

AN-6086

© 2009 Fairchild Semiconductor Corporation

www.fairchildsemi.com
Rev. 1.0.4 • 4/22/10
7

Figure 11. Input Voltage Sensing
The line peak detection circuit is saturated when VIN
exceeds 3.7V, as depicted in Figure 11. Therefore, line
feedforward does not work for VIN higher than 3.7V, as
illustrated in Figure 12. The minimum brownout protection
trip point that allows proper line feedforward operation for
universal line range is 66VAC (265VAC×0.925/3.7). When
the brownout protection threshold is lower than 68VAC for
universal range input, line feedforward can be lost for high
line and, therefore, the limited output power increases as
line voltage increases:
.
.
2
(
)
3.7
MAX NO FF
MAX
IN
OUT
OUT
V
P
P
=
⋅

(17)
Another effect of VIN sensing saturation is that the phase
management threshold as a percentage of nominal output
power increases as peak of VIN increases above 3.7V
because the line feedforward does not work above 3.7V.
Since FAN9611/12 uses peak detection for the line voltage
sensing, it is typical to use a small capacitor (CINF) to
bypass switching noise. To minimize the effect of sensing
delay, the RC time constant between RIN2 and CINF should
be smaller than 5% of AC line period.


Figure 12. VIN Feedforward Range

 (Design Example) Setting the brown-out protection
threshold at 70VAC and selecting RIN1=2MΩ, RIN2 is
obtained as:
1
2
,
6
( 2
/ 0.925 1)
2 10
18.9
2 70/ 0.925 1
IN
IN
LINE UVLO
R
R
V
k
=
-
×
=
=
Ω
⋅
-

Assuming the hysteresis for brownout protection is
3VAC, RIN,HYS is obtained as:
.
2
,
1
1
2
3
6
6
6
3
2
(
)
2
2 3
18.9 10
(
2 10 )
1.1
2 10
2 10
18.9 10
LINE HYS
IN
IN HYS
IN
IN
IN
V
R
R
R
A
R
R
k
μ
-
=
-
⋅
+
⋅
×
=
-×
⋅
=
Ω
×
×
+
×

RIN.HYS can be omitted since the hysteresis of 2.8VAC is
obtained without RIN,HYS from Equation 15. CINF is
selected as 10nF, which results in RC time constant as:
3
9
2
.
(
)
18.9 10 10 10
189
IN
IN HYS
INF
R
R
C
s
τ
μ
-
=
+
⋅
=
×
⋅
×
=


[STEP-4] Determine MOT Pin Resistor
The on time of the gate drive signal is proportional to the
compensation voltage as shown in Figure 13. The
compensation voltage is internally clamped at 4.3V where
the maximum on time is obtained. The Maximum On Time
(MOT) of the gate drive signal of each channel is
programmed by the resistor on the MOT pin as:
12
2
1
2
,
2
230 10
(
)
2
IN
IN
ON MAX
MOT
IN
LINE
R
R
t
R
R
V
-
+
=
⋅
×

(18)
As can be observed in Equation 18, the maximum on time
is inversely proportional to the square of line voltage due
to the line feed-forward operation.
The MOT resistor should be determined by considering the
output power since the maximum on time limits the
maximum output power during overload condition as:
2
,
,
,
2
LINE
MAX CH
MAX
OUT CH
ON MAX
V
P
K
P
t
L
η
⋅
=
⋅
=

(19)
where PMAX,CH is the limited maximum output power per
channel and KMAX is maximum power limiting factor,
which is a ratio between the limited maximum output
power and nominal output power.
Considering the tolerances of inductor, resistor, and
controller variation; it is typical to set the limited maximum
power as 20~30% higher than the nominal output power
(KMAX = 1.2~1.3).

## [стр. 8]

AN-6086

© 2009 Fairchild Semiconductor Corporation

www.fairchildsemi.com
Rev. 1.0.4 • 4/22/10
8
TON
VCOMP
4.3
0.73
0.93
TON
MAX
13% of POUT
MAX (TON
MAX)
18% of POUT
MAX (TON
MAX)
POUT
MAX
POUT
0.2

Figure 13. VCOMP vs. On Time of Gate Drive Signal

FAN9611/12 determines the phase management according
to the COMP pin voltage (0.73V and 0.93V). Since the
COMP pin voltage is proportional to the output power, the
power levels for phase shedding and adding are given as
percentages of limited maximum power, as shown in
Figure 13. Thus, the maximum power limiting factor
affects the actual phase management thresholds as
percentages of nominal output power, as shown in Figure
14, which shows an example where the maximum power
limit is 170% of the nominal output power. In that case, the
actual phase management thresholds are 22% and 31% of
nominal output power, which can maximize the efficiency
at 20% of nominal load for 80-plus efficiency requirement.
In this way, the phase management thresholds can be
adjusted upward by adjusting the maximum on time
(through RMOT).
Output Power Normalized to PO
MAX
# of phase
operating
2
1
13%
18%
100%
50%
Output Power Normalized to PO
NOMINAL
# of phase
operating
2
1
22% 31%
100%
50%
PO
MAX=1.7 PO
NOMINAL
170%

Figure 14. Phase Management Threshold

When the resulting maximum power limit to obtain the
desired phase management threshold is too high compared
to the nominal output power, the maximum power limit
level can be reduced using clamping circuit on COMP pin,
as shown in Figure 15. The COMP pin voltage is clamped
at 3.3V and the resulting maximum power limit level is
reduced from 170% to 130% of nominal output power.



Figure 15. COMP Voltage Clamping Circuit and Phase
Management Threshold

After determining the limited maximum output power, the
boost inductor maximum flux density should be examined
to make sure that the inductor is not saturated during
overload condition. The maximum flux density of boost
inductor during overload condition is given by:
,
max
L PK
MAX
e
BOOST
I
K
L
B
A
N
⋅
⋅
=
⋅

(20)

## [стр. 9]

AN-6086

© 2009 Fairchild Semiconductor Corporation

www.fairchildsemi.com
Rev. 1.0.4 • 4/22/10
9
(Design Example) Setting the limited output power as
120% of nominal output power, the maximum on time is
given as:
,
,
,
2
2
,
,
6
2
2
(
) 2
(1.2 200) 2 202 10
14.1
85
0.95
MAX CH
MAX
OUT CH
ON MAX
LINE MIN
LINE MIN
P
L
K
P
L
t
V
V
s
η
η
μ
-
⋅
⋅
⋅
=
=
⋅
⋅
⋅
⋅⋅
×
=
=
⋅

Then, the resistor on MOT pin is obtained as:

,
IN2
,
2
12
IN1
IN2
6
2
12
2
(
)
230 10
14.1 10
18.9
2 85
(
)
78
18.9
2000
230 10
ON MAX
LINE MIN
MOT
t
R
V
R
R
R
k
-
-
-
=
+
×
×
⋅
⋅
=
=
Ω
+
×

The maximum flux density during overload condition is
obtained as:
6
,
max
6
7 1.2 202 10
161 10
30
0.35
L PK
MAX
e
BOOST
I
K
L
B
A
N
tesla
-
-
⋅
⋅
⋅
⋅
×
=
=
⋅
×
⋅
=


[STEP-5] Design Feedback Circuit
To regulate the output voltage to a desired value, the
voltage divider for feedback should be designed to result in
3V to the feedback (FB) pin, expressed as:
2
1
2
3
FB
OUT
FB
FB
R
V
V
R
R
⋅
=
+

(21)
(Design Example) Selecting RFB1 as 1MΩ, RFB2 is
obtained as:
6
1
2
1 10
7.56
400
1
1
3
3
FB
FB
OUT
R
R
k
V
×
=
=
=
Ω
-
-

[STEP-6] Design OVP Circuit
FAN9611/12 has two levels of over-voltage protection
(OVP) for the output. Non-latching OVP is combined with
the feedback (FB) pin and trips when the output voltage
exceeds 108% of its nominal value. The latching OVP uses
dedicated pin and trips when the OVP pin voltage exceeds
an independent threshold of 3.5V, expressed as:
2
,
1
2
3.5
FB
OUT LATCH
FB
FB
R
V
V
R
R
⋅
=
+

(22)
When the latching OVP is combined with FB pin, it trips at
115% of the nominal output voltage.
(Design Example) Selecting OVP level as 472V and
ROV1 as 2MΩ, ROV2 is obtained as:
6
1
2
,
2 10
14.9
472
1
1
3.5
3.5
OV
OV
OUT LATCH
R
R
k
V
×
=
=
=
Ω
-
-



[STEP-7] Determine current sensing resistor
It is typical to set the pulse-by-current limit level a little
higher than the maximum inductor current at maximum
power limit condition as:
,
,
,
2 2
MAX CH
CS LIM
LINE MIN
P
I
V
η
≥
⋅
⋅

(23)
Then, the sensing resistor is selected as:
.
0.2
CS
CS LIM
R
I
=

(24)
(Design Example)
,
,
,
200 1.2
2 2
2 2
8.4
85 0.95
MAX CH
CS LIM
LINE MIN
P
I
A
V
η
⋅
≥
⋅
=
⋅
=
⋅
⋅

Choosing ICS.LIM as 9.1A (10% margin on 8.4A), the
sensing resistor is selected as:

.
0.2
0.2
0.022
9.1
CS
CS LIM
R
I
=
=
=
Ω

[STEP-8] Output Capacitor Selection
The output voltage ripple should be considered when
selecting the output capacitor. Figure 16 shows the twice
line frequency ripple on the output voltage. With a given
specification of output ripple, the condition for the output
capacitor is obtained as:
,
2
OUT
OUT
LINE
OUT RIPPLE
I
C
f
V
π
>
⋅
⋅

(25)
where IOUT is total nominal output current of two boost
PFC stage and VOUT,RIPPLE is the peak-to-peak output
voltage ripple specification.
Since too large ripple on the output voltage may cause
premature OVP during normal operation, the peak-to-peak
ripple specification should be smaller than 15% of the
nominal output voltage.
The holdup time also should be considered when
determining the output capacitor as:
2
2
,
2 OUT
HOLD
OUT
OUT
OUT MIN
P
t
C
V
V
⋅
>
-

(26)
where:
POUT is total nominal output power of two boost PFC stage
(2POUT,CH);
tHOLD is the required holdup time; and
VOUT,MIN is the allowable minimum output voltage during
the holdup time.

## [стр. 10]

AN-6086

© 2009 Fairchild Semiconductor Corporation

www.fairchildsemi.com
Rev. 1.0.4 • 4/22/10
10
,
(1 cos(4
))
D AVG
OUT
LINE
I
I
f
t
π
=
-
⋅
⋅
OUT
I
,
2
OUT
OUT RIPPLE
LINE
OUT
I
V
f
C
π
=
OUT
V
D
I
,
D AVG
I

Figure 16. Output Voltage Ripple

(Design Example) With the ripple specification of
8Vp-p, the capacitor should be:

,
1
398
2
2
50 8
OUT
OUT
LINE
OUT RIPPLE
I
C
F
f
V
μ
π
π
>
=
=
⋅
⋅
⋅
⋅

Since minimum allowable output voltage during one
cycle line (20ms) drop-outs is 330V, the capacitor
should be:
3
2
2
2
2
,
2
2 400 20 10
313
400
330
OUT
HOLD
OUT
OUT
OUT MIN
P
t
C
F
V
V
μ
-
⋅
⋅
⋅
×
>
=
=
-
-

Thus, two 220μF capacitors in parallel are selected
for the output capacitor.

[STEP-9] Design Compensation Network
The boost PFC power stage can be modeled as shown in
Figure 17. Since FAN9611/12 employs line feed-forward,
the power stage transfer function becomes independent of
the line voltage. Then, the power stage can be modeled as a
voltage-controlled current source supplying RC network.

Figure 17. Small Signal Modeling of the Power Stage

By averaging the diode current during the half line cycle,
the low frequency behavior of the voltage controlled
current source of Figure 17 is obtained as:
,
(
0.2)
4.1
COMP
D LF
OUT
MAX
V
I
I
K
-
=
⋅
⋅

(27)
where
IOUT
is
total
nominal
output
current
corresponding to POUT, VCOMP is compensation pin
voltage, 0.2V is PWM offset voltage and 4.1 is error
amplifier control range (refer to Figure 13).
Then, the low-frequency, small-signal, control-to-output
transfer function is obtained as:
ˆ
1
ˆ
4.1
2
1
2
OUT
OUT
MAX
L
COMP
P
v
I
K
R
s
v
f
π
⋅
=
⋅
⋅
+

(28)
where
2
2
P
L
OUT
f
R C
π
=
⋅
and
RL is the output load resistance in a given load condition.
Figure 18 shows the variation of the control-to-output
transfer function for different loads. As can be seen, the
characteristics at frequencies above the pole are unchanged
while the pole moves as load changes. Since the low
frequency gain increases as load decreases, the light load
condition is the worst condition for feedback loop
compensation. Assuming the load resistance is infinite, the
control-to-output transfer function at light load condition is
obtained from Equation 28 as:
@
,
ˆ
1
|
ˆ
4.1
OUT
OUT
MAX
LIGHT LOAD
COMP
OUT
v
I
K
v
sC
⋅
≅
⋅

(29)

## [стр. 11]

AN-6086

© 2009 Fairchild Semiconductor Corporation

www.fairchildsemi.com
Rev. 1.0.4 • 4/22/10
11

Figure 18. Control-to-Output Transfer Function
Proportional and integration (PI) control with high
frequency pole is typically used for compensation, as
shown in Figure 19. The compensation zero (fCZ)
introduces phase boost, while the high frequency
compensation pole (fCP) attenuates the switching ripple.
The transfer function of the compensation network is
obtained as:
1
ˆ
2
2
ˆ
1
2
COMP
CZ
I
OUT
CP
s
v
f
f
s
v
s
f
π
π
π
+
=
⋅
+

(30)
where
,
,
,
3
80
/
,
2
1
,
2
1
2
I
OUT
COMP LF
CZ
COMP
COMP LF
CP
COMP
COMP HF
A V
f
V
C
f
R
C
f
R
C
μ
π
π
π
=
⋅
⋅
=
⋅
⋅
=
⋅
⋅


,
1
2
CZ
COMP
COMP LF
f
R
C
π
=
⋅
^
^
COMP
OUT
v
v
,
1
2
CP
COMP
COMP HF
f
R
C
π
=
⋅
,
,
10
COMP HF
COMP LF
C
C
≤
,
2
1
2
SS REF
FB
FB
FB
OUT
V
R
R
R
V
=
+

Figure 19. Compensation Network
The procedure to design the feedback loop is as follows:
(a) Determine the crossover frequency (fC) around
1/10~1/5 of line frequency. Since the control-to-output
transfer function of power stage has -20dB/dec slope
and -90o phase at the crossover frequency, as shown in
Figure 20; it is required to place the zero of the
compensation network (fCZ) around the crossover
frequency so that 45° phase margin is obtained. Then,
the capacitor CCOMP,LF is determined as:
,
2
80
/
3
4.1
(2
)
OUT
MAX
COMP LF
OUT
OUT
C
A V I
K
C
V
C
f
μ
π
⋅
⋅
=
⋅
⋅
⋅

(31)
To place the compensation zero at the crossover frequency,
the compensation resistor is obtained as:
,
1
2
COMP
C
COMP LF
R
f
C
π
=
⋅
⋅

(32)
(b) Place compensator high-frequency pole (fCP) at least a
decade higher than fC to ensure that it does not
interfere with the phase margin of the voltage
regulation loop at its crossover frequency. It should
also be sufficiently lower than the switching frequency
of the converter so noise can be effectively attenuated.
Then, the capacitor CCOMP,HF is determined as:
,
1
2
COMP HF
CP
COMP
C
f
R
π
=
⋅
⋅

(33)

Figure 20. Compensation Network Design

## [стр. 12]

AN-6086

© 2009 Fairchild Semiconductor Corporation

www.fairchildsemi.com
Rev. 1.0.4 • 4/22/10
12
(Design Example) Choosing the crossover frequency
(control bandwidth) at 5Hz, CCOMP,LF is obtained as:
,
2
4
6
2
80
/
3
4.1
(2
)
10
1 1.2
3
405
400
4.1 440 10
(2
5)
OUT
MAX
COMP LF
OUT
OUT
C
A V I
K
C
V
C
f
nF
μ
π
π
-
-
⋅
⋅
=
⋅
⋅
⋅
⋅⋅
=
⋅
=
⋅
×
⋅
⋅

Actual CCOMP,LF is determined as 390nF since it is the
closest value among the off-the-shelf capacitors. Then,
RCOMP is obtained as:
9
,
1
1
82
2
2
5 390 10
COMP
C
COMP LF
R
k
f
C
π
π
-
=
=
=
Ω
⋅
⋅
⋅⋅
×

Selecting the high-frequency pole as 120Hz, CCOMP,HF is
obtained as:
,
3
1
1
16.3
2
2
120 82 10
COMP HF
CP
COMP
C
nF
f
R
π
π
=
=
=
⋅
⋅
⋅
×

Actual COMP,HF is determined as 15nF since it is the
closest value among the off-the-shelf capacitors. These
components result in a control loop with a bandwidth of
6Hz and phase margin of 45° as below. The actual
bandwidth is a little larger than the asymptotic design
[STEP-10] Soft-Start Capacitor Selection
FAN9611/12 employs closed-loop soft-start, where the
reference of the error amplifier is gradually increased to the
final value corresponding to the nominal output voltage. The
reference is also actively managed during the soft-start
period to prevent the reference running away from the
feedback voltage. The slope of the voltage reference is made
a function of the error amplifier output voltage (VCOMP), i.e.
the output power of the converter. The soft-start time is then
adjusted according to load condition.
It is typical to set he maximum rising speed of the soft-start
capacitor such that it is 30%~60% of that of the output
voltage, defined by the maximum power limit as:
,
5
0.3
0.6
OUT
MAX
OUT
MAX
OUT
OUT
SS
SS REF
OUT
OUT
I
K
I
K
A
C
V
C
V
C
V
μ
⋅
⋅
⋅
<
<
⋅
⋅
⋅
⋅

(34)
where VSS,REF is the final value of soft-start capacitor
voltage. Then, the condition for the soft-start capacitor is
given as:
,
,
5
5
0.6
0.3
OUT
OUT
OUT
OUT
SS
OUT
MAX
SS REF
OUT
MAX
SS REF
A C
V
A C
V
C
I
K
V
I
K
V
μ
μ
⋅
⋅
⋅
⋅
<
<
⋅
⋅
⋅
⋅
⋅
⋅
 (35)
(Design Example) Since two 220μF capacitors in
parallel are selected for the output capacitor:

,
,
5
5
0.6
0.3
OUT
OUT
OUT
OUT
SS
OUT
MAX
SS REF
OUT
MAX
SS REF
A C
V
A C
V
C
I
K
V
I
K
V
μ
μ
⋅
⋅
⋅
⋅
<
<
⋅
⋅
⋅
⋅
⋅
⋅

406
813
SS
nF
C
nF
<
<

Thus, a 470nF capacitor is selected for the soft-start
capacitor.

[STEP-11] Line Filter Capacitor Selection
It is typical to use small bypass capacitors across bridge
rectifier output stage to filter the switching current ripple,
as shown in Figure 21. Since the impedance of the line
filter inductor at line frequency is negligible compared to
the impedance of the capacitors, the line frequency
behavior of the line filter stage can be simply modeled, as
shown in Figure 21. Even though the bypass capacitors
absorb switching ripple current, it also generates
circulating capacitor current, which leads the line voltage
by 90o, as shown in Figure 22. As observed, the circulating
current through the capacitor is added to the load current
and generates displacement between line voltage and line
current.
The displacement angle is given by:
2
,
1
2
tan (
)
LINE MAX
LINE
EQ
OUT
V
f
C
P
η
π
θ
-
⋅
⋅
⋅
=

(36)
where CEQ is the equivalent capacitance that appears across
the AC line (CEQ=CF1+CF2+CHF).
The resultant displacement factor is:
cos( )
DF
θ
=

(37)
Since the displacement factor is related to power factor, the
capacitors in the line filter stage should be selected
carefully. With a given minimum displacement factor
(DFMIN) at full load condition, the allowable effective input
capacitance is obtained as:
1
2
,
tan(cos (
))
2
OUT
EQ
MIN
LINE MAX
LINE
P
C
DF
V
f
η
π
-
<
⋅
⋅
⋅

(38)

## [стр. 13]

AN-6086

© 2009 Fairchild Semiconductor Corporation

www.fairchildsemi.com
Rev. 1.0.4 • 4/22/10
13
(Design
Example)
Assuming
the
minimum
displacement factor at full load is 0.99, the equivalent
input capacitance is obtained as:

1
2
,
1
2
tan(cos (
))
2
400
tan(cos (0.99))
2.7
0.95 265
2
50
OUT
EQ
MIN
LINE MAX
LINE
P
C
DF
V
f
F
η
π
μ
π
-
-
<
⋅
⋅
⋅
<
⋅
=
⋅
⋅
⋅

Thus, the sum of the capacitors in the input side
should be smaller than 2.7µF.


Figure 21. Equivalent Circuit of Line Filter Stage
θ

Figure 22. Line Current Displacement

## [стр. 14]

AN-6086

© 2009 Fairchild Semiconductor Corporation

www.fairchildsemi.com
Rev. 1.0.4 • 4/22/10
14
PCB Layout Guidelines
For high-power applications, two or more PCB layers are
recommended to effectively use the ground pattern to
minimize the switching noise interference from the two
high-frequency outputs. The following guidelines are
recommended for all layout designs, but especially strongly
for the single-layer PCB designs.
Power Ground and Analog Ground

Power ground (PGND) and analog ground (AGND)
should meet at one point only.

All the control components should be connected to
AGND without sharing the trace with PGND.

The return path for the gate drive current and VDD
capacitor should be connected to the PGND pin.

The ground loops between the driver outputs
(DRV1/2), MOSFETs, and PGND should be
minimized.

Adding the by-pass capacitor for noise on the VDD pin
is recommended. It should be connected as close to the
pin as possible.
Gate Drive Pattern

The gate drive pattern should be wide enough to
handle 1A peak current.

The gate drive pattern should be as short as possible to
minimize interference.
Current Sensing

Current Sensing should be as short as possible.

To minimize switching noise, current sensing should
not make a loop.
Input Voltage Sensing (VIN)

Since the impedance of voltage divider is large and
FAN9611/12 detects the peak of the line voltage, the
VIN pin can be sensitive to the switching noise.
Therefore, the trace connected to this pin should not
cross traces with high di/dt to minimize the
interference.

The noise bypass capacitor for VIN should be
connected as close to the pin as possible.

Figure 23 shows the single-layer PCB example, where the
FAN9611/12 is on the bottom of PCB (SOIC package).

ZCD1
ZCD2
5VB
MOT
AGND
SS
CS1
CS2
VDD
DRV1
DRV2
PGND
VIN
OVP
COMP
FB
1
2
3
4
5
6
7
8
9
16
15
14
13
12
11
10

Figure 23. Single-Layer PCB Layout Example

## [стр. 15]

AN-6086

© 2009 Fairchild Semiconductor Corporation

www.fairchildsemi.com
Rev. 1.0.4 • 4/22/10
15
Design Summary
Figure 24 shows the final schematic of the 400W interleaved BCM Boost PFC design example. PQ3230 cores are used for
the boost inductors.
CS2
CS1
VDD
DRV1
DRV2
PGND
VIN
OVP
FB
COMP
SS
AGND
MOT
5VB
ZCD2
ZCD1
1
2
3
4
5
6
7
8
16
15
14
13
12
11
10
9
FAN9612
LF
CF1
CF2
CHF1
L1
L2
N1
N2
N1
N2
Q1
Q2
RG
RG
Rsense
Rsense
D1
D2
CVDD2
RZCD2
RZCD1
RIN1
RIN2
CIN
CV1
CV2
RV1
CSS
RMOT
C5V
RFB1
RFB2
ROV2
ROV1
CO
470nF
LF
CF3
470nF
470nF
470nF
150nF
GBJ1006
2M
18.9k
10nF
220uF
220uF
200uH
200uH
(N1:N2=10:1)
(N1:N2=10:1)
RURP860
RURP860
47k
47k
78k
82k
390nF
15nF
22uF
15
15
0.022
0.022
FDPF18N50
FDPF18N50
220nF
1M
7.56k
15k
2M
VDD from Aux
power Supply
CVDD1
2.2uF
150nF
CHF2


Figure 24. Final Schematic of Design Example


Figure 25. Boost Inductor Specification

Table 1. Winding Specification

Pin
Diameter / Thickness
Turns
N1
5 Æ 3
0.1mm × 100 (Litz wire)
30
Insulation Tape
0.05mm
3
N2
2 Æ 4
0.2mm
3
Insulation Tape
0.05mm
3

Core: PQ3230 (Ae=161 mm2)
Bobbin: PQ3230
Inductance: 200μH

## [стр. 16]

AN-6086

© 2009 Fairchild Semiconductor Corporation

www.fairchildsemi.com
Rev. 1.0.4 • 4/22/10
16
6. Experimental Verification
To show the validity of the design procedure presented in
this application note, the converter of the design example
was built and tested. All the circuit components are used as
designed in the design example.
Figure 26 and Figure 27 show the inductor current ripple
cancellation
for
115VAC
and
230VAC
condition,
respectively. As can be observed, the sum of two inductor
currents has very small ripple due to the interleaving
operation.
Figure 28 shows the brown-out protection. As designed,
the protection trips when the line voltage drops below
70VAC. Figure 29 and Figure 30 show the soft-start
waveforms at full load for 115VAC and 230VAC line
voltage, respectively. As observed, there is no overshoot
on the output voltage during startup. Figure 31 shows the
measured efficiency for 115VAC and 230VAC line voltage.
The full-load efficiency is 96.4% and 98.2% for 115VAC
and 230VAC, respectively. The power factor is shown in
Table 2. The power factor at full load is 0.993 and 0.988
for 115VAC and 230VAC, respectively.

CH2: Inductor current IL1 (5A/div)
CH4: Sum of two inductor current IL1+IL2 (5A/div)
Figure 26. Inductor Current Waveforms at 115VAC

CH2: Inductor current IL1 (5A/div)
CH4: Sum of two inductor current IL1+IL2 (5A/div)
Figure 27. Inductor Current Waveforms at 230VAC

CH1: Gate drive signal VGS1 (20V/div)
CH2:
Line
current
(5A/div),
CH4:
Line
voltage
(100VA/div)
Figure 28. Brownout Protection

CH1: Gate drive signal VGS1 (20V/div)
CH3: Output voltage (100V/div)
CH4: Line current (5A/div)
Figure 29. Soft-Start Waveforms at Full-Load and
115VAC Line Condition

CH1: Gate drive signal VGS1 (20V/div)
CH3: Output voltage (100V/div)
CH4: Line current (5A/div)
Figure 30. Soft-Start Waveforms at Full-Load and
230VAC Line Condition

## [стр. 17]

AN-6086

© 2009 Fairchild Semiconductor Corporation

www.fairchildsemi.com
Rev. 1.0.4 • 4/22/10
17

Figure 31. Measured Efficiency
Table 2. Measured Power Factor
Line Voltage
100% Load
75% Load 50% Load
115VAC
0.993
0.990
0.984
230VAC
0.988
0.983
0.974


Definition of Terms
η is the efficiency.
ΔB is the maximum flux swing of the core at nominal output power in Tesla.
Ae is the cross-sectional area of core.
BMAX is the maximum flux density of boost inductor at maximum output power in Tesla.
CDD is the total capacitance of capacitors connected to the VDD pin.
fC is the crossover frequency.
fCP is the high frequency compensation pole to attenuate the switching ripple.
fCZ is the compensation zero.
fLINE is the line frequency.
fSW,MIN is the minimum switching frequency.
ICS,LIM is the pulse-by-pulse current limit level determined by sensing resistor.
IL,PK is the maximum peak inductor current at the nominal output power.
IOUT is total nominal output current of two boost PFC stages.
IOUT,MAX is the maximum output current, which corresponds to PMAX.
KMAX is maximum power limiting factor (a ratio between the limited maximum output power and nominal output power).
L is the boost inductance.
NAUX is the number of turns of auxiliary winding in boost inductor.
NBOOST is the number of turns of primary winding in boost inductor.
PMAX is the limited maximum output power of two boost PFC stages (2PMAX,CH).
PMAX,CH is the limited maximum output power per channel.
POUT is total nominal output power of two boost PFC stages (2POUT,CH).
POUT,CH is the nominal output power per channel.
tHOLD is the required hold-up time.
tON,MAX is the maximum on time determined by the MOT resistor.
VCOMP is compensation pin voltage.
VIN(t) is the rectified line voltage.
VIN,PK is the amplitude of line voltage.
VLINE is RMS line voltage.
VLINE,HYS is the hysteresis RMS line voltage of brownout protection.
VLINE,MAX is the maximum RMS line voltage.
VLINE,MIN is the minimum RMS line voltage.
VLINE,MINF is the RMS line voltage that results in minimum switching frequency.
VLINE,OVP is the line OVP trip point in RMS.
VON is UVLO start voltage for VDD.
VOUT is the PFC output voltage.
VOUT,LATCH is the output OVP trip point.
VOUT,MIN is the allowable minimum output voltage during the hold-up time.
VOUT,RIPPLE is the peak-to-peak output voltage ripple.
VREF,SS is the reference voltage for soft-start and feedback compensation.

## [стр. 18]

AN-6086

© 2009 Fairchild Semiconductor Corporation

www.fairchildsemi.com
Rev. 1.0.4 • 4/22/10
18

References
[1] Fairchild Datasheet FAN9611 / FAN9612 Interleaved Dual BCM, PFC Controller
[2] Fairchild Application Note AN-6027, Design of Power Factor Correction Circuit Using FAN7530
[3] Fairchild Power Seminar 2008-2009 Paper, Understanding Interleaved Boundary Conduction Mode PFC Converters
[4] Fairchild Evaluation Board User Guide FEB279, 400W Evaluation Board using FAN9612 ((AN-8018)
[5] Fairchild Application Note AN-8021, Building Variable Output Voltage Boost PFC Converters Using FAN9611/12
[6] Fairchild Evaluation Board User Guide FEB301, 400W Single-Layer Evaluation Board using FAN9612 (AN-8026)


Related Datasheets
FAN9611 / FAN9612 - Interleaved Dual BCM PFC Controllers
FDPF18N50 - 500V N-Channel MOSFET, UniFET
RURP860 - 8A, 600V UltraFast Diodes


Author
Hangseok Choi / Ph. D
He received B.S., M.S., and Ph.D degrees in electrical engineering from Seoul National University in 1996, 1999, and
2002, respectively. From 2002 to 2007, he worked for Fairchild Semiconductor in Korea as a system and application
engineer. He is currently working for Fairchild Semiconductor in NH, USA, as a principal system and application engineer.
His research interests include soft-switching techniques, modeling, and control of converters.



Important Notice
DISCLAIMER
FAIRCHILD SEMICONDUCTOR RESERVES THE RIGHT TO MAKE CHANGES WITHOUT FURTHER NOTICE TO ANY PRODUCTS
HEREIN TO IMPROVE RELIABILITY, FUNCTION, OR DESIGN. FAIRCHILD DOES NOT ASSUME ANY LIABILITY ARISING OUT OF
THE APPLICATION OR USE OF ANY PRODUCT OR CIRCUIT DESCRIBED HEREIN; NEITHER DOES IT CONVEY ANY LICENSE
UNDER ITS PATENT RIGHTS, NOR THE RIGHTS OF OTHERS.

LIFE SUPPORT POLICY
FAIRCHILD'S PRODUCTS ARE NOT AUTHORIZED FOR USE AS CRITICAL COMPONENTS IN LIFE SUPPORT DEVICES OR
SYSTEMS WITHOUT THE EXPRESS WRITTEN APPROVAL OF THE PRESIDENT OF FAIRCHILD SEMICONDUCTOR
CORPORATION.
As used herein:

1.
Life support devices or systems are devices or systems
which, (a) are intended for surgical implant into the body,
or (b) support or sustain life, or (c) whose failure to perform
when properly used in accordance with instructions for use
provided in the labeling, can be reasonably expected to
result in significant injury to the user.
2.
A critical component is any component of a life support
device or system whose failure to perform can be
reasonably expected to cause the failure of the life support
device or system, or to affect its safety or effectiveness.
