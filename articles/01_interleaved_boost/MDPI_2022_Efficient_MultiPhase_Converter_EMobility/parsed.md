# Efficient Multi-Phase Converter for E-Mobility

> Автоматически извлечено из `source.pdf` скриптом `parse_pdf.py`
> Движок: pymupdf. Страниц: 16 из 16.
> Дата извлечения: 2026-08-07 06:42 UTC

Текст не редактировался. Формулы и таблицы могут быть искажены —
при сомнении сверяться с исходным PDF.

---

## [стр. 1]



Citation: Sampath, S.; Rahiman, Z.;
Chenniappan, S.; Sundaram, E.;
Subramaniam, U.; Padmanaban, S.
Efficient Multi-Phase Converter for
E-Mobility. World Electr. Veh. J. 2022,
13, 67. https://doi.org/10.3390/
wevj13040067
Academic Editor: Hang Gao
Received: 23 February 2022
Accepted: 11 April 2022
Published: 13 April 2022
Publisher's Note: MDPI stays neutral
with regard to jurisdictional claims in
published maps and institutional affiliations.
Copyright:
© 2022 by the authors.
Licensee MDPI, Basel, Switzerland.
This article is an open access article
distributed
under
the
terms
and
conditions of the Creative Commons
Attribution (CC BY) license (https://
creativecommons.org/licenses/by/
4.0/).
Article
Efficient Multi-Phase Converter for E-Mobility
Suresh Sampath 1
, Zahira Rahiman 1,*
, Sharmeela Chenniappan 2, Elango Sundaram 3
,
Umashankar Subramaniam 4,*
and Sanjeevikumar Padmanaban 5
1
Department of Electrical Engineering, B S Abdur Rahman Crescent Institute of Science and Technology,
Chennai 600 048, India; ssureshavy@gmail.com
2
Department of Electrical Engineering, Anna University, Chennai 600 025, India; sharmeela@annauniv.edu
3
Department of Electrical Engineering, Coimbatore Institute of Technology, Coimbatore 641 014, India;
selangocit@gmail.com
4
Renewable Energy Laboratory, Department of Communications and Networks, College of Engineering,
Prince Sultan University, Riyadh 11586, Saudi Arabia
5
CTiF Global Capsule, Department of Business Development and Technology, Aarhus University,
7400 Herning, Denmark; sanjeevi_12@yahoo.co.in
*
Correspondence: zahirajaved@gmail.com (Z.R.); usubramaniam@psu.edu.sa (U.S.)
Abstract: The recent growth of battery-powered applications has increased the need for highefficiency step-up dc-dc converters. The step-up conversion is commonly used in several applications,
such as electric vehicle (EV); plug-in hybrid electric vehicles (PHEV); photovoltaic (PV) systems; uninterruptible power supplies (UPS); and fuel cell systems. The input current is shared among inductors
by paralleling the converters; resulting in high reliability and efficiency. In this paper; a detailed
analysis for reducing power loss and improving efficiency is discussed. In continuous conduction
mode; the converters are tested with a constant duty cycle of 50%. The multi phase interleaved boost
converter (MPIBC) is controlled by interleaved switching techniques; which have the same switching
frequency but phases are shifted. The efficiency of the six phase IBC model is 93.82% and 95.74%
for an input voltage of 20 V and 200 V, respectively. The presented six phase MPIBC is validated
by comparing it with the existing six phase IBC. The result shows that the presented converter is
better than the existing converter. The prototype of the two phase and six phase IBC is fabricated
to test the performance. It is found that the output power at the load end is highest for the 5 kHz
switching frequency.
Keywords: boost converter; interleaved boost converter; multi-phase interleaved boost converter;
electric vehicle
1. Introduction
In recent years, renewable energy vehicles, EVs and PHEVs are starting to play a
significant role in addressing energy shortages and emissions issues as representatives
of clean energy vehicles [1,2]. The EVs and PHEVs are also regarded as energy storage
units, with the ability to return stored energy to the grid when required [3]. The two-way
communication between the electric vehicle and the grid is referred to as vehicle-to-grid
(V2G) technology [4]. EVs and PHEVs can have various benefits in this application, such as
regulating peak power and shifting peak load. The increased use of battery-powered electric
vehicles has increased the need for power generation. Any renewable energy generation
system, such as a fuel cell, PV, or wind power generation system can be integrated with
an EV to help minimize the burden on the electricity grid. Power converters are in high
demand in renewable energy systems, such as V and fuel cells, as well as EV and standalone battery-powered installations [5]. The ability to provide high gain to raise the
low voltage available from the sources to a usable level is the key requirement of these
converters [6]. The DC-DC converter is the most important part of the conventional BC
providing good gain, simple structure and continuous input current. Using the traditional
World Electr. Veh. J. 2022, 13, 67. https://doi.org/10.3390/wevj13040067
https://www.mdpi.com/journal/wevj

## [стр. 2]

World Electr. Veh. J. 2022, 13, 67
2 of 16
boost topology, it is unable to achieve high gain [7]. Electrical isolation requirements are
not met by the BC method. The wide magnitude difference between the input and output
puts a lot of strain on the switch, and this topology has a lot of current and voltage ripples,
as well as the immense volume and weight of the components [8,9]. These issues can be
solved with the help of the MPIBC model.
The MPIBC method is used to improve power converter performance in terms of efficiency, size, conducted electromagnetic emission and transient response [10]. The benefits
of interleaving include high power capability, modularity, and improved reliability [11,12].
The interleaved technique is presented to improve the performance of the converter [13].
Based on the interleaving techniques as multi-phase, the switching losses are reduced, in
turn, improving the efficiency of the converter [14-16]. The interleaving techniques of
multilevel BC are discussed in [17]. Slah F et al. proposed a converter with reduced voltage
stress of the components [18]. Kim J H et al. presented a new converter topology to reduce
the switching power loss [19]. The input current is distributed equally in the BC inductor,
to reduce the transient current and minimize switching during the transient period [20,21].
For high power applications, IBC is used to develop high voltage gain and reduce the power
loss and design a new model [22,23]. A hardware setup for two stage IBC is presented.
The performance of the converter is compared for two switching frequencies [24]. Lipu
M S H et al. presented a comprehensive review of the various converter configurations.
The various control schemes for EV applications incorporating optimization techniques
are discussed. This paper presents detailed suggestions and challenges for various DC-DC
converter topologies [25].
To demonstrate the effectiveness of the presented MPIBC, a comparison with other
existing converters is presented in Table 1. The parameters, such as ripple voltage, current,
switching frequency, the complexity of the control circuit, high power conversion, and cost
are compared for the converters, such as IBC [1], quasi-Z source converter (QZBC) [26],
multi-port isolated converter (MPIC) [27]. It is observed that in the presented MPIBC
the ripple content, switching frequency and cost is low compared to other converters.
The objectives of various converters with their specific outcomes and their benefits are
compared in Table 2. It is evident from Table 2 that the presented MPIBC is best compared to
other existing converters in terms of low ripple, reduced transients and improved efficiency.
Table 1. MPIBC comparison with other converters.
DC-DC
Converter
Ripple
(Voltage/Current)
Switching
Frequency
Complicity of
Control Circuit
High Power
Conversion
Cost
IBC [1]
Reasonable
High
Reasonable
Suitable
Low
QZBC [26]
Simple
High
Multifaceted
Suitable
Medium
MPIC [27]
Multifaceted
Low
Multifaceted
Suitable
High
MPIBC
Simple
Low
Reasonable
Suitable
Medium
Table 2. Comparison of objective, outcome and benefits of different converters with MPIBC.
DC-DC Converter
Objective
Outcomes
Benefits
IBC [1]
•
Number of passive
components are reduced
•
Obtains a quick
dynamic response
•
Loses are reduced
•
Low ripple current at low
output voltage
•
High switching loss
QZBC [26]
•
To achieve a wide range of
voltage gain as well as an
absolute common ground
•
Achieved maximum
efficiency
•
Switching stress is lower
•
Component ratings are small

## [стр. 3]

World Electr. Veh. J. 2022, 13, 67
3 of 16
Table 2. Cont.
DC-DC Converter
Objective
Outcomes
Benefits
MPIC [27]
•
To optimize the system
behavior by controlling
duty cycle
•
To reduce overall
system losses
•
To look into dynamic analysis.
•
Obtains a quick
dynamic response
•
Power flow can be
controlled independently
•
To obtain high efficiency
•
Voltage gain is high.
•
Low output voltage ripple
MPIBC
•
To decrease ripples in output
current and inductor current
•
In order to achieve optimal
control and a quick
transient response
•
To reduce overall
system losses
•
To improve the
system efficiency
•
Obtains a quick dynamic
response
•
In comparison to IBC, the
current and voltage ripple
are reduced
•
Low switching stress
are obtained
•
More stable
•
Low ripple current at low
output voltage
•
Efficiency improved to
compare with IBC
•
Transients are reduced
The Contribution of this paper is listed as follows:
#
The output power and output voltage of the presented converter are 33.38 kW and
500 V. The inductor ripple current is reduced by 25.76%, hence the size and cost of the
inductor are also less compared to the existing converter, such as BC and IBC.
#
Circuit size reduces due to the reduction in the size of the passive components, which
is a major advantage for the EV model.
#
Based on the interleaved techniques the total power loss is reduced and the total
inductor current is reduced by 26.92% compared to the existing converter.
#
The efficiency of the six phase MPIBC is 98.68% compared to the existing converter
presented in [28]. The efficiency of the six phase converter presented in [28] is 96.9%.
Therefore, the presented converter has improved the efficiency by 1.78%.
2. Multi-Phase Interleaved Boost Converter
2.1. N Phase IBC Schematic Diagram
The MPIBC has an 'N' number of parallel converters are connected and operated by
2π/N or 360◦/N radian phase-shifted among the power switches and same duty ratio (D).
The MPIBC diagram is shown in Figure 1. In MPIBC, the total power is divided by the
number of paralleled converters, and the input and output currents ripples are reduced by
1/N. The inductor currents (IL) are interleaved using phase shifting between the signals of
switches, and the converter's input current (Iin) is the sum of inductor currents of N phases.
MPIBC has the 'N' inductor (L1, L2 . . . LN), 'N' diodes (D1, D2 . . . DN) and 'N' MOSFET
switches (S1, S2 . . . SN). To achieve interleaving, the circuit uses identical inductors, diodes,
and capacitors.
2.2. Design Parameter Calcultaion
The values for inductor, capacitor and duty ratio are calculated for MPIBC by using
the following Equations (1)-(3):
LN =

D ∗Vin
fs ∗N ∗∆Iin

,
(1)
CN =

D ∗Iout
fs ∗N ∗∆Vout

,
(2)
D = 1 -
 Vin
Vout

,
(3)

## [стр. 4]

World Electr. Veh. J. 2022, 13, 67
4 of 16
In this paper, 50% duty ratio is used to design of two, three, four and six phases IBC.
The parameters of interleaved boost converters are listed in Table 3.
Figure 1. N phase IBC schematic diagram.
Table 3. Parameter values of MPIBC.
Parameter
Value
Unit
Solar PV voltage
20
V
Output voltage
40
V
Output current
1.25
A
Output power
50
W
L1 = L2 = L
(2 phase IBC)
3.225 m
H
L1 = L2 = L3 = L
(3 phase IBC)
2.15 m
H
L1 = L2 = L3 = L4 = L
(4 phase IBC)
1.613 m
H
L1 = L2 = L3 = L4 = L5 = L6 = L
(6 phase IBC)
1.075 m
H
C (2 phase IBC)
504 µ
F
C (3 phase IBC)
336 µ
F
C (4 phase IBC)
252 µ
F
C (6 phase IBC)
168 µ
F
Rload
32
Ω
Lload
120 m
H
Switching frequency (fs)
31 k
Hz
Input Current Ripple (∆Iin)
5%
-
Output Voltage Ripple (∆Vout)
2%
-
Duty ratio (D)
50%
-
Drain Source Resistance (RDS(on))
0.045
Ω
Series resistance of Diode (rD)
0.30
Ω
Internal Series resistance of the inductor (rL)
0.25
Ω
Internal Series resistance of the capacitor (rC)
0.05
Ω
The power losses due to MOSFET, diode, inductor and capacitor are calculated using
the equations presented in Table 4. Further, Table 4 shows the equation used for input
power and efficiency calculation.

## [стр. 5]

World Electr. Veh. J. 2022, 13, 67
5 of 16
Table 4. Loss estimation equation for MPIBC.
Equation
Equation Meaning
Equation Number
Pswitch = N ∗RDS(on) ∗D ∗
h
Iout
N∗(1-D)
i2
Switching loss
(4)
Pdiode = ((rD ∗I2
out) + (VF ∗Iout))
Diode loss
(5)
Pinductor = rL ∗
h
Iout
(1-D)
i2
Inductor loass
(6)
Pcapacitor = rC ∗I2
out
Capactior loss
(7)
Pinput = Poutput + Pswitch + Pdiode + Pinductor + Pcapacitor
Input power
(8)
%η =
 Poutput
Pinput

× 100
Efficiency
(9)
3. MPIBC Simulation Result and Discussion
The simulation of two, three, four and six phase IBC is presented in this section for two
different input voltages, such as 20 V and 200 V. The power loss calculation and efficiencies
are compared for different phases. For an input voltage of 20 V, the output voltage of all
phases of MPIBC is shown in Figure 2. From the waveform, the output voltage of two phase
IBC is settled at 38.74 V in 0.2 s. The output current and power comparison are depicted as
shown in Figures 3 and 4 for an input voltage of 20 V. The output current and power values
are 1.211 A and 46.914 W. Similarly, the three, four and six phase IBC output voltages are
settled at 38.89 V, 38.96 V, 39.04 V in 0.15 s, 0.11 s and 0.05 s, respectively. The output current
and power values of the three, four and six phase are 1.215 A, 1.218 A, 1.22 A and 47.251 W,
47.453 W, 47.628 W, respectively. All inductor currents are depicted as shown in Figure 5.
Figure 2. Output voltage comparison of MPIBC at duty cycle of 50%.
Figure 3. Output current comparison of MPIBC at duty cycle of 50%.
Figure 4. Output power comparison of MPIBC at duty cycle of 50%.

## [стр. 6]

World Electr. Veh. J. 2022, 13, 67
6 of 16
Figure 5. All phases inductor current comparison of MPIBC at duty cycle of 50%.
Based on the MPIBC MATLAB simulation at different phases, the output parameters
are listed in Tables 5 and 6. The results presented in Tables 5 and 6 show that if the number
of MPIBC phases is increased, the output parameter, such as the voltage, current and power
also increases. The reason behind this is the reduction of induction current thereby reducing
the switching stress. It indicates that the power losses are decreased while the efficiency of
MPIBC is increased.
Table 5. Output parameter values of MPIBC (input voltage: 20 V).
Number of Phases of
MPIBC
Output Voltage
(Vout) in V
Output Current
(Iout) in A
Output Power
(Po) in W
2
38.74
1.211
46.914
3
38.89
1.215
47.251
4
38.96
1.218
47.453
6
39.04
1.220
47.628
Table 6. Output parameter values of MPIBC (input voltage: 200 V).
Number of Phases of
MPIBC
Output Voltage
(Vout) in V
Output Current
(Iout) in A
Output Power
(Po) in kW
2
434
13.56
5.887
3
435.7
13.62
5.933
4
436.6
13.64
5.956
6
437.4
13.67
5.979
Power Loss and Efficiency Calculation of MPIBC
The total losses and efficiency are calculated from Equations (4)-(9) for two different
input voltages. The values are listed in Tables 7 and 8. The MPIBC total power loss and
percentage of efficiency comparison (two phase IBC) are shown in Figures 6 and 7. It
clearly shows that, as with the increase in phase, the power loss is reduced and percent
efficiency improved. By comparing the four phases of MPIBC, power loss is reduced at
the six phase IBC and the efficiencies of 93.82% (at an input voltage is 20 V) and 95.74% (at
the input voltage is 200 V) are achieved. It is evident that the inductor and capacitor value
(calculated using Equations (1) and (2)) decreases with an increase in the number of phases.
The inductor and capacitor value is minimal for the six phase IBC compared to the four
phase, three phase and two phase IBC. The inductor and capacitor values for the six phase
IBC are 1.075 mH and 168 µF, respectively (refer to Table 1). This reduces the size of the
inductor and capacitor significantly.

## [стр. 7]

World Electr. Veh. J. 2022, 13, 67
7 of 16
Table 7. Total power loss and efficiency values of MPIBC (input voltage: 20 V).
Number of
Phases of
MPIBC
Ploss
(W)
Pinput
(W)
Poutput
(W)
%Efficiency
2
3.1772
50.1772
46.914
93.66
3
3.1565
50.1565
47.251
93.74
4
3.1448
50.1448
47.453
93.78
6
3.1330
50.1330
47.628
93.82
Table 8. Total power loss and efficiency values of MPIBC (input voltage: 200 V).
Number of
Phases of
MPIBC
Ploss
(W)
Pinput
(kW)
Poutput
(kW)
%Efficiency
2
267.347
6.154
5.887
95.66
3
266.880
6.199
5.933
95.71
4
266.263
6.222
5.956
95.72
6
266.010
6.245
5.979
95.74
3.11
3.12
3.13
3.14
3.15
3.16
3.17
3.18
MPIBC( 2 Phase)
MPIBC( 3 Phase)
MPIBC( 4 Phase)
MPIBC( 6 Phase)
Figure 6. Total power loss comparison of MPIBC (input voltage: 20 V).
93.55
93.6
93.65
93.7
93.75
93.8
93.85
MPIBC( 2 Phase)
MPIBC( 3 Phase)
MPIBC( 4 Phase)
MPIBC( 6 Phase)
Figure 7. %Efficiency comparison of MPIBC (input voltage: 20 V).

## [стр. 8]

World Electr. Veh. J. 2022, 13, 67
8 of 16
To validate the results obtained from the MPIBC, a comparison is made with the
existing converters, such as BC and IBC. The passive components, such as the inductor and
capacitor are designed for all the converters taken for comparison. The common parameters
used for BC and IBC are compared with the six phase MPIBC converter. From Table 9, it is
clear that the MPIBC provides better output voltage and output power. The output voltage
and output powers are 500 V and 34.38 kW, respectively. Inductor current reduces by
26.92%. The MPIBC reduces inductor and capacitor values significantly. The inductor and
capacitor values of the six phase MPIBC are 66.67 µH and 168 µF, respectively. Therefore, it
is concluded that the six phase MPIBC is better than the existing converter.
Table 9. MPIBC comparison with existing converter.
Parameters
BC [1]
IBC [1]
MPIBC
Input Voltage (V)
200
200
200
Output Voltage (V)
400
400
500
Number of Phase
1
4
6
Output Power (kW)
30
30
34.38
Switching Freqency (kHz)
20
20
20
Inductor Current (A)
250
250
182.7
Inductor (µH)
400
100
66.67
Capactior (µF)
780
195
168
Duty Cycle
0.5
0.5
0.5
Inductor Current Ripple (A)
12.5
12.5
9.28
To validate specifically the six phase MPIBC, the presented converter is compared with
the existing converter presented in [28]. The comparison result shows that the presented
converter has an efficiency of 98.6% which is better than the existing converter. This
comparison is presented in detail with other parameters in Table 10.
Table 10. Six phase MPIBC comparison with existing converter.
Parameters
Six Phase IBC [28]
Six Phase MPIBC
Input Voltage (V)
24
24
Number of Phase
6
6
Switching Freqency (kHz)
25
25
Duty Cycle
0.6
0.6
Output Voltage (V)
207
213.8
Output Power (W)
453
487.6
%Efficiency
96.90
98.68
4. Hardware Setup for MPIBC
Figure 8 shows a block diagram of a two phase IBC based EV. Two phase IBC hardware
is developed by the two identical inductors, two diodes and two MOSFET switches. The
filter circuit is reduced to harmonic contents. This EV hardware prototype was performed
on a 5 V input supply. To invert a signal, transistors are used, because IBC needs a 180◦
phase shift for the two phase interleaved technique.
4.1. Two Phase IBC Hardware Results and Discussion
A hardware prototype was developed and assembled to validate the actual performance of the two phase IBC. The two phase IBC hardware is designed for 5 kHz and 10 kHz
switching frequencies. The EV hardware prototype for MPIBC (two phase) is shown in
Figure 9. The supply voltage range is considered to be 0-5 V. The converter is fed with a
nominal voltage of 5 V. Figure 10 depicts the two phase IBC output voltage.

## [стр. 9]

World Electr. Veh. J. 2022, 13, 67
9 of 16
Figure 8. MPIBC (Two phase) hardware circuit diagram.

Figure 9. Hardware prototype for MPIBC (two phase).
Figure 10. Load output voltage waveform.

## [стр. 10]

World Electr. Veh. J. 2022, 13, 67
10 of 16
The output voltage comparison at different duty ratios of both switching frequencies
5 kHz and 10 kHz are listed in Table 11. Figures 11 and 12 indicate that the duty ratio
increases simultaneously as the load voltage increases.
Table 11. Comparison of output voltages at different duty cycles and with fs = 5 kHz and fs = 10 kHz.
Vin
(V)
Switching Frequency
fs = 5 kHz
Switching Frequency
fs = 10 kHz
Vout (V)
at
D = 0.3
Vout (V)
at
D = 0.4
Vout (V)
at
D = 0.5
Vout (V)
at
D = 0.7
Vout (V)
at
D = 0.3
Vout (V)
at
D = 0.4
Vout (V)
at
D = 0.5
Vout (V)
at
D = 0.7
0.5
1.2
1.4
1.2
1.2
1.4
1.2
1
1.6
1
2.6
2.8
2.8
3.2
2.8
3.2
2
3.2
1.5
4.4
4.2
4.4
4.4
4.4
4
4.2
5
2
6
5.4
5.6
6
5.6
5.8
6.4
6.4
2.5
6.8
7.2
7.2
7.6
7.2
7.4
8.2
8.2
3
8
8.6
8.8
9.4
8.2
9.6
9.2
10.8
3.5
9.8
9.8
10.2
11
9.4
10
11.6
11.8
Figure 11. Output voltage comparison at different duty cycles and fs = 5 kHz.

Figure 12. Output voltage comparison at different duty cycles and fs = 10 kHz.
Table 12 compares the experimental results of the IBC-based EV that was implemented
in terms of output current, output voltage, and output power at two switching frequencies
of 5 kHz and 10 kHz also maintained at a duty cycle of 50%.

## [стр. 11]

World Electr. Veh. J. 2022, 13, 67
11 of 16
Table 12. Output voltage, current and power comparison at fs = 5 kHz and fs = 10 kHz.
Vin
(V)
Switching Frequency
fs = 5 kHz
Switching Frequency
fs = 10 kHz
Vout
(V)
Iout
(mA)
Pout
(mW)
Vout (V)
Iout
(mA)
Pout
(mW)
0.5
1.4
14
19.6
1.4
14
19.6
1.1
2.3
23
52.9
2.8
28
78.4
1.5
4.3
43
184.9
3.6
36
129.6
2
5.12
51.2
262.14
4.4
44
193.6
2.5
7.38
73.8
544.64
6.2
62
384.4
3
9.46
94.6
894.92
7.4
74
547.6
3.5
9.83
98.3
966.29
8.6
86
739.6
4
11.22
112.2
1258.88
10.2
102
1040.4
4.5
12.54
125.4
1572.52
11
110
1210
5
13.2
132
1742.4
12.4
124
1537.6
Based on the output current, voltage and power comparison at two different switching
frequencies, the load voltage is boosted more at 5 kHz switching frequencies, and the value
of the output voltage is 13.2 V. This output voltage is 1.06 times more than the output
voltage at 10 kHz switching frequency it is shown in Figure 13. If the supply voltage
increases the output current also increased. To achieve more output power at the switching
frequency of 5 kHz compared with a switching frequency of 10 kHz.
Figure 13. Output voltage, current and power comparison at switching frequencies fs = 5 kHz and
fs = 10 kHz.
Inductor voltage, current, and power losses at two different switching frequencies
with a 50% duty cycle are listed in Tables 13 and 14. At 5 kHz switching frequency the two
phase IBC's two inductor voltage, current and power comparison are shown in Figure 14.
The comparison of inductor currents indicates that the second inductor current is minimal.
At a 10 kHz switching frequency and duty cycle of 50%, the two phase IBC's two inductor
voltage, current and power comparison are shown in Figure 15. Over the two phase IBC
power loss is minimum at fs = 5 kHz compared with fs = 10 kHz.
Table 13. Inductor voltage, current and power loss at fs = 5 kHz and D = 50%.
Inductor1
Voltage
(V)
Inductor2
Voltage
(V)
IL1
(A)
IL2
(A)
PL1
(W)
PL2
(W)
0.28
0.28
0.35
0.23
0.098
0.065
0.36
0.36
0.45
0.30
0.162
0.108
0.72
0.56
0.9
0.47
0.648
0.261
0.76
0.68
0.95
0.57
0.722
0.385
0.96
0.84
1.2
0.70
1.152
0.588

## [стр. 12]

World Electr. Veh. J. 2022, 13, 67
12 of 16
Table 13. Cont.
Inductor1
Voltage
(V)
Inductor2
Voltage
(V)
IL1
(A)
IL2
(A)
PL1
(W)
PL2
(W)
1.16
1.04
1.45
0.87
1.682
0.901
1.32
1.2
1.65
1.00
2.178
1.200
1.44
1.28
1.8
1.07
2.592
1.365
1.56
1.48
1.95
1.23
3.042
1.825
1.64
1.64
2.05
1.37
3.362
2.241
Table 14. Inductor voltage, current and power loss at fs = 10 kHz and D = 50%.
Inductor1
voltage
(V)
Inductor2
voltage
(V)
IL1
(A)
IL2
(A)
PL1
(W)
PL2
(W)
0.360
0.240
0.450
0.200
0.162
0.048
0.440
0.280
0.550
0.233
0.242
0.065
0.560
0.400
0.700
0.333
0.392
0.133
0.720
0.520
0.900
0.433
0.648
0.225
0.920
0.720
1.150
0.600
1.058
0.432
1.000
0.760
1.250
0.633
1.250
0.481
1.200
0.960
1.500
0.800
1.800
0.768
1.320
1.040
1.650
0.867
2.178
0.901
1.520
1.160
1.900
0.967
2.888
1.121
1.560
1.280
1.950
1.067
3.042
1.365
Figure 14. Inductor voltage, current and power loss comparison at fs = 5 kHz and D = 50%.
Figure 15. Inductor voltage, current and power loss comparison at fs = 10 kHz and D = 50%.

## [стр. 13]

World Electr. Veh. J. 2022, 13, 67
13 of 16
4.2. Six Phase IBC Hardware Results and Discussion
A hardware prototype was developed and assembled to validate the actual performance of the six phase IBC. The six phase IBC hardware is designed for a 5 kHz switching
frequency. The EV hardware prototype for MPIBC (six phase) is shown in Figure 16. The
supply voltage range is considered to be 0-5 V. The converter is fed with a nominal voltage
of 5 V. Figure 17 depict the six phase MPIBC pulses waveform and Figure 18 shows the six
phase MPIBC output voltage waveform.
Figure 16. Hardware prototype MPIBC (six phase).
Figure 17. Pulse waveform MPIBC (six phase).
Figure 18. Output voltage waveform MPIBC (six phase). **** Duty Cycle = 0.5.
The output current, output voltage, and output power of MPIBC (six phase) at a
switching frequency of 5 kHz are listed in Table 15; if also maintained at a duty cycle
of 50%.

## [стр. 14]

World Electr. Veh. J. 2022, 13, 67
14 of 16
Table 15. Output voltage, current and power at fs = 5 kHz.
Vin
(V)
Switching Frequency
fs = 5 kHz
Vout
(V)
Iout
(mA)
Pout
(W)
0.5
11
110
1.21
1.0
11.6
116
1.34
1.5
11.8
118
1.39
2
12.1
121
1.46
2.5
12.4
124
1.53
3
12.8
128
1.64
3.5
13.1
131
1.72
4
13.6
136
1.85
4.5
14
140
1.96
5
15.6
156
2.43
Based on the output current, voltage and power comparison at 5 kHz switching
frequency of six phase IBC, the values of output voltage is boosted 15.6 V at input voltage
of 5 V. The output voltage and output power values are more for the six phase hardware
setup compare with two phase IBC hardware results. The six phase IBC output voltage
and output power values are 1.181 times and 1.409 times higher than the two phase IBC
hardware setup (refer Tables 11 and 14).
5. Conclusions
A simulation model and hardware implementation of the MPIBC-based EV is discussed in this paper. MPIBC based EV simulation is carried out for four different phases
of IBC and two, three, four and six phases of MPIBC. The simulation is performed with
an input voltage of 20 V and the boosted output voltage is 39.04 V. By comparing four
different phases of MPIBC, the output voltage, current and power values quickly settle
for the six phase model of MPIBC. The power loss calculation of four models reveals that
the six phase IBC has minimum loss with an efficiency of 93.82% for 20 V input voltage.
Further, efficiency of 95.74% is obtained for 200 V input voltage. The effectiveness of the
six phase MPIBC is validated by comparing it with the existing converters, such as BC
and IBC. Further, six phase MPIBC is specifically compared with the existing converter.
The presented converter provides efficiency of 98.68% which is 1.78% better than the existing converter. The two phases of the MPIBC hardware prototype are fabricated and
various comparative analyses are performed in the hardware prototype. The output power
is increased at a 5 kHz switching frequency compared to 10 kHz as per the qualitative
study. The performance and features of the two phases of the MPIBC system under various
duty cycle conditions have been analyzed. The simulation and experimental results show
that the MPIBC can reduce the switching stresses and increases efficiency. By using the
proposed two phase and six phase fabricated MPIBC hardware, the EV output can be
easily controlled. The presented converter provides better performance, smooth speed
control and improved battery life. The proposed converter can be used in various other
applications, such as battery charging, fuel cells, solar panels, PHEV, etc.
Author Contributions: Conceptualization, S.S. and Z.R.; methodology, S.S.; software, S.S.; validation,
Z.R. and S.C.; formal analysis, E.S.; investigation, resources, S.S. and S.P.; data curation, U.S.; writingoriginal draft preparation, S.S.; writing-review and editing, Z.R., S.C., S.P. and U.S.; visualization,
S.S.; supervision, Z.R. and S.P.; project administration, Z.R. and S.C.; funding acquisition, U.S. All
authors have read and agreed to the published version of the manuscript.
Funding: This research received no external funding.
Institutional Review Board Statement: Not applicable.
Informed Consent Statement: Not applicable.

## [стр. 15]

World Electr. Veh. J. 2022, 13, 67
15 of 16
Data Availability Statement: Not applicable.
Acknowledgments: The authors would like to thank the support of Renewable Energy Lab, Prince
Sultan University for technical guidance and contributions to this work.
Conflicts of Interest: The authors declare no conflict of interest.
Nomenclature
N
no phase for MPIBC
D
duty ratio
Vin
input voltage (V)
fs
switching frequency (Hz)
∆Iin
input current ripple
∆Vout
output voltage ripple
Iout
output current (A)
Vout
output voltage (V)
LN
inductance at Nth phase (H)
CN
capacitance at Nth phase (H)
RDS(on)
drain source resistance (Ω)
rD
series resistance of diode (Ω)
VF
diode forward voltage (V)
rL
internal series resistance of the inductor (Ω)
rC
internal Series resistance of the capacitor (Ω)
Pinput
input power (W)
Poutput
output power (W)
Pswitch
losses due to switching operation (W)
Pdiode
losses due to diode (W)
Pinductor
losses due to diode (W)
Pinductor
capacitor power loss (W)
η
efficiency
References
1.
Chakraborty, S.; Vu, H.N.; Hasan, M.M.; Tran, D.D.; Baghdadi, M.E.; Hegazy, O. DC-DC converter topologies for electric vehicles,
plug-in hybrid electric vehicles and fast charging stations: State of the art and future trends. Energies 2019, 12, 1569. [CrossRef]
2.
Elsied, M.; Salem, A.; Oukaour, A.; Gualous, H.; Chaoui, H.; Youssef, F.T.; Belie, D.; Melkebeek, J.; Mohammed, O. Efficient
power-electronic converters for electric vehicle applications. In Proceedings of the 2015 IEEE Vehicle Power and Propulsion
Conference (VPPC), Montreal, QC, Canada, 19-22 October 2015; pp. 1-6.
3.
Lai, C.M. Development of a novel bidirectional DC/DC converter topology with high voltage conversion ratio for electric vehicles
and DC-microgrids. Energies 2016, 9, 410. [CrossRef]
4.
Zahira, R.; Amirtharaj, S.; Selvarani, M.; Lakshmi, D. Design of MOSFET Inverter for a Grid Connected Photovoltaic System. In
Proceedings of the AICTE Sponsored National Conference on Recent Advances in On-Board Ship Automation (RAOBSA-2019),
Chennai, India, 26-27 September 2019; pp. 253-256.
5.
Guo, J.; Rodriguez, R.; Gareau, J.; Schumacher, D.; Alizadeh, M.; Azer, P.; Bauman, J.; Bilgin, B.; Emadi, A. A Comprehensive
Analysis for High-Power Density, High-Efficiency 60 kW Interleaved Boost Converter Design for Electrified Powertrains. IEEE
Trans. Veh. Technol. 2020, 69, 7131-7145. [CrossRef]
6.
Sunddararaj, S.P.; Rangarajan, S.S.; Subashini, N.; Subramaniam, U.; Collins, E.R.; Senjyu, T. A novel T-Type Multilevel Inverter
for Electric Vehicle and Grid-connected applications. In Proceedings of the 2021 7th International Conference on Electrical Energy
Systems (ICEES), Chennai, India, 11-13 February 2021; pp. 166-170.
7.
Subramaniam, U.; Ganesan, S.; Bhaskar, M.S.; Padmanaban, S.; Blaabjerg, F.; Almakhles, D.J. Investigations of AC Microgrid
Energy Management Systems Using Distributed Energy Resources and Plug-in Electric Vehicles. Energies 2019, 12, 2834. [CrossRef]
8.
Sunddararaj, S.P.; Rangarajan, S.S.; Subramaniam, U.; Collins, E.R.; Senjyu, T. A new topology of DC-DC Converter with
Bidirectional Power Flow Capability Coupled with a Nine Multilevel Inverter for EV Applications. In Proceedings of the 2021 7th
International Conference on Electrical Energy Systems (ICEES), Chennai, India, 11-13 February 2021; pp. 177-182.
9.
Dawidziuk, J. Review and comparison of high efficiency high power boost DC/DC converters for photovoltaic applications. Bull.
Pol. Acad. Sci. Tech. Sci. 2011, 59, 499-506. [CrossRef]
10.
Wang, L.; Jiao, H.; Yang, G.; Li, J.; Zhang, Y. Current sharing compensation control method for interleaved current source isolated
bidirectional DC/DC converters. J. Power Electron. 2022, 22, 1-9. [CrossRef]
11.
Zhang, Z.; Xie, S.; Wu, Z.; Xu, J. Soft-switching and low conduction loss current-fed isolated bidirectional DC-DC converter with
PWM plus dual phase-shift control. J. Power Electron. 2020, 20, 664-674. [CrossRef]

## [стр. 16]

World Electr. Veh. J. 2022, 13, 67
16 of 16
12.
Geetha, E.; Maddah, M.; Khosravi, M.M.; Kokabi, A.; Samavatian, V. Dynamic enhancement of interleaved step-up/step-down
DC-DC converters using passive damping networks. J. Power Electron. 2020, 20, 657-663. [CrossRef]
13.
Lai, C.M.; Pan, C.T.; Cheng, M.C. High-efficiency modular high step-up interleaved boost converter for DC-microgrid applications.
IEEE Trans. Ind. Appl. 2011, 48, 161-171. [CrossRef]
14.
Subramaniam, U.; Palanisamy, K.; Deb, S.; Paul, S.; Bharadwaj, S.C.; Dutta, N. A Solution to Fast Battery Charging Technology
With Bi-Directional Series Parallel Resonant Converter LCC In Grid to Vehicle Ambient. In Proceedings of the Innovations in
Power and Advanced Computing Technologies (i-PACT), Vellore, India, 22-23 March 2019; pp. 1-6.
15.
Henn, G.A.; Silva, R.N.A.L.; Praca, P.P.; Barreto, L.H.; Oliveira, D.S. Interleaved-boost converter with high voltage gain. IEEE
Trans. Power Electron. 2010, 25, 2753-2761. [CrossRef]
16.
Sunddararaj, S.P.; Rangarajan, S.S.; Subramaniam, U.; Collins, E.R.; Senjyu, T. Performance of P/PI/PID Based controller in
DC-DC Converter for PV applications and Smart Grid Technology. In Proceedings of the 2021 7th International Conference on
Electrical Energy Systems (ICEES), Chennai, India, 11-13 February 2021; pp. 171-176.
17.
Iqbal, A.; Bhaskar, M.S.; Meraj, M.; Padmanaban, S.; Rahman, S. Closed-loop control and boundary for CCM and DCM of
nonisolated inverting N× multilevel boost converter for high-voltage step-up applications. IEEE Trans. Ind. Electron. 2019,
67, 2863-2874. [CrossRef]
18.
Abhiram, J.S.; Kumar, S.S.; Jayaprakash, P.; Subramaniam, U. Design and Analysis of a High Step-Up DC-DC Converter Fed Grid
Connected Fuel Cell System. In Proceedings of the 2020 International Conference on Power Electronics and Renewable Energy
Applications (PEREA), Kannur, India, 27-28 November 2020; pp. 1-6.
19.
Kim, J.H.; Jung, Y.C.; Lee, S.W.; Lee, T.W.; Won, C.Y. Power loss analysis of interleaved soft switching boost converter for
single-phase PV-PCS. J. Power Electron. 2010, 10, 335-341. [CrossRef]
20.
Wang, S.; Wang, Y.; Wang, F. Low current ripple high step-up interleaved boost converter with switched-capacitors and switchedinductors. J. Power Electron. 2021, 21, 1646-1658. [CrossRef]
21.
Murali, A.; Wahab, R.S.; Gade, C.S.R.; Annamalai, C.; Subramaniam, U. Assessing Finite Control Set Model Predictive Speed
Controlled PMSM Performance for Deployment in Electric Vehicles. World Electr. Veh. J. 2021, 12, 41. [CrossRef]
22.
Meraj, M.; Bhaskar, M.S.; Iqbal, A.; Al-Emadi, N.; Rahman, S. Interleaved multilevel boost converter with minimal voltage
multiplier components for high-voltage step-up applications. IEEE Trans. Power Electron. 2020, 35, 12816-12833. [CrossRef]
23.
Ghaffarpour, S.H.; Afjei, S.E.; Salemnia, A. A novel soft-switched interleaved high step-up DC-DC converter for high-efficiency
conversion. Int. J. Circuit Theory Appl. 2021, 49, 2515-2532. [CrossRef]
24.
Suresh, S.; Zahira, R. Hardware Implementation of Two Stage Interleaved Boost Converter for Electric Vehicle Application. Int. J.
Veh. Struct. Syst. 2021, 13, 373-377. [CrossRef]
25.
Lipu, M.S.H.; Faisal, M.; Ansari, S.; Hannan, M.A.; Karim, T.F.; Ayob, A.; Hussain, A.; Miah, M.; Saad, M.H.M. Review of Electric
Vehicle Converter Configurations, Control Schemes and Optimizations: Challenges and Suggestions. Electronics 2021, 10, 477.
[CrossRef]
26.
Zhang, Y.; Liu, Q.; Li, J.; Sumner, M. A common ground switched Quasi- Z -Source Bidirectional DC-DC Converter with wide
voltage -Gain range for EVs with Hybrid Energy Sources. IEEE Trans. Ind. Electron. 2017, 65, 5188-5200. [CrossRef]
27.
Zhao, C.; Round, S.D.; Kolar, J.W. An isolated three- port bidirectional DC-DC converter with decoupled with power flow
management. IEEE Trans. Power Electron. 2018, 23, 2443-2453. [CrossRef]
28.
Maalandish, M.; Hosseini, S.H.; Ghasemzadeh, S.; Babaei, E.; Alishah, R.S.; Jalilzadeh, T. Six-phase interleaved boost dc/dc
converter with high-voltage gain and reduced voltage stress. IET Power Electron. 2017, 10, 1904-1914. [CrossRef]
