# AN-1820 LM5032 Interleaved Boost Converter (Rev. A)

<!-- FORMULA-WARNING -->
> **Формулы в этом файле недостоверны.** Текстовый слой PDF теряет дробные черты, радикалы и группировку степеней; знак интеграла приходит как `Z` или `R`, знак суммы -- как `P`. Формул вырезано: **11**, читать их в `formulas/` (картинки 300 dpi, перечень в `formulas/INDEX.md`).
<!-- /FORMULA-WARNING -->

> Автоматически извлечено из `source.pdf` скриптом `parse_pdf.py`
> Движок: pymupdf. Страниц: 13 из 13.
> Дата извлечения: 2026-08-07 06:42 UTC

Текст не редактировался. Формулы и таблицы могут быть искажены —
при сомнении сверяться с исходным PDF.

---

## [стр. 1]

Application Report
SNVA335A-May 2008-Revised May 2013
AN-1820 LM5032 Interleaved Boost Converter
Ronald Crews .................................................................................................................................
ABSTRACT
The LM5032 dual current mode PWM controller contains all the features needed to control an interleaved
boost converter. The two outputs operate 180° out of phase and have separate current limit inputs for
each channel. In addition to a high input voltage range, the controller contains all the auxiliary features
needed to control a complete converter.
Contents
1
Introduction .................................................................................................................. 2
2
Modes of Operation ......................................................................................................... 2
3
Continuous Versus Discontinuous Mode ................................................................................ 3
4
Selection of Boost Power Stage Components .......................................................................... 3
5
Inductor Selection ........................................................................................................... 4
6
Output Capacitor ............................................................................................................ 4
7
Input Capacitor Selection .................................................................................................. 5
8
Power Switches Selection ................................................................................................. 6
9
Output Diode Selection ..................................................................................................... 6
10
Compensation Components Selection ................................................................................... 7
11
Prototype ..................................................................................................................... 7
12
Performance ................................................................................................................ 10
13
Bill of Materials (BOM) .................................................................................................... 12
List of Figures
1
Interleaved Boost Basic Diagram.........................................................................................
2
2
Inductor Current (IL) Waveforms ..........................................................................................
3
3
Normalized Output Capacitor Ripple Current ...........................................................................
5
4
Normalized Input Capacitor Ripple Current .............................................................................
6
5
Schematic of Prototype ....................................................................................................
8
6
Current Sense DC Offset Circuit..........................................................................................
9
7
Photographs of the Prototype .............................................................................................
9
8
Efficiency ...................................................................................................................
10
9
Output Ripple ..............................................................................................................
11
All trademarks are the property of their respective owners.
1
SNVA335A-May 2008-Revised May 2013
AN-1820 LM5032 Interleaved Boost Converter
Submit Documentation Feedback
Copyright © 2008-2013, Texas Instruments Incorporated

## [стр. 2]

LM5032
+
-
D1
D2
Q2
Q1
Rs1
Rs2
U2
U1
L1
L2
REF
Cout
Cin
Vin
Gnd
Introduction
www.ti.com
1
Introduction
A basic boost converter converts a DC voltage to a higher DC voltage. Interleaving adds additional
benefits such as reduced ripple currents in both the input and output circuits. Higher efficiency is realized
by splitting the output current into two paths, substantially reducing I2R losses and inductor AC losses.
Figure 1 shows the basic interleaved boost topology.
When Q1 turns on, current ramps up in L1 with a slope depending on the input voltage, storing energy in
L1. D1 is off during this time since the output voltage is greater than the input voltage. Once Q1 turns off,
D1 conducts delivering part of its stored energy to the load and the output capacitor. Current in L1 ramps
down with a slope dependent on the difference between the input and output voltage. One half of a
switching period later, Q2 also turns on completing the same cycle of events. Since both power channels
are combined at the output capacitor, the effective ripple frequency is twice that of a conventional single
channel boost regulator.
Figure 1. Interleaved Boost Basic Diagram
2
Modes of Operation
The mode of operation can be analyzed based on one channel. Since both power channels share current
and because both inductors are identical, each power channel behaves identically. Based on the amount
of energy that is delivered to the load during each switching period, the boost converter can be classified
into continuous or discontinuous conduction mode. If all the energy stored in the inductor is delivered to
the load during each switching cycle, the mode of operation is classified as discontinuous conduction
mode (DCM). In this mode the inductor current ramps down to zero during the switch off-time. If only part
of the energy is delivered to the load, then the converter is said to be operating in continuous conduction
mode (CCM). Figure 2 shows the inductor current waveforms for both modes of operation.
The mode of operation is a fundamental factor in determining the electrical characteristics of the
converter. The characteristics vary significantly from one mode to the other.
2
AN-1820 LM5032 Interleaved Boost Converter
SNVA335A-May 2008-Revised May 2013
Submit Documentation Feedback
Copyright © 2008-2013, Texas Instruments Incorporated

## [стр. 3]

CCM
DCM
Boundary
Condition
Ip
0
Ip
0
Ip
0
DTS
TS=1/fs
www.ti.com
Continuous Versus Discontinuous Mode
Figure 2. Inductor Current (IL) Waveforms
3
Continuous Versus Discontinuous Mode
Both modes of operation have advantages and disadvantages. The main disadvantages in using CCM is
the inherent stability problems caused by the right-half-plane zero in the transfer function . However, the
switch and output diode peak currents are larger when the converter is operating in the DCM mode.
Larger peak currents necessitate using larger current and power dissipation rated switches and diodes.
Also, the larger peak currents cause greater EMI/RFI problems. Most modern designs use CCM because
higher power densities are possible. For these reasons, this design is based on continuous conduction
mode.
4
Selection of Boost Power Stage Components
The interleaved boost converter design involves the selection of the inductors, the input and output
capacitors, the power switches and the output diodes. Both the inductors and diodes should be identical in
both channels of an interleaved design. In order to select these components, it is necessary to know the
duty cycle range and peak currents. Since the output power is channeled through two power paths, a
good starting point is to design the power path components using half the output power. Basically, the
design starts with a single boost converter operating at half the power. However, a trade-off exists that will
depend on the goals of the design. The designer may use smaller components since currents are smaller
in each phase. Or, larger components may be selected to minimize losses. Specifically, this design uses
the criteria of room temperature operation over the entire input voltage range without the requirement of
airflow. Obviously, there are many trade-offs possible, such as requiring external airflow that would allow
the use of smaller components and more power per watt.
Knowing the maximum and minimum input voltages, the output voltage, and the voltage drops across the
output diode and switch, the maximum and minimum duty cycles are calculated. Next, the average
inductor current can be estimated from the load current and duty cycle. Assuming the peak-to-peak
inductor current ripple to be a certain percentage of the average inductor current, the peak inductor
current can be estimated. The inductor value is then calculated using the ripple current, switching
frequency, input voltage, and duty cycle information. Finally, the boundary between CCM and DCM is
determined which will determine the minimum load current.
Once the inductor value has been chosen and the peak currents have been calculated, the other
components may be selected. Selection of the input and output capacitors differ from a single phase
design because of the reduced ripple and increased effective frequency.
3
SNVA335A-May 2008-Revised May 2013
AN-1820 LM5032 Interleaved Boost Converter
Submit Documentation Feedback
Copyright © 2008-2013, Texas Instruments Incorporated

## [стр. 4]

L(crit) =
fS x IOUT
(VIN(MIN) - VON) x DMAX x (1 - DMAX)
IPEAK =
IOUT
1 - DMAX
IL(avg-critical) = 'IPEAK
2
L(MIN) =
fS x 'IL
(VIN(MIN) - V(ON)) x DMAX
IPEAK = IL(avg) + 'IL
2
IL(avg) = 0.5 x IOUT
1 - DMAX
Dmin =
VOUT + Vd - VIN(MAX)
VOUT + Vd - V(ON)
Dmax =
VOUT + Vd - VIN(MIN)
VOUT + Vd - V(ON)
Inductor Selection
www.ti.com
5
Inductor Selection
(1)
(2)
Where, VOUT is the output voltage, Vd is the forward voltage drop of the output diode, and V(ON) is the on
stage voltage of the switching MOSFET. VIN(MAX) is the maximum input voltage, and VIN(MIN) is the minimum
input voltage.
The average inductor current (maximum) per phase can be calculated knowing the output current, IOUT,
remembering that the current per phase is one-half the total current. This is the origin of the 0.5 term in
the numerator in Equation 3:
(3)
As a starting point assume the peak inductor current ripple per phase, ΔIL to be a certain percentage of
the average inductor current calculated in Equation 3. A good starting value of ΔIL is about 40% or the
output current, which is 20% of the individual phase current. Inductor ripple will also determine the
minimum output current for continuous mode operation, so some iteration may be necessary in choosing
this parameter. The peak inductor current per phase is given by:
(4)
Knowing the switching frequency, fs the required inductance value per phase can be selected using:
(5)
At the boundary between CCM and DCM modes of operation, the peak inductor current per phase, IPEAK is
the same as the peak-to-peak inductor current ripple per phase, ΔIL, as shown in Figure 2. Therefore, the
average inductor current at the boundary is given by:
(6)
From Equation 3 and Equation 6:
(7)
The critical value of the inductance per phase to maintain the converter in continuous mode related to
output current is given by Equation 5 and Equation 7.
(8)
Knowing the minimum load current in a particular design L can be chosen. Obviously, there are trade-offs
between minimum load current, percent ripple, and inductor size. Increasing the frequency helps in
reducing inductor size.
6
Output Capacitor
In a boost converter, the output capacitor must be chosen to withstand relatively high ripple current
compared to an equivalent power buck regulator. The high ripple current flows through the equivalent
series resistance (ESR) of the capacitor. ESR increases the capacitor temperature and increases ripple
voltage. First, calculate the worst case duty cycle for ripple, which is usually the maximum duty cycle (for
this value, see Figure 3). Then, read the y axis value or normalized rms ripple in the output capacitor from
Figure 3 using the two phase graphs.
4
AN-1820 LM5032 Interleaved Boost Converter
SNVA335A-May 2008-Revised May 2013
Submit Documentation Feedback
Copyright © 2008-2013, Texas Instruments Incorporated

## [стр. 5]

VIN
L x fS
IRIPPLE(Normalized) =
'VOUT =
IOUT(MAX) x (1 - DMIN)
fS x COUT
+ IPEAK x ESR
0
0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9
1
0.0
3.5
IRMS/IOUT
DUTY CYCLE
0.5
1.0
1.5
2.0
2.5
3.0
2 Phase
1 Phase
www.ti.com
Input Capacitor Selection
Figure 3. Normalized Output Capacitor Ripple Current
Then, multiply the output current by this number to get the actual RMS output capacitor ripple. Using the
actual ripple, the capacitor can be selected. The capacitor must be chosen to withstand this RMS ripple
current at extreme operating conditions. Frequently several capacitors in parallel can be selected. Next,
use Equation 9 to determine the capacitance necessary to insure a given voltage ripple. In this case, the
ESR is the dominate term, which determines the capacitor's value. Both conditions, RMS rating and ESR
value must be met. In Equation 9, fs is double the frequency of an individual phase, since both phases are
combined at the output capacitor.
(9)
It is interesting to observe from Figure 3 that the reduction in RMS (and peak-to-peak) ripple by using a
two phase converter vs. a single phase solution. At 50% duty cycle, ripple is nearly perfectly canceled,
which occurs when VIN is twice VOUT.
7
Input Capacitor Selection
Because an inductor is in series with the input supply in a boost converter, input capacitor selection is less
severe than the output capacitor. In a two-phase design, there is a further reduction in input ripple due to
ripple cancellation, allowing a smaller input capacitor than in a single phase design. The input ripple can
be read from the graph in Figure 4. This graph is normalized according to
(10)
where fs is the switching frequency per phase.
5
SNVA335A-May 2008-Revised May 2013
AN-1820 LM5032 Interleaved Boost Converter
Submit Documentation Feedback
Copyright © 2008-2013, Texas Instruments Incorporated

## [стр. 6]

PMOSFET =
x RDS(ON) x D x 1.3 + VIN(MAX) x Qg x fS +
IOUT(MAX)
2 x (1 - D)
0.5 x VIN(MAX) x IOUT x fS x (tg + tF)
(1 - D)
0
0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9
1
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
1.0
IRMS/N
DUTY CYCLE
2 Phase
1 Phase
Power Switches Selection
www.ti.com
Figure 4. Normalized Input Capacitor Ripple Current
This normalization keeps the y axis of the graph in reasonable limits and results in an easier to read
graph. As in the output capacitor case, determine the worst case duty cycle for a given design and read
the normalized ripple current from the two-phase graph. Then convert the normalized ripple current to
actual ripple current by multiplying by the normalization factor. Then size the input capacitor to handle this
rms ripple value.
8
Power Switches Selection
Each MOSFET should be selected based on several parameters. The drain-source breakdown should be
greater than the maximum input voltage plus some margin for ringing. The RDS(ON) value will determine
conduction losses and must low enough to keep junction temperatures within specifications at the
maximum drain current condition. Gate to source and gate to drain changes will contribute to AC losses.
The thermal resistance rating will determine heatsink and airflow requirements. A more detailed
calculation for the power dissipated in each MOSFET is given by:
(11)
The first term is the I2R term. The 1-D term in the denominator relates the output current to inductor
current. The 2 in the denominator is necessary to get current per phase. The second term is the AC gate
charge loss term that depends on phase frequency and the third term represents conduction switching
loss.
9
Output Diode Selection
The output diode selection is based on voltage and current ratings, and reverse recovery time. The
voltage rating should be VOUT plus some margin for ringing. VF should be as low as possible at the
maximum output current specification to minimize conduction losses. Reverse recovery time trr should be
as low as possible to minimize switching losses. Chose a Schottky rectifier if voltage ratings permit,
otherwise an ultra-fast rectifier is required.
6
AN-1820 LM5032 Interleaved Boost Converter
SNVA335A-May 2008-Revised May 2013
Submit Documentation Feedback
Copyright © 2008-2013, Texas Instruments Incorporated

## [стр. 7]

RLOAD x (1 - D)2
2 x S x L
fRHPZ =
RLOAD x VIN
2
2 x S x L x VOUT
2
=
www.ti.com
Compensation Components Selection
10
Compensation Components Selection
Compensation is similar to an equivalent power single phase boost regulator with the same inductor value.
There is a right-half-plane zero in the continuous conduction mode that will influence loop bandwidth. A
conservative approach is to insure the loop gain crosses zero at lower than 1/4 the switching (per phase)
frequency. The frequency of the right-half-plane zero is given by:
(12)
11
Prototype
A prototype was constructed using the LM5032 as the controller. The design goal was an interleaved
converter with high efficiency and operation at full power without air or a heatsink at room temperature
environment. Power was designed around a limit of about 14 amps of input current, allowing the use of off
the shelf surface mount inductors. Specifically, the specifications are:
VIN = 12 to 45 volts
VOUT = 48 volts
IOUT = 4.5 amps
VRIPPLE-OUT < 50 mV
For a complete schematic of the prototype, see Figure 5.
The circuit is built around the LM5032, a 2 phase PWM controller with separate inputs for current limit and
compensation for each channel. The separate inputs for the PWM comparator are combined in this design
since we are implementing a two-phase, single output converter, not two independent converters. The two
current limit inputs are used, since this insures current balance in each phase. Each output phase drives
its own power channel consisting of switching FETs Q1 and Q2, Inductors L2 and L3, and output dual
diode D2. The two power outputs are combined at the output capacitors C15-C20. The IC is internally
configured to drive its two outputs 180 degrees out of phase.
7
SNVA335A-May 2008-Revised May 2013
AN-1820 LM5032 Interleaved Boost Converter
Submit Documentation Feedback
Copyright © 2008-2013, Texas Instruments Incorporated

## [стр. 8]

Prototype
www.ti.com
Figure 5. Schematic of Prototype
8
AN-1820 LM5032 Interleaved Boost Converter
SNVA335A-May 2008-Revised May 2013
Submit Documentation Feedback
Copyright © 2008-2013, Texas Instruments Incorporated

## [стр. 9]

CS1
R10
1k
R12-R16
0.022
Q1
U1
R23
10k
U3 VREF
2.0V
www.ti.com
Prototype
A single feedback network consisting of error amplifier U4 and associated passive components drives both
comp inputs that are tied together at the IC.
In order to reduce the sense resistor losses, a DC offset circuit was constructed to offset the current sense
inputs by 185 mV. This allowed the use of lower value sense resistors in each phase, reducing I2R losses.
The circuit of Figure 6 illustrates the DC offset circuit.
Figure 6. Current Sense DC Offset Circuit
Since U3 is already in use as the error amplifier reference, the circuit only adds a few low current
resistors. Resistors R23, R10, and the current sense resistors form a voltage divider from the 2 volt
reference. With the values from Figure 1, the DC offset is 0.185 volts, effectively reducing the current limit
threshold of 0.5 volts by that amount. As long as R23 is much larger than R10 and with R10 much larger
than the sense resistors, the DC offset will not adversely interact with the actual sensed current waveform.
More offset could be used, consistent with compressing the actual current signal vs. noise.
In order to further reduce losses, a switching bias supply was constructed with adjustable controller U2, an
LM5009. As can be seen from the photograph of the actual prototype in Figure 7, this circuit is very small
and offers a good solution for a bias supply. If a linear regulator or zener diode were used, in would be
necessary to drop about 31 volts from the input supply at Vin(max). With an overhead current of 500 mA,
a loss of about 16 watts was avoided. Diode D3 prevents the error amplifier from holding the comp pin of
U1 high during startup, converting the error amplifier to a sink only configuration. The LM5032 contains an
internal 5K pull-up resistor.
9
SNVA335A-May 2008-Revised May 2013
AN-1820 LM5032 Interleaved Boost Converter
Submit Documentation Feedback
Copyright © 2008-2013, Texas Instruments Incorporated

## [стр. 10]

LOAD (A)
EFFICIENCY (%)
80
85
90
95
100
0.1 0.5 0.9 1.3 1.7 2.1 2.5 2.9 3.3 3.7
Vin = 12V
Vin = 24V
Vin = 36V
Vin = 42V
Performance
www.ti.com
Figure .
Figure 7. Photographs of the Prototype
Referring to the left photograph in Figure 7, the two power inductors occupy the top part of the left
photograph, with rectification accomplished with the common cathode Schottky diode located just below
the inductors. The LM5032 PWM controller is located in the lower left portion of the board. On the bottom
side of the board the bias supply is located near the upper right, with the two switching FETs at center
right. The error amplifier is located near the top left of the board. No heat-sinking other than the copper in
the PCB is used. A four layer board was used for compactness of design and heat dissipation properties.
12
Performance
Figure 8. Efficiency
10
AN-1820 LM5032 Interleaved Boost Converter
SNVA335A-May 2008-Revised May 2013
Submit Documentation Feedback
Copyright © 2008-2013, Texas Instruments Incorporated

## [стр. 11]

www.ti.com
Performance
Figure 9. Output Ripple
Referring to the plots in Figure 8 taken at the DCM/CM boundary, efficiencies range from 95% to 98% up
to the full 4 amps of output current, and over a 3.5:1 input voltage range. The very low current region
where overhead bias currents dominate does have less efficiency, but this is true of all regulators. These
plots illustrate the possibility of building a compact, high power boost converter without sacrificing
excellent efficiency.
Input and output ripple reduction are some of the benefits of an interleaved converter. Since the output
ripple is double the frequency of the individual phases and at a lower RMS current value, the designer has
the choice of smaller output capacitors with the same ripple as a single phase converter, or using larger
capacitors to achieve even lower output ripple. Effective ripple is a function of duty cycle. Figure 3 and
Figure 4 illustrates the input and output ripple currents vs. duty cycle relationships. Figure 9 shows the
output ripple of the prototype that is less than the 50mV target. Since ripple reduction is a function of duty
cycle, the degree of ripple overlap is also a function of duty cycle. There is near perfect cancellation of
ripple at 50% duty cycle. This opens the intriguing possibility of building a converter with little to no output
ripple if the designer can limit Vin to the proper value for 50% duty cycle. In the more general case, ripple
is reduced by as much as 50% compared to an equivalent power single phase converter. Likewise,
inductor selection is flexible with the two phase design. One-half the single phase inductor value can be
chosen, which makes each inductor smaller, but results in the same ripple currents as the single phase
design. Or the inductors can remain the same value as in the single phase design, reducing the ripple by
one-half. The proper trade-offs will depend on the overall design goal. Attention to ESR requirements will
keep capacitors within temperature ratings and the output voltage ripple within specifications.
11
SNVA335A-May 2008-Revised May 2013
AN-1820 LM5032 Interleaved Boost Converter
Submit Documentation Feedback
Copyright © 2008-2013, Texas Instruments Incorporated

## [стр. 12]

Bill of Materials (BOM)
www.ti.com
13
Bill of Materials (BOM)
Table 1. Bill of Materials (BOM)
Qty
Parts
Value
Description
Part Number
Manufacturer
7
C1, C2, C3, C4,
2.2 µF
CAP CER 2.2 µF 50V X7R 10% 1210
C3225X7R1H225K
TDK
C17, C18, C19
8
C5, C6, C10, C12,
0.1 µF
CAP CER .10 µF 100V X7R 10% 0805
C2012X7R2A104K
TDK
C21, C22, C23,
C25
2
C7, C8
0.01 µF
CAP CERM .01 µF 10% 50V X7R 0805
08055C103KAT2A
AVX
1
C9
22 µF
CAP CER 22 µF 10V 10% X7R 1210
GRM32ER71A226KE20L
MURATA
3
C11, C13, C14
100 pF
CAP CER 100 pF 50V C0G 5% 0805
C2012C0G1H101J
TDK
2
C15, C16
150 µF
CAP 150 µF 63V ELECT FK SMD
EEV-FK1J151Q
PANASONIC
1
C20
0.1 µF
CAP CER .1 µF 100V X7R 10% 1206
C3216X7R2A104K
TDK
1
C24
470 pF
CAP CER 470 pF 50V 5% C0G 0805
GRM2165C1H471JA01D
MURATA
1
D1
ZHCS506TA
DIODE SCHOTTKY 60V 0.5A SOT-23
ZHCS506TA
ZETEX
1
D2
MBRB1560
SCHOTTKY 15 AMP 60 VOLT DUAL
MBRB1560CT/31
VISHAY
D2PAK
1
D3
CMHD4448
HIGH SPEED SWITCHING DIODE
CMHD4448
CENTRAL SEMI
4
J1, J2, J3, J4
I/O
TERM SCREW VERT SNAP-IN PC MNT
7693
KEYSTONE
3
J5, J6, J7
TP
TEST POINT PC MULTI PURPOSE WHT
5012
KEYSTONE
1
L1
330 µH
INDUCTOR 330 µH LEADFREE
SDR0503-331KL
BOURNS
2
L2, L3
15 µH
INDUCTOR 15 µH, 2.3mOHM, 28A RMS
SER2807H-153KL
COILCRAFT
2
Q1, Q2
SUD50N06-9L
N-CHANNEL MOSFETs N-CH 60V 50A
SUD50N06-09L-E3
VISHAY
1
R1
160k
RES 160K OHM 1/8W 1% 0805 SMD
CRCW0805160KFKEA
VISHAY
10
R12, R13, R14,
0.11
RES .11 OHM 1/2W 1% 1206 SMD
RL1632R-R110-F
SUSUMU
R15, R16, R17,
R18, R19, R20,
R21
1
R2
110k
RES 110K OHM 1/8W 1% 0805 SMD
CRCW0805110KFKEA
VISHAY
2
R23, R24
10.0k
RES 10.0K OHM 1/8W 1% 0805 SMD
CRCW080510K0FKEA
VISHAY
1
R25
4.75k
RES 4.75K OHM 1/8W 1% 0805 SMD
CRCW08054K75FKEA
VISHAY
1
R26
30.1k
RES 30.1K OHM 1/8W 1% 0805 SMD
CRCW080530K1FKEA
VISHAY
1
R27
10
RES 10.0 OHM 1/8W 1% 0805 SMD
CRCW080510R0FKEA
VISHAY
1
R28
24.9k
RES 24.9K OHM 1/8W 1% 0805 SMD
CRCW080524K9FKEA
VISHAY
1
R29
1.10k
RES ANTI-SULFUR 1.1K OHM 1% 0805
ERJ-S06F1101V
PANASONIC
1
R3
22.1k
RES 22.1K OHM 1/8W 1% 0805 SMD
CRCW080522K1FKEA
VISHAY
1
R4
7.32k
RES 7.32K OHM 1/8W 1% 0805 SMD
CRCW08057K32FKEA
VISHAY
1
R5
4.02
RES 4.02K OHM 1/8W 1% 0805 SMD
CRCW08054K02FKEA
VISHAY
1
R6
17.4k
RES 17.4K OHM 1/8W 1% 0805 SMD
CRCW080517K4FKEA
VISHAY
3
R7, R10, R11
1.00k
RES 1.00K OHM 1/8W 1% 0805 SMD
CRCW08051K00FKEA
VISHAY
2
R8, R22
2.00k
RES 2.00K OHM 1/8W 1% 0805 SMD
CRCW08052K00FKEA
VISHAY
2
R9, R30
69.8k
RES 69.8K OHM 1/8W 1% 0805 SMD
CRCW080569K8FKEA
VISHAY
1
U1
LM5032
DUAL INTERLEAVED CM
LM5032
Texas
CONTROLLER
Instruments
1
U2
LM5009
100V STEP DOWN SWITCHING
LM5009
Texas
REGULATOR
Instruments
1
U3
LM4040
MICROPOWER SHUNT VOLTAGE
LM4040
Texas
REFERENCE
Instruments
1
U4
LM8261
OP-AMP RR I/O HIGH CURRENT
LM8261
Texas
Instruments
12
AN-1820 LM5032 Interleaved Boost Converter
SNVA335A-May 2008-Revised May 2013
Submit Documentation Feedback
Copyright © 2008-2013, Texas Instruments Incorporated

## [стр. 13]

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
Copyright © 2013, Texas Instruments Incorporated
