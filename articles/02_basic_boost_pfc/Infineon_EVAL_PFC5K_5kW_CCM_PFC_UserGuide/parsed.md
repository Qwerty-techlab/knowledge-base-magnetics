# EVAL-PFC5KIKWWR5SYS - User Guide

> Автоматически извлечено из `source.pdf` скриптом `parse_pdf.py`
> Движок: pymupdf. Страниц: 38 из 38.
> Дата извлечения: 2026-08-07 06:42 UTC

Текст не редактировался. Формулы и таблицы могут быть искажены —
при сомнении сверяться с исходным PDF.

---

## [стр. 1]

User guide
Please read the Important notice and the Safety precautions and the Warnings

www.infineon.com
page 1 of 38
2021-12-06
UG-2021-06


The 5 kW, two-channel, interleaved CCM PFC
EVAL board
IKW40N65WR5, IDW60C65D1, and 1ED44175 in high frequency PFC
applications
About this document
Scope and purpose
This user manual provides an overview of the reference design developed for the EVAL-PFC5KIKWWR5SYS
evaluation board, its main features, key data, and mechanical dimensions.
EVAL-PFC5KIKWWR5SYS is a fast-switching, analog-controlled, two-channel, interleaved, 5 kW PFC converter
with Infineon's TRENCHSTOP™ 5 WR5 IGBT - IKW40N65WR5. It is designed to show case the use of WR5 IGBT
with high switching frequencies (up to 60 kHz) in an interleaved power factor correction (PFC) application that
enables many system benefits such as smaller size PFC choke, overall system size, and bill of material (BOM) cost.
This document also discusses an effective design example using Infineon's low-side gate driver - 1ED44175 and
rapid1 power silicon diode - IDW60C65D1.
This evaluation board has a flexible input AC voltage of 180-264 V and provides a 400 V output voltage with
maximum current of 12.5 A. Suggestions on developing interleaved PFC converters in similar power ranges,
adapted to specific requirements in major home appliances such as high-power, switched-mode power supply
(SMPS) and floor-standing air conditioners are provided in this guide.
Intended audience
This user guide is intended for all technical specialists familiar with high-speed AC/DC power stage design and
high-power interleaved PFC converters. The reference designs must be used under laboratory conditions and
only by trained specialists.
Evaluation Board
The EVAL-PFC5KIKWWR5SYS board will be used during design-in for evaluation and measurement of
characteristics and verification of data sheet specifications.
Note:
PCB and auxiliary circuits are NOT optimized for final customer design.
Note:
Boards do not necessarily meet safety, EMI, quality standard (for example UL, CE) requirements.

## [стр. 2]

User guide
2 of 38
v2.0


2021-12-06
The 5-kW, two-channel, interleaved CCM PFC EVAL board
IKW40N65WR5, IDW60C65D1, and 1ED44175 in high frequency PFC applications
Important notice

Important notice
"Evaluation Boards and Reference Boards" shall mean products embedded on a printed circuit board
(PCB) for demonstration and/or evaluation purposes, which include, without limitation, demonstration,
reference and evaluation boards, kits and design (collectively referred to as "Reference Board").

Environmental conditions have been considered in the design of the Evaluation Boards and Reference
Boards provided by Infineon Technologies. The design of the Evaluation Boards and Reference Boards
has been tested by Infineon Technologies only as described in this document. The design is not qualified
in terms of safety requirements, manufacturing and operation over the entire operating temperature
range or lifetime.

The Evaluation Boards and Reference Boards provided by Infineon Technologies are subject to functional
testing only under typical load conditions. Evaluation Boards and Reference Boards are not subject to the
same procedures as regular products regarding returned material analysis (RMA), process change
notification (PCN) and product discontinuation (PD).

Evaluation Boards and Reference Boards are not commercialized products, and are solely intended for
evaluation and testing purposes. In particular, they shall not be used for reliability testing or production.
The Evaluation Boards and Reference Boards may therefore not comply with CE or similar standards
(including but not limited to the EMC Directive 2004/EC/108 and the EMC Act) and may not fulfill other
requirements of the country in which they are operated by the customer. The customer shall ensure that
all Evaluation Boards and Reference Boards will be handled in a way which is compliant with the relevant
requirements and standards of the country in which they are operated.

The Evaluation Boards and Reference Boards as well as the information provided in this document are
addressed only to qualified and skilled technical staff, for laboratory usage, and shall be used and
managed according to the terms and conditions set forth in this document and in other related
documentation supplied with the respective Evaluation Board or Reference Board.

It is the responsibility of the customer's technical departments to evaluate the suitability of the
Evaluation Boards and Reference Boards for the intended application, and to evaluate the completeness
and correctness of the information provided in this document with respect to such application.

The customer is obliged to ensure that the use of the Evaluation Boards and Reference Boards does not
cause any harm to persons or third-party property.
The Evaluation Boards and Reference Boards and any information in this document is provided "as is"
and Infineon Technologies disclaims any warranties, express or implied, including but not limited to
warranties of non-infringement of third-party rights and implied warranties of fitness for any purpose, or
for merchantability.

Infineon Technologies shall not be responsible for any damages resulting from the use of the Evaluation
Boards and Reference Boards and/or from any information provided in this document. The customer is
obliged to defend, indemnify and hold Infineon Technologies harmless from and against any claims or
damages arising out of or resulting from any use thereof.

Infineon Technologies reserves the right to modify this document and/or any information provided
herein at any time without further notice.

## [стр. 3]

User guide
3 of 38
v2.0


2021-12-06
The 5-kW, two-channel, interleaved CCM PFC EVAL board
IKW40N65WR5, IDW60C65D1, and 1ED44175 in high frequency PFC applications
Safety precautions

Safety precautions
Note:
Please note the following warnings regarding the hazards associated with development systems.
Table 1
Safety precautions

Warning: The DC link potential of this board is up to 400 V DC. When measuring
voltage waveforms by oscilloscope, high voltage differential probes must be used.
Failure to do so may result in personal injury or death.

Warning: The evaluation board contains DC bus capacitors which take time to
discharge after removal of the main supply. Before working on the drive system, wait
five minutes for capacitors to discharge to safe voltage levels. Failure to do so may
result in personal injury or death.

Warning: The evaluation board is connected to the grid input during testing. Hence,
high-voltage differential probes must be used when measuring voltage waveforms by
oscilloscope. Failure to do so may result in personal injury or death.
Caution: The heat sink and device surfaces of the evaluation or reference board may
become hot during testing. Hence, necessary precautions are required while handling
the board. Failure to comply may cause injury.
Caution: Only personnel familiar with the drive, power electronics and associated
machinery should plan, install, commission and subsequently service the system.
Failure to comply may result in personal injury and/or equipment damage.

Caution: The evaluation board contains parts and assemblies sensitive to
electrostatic discharge (ESD). Electrostatic control precautions are required when
installing, testing, servicing or repairing the assembly. Component damage may result
if ESD control procedures are not followed. If you are not familiar with electrostatic
control procedures, refer to the applicable ESD protection handbooks and guidelines.
Caution: A drive that is incorrectly applied or installed can lead to component damage
or reduction in product lifetime. Wiring or application errors such as undersizing the
motor, supplying an incorrect or inadequate AC supply, or excessive ambient
temperatures may result in system malfunction.

Caution: The evaluation or reference board is shipped with packing materials that
need to be removed prior to installation. Failure to remove all packing materials that
are unnecessary for system installation may result in overheating or abnormal
operating conditions.

## [стр. 4]

User guide
4 of 38
v2.0


2021-12-06
The 5-kW, two-channel, interleaved CCM PFC EVAL board
IKW40N65WR5, IDW60C65D1, and 1ED44175 in high frequency PFC applications
Table of contents

Table of contents
About this document ....................................................................................................................... 1
Important notice ............................................................................................................................ 2
Safety precautions .......................................................................................................................... 3
Table of contents ............................................................................................................................ 4
1
The board at a glance .............................................................................................................. 5
1.1
Interleaved PFC ....................................................................................................................................... 5
1.2
Block diagram of the EVAL-PFC5KIKWWR5SYS ...................................................................................... 6
2
System and functional description ........................................................................................... 8
2.1
General overview ..................................................................................................................................... 8
2.1.1
UCC28070 - Analogy controller ........................................................................................................ 9
2.1.2
IKW40N65WR5 - Fast-switching WR5 IGBT ...................................................................................... 9
2.1.3
IDW60C65D1 - Rapid1 power silicon diode ..................................................................................... 9
2.1.4
1ED44175 - Low-side gate driver ................................................................................................... 10
2.2
Board specifications .............................................................................................................................. 10
3
System design....................................................................................................................... 11
3.1
Schematics ............................................................................................................................................ 11
3.2
Layout .................................................................................................................................................... 15
3.3
Bill of material ....................................................................................................................................... 18
3.4
Connector details .................................................................................................................................. 21
4
System performance ............................................................................................................. 22
4.1
Efficiency and PFC measurements ....................................................................................................... 22
4.2
Start-up behavior .................................................................................................................................. 23
4.3
Input current and inductor current cancellation ................................................................................. 24
4.4
Switching performance of the IGBT at steady state ............................................................................ 27
4.5
Output ripple voltage ............................................................................................................................ 28
4.6
Input voltage and input current ............................................................................................................ 30
4.7
Load step tests ...................................................................................................................................... 31
4.8
Thermal measurements ........................................................................................................................ 33
5
Conclusion ........................................................................................................................... 35
6
References and appendices .................................................................................................... 36
6.1
Abbreviations and definitions ............................................................................................................... 36
6.2
References ............................................................................................................................................. 36
6.3
Additional information .......................................................................................................................... 36
Revision history ............................................................................................................................. 37

## [стр. 5]

User guide
5 of 38
v2.0


2021-12-06
The 5-kW, two-channel, interleaved CCM PFC EVAL board
IKW40N65WR5, IDW60C65D1, and 1ED44175 in high frequency PFC applications

The board at a glance
1
The board at a glance
This section of the guide describes the basic concepts of an interleaved PFC and provides a brief introduction on
the design of the EVAL-PFC5KIKWWR5SYS board.
1.1
Interleaved PFC
The standard boost converter is the most popular topology for power factor correction due to its simple control
of the input current while keeping the output voltage constant. For medium power levels, to increase the output
power and improve overall efficiency, several converters must be used in a parallel connection; for e.g. two
channels or three channels connected in parallel. If the switches operate with a two-channel connection 180° out
of phase or a three-channel connection 120° out of phase, the interleaved operation will share the same load
capacitors and reduce the input current ripple significantly.  This also eases the burden of filtering conducted
electro-magnetic interference (EMI) noise and helps reduce the EMI filter and input capacitor sizes.
The interleaved PFC topology has several benefits, such as ease of implementation, the use of smaller (but more)
components, and better heat distribution. On the other hand, the output capacitor current ripple is decreased
and evenly distributed in each channel. This can extend the life of the capacitors and reduce its size and cost.
Unlike single-boost converters, the inductors in an interleaved PFC handle only half or one-third of the current.
Inductors with low inductance values can reach the same high power as single-boost converters and lower
inductance also means smaller inductors and higher power density for a given power rating.
Figure 1 shows an example of a two-channel interleaved PFC. Its detailed operation principles and key
waveforms are shown in Figure 2.

Iin
IL2
IL1
ID2
ID1
Ic
IQ2
IQ1
Iout
Figure 1
Block diagram of a two-channel interleaved PFC

## [стр. 6]

User guide
6 of 38
v2.0


2021-12-06
The 5-kW, two-channel, interleaved CCM PFC EVAL board
IKW40N65WR5, IDW60C65D1, and 1ED44175 in high frequency PFC applications

The board at a glance


Figure 2
Principles of operation of a two-channel interleaved PFC
1.2
Block diagram of EVAL-PFC5KIKWWR5SYS
Reducing the size of power converters by increasing their switching frequency and reducing the size of  their
magnetic component is a goal that has been pursued for decades. This is especially true when using IGBTs in a
switching mode power supply. Higher switching frequency means smaller size and lower cost. A high
performance IGBT is a key component in helping customers gain a bigger market share. Infineon's WR5 IGBT is
specifically optimized for full-rated, hard-switching applications with an excellent price to performance ratio. Its
use is recommended in the AC-DC PFC stage of cost-sensitive applications. The EVAL-PFC5KIKWWR5SYS
evaluation board is used for demonstrating the switching performance of the TRENCHSTOP™ 5 WR5 IGBT
IKW40N65WR5 with high switching frequencies (up to 60 kHz) in an interleaved PFC application.
Figure 3 shows the block diagram of EVAL-PFC5KIKWWR5SYS.
This reference design includes:
• Two-channel boost converters
• A high-speed, 650 V, 40 A, reverse conducting TRENCHSTOP™ 5 WR5 IGBT in TO-247 package
• Gate driver ICs for WR5 IGBTs
• Rapid1 power silicon diode for boost rectification
• Loss-free current monitoring for switching current
• 15 V auxiliary power supply
• Connectors for easy set up
• External force cooling for high-power applications

## [стр. 7]

User guide
7 of 38
v2.0


2021-12-06
The 5-kW, two-channel, interleaved CCM PFC EVAL board
IKW40N65WR5, IDW60C65D1, and 1ED44175 in high frequency PFC applications

The board at a glance

IL2
IL1
ID2
ID1
Ic
IQ2
IQ1
Iout
CT1
CT2
UCC28070 interleaved CCM PFC controller
GDA
GDB
CSA
CSB
1ED44175
1ED44175
IKW40N65WR5
IKW40N65WR5
IDW60C65D1
Figure 3
Block diagram of EVAL-PFC5KIKWWR5SYS

## [стр. 8]

User guide
8 of 38
v2.0


2021-12-06
The 5-kW, two-channel, interleaved CCM PFC EVAL board
IKW40N65WR5, IDW60C65D1, and 1ED44175 in high frequency PFC applications

System and functional description
2
System and functional description
2.1
General overview
EVAL-PFC5KIKWWR5SYS is the reference design for a 5 kW interleaved PFC for, but not limited to, floor-standing
air conditioners in major home appliances.


Figure 4
Board view of EVAL-PFC5KIKWWR5SYS
Design characteristics of the EVAL-PFC5KIKWWR5SYS evaluation board include:
Board performance
• High power factor, PF > 0.995
• Low THDi
•  High efficiency
Control technology
• Continuous conduction mode (CCM) average current control
• Frequency-dithering for enhanced EMI reduction
Fault protection
• Input undervoltage protection and overvoltage protection
• Output overvoltage protection
• Open-circuit protection for AC input and DC output
• Cycle-by-cycle peak current limiting
• Thermal shutdown for power semiconductors

## [стр. 9]

User guide
9 of 38
v2.0


2021-12-06
The 5-kW, two-channel, interleaved CCM PFC EVAL board
IKW40N65WR5, IDW60C65D1, and 1ED44175 in high frequency PFC applications

System and functional description
2.1.1
UCC28070 - Analogy controller
Infineon does not have a dedicated interleaved PFC controller. Therefore, the UCC28070 from Texas Instruments
(popular choice in this field) was chosen as the analogy controller. Figure 5 shows a simplified application
diagram of the UCC28070.

Figure 5
Simplified application diagram of the UCC28070
2.1.2
IKW40N65WR5 - Fast-switching WR5 IGBT
The IKW40N65WR5 is a high-speed, 650 V, 40 A, reverse-conducting TRENCHSTOP™ 5 WR5 IGBT in a TO-247
package. It is optimized for hard-switching applications with the best price to performance ratio and is a good fit
with mainstream designs in which FSW  > 20 kHz. The key characteristics of the IKW40N65WR5 are:
• A very low VCEsat of 1.35 V at 25°C
• Low Etot
• Soft recovery and low Qrr for the diode
• Good R(G)off controllability
• Low T j and T c for lower heat sink and cooling costs
2.1.3
IDW60C65D1 - Rapid1 power silicon diode
The IDW60C65D1 is a 650 V, 60 A, rapid1 emitter-controlled power silicon diode in the common cathode
configuration in a TO-247 package. It enables design optimization for a more compact dimension, easier
assembly, and consequently lower costs. Its features include:
• Highest softness factor for ultimate softness and low EMI filtering
• A temperature-stable forward voltage (VF) of 1.35 V

## [стр. 10]

User guide
10 of 38
v2.0


2021-12-06
The 5-kW, two-channel, interleaved CCM PFC EVAL board
IKW40N65WR5, IDW60C65D1, and 1ED44175 in high frequency PFC applications

System and functional description
• Lowest Irrm for lowest turn-on losses on the boost switch
2.1.4
1ED44175 - Low-side gate driver
The 1ED44175 is an EiceDRIVER™ 25 V single-channel, low-side, non-inverting gate driver with typical 2.6 A
source and sink currents in a tiny 6-lead PG-SOT23 package. The 1ED44175N01B provides cost and space
savings by integrating the comparator. It utilizes Infineon's proprietary latch-immune complementary metaloxide-semiconductor transistor (CMOS) technology to enable a rugged, monolithic construction while
achieving best-in-class fault reporting accuracy with an overcurrent protection (OCP) threshold tolerance of +/-
5%.
Its features include:
• -0.246 V overcurrent threshold with a tolerance accuracy of ± 5%
• Overcurrent detection with negative voltage input
• Single pin for fault output and enable
• Programmable fault-clear time
• Undervoltage lockout for IGBTs
• CMOS Schmitt-triggered inputs
• Compatible with 3.3 V, 5 V, and 15 V input logic
• Output in phase with input
• OCP pin with - 10 Vdc negative input capability
• 3 kV electronic static discharge (ESD)
2.2
Board specifications
Table 2 lists the key specifications of the reference design used in EVAL-PFC5KIKWWR5SYS.
Table 2
Specifications of EVAL-PFC5KIKWWR5SYS
NO.
Parameters
Symbol
Value
1
Output power
Pout
5000 watts
2
Input voltage range (rms)
Vin
180 Vac to 264 Vac
3
Input frequency range
f
50 Hz or  60 Hz
4
Output voltage
VDC
400 V
5
Output ripple voltage
Vripple
20 V
6
Inductance
L1, L2
53 µH
7
Switching frequency
Fs
60 kHz

## [стр. 11]

User guide
11 of 38
v2.0


2021-12-06
The 5-kW, two-channel, interleaved CCM PFC EVAL board
IKW40N65WR5, IDW60C65D1, and 1ED44175 in high frequency PFC applications

System design
3
System design
This chapter discusses all the necessary technical data such as schematics, layout, and components that are
essential to meet individual customer requirements and to make the EVAL-PFC5KIKWWR5SYS evaluation board
a basis for development or modification.
EVAL-PFC5KIKWWR5SYS consists of three blocks - power stage, controller circuit, and auxiliary supply - all of
which are on the same board. All surface mounted devices are mounted on the bottom layer, enabling customers
to modify parameters if necessary.
3.1
Schematics
There are a total of six schematic diagrams in the design of EVAL-PFC5KIKWWR5SYS. The images in this section
describe the functions of each individual schematic.
Figure 6 shows the converter's EMI filter, soft-start control, and diode rectifiers. Connectors X1, X3, and X6
connect to the grid line, neutral, and ground respectively. Three metal oxide varistors (MOV) R58, R60, and R61
and a gas discharge tube GT1 consist of a surge protection circuit. The positive temperature coefficient (PTC)
resistors R54 and R55 limit the input current ramp slope at start-up. Once the voltage of output capacitors
reaches about 230 V, the K1 relay turns on and bypasses R54 and R55. At this point, the PFC converter works with
a very high efficiency.


Figure 6
EMI filter, soft start control, and rectifiers of EVAL-PFC5KIKWWR5SYS
Figure 7 shows two-channel boost converters connect in parallel with a 180° out-of-phase control. Each channel
has a WR5 IGBT (IKW40N65WR5) as the main switch and a rapid1 fast-recovery diode (IDW60C65D1) with a
common cathode as the boost diodes for both channels. In practical applications, customers can select two
separated silicon fast-recovery diodes or two SiC diodes to replace this common cathode diode, and use them
as D21 and D22. A current transformer monitors the IGBT current for normal operation and limits the cycle-by-

## [стр. 12]

User guide
12 of 38
v2.0


2021-12-06
The 5-kW, two-channel, interleaved CCM PFC EVAL board
IKW40N65WR5, IDW60C65D1, and 1ED44175 in high frequency PFC applications

System design
cycle current. Each gate driver (1ED44715) matches one IGBT. Two boost inductors that come from the magnetic
device supplier POCO perform better than inductors with traditional powder materials.


Figure 7
Interleaved PFC power stage of EVAL-PFC5KIKWWR5SYS
Figure 8 shows the UCC28070 analog control and its parameter settings with external resistors and capacitors.
The potentiometer (R115) sets the converter's switching frequency and customers can adjust this switching
frequency easily.

## [стр. 13]

User guide
13 of 38
v2.0


2021-12-06
The 5-kW, two-channel, interleaved CCM PFC EVAL board
IKW40N65WR5, IDW60C65D1, and 1ED44175 in high frequency PFC applications

System design


Figure 8
UCC28070 parameter settings for EVAL-PFC5KIKWWR5SYS
Great care has been taken to select the proper value for the RC filters applied to VSENSE and VINAC to prevent the
destabilizing effects of excess noise on these inputs in a noisy environment. If applied, the RC time constant of
these two pins should not exceed 100 μs. More information about how to control the UCC28070 with external
components can be found in [1].
Figure 9 shows fault protection in EVAL-PFC5KIKWWR5SYS. Thermal shutdown of the power semiconductors is
implemented by an external comparator. If the cooling fans fixed on the mechanical box fail or do not work, the
resistance of the negative temperature coefficient (NTC) fixed on the heat sink decreases dramatically and the
SS pin of the UCC28070 is pulled down to the ground, in which case both gate signals are disabled.

## [стр. 14]

User guide
14 of 38
v2.0


2021-12-06
The 5-kW, two-channel, interleaved CCM PFC EVAL board
IKW40N65WR5, IDW60C65D1, and 1ED44175 in high frequency PFC applications

System design


Figure 9
Fault protection in EVAL-PFC5KIKWWR5SYS
The UCC28070 already has an integrated output overvoltage protection through the continuous monitoring of
VVSENSE, therefore, the input overvoltage and undervoltage protection in this converter are implemented by an
external comparator, both of which are connected to the SS pin of the UCC28070.


Figure 10
Auxiliary supply schematic of EVAL-PFC5KIKWWR5SYS

## [стр. 15]

User guide
15 of 38
v2.0


2021-12-06
The 5-kW, two-channel, interleaved CCM PFC EVAL board
IKW40N65WR5, IDW60C65D1, and 1ED44175 in high frequency PFC applications

System design
Figure 10 shows the auxiliary supply schematic of the evaluation board that supplies voltage to the controller
circuit, gate drivers, and cooling fans. The ICE5QSAG [2] is a quasi-resonance mode controller for the softswitching operation of Q5. It increases the system efficiency. In a simplified design of the flyback transformer
(TX1 in Figure 10), there is only one secondary winding with an output voltage of 15 V - an optimized voltage for
driving IGBTs.
The maximum recommended voltage for cooling fans is 13.8 V. Therefore, as shown in Figure 11, two low
dropout regulator chips (IFX1963) provide about 13.6 V voltage to the fans directly, without regulating the fan
speed.

Figure 11 Low-dropout regulator for cooling fans in EVAL-PFC5KIKWWR5SYS
3.2
Layout
The layout of EVAL-PFC5KIKWWR5SYS can help customers understand the placements of components and the
routing of wires for the whole board. In the default layout, the PCB has four electrical layers with 70 µm of copper
and a dimension of 244 mm × 142 mm. The PCB board's thickness is 2 mm. Please visit Infineon's website
(https://www.infineon.com/cms/en/product/evaluation-boards/eval-pfc5kikwwr5sys/)
to
obtain
detailed
information and the latest Gerber files.

## [стр. 16]

User guide
16 of 38
v2.0


2021-12-06
The 5-kW, two-channel, interleaved CCM PFC EVAL board
IKW40N65WR5, IDW60C65D1, and 1ED44175 in high frequency PFC applications

System design


Figure 12
 Top layer routing of EVAL-PFC5KIKWWR5SYS
Figure 12 shows the top layer routing of the evaluation board.


Figure 13
Mid layer 1 routing of EVAL-PFC5KIKWWR5SYS
Figure 13 shows the mid layer 1 routing of the evaluation board.

## [стр. 17]

User guide
17 of 38
v2.0


2021-12-06
The 5-kW, two-channel, interleaved CCM PFC EVAL board
IKW40N65WR5, IDW60C65D1, and 1ED44175 in high frequency PFC applications

System design


Figure 14
Mid layer 2 routing of EVAL-PFC5KIKWWR5SYS
Figure 14 shows the mid layer 2 routing of the evaluation board.


Figure 15
Bottom layer routing of EVAL-PFC5KIKWWR5SYS
Figure 15 shows the bottom layer routing of the evaluation board.

## [стр. 18]

User guide
18 of 38
v2.0


2021-12-06
The 5-kW, two-channel, interleaved CCM PFC EVAL board
IKW40N65WR5, IDW60C65D1, and 1ED44175 in high frequency PFC applications

System design
3.3
Bill of material
The complete bill of material for EVAL-PFC5KIKWWR5SYS can be downloaded (a customer login is required)
from the Download section on the homepage of Infineon's website
(https://www.infineon.com/cms/en/product/evaluation-boards/eval-pfc5kikwwr5sys/).
Table 3
BOM for EVAL-PFC5KIKWWR5SYS
Quantity
Ref.
Designator
Value
Description
Manufacturer
Manufacturer P/N
15
C1, C5, C6, C8,
C13, C28, C30,
C33, C35, C39,
C46, C48, C58,
C59, C73
100nF
Chip monolithic ceramic capacitor
MuRata
GRM188R71E104KA01,
2
C2, C18
180nF
Chip monolithic ceramic capacitor
MuRata
GCM188R71E184JA55
6
C3, C9, C27,
C76, C89, C90
1nF
Chip monolithic ceramic capacitor
MuRata
GRM188R71E102KA01,
4
C4, C34, C36,
C37
2.2uF
Chip monolithic ceramic capacitor
MuRata
GRM188R61E225KA12
18
C7, C29, C31,
C56, C57, C61,
C62, C63, C66,
C67, C70, C71,
C72, C82, C83,
C84, C86, C88
10uF
Commercial grade multilayer
ceramic chip capacitor
TDK Corporation
C3216X7R1E106K160AB
2
C10, C81
100pF
Multilayer ceramic chip capacitor,
C-series, commercial grade,
general
TDK Corporation
C1608X7R1H101M
1
C11
22nF
Chip monolithic ceramic capacitor
Kemet
C0603C223K5RACTU
2
C21, C23
2.2nF
Chip monolithic ceramic capacitor
MuRata
GRM188R71E222KA01
1
C12
51nF
Chip monolithic ceramic capacitor
MuRata
GCM188R71E473KA37
4
C14, C32, C38,
C68
1uF
Chip monolithic ceramic capacitor
MuRata
GRM188R71E105KA12
1
C15
470nF
Chip monolithic ceramic capacitor
MuRata
GRM188R71C474KA88
2
C16, C91
330pF
Chip monolithic ceramic capacitor
MuRata
GRM216R71H331KA01
3
C17, C53, C54
330pF
Chip monolithic ceramic capacitor
MuRata
GRM188R71H331KA01
4
C19, C20, C25,
C26
470pF
Chip monolithic ceramic capacitor
MuRata
GRM188R71H471KA01
2
C22, C24
560pF
Chip monolithic ceramic capacitor
MuRata
GRM1885C1E561JA01
2
C40, C41
1uF
Metallized polypropylene film
capacitor
TDK Corporation
B32923C3105M000
1
C42
1uF
Metallized polypropylene film
capacitor
Epcos
B32522N6105K000
1
C43
NC
Metallized polypropylene film
capacitor
Epcos
B32522N6105K000
5
C44, C45, C47,
C55, C80
2.2nF
AC-line rated ceramic disc
capacitor class X1, 760 VAC/class
Y1, 500 VAC
Vishay
440LD22-R
4
C49, C50, C51,
C52
680uF
CAP/ELCO/680 uF/450 V/20% / - /
-40℃ to 105℃ /  10.00 mm pitch X
35.00 mm dia X 62.00 mm H body /
- / -
Aishi
ELP2WM681R60KT
1
C60
68uF
Miniature aluminum electrolytic
capacitor
Aishi
EHL2WM680W50OT
4
C64, C65, C85,
C87
470uF
Aluminum electrolytic capacitor/FC
series
Aishi
SPD1CM102G12O00RA
XXX
1
C69
220uF
Miniature aluminum electrolytic
capacitor
Aishi
EML1EM221F09OT

## [стр. 19]

User guide
19 of 38
v2.0


2021-12-06
The 5-kW, two-channel, interleaved CCM PFC EVAL board
IKW40N65WR5, IDW60C65D1, and 1ED44175 in high frequency PFC applications

System design
Quantity
Ref.
Designator
Value
Description
Manufacturer
Manufacturer P/N
1
C74
12pF
Chip monolithic ceramic capacitor
MuRata
GRM31A5C2H120JW01
1
C75
1nF
Chip monolithic ceramic capacitor
MuRata
GRM319R71H102JA01
1
C77
220pF
Chip monolithic ceramic capacitor
MuRata
GRM188R71H221KA01
1
C78
NC
Multilayer ceramic chip capacitor,
C-series, commercial grade,
general
TDK Corporation
C1608X7R1H101M
1
C79
33nF
Chip monolithic ceramic capacitor
MuRata
GRM188R71E333JA01
2
CT1, CT2
750344822-00
Transformer, 10.50 mH, turn ratio
400:1
Würth Elektronik
750344822-00
13
D1, D2, D3, D4,
D5, D13, D14,
D23, D24, D25,
D26, D28, D29
BAS16J
Silicon switching diode
Nexperia
BAS16J
6
D6, D7, D8, D9,
D11, D12
BAT54-03W
Silicon Schottky diode
Infineon
Technologies
BAT54-03W
1
D10
NC
Silicon Schottky diode
Infineon
Technologies
BAT54-03W
3
D15, D16, D30
1N4007E-E3/54
General purpose plastic rectifier
Vishay
1N4007E-E3/54
2
D17, D18
GBJ2508-F
Glass passivated bridge rectifier
600V
Micro Commercial
Components
GBJ2508-F
1
D19
IDW60C65D1
650 V rapid 1  diode,  IF
30/60A,TO247-3
Infineon
Technologies
IDW60C65D1
1
D20
STTH10LCD06FP
Turbo2 ultrafast high voltage
rectifier for flat-panel displays
STMicroelectronics
STTH10LCD06FP
2
D21, D22
NC
650 V rapid1 diode, 30 A, TO247-3
Infineon
Technologies
IDW30E65D1
1
D27
BAV99
High-speed switching diode
Nexperia
BAV99
1
D31
MBRS1100T3G
Schottky power rectifier
ON Semiconductor
MBRS1100T3G
2
D32, D34
BAT165
Medium power AF Schottky diode
Infineon
Technologies
BAT165
1
D33
STPS4S200S
Surface mount Schottky barrier
rectifier
STMicroelectronics
STPS4S200S
2
F1, F2
12.8mR
Fast-acting fuse cartridge, 20 A/250
V
Conquer
ABE 020
1
GT1
2049-60-BLF
RES/STD/ - / - / 30% / - / -30℃ to
85℃/12.80 mm pitch, 6.00 mm L X
8.00 mm W, 8.3 mm H body / - / -
Bourns
2049-60-BLF
1
HS1
Heatsink
L115mm*W30mm*
H50mm
Heat sink L115 mm * W30 mm *
H50 mm
-
Heatsink
L115mm*W30mm*H50m
m
1
HS2
Heatsink
L137mm*W35mm*
H60mm
Heat sink L137 mm * W35 mm *
H60 mm
-
Heatsink
L137mm*W35mm*H60m
m
1
HS3
Heatsink HS15-11
Heat sink L15 * W11
-
Heatsink HS15-11
1
K1
HF161F-W/18-HT
Solar relay, applicable to inverter
used for photovoltaic power
generation systems
HongFa
HF161F-W/18-HT
1
L1
1.5mH
Common mode power line choke
Würth Elektronik
7448063801
2
L2, L3
85uH
IND/STD/85 µH / - / 10% / - /16
mR/THT/Inductor, THT, 4-pin,
54.00 mm L X 32.00 mm W X 56.00
mm H body / THT / -
POCO
PI200273V1
1
L4
10uH
IND/STD/10uH/4A/20%/-40℃ to
150℃ / 33 mR/SMD/Inductor, SMD,
6.90 mm L X 6.90 mm W X 5.00
mm H body/SMD/ -
Würth Elektronik
744314101
2
L5, L6
220R
Chip ferrite bead
Würth Elektronik
742792031
1
NTC1
AYN-MF56-503F3950FB-28#-100
Header, 2-pin

AYN-MF56-503F3950FB-28#-100
2
P1, P2
66100211622
Connector header VERT 2POS
2.54 MM
Würth Elektronik
66100211622

## [стр. 20]

User guide
20 of 38
v2.0


2021-12-06
The 5-kW, two-channel, interleaved CCM PFC EVAL board
IKW40N65WR5, IDW60C65D1, and 1ED44175 in high frequency PFC applications

System design
Quantity
Ref.
Designator
Value
Description
Manufacturer
Manufacturer P/N
1
Q1
IRLML6402TRPBF HEXFET P-channel power
MOSFET, 20 V, 3.7 A
Infineon
Technologies
IRLML6402TRPB
2
Q2, Q3
IKW40N65WR5
High-speed fast IGBT in
TRENCHSTOPTM 5 technology,
VCE 650V, IC 40A
Infineon
Technologies
IKW40N65WR5
1
Q5
IPP90R340C3
900V CoolMOS C3 power
transistor, RDS(on) 340 mΩ
Infineon
Technologies
IPP90R340C3
3
R1, R15, R81
4.7k
General purpose chip resistor
Yageo
RC0603FR-074K7L
4
R2, R14, R108,
R109
0R
0R/75V
Panasonic
ERJ3GEY0R00V
1
R3
NC
Standard thick film chip resistor
Vishay
CRCW0603115KFK,
1
R11
NC
Standard thick film chip resistor
Vishay
CRCW060310K0FK
1
R97
NC
Standard thick film chip resistor
Vishay
CRCW06031K20FK
2
R4, R27
1.82k
Standard thick film chip resistor
Vishay
CRCW06031K82FK
1
R5
180K
Standard thick film chip resistor
Vishay
CRCW0603180KFK
2
R6, R50
82k
Standard thick film chip resistor
Vishay
CRCW060382K0FK
2
R7, R19
22.6k
Standard thick film chip resistor
Vishay
CRCW060322K6FK
3
R8, R66, R67
1k
Standard thick film chip resistor
Vishay
CRCW12061K00FK
1
R9
1.5k
Standard thick film chip resistor
Vishay
CRCW06031K50FK
8
R10, R32, R33,
R35, R38, R45,
R48, R100
10k
Standard thick film chip resistor
Vishay
CRCW060310K0FK
1
R12
118k
Standard thick film chip resistor
Vishay
CRCW0603118KFK
1
R13
1k
1 k/200 V/1%
TT Electronics
ASC1206-1K0FT5
1
R16
124k
Standard thick film chip resistor
Vishay
CRCW0603124KFK
1
R17
33k
Standard thick film chip resistor
Vishay
CRCW060333K0FK
1
R18
84.5k
Standard thick film chip resistor
Vishay
CRCW060384K5FK
4
R20, R21, R22,
R23
62R
Standard thick film chip resistor
Vishay
CRCW121062R0FK
1
R24
3.65k
Standard thick film chip resistor
Vishay
CRCW06033K65FK
2
R25, R26
5.62k
Standard thick film chip resistor
Vishay
CRCW06035K62FK
1
R28
5.49k
Standard thick film chip resistor
Vishay
CRCW06035K49FK
1
R29
200k
Standard thick film chip resistor
Vishay
CRCW0603200KFK
3
R30, R43, R51
100k
General purpose chip resistor
Yageo
RC0603FR-07100KL
18
R31, R34, R36,
R37, R41, R42,
R56, R57, R59,
R63, R64, R65,
R73, R74, R75,
R78, R79, R80
1MEG
Standard thick film chip resistor
Vishay
CRCW12061M00FK
1
R39
10k
General purpose chip resistor
Yageo
RC1206FR-0710KL
2
R40, R44
1k
Standard thick film chip resistor
Vishay
CRCW06031K00FK
1
R46
5.1k
Standard thick film chip resistor
Vishay
CRCW06035K10FK
1
R47
1MEG
Standard thick film chip resistor
Vishay
CRCW06031M00FK
2
R49, R99
47k
Standard thick film chip resistor
Vishay
CRCW060347K0FK
2
R52, R53
16k
Standard thick film chip resistor
Vishay
CRCW060316K0FK
2
R54, R55
10R
NTC thermistor for inrush current
limiting
Epcos
B57237S0100M000
3
R58, R60, R61
275V
Multi-pulse handling SIOV metal
oxide varistor
Epcos
B72220S0271K101
3
R62, R76, R77
4.7k
Standard thick film chip resistor
Vishay
CRCW08054K70FK
1
R68
33k
33 k/50 V/1%
ROHM
Semiconductors
MCR03ERTF3302
1
R69
470k
Standard thick film chip resistor
Vishay
CRCW0603470KFK
1
R70
220R
Standard thick film chip resistor
Vishay
CRCW0805220RFK
2
R71, R72
5.1R
Standard thick film chip resistor
Vishay
CRCW12065R10FK
1
R82
4.7k
Standard thick film chip resistor
Vishay
CRCW12064K70FK
2
R83, R84
30k
Standard thick film chip resistor
Vishay
CRCW060330K0FK

## [стр. 21]

User guide
21 of 38
v2.0


2021-12-06
The 5-kW, two-channel, interleaved CCM PFC EVAL board
IKW40N65WR5, IDW60C65D1, and 1ED44175 in high frequency PFC applications

System design
Quantity
Ref.
Designator
Value
Description
Manufacturer
Manufacturer P/N
2
R85, R86
680R
Standard thick film chip resistor
Vishay
CRCW0603680RFK
2
R87, R105
3k
3 k/50 V/1%
ROHM
Semiconductors
MCR03EZPFX3001
3
R88, R91, R93
3.3MEG
Standard thick film chip resistor
Vishay
CRCW12063M30FK
3
R89, R92, R94
10MEG
Standard thick film chip resistor
Vishay
CRCW120610M0FK
1
R90
24k
Standard thick film chip resistor
Vishay
CRCW060324K0FK
1
R95
6.8k
General purpose chip resistor
Yageo
RC0805FR-076K8L
1
R96
20R
Standard thick film chip resistor
Vishay
CRCW120620R0FK
2
R98, R104
2.49k
Standard thick film chip resistor
Vishay
CRCW06032K49FK
1
R101
0R
Standard thick film chip resistor
Vishay
CRCW06030000Z0
2
R102, R103
1.2R
Standard thick film chip resistor
Vishay
CRCW12061R20FK
2
R106, R107
3R
3R/0.5 W/1%
Panasonic
ERJ8BQF3R0V
1
R114
0R
Standard thick film chip resistor
Vishay
CRCW08050000Z0
1
R115
250k
RES/VAR/250 k/250 mW/20%/ 100
ppm/K/-55℃ to 125℃/ 3-pin, 5.00
mm L X 4.50 mm W X 2.85 mm H
Body/SMD
/ -
Bourns
3314G-1-254E
1
TX1
750344821-00
Transformer 10-terminal EXT, THT,
horizontal, EE style bobbins, EE20
Würth Elektronik
Midcom
750344821-00
1
U1
UCC28070DW
PFC controller
Texas Instruments
UCC28070DW
2
U2, U8
TL431CDBZR
Precision programmable reference
Texas Instruments
TL431CDBZR
2
U3, U4
1ED44175N01B
Gate drivers, low-side drivers
Infineon
Technologies
1ED44175N01B
2
U5, U9
IFX1963TEV
1.5 A low-dropout linear voltage
regulator
Infineon
Technologies
IFX1963TEV
1
U6
ICE5QSAG
Quasi-resonant PWM controller
Infineon
Technologies
ICE5QSAG
1
U7
SFH617A-3
Optocoupler, phototransistor
output, high reliability, 5300 VRMS,
110 Â°C rated
Vishay
SFH617A-3
2
U11, U12
LM2903D
Dual differential comparators
Texas Instruments
LM2903D
5
X1, X3, X6, X7,
X9
7460307
WP-BUTR Redcube Press Fit with
internal thread and two-rows pin
plate
Würth Elektronik
7460307
2
X2, X8
691311500102
Terminal block, 2-pins, 5.08 mm
pitch, board to cable
Würth Elektronik
691311500102
4
X4, X5
3513
Through hole 3AG snap-in fuse clip
Conquer
CQ-205S
2
FAN1, FAN2
AFB0612EHABF00
Cooling fans
Delta
AFB0612EH-ABF00


3.4
Connector details
Table 4
Connectors
PIN
Label
Function
X1
Grid Line
AC input of PFC, connect to grid line
X3
Grid Neutral
AC input of PFC, connect to grid neutral
X6
Earth
Protective earth
X7
PFC DC output
Connect to load positive
X9
PFC Ground
Connect to load negative
X2
Auto Test
For AC input auto test
X8
Auto Test
For PFC output auto test

## [стр. 22]

User guide
22 of 38
v2.0


2021-12-06
The 5-kW, two-channel, interleaved CCM PFC EVAL board
IKW40N65WR5, IDW60C65D1, and 1ED44175 in high frequency PFC applications

System performance
4
System performance
4.1
Efficiency and PFC measurements
All test conditions are based on a 25°C ambient temperature. For the efficiency test, it is important to monitor
the voltage directly on the input connector X2 and output connector X8.
All efficiency and PF were carried out using the WT33E Yokogawa power meter.
Figure 16 shows the overall efficiency of EVAL-PFC5KIKWWR5SYS, including the aux supply for cooling fans at
different input voltages from 180 VAC to 264 VAC. The efficiency curves show that the WR5 IGBT enables customers
to increase the PFC switching frequencies (up to 60 kHz) while maintaining high efficiency.

Figure 16
Efficiency of EVAL-PFC5KIKWWR5SYS
Figure 17 shows the power factor curve at different loads and different AC input voltages. The power factor is
higher than 0.96 for light loads and an almost unity power factor (higher than 0.99) is achieved for loads above
30% of the rated power.
92,500%
93,500%
94,500%
95,500%
96,500%
97,500%
98,500%
500
1000
1500
2000
2500
3000
3500
4000
4500
5000
Efficiency %
Output power (watt)
Efficiency
180VAC
230VAC
264VAC

## [стр. 23]

User guide
23 of 38
v2.0


2021-12-06
The 5-kW, two-channel, interleaved CCM PFC EVAL board
IKW40N65WR5, IDW60C65D1, and 1ED44175 in high frequency PFC applications

System performance
Figure 17
Power factor of EVAL-PFC5KIKWWR5SYS
4.2
Start-up behavior
After EVAL-PFC5KIKWWR5SYS is connected to a grid, the auxiliary power supply to the devices starts. During the
output capacitor's pre-charging phase both channels are bypassed by D20 - an ultrafast high-voltage rectifier
- and the inrush current is limited by two NTC resistors. When the output voltage reaches about 230 VDC, the K1
relay turns on and the two NTC resistors are shorted, thus ensuring that the convertor works with high efficiency.
The board is designed to start in both "no load" and "full load" conditions. Figure 18 and Figure 19 show the
converter's full load start-up waveforms at VIN = 180 VAC and VIN = 264 VAC respectively.


Vout = Blue, VGE = Yellow, IL1 = Red, VCE = Green
Figure 18
Full load start-up at VIN = 180 VAC
0,9550
0,9600
0,9650
0,9700
0,9750
0,9800
0,9850
0,9900
0,9950
1,0000
500
1000
1500
2000
2500
3000
3500
4000
4500
5000
PF
Output power (watt)
Power factor
180VAC
230VAC
264VAC

## [стр. 24]

User guide
24 of 38
v2.0


2021-12-06
The 5-kW, two-channel, interleaved CCM PFC EVAL board
IKW40N65WR5, IDW60C65D1, and 1ED44175 in high frequency PFC applications

System performance


Vout = Blue, VGE = Yellow, IL1 = Red, VCE = Green
Figure 19
Full load start-up at VIN = 264 VAC
4.3
Input current and inductor current cancellation
The following images (Figure 20-25) show six waveforms of the input AC current and two inductor current
waveforms of the converter at full load. The interleaving operation is highlighted and the two-channel currents
are phase shifted by 180°.


IIN = Green, IL1 = Yellow, IL2 = Red
Figure 20
Interleaving operation at full load at VIN = 180 VAC

## [стр. 25]

User guide
25 of 38
v2.0


2021-12-06
The 5-kW, two-channel, interleaved CCM PFC EVAL board
IKW40N65WR5, IDW60C65D1, and 1ED44175 in high frequency PFC applications

System performance


IIN = Green, IL1 = Yellow, IL2 = Red, VIN = Blue
Figure 21
Detailed view of interleaving operation at full load at VIN = 180 VAC


IIN = Green, IL1 = Yellow, IL2 = Red
Figure 22
Interleaving operation at full load at VIN = 230 VAC

## [стр. 26]

User guide
26 of 38
v2.0


2021-12-06
The 5-kW, two-channel, interleaved CCM PFC EVAL board
IKW40N65WR5, IDW60C65D1, and 1ED44175 in high frequency PFC applications

System performance


IIN = Green, IL1 = Yellow, IL2 = Red, VIN = Blue
Figure 23
Detailed view of interleaving operation at full load at VIN = 230 VAC


IIN = Green, IL1 = Yellow, IL2 = Red
Figure 24
Interleaving operation at full load at VIN = 264 VAC

## [стр. 27]

User guide
27 of 38
v2.0


2021-12-06
The 5-kW, two-channel, interleaved CCM PFC EVAL board
IKW40N65WR5, IDW60C65D1, and 1ED44175 in high frequency PFC applications

System performance


IIN = Green, IL1 = Yellow, IL2 = Red, VIN = Blue
Figure 25
Detailed view of interleaving operation at full load at VIN = 264 VAC
4.4
Switching performance of the IGBT at steady state
This board's design aims at achieving high efficiency by using the 650 V TRENCHSTOP™ 5 WR5 IGBT -
IKW40N65WR5 - as the main switch in a high-frequency, interleaved PFC application. Compared to Infineon's
H3 IGBT, the WR5 IGBT has lower conduction and switching losses. The WR5 IGBT can, therefore, replace the
MOSFET in applications with switching frequencies up to 100 kHz.
The following three waveforms (Figure 26-28) show switching performances of the IKW40N65WR5 with the lowside gate driver, 1ED44175. To check the driver's current capability, in this design, the turn-on gate resistance for
each KW40N65WR5 is 5.1 Ω and turn-off resistance is 3 Ω. A smaller gate resistance for turn-on and turn-off
decreases the turn-on and turn-off losses of the IGBT. However, during the design process, there is always a
trade-off between achieving high efficiency and EMI. In high frequency applications, customers must make extra
effort to reduce the noise created by high dv/dt and high di/dt.


VCE = Green, VGE = Yellow, IL1 = Red, VOUT = Blue
Figure 26
Switching waveforms of the IGBT at  VIN = 180 VAC at full load

## [стр. 28]

User guide
28 of 38
v2.0


2021-12-06
The 5-kW, two-channel, interleaved CCM PFC EVAL board
IKW40N65WR5, IDW60C65D1, and 1ED44175 in high frequency PFC applications

System performance


VCE = Green, VGE = Yellow, IL1 = Red, VOUT = Blue
Figure 27
Switching waveforms of IGBT at  VIN = 200 VAC at full load (continuous current at high point
of the input voltage)


VCE = Green, VGE = Yellow, IL1 = Red, VOUT = Blue
Figure 28
Switching waveforms of IGBT at  VIN = 200 VAC at full load  (current discontinued at low point
of the input voltage)
4.5
Output ripple voltage
Due to the limitation of the board size and cost considerations, only four output filter capacitors with a total of
2720 uF are placed at the output stage . As seen in the following three waveforms (Figure 29-31), the permissible
low-frequency ripple of the output voltage is lesser than 20 V at full load at different input voltages. This meets
the design specifications as well.

## [стр. 29]

User guide
29 of 38
v2.0


2021-12-06
The 5-kW, two-channel, interleaved CCM PFC EVAL board
IKW40N65WR5, IDW60C65D1, and 1ED44175 in high frequency PFC applications

System performance


VOUT = Blue, IIN = Red
Figure 29
PFC output ripple voltage at VIN = 180 VAC  at full load


VOUT = Blue, IIN = Red
Figure 30
PFC output ripple voltage at VIN = 230 VAC  at full load

## [стр. 30]

User guide
30 of 38
v2.0


2021-12-06
The 5-kW, two-channel, interleaved CCM PFC EVAL board
IKW40N65WR5, IDW60C65D1, and 1ED44175 in high frequency PFC applications

System performance


VOUT = Blue, IIN = Red
Figure 31
PFC output ripple voltage at VIN = 264 VAC  at full load
4.6
Input voltage and input current
The line current shown in Figure 32-34 are nearly perfect sinusoidal waves, in phase with the line voltage. Here
the output voltage is regulated at 400 V at full load.


VIN = Blue, IIN = Red
Figure 32
PFC input voltage and input current at VIN = 180 VAC  at full load

## [стр. 31]

User guide
31 of 38
v2.0


2021-12-06
The 5-kW, two-channel, interleaved CCM PFC EVAL board
IKW40N65WR5, IDW60C65D1, and 1ED44175 in high frequency PFC applications

System performance


VIN = Blue, IIN = Red
Figure 33
PFC input voltage and input current at VIN = 230 VAC  at full load


VIN = Blue, IIN = Red
Figure 34
PFC input voltage and input current at VIN = 264 VAC  at full load
4.7
Load step tests
Figure 35 and 36 show the response of the PFC converter during a load step from no load to full load with the
voltage undershoot reduced to 352 VDC and 360 VDC, respectively. After such an abrupt load demand, the PFC
controller returns to regulation in about 60 milliseconds.

## [стр. 32]

User guide
32 of 38
v2.0


2021-12-06
The 5-kW, two-channel, interleaved CCM PFC EVAL board
IKW40N65WR5, IDW60C65D1, and 1ED44175 in high frequency PFC applications

System performance


VOUT = Blue, IOUT = Green
Figure 35
Load step: 0% → 100% at VIN = 180 VAC


VOUT = Blue, IOUT = Green
Figure 36
Load step: 0% → 100% at VIN = 264 VAC

## [стр. 33]

User guide
33 of 38
v2.0


2021-12-06
The 5-kW, two-channel, interleaved CCM PFC EVAL board
IKW40N65WR5, IDW60C65D1, and 1ED44175 in high frequency PFC applications

System performance


VOUT = Blue, IOUT = Green
Figure 37
Load step: 100% → 0% at VIN = 180 VAC
Figure 37 shows the response of the voltage control loop during a load step from 100% to 0% and a voltage
overshoot of up to 425 V. A similar response can be observed at VIN = 230 VAC and VIN = 264 VAC.
4.8
Thermal measurements
The EVAL-PFC5KIKWWR5SYS board is provided with an enclosure. The thermal concept implemented in it
includes two low-power fans attached to two heat sinks in which the power semiconductors dissipate their
generated losses.

## [стр. 34]

User guide
34 of 38
v2.0


2021-12-06
The 5-kW, two-channel, interleaved CCM PFC EVAL board
IKW40N65WR5, IDW60C65D1, and 1ED44175 in high frequency PFC applications

System performance

Figure 38
Thermal capture at room temperature at nominal input (180 V) and full load conditions for
the PFC operation
Figure 38 shows that the PFC chokes are not the hotspot on the board. This is because of the two power fans in
an enclosed environment. The WR5 IGBT (Q3) is the hottest power device on this board because it is far from the
cooling fans. Table 5 lists the temperature data collected by Keysight 34970A with thermal couples. The highest
temperature of the IGBT is 84.2°C at full load when the input voltage is 180 VAC.  Fortunately, in floor-standing airconditioner applications, the IGBT's output power is de-rated to a low-input voltage; and as evident from the
temperature data at half load when the input voltage is 180 VAC, its highest temperature is only 45.9°C.
Table 5
Temperature of power semiconductors
Devices
VIN = 230 VAC, full load
VIN = 180 VAC, full load
VIN = 180 VAC, half load
Q2  (IKW40N65WR5)
51.7°C
67.8°C
39.8°C
D19 (IDW60C65D1)
61.6°C
74.2°C
40.3°C
Q3 (IKW40N65WR5)
62.1°C
84.2°C
45.9°C

## [стр. 35]

User guide
35 of 38
v2.0


2021-12-06
The 5-kW, two-channel, interleaved CCM PFC EVAL board
IKW40N65WR5, IDW60C65D1, and 1ED44175 in high frequency PFC applications

Conclusion
5
Conclusion
This user guide described the implementation of an analog-controlled, single-phase, two-channel interleaved
PFC converter that operates in a continuous conduction mode. This interleaved PFC converter achieves a peak
efficiency of 97.804% using an Infineon 650 V TRENCHSTOP™ 5 WR5 IGBT - IKW40N65WR5 and a rapid1 power
silicon diode - IDW60C65D1.
The EVAL-PFC5KIKWWR5SYS board has been tested using a programmable AC source and an electronic load to
demonstrate the key performance and behaviors during a PFC operation.
Customers can increase the switching frequency or extend the converter input voltage from 85 VAC to 264 VAC to
decrease the size and cost of the inductors. To optimize new requirements, external parameter setting for the
resistors and capacitors of the UCC28070 is also necessary.

## [стр. 36]

User guide
36 of 38
v2.0


2021-12-06
The 5-kW, two-channel, interleaved CCM PFC EVAL board
IKW40N65WR5, IDW60C65D1, and 1ED44175 in high frequency PFC applications

References and appendices
6
References and appendices
6.1
Abbreviations and definitions
Table 6
Abbreviations
Abbreviation
Meaning
CE
Conformité Européenne
EMI
Electromagnetic interference
UL
Underwriters Laboratories
BOM
Bill of Material
QR
Quasi-resonant
PF
Power factor
POCO
A Chinese powder core manufacturer
NPH-L
A powder core material from POCO
6.2
References
[1]
Texas instruments, "UCC28070 300W Interleaved PFC Pre-regulator Design Review (Rev. B)", Application
Report, SLUA479B, August 2008
[2] Infineon Technologies, "Fifth-generation QR design guide for ICE5QSAG and ICE5QRXXXXAX", Application
Report, DG_201609_PL83_026, September 2017
6.3
Additional information
For more information about the Infineon devices mentioned in this guide, click the following links:
⚫
TRENCHSTOP™ 5 WR5 IGBT IKW40N65WR5
⚫
Low-side gate driver 1ED44175N01B
⚫
Rapid1 power silicon diode IDW60C65D1
⚫
QR Flyback controller ICE5QSBG for auxiliary supply

## [стр. 37]

User guide
37 of 38
v2.0


2021-12-06
The 5-kW, two-channel, interleaved CCM PFC EVAL board
IKW40N65WR5, IDW60C65D1, and 1ED44175 in high frequency PFC applications
Revision history

Revision history

Document
version
Date of release
Description of changes
V 1.0
05-03-2021
Initial release
V 2.0
06-12-2021
Update schematic about over temperature protection and clock sync.

## [стр. 38]

Published by
Infineon Technologies AG
81726 Munich, Germany

© 2022 Infineon Technologies AG.
All Rights Reserved.

Do you have a question about this
document?
Email: erratum@infineon.com

Document reference

For further information on the product, technology,
delivery terms and conditions and prices please
contact your nearest Infineon Technologies office
(www.infineon.com).

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




Edition 2021-12-06
UG-2021-06
Trademarks
All referenced product or service names and trademarks are the property of their respective owners.
