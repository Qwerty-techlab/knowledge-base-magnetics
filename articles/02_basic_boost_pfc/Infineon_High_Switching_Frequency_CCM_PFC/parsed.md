# High switching frequency CCM PFC operation with TRENCHSTOP™ 5 WR5 IGBT discretes

> Автоматически извлечено из `source.pdf` скриптом `parse_pdf.py`
> Движок: pymupdf. Страниц: 23 из 23.
> Дата извлечения: 2026-08-07 06:42 UTC

Текст не редактировался. Формулы и таблицы могут быть искажены —
при сомнении сверяться с исходным PDF.

---

## [стр. 1]

Application Note
Please read the Important Notice and Warnings at the end of this document
V1.2
www.infineon.com
page 1 of 23
2022-09-21
AN-2020-19

High switching frequency CCM PFC operation
with TRENCHSTOP™ 5 WR5 IGBT discrete
Validity of TRENCHSTOP™5 WR5 IGBT in high switching frequency
operation in CCM (continuous conduction mode) PFC (power factor
correction)
About this document
This application note demonstrates the performances of TRENCHSTOP™ 5 WR5 IGBT in high switching
frequency and its application benefits CCM PFC for major home appliances.
Scope and purpose
This document aims to help PFC design engineers in home appliance applications who want to increase
switching frequency to achieve the inductor on the board to minimize the system form factor and lower the
system cost.
Intended audience
Design engineers of major home appliances power systems, application engineers, students

Table of contents
About this document ....................................................................................................................... 1
Table of contents ............................................................................................................................ 1
1
Introduction .......................................................................................................................... 2
2
PFC for major home appliances ................................................................................................ 3
3
Power loss analysis of IGBT in CCM PFC ..................................................................................... 5
3.1
Conduction loss calculation ................................................................................................................... 5
3.2
Switching loss calculation ...................................................................................................................... 6
3.3
Power loss analysis of Infineon's TRENCHSTOP™ 5 WR5 IGBT .............................................................. 6
3.3.1
Electrical characteristics .................................................................................................................... 7
3.3.2
Power loss simulation ...................................................................................................................... 11
4
Experimental results ............................................................................................................. 13
4.1
System description ................................................................................................................................ 13
4.2
Efficiency and thermal performance evaluation ................................................................................. 14
4.3
EMI performance evaluation ................................................................................................................. 15
4.4
SC immunity of IKW40N65WR5 ............................................................................................................. 17
5
Conclusion ........................................................................................................................... 20
6
References ........................................................................................................................... 21
Revision history............................................................................................................................. 22

## [стр. 2]

Application Note
2 of 23
V1.2
2022-09-21
High switching frequency CCM PFC operation with TRENCHSTOP™ 5
WR5 IGBT discretes
Introduction
1
Introduction
In modern society, as the energy consumed by home appliances is steadily increasing, it has become more and
more important to maintain a high-power factor (PF) when using these appliances. Air conditioners in
particular are the most power-consuming home appliance; and for their design, a power factor correction (PFC)
is mandatory. In general, air conditioner applications have a power rating of 1.8 kW or higher, thereby IGBTs are
the most appropriate switching device considering the cost-performance ratio. Although IGBTs show much
lower conduction loss than power MOSFETs, slower switching speed and tail current characteristics of IGBTs
have been limited to increase in the switching frequency. In general, the proper switching frequency of IGBTs
has been considered to be far below 60 kHz. In PFC systems, lower switching frequency increases the size of the
boost inductor, which cannot then be placed on the main circuit board. In this case, the cost of the inductor is
inevitably high, and the form factor of the system will be limited. Moreover, the high risk of short-circuit
incidents that may occur during installation or maintenance processes requires short-circuit rated IGBTs for
safety. In order to ensure the protection of IGBTs from short-circuit (SC) conditions, a SC rated IGBT is required.
In this case, the IGBT has to cope with certain disadvantages in terms of Vce(sat) and switching performance in
order to ensure short-circuit immunity. Thus, the demand for integrating the PFC inductor on the main board
by increasing switching frequency continues to increase, to minimize the system form factor, to reduce the cost
of inductor, and to use high performance IGBTs.

## [стр. 3]

Application Note
3 of 23
V1.2
2022-09-21
High switching frequency CCM PFC operation with TRENCHSTOP™ 5
WR5 IGBT discretes
PFC for major home appliances
2
PFC for major home appliances
The boost converter in Figure 1 is the most common topology for active PFC circuits, as it can maintain
continuous input current, which is most beneficial in terms of lower harmonics and less EMI filter requirements.
For PFC in major home appliances especially, CCM (continuous conduction mode) is used because of easier EMI
filter design owing to fewer harmonics, lower conduction loss due to lower RMS current, and lower turn-off
loss.
vac
L
D
Co
Ro
+
-
Vout
S
EMI filter
BD

Figure 1
PFC circuit with boost converter topology
The inductor current ripple reaches its maximum value when the instantaneous value of AC input is equal to
𝑉𝑜𝑢𝑡/2. However, at high power CCM PFC, the minimum AC input voltage, 𝑉𝑎𝑐_𝑚𝑖𝑛, is approximately at least
180V and its peak value is always higher than 𝑉𝑜𝑢𝑡/2. The required inductance, L, for CCM PFC is obtained by
using the follow equations.

∆𝐼𝐿= 1
𝐿∫
√2𝑉𝑎𝑐_𝑚𝑖𝑛(𝑡)𝑑𝑡
𝐷𝑇𝑠
0
= 𝑉𝑜𝑢𝑡
𝐿∙𝑓𝑠𝑤
(𝑉𝑜𝑢𝑡-√2𝑉𝑎𝑐_𝑚𝑖𝑛
𝑉𝑜𝑢𝑡
)
(1)

𝐿≥
𝑉𝑎𝑐_𝑚𝑖𝑛2
%𝑟𝑖𝑝𝑝𝑙𝑒∙𝑃𝑜𝑢𝑡∙𝑓𝑠𝑤(
𝑉𝑜𝑢𝑡-√2𝑉𝑎𝑐_𝑚𝑖𝑛
𝑉𝑜𝑢𝑡
)
(2)

where, %ripple = ∆𝐼𝐿/𝐼𝐿_𝑝𝑘, and 𝐼𝐿_𝑝𝑘= √2𝑃𝑜𝑢𝑡/𝑉𝑎𝑐_𝑚𝑖𝑛.
As the value of inductance becomes larger, the switching ripple current will become smaller. However, a bulkier
inductor is required and this can result in an increase in cost. Meanwhile, the PFC can maintain CCM operation
as long as ∆𝐼𝐿/2  is less than 𝐼𝐿; thereby, it is necessary to choose the optimal inductance in terms of cost and
performance. The required inductance for CCM PFC in accordance with the switching frequency is indicated in
Figure 2. Figure 2 shows that the required inductance becomes significantly smaller as switching frequency
increases. When it exceeds 60 kHz, it will become small enough to be placed on the main board.
The capacitance of the PFC output capacitor is independent of the switching frequency, but needs to meet both
hold-up time requirement (when brownout occurs) and low-frequency ripple voltage requirements as shown in
Equation 2 and Equation 3.

## [стр. 4]

Application Note
4 of 23
V1.2
2022-09-21
High switching frequency CCM PFC operation with TRENCHSTOP™ 5
WR5 IGBT discretes
PFC for major home appliances
𝐶𝑜𝑢𝑡≥2𝑃𝑜𝑢𝑡∙𝑡ℎ𝑜𝑙𝑑-𝑢𝑝
𝑉𝑜𝑢𝑡
2 -𝑉𝑜𝑢𝑡_𝑚𝑖𝑛
2
(3)
𝐶𝑜𝑢𝑡≥
𝑃𝑜𝑢𝑡
2𝜋∙𝑓𝑎𝑐∙∆𝑉𝑜𝑢𝑡∙𝑉𝑜𝑢𝑡

(4)

In general, the hold-up time is defined as one cycle of line frequency, i.e it is greater than than 20 ms at 50 Hz or
16 ms at 60 Hz. Meanwhile, the ripple voltage requirement is defined by the customer, and is determined at the
range approximately 10-20 V.

0
200
400
600
800
1000
20
30
40
50
60
70
80
Inductance [uH]
fsw [kHz]
0.2
0.3
0.4
0.5
%ripple

Figure 2
Inductance vs. switching frequency for Pout=2.5 kW, and Vac_min=180 V

## [стр. 5]

Application Note
5 of 23
V1.2
2022-09-21
High switching frequency CCM PFC operation with TRENCHSTOP™ 5
WR5 IGBT discretes
Power loss analysis of IGBT in CCM PFC
3
Power loss analysis of IGBT in CCM PFC
In order to verify the validity of Infineon's TRENCHSTOP™ 5 WR5 IGBT, power loss calculation methods are
described as follows.
3.1
Conduction loss calculation
Ia
Ts
Ib
ILavg.
ΔIL
0
Diode
If(t)
IGBT
Ic(t)
IL(t)
t
DTs
ΔIL
0
π
( 2Vac/L)sinωt
 2Vacsinωt
Vac_avg
Iac_avg
IL(t)
Ts
DTs
ωt

Figure 3
IGBT and FRD waveforms of PFC in CCM operation
Figure 3 indicates the IGBT and FRD waveforms of PFC in CCM operation.
In CCM boost-converter operation, the voltage drops at IGBT, Vce_sat and FRD, VF can be indicated as follows:

𝑉𝑐𝑒𝑠𝑎𝑡(𝑡) = 𝑟𝑐𝑒 𝐼𝑐(𝑡) + 𝑉𝑐𝑒0
(5)

𝑉𝐹(𝑡) = 𝑟𝐹 𝐼𝑐(𝑡) + 𝑉𝐹0
(6)

where,  𝐼𝑐(𝑡) = 𝐼𝑎+
𝐼𝑏-𝐼𝑎
𝐷𝑇𝑠𝑡

Therefore, the conduction loss of the IGBT for a single period can be calculated by

𝑃𝐼𝐺𝐵𝑇_𝐶𝑂𝑁= 1
𝑇𝑠
∫
𝑉𝑐𝑒(𝑡) × 𝐼𝑐(𝑡)𝑑𝑡
𝐷𝑇𝑠
0

                    = 1
𝑇𝑠
∫
{𝑉𝑐𝑒0 (𝐼𝑎+ 𝐼𝑏-𝐼𝑎
𝐷𝑇𝑠
𝑡) + 𝑟𝑐𝑒(𝐼𝑎+ 𝐼𝑏-𝐼𝑎
𝐷𝑇𝑠
𝑡)
2
} 𝑑𝑡
𝐷𝑇𝑠
0

                    = 𝐷{ 𝑉𝑐𝑒0
2 (𝐼𝑎+ 𝐼𝑏) + 𝑟𝑐𝑒
3 (𝐼𝑎
2 + 𝐼𝑎𝐼𝑏+ 𝐼𝑏
2)}

(7)

However, small amounts of ripple current do not contribute much to RMS (root mean square) value, as it makes
the calculation more complicated. Thus, the ripple component can be neglected, and equation 7 can be simply
expressed as

𝑃𝐼𝐺𝐵𝑇_𝐶𝑂𝑁= 𝐷(𝑡)(𝑉𝑐𝑒0𝑖𝐿(𝑡) + 𝑟𝑐𝑒𝑖𝐿
2(𝑡))
(8)

Meanwhile, since the input voltage is sinusoidal, D(t) and iL(t) are expressed as

𝐷(𝑡) =
𝑉𝑜𝑢𝑡-√2𝑉𝑎𝑐𝑠𝑖𝑛𝜔𝑡
𝑉𝑜𝑢𝑡

(9)

𝑖𝐿(𝑡) = √2𝐼𝑎𝑐𝑠𝑖𝑛𝜔𝑡
             = √2𝑃𝑜𝑢𝑡
𝜂𝑉𝑎𝑐 𝑠𝑖𝑛𝜔𝑡
(10)

## [стр. 6]

Application Note
6 of 23
V1.2
2022-09-21
High switching frequency CCM PFC operation with TRENCHSTOP™ 5
WR5 IGBT discretes
Power loss analysis of IGBT in CCM PFC
Therefore, the average conduction loss of the IGBT can be derived by

< 𝑃𝐼𝐺𝐵𝑇_𝐶𝑂𝑁>= 1
𝜋∫(𝑉𝑜𝑢𝑡-√2𝑉𝑎𝑐𝑠𝑖𝑛𝜔𝑡
𝑉𝑜𝑢𝑡
) (√2𝑉𝑐𝑒0𝐼𝑎𝑐𝑠𝑖𝑛𝜔𝑡+ 2𝑟𝑐𝑒𝐼𝑎𝑐
2𝑠𝑖𝑛2𝜔𝑡)𝑑𝜔𝑡
𝜋
0

                         = 𝑉𝑐𝑒0𝐼𝑎𝑐(
2√2
𝜋𝑉𝑎𝑐
𝑉𝑜𝑢𝑡) + 𝑟𝑐𝑒𝐼𝑎𝑐
2 (1 -
8√2𝑉𝑎𝑐
3𝜋𝑉𝑜𝑢𝑡)[W]

(11)

In the same way, the conduction loss of the diode is obtained by

< 𝑃𝐹𝑅𝐷_𝐶𝑂𝑁>= 1
𝜋∫-√2𝑉𝑎𝑐𝑠𝑖𝑛𝜔𝑡
𝑉𝑜𝑢𝑡
(√2𝑉𝐹0𝐼𝑎𝑐𝑠𝑖𝑛𝜔𝑡+ 2𝑟𝐹𝐼𝑎𝑐
2𝑠𝑖𝑛2𝜔𝑡)𝑑𝜔𝑡
𝜋
0

                          =
𝑉𝑎𝑐
𝑉𝑜𝑢𝑡(𝑉𝐹0𝐼𝑎𝑐+
8√2
3𝜋𝑟𝐹𝐼𝑎𝑐
2)[W]

(12)
3.2
Switching loss calculation
The conduction loss of IGBT can be obtained with relatively accurate values from a datasheet. On the other
hand, it is impossible to derive the reliable switching loss of an IGBT with datasheet parameters alone. In
particular, turn-on loss is significantly affected by the performance of rectifier diodes. However, if the switching
energy at high temperatures (generally @ 100°C) is predefined in accordance with the gate resistance value and
the level of switching current when combined with a certain diode, switching losses of IGBT can be easily
calculated using the equation below.

𝑃𝑜𝑛 = 𝑓𝑠𝑤∙𝐼𝑜𝑛𝑎𝑣𝑔∙𝐸𝑜𝑛_𝑓𝑎𝑐𝑡𝑜𝑟∙𝑅𝑔_𝑜𝑛_𝑓𝑎𝑐𝑡𝑜𝑟
(13)

𝑃𝑜𝑓𝑓 = 𝑓𝑠𝑤∙𝐼𝑜𝑓𝑓𝑎𝑣𝑔∙𝐸𝑜𝑓𝑓_𝑓𝑎𝑐𝑡𝑜𝑟∙𝑅𝑔_𝑜𝑓𝑓_𝑓𝑎𝑐𝑡𝑜𝑟
(14)

Additionally, the switching loss of diode can be simplified by

𝑃𝐷_𝑠𝑤= 1
2 𝑉𝑜𝑢𝑡∙𝑄𝑐∙𝑓𝑠𝑤
(15)

3.3
Power loss analysis of Infineon's TRENCHSTOP™ 5 WR5 IGBT
In the boost PFC circuit in Figure 1, the potential at the IGBT collector is always higher than the potential at the
IGBT emitter under all conditions. Therefore, the anti-parallel diode of the switch device should not be
conducted in normal operation, except for a very small resonant current when the PFC operates in CrCM
(critical conduction mode). Therefore, the performance requirement of anti-parallel diodes is not that high, this
diode needs to protect the IGBT only for abnormal conditions. Meanwhile, as the demand for higher switching
frequency increases in major home appliances, the switching performance of IGBTs is becoming increasingly
important.
Infineon's TRENCHSTOPTM 5 WR5 IGBT with monolithic anti-parallel diodes, namely reverse conducting (RC)
IGBTs, is shown in Figure 4. The RC IGBT concept is that N+ regions are partially implanted into the P-collector
layer that forms intrinsic P-N diodes allowing the reverse current to flow without a co-pack diode. This IGBT
concept is suitable for boost PFC applications, for which high-performance co-pack diode is not required. This
IGBT family offers the best-in-class performance in terms of both conduction and switching behaviors when
combined with a SiC diode, and it allows high switching frequency operation beyond 60 kHz.

## [стр. 7]

Application Note
7 of 23
V1.2
2022-09-21
High switching frequency CCM PFC operation with TRENCHSTOP™ 5
WR5 IGBT discretes
Power loss analysis of IGBT in CCM PFC

Figure 4
TRENCHSTOPTM 5 WR5 IGBT using reverse conducting (RC) IGBT concept
3.3.1
Electrical characteristics
In order to verify the validity of TRENCHSTOP™ 5 WR5 IGBT in high switching frequency operation, the
IKW40N65WR5 was chosen, and the electrical characteristics with CoolMOSTM P7 MOSFET of the equivalent
rating were compared. Figure 5 shows the static characteristics' comparison between IKW40N65WR5 and an 80
mΩ CoolMOSTM P7 MOSFET. As shown in Figure 5, at low current, the CoolMOSTM P7 MOSFET should be more
advantageous than the IGBT. However, in the case of CoolMOSTM P7 MOSFET, the RDS_on increases rapidly as the
junction temperature increases, while the variation in voltage drop of the IGBT in accordance with its junction
temperature is insignificant. Therefore, as the output power increases and the junction temperature increases,
the IGBT becomes more advantageous. Given the output characteristics in Figure 5 (b), IKW40N65WR5 under
Tj=100°C conditions has superior performance over the 80 mΩ CoolMOSTM P7 MOSFET when the current is 7-8 A
or higher.

## [стр. 8]

Application Note
8 of 23
V1.2
2022-09-21
High switching frequency CCM PFC operation with TRENCHSTOP™ 5
WR5 IGBT discretes
Power loss analysis of IGBT in CCM PFC

(a) Output characteristics @ 25°C
(b) Output characteristics @ 100°C
Figure 5
Output characteristics comparison
In order to validate the TRENCHSTOP™ 5 WR5 IGBT in high-switching frequency and high-power operation, a
double-pulse test was carried out assuming operating conditions of input voltage 180 V, 2.5 kW CCM PFC, and
RMS current of approximately 14.5A.

(a) Turn-on
(b) Turn-off
Figure 6
Switching comparison between TRENCHSTOP™ 5 WR5 IGBT and competitor's highest
performing IGBT with 20 A SiC diode

## [стр. 9]

Application Note
9 of 23
V1.2
2022-09-21
High switching frequency CCM PFC operation with TRENCHSTOP™ 5
WR5 IGBT discretes
Power loss analysis of IGBT in CCM PFC
(a) Turn-on
(b) Turn-off
Figure 7
Switching comparison between TRENCHSTOP™ 5 WR5 IGBT and CoolMOSTM P7 MOSFET
with 30 A Rapid 1 diode
Figure 6 shows the switching performance comparison between IKW40N65WR5 and a competitor's highest
performing IGBT combined with 20A SiC diode. As shown in Figure 6, the competitor's IGBT has 2.1 times higher
Eon and 13.4 % higher Eoff than IKW40N65WR5. Considering the inferior switching performance as well as higher
Vce_sat of the competitor, it is easy to predict that the competitor product will not be suitable for high switching
frequency operation.
Figure 7 shows the switching test results of IKW40N65WR5 and 80 mΩ CoolMOSTM P7 MOSFET combined with 30
A Si diode. Since the reverse recovery current of the boost diode is extremely high when the devices are turned
on instantly, it significantly affects the turn-on energies of both devices, which are much higher than their turnoff energies. The Eon of IKW40N65WR5 and 80 mΩ CoolMOSTM P7 MOSFET are 259 μJ and 255.3 μJ, respectively,
while the Eoff is 123.4 μJ and 74.1 μJ, respectively.
Meanwhile, it is remarkable that the turn-on energy of the TRENCHSTOP™ 5 WR5 IGBT was measured to be
similar to the equivalent CoolMOSTM P7 MOSFET. Nevertheless, neither device is suitable for high-power and
high switching frequency applications with Si diodes due to their extremely high switching energy.

## [стр. 10]

Application Note
10 of 23
V1.2
2022-09-21
High switching frequency CCM PFC operation with TRENCHSTOP™ 5
WR5 IGBT discretes
Power loss analysis of IGBT in CCM PFC
(a) Turn-on
(b) Turn-off
Figure 8
Switching comparison between TRENCHSTOP™ 5 WR5 IGBT and CoolMOSTM P7 MOSFET with
20 A SiC diode
(a) Eon
(b) Eoff
Figure 9
Effect from SiC diode in CCM PFC
Figure 8 shows the switching performance comparison between IKW40N65WR5 and 80 mΩ CoolMOSTM P7
MOSFET combined with 20 A SiC diode, which well demonstrates the effectiveness of the SiC diode. At turn-on
mode, the reverse-recovery current for both devices is much lower than when they are combined with a Si
diode. As a result, the turn-on energy for both devices also become significantly smaller than the turn-on
energy combined with the Si diode.  The Eon of IKW40N65WR5, and 80 mΩ CoolMOSTM P7 MOSFET are 126.1 μJ
and 120.2 μJ, respectively. The turn-off energies of both devices are not as significant as the turn-on energy
improvement. The Eoff of IKW40N60WR5 and 80 mΩ CoolMOSTM P7 MOSFET are 118.3 μJ and 59.9 μJ,
respectively.
Figure 9 well demonstrates how much switching energy can be improved. By combining with a SiC diode, the
turn-on energy of IKW40N65WR5 and 80 mΩ CoolMOSTM P7 MOSFET are improved by 51% and 53%,
respectively.

## [стр. 11]

Application Note
11 of 23
V1.2
2022-09-21
High switching frequency CCM PFC operation with TRENCHSTOP™ 5
WR5 IGBT discretes
Power loss analysis of IGBT in CCM PFC
3.3.2
Power loss simulation
A power loss simulation was carried out to estimate the validity of TRENCHSTOP™ 5 WR5 IGBT in high switching
frequency operations. Table 1 shows the key input parameters for the simulation and its corresponding
calculated values, and the loss simulation results from them are given in Table 2 where the switching frequency
of 60 kHz is applied. The coefficients given in Table 2 are based on the measured data and can be used to
estimate Eon and Eoff at Vce=400V and Tc=100°C, allowing comparison of losses in WR5 and P7 at varied load
conditions and Rg values. The coefficients Eon_factor and Eoff_factor is the gradient of the approximated linear curves
of the measured switching energies as a function of device current. In addition, the coefficients of the linear
equation Esw vs. Rg, normalized to Eon and Eoff values at a given current are also obtained by curve fitting to the
measured switching energies as a function of gate resistance.
Table 1
Loss simulation parameters 1
Table 2
Loss simulation parameters 2
Device
Vce0@100°C
[V]
Rce@100°C
[Ω]
Eon_Factor@100°C
[μJ]
Eoff_factor@100°C
[μJ]
R g_on_factor@100°C
Rg_off_factor@100°C
Pcon
[W]
Pon
[W]
Poff
[W]
Ptot
[W]
IKW40N65WR5
0.67
0.028 9.7E-06*Ion
14.2E-06*Ioff  0.026Rg + 0.41
0.020Rg + 0.71
6.96
5.39 10.64
22.99
80mΩ CoolMOS P7
0
0.130 8.42E-06*Ion  10.7E-06*Ioff  0.011Rg + 0.59
0.03Rg + 0.42
12.26
4.52
6.38
23.16

The summarized loss analysis results are described in Figure 10. The simulation result shows that
IKW40N65WR5 will perform superior to 80 mΩ CoolMOSTM P7 MOSFET at the switching frequency of 60 kHz, a
frequency high enough to have the boost inductor installed on the main board. In the case of IKW40N65WR5, its
conduction loss at high power (2.5 kW) & high switching frequency is expected to be only about 30% -35%; the
remaining 65% -70% is expected to be switching losses. In the case of 80 mΩ CoolMOSTM P7 MOSFET on the
other hand, the conduction loss is expected to be about twice that of IKW40N65WR5, while its switching loss is
smaller than that of IKW40N65WR5.


Input parameter
Value
Unit
Calculated value
Value
Unit
Pout
2500
W
Pin
2577.3
W
fsw
60
kHz
D_avg
0.55

Vin_min
180
Vac
Vin_avg
162.1
V
Vout
400
Vdc
Iin_rms
14.3
A
Eff.
0.97

Iin_avg
12.9
A
Rg_on
15
Ω
Iin_pk
20.2
A
Rg_off
10
Ω
Ia_avg
11.6
A
Delta I
0.2

Ib_avg
14.2
A

## [стр. 12]

Application Note
12 of 23
V1.2
2022-09-21
High switching frequency CCM PFC operation with TRENCHSTOP™ 5
WR5 IGBT discretes
Power loss analysis of IGBT in CCM PFC

Figure 10
Loss calculation result at 60 kHz

## [стр. 13]

Application Note
13 of 23
V1.2
2022-09-21
High switching frequency CCM PFC operation with TRENCHSTOP™ 5
WR5 IGBT discretes
Experimental results
4
Experimental results
4.1
System description
In order to validate the devices for high switching frequency operation, an experiment using 2.5 kW CCM PFC in
Figure 11 was carried out. The system conditions and tested devices are as follows:
›
Pout: 250 W-2500 W
›
Vin: AC 180/230 V-50 Hz
›
Vout: 400 V
Table 3
Tested devices and conditions
Diode
IGBT
30kHz
60kHz
Remark
IDW30C65D1
(30 A Si Rapid 1 diode)
IKW40N60H3
⃝

Rg=20 Ω
IKW40N65WR5
⃝

20A SiC Diode
IDW20G65C2
(20 A SiC diode)
IKW40N65WR5

⃝
Rg=10 Ω
Competitor's highest
performing part

⃝
80 mΩ CoolMOSTM P7
MOSFET

⃝


Figure 11
Test setup: 2.5 kW CCM PFC

## [стр. 14]

Application Note
14 of 23
V1.2
2022-09-21
High switching frequency CCM PFC operation with TRENCHSTOP™ 5
WR5 IGBT discretes
Experimental results
4.2
Efficiency and thermal performance evaluation
Figure 12 shows the results of measuring the efficiency and thermal performance of IKW40N65WR5 and a
conventional SC rated IGBT, IKW40N60H3 at 30 kHz switching frequency conditions. The TRENCHSTOP™ 5 WR5
IGBT is a device that maximizes performance instead of guaranteeing a SCWT (short-circuit withstand time),
and is far superior to IKW40N60H3 that has a SCWT of 5 μsec. The efficiency difference between the two devices
is up to 0.33 %, and the temperature difference at the front side of package is about 25°C respectively, which
means the conventional SC rated IGBT cannot be considered for high switching frequency operation despite its
high reliability.
In Figure 13, IKW40N65WR5, 80 mΩ CoolMOSTM P7 MOSFET, and a competitor's highest performing IGBT are
compared in terms of efficiency and thermal performance under the switching frequency of 60 kHz. The results
show that IKW40N65WR5 overwhelms the competitor's IGBT, both in terms of efficiency and thermal
performance over the entire load condition. Between IKW40N65WR5 and the competitor, the maximum
temperature gap is more than 23°C and the efficiency gap is about 0.3 % at the maximum load. In addition,
IKW40N65WR5 shows better thermal and efficiency performance than the equivalent CoolMOSTM P7 MOSFET at
approximately 2 kW and above, while the equivalent CoolMOSTM P7 MOSFET shows slightly better performance
in the low to mid-load range.



IKW40N65WR5 vs. 40 A SC rated IGBT
Figure 12
Efficiency & thermal performance test result @ fsw=30 kHz

## [стр. 15]

Application Note
15 of 23
V1.2
2022-09-21
High switching frequency CCM PFC operation with TRENCHSTOP™ 5
WR5 IGBT discretes
Experimental results

IKW40N65WR5 vs. Competitor's best performing 40 A IGBT & 80 mΩ CoolMOSTM P7
Figure 13
Efficiency & thermal performance test result @ fsw=60 kHz
The above experimental results are relatively good as seen in the loss simulation results in 2.3.2. From the
results in Fig. 13, CoolMOSTM P7 MOSFET would be ideal for light load conditions, on the other hand, for major
appliances such as air conditioners where full load conditions are very important, TRENCHSTOP™ 5 WR5 IGBT is
clearly the best choice considering cost as well as performance.
4.3
EMI performance evaluation

Figure 14
Conduction EMI test set-up and conditions

## [стр. 16]

Application Note
16 of 23
V1.2
2022-09-21
High switching frequency CCM PFC operation with TRENCHSTOP™ 5
WR5 IGBT discretes
Experimental results
Besides the efficiency and the thermal performance, EMI characteristics are also considered a very important
factor in switching devices for MHA applications. EMI performance is determined by various factors such as
dv/dt, di/dt, gate resistance, EMI filter design and so on, thereby its improvement can vary from system to
system. However, EMI characteristics of each device can be compared by means of testing under the exact
same conditions. The experimental set-up and conditions for comparing EMI performance of devices is
displayed in Figure 14.  Figure 15 shows the EMI characteristics of IKW40N65WR5 and 80 mΩ CoolMOSTM P7
MOSFET combined with 20 A SiC diode. The result shows that the EMI level of IKW40N65WR5 is lower than that
of the CoolMOSTM P7 MOSFET.


Vin : 230 Vac/50 Hz (L, N, & PE), and Pout : 2.5 kW (400 VDC, 6.25 A)
Figure 15
EMI characteristics of IKW40N65WR5 and 80 mΩ CoolMOSTM P7 MOSFET with 20 A SiC diode
combination @ fsw=60 kHz

## [стр. 17]

Application Note
17 of 23
V1.2
2022-09-21
High switching frequency CCM PFC operation with TRENCHSTOP™ 5
WR5 IGBT discretes
Experimental results
4.4
SC immunity of IKW40N65WR5
The TRENCHSTOP™ 5 WR5 IGBT does not guarantee SCWT, but it can withstand the SC condition for a short
period of time in practice because there is parasitic inductance around 1 ~ 2 μH existing in the PCB of PFC
circuit. SC test waveforms of a conventional IGBT guaranteeing SCWT and IKW40N65WR5 are compared in
Figure 16. As a result, IKW40N65WR5 withstands SC condition for 1.9 μsec, which can be sufficient to protect the
IGBT when a proper over current protection circuit is applied.


(a) IKW40N65WR5
12 usec

(b) IKW40N60H3
Figure 16
SC immunity of IKW40N65WR5 vs. a conventional SC rated IGBT, IKW40N60H3

## [стр. 18]

Application Note
18 of 23
V1.2
2022-09-21
High switching frequency CCM PFC operation with TRENCHSTOP™ 5
WR5 IGBT discretes
Experimental results

Figure 17
Example of an overcurrent protection by gate drive IC, 1ED44175N01B
Figure 17 indicates an example of an overcurrent protection circuit by gate drive IC (integrated circuit),
1ED44175N. In CCM PFC, a shunt resistor is generally required for average current mode control, and can also
be used for overcurrent protection using the gate drive IC as shown in this Figure.


Rcs
Rg
Vbus+
VbusAC
1
3
4
OCP
COM
VCC
EN/FLT
2
6
IN
5
OUT
1ED44175N01B
Vcc
Vdd
VRcs for PFC loop control
I/O1
I/O2
I/O3
Power supply of
Vcc and Vdd
Vdd
μ-Controller

## [стр. 19]

Application Note
19 of 23
V1.2
2022-09-21
High switching frequency CCM PFC operation with TRENCHSTOP™ 5
WR5 IGBT discretes
Experimental results
C1:IN (Input voltage of 1ED44175N01B)
C2:Vge (Gate voltage of IGBT)
C2:OCP (Voltage of OCP pin for 1ED44175N01B)
C4:IL (Current of PFC inductor)
C1:IN (Input voltage of 1ED44175N01B)
C2:Vge (Gate voltage of IGBT)
C2:OCP (Voltage of OCP pin for 1ED44175N01B)
C4:IL (Current of PFC inductor)
(a) Cycle by cycle OCP operation
(b) Zoomed in waveform
Figure 18
Cycle-by-cycle overcurrent protection by 1ED44175
C1:IN (Input voltage of 1ED44175N01B)
C2:Vge (Gate voltage of IGBT)
C2:OCP (Voltage of OCP pin for 1ED44175N01B)
C4:IL (Current of PFC inductor)
1 μsec
▪
Rg_on = 27 Ω, Rg_off = 22 Ω
▪
External RC filter of OCP pin (330 Ω/1 nF)
▪
OCP delay time: Tdelay < 500 nsec
Figure 19
PFC inductor SC test
Figure 18 shows a cycle-by-cycle OCP (overcurrent protection) test result using 1ED44175N in CCM PFC. The
collect current of IGBT is limited to the certain OCP level, thereby the IGBT can be protected from overcurrent
conditions. Figure 19 indicates a boost inductor SC test result that clearly shows the IGBT is protected within 1
μsec under the SC condition.

## [стр. 20]

Application Note
20 of 23
V1.2
2022-09-21
High switching frequency CCM PFC operation with TRENCHSTOP™ 5
WR5 IGBT discretes
Conclusion
5
Conclusion

The validity of TRENCHSTOP™ 5 WR5 IGBT at CCM PFC circuit for major home appliances with high switching
frequency up to 60 kHz was investigated and the performance comparison with a competitor's highest
performing part and the equivalent CoolMOSTM P7 MOSFET was carried out. The results showed that the
TRENCHSTOP™ 5 WR5 IGBT has far superior efficiency and thermal performance in high-frequency operation
compared to the competitor's best performing part. At 60 kHz switching frequency, the TRENCHSTOP™ 5 WR5
IGBT showed 23°C lower temperature on the front side of PKG, and 0.34 % higher efficiency than the
competitor's part. Compared to the equivalent CoolMOSTM P7 MOSFET, IKW40N65WR5 fared better in both
efficiency and temperature characteristics at approximately 2 kW and above. In addition, the PKG temperature
of TRENCHSTOP™ 5 WR5 IGBT at the switching frequency 60 kHz was 7°C lower than that of CoolMOSTM P7
MOSFET at the maximum power, 2.5 kW. TRENCHSTOP™ 5 WR5 IGBT also showed lower EMI levels than
CoolMOSTM P7 MOSFET, which can be an additional merit. Lastly, even though TRENCHSTOP™ 5 WR5 IGBT is not
a SC rated IGBT, it withstands SC conditions of more than 1 μsec. Therefore, this IGBT can be protected from
the SC condition if the OCP response is fast enough. An OCP circuit using a fast-responding gate drive IC,
1ED44175N is proposed, and the validation results are also presented. Through the analysis results, it has been
confirmed that TRENCHSTOP™ 5 WR5 IGBT is very suitable for PFC circuits for home-appliance applications
where the performance of anti-parallel diodes is not important.

## [стр. 21]

Application Note
21 of 23
V1.2
2022-09-21
High switching frequency CCM PFC operation with TRENCHSTOP™ 5
WR5 IGBT discretes
References
6
References
[1]
E. M. Findlay and F. Udrea, "Reverse-Conducting Insulated Gate Bipolar Transistor: A Review of Current
Technologies," in IEEE Transactions on Electron Devices, vol. 66, no. 1, pp. 219-231, Jan. 2019, doi:
10.1109/TED.2018.2882687.
[2]
PFC boost converter design guide, Infineon Technologies AG, application note, Infineon Technologies AG,
2016
InfineonApplicationNote_PFCCCMBoostConverterDesignGuide-AN-v02_00-EN.pdf
[3]
EVAL_2.5KW_CCM_4PIN, application note, Infineon Technologies AG, 2015
Infineon-ApplicationNote_EVAL_2.5KW_CCM_4PIN-ApplicationNotes-v01_00-EN.pdf

## [стр. 22]

Application Note
22 of 23
V1.2
2022-09-21
High switching frequency CCM PFC operation with TRENCHSTOP™ 5
WR5 IGBT discretes
References
Revision history

Document
version
Date of release
Description of changes
V1.0
2020-10-14
Initial version
V1.1
2020-12-09
Added complement description in Page 3
V1.2
2022-09-21
Corrected hold-up times on Page 4
Corrected the values in the tables on Page 11

## [стр. 23]

Trademarks
All referenced product or service names amany
2020-12-09














AN-2020-19 Number


Published by
Infineon Technologies AG
81726 Munich, Ger2022T 2020 Infineon
Technologies AG.
All Rights Reserved.

Do you have a question about this
document?
Email: erratum@infineon.com

Document reference
IMPORTANT NOTICE
The information contained in this application note is
given as a hint for the implementation of the product
only and shall in no event be regarded as a
description or warranty of a certain functionality,
condition or quality of the product. Before
implementation of the product, the recipient of this
application note must verify any function and other
technical information given herein in the real
application. Infineon Technologies hereby disclaims
any and all warranties and liabilities of any kind
(including without limitation warranties of noninfringement of intellectual property rights of any
third party) with respect to any and all information
given in this application note.

The data contained in this document is exclusively
intended for technically trained staff. It is the
responsibility of customer's technical departments
to evaluate the suitability of the product for the
intended application and the completeness of the
product information given in this document with
respect to such application.


For further information on the product, technology,
delivery terms and conditions and prices please
contact your nearest Infineon Technologies office
(www.infineon.com).

Please note that this product is not qualified
according to the AEC Q100 or AEC Q101 documents
of the Automotive Electronics Council.

WARNINGS
Due to technical requirements products may contain
dangerous substances. For information on the types
in question please contact your nearest Infineon
Technologies office.

Except as otherwise explicitly approved by Infineon
Technologies in a written document signed by
authorized
representatives
of
Infineon
Technologies, Infineon Technologies' products may
not be used in any applications where a failure of the
product or any consequences of the use thereof can
reasonably be expected to result in personal injury.
