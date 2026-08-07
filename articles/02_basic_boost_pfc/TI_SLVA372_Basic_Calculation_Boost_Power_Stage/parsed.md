# Basic Calculation of a Boost Converter's Power Stage (Rev. D)

> Автоматически извлечено из `source.pdf` скриптом `parse_pdf.py`
> Движок: pymupdf. Страниц: 10 из 10.
> Дата извлечения: 2026-08-07 06:43 UTC

Текст не редактировался. Формулы и таблицы могут быть искажены —
при сомнении сверяться с исходным PDF.

---

## [стр. 1]

Application Note
Basic Calculation of a Boost Converter's Power Stage
Brigitte Hauke
Low Power DC/DC Application
ABSTRACT
This application note gives the equations to calculate the power stage of a boost converter built with an IC
with integrated switch and operating in continuous conduction mode. It is not intended to give details on the
functionality of a boost converter (see Reference 1) or how to compensate a converter. See the references at the
end of this document if more detail is needed.
For the equations without description, See section 8.
Table of Contents
1 Basic Configuration of a Boost Converter...........................................................................................................................2
1.1 Necessary Parameters of the Power Stage.......................................................................................................................2
2 Calculate the Maximum Switch Current............................................................................................................................... 2
3 Inductor Selection...................................................................................................................................................................4
4 Rectifier Diode Selection........................................................................................................................................................4
5 Output Voltage Setting........................................................................................................................................................... 5
6 Input Capacitor Selection.......................................................................................................................................................6
7 Output Capacitor Selection....................................................................................................................................................6
8 Equations to Calculate the Power Stage of a Boost Converter..........................................................................................7
9 References.............................................................................................................................................................................. 9
10 Revision History................................................................................................................................................................... 9
www.ti.com
Table of Contents
SLVA372D - NOVEMBER 2009 - REVISED NOVEMBER 2022
Submit Document Feedback
Basic Calculation of a Boost Converter's Power Stage
1
Copyright © 2022 Texas Instruments Incorporated

## [стр. 2]

1 Basic Configuration of a Boost Converter
Figure 1-1 shows the basic configuration of a boost converter where the switch is integrated in the used IC.
Often lower power converters have the diode replaced by a second switch integrated into the converter. If this is
the case, all equations in this document apply besides the power dissipation equation of the diode.
VIN
VOUT
IIN
IOUT
CIN
COUT
L
D
SW
Figure 1-1. Boost Converter Power Stage
1.1 Necessary Parameters of the Power Stage
The following four parameters are needed to calculate the power stage:
1.
Input Voltage Range: VIN(min) and VIN(max)
2.
Nominal Output Voltage: VOUT
3.
Maximum Output Current: IOUT(max)
4.
Integrated Circuit used to build the boost converter. This is necessary, because some parameters for the
calculations have to be taken out of the data sheet.
If these parameters are known the calculation of the power stage can take place.
2 Calculate the Maximum Switch Current
The first step to calculate the switch current is to determine the duty cycle, D, for the minimum input voltage. The
minimum input voltage is used because this leads to the maximum switch current.
IN(min)
OUT
V
η
D = 1
V
´
-
(1)
VIN(min) = minimum input voltage
VOUT = desired output voltage
η = efficiency of the converter, e.g. estimated 80%
The efficiency is added to the duty cycle calculation, because the converter has to deliver also the energy
dissipated. This calculation gives a more realistic duty cycle than just the equation without the efficiency factor.
Either an estimated factor, e.g. 80% (which is not unrealistic for a boost converter worst case efficiency), can be
used or see the Typical Characteristics section of the selected converter's data sheet
(Reference 3 and 4).
The next step to calculate the maximum switch current is to determine the inductor ripple current. In the
converters data sheet normally a specific inductor or a range of inductors is named to use with the IC. So
either use the recommended inductor value to calculate the ripple current, an inductor value in the middle of the
recommended range or, if none is given in the data sheet, the one calculated in the Inductor Selection section of
this application note.
IN(min)
L
S
V
D
ΔI
=
f
L
´
´
(2)
VIN(min) = minimum input voltage
D = duty cycle calculated in Equation 1
fS = minimum switching frequency of the converter
L = selected inductor value
Basic Configuration of a Boost Converter
www.ti.com
2
Basic Calculation of a Boost Converter's Power Stage
SLVA372D - NOVEMBER 2009 - REVISED NOVEMBER 2022
Submit Document Feedback
Copyright © 2022 Texas Instruments Incorporated

## [стр. 3]

Now it has to be determined if the selected IC can deliver the maximum output current.
L
MAXOUT
LIM(min)
ΔI
I
=
I
(1 D)
2
æ
ö
-
´
-
ç
÷
è
ø
(3)
ILIM(min) = minimum value of the current limit of the integrated switch (given in the data sheet)
ΔIL = inductor ripple current calculated in Equation 2
D = duty cycle calculated in Equation 1
If the calculated value for the maximum output current of the selected IC, IMAXOUT, is below the systems required
maximum output current, another IC with a higher switch current limit has to be used.
Only if the calculate value for IMAXOUT is just a little smaller than the needed one, it is possible to use the
selected IC with an inductor with higher inductance if it is still in the recommended range. A higher inductance
reduces the ripple current and therefore increases the maximum output current with the selected IC.
If the calculated value is above the maximum output current of the application, the maximum switch current in
the system is calculated:
OUT(max)
L
SW(max)
I
ΔI
I
=
+
2
1 D
-
(4)
ΔIL = inductor ripple current calculated in Equation 2
IOUT(max) = maximum output current necessary in the application
D = duty cycle calculated in Equation 1
This is the peak current, the inductor, the integrated switch(es) and the external diode has to withstand.
www.ti.com
Calculate the Maximum Switch Current
SLVA372D - NOVEMBER 2009 - REVISED NOVEMBER 2022
Submit Document Feedback
Basic Calculation of a Boost Converter's Power Stage
3
Copyright © 2022 Texas Instruments Incorporated

## [стр. 4]

3 Inductor Selection
Often data sheets give a range of recommended inductor values. If this is the case, it is recommended to choose
an inductor from this range. The higher the inductor value, the higher is the maximum output current because of
the reduced ripple current.
The lower the inductor value, the smaller is the solution size. Note that the inductor must always have a higher
current rating than the maximum current given in Equation 4 because the current increases with decreasing
inductance.
For parts where no inductor range is given, the following equation is a good estimation for the right inductor:
(
)
IN
OUT
IN
L
S
OUT
V
×
V
V
L =
ΔI
f
V
-
´
´
(5)
VIN = typical input voltage
VOUT = desired output voltage
fS = minimum switching frequency of the converter
ΔIL = estimated inductor ripple current, see below
The inductor ripple current cannot be calculated with Equation 1 because the inductor is not known. A good
estimation for the inductor ripple current is 20% to 40% of the output current.
OUT
L
OUT(max)
IN
V
ΔI
= (0.2 to 0.4)
I
V
´
´
(6)
ΔIL = estimated inductor ripple current
IOUT(max) = maximum output current necessary in the application
4 Rectifier Diode Selection
To reduce losses, Schottky diodes should be used. The forward current rating needed is equal to the maximum
output current:
F
OUT(max)
I
= I
(7)
IF = average forward current of the rectifier diode
IOUT(max) = maximum output current necessary in the application
Schottky diodes have a much higher peak current rating than average rating. Therefore the higher peak current
in the system is not a problem.
The other parameter that has to be checked is the power dissipation of the diode. It has to handle:
D
F
F
P
= I
V
´
(8)
IF = average forward current of the rectifier diode
VF = forward voltage of the rectifier diode
Inductor Selection
www.ti.com
4
Basic Calculation of a Boost Converter's Power Stage
SLVA372D - NOVEMBER 2009 - REVISED NOVEMBER 2022
Submit Document Feedback
Copyright © 2022 Texas Instruments Incorporated

## [стр. 5]

5 Output Voltage Setting
Almost all converters set the output voltage with a resistive divider network (which is integrated if they are fixed
output voltage converters).
With the given feedback voltage, VFB, and feedback bias current, IFB, the voltage divider can be calculated.
R1
R2
IR1/2
IFB
VOUT
VFB
Figure 5-1. Resistive Divider for Setting the Output Voltage
The current through the resistive divider shall be at least 100 times as big as the feedback bias current:
R1/2
FB
I
100
I
³
´
(9)
IR1/2 = current through the resistive divider to GND
IFB = feedback bias current from data sheet
This adds less than 1% inaccuracy to the voltage measurement. The current can also be a lot higher. The only
disadvantage of smaller resistor values is a higher power loss in the resistive divider, but the accuracy will be a
little increased.
With the above assumption, the resistors are calculated as follows:
FB
2
R1/2
V
R
= I
(10)
OUT
1
2
FB
V
R = R
1
V
æ
ö
´
-
ç
÷
è
ø
(11)
R1,R2 = resistive divider, see Figure 5-1.
VFB = feedback voltage from the data sheet
IR1/2 = current through the resistive divider to GND, calculated in Equation 9
VOUT = desired output voltage
www.ti.com
Output Voltage Setting
SLVA372D - NOVEMBER 2009 - REVISED NOVEMBER 2022
Submit Document Feedback
Basic Calculation of a Boost Converter's Power Stage
5
Copyright © 2022 Texas Instruments Incorporated

## [стр. 6]

6 Input Capacitor Selection
The minimum value for the input capacitor is normally given in the data sheet. This minimum value is necessary
to stabilize the input voltage due to the peak current requirement of a switching power supply. the best practice
is to use low equivalent series resistance (ESR) ceramic capacitors. The dielectric material should be X5R
or better. Otherwise, the capacitor cane lose much of its capacitance due to DC bias or temperature (see
references 7 and 8).
The value can be increased if the input voltage is noisy.
7 Output Capacitor Selection
Best practice is to use low ESR capacitors to minimize the ripple on the output voltage. Ceramic capacitors are a
good choice if the dielectric material is X5R or better (see reference 7 and 8).
If the converter has external compensation, any capacitor value above the recommended minimum in the data
sheet can be used, but the compensation has to be adjusted for the used output capacitance.
With internally compensated converters, the recommended inductor and capacitor values should be used or the
recommendations in the data sheet for adjusting the output capacitors to the application should be followed for
the ratio of L × C.
With external compensation, the following equations can be used to adjust the output capacitor values for a
desired output voltage ripple:
OUT(max)
OUT(min)
S
OUT
I
D
C
=
f
ΔV
´
´
(12)
COUT(min) = minimum output capacitance
IOUT(max) = maximum output current of the application
D = duty cycle calculated with Equation 1
fS = minimum switching frequency of the converter
ΔVOUT = desired output voltage ripple
The ESR of the output capacitor adds some more ripple, given with the equation:
OUT(max)
L
OUT(ESR)
I
ΔI
ΔV
= ESR
+
1 D
2
æ
ö
´ ç
÷
-
è
ø
(13)
ΔVOUT(ESR) = additional output voltage ripple due to capacitors ESR
ESR = equivalent series resistance of the used output capacitor
IOUT(max) = maximum output current of the application
D = duty cycle calculated with Equation 1
ΔIL = inductor ripple current from Equation 2 or Equation 6
Input Capacitor Selection
www.ti.com
6
Basic Calculation of a Boost Converter's Power Stage
SLVA372D - NOVEMBER 2009 - REVISED NOVEMBER 2022
Submit Document Feedback
Copyright © 2022 Texas Instruments Incorporated

## [стр. 7]

8 Equations to Calculate the Power Stage of a Boost Converter
IN(min)
OUT
V
η
Maximum Duty Cycle: D = 1
V
´
-
(14)
VIN(min) = minimum input voltage
VOUT = desired output voltage
η = efficiency of the converter, e.g. estimated 85%
IN(min)
L
S
V
D
Inductor Ripple Current: ΔI
=
f
L
´
´
(15)
VIN(min) = minimum input voltage
D = duty cycle calculated in Equation 14
fS = minimum switching frequency of the converter
L = selected inductor value
L
MAXOUT
LIM(min)
ΔI
Maximum output current of the selected IC: I
=
I
(1 D)
2
æ
ö
-
´
-
ç
÷
è
ø
(16)
ILIM(min) = minimum value of the current limit of the integrated witch (given in the data sheet)
ΔIL = inductor ripple current calculated in Equation 15
D = duty cycle calculated in Equation 14
OUT(max)
L
SW(max)
I
ΔI
Application specific maximum switch current: I
=
+
2
1 D
-
(17)
ΔIL = inductor ripple current calculated in Equation 15
IOUT(max) = maximum output current necessary in the application
D = duty cycle calculated in Equation 14
(
)
IN
OUT
IN
L
S
OUT
V
×
V
V
Inductor Calculation: L =
ΔI
f
V
-
´
´
(18)
VIN = typical input voltage
VOUT = desired output voltage
fS = minimum switching frequency of the converter
ΔIL= estimated inductor ripple current, see Equation 19
OUT
L
OUT(max)
IN
V
Inductor Ripple Current Estimation: ΔI
= (0.2 to 0.4)
I
V
´
´
(19)
ΔIL = estimated inductor ripple current
IOUT(max) = maximum output current necessary in the application
F
OUT(max)
Average Forward Current of Rectifier Diode: I
= I
(20)
IOUT(max) = maximum output current necessary in the application
D
F
F
Power Dissipation in Rectifier Diode: P
= I
V
´
(21)
IF = average forward current of the rectifier diode
VF = forward voltage of the rectifier diode
www.ti.com
Equations to Calculate the Power Stage of a Boost Converter
SLVA372D - NOVEMBER 2009 - REVISED NOVEMBER 2022
Submit Document Feedback
Basic Calculation of a Boost Converter's Power Stage
7
Copyright © 2022 Texas Instruments Incorporated

## [стр. 8]

R1/2
FB
Current Through Resistive Divider Newtwork for Output Voltage Setting: I
100
I
³
´
(22)
IFB = feedback bias current from data sheet
FB
2
R1/2
V
Value of Resistor Between FB Pin and GND: R
= I
(23)
OUT
OUT
1
2
FB
V
Value of Resistor Between FB Pin and V
: R = R
1
V
æ
ö
´
-
ç
÷
è
ø
(24)
VFB = feedback voltage from the data sheet
IR1/2 = current through the resistive divider to GND, calculated in Equation 22
VOUT = desired output voltage
OUT(max)
OUT(min)
S
OUT
I
D
Minimum Output Capacitance, if not given in the data sheet: C
=
f
ΔV
´
´
(25)
IOUT(max) = maximum output current of the application
D = duty cycle calculated in Equation 14
fS = minimum switching frequency of the converter
ΔVOUT = desired output voltage ripple
:
OUT(max)
L
OUT(ESR)
I
ΔI
Additional Output Voltage Ripple due to ESR
ΔV
= ESR
+
1 D
2
æ
ö
´ ç
÷
-
è
ø
(26)
ESR = equivalent series resistance of the used output capacitor
IOUT(max) = maximum output current of the application
D = duty cycle calculated in Equation 14
ΔIL = inductor ripple current from Equation 15 or Equation 19
Equations to Calculate the Power Stage of a Boost Converter
www.ti.com
8
Basic Calculation of a Boost Converter's Power Stage
SLVA372D - NOVEMBER 2009 - REVISED NOVEMBER 2022
Submit Document Feedback
Copyright © 2022 Texas Instruments Incorporated

## [стр. 9]

9 References
1.
Understanding Boost Power Stages in Switchmode Power Supplies (SLVA061)
2.
Voltage Mode Boost Converter Small Signal Control Loop Analysis Using the TPS61030 (SLVA274)
3.
Data sheet of TPS65148 (SLVS904)
4.
Data sheet of TPS65130 and TPS65131 (SLVS493)
5.
Robert W. Erickson: Fundamentals of Power Electronics, Kluwer Academic Publishers, 1997
6.
Mohan/Underland/Robbins: Power Electronics, John Wiley & Sons Inc., Second Edition, 1995
7.
Improve Your Designs with Large Capacitance Value Multi-Layer Ceramic Chip (MLCC) Capacitors by
George M. Harayda, Akira Omi, and Axel Yamamoto, Panasonic
8.
Comparison of Multilayer Ceramic and Tantalum Capacitors by Jeffrey Cain, Ph.D., AVX Corporation
Spacer
10 Revision History
Changes from Revision C (January 2014) to Revision D (November 2022)
Page
•
Updated the numbering format for tables, figures, and cross-references throughout the document..................1
Changes from Revision B (July 2010) to Revision C (January 2014)
Page
•
Changed VIN to VOUT in Figure 5-1 ....................................................................................................................5
Changes from Revision A (April 2010) to Revision B (July 2010)
Page
•
Changed IOUT(max) x (1-D) To: IOUT(max) x D in Equation 12 ..............................................................................6
•
Changed IOUT(max) x (1-D) To: IOUT(max) x D in Equation 25 ..............................................................................7
Changes from Revision * (November 2009) to Revision A (April 2010)
Page
•
Added VOUT/VIN (Typical) to Equation 6 ............................................................................................................ 4
•
added VOUT/VIN (Typical) to Equation 19 ...........................................................................................................7
www.ti.com
References
SLVA372D - NOVEMBER 2009 - REVISED NOVEMBER 2022
Submit Document Feedback
Basic Calculation of a Boost Converter's Power Stage
9
Copyright © 2022 Texas Instruments Incorporated

## [стр. 10]

IMPORTANT NOTICE AND DISCLAIMER
TI PROVIDES TECHNICAL AND RELIABILITY DATA (INCLUDING DATA SHEETS), DESIGN RESOURCES (INCLUDING REFERENCE
DESIGNS), APPLICATION OR OTHER DESIGN ADVICE, WEB TOOLS, SAFETY INFORMATION, AND OTHER RESOURCES "AS IS"
AND WITH ALL FAULTS, AND DISCLAIMS ALL WARRANTIES, EXPRESS AND IMPLIED, INCLUDING WITHOUT LIMITATION ANY
IMPLIED WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE OR NON-INFRINGEMENT OF THIRD
PARTY INTELLECTUAL PROPERTY RIGHTS.
These resources are intended for skilled developers designing with TI products. You are solely responsible for (1) selecting the appropriate
TI products for your application, (2) designing, validating and testing your application, and (3) ensuring your application meets applicable
standards, and any other safety, security, regulatory or other requirements.
These resources are subject to change without notice. TI grants you permission to use these resources only for development of an
application that uses the TI products described in the resource. Other reproduction and display of these resources is prohibited. No license
is granted to any other TI intellectual property right or to any third party intellectual property right. TI disclaims responsibility for, and you
will fully indemnify TI and its representatives against, any claims, damages, costs, losses, and liabilities arising out of your use of these
resources.
TI's products are provided subject to TI's Terms of Sale or other applicable terms available either on ti.com or provided in conjunction with
such TI products. TI's provision of these resources does not expand or otherwise alter TI's applicable warranties or warranty disclaimers for
TI products.
TI objects to and rejects any additional or different terms you may have proposed. IMPORTANT NOTICE
Mailing Address: Texas Instruments, Post Office Box 655303, Dallas, Texas 75265
Copyright © 2022, Texas Instruments Incorporated
