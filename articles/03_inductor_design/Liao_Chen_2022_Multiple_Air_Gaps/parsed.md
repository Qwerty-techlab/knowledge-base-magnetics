# Design process of high‐frequency inductor with multiple air‐gaps in the dimensional limitation

> Автоматически извлечено из `source.pdf` скриптом `parse_pdf.py`
> Движок: pymupdf. Страниц: 18 из 18.
> Дата извлечения: 2026-08-07 06:43 UTC

Текст не редактировался. Формулы и таблицы могут быть искажены —
при сомнении сверяться с исходным PDF.

---

## [стр. 1]

Received: 27 April 2021
Revised: 29 August 2021
Accepted: 9 September 2021
The Journal of Engineering
DOI: 10.1049/tje2.12087
ORIGINAL RESEARCH PAPER
Design process of high-frequency inductor with multiple air-gaps
in the dimensional limitation
Hsuan Liao
Jiann-Fuh Chen
Department of Electrical Engineering, National
Cheng Kung University, Tainan, Taiwan
Correspondence
HsuanLiao, DepartmentofElectricalEngineering,
NationalChengKungUniversity, Tainan, Taiwan.
Email: n28064046@gs.ncku.edu.tw
Fundinginformation
Delta ElectronicsFoundation; MinistryofEducation(MOE)inTaiwan; MinistryofScienceand
Technology, Taiwan
Abstract
To find the optimal magnetic components designing process within the dimensional limitation, different inductor arrangements are developed. Different combinations of air-gaps
and material arrangements are used within the limited bobbin space to improve the saturation current capacity within the already set dimension. In this study, the mechanism
requirement set at 1U height is the limitation. There are two center-pole material cores,
and air-gap distribution arrangement in the magnetic components. The saturation current
value, magnetic flux density, flux fringing, and power loss of inductors are investigated
with simulation, equation calculation and actual circuit measurement. The magnetic distribution affects the inductor performance because of the different relative permeability values, skin effect, proximity effect, and fringing effect. This research uses equations to find
the magnetic flux density and the fringing magnetic flux, and uses Comsol Multiphysics®
software to simulate the magnetic field. A 500 W boost power factor corrections (PFC)
converter topology is used as an example experiment to compare and verify the inductors
selected with proposed design methodology. Finally, the most appropriate core is chosen
to implement the two-stage AC/DC power supply products to improve the power supply
performance.
1
INTRODUCTION
Power electronic technology on electric power supplies has
developed rapidly and has applied to applications such as electric vehicles, telecommunications, and alternative-energy systems. Magnetic components are an indispensable part of the
electric power supply circuit. All electronic circuits require the
use of inductors, indicating the importance of the design of
the magnetic components in the circuit. High-frequency inductors are very important components in modern switched-mode
power supplies (SMPS's) electronic devices. They are essential
for SMPS to achieve compliance with SMPS's standards and to
meet the requirements of harmonic current and power factor,
such as IEC61000-3-2 [1].
Moreover, inductors are the key component to influence
the overall circuit efficiency. Different materials, winding methods, and center-pole segments are techniques with abundance
researches to improve the design of the inductor for inductor
loss minimization [2-7]. Inductor losses can be divided into
This is an open access article under the terms of the Creative Commons Attribution License, which permits use, distribution and reproduction in any medium, provided the original work is
properly cited.
© 2021 The Authors. The Journal of Engineering published by John Wiley & Sons Ltd on behalf of The Institution of Engineering and Technology
copper loss and iron loss. The latter can be segmented into hysteresis and eddy-current losses. The eddy-current losses caused
by the skin and proximity effects has gradually exceeded the
core loss and become a major part of the inductor loss due
to high operation frequencies [2, 8, 9]. The high-frequency
effect causes circuit reliability and stability to decrease. Therefore, research on high-frequency related inductors is extremely
important.
Currently, Jez focused on the influence of different air-gap
arrangement of low frequency inductors [3]. It indicated that
higher number of air-gap could reduce the magnetic component power losses. This research, however, looks at the air-gap
arrangement in the inductors related to much higher frequency
when compared with Jez's work [3]. Ayachit et al. proposed
the modified Steinmetz equation for power loss density of
different air gap lengths and frequencies at the magnetic core
of the inductor with one air gap [6]. Our research looks into
the arrangement of different numbers of air-gaps with finite
element methods (FEM). Saini et al. proposed a systematic
16
wileyonlinelibrary.com/iet-joe
J. Eng. 2022;2022:16-33.

## [стр. 2]

LIAO AND CHEN
17
Vac
CO
PFC
Converter
( Boost, Buck,
Buck-Boost,
Flyback, Cuk'...)
DC/DC
Converter
Db
L
Vac
CO
Sw
EMI
Filter
RL
-
+
Vo
EMI
Filter
DC/DC
Converter
RL
-
+
Vo
Boost PFC Topology
FIGURE 1
Structure of two-stage AC/DC coveter using a boost PFC
topologic
inductor design procedure for Class-E inverter which provided
core power losses and mechanical specifications [7]. In comparison with the findings published by Saini et al., this study
describes the design procedure in more detail and uses software
to obtain the fringing flux simulation [7]. Jez et al. presented
analysis model by using Comsol Multiphysics software to obtain
FEM results [10]. Our research included the real 3D module, in
Comsol Multiphysics software, to obtain more detailed simulation results such as fringing flux values. The gapped inductor
is useful in many places, particularly for the applications that
need to avoid working in the current saturation situation. These
air-gaps affect the magnetic circuit in many aspects, such as
changing the shape of the B-H curve, reducing the inductance effectiveness, increasing the saturation current capability
to avoid magnetic components saturation, and causing the
fringing flux phenomenon [3]. Therefore, the arrangements of
air-gap placements are the main research purpose in this study.
In addition, a power factor correction (PFC) converter was
used in this research, as an example set up, to compare the
use of inductors with different air-gap arrangements. PFC converters are commonly used in power supplies for power quality improvements and harmonic distortion minimization [9-12].
The boost, buck, buck-boost, flyback, and Cuk types are common topologies for active PFC [13-18]. The most commonly
used boost topology, in general, is constructed with a diode rectifier, a boost inductor L, a high-frequency switch Sw, a boost
diode Db, and a bulk capacitor Co. The structure of the twostage AC/DC converter using a boost PFC topology is shown
in Figure 1, which is the experimental circuit in this paper.
There are three aspects of magnetic component for choosing the design trade-off study: cost, size, and performance. The
boost inductors are critical components in PFC circuits, and
the performance is determined by the operating frequency, flux
density, and temperature. The power inductors design process
requires considerations of several important parameters. The
magnetic core volume is the essential determinant of power
density. Increasing the switching frequency enables the reduction of the inductor size for power density improvement [19].
Furthermore, modern electronic products are mainly thin
and small. There is a standard operating procedure for electronic product design. The product dimensions are usually
predefined to meet the international standard EIA RS-310,
established by Electronics Industries Association (EIA) [20].
Therefore, the available space for electric circuit design is
limited. U is an abbreviation for Unit in EIA RS-310 standard,
representing the external size of the electronic product. The
mechanical engineer usually uses this unit to discuss product
dimension with the electronic engineer. In this study, the
mechanism limitation is 1U height.
In this study, the pole area at the core's center part is defined
as the center-pole area. Due to the dimensional limitations and
the cost considerations, a low relative permeability material is
chosen as Sendust. The effects of different air-gaps and material arrangement at the center-pole in the limited bobbin space
are the main objective for this research. Compare the influence
of each high-frequency inductor on the saturation current capability. The objectives of this paper are listed as follows.
1. To discuss the distribution of different materials, and multiple air-gaps assignments derived inductance from the magnetic reluctance circuit [21], and considerations for designing
high-frequency inductors in the dimensional limitation.
2. To improve the saturation current capacity for the gapped
inductor design process described in detail with the related
equations addressed in Sections 2 and 3.
3. To simulate the magnetic flux and fringing flux based on
FEM in Comsol Multiphysics software [22, 23].
4. To compare the power losses and verify the experimental
results illustrated for a 500 W boost PFC converter.
5. The inductor performance can be improved if the device is
built according to the proposed design process. The design
method described in this paper can be implemented and
applied to the actual industrial AC/DC products.
6. The proposed idea of this research is that when the product
is updated and republished, the size of the mechanism cannot be replaced because of the cost. The main contribution is
replacing the different materials of the center-pole core and
the different numbers of air-gaps instead of the whole boost
inductor. It is unnecessary to use Sendust ring core which
can save cost and dimension place.
2
CONSIDERATIONS OF DESIGNING
HIGH-FREQUENCY BOOST INDUCTOR
The PQ3530 type core is selected for this study, assuming 1U
height dimension limit. The materials and center-pole segments
are techniques to improve magnetic components performance.
The high-frequency condition affects the fringing effect, and it
usually happens near the air-gap area. For the cost consideration, ferrite and low relative permeability material-Sendust are
chosen. Three different types of air-gap distributions between
ferrite/Sendust cores are compared in this study. At the same
time, the modification in inductance calculation based on the
 20513305, 2022, 1, Downloaded from https://ietresearch.onlinelibrary.wiley.com/doi/10.1049/tje2.12087, Wiley Online Library on [22/07/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

## [стр. 3]

18
LIAO AND CHEN
FIGURE 2
Indicative arrangements of the section view locations and
numbers of air-gaps with center-pole constructed using different materials
different air-gap distributions has been outlined and explained
in this section.
For a boost PFC converter, the inductor requires to handle a
sufficiently high current level to ensure the magnetization curve
remains in the first quadrant. There are four common iron core
materials and their saturation characteristics in [21]. This article uses a combination of ferrite and Sendust material. The reason for choosing Ferrite core is the low cost, low power losses,
and common for power electronics applications. Sendust is the
material composited of FE, Si, and AL materials. The reason
for choosing Sendust core is its good characteristics such as low
core loss, lower magnetic loss than conventional iron powder
cores. It also has good DC bias characteristics and cost is lower
than MPP.
Although the application of Sendust core is not a new idea in
power electronics, the proposed idea can help to deal with the
current capacity problems. It is unnecessary to use the Sendust
ring core that just replaces the ferrite center-pole core as the
Sendust center-pole core can save cost and dimension place.
2.1
Arrangements of high-frequency boost
inductor
Different air-gap locations and numbers of air gaps, and different core materials are used for the center-pole area. The
arrangements of all different center-pole cores section view
are depicted in Figure 2, which include one to three air-gaps
(lg) within the same dimensional limited magnetic core. Type I
model is an air-gap ferrite core that produces the conventional
way to store energy. Type II model is a ferrite main body with
one ferrite or Sendust made center-pole core, producing two
air-gaps. Type III model is a ferrite main body with two ferrites or Sendust center-pole cores with three air-gaps. References [3, 6, 10] illustrate the different air-gaps distribution which
could influence the circuit performance. However, the aim is to
replace the different materials and numbers of air-gaps in the
center-pole core in the same dimension which is the new proposed idea.
2.2
Derived inductance from the reluctance
of the magnetic circuit
The air gap quantity is directly related to the energy storage consumption since the energy is stored in the air gap.
FIGURE 3
Inductor with one air-gap on the center-pole. (a) One air-gap
on the, (b) Equivalent magnetic circuit center-pole
Therefore, using the magnetic reluctance of the magnetic
circuit is the method used to derive inductance for this research.
The reluctance would be varying because of the physical dimension and material. The reluctance calculation method uses one
to three air-gaps of center-pole with different core materials.
The inductance is related to the shape, size, winding method,
number of turns, and the type of intermediate magnetic material. This section uses the air gap and material permeability to
calculate the inductance [21].
2.2.1
Use one air-gap to calculate the inductance
Type I model consists of two PQ-shaped cores with one air-gap
between the center-poles. The inductor's cross-sectional view is
shown in Figure 3a. An equivalent magnetic circuit of the oneair-gap inductor is shown in Figure 3b. The equations used for
calculating the equivalent reluctance are shown below. ℜ1 represents the reluctance of the air-gap center-pole on both sides.
ℜ2 and ℜ3 represent the reluctance of the outer legs. ℜg represents the reluctance of the air-gap. NI presents the magnetomotive force (MMF) of the core that the flux production depends
on the material's resistance.
The reluctance ℜg of one air-gap is
ℜg =
lg
𝜇oAg( fe)
(1)
where lg is the length of one air-gap; Ag(fe) is the ferrite core
cross-sectional area with an air-gap; μo is the permeability of
free space. The reluctance is proportional to the air-gap length,
and inversely to the cross-sectional area, Ag(fe).
The reluctanceℜfe of one ferrite core is
ℜfe =
l fe -lg
𝜇r fe𝜇oA fe
(2)
where μrfe is the relative permeability of the ferrite core; Afe is
the ferrite core's cross-sectional area; lfe is the ferrite core total
effective magnetic path length. The higher inductance under a
 20513305, 2022, 1, Downloaded from https://ietresearch.onlinelibrary.wiley.com/doi/10.1049/tje2.12087, Wiley Online Library on [22/07/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

## [стр. 4]

LIAO AND CHEN
19
FIGURE 4
Inductor with two air-gaps on the center-pole. (a) A Sendust
or ferrite core insert into center-pole, (b) Equivalent magnetic circuit with two
air-gaps
certain volume can be obtained from the characteristic of high
relative permeability.
The overall reluctance ℜeq(1gap) of the ferrite core with one
air-gap is
ℜeq(1gap) =
l fe -lg
𝜇r fe𝜇oA fe
+
lg
𝜇oAg( fe)
(3)
The inductance L1gap for a ferrite core with one air-gap is
expressed in Equation (4).
L1gap =
𝜇oA feN 2
lg(
𝜇r feA fe-Ag( fe)
𝜇r feAg( fe)
) +
(
l fe
𝜇r fe
)
(4)
With the assumption that Ag(fe) = Afe, the inductance L1gap for
a ferrite core with one air-gap can be expressed as Equation (5)
L1gap =
𝜇oA feN 2
lg(
𝜇r fe-1
𝜇r fe ) +
(
l fe
𝜇r fe
)
(5)
The formula for the inductance value is proportional to
the magnetic permeability, the square of the winding turns N,
and the equivalent magnetic circuit cross-sectional area, and
inversely to the equivalent magnetic circuit length.
2.2.2
Use two air-gaps to calculate the
inductance
Type II-SE and type II-FE are models with two air-gaps formed
with one piece of magnetic core made with Sendust or ferrite
materials inserted into the center-pole. Figure 4a illustrates the
cross section of the two air-gaps inductor. The inductor consists of two PQ-shaped ferrite cores and a piece of Sendust or
ferrite made core at the center-pole. An equivalent magnetic circuit with two air-gaps is shown in Figure 4b. The air-gaps length
l2gt is the sum of both air-gaps, lg1 and lg2.
FIGURE 5
Inductor with three air-gaps at the center-pole. (a) Two pieces
of Sendust or ferrite core on center-pole, (b) Equivalent magnetic circuit with
three air-gaps
The overall reluctance ℜeq(2,gaps,fe) for one piece ferrite core at
the center-pole with two air-gaps is
ℜeq(2,gaps, fe) =
l fe -l2gt
𝜇r fe𝜇oA fe
+
l fe4
𝜇r fe4𝜇oA fe4
+
l2gt
𝜇oA fe
,
(6)
where Afe4 is the center-pole area with a piece ferrite core; lfe4 is
the length of the piece ferrite core. The overall reactance would
vary from the different lengths of the center-pole core.
The inductance L2,gaps(fe) of a magnetic core with two air-gaps
is expressed as
L2,gaps( fe) =
𝜇oN 2
l2gt ( fe)
A fe
(
𝜇r fe-1
𝜇r fe
)
+
(
l fe
𝜇r feA fe
)
+
(
l fe4
𝜇r fe4A fe4
)
(7)
The calculation concept of the two air-gap inductor is like
that of one air-gap inductor. Replace the ferrite center-pole
core to the Sendust center-pole core. The overall reluctance
ℜeq(2,gaps,se) for the Sendust core at the center-pole area with two
air-gaps is
ℜeq(2,gaps,se) =
l fe -l2gt
𝜇r fe𝜇oA fe
+
lse4
𝜇rse4𝜇oAse4
+
l2gt
𝜇oA fe
,
(8)
L2,gaps(se) =
𝜇oAse4N 2
l2gt (se)
(
𝜇r fe-1
𝜇r fe
)
+
(
l fe
𝜇r fe
)
+
( lse4
𝜇rse
),
(9)
where Ase4 is the cross-sectional area of the Sendust core; lse4 is
the length of the Sendust core.
2.2.3
Use three air-gaps to calculate the
inductance
Type III-SE and type III-FE are three air-gaps with two pieces
of Sendust or ferrite cores inserted in the center-pole. Figure 5a
illustrates the inductor with three air-gaps. It consists of two
 20513305, 2022, 1, Downloaded from https://ietresearch.onlinelibrary.wiley.com/doi/10.1049/tje2.12087, Wiley Online Library on [22/07/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

## [стр. 5]

20
LIAO AND CHEN
PQ-shaped ferrite cores, with two pieces of ferrite or Sendust
core at the center-pole. An equivalent magnetic circuit with
three air-gaps is shown in Figure 5b.
The air-gaps length l3gt is the sum of all air-gaps. The overall
reluctance ℜeq(3,gaps,se) for two pieces of Sendust core with three
air-gaps is
ℜeq(3,gaps,se) =
l fe -l3gt
𝜇r fe𝜇oA fe
+
lse4
𝜇rse4𝜇oAse4
+
lse5
𝜇rse5𝜇oAse5
+
l3gt
𝜇oA fe
,
(10)
where lse4 and lse5 are the lengths of two pieces of Sendust cores
on the center-pole area. Ase4 and Ase5 are cross-sectional areas
with two pieces of Sendust core.
The inductance value L3,gaps(se) for two pieces of Sendust core
with three air-gaps is expressed as
L3,gaps(se) =
𝜇oA feN 2
l3gt (se)
(
𝜇r fe-1
𝜇r fe
)
+
(
l fe
𝜇r fe
)
+
( lse4+lse5
𝜇rse4
).
(11)
There are two materials in the specific inductor, so two relative permeabilities exist in the formula. The calculation concept
of the three air-gap inductor is the same as the one air-gap and
two air-gap inductors.
On the other hand, the Sendust cores are replaced with ferrite core, assuming Afe = Afe4 = Afe5 and μrfe = μrfe4 = μrfe5,
the inductance value L3,gaps(fe) with three air-gaps can be
expressed as
L3,gaps( fe) =
𝜇oA feN 2
l3gt ( fe)
(
𝜇r fe-1
𝜇r fe
)
+
(
l fe+l fe4+l fe5
𝜇r fe
).
(12)
The inductance is based on the magnetic path length, the sum
of the air-gaps length, and the relative permeability of the different material core.
3
DESIGN MULTIPLE AIR-GAPS CORE
FOR PFC INDUCTOR METHODOLOGY
In this section, by considering all the factors that would affect
the performance of the PFC converter, a design methodology
is implemented for one air-gap, two air-gaps, and three air-gaps
inductors. Based on the boost PFC converter circuit, the parameters for the inductor can be obtained, including the output
power, operating frequency, inductance, core size, and winding
turns. The flow chart of the design methodology is shown in
Figure 6.
3.1
Step 1: Derive inductance from PFC
circuit topology
The boost inductor L can be calculated according to the equations from the appendix [7, 24, 25].
From PFC circuit obtained
specification: Vrms, Irms, fsw, D IL, L
Calculate copper loss, Pcu
Calculate  flux density
and core loss , Pfe
Bobbin-fit
calculations
Change
core size
Change
wire  size
or filar
Yes
Yes
Yes
NO
NO
NO
Select the core material, shape, size
Wa, Ku, Aws,Aw(b)
Calculate fringing flux, F
Re-calculate parameter, L, N
Calculate all air-gaps, lg
Calculate Ap value and turns N
Build and test  various magnetic cores
FIGURE 6
Flow chart of design methodology for the multiple air-gaps
inductors
3.2
Step 2: Select the core size and materials
There are different materials and shapes available for the inductor core at the center pole. MPP, high flux, Sendust powder, and
ferrite are common materials used in PFC magnetic cores [21,
24].
The low power losses and low cost are the reasons why ferrite cores are commonly used for power electronics applications.
For this research, the dimension limitation of the experiment is
set at 1U height, and the PQ3530-type is selected. Ferrite or low
relative permeability material, Sendust core, is inserted into the
center-pole.
3.3
Step 3: Estimate the area product and
the number of turns
3.3.1
Estimate the core area product
Methods for evaluating the core size include the simple scaling law method [25], the core area product method Ap, and the
core geometrical coefficients method Kg [26]. In this paper, the
Ap method is used to find the suitable inductor shape and size.
The energy-handling capability of the core is related to its area
product Ap [26], by equation
AP = 2Energy(104)
BmJmKu
,
(13)
where Ap is in cm4; Energy is in watt-seconds; Bm is flux density
which is in tesla; Jm is current density which is amps-per-cm2; Ku
 20513305, 2022, 1, Downloaded from https://ietresearch.onlinelibrary.wiley.com/doi/10.1049/tje2.12087, Wiley Online Library on [22/07/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

## [стр. 6]

LIAO AND CHEN
21
is window utilization factor which is the maximum size for the
copper winding in the window space. The normalized window
utilization, Ku, is usually influenced by multiple factors for all the
cores design [26].
The energy-handling capability of the inductor can be derived
as
Energy =
LI 2
L,pk
2
,
(14)
where IL,PK is the inductor peak current. Equation (14) shows
the maximum energy stored in the air-gap of the inductor.
The obtained area product may be several combinations of
core area, and the window area will satisfy the required area
product. In this paper, using the formulas and choosing the suitable size for the mechanism limitation (1U), the PQ3530 meets
the requirement and its cost is low, so it is commonly used in
the industry products.
3.3.2
Calculate the turn of the winding
Wire selection involves the choice of material, shape, and
size of the conductor as well as the insulation thickness. To
achieve the winding turn calculation, the first step would be
to select the desired wire for winding. Then, calculating the
required number of turns N, the number of strands Sn, and
the bare wire area for strands Aws(AWG#NO.) which are suitable for the topology needs. These equations are shown in the
appendix [7, 24].
3.4
Step 4: Derive the air-gaps lengths
The following equations can be used to derive the various airgap lengths defined in chapter 2 in different core structure combinations. Equation (15) represents the calculation method for
the air gap of the inductor with one air-gap design [23, 24].
lg =
[(
𝜇oA feN 2
L1gap
)
-
( l fe
𝜇r fe
)]
×
(
𝜇r fe
𝜇r fe -1
)
.
(15)
The length of two air-gaps inductors design with ferrite and
Sendust core can be obtained with Equations (16) and (17),
respectively.
lg2( fe) = 1
2
[(
𝜇OA feN 2
L2,gaps( fe)
)
-
(l fe + l fe4
𝜇r fe
)]
×
(
𝜇r fe
𝜇r fe -1
)
,
(16)
lg2(se) = 1
2
[(
𝜇OA feN 2
L2,gaps(se)
)
-
( l fe
𝜇r fe
)
-
( lse4
𝜇rse
)]
×
(
𝜇r fe
𝜇r fe -1
)
.
(17)
Finally, the air gap lengths for inductors with three air-gaps
design with Sendust and ferrite cores can be calculated with
Equations (18) and (19), respectively.
lg3(se) = 1
3
[
𝜇OA feN 2
L3gaps(se)
-
( l fe
𝜇r fe
)
-
(lse4 + lse5
𝜇rse
)]
×
(
𝜇r fe
𝜇r fe -1
)
,
(18)
lg3( fe) = 1
3
[
𝜇OA feN 2
L3gaps( fe)
-
(l fe + l fe4 + l fe5
𝜇r fe
)]
×
(
𝜇r fe
𝜇r fe -1
)
.
(19)
Inserting into a different material magnetic path in the air-gap
of the inductor, the effective permeability can be changed.
3.5
Step 5: Fringing flux factor
consideration
The most common analysis method of fringing effect uses the
generic fringing factor (Ff) proposed by McLyman's equation
[26].
Ff =
[
1 +
lg
√A fe
× ln 2G
lg
]
,
(20)
where G is the dimension of the core. It can be seen that the
winding length or the core's dimension affect the fringing flux.
For accuracy, Equation (20) uses a tuning coefficient q for
round cross-section [25]. The correction for fringing flux factor
(Ff') is
F ′
f =
[
1 +
qlg
√A fe
× ln 2G
lg
]
,
(21)
where q is 0.85-1.1 for round cores. It can be divided into the
round cores and the rectangular cores factors. The tuning coefficient q of PQ cores or ETD cores is 0.85-0.95, and the tuning
coefficient q of EE core is 1-1.1 [25].
The winding losses near the air-gap increased greatly and
the total losses for the gapped inductor should be taken into
account. The finite element analysis (FEA) simulation is available to determine the winding loss due to the fringing effect
[23]. The simulated result could be compared with the results
from FEM via the simulation software [25].
This is achieved by building a reality 3 dimensions (3D)
inductor in computer-aided design (CAD) software Solidworks
software, followed by linking the 3D file into Comsol Multiphysics software to simulate the magnetic field [27, 28].
The multiple air-gap arrangements are computed under the
same setup conditions. In this manner, the fringing flux distribution and flux density of the inductors could be characterized. The distribution shows that energy can be stored in the
air-gaps, regardless of the number of gaps. The FEM models
offer a more analytical approach to confirm the fringing flux
distributions.
The leakage flux value depends on the useful flux. In the magnetic theory definition, the useful flux is defined from the air
 20513305, 2022, 1, Downloaded from https://ietresearch.onlinelibrary.wiley.com/doi/10.1049/tje2.12087, Wiley Online Library on [22/07/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

## [стр. 7]

22
LIAO AND CHEN
gap which means the fringing flux [24, 26]. From the FEM simulations, the leakage flux is negligible because the leakage flux
values are smaller than the fringing flux values in this paper.
3.6
Step 6: Calculate the new winding turns
with fringing flux factor
The corrected fringing flux factor Ff' can be rewritten from
Equations (5), (7), (9), (11), and (12) which can solve the
required turns N, so that premature core saturation can be
avoided. The number of turns N' corrected for fringing flux are
N ′
1gap =
√
√
√
√
√
√
L1gap
[
lg
(
𝜇r fe-1
𝜇r fe
)
+
(
l fe
𝜇r fe
)]
𝜇oF ′
f A fe
,
(22)
N ′
2,gaps( fe) =
√
√
√
√
√
√
L2,gaps( fe)
[
l2gt ( fe)
(
𝜇r fe-1
𝜇r fe
)
+
(
l fe+l fe4
𝜇r fe
)]
𝜇oF ′
f A fe
,
(23)
N ′
2,gaps(se) =
√
√
√
√
√
√
L2,gaps(se)
[
l2gt (se)
(
𝜇r fe-1
𝜇r fe
)
+
(
l fe
𝜇r fe
)
+
( lse4
𝜇rse
)]
𝜇oF ′
f A fe
,
(24)
N ′
3,gaps(se) =
√
√
√
√
√
√
L3,gaps(se)
[
l3gt (se)
(
𝜇r fe-1
𝜇r fe
)
+
(
l fe
𝜇r fe
)
+
( lse4+lse5
𝜇rse4
)]
𝜇oF ′
f A fe
,
(25)
N ′
3,gaps( fe) =
√
√
√
√
√
√
L3,gaps( fe)
[
l3gt ( fe)
(
𝜇r fe-1
𝜇r fe
)
+
(
l fe+l fe4+lse5
𝜇r fe
)]
𝜇oF ′
f A fe
.
(26)
Equations (22)-(26) are the new winding turns of one airgap to three air-gaps with two different materials that have the
accuracy fringing flux factor.
3.7
Step 7: Calculate the inductor losses
The Eddy-current losses are caused by the skin and proximity effects which is the major part of the inductor loss due to
high operation frequencies [2, 8, 9]. The high-frequency power
inductor losses consist of three different types of losses: dc winding loss, ac winding loss, and core losses. The dc winding loss
occurs from the resistivity of the conductor and the loss can be
reduced easily by increasing the cross-sectional area of the conductor. The ac winding power loss occurs from skin and proximity effect of ac current [24, 29-32]. The inductor core loss,
which is dependent on core volume, occurs due to the change
in magnetic flux field within the core.
3.7.1
The dc winding losses
The dc resistance of the conductor cross-sectional area with a
winding total length is [24, 30]
Rwdc = 4𝜌wNlT
𝜋d 2
,
(27)
where ρw is the resistivity of the conductor material, lT is the
mean turn length (MTL), and d is the bare round conductor
diameter.
The resistivity of the conductor material at the maximum
operating temperature is given by
𝜌w(T ) = 𝜌w(TO)[1+𝛼(TO)(Tmax -TO)],
(28)
where TO is the room temperature, Tmax is the maximum temperature, ρw(To) is the conductor resistivity at temperature TO,
and α(To) is the temperature coefficient of the conductor resistivity.
The wire sizes are selected from the standard wire table,
which also specifies the resistance of the wire selected [24, 33].
The dc winding loss can be expressed by [30]
Pwdc(Cu) = RwdcI 2rms.
(29)
The dc winding power loss is proportional to the dc winding
resistance.
3.7.2
The ac winding loss
The ac power loss of inductor windings is caused by the skin
effect and the proximity effect. In conductors, the skin effect is
caused by the self-Eddy currents, and the proximity effect is
caused by externally induced Eddy currents. The ac-to-dc winding resistance ratio FR of the multi-layer inductor using a onedimensional model can be described by Dowell's formula [24,
26, 34, 35]
FR =
( 𝜋
4
) 3
4 ( d
𝛿
) √𝜅p
[
sinh(2Δ)+sin(2Δ)
cosh(2Δ)-cos(2Δ) +
2(N 2
l -1)
3
sinh(Δ)-sin(Δ)
cosh(Δ)+cos(Δ)
] ,
(30)
where Nl is the number of layers and Δ is the ratio of the layer
thickness d to the skin depth δ at the switching frequency. kp
is the porosity factor (kp = d/p) and the skin effect factor is a
function of d/δ, where δ is the skin depth of a conductor at the
switching frequency fsw [26, 34]. This is given by
𝛿=
√
𝜌w(TO)[1 + 𝛼(TO)(T -To)]
𝜋𝜇r (T )𝜇o fsw
.
(31)
 20513305, 2022, 1, Downloaded from https://ietresearch.onlinelibrary.wiley.com/doi/10.1049/tje2.12087, Wiley Online Library on [22/07/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

## [стр. 8]

LIAO AND CHEN
23
The skin effect is related to the current near the surface in a
skin depth δ.
When the circuit is operating at high frequency, the current
density is non-uniform. The winding ac resistance Rwac is higher
than dc resistance Rwdc due to the skin and proximity effects [24,
30]. The winding power loss is given by
Pwac = FRRwdcI 2rms.
(32)
The total ac-to-dc winding loss Pw(Cu) could then be calculated
with
Pw(Cu) = Pwac + Pwdc(Cu).
(33)
3.7.3
Magnetic core losses
In general, the power loss density of the core can be obtained
with the Steinmetz equation [24, 25, 30].
Pfe,s = KC f 𝛼B𝛽
m,
(34)
where f is the operation frequency in kHz and Bm is the magnetic
flux density in mT. The frequency exponent, α, is the induction
peak value of the ac waveform and β is the core loss exponent.
The total magnetic power loss of the core volume Vc is given
by
Pfe,v = VC Pfe,p.
(35)
The total inductor power loss PT can be calculated with
PT = Pw(Cu) + Pfe,v.
(36)
The core loss, Pfe,v, is a fixed loss, and the cooper loss, Pw(Cu),
is related to the rated current load. The values would be calculated and shown in Section 4.
4
EXPERIMENTAL AND
MEASUREMENT RESULTS
According to the design flow chart in Section 3, a 500 W experimental prototype with universal input voltage and 390 V output voltage was constructed. The specifications for the boost
PFC circuit are listed in Table 1. The calculated boost inductance value of the PFC circuit is about 440 μH. The converter
operates at a fixed frequency of 65 kHz.
The experiment uses two types of cores made with different
materials to compare five different cases of multiple air-gaps
cores. Ferrite cores have been used for electrical applications
normally. The ferrite inductor type allows tight winding, with
the window utilization factor, Ku, at 0.6, Bpk at 0.41 T, and Jm at
5 A/mm2. The PQ3530 ferrite core is the main body that fits
the 1U height limitation. Detailed parameters of the DMEGC
ferrite cores [36], DMR95 material, and Sendust 60 core mateTABLE 1
Design specifications for the power stage circuit
Symbol
Description
Value
Vac,rms
Universal mains
voltage
90 V TO 264 V
fline
Line frequency
47 HZ TO 63 HZ
Vo
Output voltage
390 V
Po
Output power
500 W
fsw
Switching frequency
65 KHZ
Δk,Ripple
Inductor current ripple
0.35 AT LOW LINE,
FULL LOAD
TABLE 2
Parameters and materials of analysed inductors [36]
Symbol
Description
Value
L
Inductance of boost inductor
440 𝜇H ± 7%
Irms
RMS current
6 A
Bsat
Saturation magnetic flux
(100◦C)
0.41 T
μrfe
Relative permeability of ferrite
core
3300
μrse60
Relative permeability of
Sendust core
60
Afe, Ase
Cross-section area of the
ferrite or Sendust
1.73 cm2
lc
Magnetic path length (MPL)
7.0 cm
Wa
Window area
1.71 cm2
AP
Area product
2.9583 cm4
VC
Volume of core
12.11 cm3
rial are listed in Table 2. The appearance of all core types of
shapes in the experiment is shown in Figure 7.
From Equation (31), the skin depth of a copper conductor
can be calculated to be 0.299 mm. From Equations (A5) and
(A6), the number of strands Sn is determined and the actual
winding designed is around 150. The number of windings N
is calculated by Equation (A4). By substituting N into Equations (15)-(19), the air-gap lengths for different air-gap arrangements can be derived. The derived air-gap lengths can then be
used to calculate the generic and corrected fringing flux factor value via Equations (20) and (21). The inductances of the
cores were measured by DPG10 LCR meter [37], and are listed
in Table 3.
FIGURE 7
The appearance of all the cores for the experiments. (a) Type I
model, (b) type II model, (c) type III model
 20513305, 2022, 1, Downloaded from https://ietresearch.onlinelibrary.wiley.com/doi/10.1049/tje2.12087, Wiley Online Library on [22/07/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

## [стр. 9]

24
LIAO AND CHEN
TABLE 3
Measured inductance for the five types model
Type
Centerpole
material
Air-gaps
(mm)
L (μH)
DCR
(mΩ)
Winding
Turns
I
Non-use
lgt = 2.18
445.21
66.89
0.1*150c
55
II-FE
DMR95
l2gt = 2.18
445.35
II-SE
S060
l2gt = 1.89
440.05
III-SE
S060
l3gt = 1.4
454.99
III-FE
DMR95
l3gt = 1.4
453.68
Current vs. Incremental Inductance Curve
for Five Types
I (A)
0
5
10
15
20
L (uH)
0
100
200
300
400
500
Type I
Type II-FE
Type II-SE
Type III-SE
Type III-FE
FIGURE 8
Incremental inductance versus current for five types
In this study, the ferrite core's relative permeability is 3300,
and the Sendust core's relative permeability is 60. The difference
in relative permeability of the cores is based on the magnetic
field intensity. The incremental inductance versus current curves
for the five types of cores is shown in Figure 8. The current
curves can be divided into two parts. One has a gapped ferrite
core, with one or two ferrite cores at the center-pole. The other
has a ferrite main body with one or two Sendust cores at the
center-pole.
In comparing the five curves, it can be seen that the current
curves of the inductors with low relative permeability Sendust
cores in the center-pole are flatter than the inductors with the
ferrite cores, indicating the change of inductance per current
interval is smaller for inductors with Sendust core. However,
the inductance is drastically decreased for the inductors with the
ferrite core in the center-pole area.
4.1
The losses of high-frequency power
inductor
Using the equation shown in Section 3, the copper loss and
the core loss can be calculated. From Equation (27), the dc
copper winding loss is 2.208 W. Given Nl as 6 layers, by using
Equation (30), the FR ratio of 1.0844 can be calculated. From
TABLE 4
High-frequency inductor power loss results
Symbol
Description
Value (W)
Pwdc(Cu)
dc winding loss for copper
2.2080
Pwac
ac winding loss for copper
2.3942
Pw (Cu)
ac-to-dc winding loss for copper
4.6022
Pfe,v
The total magnetic core loss
2.9300
PT
Total inductor power loss
7.5322
Equation (32), the ac winding resistance Rwac can then be
obtained as 2.3942 W. The total loss Pw(Cu) of the ac-to-dc winding is 4.6022 W, then the total power loss for copper winding
PT(Cu) can be obtained. The core power loss can be calculated
from Equation (34), for which the parameters, kc = 8.4683e-08,
α = 1.8787 and β = 2.5207 are constant parameters provided
by the core manufacturer [33].
Using the core material parameters with Equations (35) and
(36) yields a core power density Pfe,p of 242 mW/cm3 and a magnetic core loss Pfe,v of 2.93 W. The total inductor power loss, PT,
is 7.5322 W. All the power losses calculated are listed in Table 4.
4.2
Analysis steps and results of FEM
simulation
4.2.1
Steps of FEM software
In this study, Comsol Multiphysics software was chosen for the
simulation. First, CAD software Solidworks is used to draw five
models. The steps involved are introduced below:
The first step-Geometry: (a) Link CAD software Solidworks figures to Comsol Multiphysics software, add the 3D
PQ3530 core into the "Geometry". (b) Define the "core"
domain and "coil" domain in this case. (c) Build a "cylinder" in
Geometry, and put the PQ3530 core in the cylinder. The added
cylinder will be filled with the air in the material setup section.
(d) Form a union of all objects in the Geometry section [38, 39].
The second step-Material: (a) Add the materials from the
material library [38-40]. (b) In the proposed model, domains are
used to assign materials to the objects. (c) The air is filled with
the air-gaps and cylinder in this paper. (d) PQ3530 core are ferrite or Sendust materials, and the coil is cooper material. (e) Add
the thermal parameters in the material blocks. (f) The detailed
parameters of the DMEGC ferrite cores, DMR95 material, and
Sendust 60 core material are listed in Table 6 [36].
The third step-Physics interface: (a) FEM software Comsol
Multiphysics is widely used by many institutes in recent years. (b)
Using "AC/DC module" to predict the magnetic fields is very
common [39]. (c) This software module can simulate the 1D, 2D
and 3-dimensions; the passive and active devices can be modelled on Maxwell's equations [39]. (d) Ampère's Law, Magnetic
Insulation and Initial Values are automatically added under the
interface to define the basic principle and equations to compute
the magnetic field [38, 39]. (e) Add the option "coil" and Geometry analysis shows the input and output boundary domain. (f)
 20513305, 2022, 1, Downloaded from https://ietresearch.onlinelibrary.wiley.com/doi/10.1049/tje2.12087, Wiley Online Library on [22/07/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

## [стр. 10]

LIAO AND CHEN
25
TABLE 5
Mesh quality of different types for proposed models
Model
Element type
Number of
mesh
Element
quality
Type I
Triangle
168,414
0.9700
Tetrahedron
847,199
0.8077
Type II-FE
Triangle
169,669
0.9697
Tetrahedron
855,150
0.8080
Type II-SE
Triangle
171,761
0.9700
Tetrahedron
869,510
0.8086
Type III-SE
Triangle
174,533
0.9700
Tetrahedron
883,896
0.8093
Type III-FE
Triangle
174,557
0.9699
Tetrahedron
884,911
0.8086
Submit 5 A as the coil current in this case. In this case, add
the thermal FEM simulation step after the magnetic field simulation. (g) Establish a new physics interface-"heat transfer in
solids". (h) Add the options of inflow heat flux and outflow
heat flux. (i) Set the surface of the inflow and outflow. (j) The
heat source is set at the heat consumption rate Po = 500 W,
V = 390 V, and Qo = 1.28. (k) Must set the "thermoelectromagnetics" of "multiple physical interfaces".
The fourth step-Mesh built: (a) After defining the physics
interface for the model, the next step in the process is mesh
creation [40]. (b) The geometric model is divided into thousands of tiny finite elements, which can be in different shapes.
(c) Select "physics-controlled mesh" and the element size is
"Fine".
The fifth step- Study: (a) Because of the proposed inductor
with a coil in the simulation, selecting "coil geometry analysis"
is crucial and required for computing the coil current. (b) In this
section, "stationary" step is the automatic function to calculate
the formula.
The sixth step-Result: (a) The magnetic field and the fringing flux are shown in the file. (b) The figures or data can be
downloaded. (c) The results of this paper are shown in the
manuscript.
4.2.2
The importance of the mesh independent
In 3D FEM models, mesh independent study is crucial. Comsol Multiphysics software is used to build the different element
types of the mesh. Two different element types are used for
segmentation, and the number of mesh are varying due to different segmentation shapes. In order to find the suitability of
mesh cutting, an independent mesh analysis is carried out. The
mesh quality of different element types is shown in Table 5.
The different element types of five models in the mesh statistics,
the number of mesh and the element quality can be observed.
Therefore, triangle mesh cutting is more suitable since the
element quality can reach almost 0.9700 in the simulation
part.
TABLE 6
Material parameters of COMSOL models [36]
Material
Relative
permeability
(μ)
Specific heat
Cp [J/(kg*k)]
Thermal
conductivity k
(J/mm S K]
Approximate
density
ρ(g/cm3)
Air
1
1005
2.6*10-3
1.225
Ferrite
3300
600
9.5*10-3
4.8
Sendust
60
623
9.2*10-3
1.622
FIGURE 9
The fringing flux simulations of type I model
4.2.3
The magnetic field results of the
simulations
The five types of different air-gap arrangements are computed
under the same conditions with FEM simulation software.
Detailed parameters of the DMEGC ferrite cores, DMR95
material, and Sendust 60 core material are listed in Table 6 [36].
Type I is the fringing flux simulation analysis for the conventional one air-gap inductor shown in Figure 9. The maximum
fringing flux is 0.428 T. Figure 10 represents the analysis for
type II-FE inductor with one ferrite core at the center-pole
resulting in two air-gaps. The maximum fringing flux is 0.387 T.
Figure 11 shows the analysis of type II-SE inductor consisting
Sendust core at the center-pole with two air-gaps. The maximum fringing flux is 0.359 T. Figure 12 is the type III-SE
inductor simulation with three air-gaps using two Sendust cores
at the center-pole. The maximum fringing flux is 0.383 T. The
type III-FE inductor simulation consists of two ferrite cores at
the center-pole with three air-gaps. The maximum fringing flux
is 0.438 T, as shown in Figure 13.
According to the simulation figures, Sendust material is better than ferrite core in minimizing losses. Moreover, the multiple air-gap arrangements appear to be better than the single
air-gap application. Furthermore, the multiple air-gap inductor
FIGURE 10
The fringing flux simulations of type II-FE model
 20513305, 2022, 1, Downloaded from https://ietresearch.onlinelibrary.wiley.com/doi/10.1049/tje2.12087, Wiley Online Library on [22/07/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

## [стр. 11]

26
LIAO AND CHEN
FIGURE 11
The fringing flux simulations of type II-SE model
FIGURE 12
The fringing flux simulations of type III-SE model
with same air gap lengths is also better than the multi-air-gap
inductor with different air gap lengths. Using five air-gaps with
Sendust cores as an example for simulation, the maximum fringing flux of the model with different air-gap lengths is 0.219 T,
and the maximum fringing flux of the model with same air-gap
lengths is 0.185 T. This is shown in Figure 14. For the simulation
in this research, the leakage flux value is about 0.02 T, and the
fringing flux value is about 0.2 T. The leakage flux value is much
smaller than fringing flux value. Therefore, the leakage flux can
be neglected in this study.
The magnetic flux densities along with the path from A1 to
A2 for each air-gap arrangement are represented in Figure 15.
The higher edge flux values are distributed at the edge of the
center-pole. The fringing flux values of path A1 to A2 measured
with type I model has the highest value of 0.22 T. Type II-FE and
II-SE models are the second highest with 0.2 T and type III-SE
and III-FE models are the lowest with 0.17 T.
FIGURE 13
The fringing flux simulations of type III-FE model
FIGURE 14
The multiple air-gaps arrangement simulation (a) model
with different air-gap lengths (b) model with same air-gap length
-10
-5
0
5
10
0.00
0.05
0.10
0.15
0.20
0.25
A1
B(T)
A2
Distance x(mm)
Type I
Type II-FE
Type II-SE
Type III-SE
Type III-FE
FIGURE 15
The magnetic flux distribution along the A1 to A2 paths for
different arrangements of air-gaps
4.2.4
The thermal results of the simulations
The thermal FEM simulation results are shown below. The simulated conditions are set as the actual detection temperature
experiment environment. The input voltage is 115V/60 Hz, the
rated power is 500 W, the ambient temperature is 26°C, and
place the PFC circuit for 20 min then do the practical experiments.
 20513305, 2022, 1, Downloaded from https://ietresearch.onlinelibrary.wiley.com/doi/10.1049/tje2.12087, Wiley Online Library on [22/07/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

## [стр. 12]

LIAO AND CHEN
27
FIGURE 16
(a) The thermal simulation of type I model, (b) the thermal simulations of type II-FE model, (c) the thermal simulations of type II-SE model, (d)
the thermal simulations of type III-SE model, (e) the thermal simulations of type II-FE model
Follow the above FEM simulation steps to obtain the temperature result of the five proposed models. The figures show
the equipotential line and the distribution of temperature. Figure 16a shows the Type I core; the highest temperate is 74.6°C
of PQ3530 core with one air-gap. Figure 16b shows the Type
II-FE core; the highest temperate is 67.6°C of PQ3530 core
with two air- gaps. Figure 16c shows the Type II-SE core; the
highest temperate is 64.3 °C of PQ3530 core with two air-gaps.
Figure 16d shows the Type III-SE core, the highest temperate is
61.8°C of PQ3530 core with two air-gaps. Figure 16e shows the
Type III-FE core, the highest temperate is 65.1°C of PQ3530
core with two air-gaps. It can be observed that the heats are
distributed near the middle of the air-gaps of all type cores.
The maximum and minimum temperatures of the five thermal
models are in Table 7.
4.3
Fringing flux factor calculation
The core at the center pole with one single circular shaped airgap is considered for the PQ3530 core. Figure 17 shows a magnetic equivalent circuit for an inductor with one air-gap and the
fringing flux associated. The ratio of the cross-sectional area's
mean width and the mean magnetic path length of the fringing
 20513305, 2022, 1, Downloaded from https://ietresearch.onlinelibrary.wiley.com/doi/10.1049/tje2.12087, Wiley Online Library on [22/07/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

## [стр. 13]

28
LIAO AND CHEN
TABLE 7
Temperatures of five thermal models
Model
Max. temperature
Min. temperature
Type I
74.6 °C
26.8 °C
Type II-FE
67.6 °C
21.7 °C
Type II-SE
64.3 °C
21.6 °C
Type III-SE
61.8 °C
21.6 °C
Type III-FE
65.1 °C
21.7 °C
FIGURE 17
An equivalent circuit of fringing flux distribution
flux to the air-gap length are defined as [41]
𝛼=
w fr
lg
,
(37)
𝛽=
l fr
lg
,
(38)
where wfr is the mean width of the fringing flux, lfr is the mean
MPL of the fringing flux, lg is the length of the air-gap.
The fringing flux factor (Ffr) for the circular air-gap [41] is
Ffr = 1 +
A fr
A fe
lg
l fr
.
(39)
Substituting Equations (37) and (38) into Equation (39), Ffr
can be derived from Equation (40)
Ffr = 1 +
4𝛼⋅l g(DCP + 𝛼⋅lg)
𝛽⋅DCP
2
,
(40)
where Dcp is the diameter of the center-pole. The fringing flux
factor values can be obtained by Equations (20), (21), and (40)
as shown in Table 8. These values are calculated from three
different formulas. Therefore, the calculated values would be
different because of the different methods used. However, it is
difficult to determine the factors α and β in practical experience.
TABLE 8
Fringing flux factor value for five types cores
Factor∖type
I
II-FE
II-SE
III-SE
III-FE
Ff
1.41
1.26
1.18
1.14
1.17
Ff'
1.37
1.24
1.16
1.13
1.15
Ffr
1.34
1.14
1.08
1.06
1.07
FIGURE 18
Magnetic saturation current of type II-SE model, at 519.76
W, 90 Vac/47 Hz (Ch2: output voltage, VO = 397 V; Ch4: inductor current,
iL = 6.51 A)
4.4
Saturation current of the high-frequency
inductor
Another important consideration is the saturation current level
of the inductor. It means that all inductance must operate within
a safe range or less than the saturation current value to ensure
the circuit functions correctly. The inductances of all five types
of high-frequency inductors are defined as a nominal value and
the tolerance in the analysed case is L = 440 μH ± 7 %.
Type II-SE model reached the magnetic core saturation when
the inductor current iL reached 6.51 A at about 519.76 W, which
was the best performance out of all models. Type III-FE model
showing the worst performance with the magnetic saturation
occurs when the inductor current iL reached 5.47 A at about
439.25 W. Figures 18 and 19 show the measured magnetic saturation current iL of the PFC circuit for type II-SE and III-FE
models at an input of 90 Vac/47 Hz.
The experimental results show that using the inductor with
the PQ3530 ferrite core as the main body and one or two pieces'
ferrite core at the center-pole, the number of air-gaps does not
change the saturation current value. However, substituting ferrite cores with the low relative permeability Sendust made cores
to the center-pole of the multiple air gap models can increase
its saturation current value by about 6-9%, when compared to
type I (an air-gap) inductor.
The results of the measured current saturation and power
of the PFC circuit are listed in Table 9. The saturation current
of Type II-SE and type III-SE inductors are 6.51 A and 6.4 A,
respectively, with the power reaching 519.76 W for type II-SE
and 510.00 W for type III-SE. As such, according to the actual
application needs, type II-FE and type III-FE models can reach
 20513305, 2022, 1, Downloaded from https://ietresearch.onlinelibrary.wiley.com/doi/10.1049/tje2.12087, Wiley Online Library on [22/07/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

## [стр. 14]

LIAO AND CHEN
29
FIGURE 19
Magnetic saturation current of type III-FE model, at 439.25
W, 90 Vac/47 Hz (Ch2: output voltage, VO = 400 V; Ch4: inductor current,
iL = 5.47 A)
TABLE 9
Comparison of the saturation current of the PFC circuit using
the inductors with five different air-gap arrangements
Type
Number of
air-gaps
Saturation
current
Saturation power
(W)
I
1 air-gap
5.99 A
478.37
II-FE
2 air-gaps
5.85 A
468.86
II-SE
2 air-gaps
6.51 A
519.76
III-SE
3 air-gaps
6.40 A
510.00
III-FE
3 air-gaps
5.47 A
439.25
the 500 W requirement. However, the inductor currents of types
I, II-FE, and III-FE operate from 5.47 A to 5.99 A, causing overcurrent saturation of the inductor current. This means that types
I, II-FE, and III-FE cannot meet the product design requirements of operation power limit at 500 W.
4.5
The efficiency of PFC converter circuit
The parameter assumptions of the circuit are the same as the
experiment setup. The design specifications for the boost PFC
circuit are listed in Table 10.
Figures 20a-d show the efficiency curves for the boost PFC
converter circuits with different inductor types in the 500 W
prototype with input voltages of 90 Vac, 115 Vac, 230 Vac, and
264 Vac. The average efficiency values of the PFC circuits at 500
TABLE 10
Design specifications for the power stage circuit
Symbol
Description
Value
Vac,rms
Universal mains voltage
90 V to 264 V
fline
Line frequency
47 Hz to 63 Hz
Vo
Output voltage
390 V
Po
Output power
500 W
fsw
Switching frequency
65 kHz
TABLE 11
Average efficiencies of the PFC converter circuit at 500 W
Vin/Hz
Type I
Type
II-FE
Type
II-SE
Type
III-SE
Type
III-FE
90/47
91.18%
91.33%
91.30%
91.08%
91.23%
115/60
93.66%
93.92%
93.76%
93.77%
93.73%
230/50
96.67%
96.78%
96.63%
96.80%
96.68%
264/63
96.95%
97.08%
96.87%
97.03%
96.94%
TABLE 12
Inductor power loss at input 90 Vac/47 Hz
Operating watt
Power loss value
50 W
638 mW
100 W
1.554 W
150 W
2.723 W
200 W
3.350 W
250 W
4.422 W
300 W
4.759 W
350 W
5.236 W
400 W
5.836 W
450 W
6.760 W
500 W
7.867 W
W are presented in Table 11. Figure 20c shows the input voltage for the measuring curves set at 115 Vac/60 Hz, the average efficiency of the type III-FE inductor shows the best result
with highest efficiency of 95.1% at 250 W. The circuit efficiency
of the five different types of cores with input voltage of 230
Vac/50 Hz, 500 W is shown in Figure 20d. The highest efficiency attained is 97.67 %.
4.6
Prototype of two-stage converter and
experimental results
Based on the above comparison and analysis, the proposed
methodology is verified, and it is better than the available
methodology. According to the saturation current performance,
type II-SE inductor is selected as the choke inductor of the
boost PFC converter. The image of the prototype is shown in
Figure 21. Its entire power supply consists of a boost PFC converter and an LLC converter.
The experimental results show the proposed design methodology for the type II-SE inductor in the boost PFC converter according to the design specification. The inductor's
power loss values are presented in Table 12. The results
were obtained using Tektronix oscilloscope, MSO46-4-BW500, with DPOPWR software to measure the inductor power
losses of 500 W application for every 50 W at input
90 Vac/ 47 Hz.
The proposed 500 W boost PFC converter requires to do the
IEC 61000-3-2 Class-D harmonic experiment. The test specification of Europe - Class D is verified by MODEL 6630 - the
 20513305, 2022, 1, Downloaded from https://ietresearch.onlinelibrary.wiley.com/doi/10.1049/tje2.12087, Wiley Online Library on [22/07/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

## [стр. 15]

30
LIAO AND CHEN
0
100
200
300
400
500
91.0
92.0
93.0
94.0
Watts
Efficiency
(%)
Efficiency vs. Output Power for Five Types at 90 Vac
Type I
Type II-FE
Type II-SE
Type III-SE
Type III-FE
0
100
200
300
400
500
92.0
93.0
94.0
95.0
Watts
Efficiency
(%)
Efficiency vs. Output Power for Five Types at 115 Vac
Type I
Type II-FE
Type II-SE
Type III-SE
Type III-FE
(a)
(c)
(b)
(d)
Watts
Efficiency
(%)
Efficiency vs. Output Power for Five Types at 230 Vac
0
100
200
300
400
500
93.0
94.0
95.0
96.0
97.0
Type I
Type II-FE
Type II-SE
Type III-SE
Type III-FE
Watts
Efficiency
(%)
Efficiency vs. Output Power for Five Types at 264 Vac
0
100
200
300
400
500
93.0
94.0
95.0
96.0
97.0
Type I
Type II-FE
Type II-SE
Type III-SE
Type III-FE
FIGURE 20
(a) The efficiency of the PFC circuit using the five types at input 90 Vac/47 Hz. (b) The efficiency of the PFC circuit using the five types at input
115 Vac/60 Hz. (c) The efficiency of the PFC circuit using the five types at input 230 Vac/50 Hz. (d) The efficiency of the PFC circuit using the five types at input
264 Vac/63 Hz
FIGURE 21
Photograph of the two-stage converter prototype
Power Analyzer of Chroma Co., Ltd to perform the harmonic
variation experiments. Taking 230 V/50 Hz as an example, the
proposed five boost inductor models experiment are shown as
below.
FIGURE 22
Bar graph of harmonic experiment data
The harmonic test data is organized to obtain Figure 22.
It can be observed that the harmonic order 11 is the most
influential of the type II-FE, type II-SE, and type III-FE. In
the five models, type II-FE is the smallest THD, and type I is
 20513305, 2022, 1, Downloaded from https://ietresearch.onlinelibrary.wiley.com/doi/10.1049/tje2.12087, Wiley Online Library on [22/07/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

## [стр. 16]

LIAO AND CHEN
31
TABLE 13
Thermal experiments of 115 V/60 Hz PFC circuit at 500 W
Model
Temperature of core
Temperature of coil
Type I
core
coil
64.8 °C
67.5 °C
Type II-FE
core
coil
60.6 °C
67.6 °C
Type II-SE
core
coil
60.2 °C
64.1 °C
Type III-SE
core
coil
60.3 °C
62.4 °C
Type III-FE
core
coil
58.1 °C
63.0 °C
the largest one. The specification for harmonic experiment is
230 V/50 Hz. All the proposed type core is passed in the harmonic test.
4.7
The thermal experiment of PFC
converter circuit
The power losses would cause the temperature to increase
which affect the efficiency. The thermal conditions set that the
input specification is 115V/60 Hz, the rated power is 500 W,
ambient temperature is 26°C, and the PFC circuit is placed for
20 min, then the practical experiments are done. Equipment of
visual IR thermometer, testing results are in Table 13.
5
CONCLUSION
In this study, finding the combination of different air-gaps and
material arrangement of the center-pole used in the limited bobbin space is the main objective. The saturation current capacity
of the boost inductor can be improved within a fixed mechanical dimension. The design process and related equations for
saturation current capacity improvement were addressed in
detail.
The inductors with different air-gaps placements and material configurations are compared in this study. The analytical
equations, FEA simulation results, and measurements verify the
proposed design process works as expected and provide more
detail than references [8]. Comsol Multiphysics software is used
to perform the magnetic distribution simulations. The 3D FEM
models offer an analytical approach to confirm the flux distributions and fringing flux. Based on the comparison of FEM simulation and actual measurement results, type II-SE inductor was
better than type I inductor. Finally, choosing type II-SE, the two
air-gaps and the center-pole made by low relative permeability
material (Sendust) inductor, to do the practical experiment. The
boost PFC converter prototype of a two-stage AC/DC power
supply is also implemented. The contributions in this paper are
as follows.
1. Improve the high-frequency inductor design process with
different materials and multiple air-gaps in dimension limitations.
2. Promote the saturation current capacity for the gapped magnetic components.
3. Use Comsol Multiphysics software to simulate the magnetic
flux and fringing flux.
4. Compare the calculated power losses with experimental
results for a 500W boost PFC converter.
5. The design process can be applied to AC/DC products,
which can replace the suitable air-gap inductor rapidly.
6. The proposed idea of this research is that when the product is required to be updated and republished, the size of
the mechanism cannot be replaced because of the cost. The
main contribution is that it is not necessary to use Sendust
ring core; just replace the different materials of the centerpole core and the different number of air-gaps instead of the
whole boost inductor. It is unnecessary to use Sendust ring
core which can save cost and dimension place.
ACKNOWLEDGEMENTS
This study is supported by the Delta Electronics Foundation,
and it was financially supported by The Featured Areas Research
Center Program within the framework of the Higher Education Sprout Project by the Ministry of Education (MOE) in Taiwan, and the Ministry of Science and Technology under Project
MOST 110-2221-E-006-125, MOST 110-2634-F-006-017.
CONFLICT OF INTEREST
The authors declare no conflict of interest.
DATA AVAILABILITY STATEMENT
The data that support the findings of this study are available on
request from the corresponding author. The data are not publicly available due to privacy or ethical restrictions.
REFERENCES
1. Electromagnetic Compatibility (EMC): Part 3-2: Limits - Limits for Harmonic Current Emissions (Equipment Input Current ≤16 A per phase).
Int. Std. IEC 61000-3-2, (2018)
 20513305, 2022, 1, Downloaded from https://ietresearch.onlinelibrary.wiley.com/doi/10.1049/tje2.12087, Wiley Online Library on [22/07/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

## [стр. 17]

32
LIAO AND CHEN
2. Li, M.Y., Chen, M., Zhai, J.Y., et al.: Analysis and calculation of the
loss of high-frequency inductor. Power Electron. Technol. 41(9), 47-49
(2007)
3. Jez, R.: Influence of the distributed air gap on the parameters of an industrial inductor. IEEE Trans. Magnetic 53(11), 1-5 (2017)
4. Ayachit, A., Reatti, A., Kazimierczuk, M.K.: Magnetising inductance of
multiple-output flyback dc-dc convertor for discontinuous-conduction
mode. IET Power Electron. 10(4), 451-461 (2016)
5. Kazimierczuk, M.K.: High-Frequency Magnetic Components, 2nd ed.
Wiley, NewYork (2014)
6. Ayachit, A., Kazimierczuk, M.K.: Steinmetz equation for gapped magnetic
cores. IEEE Magnetic Lett. 7, 1302704 (2016)
7. Saini, D.K., Ayachit, A., Reatti, A., et al.: Analysis and design of choke
inductors for switched-mode power inverters. IEEE Trans. Ind. Electron.
65(3), 2234-2244, (2018)
8. Dae, Y.U., Gwan, S.P.: Resistance variations in high-frequency inductors
considering induced fields among conductors. IEEE Trans. Magnet. 57(2),
1-5 (2021)
9. Igarashi, H.: Semi-analytical approach for finite element analysis of multiturn coil considering skin and proximity effects. IEEE Trans. Magnet.
53(1), 1-7 (2017)
10. Jez, R., Polit, A.: Influence of air-gap length and cross-section on magnetic
circuit parameters. In: COMSOL Conference in Cambridge. COMSOL,
Burlington (2014)
11. Agamy, M.S., Jain, P.K.: A three-level resonant single-stage power factor
correction converter: Analysis, design, and implementation. IEEE Trans.
Ind. Electron. 56(6), 2095-2107 (2009)
12. Liu, Y.M., Chang, L.K.: Single-stage soft-switching ac-dc converter with
input-current shaping for universal line applications. IEEE Trans. Ind.
Electron. 56(2), 467-479 (2009)
13. Azcondo, F.J., Castro, A.D., Lopez, V.M., et al.: Power factor correction
without current sensor based on digital current rebuilding. IEEE Trans.
Power Electron. 25(6), 1527-1536 (2010)
14. Athab, H.S., Lu, D.D.C.: A high-efficiency ac/dc converter with quasiactive power factor correction. IEEE Trans. Power Electron. 25(5), 11031109 (2010)
15. Nussbaumer, T., Raggl, K., Kolar, J.W.: Design guidelines for interleaved
single-phase boost PFC circuits. IEEE Trans. Ind. Electron. 56(7), 25592573 (2009)
16. Hwu, K.I., Yau, Y.T.: An interleaved AC-DC converter based on current
tracking. IEEE Trans. Ind. Electron. 56(5), 1456-1463 (2009)
17. Zhang, J., Lu, D.D.C., Sun, T.: Flyback-based single-stage power-factorcorrection scheme with time-multiplexing control. IEEE Trans. Ind. Electron. 57(3), 1041-1049 (2010)
18. Lu, D.D.C., Iu, H.H.C., Pjevalica, V.: Single-stage AC/DC boost-forward
converter with high power factor and regulated bus and output voltages.
IEEE Trans. Ind. Electron. 56(6), 2128-2132 (2009)
19. Raggl, K., Nussbaumer, T., Doerig, G., et al.: Comprehensive design
and optimization of a high-power-density single-phase boost PFC. IEEE
Trans. Ind. Electron. 56(7), 2574-2587 (2009)
20. ANSI/EIA RS-310, Racks, Panels, and Associated Equipment (2007)
21. Liao, H., Wang, S.P., Chen, J.F., et al.: Analysis and implementation of boost
PFC with different cores. In: IEEE 7th World Conference on Photovoltaic
Energy Conversion (WCPEC). IEEE, Piscataway (2018)
22. Robert, D.C.: Concepts and Applications of Finite Element Analysis, 4th
ed. Wiley, New York (2002)
23. Robert, D.C.: Finite Element Modeling for Stress Analysis. Wiley, New
York (1995)
24. Valchev, V.C., Bossche, A.V.D.: Inductors and Transformers for Power
Electronics. CRC Press, Boca Raton (2005)
25. Hurley, W.G., Wölfle, W.H.: Transformers and Inductors for Power Electronics: Theory, Design and Applications. Wiley-Blackwell, Hoboken
(2013)
26. McLyman, C.W.T.: Transformer and Inductor Design Handbook, 4th ed.
CRC Press, Boca Raton (2011)
27. Hurley, W.G., Gath, E., Breslin, J.G.: Optimizing the AC resistance of
multilayer transformer windings with arbitrary current waveforms. IEEE
Trans. Power Electron. 15(2), 369-376, (2000)
28. Wojda, R.P., Kazimierczuk, M.K.: Analytical optimization of solid-roundwire windings. IEEE Trans. Ind. Electron. 60(3), 1033-1041, (2013)
29. Wojda, R.P., Kazimierczuk, M.K.: Winding Resistance and power of Inductors with Litz and Solid-Round Wires. IEEE Trans. Ind. Electron. 60(3),
1033-1041 (2017)
30. Kondrath, N., Kazimierczuk, M.K.: Inductor winding loss owing to skin
and proximity effects including harmonics in non-isolated pulse width
modulated dc-dc converters operating in continuous conduction mode.
IET Power Electron. 3(6), 989-1000 (2010)
31. Dowell, P.L.: Effects of eddy currents in transformer windings. Proc. Inst.
Electr. Eng. 113(8), 1387-1394 (1966)
32. Mulder, S.A.: Fit Formulae for power loss in ferrites and their use in transformer design. In: Proceedings of Power Conversion Conference, pp. 345359. IEEE, Piscataway (1993)
33. ASTM International: ASTM B258-14 Standard Specification for Standard
Nominal Diameters and Cross-sectional Areas of AWG Sizes of Solid
Round Wires Used as Electrical Conductors (2015)
34. Holguín, F.A., Asensi, R., Prieto, R., Cobos, J.A., Simple analytical
approach for the calculation of winding resistance in gapped magnetic
components. In: 2014 IEEE Applied Power Electronics Conference and
Exposition (APEC), pp. 2609-2614. IEEE, Piscataway (2014)
35. Dowell, P.L.: Effects of eddy currents in transformer winding. Proc. IEE
113(8), 1387-1394 (1966)
36. DMEGC material characteristics of magnetic components (Mn-Zn Ferrite
Power Core), Hengdian Group DMEGC Magnetics Co., Ltd (2018)
37. DPG10-1000B Datasheet of the Power Choke Tester. ed-k Electronic
Development, Planeg (2017)
38. Mammadov, J.,: Models of Simple Iron Cored Electromagnets. In: COMSOL Conference in Cambridge. COMSOL, Burlington (2014)
39. COMSOL Multiphysics: The AC/DC Module. Version: COMSOL 4.3
(2012)
40. Griesmer, A.: Size parameters of Free Tetrahedral Meshing in Comsol Multiphysics. Comsol Blog. 30 (2014)
41. Snelling, E.C.: Soft Ferrites: Properties and Applications, 2nd ed. Butterworth, London, Boston (1988)
How to cite this article: Liao, H., Chen, J.-.F.: Design
process of high-frequency inductor with multiple
air-gaps in the dimensional limitation. J. Eng. 2022,
16-33 (2022). https://doi.org/10.1049/tje2.12087
APPENDIX
In order to derive inductance from the PFC topology, the boost
inductor L can be calculated according to the following equations [7]. Assuming the boost PFC converter efficiency is η, the
minimum input ac voltage is Vac,min, the output voltage is Vo,
the maximum duty ratio Dmax is the boost switching control at
the peak of line voltage which are given as
Dmax =
VO -
√
2Vac,min
VO
.
(A1)
A first approximation of boost inductor L can be obtained
with the following equation,
L =
𝜂DmaxVac,min
2
KRipple fswPO
,
(A2)
where fsw is operating frequency; KRipple is current ripple factor.
 20513305, 2022, 1, Downloaded from https://ietresearch.onlinelibrary.wiley.com/doi/10.1049/tje2.12087, Wiley Online Library on [22/07/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

## [стр. 18]

LIAO AND CHEN
33
The peak of boost inductor current over one switching cycle
at the peak of the line voltage for the low line is given as
IL,pk =
√
2PO
𝜂Vac,min
.
(A3)
Use the following equations to calculate the required number
of turns N, the number of strands Sn, and the bare wire area for
strands Aws(AWG#NO.).
N =
WaKu
SnAws(AWG#NO.)
,
(A4)
where Wa is the window area of the bobbin. The strands number is
Sn =
Aw(B)
Aws(AWG#No.)
,
(A5)
where Aw(B) is required bare wire area.
The bare wire area that handles the specified maximum current density Jm is
Aw(B) = Irms
Jm
(A6)
 20513305, 2022, 1, Downloaded from https://ietresearch.onlinelibrary.wiley.com/doi/10.1049/tje2.12087, Wiley Online Library on [22/07/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
