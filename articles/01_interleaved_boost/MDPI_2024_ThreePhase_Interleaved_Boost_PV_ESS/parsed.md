# Design and Analysis of a Three-Phase Interleaved DC-DC Boost Converter with an Energy Storage System for a PV System

> Автоматически извлечено из `source.pdf` скриптом `parse_pdf.py`
> Движок: pymupdf. Страниц: 14 из 14.
> Дата извлечения: 2026-08-07 06:42 UTC

Текст не редактировался. Формулы и таблицы могут быть искажены —
при сомнении сверяться с исходным PDF.

---

## [стр. 1]

Citation: Pirashanthiyah, L.;
Edirisinghe, H.N.; De Silva, W.M.P.;
Bolonne, S.R.A.; Logeeshan, V.;
Wanigasekara, C. Design and Analysis
of a Three-Phase Interleaved DC-DC
Boost Converter with an Energy
Storage System for a PV System.
Energies 2024, 17, 250. https://
doi.org/10.3390/en17010250
Received: 29 November 2023
Revised: 18 December 2023
Accepted: 24 December 2023
Published: 3 January 2024
Copyright: © 2024 by the authors.
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
energies
Article
Design and Analysis of a Three-Phase Interleaved DC-DC Boost
Converter with an Energy Storage System for a PV System
L. Pirashanthiyah 1
, H. N. Edirisinghe 1, W. M. P. De Silva 1, S. R. A. Bolonne 1, V. Logeeshan 1,*
and C. Wanigasekara 2,*
1
Department of Electrical Engineering, University of Moratuwa, Moratuwa 10400, Sri Lanka;
170451x@uom.lk (L.P.); 170155t@uom.lk (H.N.E.); 170111g@uom.lk (W.M.P.D.S.); sheronb@uom.lk (S.R.A.B.)
2
Institute for the Protection of Maritime Infrastructures, German Aerospace Center (DLR),
27572 Bremerhaven, Germany
*
Correspondence: logeeshanv@uom.lk (V.L.); chathura.wanigasekara@dlr.de (C.W.)
Abstract: This paper describes a groundbreaking design of a three-phase interleaved boost converter
for PV systems, leveraging parallel-connected conventional boost converters to reduce input current
and output voltage ripple while improving the dynamic performance. A distinctive feature of this
study is the direct connection of a Li-Ion battery to the DC link, which eliminates the need for
an additional charging circuit, which is a departure from conventional approaches. Furthermore,
the combination of an MPPT controller and a closed-loop fuzzy controller with a current control
mode ensures accurate switching signal generation for all three phases. The meticulously tuned
system exhibits a remarkably low ripple content in the output voltage, surpassing calculated values,
and demonstrates a superior dynamic performance. The investigation extends to a comprehensive
analysis of losses, encompassing inductor copper loss and semiconductor conduction loss. In all
scenarios, the converter exhibits an efficiency exceeding 93%, highlighting its robust performance as
an effective solution for PV systems.
Keywords: three-phase interleaved boost converter; fuzzy logic controller; MPPT controller;
lithium-ion battery
1. Introduction
The prevailing global energy mix is predominantly sustained by conventional sources,
notably fossil fuels, giving rise to environmentally harmful consequences through the
emission of toxic gases. This phenomenon greatly adds to the general concern about global
warming and intensifies climate-related issues. A noticeable global trend towards renewable energy alternatives has been seen, in response to environmental requirements and the
growing expenses linked with conventional fuel sources [1]. A global pledge has been made
to reach a significant 70% renewable energy consumption by 2030 [1]. Solar energy emerges
as a promising and reliable renewable energy solution in the face of challenges faced by saturated hydroelectric resources and the demanding prerequisites of wind power adoption,
such as extended prefeasibility studies, expansive land requirements, significant initial
investments, and advanced technological infrastructures. This is especially important for
tropical nations, where the plentiful solar resource provides an exceptional opportunity for
sustainable and eco-friendly energy generation, addressing both environmental concerns
and the specialized energy demands of tropical climatic zones.
In this scenario, a substantial integration of solar power into the grid can give rise to
various technical challenges. These challenges encompass low inertia, voltage irregularities,
frequency fluctuations, power oscillations, harmonic distortions, a diminished power factor,
transient disturbances, flickering, and increased strain on power lines, transformers, and
energy storage systems [2]. Given the intermittent nature of solar electricity, ensuring
voltage stability becomes a critical concern for utility providers [3]. Nonetheless, it is crucial
Energies 2024, 17, 250. https://doi.org/10.3390/en17010250
https://www.mdpi.com/journal/energies

## [стр. 2]

Energies 2024, 17, 250
2 of 14
to uphold the voltage to a permissible level to guarantee the safe operation of equipment.
Therefore, energy storage systems along with power electronic converters can be utilized
to mitigate voltage violation [4]. Power electronic converters are widely used in renewable
energy systems to maintain the output voltage at a constant level [5]. Buck, boost, buckboost, and push-pull converters are some basic converters that have been used for decades.
Nonetheless, they have some issues that add intolerable ripples to the input current [6].
Generally, solar energy produces relatively low output voltages that need to be boosted
to a certain level. Conventional DC-DC boost converters are simple power electronic devices. Still, they cannot be used in high-power applications due to their low voltage gain
and high current ripple and voltage ripple [7]. Moreover, substantial switching and conduction losses led to poor efficiency in addition to the reverse recovery problem [6]. As
a result, conventional boost converters were modified with various voltage booster circuits/techniques to improve their performance. Magnetic coupling, the voltage multiplier
circuit, the switched inductor and voltage lift technique, the multi-stage/level, and the
switched capacitor (charged pump) are some available techniques that can be used to boost
the voltage further [8,9].
As a voltage-boosting technique, magnetic coupling is a suitable option because it
offers a lot of possibilities for design freedom [10]. It also offers high efficiency in softswitched types and low conduction losses since the switches can be designed on the LV
side. Its ease of adjustment also makes it attractive [11]. Thus, it can be widely used
in high-power applications, DC microgrids, and regenerative, as well as bidirectional,
applications. Nonetheless, this approach has limitations, such as enormous dimensions,
leakage inductances, and significant voltage spikes [8,12].
Additionally, the voltage multiplier technique is appealing due to its ability to handle high voltages, structure, and integration with various other converters. However, it
requires many cells for the HV application and causes more stress on components [8,13].
Moreover, switch inductors and voltage lift circuits are also used in large-gain DC-DC
boost converters due to their excellent boost capability and ability to integrate with many
converters. Nevertheless, this is not recommended for high-power applications, and they
need more passive components [8,14].
In addition to single-level boost converters, multi-level boost converters are widely
used in renewable energy systems because they offer a high power density, high-quality
output voltage, high efficiency, high voltage-to-current ratio, compatible structure, low
switching losses, lower harmonic distortion, large voltage gain without an extreme duty
cycle, and high switching frequency [15]. However, controlling this converter is extremely
difficult and requires an external balancing circuit since they do not provide a voltage
balance for the DC link [16]. Additionally, the large number of components makes this
converter relatively bulky in size [8,13]. The switched capacitor/charge pump circuit is
also commonly used in high-gain DC-DC applications due to its merits, such as its low
cost, compactness, weightlessness, high power density, and fast response time. The major
drawback of this option is the lack of output voltage regulation [8,14].
The quadratic boost converter is another option that can be formed by cascading
two conventional boost converters [17]. Here, the quadratic function of the duty ratio
gives the voltage gain value. Thus, this limited voltage gain restricts this converter from
high-power applications [18]. Also, high ripples in the input current support the demerits
of this converter [8-13].
This study aims to fill a significant research gap by concentrating on the unexplored
domain of three-phase interleaved boost converters directly connected to Li-Ion batteries
without the incorporation of a charging circuit. The existing literature predominantly
focuses on conventional boost converters or their modifications, leaving space in the exploration of three-phase interleaved boost converters in this specific configuration. Addressing
this gap, this research introduces and investigates a novel configuration, sorting out an
underrepresented area of power electronics. Furthermore, this investigation extends to the
often-neglected aspect of loss analysis in three-phase interleaved boost converters. While

## [стр. 3]

Energies 2024, 17, 250
3 of 14
efficiency is commonly mentioned in the context of conventional boost converters, detailed
loss analysis, particularly considering inductor copper loss and semiconductor conduction
loss in the proposed system, remains less common in the literature. This research aims to
bridge this gap by providing a comprehensive examination of the losses associated with
the proposed configuration, contributing valuable insights to the field of power electronics
and converter design.
Interleaved boost converters (IBCs) are outstanding in addressing the limitations
of traditional boost converters, particularly in high-power applications. Their parallel
configuration enhances their performance, making IBCs increasingly popular. In highpower scenarios, IBC deployment is essential, offering benefits such as ripple reduction,
an improved conversion efficiency, reliability, a minimized filter component size, reduced
stress on switching elements, and an increased power density [6,19,20].
This study explores a 3Ph-IBC with an energy storage system for a solar power generation unit. Furthermore, the performance of the converter and controller is investigated
using numerical simulations at various irradiance and temperature levels. A charging
circuit is typically employed to connect batteries to a DC link. In contrast, the Li-Ion battery
is directly connected to the DC link in this design. Additionally, a three-phase voltage
source inverter (VSI) is deployed to transfer the generated energy to the AC grid using
MATLAB Simulink. Finally, a detailed loss analysis was carried out to investigate the effect
of parasitic losses in a 3-Ph-IBC.
The main contributions of this investigation are as follows:
1.
A three-phase IBC with Li-ion battery integration;
2.
The integration of a current control fuzzy logic controller with an MPPT for a 3-Ph IBC;
3.
Loss analysis for a 3-Ph IBC.
Overall, this research introduces a novel and comprehensive solution to address
technical challenges in solar power integration, presenting a three-phase interleaved
boost converter with unique features and providing a detailed analysis of its performance
and efficiency.
The following is an outline of this article: Section 1 discusses several existing DC-DC
converters, the motivation, and the main contribution. Section 2 covers the converter circuit
description and mathematical modeling, the controller, and the energy storage system.
Section 3 provides simulation results and discussion. Section 4 focuses on the impact of
inductor internal resistance and semiconductor devices on the efficiency of the 3Ph-IBC and
power losses. Finally, Section 5 presents the conclusion based on a thorough examination
of the obtained simulation results.
2. The Design of the Interleaved Boost Converter
The following section describes the design of the interleaved boost converter.
2.1. Proposed System Description and Mathematical Modeling
The 3Ph-IBC has proven to be the best multi-phase IBC due to its numerous benefits [21,22]. A schematic of a simple three-phase interleaved boost converter is shown in
Figure 1. In this case, the converter's input has three conventional boost converters in
parallel, each consisting of an inductor, a diode, and an IGBT switch. The design and simulation of the converter and associated systems are executed using the MATLAB Simulink
platform. It is important to note that this study primarily concentrates on the integration of
the converter with the battery storage and the mathematical modeling and design of the
variable source inverter fall outside the scope of this study at the moment.
The specifications of the selected solar module are shown in Table 1.
PV Array Modeling:
The SolarTech Universal PERCB-W-285 model was used for the simulation.

## [стр. 4]

Energies 2024, 17, 250
4 of 14
Phase 2
Phase 3
Phase 1
Switch 1
Switch 2
Switch 3
Phase 1
Phase 2
Phase 3
Switch 2
Switch 3
Switch 1
Figure 1. Three-phase interleaved boost converter.
Table 1. Specifications of solar module-SolarTech Universal PERCB-W-285.
Parameters
Quantity
Maximum Power
285 W
Number of cells
60
Voc
39.6 V
Isc
9.25 A
Vmp
32.2 V
Imp
8.85 A
Temperature coefficient of Voc
-0.281%
Temperature coefficient of Isc
0.041005%
Temperature coefficient of Pmpp
-0.36%
Operating temperature
-40 °C to 85 °C
NOCT
41 ± 3 °C (at lowest temperature 20 °C)
The 3Ph-IBC is designed for a 5 kW power rating and a 10 kHz switching frequency. It
tries to stabilize the output voltage at 400 V, delivering a dependable and constant power
supply. To minimize fluctuations and ensure a smooth power delivery, the intended output
voltage ripple is restricted to 1%, and the input current ripple is meticulously maintained
at 5%.
When designing the solar PV system, the operating voltage range of the system was
initially determined. The panel string output voltage should be within this range. The
maximum module voltage is related to the lowest ambient temperature.
ModuleVOC,max = VOC × [1 + (Tmin -TSTC) × (Tk,Voc) × (0.01)]
(1)
ModuleVOC,min = Vmpp × [1 + (Tmax -TSTC) × (Tk,mpp) × (0.01)]
(2)
The lowest expected ambient temperature was considered to be 25 °C in this study.
Furthermore, the NOCT was assumed to be 44 °C, and the maximum temperature was calculated as 54 °C. By substituting the provided values from Table 1 into Equations (1) and (2),
the operating voltage range of the solar PV module was calculated to be 28.84 V and 39.38 V,
respectively.
Pmpp = Num.o f.modules × Num.o f.strings × ModulePmax
(3)
Further, to obtain the design specifications, nine modules per string and two parallel
connected strings are selected to have the 5 kW rated output according to Equation (3).

## [стр. 5]

Energies 2024, 17, 250
5 of 14
Calculations for the components:
Vout
Vin
=
1
1 -D
(4)
I = Power
V
(5)
∆I = 0.05 × Iin
(6)
∆V = 0.01 × Vout
(7)
Inductance(L) =
D × Vin
Fsw × ∆I
(8)
Capacitance(C) =
D × Vout
Fsw × ∆V × Rout
(9)
Equations (1)-(9) were utilized to calculate the converter parameters for the simulation
model. The values obtained are shown in Table 2 below.
Table 2. Converter parameters of the simulation model.
Parameters
Quantity
Power rating (kW)
5
Switching frequency (kHz)
10
Output voltage ripple (%)
1%
Input current ripple (%)
5%
Output voltage (V)
400
Input voltage (V)
260-355
Input current (A)
14.085-19.23
Output current (A)
12.5
Duty ratio
0.1125-0.35
Gain
1.13-1.54
Inductance (mH)
15
Output capacitance (µF)
35
Input capacitance (µF) (VInitial = 50 V)
50
When a converter operates in discontinuous conduction mode (DCM), the efficiency
can be impacted negatively. The DCM introduces additional switching losses due to the
discontinuity in the inductor current. The efficiency reduction is generally associated with
increased conduction losses and potentially higher peak currents. For the three-phase
interleaved boost converter, maintaining a continuous conduction mode is necessary to
obtain the most power from the PV panels.
Furthermore, the Li-Ion battery is directly linked to the converter output/DC connection, eliminating the need for a separate charging circuit. Consequently, it is guaranteed
that the DC link voltage remains constant. A three-phase voltage source inverter is further
attached to the DC link for the purpose of converting the DC to AC and transmitting
electricity to the AC grid. A block diagram of the whole system is shown in Figure 2.
Figure 2. System block diagram.

## [стр. 6]

Energies 2024, 17, 250
6 of 14
2.2. Controller
To optimize the converter's dynamic performance, closed-loop controllers can be
employed. Due to their simplicity, PI/PD/PID controllers are frequently used. However,
the core issue with the PID contoller is that it is challenging to adopt and achieve the
greatest performance when utilized with a non-linear system. In addition, it influences
output voltage regulation and requires exact linear mathematical modeling [23]. Fuzzy
logic controllers, in comparison to conventional controllers, provide superior precision
and an enhanced performance under transient situations. Also, they provide a reliable
performance while regulating the output voltage without the requirement for precise
mathematical models [24]. Therefore, the fuzzy logic controller is adopted for this design
in this study.
Furthermore, when integrating a solar system, it is critical to discuss MPPT controllers
since solar energy is intermittent and temperature- and insolation-dependent. Hence, it
is crucial to guarantee that the power generation is always at its maximum, regardless
of the state of the atmosphere. Because of this, a maximum power point tracker (MPPT)
was utilized in this design to generate the maximum power under various environmental
circumstances. The hill-climbing algorithm/Perturb and Observe method (P&O Algorithm)
has been selected for MPPT implementation even though there are many other options
available [25,26]. A P-V curve and a flowchart for a hill-climbing algorithm are shown in
Figure 3 and Figure 4, respectively.
Left of MPP
Increase
in P
Decrease
in P
Increase in P
Decrease in P
MPP
Reduction in VPV
Increase in VPV
VMPP
V
P
Right of MPP
Figure 3. The P-V curve of the solar panel.
Measure I(n) & v(n)
START
Calculate Power
P(n) = V(n) * I(n)
P(n) > P(n-1)
V(n) > V(n-1)
V(n) > V(n-1)
VREF (n) = VREF (n-1) + ΔVREF
VREF (n) = VREF (n-1) - ΔVREF
VREF (n) = VREF (n-1) - ΔVREF
VREF (n) = VREF (n-1) + ΔVREF
YES
NO
YES
NO
YES
NO
RETURN
Figure 4. Hill-climbing algorithm flowchart.

## [стр. 7]

Energies 2024, 17, 250
7 of 14
In this hill-climbing algorithm, the PV current and voltage are sent into the MPPT
controller where it calculates the power, change in power, and change in voltage to deliver
an output as a reference voltage. This reference voltage could be used to calculate the
reference current for the closed-loop current controller. A comparison of the 3Ph-IBC
output current with this reference current generates an error signal. The error signal and
the error signal change are then supplied to the fuzzy inference system to generate a switch
control signal. To create switch pulses, the triangular carrier signal is compared to the
switch control signal. The controller is shown in Figure 5.
FUZZY
Controller
Pulse Generator
MPPT
Controller
I PV
V PV
V Ref_MPPT
I PV
V PV
X
P PV_Input
V Ref_MPPT
X

%
I Ref_MPPT
I Ref_MPPT
I Out_IBC
Memory

Error
+

-
Change of Error
Switching Pulses
+

-
Figure 5. The converter controller.
2.3. Energy Storage System
A Li-Ion battery is connected across the converter terminals in the proposed architecture. Since the battery serves as a source, the converter's output voltage is always fixed.
In this case, the charging current for the energy storage is determined by substituting the
values of the power and converter output voltage into Equation (5). However, the ultimate
objective is to draw the maximum energy from the solar panel. Since the converter's terminal voltage is constant, the converter's output current should be controlled by changing
the duty factor. The PV current and PV terminal voltage must be monitored in the MPPT
control scheme to sense the power extracted from the PV module. The reference current
is calculated from this power and compared to the feedback current, which is the output
of the 3Ph-IBC. In this way, the current mode fuzzy logic controller is used to connect the
battery to the DC link directly.
Furthermore, a current controller is highly advised for direct battery connections.
The battery is a voltage source, and the PV module-connected converter also works as
a controlled voltage source if the voltage is regulated. As there is no series impedance
between the two in such a case, a high circulating current flows through the controlled
source. Thus, a current-based controller must be implemented and combined with the
MPPT controller to provide a duty factor to achieve the ultimate goal.
The primary goal of this battery storage system is to meet the peak demand. Also,
when solar energy production is poor, this battery may be utilized to supply the energy
to the grid. This battery is beneficial for adjusting the voltage as well as functioning as a
backup power source in the case of a system breakdown.
This battery bank is designed to provide 2 kWh energy each day. Moreover, the
load subsystem efficiency, including the round-trip battery efficiency, wiring loss, and
conversion efficiency, needs to be considered as no battery is 100% efficient. Further, the
round-trip efficiency is assumed to be around 95% for Li-Ion batteries, and this loss estimate
is simply based on the chemistry of the battery. In addition to that, wiring losses that may
occur as the current flows between the battery and the converter are also considered. It is
better to combine all these losses into a single factor in this case.
We will multiply 0.95 for round-trip efficiency by 0.97 for wiring losses by 0.92 for
conversion efficiency, and this provides an overall subsystem efficiency of 85%. Further, in
this case, we will select 3 days of autonomy, which should provide sufficient reserve power
for our application. Additionally, a temperature coefficient factor also needs to be included
in the calculation, as the battery capacity will typically drop at lower temperatures. Next,

## [стр. 8]

Energies 2024, 17, 250
8 of 14
the depth of discharge (DoD) describes how far down the battery can be drained. In this
design, it is kept as 30% to avoid complete discharge. The total usable battery capacity is
given by
TUBC =
DD × DoA × α
V × LSE × MDOD = 2000 × 3 × 1.2
408 × 0.85 × 0.3 = 69.2 Ah
(10)
where TUBC is the total usable battery capacity, DD is the daily demand, DoA is the days
of autonomy, α is the temperature coefficient, V is the voltage, LSE is the load subsystem
efficiency, and MDOD is the maximum depth of discharge.
In this case, 34 batteries with terminal voltages of 12 V are connected in series to
provide a nominal voltage of 408 V, which is closer to the recommended 400 V. Furthermore,
the battery state control algorithm is designed to ensure that the SOC is kept between 30%
and 80%. To prevent a 100% depth of discharge during failures, the band's bottom margin
is retained at a maximum of 30%.
It is extremely important to select a good algorithm to regulate the charging and
discharging of the battery because we developed this battery without a charging circuit.
Overcharging is not permitted in a battery. Thus, it is necessary to guarantee that the
battery is not overcharged while still ensuring a long operating life without interfering
with the system's performance [27]. The state control method is illustrated schematically in
Figure 6, which also reveals the operating modes of the Li-Ion battery.
Measure SOC & Pin
30 ≤ SOC ≤ 80
Sense Pin
400 ≤ Pin ≤ 1000
Yes
Discharge

Pout = 0
Yes
Pin < 400
No
No

Discharge
Pout = 0

Yes
SOC > 80
Charge
No
No
HALT

(No operation)
Yes
SOC < 30 //  Pin > 400
SOC > 80 // Pin < 1000
Discharge

Pout = 1000
Pin > 1000

Yes
Discharge

Pout = Pin - 1000



Discharge
Pout = Pin

SOC < 30
Yes
Figure 6. Battery state-control diagram.
3. Simulation Results and Discussion
The simulation results are provided in this section to validate the operation of the
proposed converter. The MATLAB Simulink platform was utilized to design the converter
in this case, and the simulation results are discussed further below.
The output voltage and ripple level are shown in Figure 7a. In this instance, the
measured ripple voltage is 0.51 V, or 0.125%, greatly exceeding our expectations. The target
output ripple is 1%. Additionally, Figure 7b-d serve as evidence for the fact that the converter's input voltage, solar panel output power, and insolation are all subject to variations
over time. It is more than sufficient to confirm the MPPT controller's functionality.
Furthermore, Figure 8 shows switch pulses generated by the three switches, each of
which is 120 degrees phase-shifted. In Figure 9, the inductor current ripple waveforms
for three phases vary between 0.086 V and 0.561 V, accounting for 0.475 V of peak-to-peak
ripple. Further, it is 3.4% of the input current, which is less than the specified value of 5%.
Figure 10 depicts the diode current waveforms for three diodes with a peak-to-peak ripple
of 1 A. Additionally, Figure 11 illustrates the voltage stress on switches for the three phases.

## [стр. 9]

Energies 2024, 17, 250
9 of 14
400
300
200
100
0
Voltage (V)
0       0.5        1       1.5       2        2.5       3        3.5       4       4.5        5
Time (s)
0       0.5        1       1.5       2        2.5       3        3.5       4       4.5        5
Time (s)
300
250
200
150
100
50
Voltage (V)
6000
5000
4000
3000
2000
1000
0
Power (W)
0       0.5        1       1.5       2        2.5       3        3.5       4       4.5        5
Time (s)
1400
1200
1000
800
600
400
200
0       0.5        1       1.5       2        2.5       3        3.5       4       4.5        5
Time (s)
Power density (W/m2)
(a)
(b)
(c)
(d)
P_in_pv
Insolation
V_in_pv
Converter Output Voltage
Figure 7. (a) Converter output voltage (inset: shows the zoomed view of the ripple), (b) converter
input voltage variation, (c) generated solar power, (d) insolation.
Figure 8. Switch pulses (blue: Switch 1, red: Switch 2, green: Switch 3).
Figure 9. Inductor current waveform (blue: Inductor 1, red: Inductor 2, green: Inductor 3).

## [стр. 10]

Energies 2024, 17, 250
10 of 14
Figure 10. Diode-current waveform (blue: Diode 1, red: Diode 2, green: Diode 3).
Figure 11. Voltage stress on switches (blue: switch 1, red: Switch 2, green: Switch 3).
The findings of the simulation verify the operational integrity of the suggested converter and offer information on its performance that is consistent with the objective of
this research. Achieving a ripple voltage of 0.51 V, below the 1% target, demonstrates the
converter's efficacy in maintaining stable output characteristics. Dynamic variations in
the input voltage, solar panel output power, and insolation, as depicted in Figure 7b-d,
underscore the converter's adaptability to real-world conditions, supporting the motivation
to address technical challenges in solar power integration.
Additionally, the detailed analysis of critical components, including switch pulses,
inductor current ripple, diode current waveforms, and voltage stress on switches, validates
the converter's robustness under various operating conditions. The consistent adherence to
design specifications and the mitigation of ripple effects align with the identified research
gaps, emphasizing the significance of the proposed converter in addressing issues associated with voltage violation, frequency fluctuation, and energy storage in solar power
systems. Overall, the simulation results support the aims and highlight the converter's
potential to accelerate the shift to efficient and reliable renewable energy alternatives.
4. Loss Analysis
The interleaved boost converter's voltage gain must increase with the increase in the
duty cycle, but this is typically not the case because of parasitic losses. This section explains

## [стр. 11]

Energies 2024, 17, 250
11 of 14
how parasitic losses and converter efficiency change as elements such as inductors, diodes,
and transistors change.
The 3Ph-IBC is only taken into consideration for loss analysis here due to its simplicity.
Rather than connecting to a solar panel, a simple DC voltage supply is connected to the
converter's input and boosted to a constant 400 V via closed-loop voltage control fuzzy
logic control for this loss analysis.
Furthermore, loss analysis was performed in four different scenarios, with one parameter changing while the others remained constant. First, the series inductor resistance was
varied for three phases to investigate inductor copper loss and semiconductor conduction
losses. The input voltage, or gain, was then varied to determine the efficiency relationship.
Afterward, by varying the switching resistance, semiconductor conduction losses were
investigated. Finally, the converter's efficiency was investigated under various load conditions by varying the load without changing the cumulative impedance value (the total load
impedance is 100 Ω).
Evidently, the inductor copper loss shows a linear escalation concerning the inductor
resistance value, as depicted in Figure 12a. Notably, the semiconductor conduction loss
follows a similar trend, increasing alongside higher inductor resistance values, as observed
in the same image. Consequently, the efficiency decreases with increasing resistance levels,
as seen in Figure 12b.
In Figure 13a, the inductor copper loss exhibits an upward trend with increasing gain
values. This observation leads to the conclusion that maintaining lower gain values is
preferable to mitigate inductor copper loss. Similarly, Figure 13b illustrates an increasing
trend in semiconductor conduction loss with gain values, considering switches and diodes
collectively for simplicity. The collective rise in the inductor copper loss and semiconductor
conduction losses with gain values indicates a decrease in efficiency. This deduction is
affirmed by the findings in Figure 13c.
The influence of switch resistance on inductor copper losses is apparent from the
approximately declining trend observed in Figure 13d. With an increase in switch resistance, semiconductor conduction losses exhibit fluctuating waveforms in Figure 13e, and,
similarly, the waveform in Figure 13f reflects the resultant reduction in overall converter
efficiency. Despite waveform changes, the overall trends in Figure 13e,f show an increase
in semiconductor conduction losses and a fall in efficiency.
Figure 13g shows that changing the output resistance does not affect the inductor copper loss. Finally, Figure 13h,i show how the semiconductor conduction loss and converter
efficiency vary with the output resistance while maintaining a constant cumulative output
impedance of 100 Ω.
20
30
40
50
60
70
0
10
20
30
40
50
60
Loss (W)
Inductor resistance (mΩ)
Inductor copper loss
Semiconductive conduction loss
0
10
20
30
40
50
60
Efficiency (%)
Inductor resistance (mΩ)
(a)
(b)
96.4
96.0
95.6
95.2
94.8
94.4
94.4
94.0
Figure 12. (a) Loss vs. inductor resistance graph; (b) converter efficiency vs. inductor resistance graph.

## [стр. 12]

Energies 2024, 17, 250
12 of 14
14
16
18
20
22
24
26
28
30
32
34
1.25
2.25
3.25
4.25
Inductor copper loss (W)
Gain
0
10
20
30
40
50
60
70
80
1.25
2.25
3.25
4.25
Semiconductor losses (W)
Gain
1.25
2.25
3.25
4.25
Efficiency(%)
Gain
99
98
97
96
95
94
93
(a)
(b)
(c)
21.91
21.92
21.93
21.94
21.95
21.96
0.000
0.003
0.006
0.009
0.012
Inductor copper losses (W)
Switch resistance (Ω)
42
44
46
48
50
52
54
0.000
0.003
0.006
0.009
0.012
Semiconductor losses (W)
Switch resistance(Ω)
0.000
0.003
0.006
0.009
0.012
Efficiency (%)
Switch resistance (Ω)
96.1
96.0
95.9
95.8
95.7
95.6
95.5
95.4
(d)
(e)
(f)
21.4
21.6
21.8
22.0
22.2
22.4
0
20
40
60
80
100
Inductor copper losses (W)
Output resistance (Ω)
40
42
44
46
48
50
52
0
20
40
60
80
100
Semiconductor losses (W)
Output resistance (Ω)
0
20
40
60
80
100
Efficiency(%)
Output resistance (Ω)
96.0
95.8
95.5
95.3
95.0
94.8
94.5
(g)
(h)
(i)
Figure 13. (a) Inductor copper loss vs. gain graph, (b) semiconductor conduction loss vs. gain graph,
(c) converter efficiency vs. gain graph, (d) inductor copper loss vs. switch resistance, (e) semiconductor conduction loss vs. switch resistance graph, (f) converter efficiency vs. switch resistance,
(g) inductor copper loss vs. output resistance, (h) semiconductor conduction loss vs. output resistance,
(i) converter efficiency vs. output resistance.
5. Conclusions
Our research efforts concluded in the detailed design and study of a three-phase
interleaved DC-DC boost converter linked with an energy storage system, specifically
adapted for a 5 kW solar power generation unit. The system is implemented using MATLAB/Simulink and connects with the grid through a three-phase voltage source inverter.
The direct connection of the Li-ion battery to the DC link, which eliminates the need for an
additional charging circuit, distinguishes this study from other studies.
This study adds a new perspective to the current literature by including a detailed
loss analysis that sheds information on the converter's efficiency. In addition to adding
to the expanding body of knowledge in power electronics, the aforementioned approach
demonstrates the design's originality and practicality in the three-phase interleaved DC-DC
boost converter.
This study includes both steady-state analysis and simulation, demonstrating how
well the converter performs in meeting predetermined objectives, especially in reducing

## [стр. 13]

Energies 2024, 17, 250
13 of 14
voltage violations. The simulation results show substantially decreased voltage fluctuations,
confirming the efficiency of the technology. Moreover, the thorough loss analysis yields an
impressive minimum observed efficiency of almost 93%.
In addition to technical considerations, the research focuses on the system's dynamic
performance, with the controller smoothly calibrated to elicit appealing dynamics. This
approach not only tackles voltage-related difficulties but also assures the converter's ability
to handle dynamic conditions. Currently, we are actively working on the experimental
design and practical implementation, with the aim of presenting comprehensive results in
our follow-up publication.
Author Contributions: Conceptualization, V.L., L.P. and W.M.P.D.S.; Methodology, H.N.E.; Investigation, S.R.A.B.; Supervision, V.L. and C.W. All authors have read and agreed to the published version
of the manuscript.
Funding: The APC was funded by German Aerospace Centre (DLR).
Conflicts of Interest: We have no conflict of interest to disclose.
References
1.
Chilamkurti, N.R.; Vinod, A.; Al-Madfai, H.A. Ä Smart System Architecture for 70% Renewable Energy Penetration by 2030.
IEEE Access 2021, 9, 43855-43865.
2.
Shirbhate, A.S.; Jawale, P.D.; Professor, A. Power Quality Improvement in PV Grid Connected System by Using Active Filter:
Review. Int. J. Adv. Res. Electr. Electron. Instrum. Eng. 2007, 3297, 388-395.
3.
Yadav, A.; Kishor, N.; Negi, R. Bus Voltage Violations under Different Solar Radiation Profiles and Load Changes with Optimally
Placed and Sized PV Systems. Energies 2023, 16, 653. [CrossRef]
4.
Saha, A.N.; Saha, S.; Das, S.R. Mitigating Voltage Violation Issues using Battery Storage System with Power Electronics Converters.
In Proceedings of the IEEE International Conference on Power Electronics, Drives and Energy Systems, Montreal, QC, Canada,
27-30 June 2021; pp. 1-6.
5.
Elgendy, M.A.; Zahawi, B.; Atkinson, D.J. Power Electronic Converters for Control of Renewable Energy Systems with Constant
Voltage Output. IEEE Trans. Power Electron. 2016, 31, 1683-1696.
6.
Newlin, D.J.S.; Ramalakshmi, R.; Rajasekaran, S. A performance comparison of interleaved boost converter and conventional
boost converter for renewable energy application. In Proceedings of the International Conference on Green High Performance
Computing, Denver, CO, USA, 17-21 November 2013.
7.
Bhattacharyya, S.P.; Saha, S.; Roy, A.K. Ä High Gain Voltage Lift Quasi-Z-Source Converter for Renewable energy Applications.
IEEE Trans. Power Electron. 2018, 33, 1267-1279.
8.
Shrivastava, V.; Gupta, A.K. A Literature Review on High Gain dc-dc Boost Converter. Int. J. Res. Advent Technol. 2019, 7, 397-404.
[CrossRef]
9.
Hasanpour, S.; Siwakoti, Y.; Blaabjerg, F. New single-switch quadratic boost dc/dc converter with low voltage stress for renewable
energy applications. IET Power Electron. 2020, 13, 4592-4600. [CrossRef]
10.
Hu, J.; Li, X.; Li, C. A Dual-Sided LCC Resonant Converter with Magnetic-Coupling-Enhanced Voltage Gain for High-Power
applications. IEEE Trans. Power Electron. 2021, 36, 136-147.
11.
Kashem, M.A.; Islam, M.A.; Zahirul Alam, A.H.M. A Soft-Switched DC-DC Converter with Magnetic Coupling for High-Efficiency
and Low-Profile Applications. IEEE Trans. Ind. Electron. 2020, 67, 6679-6689.
12.
Alzahrani, A.; Ferdowsi, M.; Shamsi, P. A family of scalable non-isolated interleaved DC-DC boost converters with voltage
multiplier cells. IEEE Access 2019, 7, 11707-11721. [CrossRef]
13.
Rosas-Caro, J.C.; Ramirez, J.M.; Peng, F.Z.; Valderrabano, A. A DC-DC multilevel boost converter. IET Power Electron. 2010, 3,
129-137. [CrossRef]
14.
Bakhtiyari, N.T.; Prabhu, B.R.; Patil, S. Engineering and Technology (A High Impact Factor). Int. J. Innov. Res. Sci. 2019, 8,
1101-1114.
15.
Chen, S.; Yuan, Y.; Wang, F. A High Voltage-Gain Five-Level Boost Converter with Low Switching Voltage Stress. IEEE Trans.
Power Electron. 2021, 36, 11336-11345.
16.
Zhang, J.; Yang, Z.; Liu, F. A Modified Career-Based Phase-Shifted PWM Strategy for Multilevel Boost Converter with Self-Voltage
Balance. IEEE Trans. Ind. Electron. 2019, 66, 9628-9639.
17.
Maity, P.K.; Singh, B.P. Design and Analysis of Quadratic Boost Converter for Photovoltaic Applications. IEEE Trans. Ind. Electron.
2021, 68, 746-756.
18.
Mishra, S.; Panda, S.K. An Interleaved Quadratic Boost Converter with Novel Charge Pumping Technique for High Power PV
Applications. IEEE Trans. Power Electron. 2021, 36, 12261-12273.
19.
Nahar, S.; Uddin, M.B. Analysis the performance of interleaved boost converter. In Proceedings of the International Conference on
Electrical Engineering and Information & Communication Technology, Dhaka, Bangladesh, 13-15 September 2018; pp. 547-551.

## [стр. 14]

Energies 2024, 17, 250
14 of 14
20.
Shenoy, L.; Nayak, C.; Mandi, R. Design and Implementation of Interleaved Boost Converter. Int. J. Eng. Technol. 2017, 9, 496-502.
21.
Chitra, P.; Seyezhai, R. Basic Design and Review of Two Phase and Three Phase Interleaved Boost Converter for Renewable
Energy Systems. Int. J. Appl. Sci. 2014, 1, 1-26.
22.
Wang, H.; Lee, F.C. Control and Design of a Three-Phase Interleaved Boost Converter for High-Power Applications. IEEE Trans.
Power Electron. 2018, 33, 5224-5234.
23.
Bharathi, M.L.; Kirubakaran, D. Fuzzy logic controlled PV supported triple stage ILBC converter system with improved dynamic
response. In Proceedings of the 2017 International Conference on Computation of Power, Energy Information and Commuincation
(ICCPEIC), Melmaruvathur, India, 22-23 March 2017; pp. 592-598.
24.
Jantzen, J.; Design of Fuzzy Controllers; Technical University of Denmark: Kongens Lyngby, Denmark, 1998.
25.
Reddy, J.; Natarajan, S. Control and Analysis of MPPT Techniques for Standalone PV System with High Voltage Gain Interleaved
Boost Converter. Gazi Univ. J. Sci. 2018, 31, 515-530.
26.
Rajeswari, S. Comparative analysis on performance of power converters for MPPT using PAO technique. Int. J. Eng. Sci. Res.
Technol. 2017, 6, 364-369.
27.
Bolonne, S.R.A.; Chandima, D.P. Sizing an energy system for hybrid li-ion battery-supercapacitor RTG cranes based on state
machine energy controller. IEEE Access 2019, 7, 71209-71220. [CrossRef]
Disclaimer/Publisher's Note: The statements, opinions and data contained in all publications are solely those of the individual
author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to
people or property resulting from any ideas, methods, instructions or products referred to in the content.
