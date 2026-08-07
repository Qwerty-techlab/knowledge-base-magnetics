# UCC28070 300W Interleaved PFC Pre-regulator Design Review

<!-- FORMULA-WARNING -->
> **Формулы в этом файле недостоверны.** Текстовый слой PDF теряет дробные черты, радикалы и группировку степеней; знак интеграла приходит как `Z` или `R`, знак суммы -- как `P`. Формул вырезано: **54**, читать их в `formulas/` (картинки 300 dpi, перечень в `formulas/INDEX.md`).
<!-- /FORMULA-WARNING -->

> Автоматически извлечено из `source.pdf` скриптом `parse_pdf.py`
> Движок: pymupdf. Страниц: 27 из 27.
> Дата извлечения: 2026-08-07 06:42 UTC

Текст не редактировался. Формулы и таблицы могут быть искажены —
при сомнении сверяться с исходным PDF.

---

## [стр. 1]

Application Report
SLUA479B-August 2008-Revised July 2010
UCC28070 300-W Interleaved PFC Pre-Regulator Design
Review
MIchael O'Loughlin........................................................................ PMP - Power Supply Control Products
ABSTRACT
In higher power applications to utilize the full line power and reduce line current harmonics PFC
Pre-regulators are generally required. In these high power applications interleaving PFC stages can
reduce inductor volume and reduce input and output capacitor ripple current. This results in smaller overall
magnetic volume and filter capacitor volume increasing the converters overall power density. This is made
possible through distributing the power over two interleaved boost converters and the inductor ripple
current cancellation that occurs with interleaving, reference [5]. This application note will review the design
of a 300W two-phase interleaved power factor corrected (PFC) pre-regulator. This power converter
achieves PFC with the use of the UCC28070 interleaved PFC controller, reference [7].
1
Design Goals
The specifications for this design were chosen based on the power requirements of a medium power LCD
TV.
Table 1. Design Specifications
PARAMETER
MIN
TYP
MAX
UNITS
85
265
VIN
RMS input voltage
(VIN_MIN)
(VIN_MAX)
V
VOUT
Output voltage
390
47 Hz
Line frequency
63
Hz
(fLINE)
PF
Power factor at maximum load
0.90
POUT
Output power
300
W
h
Full load efficiency
90%
fs
Individual phase switching frequency
200
kHz
1
SLUA479B-August 2008-Revised July 2010
UCC28070 300-W Interleaved PFC Pre-Regulator -Design Review
Copyright © 2008-2010, Texas Instruments Incorporated

## [стр. 2]

+
-
Vin
VOUT
12V to 21V
Q2
RB2
RA1
RB1
Q1
L2
L1
D2
D1
COUT
RA2
CPCA
RRDM
T2
CCDR
CB2
RPK1
1
2
3
4
5
6
7
8
9
10
20
19
18
17
16
15
14
13
12
11
CAOA
CAOB
PKLMT
GND
VAO
VINAC
VSENSE
CSA
CSB
RT
CDR
SS
GDB
GDA
IMO
VCC
RSYNTH
VREF
DMAX
RDM
RIMO
RPK2
CZCA
RZCA
CPCB
CZCB
RZCB
CPV
CZV
RZV
CB3
0.1uF
0.1uF
CSS
T1
T1
T2
RSYN
DRA
RSA
RSB
RR
RR
CFA
CFB
RFA
RFB
220pF
220pF
1k
1k
DRB
RDMX
RRT
DB
UCC28070
IIN
IL1
IL2
CB1
1.2nF
CB4
1.2nF
ROB
ROA
4.7pF
CRR
4.7pF
CRR
DPA2
DPB2
DPA1
DPB1
CTA
CTB
RTA
RTB
VCC=13V
GDA
GDB
Schematic
www.ti.com
2
Schematic
UCC28070 PFC controller in a two-phase average current mode control interleaved PFC pre-regulator.
Figure 1. Typical Average Current Mode Interleaved PFC Pre-Regulator
2
UCC28070 300-W Interleaved PFC Pre-Regulator -Design Review
SLUA479B-August 2008-Revised July 2010
Copyright © 2008-2010, Texas Instruments Incorporated

## [стр. 3]

IN
L1
I
K(D) =
I
D
D
1 2D
K(D) =
if D is < 05 = 0.5
1 D
-
-
2D 1
K(D) =
if D is > 0.5
D
-
D - Duty Cycle
K(D)=DIIN/DIL1
www.ti.com
Inductor Selection
3
Inductor Selection
One of the benefits of interleaved PFC boost pre-regulators is inductor ripple current reduction that is seen
at the input of the converter. The following equations and Figure 2 show the ratio of input ripple current
(ΔIIN) to individual inductor ripple current (ΔIL1) in a two-phase interleaved PFC as a function of duty cycle
(D). Because of this inductor ripple current cancellation, the designer can allow each inductor to have
more inductor ripple current than in a single stage design.
(1)
(2)
(3)
Figure 2. Input Inductor Ripple Current Cancellation
The boost inductors (L1 and L2) are selected based on the maximum allowable input ripple current. In
universal applications (e.g., 85 V to 265 V RMS input) the maximum input ripple current occurs at the
peak of low line and for this design the maximum input ripple current was set to 30% of the peak nominal
input current at low line.
3
SLUA479B-August 2008-Revised July 2010
UCC28070 300-W Interleaved PFC Pre-Regulator -Design Review
Copyright © 2008-2010, Texas Instruments Incorporated

## [стр. 4]

OUT
IN_MIN
PLL
OUT
V
V
2
390V
85V 2
D
=
=
0.69
V
390 V
-
-
»
PLL
2
0.69
1
K(D
) =
= 0.55
0.69
´
-
OUT
IN_MIN
PLL
P
2 × 0.3
300W
2
0.3
IL =
=
3.0 A
V
K(D
)
85V
0.90
0.55
h
´
´
´
D
»
´
´
´
´
IN_MIN
PLL
s
V
2
D
85V
2
0.69
L1 = L2 =
=
140 H
IL ×
2.96A
200 kHz
´
´
´
´
»
D
´
u
f
2
2
IN_MIN
OUT
IN_MIN
OUT
s
OUT
L1_RMS
L2_RMS
0
IN_MIN
V
2sin( )
V
V
2sin( )
P
L1
V
1
2
I
= I
=
+
V
12
p
q
q
h
p
æ
ö
-
æ
ö
ç
÷
´
ç
÷
ç
÷
´
ç
÷
ò
ç
÷
´
ç
÷
ç
÷
ç
÷
ç
÷
è
ø
è
ø
f
2
2
L1_RMS
L2_RMS
0
85V 2sin( )
390V
85V 2sin( )
300W
1
140 H
200kHz
390V
2
I
= I
=
+
2A
85V
0.90
12
p
q
q
p
æ
ö
-
æ
ö
ç
÷
´
ç
÷
´
ç
÷
»
ç
÷
ò
ç
÷
´
ç
÷
ç
÷
ç
÷
ç
÷
è
ø
è
ø
u
MIN
MIN
L1
= L2
= 140 H
u
MAX
MAX
L1
= L2
= 350 H
u
MIN
MAX
AVG
AVG
L1
+ L1
140 H + 350 H
L1
= L2
=
=
= 245 H
2
2
u
u
u
Inductor Selection
www.ti.com
The following calculations are used to select the appropriate inductance for L1 and L2. Where, variable
DPLL is the converter's duty cycle at the peak of low line operation. Variable K(DPLL) is the ratio of input
current to inductor ripple current at the peak of low line operation. ∆IL is the boost inductor ripple current
at the peak of low line based on the converters input ripple current requirements.
(4)
(5)
The following equation can be used to calculate total inductor RMS current (IL1_RMS and IL2_RMS).
(6)
(7)
A 140-mH boost inductor from Cooper Electronic Technologies part number CTX16-18060 was chosen for
the design. The inductance during normal operation will swing from 140mH to 350mH.
(8)
(9)
The average inductance is calculated for current loop compensation purposes. This will be used in the
current loop compensation section of the application note:
(10)
4
UCC28070 300-W Interleaved PFC Pre-Regulator -Design Review
SLUA479B-August 2008-Revised July 2010
Copyright © 2008-2010, Texas Instruments Incorporated

## [стр. 5]

(
)
OUT
LINE
OUT
2
2
2
2
OUT
OUT
2
P
2
300W
47 Hz
C
=
192 F
V
(V
0.75)
(390V)
292.5V
´
´
³
»
-
´
-
f
u
OUT
C
= 200 μF
OUT
RIPPLE
OUT
LINE
OUT
2 300W
2
P
1
0.90
V
=
=
14.5V
V
2
2
C
390V
2π
2
47Hz
200 μF
h
p
´
´
»
´
´
´
´
´
´
´
f
OUT
COUT_LF
OUT
P
300W
I
=
=
0.604A
V
2
0.90
390V
2
h
»
´
´
(
)
2
2
2
OUT
OUT
COUT_HF
COUT_LF
OUT
IN_MIN
P
16
V
I
=
I
V
6
V
2
h
h
p
æ
ö
´
ç
÷
-
-
ç
÷
´
è
ø
(
)
2
2
2
COUT_HF
300W
16
390V
I
=
(0.90)
0.604
1.0A
0.90
390V
6
85V 2
p
æ
ö
´
-
-
»
ç
÷
ç
÷
´
´
è
ø
www.ti.com
Output Capacitor Selection
4
Output Capacitor Selection
The output capacitor (COUT) is selected based on holdup requirements.
(11)
Two 100-mF capacitors were used in parallel for the output capacitor.
(12)
For this size capacitor the output peak to peak voltage ripple (VRIPPLE) is:
(13)
In addition to holdup requirements, a capacitor must be selected so that it can withstand both the
low-frequency RMS current (ICOUT_LF) and the high-frequency RMS current (ICOUT_HF). High-voltage
electrolytic capacitors generally have both low frequency (100 Hz to 120 Hz) and high frequency RMS
current ratings on their data sheets.
(14)
(15)
(16)
5
SLUA479B-August 2008-Revised July 2010
UCC28070 300-W Interleaved PFC Pre-Regulator -Design Review
Copyright © 2008-2010, Texas Instruments Incorporated

## [стр. 6]

OUT
L1
PEAK
IN_MIN
P
2
I
300W
2
2.97A
I
=
+
1.2 =
+
1.2
5.1A
2
V
2
2 × 85V
0.90
2
h
æ
ö
æ
ö
´
D
´
»
ç
÷
ç
÷
ç
÷
ç
÷
´
´
´
è
ø
è
ø
OUT
IN_MIN
DS
OUT
IN_MIN
P
300W
16
V
2
16
85V 2
η
0.90
I
=
2
=
2
1.685A
3
V
3
390V
2
V
2
2
85V 2
p
p
´
´
-
-
»
´
´
´
´
´
´
OUT
D
OUT
P
300W
I
=
=
0.39A
V
2
390V
»
´
Power Semiconductor Selection (Q1, Q2, D1, D2)
www.ti.com
5
Power Semiconductor Selection (Q1, Q2, D1, D2)
The selection of Q1, Q2, D1, and D2 are based on the power requirements of the design. Application note
(SLUA369), UCC28528 350-W Two Phase Interleaved PFC Pre-regulator, explains how to select power
semiconductor components for interleaved PFC pre-regulators using average current mode control
techniques, reference [4]. To meet the power requirements of this design IRFB11N50A N channel FETs
from IR were chosen for Q1 and Q2. To reduce reverse recovery losses SiC diodes CSD10060G from
CREE were chosen for the design.
Boost Diode (D1, D2) and FET (Q1, Q2) peak current (IPEAK) calculation:
A factor of 1.2 was added to the equation for added design margin.
(17)
Q1 and Q2 RMS current (IDS) calculation:
(18)
D1 and D2's average current calculation (ID):
(19)
6
UCC28070 300-W Interleaved PFC Pre-Regulator -Design Review
SLUA479B-August 2008-Revised July 2010
Copyright © 2008-2010, Texas Instruments Incorporated

## [стр. 7]

S
PEAK
CT
P
RS
N
I
5.1A
N
=
=
= 51
N
I
0.1A
³
CT
N
= 50
OUT
IN_MIN
S
M
PEAK
OUT
s
CT
V
V
2
V
3.7V
390V
85V 2
L
=
6.24mH
I
5.1A
V
390V
0.02 200kHz
0.02
50
N
-
-
³
´
´
»
´
´
´
´ f
M
L
= 8.25 mH
S
SA
SB
PEAK
CT
0.9
V
0.9
3.7V
50
R
= R
=
=
32.5
I
0.102A
N
´
´
´
»
W
S
R
= 33.2 W
S
MAX
R
MAX
R
D
33.2
× 0.97
R
=
1 k
1
D
1
0.97
´
W
³
W
-
-
;
P
R
PEAK
R
S
N
5.1A
1 k
V
= I
R
=
103V
N
50
´
W
´
´
³
www.ti.com
Current Sense Transformers Setup and Selection (T1, T2, DRA, DRB)
6
Current Sense Transformers Setup and Selection (T1, T2, DRA, DRB)
The current sense transformer is selected to handle IPEAK and have a peak current sense signal (IRS) of
roughly 100 mA.
(20)
For this design a current sense transformer with a turns ratio (NCT) of 50 was chosen for the design.
(21)
The magnetizing inductance (LM) of the current sense transformer should be selected or designed so the
magnetizing current is less than 2% of the maximum current sense signal. The following equation
calculates the minimum LM where VS is the maximum current sense signal voltage. For this design a
current sense transformer was designed by Cooper Electronic Technologies (CTX16-18294) with a
magnetizing inductance of 8.25 mH.
(22)
(23)
Selection of the current sense resistors (RSA and RSB ) is based on the peak current limit signal (VS) and
the peak current on the secondary side of the current sense transformer. A factor of 0.9 was multiplied by
the current sense signal to leave room for the 10% PWM ramp that is used to make this design more
noise immune at lighter loads.
(24)
Select a standard resistor for the design:
(25)
Resistor RR is used to reset the current sense transformer:
(26)
Current sense transformer's rectifying diodes (DR) need to be designed to withstand the current sense
transformers reset voltage (VR):
(27)
7
SLUA479B-August 2008-Revised July 2010
UCC28070 300-W Interleaved PFC Pre-Regulator -Design Review
Copyright © 2008-2010, Texas Instruments Incorporated

## [стр. 8]

GDA
IL1
0A
VRSA
VOFF
0V
Current Sense Transformers Setup and Selection (T1, T2, DRA, DRB)
www.ti.com
To improve noise immunity at extremely light loads, a PWM ramp with a dc offset is recommended to be
added to the current sense signals. Electrical components RTA, RTB, CTA, CTB, DPA1, DPA2, DPB1, and DPB2
form a PWM ramp that is activated and deactivated by the gate drive outputs of the UCC28070. Resistor
ROA and ROB add a DC offset to the CS resistors (RSA and RSB).
When the inductor current becomes discontinuous the boost inductors ring with the parasitic capacitances
in the boost stages. This inductor current rings through the CTs causing a false current sense signal.
Refer to the following graphical representation of what the current sense signal looks like when the
inductor current goes discontinuous. Note that the inductor current and VRSA may vary from this graphical
representation depending on how much inductor ringing is in the design when the unit goes discontinuous.
Figure 3. False Current Sense Signal
8
UCC28070 300-W Interleaved PFC Pre-Regulator -Design Review
SLUA479B-August 2008-Revised July 2010
Copyright © 2008-2010, Texas Instruments Incorporated

## [стр. 9]

OFF
V
= 0.2 V
(
)
(
)
VCC
OFF
SA
OA
OB
OFF
V
V
R
13V
0.2V
33.2
R
= R
=
=
2.1 k
V
0.2V
-
-
´
»
W
OA
R
= 2.05 kW
(
)
(
)
VCC
s
OFF
DPA2
SA
TA
TB
s
OFF
V
(V
0.1 V
+V
R
13V
(3.7V
0.1 0.2V)+0.6V
33.2
R
=R
=
=
2.62 k
V
0.1 V
3.7V
0.1 0.2V
-
´
-
-
´
-
´
»
W
´
-
´
-
TA
TB
R
= R
= 2.49 kW
TA
TB
SA
S
1
C
= C
=
50 nF
R
3
»
´
´
f
TA
C
= 47 nF
www.ti.com
Current Sense Transformers Setup and Selection (T1, T2, DRA, DRB)
To properly select the offset (VOFF) just requires adjusting resistors ROA and ROB to add a dc offset to the
current sense resistors, that is high enough to block DRA and DRB from conducting when a false current
sense signals is present. This occurs when the inductors are operating with discontinuous inductor current
and was described above in detail. Setting the offset to 200 mV is a good starting point and may need to
be adjusted based on individual design criteria and the amount of noise and parasitic elements present in
the system.
(28)
(29)
Select a standard resistor for the design:
(30)
(31)
Chose a standard resistor for the design:
(32)
(33)
A standard capacitor needs to be chosen for the design:
(34)
9
SLUA479B-August 2008-Revised July 2010
UCC28070 300-W Interleaved PFC Pre-Regulator -Design Review
Copyright © 2008-2010, Texas Instruments Incorporated

## [стр. 10]

S
PK1
PK2
REF
S
V
R
3.7V
3.65 kΩ
R
=
=
5.9 k
V
V
6V
3.7V
´
´
»
W
-
-
9
9
RT
s
7.5
10
Hz
7.5
10
Hz
R
=
=
= 37.5 k
200 kHz
´
W ´
´
W ´
W
f
RT
R
= 37.4 kW
(
)
(
)
DMX
RT
MAX
R
= R
2
D
1 = 37.4 kΩ 2
0.97
1 = 35 k
´
-
´
-
W
DMX
R
= 34.8 kW
3
A
R
M
=
W
A
B
OUT
VREF
R
3V
3MΩ
2
R
=
=
23.3 k
VREF
390V
3V
V
2
´
´
»
W
-
-
B
R
= 23.2 kW
A
B
OVP
B
R
+ R
3M
+ 23.2 k
V
= 3.18V
= 3.18V
414V
R
23.2 k
W
W
»
W
Setting Up Peak Current Limiting (RPK1, RPK2)
www.ti.com
7
Setting Up Peak Current Limiting (RPK1, RPK2)
The UCC28070 has an adjustable peak current limit comparator that can be set up by selecting RPK1 and
calculating the required RPK2. For this design to keep the reset voltage of the current sense transformer
manageable the peak current sense signal (VS) was set to 3.7 V.
(35)
Converter Timing and Maximum Duty Cycle Clamp
Resistor RRT and RDMX set up converter timing and the maximum PWM duty cycle clamp:
(36)
A standard resistor was selected for the design:
(37)
Resistor RDMX was selected to set the maximum duty cycle clamp (DMAX) to 0.97:
(38)
Chose a standard resistor for the design:
(39)
8
Programming VOUT
Resistor RA is selected to minimize the error due to VSENSE input bias current and to minimize loading on
the power line when the PFC is disabled. Construct resistor RA from two or more resistors in series to
meet high voltage requirements. Resistor RB is sized to program the converters output voltage (VOUT).
(40)
(41)
A standard resistor was chosen for the design.
(42)
The resistor divider formed by RA and RB from the output voltage to the VSENSE pin also sets the over
voltage protection threshold (VOVP).
(43)
10
UCC28070 300-W Interleaved PFC Pre-Regulator -Design Review
SLUA479B-August 2008-Revised July 2010
Copyright © 2008-2010, Texas Instruments Incorporated

## [стр. 11]

V
gm
= 70
S
m
VREF
OUT
V
3V
H =
=
0.0077
V
390V
»
O
RIPPLE
V
VAO
0.03
3.2V
0.03
Z
=
=
12.3 k
V
H
gm
14.5V
0.0077
70
S
m
D
´
´
»
W
´
´
´
´
PV
LINE
o
1
1
C
=
=
138nF
2
2
Z
2
2
47Hz
12.3k
p
p
»
´
´
´
´
´
´
W
f
PV
C
= 150 nF
www.ti.com
VINAC Divider Setup
9
VINAC Divider Setup
The UCC28070 also requires sensing the line input for proper operation. This requires a divider from the
rectified line voltage to the VINAC pin of the UCC28070. For simplicity the UCC28070 was designed to
use the same resistor divider values as the VSENSE pin. Resistors RA and RB need to be the same ratio
for the VINAC voltage divider as thouse in the VSENSE voltage divider to ensure the UCC28070 controller
operates correctly. Please refer to the applications schematic for proper component placement.
10
Voltage Loop Configuration
The methodology used to compensate the voltage loop is based on the compensation methodology
developed by Lloyd Dixon. A detailed explanation of this compensation scheme written by Mr. Dixon can
be found in the 1990 Unitrode Power Supply Design SEM700, High Power Factor Switching Pre-regulator
Design Optimization, Topic 7, reference [2].
Capacitor CPV is sized to attenuate low frequency ripple to less than 3% of the voltage amplifier output
range. This will ensure good power factor and low input current harmonic distortion.
Voltage Amplifier Transconductance Amplifier gain:
(44)
Voltage Divider Feedback Gain:
(45)
Output impedance (ZO) is required to attenuate the low frequency boost capacitor output ripple (VRIPPLE) to
less than 3% of the effective voltage amplifier output range (ΔVAO). This impedance is set by properly
selecting feedback capacitor CPV:
(46)
(47)
Choose as standard capacitor for the design:
(48)
11
SLUA479B-August 2008-Revised July 2010
UCC28070 300-W Interleaved PFC Pre-Regulator -Design Review
Copyright © 2008-2010, Texas Instruments Incorporated

## [стр. 12]

VAO = 3.2 V
D
OUT
OUT
CV
V
OUT
PV
1
P
j
2
C
1
η
=
H
gm
VAO
V
2
C
p
p
´
´
´
´
´
´
D
´
´
f
CV
300W
1
1
0.90
=
0.0077 70 S
11Hz
3.2V
2
200 F 390V
2
150nF
m
p
m
p
´
´
´
´
»
´
´
´
´
´
f
ZV
CV
PV
1
1
R
=
=
96.4 k
2
C
2
10.6Hz
150nF
p
p
»
W
´
´
´
´
f
ZV
R
= 100 kW
ZV
CV
ZV
1
1
C
=
=
1.5
F
11Hz
2
100 k
2
R
10
10
m
p
p
»
´
´
W
´
´
f
Voltage Loop Configuration
www.ti.com
For the highest possible power factor the voltage loop crossover frequency (fCV) needs to be set based on
the following equation:
(49)
(50)
(51)
Voltage compensation resistor RZV is then sized to put a pole at the converter's voltage loop crossover
frequency:
(52)
Select a standard resistor for the design:
(53)
Voltage compensation capacitor CZV is used to increase the dc gain of the voltage loop and gives some
added phase margin before crossover. The zero added to the voltage loop needs to be set at 1/10th the
crossover frequency.
(54)
12
UCC28070 300-W Interleaved PFC Pre-Regulator -Design Review
SLUA479B-August 2008-Revised July 2010
Copyright © 2008-2010, Texas Instruments Incorporated

## [стр. 13]

(
)
(
)
VAO
ZV
ZV
CV
V
OUT
ZV
ZV
PV
ZV
PV
ZV
PV
V
j
2
R
C
+1
G
( ) =
= H
gm
V
j
2
f
R
C
C
j
2
C
+ C
+1
C
+C
p
p
p
D
´
´
´
´
´
´
D
æ
ö
´
´
´
´
´
´
´
´
ç
÷
è
ø
f
f
f
OUT
OUT
OUT
PSV
VAO
OUT
1
P
j
2
C
V
η
G
( ) =
=
V
VAO
V
p
æ
ö
ç
÷
´
´
´
D
è
ø
´
D
D
f
f
(
)
PSV
CV
TvdB(
) = 20log G
(
)
G
(
)
´
f
f
f
1
10
100
1 .103
90
60
30
0
30
60
90
90
90
-
TvdB f( )
1 103
´
1
f
1
10
100
1 .103
0
15
30
45
60
75
90
90
0
qv f( )
1 103
´
1
f
www.ti.com
Voltage Loop Configuration
The following equations can be used to estimate voltage compensation network gain, voltage loop power
stage gain and voltage loop gain. These equations can also be used to graphically check loop stability.
Voltage Compensation Network Gain (GCV(f)) as function of frequency:
(55)
Voltage Loop Power Stage Gain (GPSV(f)) as function of frequency:
(56)
Voltage Loop Gain in dB (TvdB(f)) as function of frequency:
(57)
Figure 4 shows the theoretical loop gain (TvdB(f)) as a function of frequency and Figure 5 shows the
theoretical loop phase (qv(f)) as a function of frequency. From these figures it can be observed that the
voltage loop crossed over at roughly 9 Hz with a phase margin of 60 degrees. Compensating the voltage
loop is not an exact science and should be checked with a network analyzer and adjusted if necessary.
Figure 4. Theoretical Voltage Loop Gain (TvdB(f))
Figure 5. Theoretical Voltage Loop Phase (qv(f))
13
SLUA479B-August 2008-Revised July 2010
UCC28070 300-W Interleaved PFC Pre-Regulator -Design Review
Copyright © 2008-2010, Texas Instruments Incorporated

## [стр. 14]

B
CT
MAX
A
B
SYN
S
R
23.2 k
N
L1
50
350
H
R
+ R
3 M
+ 23.2 k
R
=
=
40.5 k
R
0.1 nF
33.2
0.1nF
m
W
´
´
´
W
W
»
W
´
W ´
SYN
R
= 38.3 kW
(
)
(
)
-6
-6
INAC
VAOMAX
2
VFF
17
10 A
V
V
1V
17
10 A
0.76V 5V
1V
IMO =
=
130
A
K
0.398V
m
´
´
-
´
´
-
»
(
)
A
B
I
B
0.76V
R
+ R
0.76V
(3M
+ 23.2k
)
V =
=
70V
R
2
23.2k
2
´
´
W
W
»
´
W ´
2
1 1
2
1
1 1
300
2
1
33 2
2 458
2
1
2
0 92
72
50
OUT
S
CT
.
P
.
W
V
R
.
.
V
V
N
.
V
h
´
´
=
´
´
=
´
´
´
W »
´
´
´
2
IMO
V
2.458 V
R
=
=
18.9k
IMO
130
A
»
W
m
IMO
R
= 19.6 kW
OUT
S
CT
PSC
s
AVG
RAMP
1
1
V
R
390 V
33.2
N
50
G
=
=
2.1
200 kHz
2
245
H
4.0V
2
L1
V
10
10
p
m
p
´
´
´
W ´
»
´
´
´
´
´
´
f
Current Loop Compensation
www.ti.com
11
Current Loop Compensation
Setting up the current synthesizer is accomplished by correctly selecting RSYN:
The inductor used in this design example swings from 350 mH to 140 mH from no load to maximum load.
When calculating RSYN the highest inductance value (L1MAX) should be used.
(58)
Chose a standard resistor:
(59)
The IMO resistor needs to be set with the following equation to center the digitized multiplier for universal
line applications:
(60)
(61)
(62)
(63)
Choose a standard resistor close to the calculated value:
(64)
The current loop in a PFC converter is generally designed to crossover at between 1/10th and 1/6th the
converter's switching frequency. The current loop in this design example is going to be designed to
crossover at 1/10th of the single stage's switching frequency. In order to properly compensate the current
loop it is required to calculate the current loop's power stage gain (GPS) at the current loop's crossover and
properly select passive components RZC1/2, CZC1/2 and CPC1/2:
(65)
14
UCC28070 300-W Interleaved PFC Pre-Regulator -Design Review
SLUA479B-August 2008-Revised July 2010
Copyright © 2008-2010, Texas Instruments Incorporated

## [стр. 15]

C
gm
= 100
S
m
ZC1
ZC2
C
PSC
1
1
R
= R
=
=
= 4.8 k
gm
G
100
S
2.1
m
W
´
´
ZC1
ZC2
s
ZC
1
1
C
= C
=
=
1.7nF
200 kHz
2
4.8 k
2
× R
10
10
p
p
»
´
W
f
PC1
PC2
ZC
1
1
C
= C
=
=
333 pF
s
200 kHz
2
R
2
4.8 k
2
2
p
p
»
´
´
W
f
,
ZC1
ZC1
PC1
R
= 4.02 k
C
= 2.2 nF, C
= 330 pF
W
(
)
(
)
P
OUT
S
ZC
ZC
C
RAMP
ZC
ZC
PC
ZC
PC
ZC
PC
N
V
Rs
N
j 2
R
C
+1
TcdB(
) = 20log
gm
j 2
L1
V
j 2
R
C
C
j 2
C
+C
+1
C
+C
p
p
p
p
æ
ö
ç
÷
´
´
´
´
´
´
ç
÷
´
´
ç
÷
´
´
´
´D
æ
ö
´
´
´
´
´
ç
÷
´
´
´
ç
÷
ç
÷
è
ø
è
ø
f
f
f
f
f
1
10
100
1 .103
1 .104
1 .105
1 .106
200
133.33
66.67
0
66.67
133.33
200
200
200
-
TcdB f( )
1 106
´
1
f
1
10
100
1 .103
1 .104
1 .105
1 .106
0
30
60
90
120
150
180
180
0
qc f( )
1 106
´
1
f
www.ti.com
Current Loop Compensation
Variable gmC is the current amplifier Transconductance Current Amplifier Gain.
(66)
(67)
(68)
(69)
Standard components close to the calculated values are chosen for the current loop compensation:
(70)
Graphically Check Theoretical Current Loop Gain (TcdB(f)) and loop phase (qc(f)): From the plots in
Figure 6 and Figure 7 it can be observed that the theoretical loop gain crossed over at roughly 20 kHz
with a phase margin of roughly 39 degrees.
(71)
Figure 6. Current Loop Gain (TdB(f))
Figure 7. Current Loop Phase (qc(f))
15
SLUA479B-August 2008-Revised July 2010
UCC28070 300-W Interleaved PFC Pre-Regulator -Design Review
Copyright © 2008-2010, Texas Instruments Incorporated

## [стр. 16]

ZV
SSMIN
2.25 V
C
2.25V
1.5
F
t
=
=
338 ms
10
A
10
A
m
m
m
´
´
»
SS
ZV
C
C
³
ss
ss
10
A
t
10
A
200 ms
C
=
=
0.889
F
2.25V
2.25 V
m
m
m
´
´
»
ss
C
= 1.5
F
m
DM = 30 kHz
f
10
DR
f
kHz
=
6
6
RDM
DM
937.5
10
937.5
10
R
=
=
= 31.13 k
f
30 kHz
´
W
´
W
W
-9
-9
RDM
CDR
RD
0.0667
10 F
R
0.0667
10 F
31.13 k
C
=
=
= 208 pF
10 kHz
´
´
´
´
W
f
RDM
R
= 31.6 kW
220
CDR
C
pF
=
Soft Start
www.ti.com
12
Soft Start
To have a controlled soft start the CSS capacitor needs to be set to at least the same value as the CZV
capacitor or larger. This means the design has a minimum soft start time based on the CZV capacitor
(72)
(73)
The soft-start timing can be set with timing capacitor CSS once the amount of soft start time (tSS) has been
determined. Our original design requirement was to have 200 ms of soft-start time. The calculated
capacitance needed for this soft-start time is less than the minimum required capacitance.
(74)
A CSS capacitor value equal to the CZV capacitor was chosen for the design.
(75)
13
Spread Spectrum Reduces EMI
It has been shown that dithering the converter's switching frequency can reduce EMI. Resistor RRDM and
CCDR program the frequency dithering magnitude and rate. For this design the frequency dither magnitude
(fDM) was set to 30 kHz and the frequency dither rate (fDR) was set to 10 kHz. The frequency will dither
around the typical frequency programmed by resistor RRT. In this example the frequency will dither from
roughly 185 kHz to 215 kHz at a 10 kHz rate.
(76)
(77)
(78)
(79)
A standard resistor and capacitor are chosen for the design:
(80)
(81)
16
UCC28070 300-W Interleaved PFC Pre-Regulator -Design Review
SLUA479B-August 2008-Revised July 2010
Copyright © 2008-2010, Texas Instruments Incorporated

## [стр. 17]

www.ti.com
Recommended PCB Device Layout
14
Recommended PCB Device Layout
Interleaved PFC techniques dramatically reduce input and output ripple current caused by the PFC boost
inductor, which allows the circuit to use smaller and less expensive filters. To maximize the benefits of
interleaving, the output filter capacitor should be located after the two phases allowing the current of each
phase to be combined together before entering the boost capacitor. Similar to other power management
devices, when laying out the PCB it is important to use star grounding techniques and to keep filter and
high frequency bypass capacitors as close to the device pins and ground pin as possible. To minimize the
interference caused by magnetic coupling from the boost inductor, the device should be located at least
one inch away from the boost inductor. It is also recommended that the device not be placed underneath
magnetic elements. To verify the application a 300-W interleaved prototype was constructed and
evaluated. This prototype consisted of mother board that was the power stage and a daughter board that
consisted of the control circuitry. Refer to Figure 8 through Figure 13 for schematics and a recommended
layout. The daughter board controller has two jumpers JP1 and JP2. If these jumpers are open the
evaluation module is running with frequency dithering. If these jumpers are shorted frequency dither is
disabled and the EVM can be synchronized through the sync input.
Figure 8. 300-W Prototype Daughter Board Controller Schematic
17
SLUA479B-August 2008-Revised July 2010
UCC28070 300-W Interleaved PFC Pre-Regulator -Design Review
Copyright © 2008-2010, Texas Instruments Incorporated

## [стр. 18]

+
+
+
UCC27324D
U1
Recommended PCB Device Layout
www.ti.com
Figure 9. 300-W Prototype Mother Board Power Stage
18
UCC28070 300-W Interleaved PFC Pre-Regulator -Design Review
SLUA479B-August 2008-Revised July 2010
Copyright © 2008-2010, Texas Instruments Incorporated

## [стр. 19]

www.ti.com
Recommended PCB Device Layout
Figure 10. Daughter Board Layout Front
Figure 11. Daughter Board Layout Back
19
SLUA479B-August 2008-Revised July 2010
UCC28070 300-W Interleaved PFC Pre-Regulator -Design Review
Copyright © 2008-2010, Texas Instruments Incorporated

## [стр. 20]

HS1
HS3
HS2
Q1
Q1
T1
T2
.
.
AC LINE
AC NEUTRAL
VOUT
RETURN
C6
C7
C5
L1
L2
F1
VAR1
RT1
C2
C2
D5
D6
J1
VCC
GND
SYNC
C11
J2
AC LINE
AC NEUTRAL
VOUT
D9
D2
D1
JP2
JP2
D3
U1
R10
R9
R19
R18
R5
R8
C8
C12
D12
C10
D11 R16
R13 R1
D13
D7 R6
D8
C4
R15
R14
R11
R2
D10
C9
R17
R12 R7
R3
R4
D4
C3
J1
RETURN
Recommended PCB Device Layout
www.ti.com
Figure 12. Mother Board Layout Front
Figure 13. Mother Board Bottom
20
UCC28070 300-W Interleaved PFC Pre-Regulator -Design Review
SLUA479B-August 2008-Revised July 2010
Copyright © 2008-2010, Texas Instruments Incorporated

## [стр. 21]

Efficiency
80%
82%
84%
86%
88%
90%
92%
94%
96%
98%
100%
10%
20%
30%
40%
50%
60%
70%
80%
90%
100%
% Output Power
% Efficiency
Efficiency at VIN = 115V
Efficiency at VIN = 230V
Efficiency
80%
82%
84%
86%
88%
90%
92%
94%
96%
98%
100%
10%
20%
30%
40%
50%
60%
70%
80%
90%
100%
% Output Power
% Efficiency
Efficency at Vin 85V RMS
Efficency at Vin = 265V RMS
Current Harmonics VIN = 230V, POUT = 300W
0.00001
0.23580
0.47159
0.70737
0.94316
1.17894
1.41473
1
3
5
7
9
11
13
15
17
19
21
23
25
27
29
31
33
35
37
39
Harmonic
Amplitude (A)
EN61000-3-2 Class D Specifications
www.ti.com
Efficiency Curves
15
Efficiency Curves
A 300-W prototype was built based on the design information presented in this application note. The
following graphs show the performance of this EVM.
15.1
Prototype Efficiency
Figure 14.
Figure 15.
Figure 16. Prototype Harmonic Content at VIN = 230 V, POUT = 300 W
21
SLUA479B-August 2008-Revised July 2010
UCC28070 300-W Interleaved PFC Pre-Regulator -Design Review
Copyright © 2008-2010, Texas Instruments Incorporated

## [стр. 22]

Pow er Factor
0.900
0.910
0.920
0.930
0.940
0.950
0.960
0.970
0.980
0.990
1.000
20%
30%
40%
50%
60%
70%
80%
90%
100%
% Output Pow er
PF
PF VIN = 115V
PF VIN = 230V
Pow er Factor
0.900
0.910
0.920
0.930
0.940
0.950
0.960
0.970
0.980
0.990
1.000
20%
30%
40%
50%
60%
70%
80%
90%
100%
% Output Pow er
PF
PF VIN = 85V
PF VIN = 265V
Efficiency Curves
www.ti.com
15.2
Prototype Power Factor
Figure 17.
Figure 18. Input Current and Output Ripple Voltage at
Maximum Output Power
Ch2 = IIN, CH2 = VOUT
Figure 19. VIN = 85 V RMS
Figure 20. VIN = 265 V RMS
22
UCC28070 300-W Interleaved PFC Pre-Regulator -Design Review
SLUA479B-August 2008-Revised July 2010
Copyright © 2008-2010, Texas Instruments Incorporated

## [стр. 23]

www.ti.com
Efficiency Curves
15.3
Inductor Ripple Current Cancellation, CH2=IL1, CH3=IL2, M1=IL1+IL2
Figure 21. VIN = 85 V RMS, Peak of Line
Figure 22. VIN = 265V RMS, Peak of Line
Figure 23. VIN = 265V RMS, Line Voltage at Half the
Figure 24. VIN = 85 V, POUT = 300 W
Output Voltage
23
SLUA479B-August 2008-Revised July 2010
UCC28070 300-W Interleaved PFC Pre-Regulator -Design Review
Copyright © 2008-2010, Texas Instruments Incorporated

## [стр. 24]

Efficiency Curves
www.ti.com
Figure 25. VIN = 265 V, POUT = 300 W
24
UCC28070 300-W Interleaved PFC Pre-Regulator -Design Review
SLUA479B-August 2008-Revised July 2010
Copyright © 2008-2010, Texas Instruments Incorporated

## [стр. 25]

www.ti.com
Efficiency Curves
15.4
Recovery from Line Dropout, CH1= Rectified Line Voltage, CH2=IL1, CH3=IL2, CH4 =
VOUT
Figure 26. Brownout at VIN = 115V, POUT = 300 W
15.5
Startup, CH2 = IL1, CH3 = IL2, CH4 = VOUT
Figure 27. VIN = 85 V, POUT = 300 W
Figure 28. VIN = 265 V, POUT = 300 W
25
SLUA479B-August 2008-Revised July 2010
UCC28070 300-W Interleaved PFC Pre-Regulator -Design Review
Copyright © 2008-2010, Texas Instruments Incorporated

## [стр. 26]

References
www.ti.com
15.6
EMI Measurements
When dithering was applied to the EVM a 4.35dBuV reduction in the Quasi Peak (QP) measurement was
observed. Note a filter was added to the front end of the EVM to clean up some of the noise to take EMI
data. Depending on the filter the amount of EMI will vary. Also, this filter was not setup to pass EMI
requirements but to show frequency dither reduced EMI.
Figure 29. EMI Quasi Peak (QP) Measurement with out Frequency Dithering, No EMI Filter Present
Figure 30. EMI Quasi Peak (QP) Measurement with Frequency Dithering, No EMI filter Present
16
References
1. Lazlo Balogh and Richard Redi, Power Factor Correction with Interleaved Boost, APEC 1993, pp.
168-174
2. Lloyd Dixon, High Power Factor Switching Pre-regulator Design Optimization, Unitrode Power Supply
Design Seminar SEM-700, 1990, Topic 7
3. Brett Miwa, David Otten, Martin F. Schlecht, High Efficiency Power Factor Correction Using Interleaved
Techniques IEEE 1992, pp. 557 to 568
4. Michael O'Loughlin, 350W, Two Phase Interleaved PFC Pre-regulator Design Review, Texas
Instrument Literature Number SLUA369, 2006
5. Michael O'Louglin, An Interleaving PFC Pre-Regulator for High-Power Converters Unitrode/TI Power
Supply Design Seminar SEM-1700, Topic 5
6. P. Zumel, O. Garcia, J. A. Cobos, J. Uceda, EMI Reduction by Interleaving of Power Converters
Presentation, APEC 2004
7. UCC28070 Data Sheet, Texas Instruments Literature Number SLUS794,
http://focus.ti.com/lit/ds/symlink/ucc28070.pdf
26
UCC28070 300-W Interleaved PFC Pre-Regulator -Design Review
SLUA479B-August 2008-Revised July 2010
Copyright © 2008-2010, Texas Instruments Incorporated

## [стр. 27]

IMPORTANT NOTICE
Texas Instruments Incorporated and its subsidiaries (TI) reserve the right to make corrections, modifications, enhancements, improvements,
and other changes to its products and services at any time and to discontinue any product or service without notice. Customers should
obtain the latest relevant information before placing orders and should verify that such information is current and complete. All products are
sold subject to TI's terms and conditions of sale supplied at the time of order acknowledgment.
TI warrants performance of its hardware products to the specifications applicable at the time of sale in accordance with TI's standard
warranty. Testing and other quality control techniques are used to the extent TI deems necessary to support this warranty. Except where
mandated by government requirements, testing of all parameters of each product is not necessarily performed.
TI assumes no liability for applications assistance or customer product design. Customers are responsible for their products and
applications using TI components. To minimize the risks associated with customer products and applications, customers should provide
adequate design and operating safeguards.
TI does not warrant or represent that any license, either express or implied, is granted under any TI patent right, copyright, mask work right,
or other TI intellectual property right relating to any combination, machine, or process in which TI products or services are used. Information
published by TI regarding third-party products or services does not constitute a license from TI to use such products or services or a
warranty or endorsement thereof. Use of such information may require a license from a third party under the patents or other intellectual
property of the third party, or a license from TI under the patents or other intellectual property of TI.
Reproduction of TI information in TI data books or data sheets is permissible only if reproduction is without alteration and is accompanied
by all associated warranties, conditions, limitations, and notices. Reproduction of this information with alteration is an unfair and deceptive
business practice. TI is not responsible or liable for such altered documentation. Information of third parties may be subject to additional
restrictions.
Resale of TI products or services with statements different from or beyond the parameters stated by TI for that product or service voids all
express and any implied warranties for the associated TI product or service and is an unfair and deceptive business practice. TI is not
responsible or liable for any such statements.
TI products are not authorized for use in safety-critical applications (such as life support) where a failure of the TI product would reasonably
be expected to cause severe personal injury or death, unless officers of the parties have executed an agreement specifically governing
such use. Buyers represent that they have all necessary expertise in the safety and regulatory ramifications of their applications, and
acknowledge and agree that they are solely responsible for all legal, regulatory and safety-related requirements concerning their products
and any use of TI products in such safety-critical applications, notwithstanding any applications-related information or support that may be
provided by TI. Further, Buyers must fully indemnify TI and its representatives against any damages arising out of the use of TI products in
such safety-critical applications.
TI products are neither designed nor intended for use in military/aerospace applications or environments unless the TI products are
specifically designated by TI as military-grade or "enhanced plastic." Only products designated by TI as military-grade meet military
specifications. Buyers acknowledge and agree that any such use of TI products which TI has not designated as military-grade is solely at
the Buyer's risk, and that they are solely responsible for compliance with all legal and regulatory requirements in connection with such use.
TI products are neither designed nor intended for use in automotive applications or environments unless the specific TI products are
designated by TI as compliant with ISO/TS 16949 requirements. Buyers acknowledge and agree that, if they use any non-designated
products in automotive applications, TI will not be responsible for any failure to meet such requirements.
Following are URLs where you can obtain information on other Texas Instruments products and application solutions:
Products
Applications
Amplifiers
amplifier.ti.com
Audio
www.ti.com/audio
Data Converters
dataconverter.ti.com
Automotive
www.ti.com/automotive
DLP® Products
www.dlp.com
Communications and
www.ti.com/communications
Telecom
DSP
dsp.ti.com
Computers and
www.ti.com/computers
Peripherals
Clocks and Timers
www.ti.com/clocks
Consumer Electronics
www.ti.com/consumer-apps
Interface
interface.ti.com
Energy
www.ti.com/energy
Logic
logic.ti.com
Industrial
www.ti.com/industrial
Power Mgmt
power.ti.com
Medical
www.ti.com/medical
Microcontrollers
microcontroller.ti.com
Security
www.ti.com/security
RFID
www.ti-rfid.com
Space, Avionics &
www.ti.com/space-avionics-defense
Defense
RF/IF and ZigBee® Solutions
www.ti.com/lprf
Video and Imaging
www.ti.com/video
Wireless
www.ti.com/wireless-apps
Mailing Address: Texas Instruments, Post Office Box 655303, Dallas, Texas 75265
Copyright © 2010, Texas Instruments Incorporated
