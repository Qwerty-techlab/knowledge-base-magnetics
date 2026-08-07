# 350-W, Two Phase Interleaved PFC Pre-Regulator (Rev. C)

<!-- FORMULA-WARNING -->
> **Формулы в этом файле недостоверны.** Текстовый слой PDF теряет дробные черты, радикалы и группировку степеней; знак интеграла приходит как `Z` или `R`, знак суммы -- как `P`. Формул вырезано: **22**, читать их в `formulas/` (картинки 300 dpi, перечень в `formulas/INDEX.md`).
<!-- /FORMULA-WARNING -->

> Автоматически извлечено из `source.pdf` скриптом `parse_pdf.py`
> Движок: pymupdf. Страниц: 22 из 22.
> Дата извлечения: 2026-08-07 06:42 UTC

Текст не редактировался. Формулы и таблицы могут быть искажены —
при сомнении сверяться с исходным PDF.

---

## [стр. 1]

Application Report
SLUA369C-February 2005-Revised September 2013
350-W, Two-Phase Interleaved PFC Pre-Regulator Design
Review
Mike O'Loughlin..................................................................................................... System Power MAN
1
Abstract
In higher power applications to utilize the full line power and reduce line current harmonics PFC preregulators are generally required. In these high power applications interleaving PFC stages can reduce
inductor area and reduce output capacitor ripple current. This is made possible through the inductor ripple
current cancellation that occurs with interleaving. This application note reviews the design of a 350-W two
phase interleaved power factor corrected (PFC) pre-regulator. This power converter achieves PFC with
the use of the UCC28528 PFC/PWM controller along with the UCC28220 interleaved PWM controller that
is used to interleave the two power stages. The converter also has a 2-W auxiliary bias supply that
supplies power to the converters gate drive and PWM/PFC circuitry. The complete schematic of the
working design is shown in Figure 7 and Figure 8.
2
Review the Benefits of Interleaving PFC Boost Pre-Regulators
Figure 1 shows the functional diagram of a two phase interleaved boost converter. The interleaved boost
converter is simply two boost converters operating 180 degrees out of phase. The input current is the sum
of the two inductor currents IL1 and IL2. Because the inductor's ripple currents are out of phase, they
cancel each other out and reduce the input ripple current caused by the boost inductors. The best input
inductor ripple current cancellation occurs at 50% duty cycle. The output capacitor current is the sum of
the two diode currents (I1 + I2) less the dc output current. This reduces the output capacitor ripple current
(IOUT) as a function of duty cycle. As the duty cycle approaches 0%, 50% and 100% duty cycle, the sum of
the two diode currents approaches dc. At any of these optimum operating points, the output capacitor only
has to filter the inductor ripple currents.
1
SLUA369C-February 2005-Revised September 2013
350-W, Two-Phase Interleaved PFC Pre-Regulator Design Review
Submit Documentation Feedback
Copyright © 2005-2013, Texas Instruments Incorporated

## [стр. 2]

L1
I1
IL1
S1
On
Off
S1
S2
On
Off
L2
I2
S1
IL2
2
I1
I2
Icout = (I1 +I2) - Iout
0A
RLOAD
COUT
ICOUT
IOUT
IIN
VIN
IIN
IIN = IL1 + IL2
Review the Benefits of Interleaving PFC Boost Pre-Regulators
www.ti.com
Figure 1. Interleaved Boost Stage
2
350-W, Two-Phase Interleaved PFC Pre-Regulator Design Review
SLUA369C-February 2005-Revised September 2013
Submit Documentation Feedback
Copyright © 2005-2013, Texas Instruments Incorporated

## [стр. 3]

D() 
VOUT  VIN()
VOUT
VIN()  VIN(rms)  2
 sin()
0
0.1
0.2
0.3
0.6
0.7
0.9
1.0
0
0.2
0.4
0.6
0.8
1.0
0.4
0.5
0.8
0.1
0.3
0.5
0.7
0.9
INPUT CURRENT/INDUCTOR RIPPLE CURRENT
vs
DUTY CYCLE
K(D) - Inductor Ripple Current - Cancelation Factor
Duty Cycle - D(Θ)
K(D)  2D  1
D
if D  0.5
K(D)  1  2D
1  D if D  0.5
K(D)  IIN
IL1
www.ti.com
Review the Benefits of Interleaving PFC Boost Pre-Regulators
2.1
Input Ripple Current Reduction as a Function of Duty Cycle
The following equations show how the ratio of input ripple current to inductor ripple current (K(D)) vary
with changes in duty cycle. Figure 2 shows how K(D) varies with changes in duty cycle. It's important to
remember these variations in input ripple current, when selecting inductors for the interleaved boost
converters. This is because the duty cycle in PFC pre-regulator is not fixed and changes with line voltage.
(1)
(2)
(3)
Figure 2. Input Ripple Current Reduction
In PFC pre-regulators the duty cycle (D(θ)) is not constant and varies with changes in line voltage
(Vin(θ) ). The amount of duty cycle variation for universal applications can be quite large. This variation in
duty cycle can be observed by evaluating a converter that was designed for a universal input of 85 V to
265 V with a regulated 385 V dc output. At low line the duty cycle (D1(θ)) varies from 100% to 68% and at
high line the duty cycle (D2(θ)) varies from 100% down to 2%. The inductor ripple current cancellation will
not be 100% throughout the line cycle. However, it is good enough to drastically reduce the input ripple
current for a given inductance. The highest ripple current in this example would occur at the peak of low
line with a duty cycle of 68%. The amount of inductor ripple current seen at the input for this duty cycle
would be 55%.
line voltage as a function of phase angle.
(4)
duty cycle as function of phase angle
(5)
where ω = 2 π fLINE
and θ = ωτ
3
SLUA369C-February 2005-Revised September 2013
350-W, Two-Phase Interleaved PFC Pre-Regulator Design Review
Submit Documentation Feedback
Copyright © 2005-2013, Texas Instruments Incorporated

## [стр. 4]

WaAcINTERLEAVED 
L 
IPEAK
2
B

IPEAK
2 2

CD
WaAcSINGLE  L  IPEAK
B

IRMS
CD
 L  IPEAK
B

IPEAK
2

CD
IPEAK 
POUT(max)  2

VIN(min)
EINTERLEAVED  1
2 LI
2
2
 1
2 LI
2
2
 1
4 LI2
ESINGLE  1
2 LI2
0
0
0.1
0.2
0.7
0.8
0.9
0.3
0.4
0.5
0.6
1.0
DUTY CYCLE
vs
PHASE ANGLE
180
160
120
90
60
30
D1 (Θ), D2 (Θ) - Duty Cycle
Phase Angle - Θ
Review the Benefits of Interleaving PFC Boost Pre-Regulators
www.ti.com
Figure 3. Duty Cycle Variation in Universal PFC Pre-Regulator
2.2
Evaluate Magnetic Volume Reduction
The inductor ripple current cancellation allows the designer to reduce boost inductor magnetic volume.
This is due to the energy storage requirement of the two interleaved inductors being half that of single
stage pre-regulator designed for the same power level, switching frequency and inductance.
single stage inductor energy.
(6)
two phase total inductor energy.
(7)
The amount of reduction in boost inductor volume can be seen mathematically by comparing the required
inductor area products of single stage PFC pre-regulator (WaAcSINGLE) with that of a two phase interleaved
pre-regulator inductor (WaAcINTERLEAVED) for a given inductance. The exact values for the inductor (L),
inductor RMS current (IRMS), current density (CD) and flux density (B) are not required to show the
reduction in area product.
(8)
(9)
(10)
4
350-W, Two-Phase Interleaved PFC Pre-Regulator Design Review
SLUA369C-February 2005-Revised September 2013
Submit Documentation Feedback
Copyright © 2005-2013, Texas Instruments Incorporated

## [стр. 5]

0
0.1
0.2
0.3
0.4
0.8
0.9
1.0
D
0
0.05
0.10
0.35
0.40
0.45
0.5
0.6
0.7
0.15
0.20
0.25
0.30
Normalized Acrms Current
0.50
SIngle Forward
2L Forward
ICOUT(D)  1
2
(2  2D)  (2  2D)2

if D  0.5
ICOUT(D)  1
2
(1  2D)  (1  2D)2

if D  0.5
ICOUT(single)(D) 
(1  D)  [1  (1  D)]

2  WaAcINTERLEAVED
WaAcSINGLE
 1
2
www.ti.com
Review the Benefits of Interleaving PFC Boost Pre-Regulators
The ratio of the total interleaved area product (2 X WaAcINTERLEAVED) to the area product of a single stage
pre-regulator is 0.5. This results in a 50% reduction in area product just by interleaving, which will result in
a substantial reduction in boost magnetic volume.
(11)
Interleaving PFC pre-regulators if done in this fashion will not increase the size of the EMI filter. A
common design practice is to select the switching frequency of the power converter below the EMI band of
150 kHz. The second harmonic of switching frequency would be twice the fundamental and will most likely
be in the EMI band and would need to be filtered to meet specifications. Interleaving two pre-regulators
causes the input to see a switching frequency that is twice the switching frequency of a single phase. This
means the fundamental switching frequency of the converter will most likely be pushed into the EMI band
and be at the second harmonic of an individual stage's switching frequency. However, the input ripple
current is reduced by a factor of two. This should not put any additional constraints on the EMI filter.
2.3
Output Capacitor Ripple Current Reductions as a Function of Duty Cycle
Figure 4 shows the normalized output capacitor RMS current in a single stage boost (ICOUT(single)(D)) and the
normalized capacitor RMS current in a two phase interleaved boost converter (ICOUT(D)) as a function of
duty cycle. Figure 4 illustrates that the output capacitor ripple current in a two phase interleaved is half
that in a traditional single stage boost converter for the same power levels. The reduction in RMS current
reduces heating caused by the capacitor's ESR losses, reducing electrical stress.
(12)
(13)
(14)
Figure 4. Normalized Output Capacitor Ripple Currents
5
SLUA369C-February 2005-Revised September 2013
350-W, Two-Phase Interleaved PFC Pre-Regulator Design Review
Submit Documentation Feedback
Copyright © 2005-2013, Texas Instruments Incorporated

## [стр. 6]

Design Review
www.ti.com
3
Design Review
The power supply design requirements are presented in Table 1. Please note this 350-W PFC preregulator design is based on a TI evaluation module HPA117, TI User's Guide Literature number
SLUU228, which is orderable through TI. Please visit www.ti.com for details. Also note that the design
presented in this application note is based on typical values. In a production environment a worst case
analysis would have to be conducted.
Table 1. Design Requirements
PARAMETER
MIN
TYP
MAX
VIN
85 V RMS
110 V or 230 V RMS
265 V RMS
VOUT
374 V
390 V
425 V
VRIPPLE
30 V
Current THD at 350 W
10%
PF at 350 W
0.95
Full load efficiency
90%
fS
100 kHz
Holdup requirements (tHOLD)
20 ms
fLINE
47 Hz
50 Hz
60 Hz
6
350-W, Two-Phase Interleaved PFC Pre-Regulator Design Review
SLUA369C-February 2005-Revised September 2013
Submit Documentation Feedback
Copyright © 2005-2013, Texas Instruments Incorporated

## [стр. 7]

+
Vref
Mult
VFF
VA
+
CA
Vout
Riac
Ra
Rb
PFCRsense
Rmo
Rmo
UCC285228
+
+
UCC27324
Cout
T1
T2
L2
L1
D1
D2
Vout
RL
Rfa
Cza
Cpa
Rfb
Czb
Cpb
UCC28220
20K
30K
Rc
Rd
Rsense
Rreset
Rsense
Rreset
Vin = 85 to 265V RMS
CTRL
T1
T2
Rgate
Rgate
Rslope
Slope
CHG
DSCHG
Rchg
Rdschg
6.81K
10K
Iac
Cvff
Rvff
MOUT
Vc
www.ti.com
Design Review
Figure 5. Functional Schematic
7
SLUA369C-February 2005-Revised September 2013
350-W, Two-Phase Interleaved PFC Pre-Regulator Design Review
Submit Documentation Feedback
Copyright © 2005-2013, Texas Instruments Incorporated

## [стр. 8]

ICOUT(rms) 

Iterations
n1 

IIN(n  Step)21
2
(2  2  D1(n  Step))  (2  2  D1(n  Step))2


2


Iterations

 1 A
IIN(t) 
POUT  2

VIN(min)
 sin(  t)
Step   1
fLINE
Iterations
Iterations 
fS
2  fLINE
 1  103
COUT 
COUT
(1  0.2)(1  0.2)  220 H
ESRMAX  VRIPPLE  0.2
POUT 2

VIN(min)
 1.3 
COUT  1
4 
POUT
VOUT0.637
VRIPPLE  0.8    fLINE
 104 F
COUT 
2  POUT 
1
fLINE
VOUT
2 
VOUT
2 
2  123 F
L1  L2 
VIN(min)  2
  DMIN(LL)
IL  fS
 85 V  2
  0.69
4.1 A  100 kHz  200 H
Design Review
www.ti.com
3.1
Boost Inductor Selection
Cooper Electronics designed the 200 μH, CTX16-17309, boost Inductors for our design.
(15)
3.2
Output Capacitor Selection (COUT)
There are three determining criteria for selecting the output capacitor. They are holdup energy, output
ripple voltage and lastly RMS ripple current. Equation 16 and Equation 17 are used to select the output
capacitor. Equation 16 selects the output capacitor based on holdup requirements, while Equation 17
sizes capacitance base on output voltage (VRIPPLE) requirements. The designer should select the largest
result of Equation 16 and Equation 17 for the design.
(16)
(17)
(18)
The capacitor should also be de-rated based on capacitor tolerances. The following equation de-rates the
output capacitor based on 20% error in capacitance tolerance and a 20% variation over the life of the
capacitor.
(19)
The RMS ripple current for the boost capacitor can be calculated with the following equations. To use
these equations it is a good idea to use MathCAD or MATLAB design tools.
(20)
(21)
(22)
(23)
8
350-W, Two-Phase Interleaved PFC Pre-Regulator Design Review
SLUA369C-February 2005-Revised September 2013
Submit Documentation Feedback
Copyright © 2005-2013, Texas Instruments Incorporated

## [стр. 9]

COSS(avg)  2  COSS(spec) 
VDS(spec)
VOUT

 2  310 pF 
25 V
385 V

 160 pF
IINtoff(t) 
POUT  2

2  VIN(min)    IL1
2  sin(  t)
IINton(t) 
POUT  2

2  VIN(min)    IL1
2  sin(  t)
IFET(rms) 
fLINE 

Iterations
n1

D1(nStep)
fS 
O
IIN(n  Step)
2

2

dt
IPEAK 
POUT 2

2  VIN(min)    IL1
2   5.3 A
PDIODE 
POUT  VF
2  VOUT    0.6 W
IDIODE(peak) 
POUT 2

2  VIN(min)    IL1
2   5.3 A
IDIODE 
POUT
2  VOUT    2.3 A
PSEMI 
POUT

 POUT  0.5  19 W
www.ti.com
Design Review
3.3
FET and Diode Selection
To meet the efficiency requirements (η) of the design a power budget (PSEMI) of 19 W was set. Selecting
these semiconductor devices are always trial an error. It may take several tries before the appropriate
semi conductor devices can be chosen for the design.
(24)
3.4
Diode Selection
To reduce switching losses CREE CSD10060 SiC rectifiers were used. These diodes have close to zero
reverse recovery current. The following equation is used to estimate the diode loss (PDIODE) and diode
peak (IDIODE(peak)) and average current (IDIODE), where Vf is the forward voltage drop of the boost diode.
These diodes in our design will dissipate around 0.6 W (PDIODE) per diode dissipating a total of 1.2 W for
both diodes in the design. This leaves 17.8 W of losses for the boost FETs and the auxiliary bias supply.
(25)
(26)
(27)
3.5
FET Selection Based on RMS and Peak Currents and Estimated FET Losses
, peak FET current.
(28)
The following equation estimates FET RMS current (IFET(rms)) which is needed to estimate boost FET (PFET)
losses.
(29)
, peak FET line currents (IIN ton (t)) at switch turn off.
(30)
, peak FET line currents (IIN toff (t)) at switch turn off.
(31)
Part of the total FET losses are contributed Coss (COSS(avg)) charging and discharging during a PWM
switching cycle. COSS varies with line voltage and is not a linear function. The following equation and
information from the FETs data sheet can be used to calculate COSS(avg). COSS(spec) is the typical COSS
measured at a specified VDS voltage (VDS(spec)). A IRF840, 8 A 500 V FET was selected for the design. The
estimated COSS(avg) was roughly 160 pF.
(32)
9
SLUA369C-February 2005-Revised September 2013
350-W, Two-Phase Interleaved PFC Pre-Regulator Design Review
Submit Documentation Feedback
Copyright © 2005-2013, Texas Instruments Incorporated

## [стр. 10]

PFET  PSWITCH(toff)  PSWITCH(ton)  PCOSS  PGATE  PRDS(on)  5 W
PRDS(on)  IFET(rms)  RDS(on)
PGATE  QOFF  VGS(max)  fS
PCOSS  1
2  COSS  VOUT
2  fS
PSWITCH(ton)  fLINE

Iterations
n1 IINton(n  Step)  VOUT  tON(delay)
PSWITCH(toff)  fLINE

Iterations
n1 IINtoff(n  Step)  VOUT  tOFF(delay)
tON(delay)  tOFF(delay) 
QGS(miller)
IGATE
IGATE 
VGS(max)
2  RGATE
QGS(max)  52 nC
QGS(miller)  30 nC
Design Review
www.ti.com
To estimate FET turn-on (tON(delay)) and turn off (tOFF(delay)) delays requires studying the FETs VGS versus QG
characteristics of Figure 6 along with the following equations.
Figure 6.
, the typical maximum miller plateau gate charge for VDS equal to 400 V.
(33)
, is the amount of gate charge when the FET VGS is at its maximum VGS(max).
(34)
, is average FET gate drive current.
(35)
(36)
, switching losses at FET turnoff.
(37)
, switching losses at FET turn-on.
(38)
, COSS loss.
(39)
, FET gate loss.
(40)
, FET RDS(on) loss
(41)
(42)
The estimated FET loss (PFET) for this design was 5 W. The total FET loss would be 10 W and with the 1.2
W total diode loss comes to a total semiconductor loss of 11.2 W, which is below the 19 W power budget
(PSEMI) that was initially set.
10
350-W, Two-Phase Interleaved PFC Pre-Regulator Design Review
SLUA369C-February 2005-Revised September 2013
Submit Documentation Feedback
Copyright © 2005-2013, Texas Instruments Incorporated

## [стр. 11]

DMAX(osc)  1  21  DMAX
FOSC  2  fS
FOSC  2  fS
KOSC  2.04  1010 
s
RRESET 
VC0.5 V
2
IPEAK 1  DMIN(LL)  a
IPEAK(startup)  2  IPEAK
RSENSE 
VC0.5 V
2
IPEAK  a
IPEAK 
POUT  2

2  Vin(min)    IL1
2   1.3
a  NP
NS
 VP
VS

IS
IP
 1
50
RSA 
TJ(max)  3
4  TAMB  PFETRJC  RCS
PFET
 16.6OC
W
www.ti.com
Design Review
3.6
Selecting Heat Sinks for the FETs
Because the diodes only dissipated 0.6 W heat sinks were not required for the boost diodes. However, the
FETs required heat sinks and the following equation was used to calculate the thermal impedance (RθSA)
of the required heat sink. This equation is based on a maximum allowable ambient temperature (TAMB) of
40°C, and the thermal impedance from junction to case Rθjc of the IR840 and the case to sink thermal
impedance of a TO220 (RθCS) which all can be found in the IRF840's data sheet. For this design we chose
an AAVID 531202 heat sink to meet the RθSA requirements.
(43)
3.7
Over Voltage Protection and Under Voltage Lockout
The OVP function and under voltage lockout (UVLO) were handled by the UCC28220. It is a simple
comparator that monitors the boost voltage. Information on setting up these thresholds can be found in the
UCC28220's data sheet. The OVP for this design was set to 425 V and UVLO was set to 108 V. The preregulator will not start switching until VOUT reaches 108 V.
3.8
Peak Current Limit
Peek current limit is set by the maximum control voltage (VC) at the input of the UCC28220's PWM
comparator. Where "a" is the current sense transformer turns ratio of T1 and T2. The peak current limit trip
point was set for 130% of the nominal peak current to protect the boost FETs.
(44)
(45)
VC = 1.8, VCTRL was set to a maximum of 3.0 V to protect the UCC28220 CTRL pin.
(46)
, this equation takes into account slope compensation that is added later.
(47)
The peak current of the FET during power up is 2 times IPEAK under normal operation. This is due the
excessive slope compensation that is needed for stability.
(48)
3.9
Current Sense Transformer Reset Resistor (T1 and T2)
(49)
3.10
Oscillator and Maximum Duty Cycle Clamp
The UCC28220's oscillator and maximum duty cycle clamp are setup through resistor RCHG and discharge.
The desired duty cycle clamp (DMAX) was set at 0.9 to stop the current sense transformers from saturating.
, UCC28220 oscillator constant.
(50)
, UCC28220 internal oscillator frequency.
(51)
, internal duty cycle clamp.
(52)
(53)
11
SLUA369C-February 2005-Revised September 2013
350-W, Two-Phase Interleaved PFC Pre-Regulator Design Review
Submit Documentation Feedback
Copyright © 2005-2013, Texas Instruments Incorporated

## [стр. 12]

HCNTRL 
VC
VCTRL
 0.6
GCA(s) 
IC
IL1 
s  RZB  CZA  1
s  RMO  CZB  CPB s 
CZBCPB
CZBCPB
 RZB  1
 HCNTRL  HCA
GID(s)  IL1
IC

VOUT  RSENSE  a
s  L1  VC1
TC(s)  GID(s)  GCA(s)
CVFF 
1
2    RVFF  fP1
fP1  fLINE  1.5%
66%
RVFF 
1.5 V
Vin(min)
2RIAC
 0.9
RIAC 
VIN(max)  2

500 A
RDISCHG  KOSC
1  DMAX(osc)
FOSC
Design Review
www.ti.com
(54)
3.11
Control Loop Compensation
All the control equations for the voltage loop and current loop are estimates. The control equations in this
paper gives starting points for feedback compensation. In most control loops it is required to adjust the
loop compensation as necessary with a network analyzer.
3.12
Current Loop
The first step in setting up the current loop is setting up the multiplier components. The RIAC resistor is tied
to the rectified line voltage and is what forces the current amplifier output to track changes in the line
voltage. This resistance typically is a group of series resistors needed to meet the high voltage
requirements.
(55)
The multiplier internal to the UCC28528 has a voltage feed forward (VFF) function that keeps the power
stage gain constant and provides soft power limiting when the line drops keeping the line current from
increasing excessively. A detailed explanation can be found in TI/Unitrode application note SLUA196A.
The VFF signal is produced through an internal current mirror within the PFC controller. The maximum
current leaving the VFF pin is equal to one half the IAC current. The following equations are used to select
a VFF resistor (RVFF) and a filter capacitor (CVFF) to remove ac components from the VFF signal.
(56)
The VFF signals ac portion has an affect on total current harmonic distortion (THD). The filter's pole (fp1)
is set at a frequency to limit the VFF contribution to 1.5% in order to meet the power supplies current THD
design requirements.
(57)
(58)
This control methodology is based on average and peak current mode control and the following formulas
to compensate the current loop. These calculations get the design close to the correct compensation and
will have to be fine tuned with a network analyzer. In this design example to compensate the current loop
(TC(s)) we set a design goal of 45 degrees of phase margin and a crossover frequency of one tenth the
switching frequency.
, current loop transfer function.
(59)
, control to output current transfer function.
(60)
VC1 = VC - 0.5 V, VC1 is the maximum control voltage at the input of the PWM comparator of the UCC28220. Note
Equation VC1 takes into account the 500 mV offset that is present in the UCC28220 PWM controller.
(61)
The current amplifier compensation transfer function GCA(s) is as follows
(62)
, internal divider of the UCC28220 CTRL pin.
(63)
12
350-W, Two-Phase Interleaved PFC Pre-Regulator Design Review
SLUA369C-February 2005-Revised September 2013
Submit Documentation Feedback
Copyright © 2005-2013, Texas Instruments Incorporated

## [стр. 13]

TV(s)  GVD(s)  GVA(s)
CPB 
1
2    RZB fs
2
CZB 
1
2    RZB  fs
10
RZB 
1
GID2jfS
10
 RMO
HCA  HCNTRL
RMO 
POUT 2
 1.1PFCRSENSE
VIN(min)
2VIN(min) 2

RIAC

VR(sense)
2  IAC
PFCRSENSE 
VSENSE
POUT 2

VIN(min)
RSLOPE  0.1 V 
1  DMIN(LL)
10 pF  ILaRSENSE
2
HCA 
VCTRL
VCA(out)

RD
RC  RD
 0.594
www.ti.com
Design Review
The voltage divider HCA was required to divide down the CA output of the UCC28528, to protect the CTRL
pin of the UCC28220. This divider should work fine for any power requirement and should be considered a
fixed variable.
(64)
For stability the current sense signal needs slope compensation. It is required to add at least half of the
inductor current down slope to the current sense signal. The UCC28220 has internal slope compensation
that is setup by resistor RSLOPE.
(65)
The UCC28528 needed a current sense resistor (PFCRSENSE) to monitor the input current. Calculating this
resistor value is based on allocating a maximum allowable current sense voltage (VSENSE).
(66)
The UCC28528 also uses the current sense signal to trigger power limiting. The power limit can be setup
by properly selecting the multiplier resistor RMO. The power limit was set to 110% of full load power.
Please refer to the UCC28528s data sheet for details on how this power limiting function works. The
power limit was set at 110% as not to interfere with the UCC28220's peak current limit function which was
set at 130%.
(67)
, resistor RZA is set to force TC(s) to cross over at (fS/10).
(68)
Putting a zero at loop crossover adds an additional 45 degrees of phase at crossover to ensure control
loop stability.
, capacitor CZB is adjusted to put a zero at frequency crossover.
(69)
, capacitor CPB is used to attenuate high frequency noise.
(70)
3.13
Voltage Loop (TV(s))
Compensating the voltage loop has two major constraints. First is attenuating the 2 x fLINE output capacitor
voltage ripple, this is required to reduce input current harmonic distortion. Second is control loop stability.
If either of these criteria is compromised PF and THD will be affected greatly.
(71)
VC2 = 5.5 V, maximum voltage amplifier (VA) output.
(72)
13
SLUA369C-February 2005-Revised September 2013
350-W, Two-Phase Interleaved PFC Pre-Regulator Design Review
Submit Documentation Feedback
Copyright © 2005-2013, Texas Instruments Incorporated

## [стр. 14]

CPA 
1
2    2  fLINE VC0.015
VRIPPLE

1
H1gm
CZA 
1
2    fC  RZA
RZA 
1
GV2jfC
H1  gm
GVA(s)  H1  gm 
s  RZA  CZA  1
s  RMO  CZA  CPA s  CZACPA
CZACPA
 RZA  1
H1 
RB
RB  RA
 VREF
VOUT
 7.5 V
VOUT
GVD(s) 
VOUT
VC

POUT

VC2  s  COUT  VOUT
Design Review
www.ti.com
, voltage control to output transfer function.
(73)
gm = 100 umho, trans-conductance voltage amplifier (VA) gain.
(74)
, this divider can also be used to set up the RA and RB voltage divider.
(75)
(76)
To ensure that this loop would have low harmonic distortion the loop was designed to crossover (fC) at 10
Hz.
(77)
, CZA is set at fC to give the voltage loop 45 degrees of added phase at crossover.
(78)
, is sized to attenuate the output ripple voltage.
(79)
After the critical parameters were calculated the power supply was constructed and evaluated. The final
design of the 350-W two phase interleaved PFC is shown in the schematics of Figure 7 and Figure 8. This
power supply also has a 2-W auxiliary power supply that is based on a discontinues current mode (DCM)
flyback topology.
14
350-W, Two-Phase Interleaved PFC Pre-Regulator Design Review
SLUA369C-February 2005-Revised September 2013
Submit Documentation Feedback
Copyright © 2005-2013, Texas Instruments Incorporated

## [стр. 15]

+
+
+
1 N/C
2 INA
3 GND
4 INB
5
OUTB
6
VDD
7
OUTA
8
N/C
UCC27324D
U4
www.ti.com
Schematic
4
Schematic
Figure 7. 350-W Interleaved PFC Boost Pre-Regulator Schematic
15
SLUA369C-February 2005-Revised September 2013
350-W, Two-Phase Interleaved PFC Pre-Regulator Design Review
Submit Documentation Feedback
Copyright © 2005-2013, Texas Instruments Incorporated

## [стр. 16]

+
Design Performance
www.ti.com
Figure 8. 2-W, Flyback and PFC/PWM Controller Schematic
5
Design Performance
16
350-W, Two-Phase Interleaved PFC Pre-Regulator Design Review
SLUA369C-February 2005-Revised September 2013
Submit Documentation Feedback
Copyright © 2005-2013, Texas Instruments Incorporated

## [стр. 17]

t - Time - 5 ms/div.
10 mV/div.
Output Ripple Voltage,
POUT = 350 W
100
Frequency
1000
10000
10000
-32
-24
-16
-8
0
8
16
24
32
40
Gain-dB
-180
-144
-108
-72
-36
0
36
72
108
144
180
Phase-Degrees
Phase
Gain
TC(f) Current Loop Frequency Response
VIN = 120 V DC, POUT = 350 W
-40
-32
-24
-16
-8
0
8
16
24
32
40
Gain-dB
-180
-144
-108
-72
-36
0
36
72
108
144
180
Phase-Degrees
Phase
Gain
TC(f) Current Loop Frequency Response
VIN = 238 V DC, POUT = 350 W
100
1000
10000
100000
Frequency
www.ti.com
Design Performance
The current loop TC(s) was measured with a network analyzer and did not exactly track the model
presented above. The TC(s) gain moved with input voltage and appeared to have a double pole around 30
kHz. This is probably due to the excessive slope compensation that this topology requires. However, the
current loop was stable and did not have to be adjusted. Note to measure the current loop or voltage loop
requires a dc input voltage, otherwise the line current and voltage affects the loop measurements. A
network analyzer with a low enough frequency range was not available to measure the voltage loop.
Figure 9.
Figure 10.
Figure 11.
17
SLUA369C-February 2005-Revised September 2013
350-W, Two-Phase Interleaved PFC Pre-Regulator Design Review
Submit Documentation Feedback
Copyright © 2005-2013, Texas Instruments Incorporated

## [стр. 18]

t - Time - 5 ms/div.
H1: 250 V/div.
Rectified Line
 Voltage
CH2: 10 mV/div.
L1 Current
CH3: 10 mV/div.
L2 Current
CH4: 20 mV/div.
Input Current
Input Inductor Ripple Current Cancellation
at VIN = 265 V RMS, POUT = 350 W
t - Time - 10 µs/div.
CH1: 100 V/div.
Rectified Line
 Voltage
CH2: 20 mV/div.
L1 Current
CH3: 20 mV/div.
L2 Current
CH4: Input Current
Inductor Ripple Current Cancellation
at VIN = 85 V RMS and POUT = 350 W
1
4
2
3
t - Time - 5 ms/div.
CH1: 250 V/div.
Rectified Line
 Voltage
CH2: 20 mV/div.
L1 Current
CH3: 20 mV/div.
L2 Current
CH4:  20 mV/div
Input Current
Input Inductor Ripple Current Cancellation
at VIN = 85 V RMS, POUT = 350 W
Design Performance
www.ti.com
5.1
Input Inductor Ripple Current Cancellation
Figure 12 shows the inductor ripple current cancellation at the peak of line with a minimum input of 85 V
RMS. From this graph it can be observed that the input current (CH4) is 1/2 the individual inductor ripple
currents of L1 (CH2) and L2 (CH3). The ratio of input ripple current to inductor ripple current agrees with
graph in Figure 2. Note that the current ratio is 0.225 A/mV in the following graphs.
Figure 13.
Figure 12.
Figure 14.
18
350-W, Two-Phase Interleaved PFC Pre-Regulator Design Review
SLUA369C-February 2005-Revised September 2013
Submit Documentation Feedback
Copyright © 2005-2013, Texas Instruments Incorporated

## [стр. 19]

t - Time - 25 ms/div.
CH4: VOUT
500 V/div.
CH3: IIN
20 mV/div.
Startup at VIN = 85 V, POUT = 350 W
t - Time - 25 ms/div.
CH2: VOUT
100 V/div.
CH1: 100 V/div.
Rectified  Line
Line Dropout at Full Load
t - Time - 25 ms/div.
CH4: VOUT
500 V/div.
CH3: IIN
20 mV/div.
Startup No Load and VIN = 85 V
t - Time - 100 ms/div.
CH2: VOUT
100 V/div.
CH1: 100 V/div.
Rectified  Line
Line Transients at 350-W Load, VIN
Stepped from 240 V to 120 V to 240 V
www.ti.com
Design Performance
5.2
Transient Response
The voltage loop of a PFC pre-regulator is generally below 10 Hz, which means the fastest the voltage
loop can respond to a small transient is roughly 100 ms. In typical applications a PFC pre-regulator takes
5 to 10 times as long to recover from a transient response. However, a large signal comparator built into
the UCC28528 control device allowed the design to recover from large signal transient responses in less
than 200 ms.
Figure 17.
Figure 15.
Figure 18.
Figure 16.
19
SLUA369C-February 2005-Revised September 2013
350-W, Two-Phase Interleaved PFC Pre-Regulator Design Review
Submit Documentation Feedback
Copyright © 2005-2013, Texas Instruments Incorporated

## [стр. 20]

0.00002
0.23643
0.47283
0.70923
0.94564
1.18204
1.41845
0
2 4
6
8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40 42 44 46 48 50
Harmonic
Amplitude - A
CURRENT HARMONICS
VIN = 265 V, POUT = 350 W
0.00007
0.77313
1.54620
2.31927
3.09234
3.86540
4.63847
0 2 4
6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40 42 44 45 48 50
Harmonic
Amplitude - A
CURRENT HARMONICS
VIN = 85 V, POUT = 350 W
100
90
80
70
60
50
40
30
20
0.88
0.90
0.92
0.94
0.96
1.00
POUT - Output Power - %
PF
PF
vs
OUTPUT POWER
0.98
VIN = 85 V
VIN = 265 V
VIN = 85 V
VIN = 265 V
100
90
80
70
60
50
40
30
20
89
90
91
92
93
94
95
96
97
POUT - Output Power - %
Efficiency - %
EFFICIENCY
vs
OUTPUT POWER
Design Performance
www.ti.com
Figure 19.
Figure 20.
Figure 21.
Figure 22.
20
350-W, Two-Phase Interleaved PFC Pre-Regulator Design Review
SLUA369C-February 2005-Revised September 2013
Submit Documentation Feedback
Copyright © 2005-2013, Texas Instruments Incorporated

## [стр. 21]

www.ti.com
Conclusion:
6
Conclusion:
By interleaving boost pre-regulator stages enables the power supply designer to reduce boost inductor
area product by 50% and reduce boost capacitance RMS current. This allows the designer to reduce the
size of the PFC pre-regulator; as well as, use output filter capacitors with lower RMS ratings.
In high power applications interleaving PFC pre-regulators would be a good choice, where many boost
FETs and boost diodes would be required for the design. In these applications the only added cost would
be adding the additional control circuitry that is needed to accomplish interleaving.
Revision History
Changes from B Revision (February 2007) to C Revision ............................................................................................. Page
•
Deleted incorrect image title. ............................................................................................................
5
NOTE: Page numbers for previous revisions may differ from page numbers in the current version.
21
SLUA369C-February 2005-Revised September 2013
Revision History
Submit Documentation Feedback
Copyright © 2005-2013, Texas Instruments Incorporated

## [стр. 22]

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
