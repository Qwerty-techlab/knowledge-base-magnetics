# source

<!-- FORMULA-WARNING -->
> **Формулы в этом файле недостоверны.** Текстовый слой PDF теряет дробные черты, радикалы и группировку степеней; знак интеграла приходит как `Z` или `R`, знак суммы -- как `P`. Формул вырезано: **22**, читать их в `formulas/` (картинки 300 dpi, перечень в `formulas/INDEX.md`).
<!-- /FORMULA-WARNING -->

> Автоматически извлечено из `source.pdf` скриптом `parse_pdf.py`
> Движок: pymupdf. Страниц: 13 из 13.
> Дата извлечения: 2026-08-07 06:43 UTC

Текст не редактировался. Формулы и таблицы могут быть искажены —
при сомнении сверяться с исходным PDF.

---

## [стр. 1]

Aalborg Universitet
Parasitic Capacitance Modeling of Copper-Foiled Medium-Voltage Filter Inductors
Considering Fringe Electrical Field
Zhao, Hongbo; Huang, Zhizhao; Dalal, Dipen Narendra; Jørgensen, Jannick Kjær;
Jørgensen, Asger Bjørn; Wang, Xiongfei; Munk-Nielsen, Stig
Published in:
IEEE Transactions on Power Electronics
DOI (link to publication from Publisher):
10.1109/TPEL.2020.3048226
Publication date:
2021
Document Version
Accepted author manuscript, peer reviewed version
Link to publication from Aalborg University
Citation for published version (APA):
Zhao, H., Huang, Z., Dalal, D. N., Jørgensen, J. K., Jørgensen, A. B., Wang, X., & Munk-Nielsen, S. (2021).
Parasitic Capacitance Modeling of Copper-Foiled Medium-Voltage Filter Inductors Considering Fringe Electrical
Field. IEEE Transactions on Power Electronics , 36(7), 8181-8192. Article 9311400.
https://doi.org/10.1109/TPEL.2020.3048226
General rights
Copyright and moral rights for the publications made accessible in the public portal are retained by the authors and/or other copyright owners
and it is a condition of accessing publications that users recognise and abide by the legal requirements associated with these rights.
            - Users may download and print one copy of any publication from the public portal for the purpose of private study or research.
            - You may not further distribute the material or use it for any profit-making activity or commercial gain
            - You may freely distribute the URL identifying the publication in the public portal -
Take down policy
If you believe that this document breaches copyright please contact us at vbn@aub.aau.dk providing details, and we will remove access to
the work immediately and investigate your claim.
Downloaded from vbn.aau.dk on: июля 30, 2026

## [стр. 2]

0885-8993 (c) 2020 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission. See http://www.ieee.org/publications_standards/publications/rights/index.html for more information.
This article has been accepted for publication in a future issue of this journal, but has not been fully edited. Content may change prior to final publication. Citation information: DOI 10.1109/TPEL.2020.3048226, IEEE
Transactions on Power Electronics
IEEE POWER ELECTRONICS REGULAR PAPER/LETTER/CORRESPONDENCE
Parasitic Capacitance Modeling of Copper-Foiled
Medium-Voltage Filter Inductors Considering
Fringe Electrical Field

Hongbo Zhao, Student Member, IEEE, Zhizhao Huang, Dipen Narendra Dalal, Student Member, IEEE, Jannick Kjær
Jørgensen, Asger Bjørn Jørgensen, Xiongfei Wang, Senior Member, IEEE, and Stig Munk-Nielsen, Member, IEEE,


Abstract- This paper characterizes three parasitic capacitances
in copper-foiled medium-voltage inductors. It is found that the
conventional modeling method overlooks the effect of the fringe
field,
which
leads to inaccurate
modeling
of
parasitic
capacitances in copper-foiled inductors. To address this problem,
the parasitic capacitances contributed by the fringe electrical
field is identified first, and a physics-based analytical modeling
method for the parasitic capacitances contributed by the fringe
electrical field is proposed, which avoids using any empirical
equations. The total parasitic capacitances are then derived for
three different cases with three different core potentials, from
which a three-terminal equivalent circuit is derived, and thus, the
parasitic capacitances in copper-foiled inductors are explicitly
identified. The calculated results show a close agreement with the
measured capacitance by using an impedance analyzer. Two
recommendations for reducing the parasitic capacitances in
copper-foiled inductors are given in this paper.

Index terms- Parasitic capacitance, copper-foiled, mediumvoltage, filter inductor, fringe field, physics-based modeling.
I.  INTRODUCTION
Thanks to the advances in the power semiconductor
devices, the wide-band-gap (WBG) transistors are widely used
in modern power conversion systems [1], where the power
converters can be designed with higher switching frequency
and less switching losses [2], [3]. Yet, the high dv/dt problem
becomes more significant during the switching transitions of
WBG transistors [4]. Under the high dv/dt conditions, the
parasitic
capacitances
of
passive
and
active
power
components, such as the common-mode capacitance of gate
drivers [5], [6], the ground capacitance of heatsink [7], the
parasitic capacitance in power modules [8], [9], and the
parasitic capacitance in transformers [10-12] and inductors
[13-15], can bring large common-/differential-mode current
into the converter circuit [13], causing electromagnetic
interferences [4] and accelerating the aging of power
components [16]. It is also reported that the parasitic
capacitances in medium voltage (MV) inductors are larger
than them in low voltage inductors due to the required higher
inductance and extra insulation [13].
The windings of inductors are commonly constructed with
round cables for a low cost. Yet, in high-frequency
applications, both the copper foil and the litz wire are
commonly used for a lower ac-resistance [17], and the copperfoil is more popular in high-voltage and high-power
applications [17-20], due to its higher power density and more
flexibility than round cables and Litz wires in the
manufacturing
process.
However,
the
intra-winding
capacitance of the copper-foiled inductors and transformers is
large due to the extensive interleaving of the windings [17],
which is not desirable in applications with high dv/dt
operations. Therefore, it is important to characterize and
reduce the parasitic capacitances in copper-foiled filter
inductors, especially when they are used in the converters
based on WBG devices.
A few works have been reported on modeling the parasitic
capacitance of copper-foiled magnetic components [17], [20],
[21]. Basically, the parasitic capacitance in magnetic devices
is divided into static capacitance and dynamical capacitance.
1) Static capacitance [21], [22]. It represents the
capacitance between two planes when disconnected,
where there is no ohmic voltage drop on each plane.
Therefore, the static capacitance is merely dependent
on the geometrical structure and material information
of the two planes.
2) Dynamical capacitance [21], [22]. This capacitance
represents the total electrical field energy stored
between any two planes, which is related to the voltage
potential distribution. In practice, the voltage potential
on each plane is not a constant value, due to the current
flows through the winding, which results in ohmic
voltage drops in the windings. The dynamical
capacitance can be calculated by the static capacitance
and dynamical voltage potential distribution.
In [17], the parasitic capacitance of a copper-foil-based
transformer between the primary side and secondary side is
calculated by using the formula of parallel plate capacitance,
which is, however, merely a static capacitance, and thus fails
to capture the dynamical capacitance in practice [14], [21],
[22]. An air-coiled inductor wound by copper foils is modeled
in [20], where the first resonant frequency caused by the intrawinding capacitance is identified, yet the modeling of parasitic
This work is supported by MVolt project, which is co-funded by the Department
of Energy Technology of Aalborg University, Innovation Fund Denmark,
Siemens Gamesa, Vestas Wind System, and KK wind solutions (Corresponding
author: Zhizhao Huang and Xiongfei Wang)
H. Zhao, D. Dalal, J. Jørgensen, A. Jørgensen, X. Wang, and S. Munk-Nielsen,
are with the Department of Energy Technology, Aalborg University, Aalborg,
Denmark (e-mail: hzh@et.aau.dk)
Z. Huang is with the School of Electrical and Electronic Engineering, Huazhong
University of Science and Technology, Wuhan, China.
Authorized licensed use limited to: Aalborg Universitetsbibliotek. Downloaded on January 07,2021 at 09:05:28 UTC from IEEE Xplore.  Restrictions apply.

## [стр. 3]

0885-8993 (c) 2020 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission. See http://www.ieee.org/publications_standards/publications/rights/index.html for more information.
This article has been accepted for publication in a future issue of this journal, but has not been fully edited. Content may change prior to final publication. Citation information: DOI 10.1109/TPEL.2020.3048226, IEEE
Transactions on Power Electronics
IEEE POWER ELECTRONICS REGULAR PAPER/LETTER/CORRESPONDENCE
capacitance is not addressed. In [21], both the static and
dynamical capacitances are calculated, considering the eddy
current effects. However, the core is assumed to be always
floating in this work, where only one equivalent capacitance
can be calculated. An improved modeling method is reported
in [22] to consider the grounding effects of the magnetic core,
yet it is only focused on the round-cable based inductors. As
found later in this paper, the method reported in [22] fails to
characterize the capacitive couplings between the core and
terminals of the copper-foiled inductor, where the fringe field
between the winding and core is significant for modeling the
parasitic capacitance in typical copper-foiled inductors.
In [23], a modeling method is proposed to calculate the
parasitic capacitance of a high-power transformer, where the
fringe electrical field between different sections are considered
by using the empirical equations that are derived from verylarge-system-integration
(VLSI) applications
[24].
The
parasitic capacitance contributed by the fringe field is usually
neglected in most previous modeling methods [10, 12, 14, 20,
25]. The parasitic capacitance introduced by the fringe field
has also been discussed in transmission lines [26], antenna
applications [27], and micro electronics [28]. However, these
empirical equations are actually restricted by the geometrical
structure [24], which is not applicable to model the fringefield capacitance between the winding and core in copperfoiled inductors due to a more complex geometrical structure.
This article thus attempts to fill this gap by first identifying
the fringe electrical field in the copper-foiled medium-voltage
(MV) filter inductors, based on which, a physics-based
modeling method for static and dynamical capacitances is then
proposed. Subsequently, the total capacitance of the filter
inductors is obtained by summing the dynamical capacitance
contributed by the fringe field, the electrical field between the
inner layer and core, the electrical field between windings, and
the electrical field between two adjacent layers. The
theoretical calculations show good agreement with the
measurements of a practical copper-foiled inductor by using
an impedance analyzer.
II.  MV COPPER-FOILED INDUCTORS
An MV copper-foiled inductor (30 mH) is taken as an
example in this study. The MV inductor is designed for a
5kHz 2-level voltage source converter based on SiC
MOSFETs with 4.16 kV line-to-line ac voltage and 6 kV dclink voltage. The insulation level of this inductor is 10 kV, and
the current rating is 8 A (rms). The windings and insulation of
the inductor are constructed by copper- and mylar-foils, which
are arranged in multiple layers. Two U-type amorphous cores
are used for the magnetic loop with an air gap in between.
The schematics of the studied MV copper-foiled inductor
are given in Fig. 1. Fig. 1 (a) shows the front view and Fig.
1(b) gives the cross-section view. Two windings are connected
in parallel for sharing the current. Spacers are used to reduce
the capacitive couplings between the inner layer and core, and
they will be modeled later.
The parameters of the studied MV foil-based inductor are
summarized in Table I, along with the definitions of symbols
used in Fig. 1.
The insulation material is selected as Dupont Mylar A [29].
The material of the bobbin and spacer is Durethan BKV 30 H3
[30], which is based on Polyamide 6 with 30% glassreinforced. The values for the relative permittivity of materials
are listed in Table II, which are identified from the datasheet.
The conductivity of the amorphous core is 130 µΩ/cm,
according to the datasheet [32].
The insulation material is selected as Dupont Mylar A [29].
The material of the bobbin and spacer is Durethan BKV 30 H3
[30], which is based on Polyamide 6 with 30% glassreinforced. The values for the relative permittivity of materials
are listed in Table II, which are identified from the datasheet.
0 mH
(Phot)
30 mH
(Pcold)
Frame/Core
(G)
Copper foil
wc × dc
Mylar foil
wm × dm
w
h
Spacer
Winding 1
Winding 2
Core
Ctt
Ctc1
Ctc2
2 mm air gap
2 mm air gap

(a)
30 mH
Copper foil
m layers
Mylar foil
m + 1 layers
p1
Core
d0
0 mH
d1
wb
p0

(b)
Fig. 1. Schematics of the studied MV copper-foiled inductor.  (a)
Front view. (b) Cross-sectional view schematic of an MV copperfoiled inductor.
Table I. Key parameters of the MV foil-based inductor
Description
Symbol
Value
Thickness of the copper foil
dc
0.05 mm
Width of the copper foil
wc
30 mm
Thickness of the mylar foil
dm
0.05 mm
Width of the mylar foil
(Height of the winding)
wm
(h)
60 mm
Distance between the two windings
pw
19 mm
Width of the winding
w
55.5 mm
Width of the spacer
wb
10 mm
Authorized licensed use limited to: Aalborg Universitetsbibliotek. Downloaded on January 07,2021 at 09:05:28 UTC from IEEE Xplore.  Restrictions apply.

## [стр. 4]

0885-8993 (c) 2020 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission. See http://www.ieee.org/publications_standards/publications/rights/index.html for more information.
This article has been accepted for publication in a future issue of this journal, but has not been fully edited. Content may change prior to final publication. Citation information: DOI 10.1109/TPEL.2020.3048226, IEEE
Transactions on Power Electronics
IEEE POWER ELECTRONICS REGULAR PAPER/LETTER/CORRESPONDENCE
Thickness of the core
d0
40 mm
Distance of the air gap between the bobbin
and core
p0
1.5 mm
Distance between the inner layer and bobbin
p1
12 mm
Thickness of the bobbin
d1
2 mm
Number of layers
m
190
Total inductance (designed value)
L
30 mH

TABLE II. RELATIVE PERMITTIVITY OF THE MATERIAL
Description
Symbol
Value
Relative permittivity of the mylar foil
[29]
εm
3.25
Relative permittivity of the bobbins and
spacers [30]
εb
4.0
The permittivity of vacuum [31]
ε0
8.82×10-12 F/m
In Fig. 1, the terminal labeled as "0 mH" is also defined as
the hot terminal Phot, which locates at the inner layer. The
terminal labeled as "30 mH" is defined as the cold terminal
Pcold, which locates at the outer layer. The core/frame is also
labeled as G.
The focus of this paper is to analytically model the
equivalent capacitance between Phot and Pcold Ctt, between Phot
and G Ctc1, and between Pcold and G Ctc2, based on the
geometrical and material information of the copper-foiled
inductors.
III.  MODELING OF THE FRINGE FIELD CAPACITANCE
In this section, the electrical field in the copper-foiled
inductors are identified. Based on [22], most capacitive
couplings in copper-foiled inductors are identified, which
includes the couplings between the inner layer and core,
between two different layers, and between two windings. Due
to the special structure of copper-foiled inductor, there is only
one turn in a single layer. Therefore, the couplings between
turns are the same as those between layers.
However, the fringe field between winding and core is not
considered in the modeling in [22], which will be proved that
is not neglectable in copper-foiled inductors by the later
sections of this paper.
A. Identify the fringe electrical field
A finite element method (FEM) simulation is given to
identify the fringe field in the copper-foiled inductors by using
Ansys, which is presented in Fig. 2. In the simulation, the
voltage potential along the layers of the copper-foils is
configurated equally, therefore, the electrical field strength
between two adjacent layers is zero in this simulation. The
core is configured as reference ground. 19-layer copper-foil
and 20-layer mylar-foil are used to construct the winding. In
this simulation, the thickness of the copper- and mylar-foil is
configurated as 0.5mm, where the distance between the innerlayer and core is 4 mm. The width of the copper-foil is 30 mm,
where the width of the mylar-foil is 60 mm in Fig. 2. The
parameters of material used in FEM simulation are the same
as Table II.
It is worth mentioning that the geometrical parameters of
the copper-foiled inductor in FEM simulations are not exactly
the same as the designed value since the main target here is to
identify the all possible electrical field existed around the
copper-foiled inductor.
According to Fig. 2, although the electrical field is strongest
between the inner-layer and core, the fringe field between the
winding and core are still obvious on both edges. Both the
fringe field between the sidewall of the inductor and core, and
the fringe field between the top-surface and core can be
identified from Fig. 2.
The energy stored in the fringe electrical field will
contribute to an equivalent capacitance (The fringe field
mentioned in this paper is the fringe electrical field). This
capacitance cannot be neglected in the copper-foiled inductors
since the extensive area of the sidewall and top surface of the
copper-foiled inductors. Usually, the fringe field is neglected
for modeling the parasitic capacitance of inductors in previous
research since its impacts are limited. However, in the copperfoiled inductor, due to a large number of layers, the sidewall
area of the copper-foils is significant. Therefore, the impacts
of the fringe field may not be neglected for the purpose of
modeling the parasitic capacitances.

Fig. 2 Fringe field between the winding and core of the copper-foil
inductors
Fringing-field between
the edge and core
Field between the
inner layer and core
Field between two
adjacent layers
Fringing-field between
the outer layer and core
Field between the two windings
Upper-edge
Lower-edge
Upper-edge
Lower-edge

Fig. 3 Identify the capacitive couplings in copper-foiled MV
inductors
Fig. 3 illustrates the field distributions between the winding
and core of the copper-foiled inductor. Besides the wellknown field between two neighbour layers (illustrated with
blue lines), the field between the inner layer and core
Authorized licensed use limited to: Aalborg Universitetsbibliotek. Downloaded on January 07,2021 at 09:05:28 UTC from IEEE Xplore.  Restrictions apply.

## [стр. 5]

0885-8993 (c) 2020 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission. See http://www.ieee.org/publications_standards/publications/rights/index.html for more information.
This article has been accepted for publication in a future issue of this journal, but has not been fully edited. Content may change prior to final publication. Citation information: DOI 10.1109/TPEL.2020.3048226, IEEE
Transactions on Power Electronics
IEEE POWER ELECTRONICS REGULAR PAPER/LETTER/CORRESPONDENCE
(illustrated with red lines), and field between the two windings
(illustrated with pink lines), it also contains the fringe field
between the sidewall of winding and core (illustrated with
green lines) and the fringe field between the top-surface and
core (illustrated with purple lines).
B. Empirical equation in VLSI applications
In VLSI applications [24], a schematic to illustrate the
parasitic capacitance with considering the fringe field effect is
presented in Fig. 4.
Cpp
C1
C2
C3
C4
w
t
h

Fig. 4 Schematic of a chip and ground in VLSI applications
In Fig. 4, C1, C2, C3, and C4 are the parasitic capacitance
contributed by the fringe field. Cpp is the parallel capacitance
between the bottom surface and reference ground. An
empirical equation [25], which is widely used in VLSI
applications, is given to calculate the total parasitic
capacitance.

total
1
2
3
4
pp
0.25
0.5
0
0.77
1.06
1.06
r
C
C
C
C
C
C
w
w
t
h
h
h
ε ε
=
+
+
+
+






≈
×
+
+
×
+
×














  (1)
However, there are some restrictions for applying the
empirical equation in calculating the parasitic capacitance of
copper-foiled inductors:
1) Only applicable for the cases with simple structures. In
VLSI applications, the structure of the conductor is
with only one layer. The conductor is assumed to be
surrounded by the same material, therefore, only one
relative permittivity is used in (1).
2) Only applicable for the cases with specific geometrical
structures. The empirical equation requires w/h > 0.3
and t/h < 10. Otherwise, it can introduce significant
errors.
3) The calculated capacitance by the empirical equation is
the static capacitance, where the voltage potential on
the inductor is assumed to be the same.
For the copper-foiled inductor illustrated in Fig. 1, it has a
more complex geometrical structure than the structure in Fig.
4. Besides, the voltage potential is distributed linear on the
windings in practice, where the calculated static capacitance
from the empirical equation cannot be correctly revealed the
energy stored in the electrical field, which is typically
represented by the dynamical capacitances.
C. Physics-based modeling method of the fringe field
capacitance
The parasitic capacitance contributed by the fringe field is
modeled as two independent capacitances, which are, the
fringe field capacitance between the sidewall and core of the
inductor, and the fringe field capacitance between the topsurface and core. The static capacitances are derived first. The
dynamical capacitance will be modeled based on the derived
static capacitance.
Some assumptions are made before modeling the fringe
field capacitance:
1) The electrical lines between the sidewall of winding and
core are assumed to be an arc of a 90-degree sector, which is
illustrated in Fig. 5(a), where the electrical field is orthogonal
to the conductor surfaces.
2) The electrical lines between the top-surface and core of
the inductor are the arc of a half-circle plus a straight line,
which is also illustrated in Fig. 5(b). The electrical field is
orthogonal to the conductor surfaces. This is an approximation
for describing the field line between the top-surface and core
of the inductor shown in Fig. 5.
3) The voltage potential on the sidewall of winding is
continuous. The sidewall of the mylar-foil is assumed to have
a virtual voltage potential, which is contributed by the fringe
field from the top and bottom surface of each copper-foil
approximately. However, it is only applicable for the cases
that wc>>dc, which is not strict for normal copper-foils. A
schematic to illustrate the assumption is presented in Fig. 6.
4) The core is a perfect conductor. The voltage potential on
the core is always the same.
5) The voltage potential on the same layer is assumed to be
the same. The error introduced by this assumption can become
less when the number of layers is larger.

(a)
p1+d1
twinding
l2

(b)
Fig. 5 Elementary capacitances contributed by the fringe field. (a)
elementary capacitance between the sidewall and core; (b)
elementary capacitance between the top-surface and core.
l1p1+d1

Fig. 6 Approximation made for distributing the voltage potential
continuously on the sidewall
Authorized licensed use limited to: Aalborg Universitetsbibliotek. Downloaded on January 07,2021 at 09:05:28 UTC from IEEE Xplore.  Restrictions apply.

## [стр. 6]

0885-8993 (c) 2020 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission. See http://www.ieee.org/publications_standards/publications/rights/index.html for more information.
This article has been accepted for publication in a future issue of this journal, but has not been fully edited. Content may change prior to final publication. Citation information: DOI 10.1109/TPEL.2020.3048226, IEEE
Transactions on Power Electronics
IEEE POWER ELECTRONICS REGULAR PAPER/LETTER/CORRESPONDENCE
C.1. Static capacitance
In order to calculate the static capacitance contributed by
the fringe field, all copper-foils are assigned to have the same
voltage potential. The capacitance contributed by the fringe
field is classified into two parts, which are the capacitance
between the sidewall of winding and core, and between the
top-surface and core, respectively.
C.1.1 Static capacitance between the sidewall of winding and
core
The elementary static capacitance contributed by the fringe
field between the sidewall of winding and core is derived in (2)
according to Fig. 6.
d1
0
1
ele_sc
1
1
1
2
(
)
dl
C
l
p
d
ε ε
π
=
+
+
                         (2)
l1 is the direct distance between the elementary capacitance
and the start point at the sidewall. εd1 is the dynamical relative
permittivity, which is contributed by both air and mylar-foils.
At different layers, the contributed ratio on the equivalent
permittivity of the mylar foil and air are different due to the
different geometrical structures. Therefore, εd1 should be
related to the position of the elementary capacitance, which
can be approximately presented as (3).
c
1
1
1
d1
1
1
1
1
2
p
d
l
l
p
d
ε
ε
+
+
+
≈
+
+
                         (3)
The equivalent static capacitance between the two sidewalls
of winding and core for single winding in 2-dimension is
presented in (4).
winding
winding
2d_sc
ele_sc
0
d1
0
1
0
1
1
1
2
2
2
(
)
t
t
C
C
dl
l
p
d
ε ε
π
=
=
+
+
∫
∫
                   (4)
A coefficient two is used in (4) since there are two sidewalls
in each winding.
C.1.2 Static capacitance between the top-surface of winding
and core
Similarly, the elementary static capacitance contributed by
the fringe field between the top-surface of winding and core is
derived in (5) according to Fig. 5.
d2
0
2
ele_tc
2
1
1
winding
dl
C
l
p
d
t
ε ε
π
=
+
+
+
                        (5)
l2 is the direct distance between the elementary capacitance
and the start point at the top surface. εd2 is the dynamical
relative permittivity, which can be presented as (6).
c
1
1
winding
2
m
c
d2
2
1
1
winding
2
m
c
d2
2
1
2
      ( <
)
2
1                                                  (
)
2
p
d
t
l
w
w
l
p
d
t
l
w
w
l
ε
π
ε
π
ε
+

+
+
+

-
=

+
+
+


-

=
≥

   (6)
The equivalent static capacitance between the top surface of
winding and core in 2-dimension is presented in (7).
foil
foil
2d_tc
ele_tc
0
d2
0
2
0
2
1
1
winding
2
2
w
w
C
C
dl
l
p
d
t
ε ε
π
=
=
+
+
+
∫
∫
            (7)
Due to the same voltage potential on all copper-foils, there
is no parasitic capacitance between adjacent layers. The
equivalent parasitic capacitance between the inner layer and
core is derived as (8).
s1
s1
0
foil
2d_lc
m
1
1
1
1
m
m
1
b
m
w
C
d
p
d
d
p
d
d
p
d
ε ε
ε
ε
ε

=

+
+

+
+

=

+
+

                             (8)
Then, the total 2D equivalent capacitance illustrated in Fig.
4 is presented as (9).
2d_total
2d_sc
2d_tc
2d_lc
C
C
C
C
=
+
+
                     (9)
By substituting the geometrical and material parameters
used given at the beginning of Section III-A, a comparison of
parasitic capacitance obtained using the FEM simulation, the
empirical equations and the proposed modeling method versus
the number of copper-foil layers is given in Fig. 7, where the
proposed model shows a better agreement with FEM
simulations than using the empirical equation (1).
0
5
10
15
20
25
30
35
40
45
Number of layers
0
20
40
60
80
100
120
140
160
180
Parasitic capacitance (pF)
FEM simulation
Empirical equation
Proposed method

Fig. 7 Comparison of the static capacitances obtained using the FEM
simulation, the empirical equations, and the proposed modeling
method [24], respectively.
C.2. Dynamical capacitance
The dynamical capacitance is dependent on both static
capacitance and practical voltage potential disturbance. Three
cases with different voltage potential distributions are
considered in this paper. The dynamical capacitance between
the sidewall of winding and core, between the top-surface and
core are calculated, respectively.
In Fig. 8, the voltage potential on the inner layer is assumed
to be 0, where the voltage potential on the outer layer is
assumed to be V1.
Case 1: Core is floating. The schematic of Case 1 is
illustrated in Fig. 8(a). [14] indicates that the core potential is
Authorized licensed use limited to: Aalborg Universitetsbibliotek. Downloaded on January 07,2021 at 09:05:28 UTC from IEEE Xplore.  Restrictions apply.

## [стр. 7]

0885-8993 (c) 2020 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission. See http://www.ieee.org/publications_standards/publications/rights/index.html for more information.
This article has been accepted for publication in a future issue of this journal, but has not been fully edited. Content may change prior to final publication. Citation information: DOI 10.1109/TPEL.2020.3048226, IEEE
Transactions on Power Electronics
IEEE POWER ELECTRONICS REGULAR PAPER/LETTER/CORRESPONDENCE
floated around (0+V1)/4 in inductors with multiple layer
structures. 0 and V1 are the voltage potential at the terminals of
the inductor.
Case 2: Core is connected to the hot layer, where the core
potential is equal to 0. The schematic of Case 2 is illustrated in
Fig. 8(b).
Case 3: Core is connected to the cold layer, where the core
potential is equal to V1. The schematic of Case 3 is illustrated
in Fig. 8(c).
0
V1
0
V1
(0+V1)/4
Hot layer
Cold layer

(a)
0
V1
0
V1
0
Hot layer
Cold layer

(b)
0
V1
0
V1
V1
Hot layer
Cold layer

(c)
Fig. 8 Schematic of the winding with linear voltage potential
distribution. a) Case1: Core is floating; b) Case 2: Core is connected
to the hot layer; c) Case 3: Core is connected to the cold layer.
In the three cases, the voltage potential on the copper-foils
is distributed linearly. Therefore, the voltage potential is not
equal at different layers of foil-winding. The energyconservation law is used to derive the dynamical capacitance
in this section.
C.2.1 Dynamical capacitance between the sidewall of winding
and core
In Case 1, the elementary energy stored between the
sidewall of the winding and core is presented as (10).
2
1
1
sc_case1
ele_sc
1
winding
2
d1
0
1
1
1
1
1
1
1
winding
0
1
W
=
0
(
0)
2
4
2
0
1
0
(
0)
2
(
)
4
V
l
d
C
V
t
V
l
V
dl
l
p
d
t
ε ε
π


+


-
+
-












+


=
-
+
-




+
+







(10)
where the total energy is given as
sc_case1
sc_case1
1
2
d1
0
1
1
1
1
1
1
1
1
winding
W
=2
W
2
0
1
2
0
(
0)
2
(
)
4
A
A
d
V
l
V
dl
l
p
d
t
ε ε
π


+


=
-
+
-




+
+






∫∫
∫∫
 (11)
A1 is the surface of the sidewall of the winding in 3dimensional. Since there are two sidewalls in a single winding,
there is a coefficient 2 in front of the integration.
Then, the equivalent sidewall-to-core capacitance to
represent the stored energy is derived by
2
sc_case1
eq_sc_case1
2
1
sc_case1
eq_sc_case1
2
2
1
1
W
=
(
)
2
2W
(
)
C
V
V
C
V
V
-
=
-
                 (12)
Similarly, the equivalent sidewall-to-core capacitance in
Case 2 and Case 3 is presented as (13) and (14), respectively.
2
d1
0
1
sc_case2
1
1
1
1
1
1
winding
sc_case2
eq_sc_case2
2
1
2
1
W
2
0
(
0)
2
(
)
2W
(
0)
A
l
V
dl
l
p
d
t
C
V
ε ε
π




=
+
-


+
+







=

-

∫∫

(13)
2
d1
0
1
sc_case3
1
1
1
1
1
1
1
winding
sc_case3
eq_sc_case3
2
1
2
1
W
2
(0
)
(
0)
2
(
)
2W
(
0)
A
l
V
V
dl
l
p
d
t
C
V
ε ε
π




=
-
+
-


+
+







=

-

∫∫

(14)
C.2.2 Dynamical capacitance between the top-surface of
winding and core
In Case 1, the elementary energy stored between the top
surface and core is presented as (14).
2
1
2
tc_case1
ele_tc
1
1
1
winding
2
d2
0
1
2
1
1
1
2
2
1
1
winding
winding
1
0
W
=
(
)
2
4
1
0
(
)
2
4
V
l
d
C
V
V
V t
V
l
V
V
V
dl
l
p
d
t
t
ε ε
π


+


-
+
-












+


=
-
+
-




+
+
+







(15)
If the boundary surface of the top layer in the winding is
defined as A2 in 3-dimensional, the equivalent top-surface to
core capacitance in Case 1 is obtained as
Authorized licensed use limited to: Aalborg Universitetsbibliotek. Downloaded on January 07,2021 at 09:05:28 UTC from IEEE Xplore.  Restrictions apply.

## [стр. 8]

0885-8993 (c) 2020 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission. See http://www.ieee.org/publications_standards/publications/rights/index.html for more information.
This article has been accepted for publication in a future issue of this journal, but has not been fully edited. Content may change prior to final publication. Citation information: DOI 10.1109/TPEL.2020.3048226, IEEE
Transactions on Power Electronics
IEEE POWER ELECTRONICS REGULAR PAPER/LETTER/CORRESPONDENCE
2
d2
0
1
2
tc_case1
1
1
1
2
2
2
1
1
winding
winding
tc_case1
eq_tc_case1
2
1
1
0
W
2
(
)
2
4
2W
(
0)
A
V
l
V
V
V
dl
l
p
d
t
t
C
V
ε ε
π



+



=
-
+
-





+
+
+








=

-

∫∫

(16)
Similarly, the equivalent top-surface to core capacitance in
Case 2 and Case 3 is calculated as (17) and (18), respectively.
2
d2
0
2
tc_case2
1
1
1
2
2
2
1
1
winding
winding
tc_case2
eq_tc_case2
2
1
1
W
2
(
0)
(
)
2
2W
(
0)
A
l
V
V
V
dl
l
p
d
t
t
C
V
ε ε
π




=
-
+
-



+
+
+






=

-

∫∫

(17)
2
d2
0
2
tc_case3
1
1
1
1
2
2
2
1
1
winding
winding
tc_case3
eq_tc_case3
2
1
1
W
2
(
)
(
)
2
2W
(
0)
A
l
V
V
V
V
dl
l
p
d
t
t
C
V
ε ε
π




=
-
+
-



+
+
+






=

-

∫∫

(18)
C.2.3 Dynamical capacitance in total
To sum Ceqsc and Ceqtc in the three cases, the dynamical
parasitic capacitance Ceq_fringe contributed by the fringe field in
the single winding is presented in (19).
eqfringe_case1
eq_sc_case1
eq_tc_case1
eqfringe_case2
eq_sc_case2
eq_tc_case2
eqfringe_case3
eq_sc_case3
eq_tc_case3
=
=
=
C
C
C
C
C
C
C
C
C
+
+
+
              (19)
IV.  TOTAL  CAPACITANCE
Besides the fringe field capacitance, the inner layer to core
capacitance, layer to layer capacitance, and winding-towinding capacitance need to be considered in order to obtain
the total capacitance of the copper-foiled inductor, where the
basic principle has been introduced in [22]. However, the
equations of the copper-foiled inductor are not exactly the
same due to the different geometrical structures.
The equivalent inner layer to core capacitance Ceqlc is
calculated for Case 1, Case 2, and Case 3, respectively.
eqlc_case1
ele_lc
2
3
eqlc_case2
ele_lc
2
3
2
eqlc_case3
ele_lc
2
3
1
1
1
=(
)
16
4
3
1
= 3
3
3
1
=
3
A
A
A
C
C
m
m
C
C
m
m
m
C
C
m
-
+
-
+
∫∫
∫∫
∫∫
            (20)
where Cele_lc is the elementary capacitance between the inner
layer and core, A3 is the boundary surface of the inner layer of
the copper-foil inductor.
Based on the geometrical structure of the researched
copper-foil inductor illustrated in Fig. 1 and the parameters are
given in Table I, the equivalent permittivity εd3 between the
inner layer and core of the researched copper-foil inductor,
which is dependent on the geometrical structure and material,
is given as
b
b
0
b
1
1
b
0
b
0
d3
1
1
0
(
)
w
d
w
p
d
p
w
d
p
d
p
ε
ε
ε
+
-
+
+
+
=
+
+
                  (21)
Then, the equivalent permittivity used for calculating
the fringe field capacitance between the sidewall of
winding and core, which is fully dependent on the
geometrical structures and material information of
designed inductors, is given in (22), approximately.
c
1
1
0
d3
1
d1_new
1
1
1
0
(1
)
(
)
2
p
d
p
l
l
p
d
p
ε
ε
ε
+
+
+
+
≈
+
+
+
                       (22)
The equivalent permittivity used for calculating the fringe
field capacitance between the top-surface of winding and core
is given in (23).
c
1
1
0
d3
winding
2
m
c
d2_new
2
1
1
0
winding
2
m
c
d2_new
2
(1
)
(
)
2
      ( <
)
2
1                                                             (
)
2
p
d
p
t
l
w
w
l
p
d
p
t
l
w
w
l
ε
ε
π
ε
π
ε
+

+
+
+
+

-
=

+
+
+
+


-

=
≥

(23)
The equivalent capacitance between two adjacent layers is
defined as (24). Due to the cylinder structure of the winding,
the boundary surface of the inner layers is always less than the
outer layers. Therefore, in order to simplify the model, the
average boundary surface A4 of all layers is used to be the
surface integral. Cele_ll is the elementary capacitance between
two adjacent layers.
eqll
ele_ll
2
4
(4
1)
=
3
A
m
C
C
m
-∫∫
                       (24)
The equivalent capacitance between the two windings is
quite dependent on the geometrical structure and winding
layout. If the two windings are totally symmetrical, there is no
parasitic capacitance. However, the geometrical structure
illustrated in Fig. 1 is a quasi-symmetrical structure. Therefore,
the equivalent capacitance between the two windings has to be
considered. A schematic to illustrate the capacitive couplings
between the two windings is given in Fig. 9. The voltage
potential on the start point and endpoint of winding is assumed
as V1 and (m-1)V1/m, respectively.
The equivalent winding-to-winding capacitances in the Region
I and II are presented as (25). A5_1 represents the boundary
surface in 3-dimensional of Region I illustrated in Fig.8,
where A5_2 represents the boundary surface in 3-dimensional
of Region II. εd3 and εd4 are the equivalent permittivities in
Region I and II, respectively. Ceq_ww is the sum of the
equivalent capacitance in Region I and II.
It is worth to mention that the elementary capacitances
Cele_lc, Cele_ll, Cele_ww can be calculated according to [22].
The total capacitances for three cases are obtained by
summing the equivalent capacitances in (19), (20), (24), and
(25).

Authorized licensed use limited to: Aalborg Universitetsbibliotek. Downloaded on January 07,2021 at 09:05:28 UTC from IEEE Xplore.  Restrictions apply.

## [стр. 9]

0885-8993 (c) 2020 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission. See http://www.ieee.org/publications_standards/publications/rights/index.html for more information.
This article has been accepted for publication in a future issue of this journal, but has not been fully edited. Content may change prior to final publication. Citation information: DOI 10.1109/TPEL.2020.3048226, IEEE
Transactions on Power Electronics
IEEE POWER ELECTRONICS REGULAR PAPER/LETTER/CORRESPONDENCE
2
d3
0
1
ww_1
3
5_1
w
3
m
m
m
3
w
d3
m
3
w
ww_1
eq_ww_1
2
1
2
d4
0
1
ww_2
4
5_ 2
w
m
m m
w
d4
m
w
ww_2
eq_ww_2
2
1
eq_ww
eq
1
W
0
2
4 (
)
2(
)
2
2
2
2
2W
(
0)
1
W
0
2
2
4 (
)
2
2
2W
(
0)
2
A
A
bV
dl
m a
b
w
l
t
t
l
w
t
l
w
C
mV
bV
dl
w
t
m a
b
t
w
t
w
C
mV
C
C
ε ε
ε
ε
ε ε
ε
ε


=
+


+
+
+


+
+
=
+
+
=
-


=
+


+
+


+
=
+
=
-
=
∫∫
∫∫
_ww_1
eq_ww_2
C



















+



(25)
Current direction
Current direction
V1
(m-1)V1/m
b
a
V1
(m-1)V1/m+bV1/(4a+4b)
(4m-3)V1/4m
Region: I
Region: I
Region: II
ww
l3
l4
(m-1)V1/m
(m-1)V1/m+aV1/(4a+4b)
(m-1)V1/m+(2b+a)V1/
(4a+4b)
(4m-3)V1/4m
(2m-1)V1/2m
(m-1)V1/m+(2b+a)V1/(4a+4b)
Fig. 9 Schematic of the capacitive coupling between two windings.
eqtotal1
eqfringe_case1
eqlc_case1
eqll
eq_ww
eqtotal2
eqfringe_case2
eqlc_case2
eqll
eq_ww
eqtotal3
eqfringe_case3
eqlc_case3
eqll
eq_ww
Case 1:
=
Case 2:
=
Case 3:
=
C
C
C
C
C
C
C
C
C
C
C
C
C
C
C
+
+
+
+
+
+
+
+
+
    (26)
A three-terminal equivalent circuit is illustrated in Fig. 10
for representing the copper-foil inductor.
Ctc1
Ctc2
Ctt
L
Phot
Pcold
Core

Fig. 10 Three-terminal equivalent circuit to represent the copperfoiled MV filter inductor
Phot is the terminal at the inner layer (hot layer), Pcold is the
terminal at the outer layer (cold layer). The equivalent
capacitance between the two terminals is Ctt, where the
equivalent capacitance between the terminals and core are Ctc1
and Ctc2, respectively.
Based on [22], the three equivalent capacitances in Fig. 10
are calculated by
tc1
tc 2
eqtotal1
tt
tc1
tc 2
eqtotal2
tt
tc 2
eqtotal3
tt
tc1
C
C
C
C
C
C
C
C
C
C
C
C

=
+

+

=
+


=
+


                     (27)
V.  MODEL VALIDATIONS
The parasitic capacitances of the copper-foil inductor
introduced in Section II are analytically calculated by using
the equations derived in Section IV.
A 10 kV/8 A copper-foiled inductor is manufactured based
on the schematic given in Fig. 1, where the pictures are
presented in Fig. 11.
24.5 cm
30.0 cm
10.2 cm

     (a) Front view                 (b) Side view
Fig. 11 Pictures of the manufactured copper-foiled MV filter inductor
A. Theoretical calculation results
By using the derived equations (2)-(27) and physical
parameters of the copper-foiled inductor, the calculated
equivalent fringe field, inner layer to core, layer-to-layer, and
winding-to-winding capacitances for the three different cases
are listed in Table III. It is worth to mention that the calculated
capacitances are only valid before the first resonant frequency
of the copper-foiled inductor due to the assumptions used for
calculating the elementary capacitance.
Based on (27), the three-terminal equivalent circuit of the
researched inductor is presented in Fig. 12. The inductance
value is used as the rated value of the researched inductor.
27.8 pF
13.2 pF
52.1 pF
30 mH
0mH (Phot)
30mH (Pcold)
Core

Fig. 12 Calculated three-terminal equivalent circuit of the researched
copper-foiled MV inductor
B. Experimental verifications
In this section, the parasitic capacitances of the copperfoiled inductor are measured to verify the theoretical analysis
using a Keysight E4990A impedance analyzer [33] and its
adapter 16047 [34], where the accuracy is between 0.1% and
1% for the measured impedance smaller than 100 kΩ. Before
measuring the impedance of the inductors, both open-loop and
short-circuit calibrations are applied to guarantee the
Authorized licensed use limited to: Aalborg Universitetsbibliotek. Downloaded on January 07,2021 at 09:05:28 UTC from IEEE Xplore.  Restrictions apply.

## [стр. 10]

0885-8993 (c) 2020 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission. See http://www.ieee.org/publications_standards/publications/rights/index.html for more information.
This article has been accepted for publication in a future issue of this journal, but has not been fully edited. Content may change prior to final publication. Citation information: DOI 10.1109/TPEL.2020.3048226, IEEE
Transactions on Power Electronics
IEEE POWER ELECTRONICS REGULAR PAPER/LETTER/CORRESPONDENCE
measurement accuracy. A picture of the experimental setup is
given in Fig. 13.
The conventional measurement method and the guarding
measurement method are used to measure the parasitic
capacitance for the three different cases, where the core
potential is different, as discussed in Section V. The principles
of the two measurement methods are well described in [35].
The measured impedance is fitted by using an equivalent LC
parallel circuit, which is integrated in Keysight E4990
impedance analyzer. Then, the inductance and capacitance of
the equivalent LC parallel circuit are obtained.
Keysight E4990A
Keysight 16047A
10 kV/8A
 copper-foiled inductor

Fig. 13 Experimental setup for measuring the parasitic
capacitances in an MV copper-foiled inductor
Fig. 14 shows the comparisons between the calculations and
measurements. The dc-bias voltage and current are selected as
0 V and 0 mA in these three researched cases. More tests
under different dc-bias voltage and current are measured,
which is however, do not show any difference on the
impedance around the first resonant point.
The value of inductance in the calculated impedance is
derived with the known value of the designed (rated)
inductance. Fig. 14(a)-(c) is the comparison between the
theoretical calculations and measured impedance using the
conventional measurement method. Fig. 14(d)-(f) is the
comparison between the theoretical calculations and measured
impedance when using guarding technology. Since there are
no damping resistors in the calculated equivalent circuit, the
magnitude at the resonance point in Fig. 14(a)-(d) is infinitely
high. Therefore, the frequency of the first resonant points
matches well, which means the calculations are close to the
measured results. In Fig. 14(e) and (f), the calculated
impedance before the first resonant point (is smaller than
1MHz in this paper) is close to the measured impedance. The
numerical comparisons are also given in Table. IV. Overall,
the theoretical calculations show good agreement with the
measurements.
C. Comparisons
The modeling method introduced in [22] is used to calculate
the parasitic capacitance of the same copper-foiled inductor,
with the same geometrical and material parameters. The
comparisons among the calculated three-terminal equivalent
circuit using the method in [22], proposed method, and two
different modeling methods are presented in Table IV.
For the three cases, compared to the measurements by using
guarding technology, the calculated parasitic capacitance
without considering the fringe field has 11.2%, 15.2%, and
13.5% error in three cases, respectively. The errors of
calculations using the proposed method in the three cases are
1.0%, 3.2%, and 7.8%, respectively. The proposed modeling
method has better accuracies with considering the fringe
electrical field effects.
For the calculated three-terminal equivalent circuits, it can
be found that the measured capacitance between Pcold and G is
11.0 pF by using the guarding technology, instead of the
theoretical calculations 0 pF by using the modeling method in
[22], which means the modeling method [22] fails to
characterize the capacitance between the terminals and core.
However, this capacitance is successfully characterized by
using the proposed modeling method, where the fringe field
effects is important in modeling the parasitic capacitances in
copper-foiled inductors.
D. Error analysis
The values of the geometrical and material parameters in
the manufactured inductor cannot be the same as the designed
value since the complex structure is utilized in the copperfoiled inductors. Several assumptions are made to simplify the
electrical field distribution for analytically modeling the
parasitic capacitance, which can introduce errors to the
calculations. Besides, the measurements can also introduce
errors. Especially the values can be easily changed by
temperature, humidity, and so on. As can be seen from Table
IV, the maximum difference between using two different
measurement methods is close to 2%. However, in this article,
the maximum error is observed as less than 10%, which is
acceptable compared to relevant research [14], [22], [36], [37].


Table III Total capacitance for the three different cases
Case
Description
Equivalent fringe
field capacitance
Equivalent layer to
layer capacitance
Equivalent inner layer
to core capacitance
Equivalent winding-towinding capacitance
Total
capacitance
Case1
Core is floating
6.1 pF
53.7 pF
1.3 pF
≈0 pF
61.1 pF
Case2
Core is connected to Phot
11.6 pF
≈0 pF
65.3 pF
Case3
Core is connected to Pcold
4.8 pF
21.5 pF
80.0 pF

Authorized licensed use limited to: Aalborg Universitetsbibliotek. Downloaded on January 07,2021 at 09:05:28 UTC from IEEE Xplore.  Restrictions apply.

## [стр. 11]

0885-8993 (c) 2020 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission. See http://www.ieee.org/publications_standards/publications/rights/index.html for more information.
This article has been accepted for publication in a future issue of this journal, but has not been fully edited. Content may change prior to final publication. Citation information: DOI 10.1109/TPEL.2020.3048226, IEEE
Transactions on Power Electronics
IEEE POWER ELECTRONICS REGULAR PAPER/LETTER/CORRESPONDENCE
E. Recommendations for reducing the parasitic capacitances
Two
recommendations
for
reducing
the
parasitic
capacitances in copper-foiled inductors are obtained based on
previous theoretical analysis:
1) The parasitic capacitance between two adjacent layers is
able to be reduced with a larger number of layers used in the
winding, according to (24).
2) The parasitic capacitance between the winding and core
(fringe field capacitance and inner-layer-to-core capacitance)
is able to be reduced by using spacers with a larger thickness,
according to (15)-(18) and (20).
VI.  CONCLUSIONS
The parasitic capacitances in copper-foiled MV filter
inductor paper have been modeled in this article. Besides the
conventional
elementary
capacitances,
the
elementary
capacitances contributed by the fringe electrical field have
been identified. A physics-based modeling method has been
proposed to analytically calculate the parasitic capacitance
contributed by the fringe electrical field, which is
computationally efficient. A three-terminal equivalent circuit
was further developed to characterize the couplings between
the terminals and the core of the inductors. The measurements
on a copper-foiled inductor have been presented. The
experimental results verified the validity of the proposed
modeling method, where the parasitic capacitance between the
cold terminal and ground was failed to be revealed in the
Calculation
Measurement
Ctc1
Ctc2
Ctt
L
Phot
Pcold
Core
Frequency (Hz)
Impedance(Ω)
102
103
104
105
106
107
108
100
105
1010

Calculation
Measurement
Ctc1
Ctc2
Ctt
L
Phot
Pcold
Core
Impedance(Ω)
100
105
1010
Frequency (Hz)
102
103
104
105
106
107
108

Calculation
Measurement
Ctc1
Ctc2
Ctt
L
Core
Phot
Pcold
Frequency (Hz)
102
103
104
105
106
107
108
Impedance(Ω)
100
105
1010

                                         (a)                                                                         (b)                                                                      (c)
Calculation
Measurement
Ctc 1
Ctc 2
Ctt
L
Core
Phot
Pcold
Frequency (Hz)
102
103
104
105
106
107
108
Impedance(Ω)
100
105
1010
Calculation
Measurement
Ctc 1
Ctc 2
Ctt
L
Core
Phot
Pcold
Frequency (Hz)
102
103
104
105
106
107
108
Impedance(Ω)
100
105
Calculation
Measurement
Ctc 1
Ctc 2
Ctt
L
Core
Phot
Pcold
Frequency (Hz)
102
103
104
105
106
107
108
Impedance(Ω)
100
105

                                        (d)                                                                           (e)                                                                     (f)
Fig. 14 Comparisons between the calculations and measured impedance (dc-bias voltage 0 V and current 0 A). (a)-(c) are Case 1, Case 2 and
Case 3, respectively, by using the conventional measurement method; (d)-(f) are Case 1, Case 2 and Case 3, respectively, by using the
measurement method with guarding technology.

Table IV Numerical comparisons of parasitic capacitances between the measurements and calculations
Case
Calculations
(w/o considering the fringe field [22])
Calculations
(Proposed method)
Measured capacitance
(Normal measurements)
Converted capacitance
based on the measurements
with guarding method
Case 1
53.7 pF
61.1 pF
61.2 pF
60.5 pF
Case 2
53.7 pF
65.3 pF
65.3 pF
63.3 pF
Case 3
75.1 pF
80.0 pF
85.1 pF
86.8 pF
Two-terminal
equivalent circuit
53.7 pF
30 mH
Phot
Pcold

61.1 pF
30 mH
Phot
Pcold

61.2 pF
30 mH
Phot
Pcold

60.5 pF
30 mH
Phot
Pcold

Three-terminal
equivalent circuit
21.5pF
0 pF
54.6 pF
30 mH
Phot
Pcold
G

27.8 pF
13.2 pF
52.1 pF
30 mH
Phot
Pcold
G

33.8 pF
14.0 pF
51.3 pF
30 mH
Phot
Pcold
Core

32.5 pF
11.0 pF
52.3 pF
30 mH
Phot
Pcold
G

Authorized licensed use limited to: Aalborg Universitetsbibliotek. Downloaded on January 07,2021 at 09:05:28 UTC from IEEE Xplore.  Restrictions apply.

## [стр. 12]

0885-8993 (c) 2020 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission. See http://www.ieee.org/publications_standards/publications/rights/index.html for more information.
This article has been accepted for publication in a future issue of this journal, but has not been fully edited. Content may change prior to final publication. Citation information: DOI 10.1109/TPEL.2020.3048226, IEEE
Transactions on Power Electronics
IEEE POWER ELECTRONICS REGULAR PAPER/LETTER/CORRESPONDENCE
conventional modeling method without considering the fringe
effects. Two recommendations for reducing the parasitic
capacitance in copper-foiled inductors are also given in this
paper.
REFERENCES
[1]
J. Casady, V. Pala, D. Lichtenwalner, E. Brunt, B. Hull and et al., "New
generation 10 kV SiC power MOSFET and diodes for Industrial
Applications," in Proc. Proceedings of PCIM Europe 2015, May 2015,
pp. 96-103.
[2]
J. Wang, R. Burgos, D. Boroyevich and Z. Liu, "Design and testing of 1
kV H-bridge power electronics building block based on 1.7 kV SiC
MOSFET module," in Proc. 2018 International Power Electronics
Conference, May 2018, pp. 3749-3756.
[3]
J. Casarin, P. Ladoux and P. Lasserre, "10kV SiC MOSFETs versus
6.5kV Si-IGBTs for medium frequency transformer application in
railway traction," in Proc. 2015 International Conference on Electrical
Systems for Aircraft, Railway, Ship Propulsion and Road Vehicles,
Aachen, 2015, pp. 1-6.
[4]
B. Zhang and S. Wang, "A Survey of EMI Research in Power
Electronics Systems With Wide-Bandgap Semiconductor Devices,"
IEEE Journal of Emerging and Selected Topics in Power Electronics,
vol. 8, no. 1, pp. 626-643, Mar. 2020.
[5]
A. Anurag, S. Acharya and S. Bhattacharya, "Gate drivers for highfrequency
application
of
silicon-carbide
MOSFETs:
design
considerations for faster growth of LV and MV applications," IEEE
Power Electronics Magazine, vol. 6, no. 3, pp. 18-31, Sep. 2019.
[6]
X. Zhang, H. Li, J. Brothers, L. Fu, M. Perales, J. Wu and J. Wang, "A
gate drive with power over fiber-based isolated power supply and
comprehensive protection functions for 15-kV SiC MOSFET," IEEE
Journal of Emerging and Selected Topics in Power Electronics, vol. 4,
no. 3, pp. 946-955, Sep. 2016.
[7]
N. Christensen, A. Jørgensen, D. Dalal, S. Sonderskov, S. Bęczkowski,
C. Uhrenfeldt and S. Munk-Nielsen, "Common-mode current mitigation
for medium voltage half-bridge SiC modules," in Proc. 2017 19th
European Conference on Power Electronics and Applications, Sep.
2017, pp. 1-8.
[8]
J. Jorgensen et al. "Multi-chip Medium Voltage SiC MOSFET Power
Module with Focus on Low Parasitic Capacitance," in Proc. 11th
International Conference on Integrated Power Electronics Systems,
Mar. 2020, pp. 154-159.
[9]
C. DiMarino, B. Mouawad, C. Johnson, M. Wang, Y. Tan, G. Lu, D.
Boroyevich and R. Burgos, "Design and experimental validation of a
wire-bond-less 10 kV SiC MOSFET power module," IEEE Journal of
Emerging and Selected Topics in Power Electronics, Early access, doi:
10.1109/JESTPE.2019.2944138.
[10] Y. Xiao, Z. Zhang, M. Andersen, and K. Sun, "Impact on ZVS operation
by splitting inductance to both sides of transformer for 1-MHz GaN
based DAB converter," IEEE Transactions on Power Electronics, vol.
35, no. 11, pp. 11988-12002, Nov. 2014.
[11] Z. Ouyang and M. Andersen, "Overview of planar magnetic technologyfundamental properties," IEEE Transactions on Power Electronics, vol.
29, no. 9, pp. 4888-4900, Sep. 2014.
[12] J. Biela and J. Kolar, "Using transformer parasitics for resonant
converters - a review of the calculation of the stray capacitance of
transformers," IEEE Transactions on Industry Applications, vol. 44, no.
1, pp. 223-233, Jan./Feb. 2008.
[13] S. Acharya, A. Anurag, Y. Prabowo, and S. Bhattacharya, "Practical
design considerations for MV LCL filter under high dv/dt conditions
considering the effects of parasitic elements," in Proc. 2018 9th IEEE
International Symposium on Power Electronics for Distributed
Generation Systems, Jun. 2018, pp. 1-7.
[14] Z. Shen, H. Wang, Y. Shen, Z. Qin and F. Blaabjerg, "An improved
stray capacitance model for inductors," IEEE Transactions on Power
Electronics, vol. 34, no. 11, pp. 11153-11170, Nov. 2019.
[15] H. Zhao et al., "Behavioral modeling and analysis of ground current in
medium-voltage inductors," IEEE Transactions on Power Electronics,
vol. 36, no. 2, pp. 1236 - 1241, Feb. 2021.
[16] A. Anurag, S. Acharya, S. Bhattacharya and T. Weatherford, "Thermal
performance and reliability analysis of a medium voltage three-phase
inverter considering the influence of high dv/dt on parasitic filter
elements," IEEE Journal of Emerging and Selected Topics in Power
Electronics, vol. 8, no. 1, pp. 486-494, Mar. 2020.
[17] R. Ramachandran et al., "Analysis and Experimental Verification of
Reducing Intra-winding Capacitance in a Copper Foil Transformer," in
Proc. 2020 IEEE Applied Power Electronics Conference and
Exposition, Mar. 2020, pp. 2653-2657.
[18] H. Kiwaki et al., "Evaluation of high power foil-type air-core
transformer by high-frequency flyback converter," in Proc. Proceedings
of 1994 Power Electronics Specialist Conference, Jun. 1994, pp. 13111314.
[19] E. Barrios et al., "High-Frequency Power Transformers With Foil
Windings: Maximum Interleaving and Optimal Design," IEEE
Transactions on Power Electronics, vol. 30, no. 10, pp. 5712-5722, Oct.
2015.
[20] R. Reeves et al., "Air-coiled foil-wound inductors," Proceedings of the
Institution of Electrical Engineers, vol. 125, no. 5, pp. 460-464, May
1978.
[21] X. Liu et al., "Calculation of capacitance in high-frequency transformer
windings," IEEE Transactions on Magnetics, vol. 52, no. 7,2003204,
Jul. 2016.
[22] H. Zhao et al., "Physics-based modeling of parasitic capacitance in
medium-voltage filter inductors," IEEE Transactions on Power
Electronics, vol. 36, no. 1, pp. 829 - 843, Jan. 2021.
[23] L. Deng et al., "Investigation on the Parasitic Capacitance of High
Frequency and High Voltage Transformers of Multi-Section Windings,"
IEEE Access, vol. 8, pp. 14065-14073, Jan. 2020.
[24] N. Van der meijs and J. Fokkema, "VLSI circuit reconstruction from
mask topology," Integration, vol. 2, no. 2, pp. 85-119, Jun. 1984.
[25] A. Massarini and M. K. Kazimierczuk, "Self-capacitance of inductors,"
IEEE Trans. Power Electron., vol. 12, no. 4, pp. 671-676, Jul. 1997.
[26] H. Wheeler, "Transmission-Line Properties of Parallel Strips Separated
by a Dielectric Sheet," IEEE Transactions on Microwave Theory and
Techniques, vol. 3, no. 2, pp 172-185, Mar. 1965.
[27] A. Elrashidi et al., "Performance Analysis of a Microstrip Printed
Antenna Conformed on Cylindrical Body at Resonance Frequency 4.6
GHz for TM01 Mode," Procedia Computer Science, vol. 10, pp. 775784, 2012.
[28] Y .Wang et al., "The Fringe-Capacitance of Etching Holes for CMOSMEMS," Micromachines, vol. 6, no. 11, pp. 1617-1628, Oct. 1015.
[29] Dupont Teijin Films, "Mylar polyester film," Jun. 2003. [Online].
Available:
http://usa.dupontteijinfilms.com/wpcontent/uploads/2017/01/Mylar_Electrical_Properties.pdf
[30] LANXESS, "DURETHAN BKV 30 H-polyamide 6", May 2005.
[Online].
Available:
https://techcenter.lanxess.com/scp/
americas/en/docguard/PIB_Durethan_BKV30H.pdf?docId=76997
[31] Wikipedia, "Vacuum permittivity", Sep. 2019. [Online]. Available:
https://en.wikipedia.org/wiki/Vacuum_permittivity
[32] Metglas, "Magnetic materials" Aug. 2020. [Online]. Available:
https://metglas.com/magnetic-materials/
[33] Keysight
Technologies,
"Keysight
Technologies
Impedance
measurement
handbook"
[Online],
Available:
https://literature.cdn.keysight.com/litweb/pdf/5950-3000.pdf
[34] Keysight Technology, "E4990A Impedance Analyze" [Online].
Available:
https://www.keysight.com/us/en/assets/7018-04256/datasheets/5991-3890.pdf
[35] Keysight Technology, "16047A Test Fixture" [Online]. Available:
https://www.keysight.com/en/pd-1000000477%3Aepsg%3Apro-pn16047A/test-fixture-axial-and-radial?pm=PL&nid=-34051.536880746
&cc=DK&lc=dan
[36] P. Thummala, H. Schneider, Z. Zhang and M. Andersen, "Investigation
of transformer winding architectures for high voltage (2.5 kV) capacitor
charging and discharging applications," IEEE Transactions on Power
Electronics, vol. 31, no. 8, pp. 5786-5796, Aug. 2016.
[37] M. Zdanowski, K. Kostov, J. Rabkowski, R. Barlik and H. Nee, "Design
and Evaluation of Reduced Self-Capacitance Inductor in DC/DC
Converters with Fast-Switching SiC Transistors," IEEE Transactions on
Power Electronics, vol. 29, no. 5, pp. 2492-2499, May 2014.


Authorized licensed use limited to: Aalborg Universitetsbibliotek. Downloaded on January 07,2021 at 09:05:28 UTC from IEEE Xplore.  Restrictions apply.

## [стр. 13]

0885-8993 (c) 2020 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission. See http://www.ieee.org/publications_standards/publications/rights/index.html for more information.
This article has been accepted for publication in a future issue of this journal, but has not been fully edited. Content may change prior to final publication. Citation information: DOI 10.1109/TPEL.2020.3048226, IEEE
Transactions on Power Electronics
IEEE POWER ELECTRONICS REGULAR PAPER/LETTER/CORRESPONDENCE
Hongbo Zhao received the B.S. degree in
electrical engineering and its automation
from
Southwest
Jiaotong
University,
Chengdu, China in 2015. He is currently
working toward the Ph.D degree with
Aalborg University, Aalborg, Denmark.
His research interests include mediumvoltage converters and their filters utilized
by wide band-gap power devices.


Zhizhao Huang received the B.S. degree in
new energy materials and devices from the
University of Electronic Science and
Technology of China, Chengdu, China, in
2015 and is currently working toward the
Ph.D. degree in the School of Electrical and
Electronic
Engineering,
Huazhong
University of Science and Technology,
Wuhan, China. From October 2019 to
October 2020, He was a visiting Ph.D.
student in the Power Electronic Systems
Section at the Department of Energy Technology, Aalborg
University, Aalborg, Denmark.
His current research interests include wide bandgap devices
packaging, integration, and high-density applications.


Dipen Narendra Dalal received the M.Sc.
degree
in
Energy
Engineering
with
specialization in Power Electronics and
Drivers from Aalborg University, Aalborg,
Denmark in 2016. He is currently working
towards the PhD degree at the Department
of Energy Technology, Aalborg University.
His current research interests include wide band-gap power
semiconductor devices and medium voltage high power converters.


Asger Bjørn Jørgensen received the M.Sc.
and Ph.D. degrees in energy engineering
from Aalborg University, Denmark, in 2016
and 2019, respectively.
He is currently working as a Postdoc at the
Department of Energy Technology, Aalborg
University. His research interests include
power module packaging, wide bandgap
power semiconductors and multi-physics
finite
element
analysis
within
power
electronic applications.


Jannick Kjær Jørgensen received his
M.Sc. degree in Nanotechnology with
specialization
in
Nanomaterials
and
Nanophysics from Aalborg University,
Aalborg, Denmark in 2018. He is currently
working as a research assistant at the
Department of Energy Technology, Aalborg
university.
His research interests include packaging
and modeling of wide-bandgap power
semiconductor devices, and medium voltage power modules.
Xiongfei Wang received the B.S. degree
from Yanshan University, Qinhuangdao,
China, in 2006, the M.S. degree from
Harbin Institute of Technology, Harbin,
China,
in
2008,
both
in
electrical
engineering, and the Ph.D. degree in
energy
technology
from
Aalborg
University, Aalborg, Denmark, in 2013.
Since 2009, he has been with the
Department
of
Energy
Technology,
Aalborg University, where he became an
Assistant Professor in 2014, an Associate Professor in 2016, a
Professor and Research Program Leader for Electronic Power Grid
(eGrid) in 2018, and the Director of Aalborg University-Huawei
Energy Innovation Center in 2020. He is also a Visiting Professor of
power electronics systems with KTH Royal Institute of Technology,
Stockholm, Sweden. His current research interests include modeling,
dynamic analysis and control of power electronic converters and
systems, power electronics for sustainable energy systems and
electrical grids, high power converters and multi-converter systems.
Dr. Wang serves as a Member-at-Large for Administrative
Committee of IEEE Power Electronics Society (PELS) in 2020-2022,
and as an Associate Editor for the IEEE TRANSACTIONS ON
POWER ELECTRONICS, the IEEE TRANSACTIONS ON
INDUSTRY APPLICATIONS, and the IEEE JOURNAL OF
EMERGING
AND
SELECTED
TOPICS
IN
POWER
ELECTRONICS. He was selected into Aalborg University Strategic
Talent Management Program in 2016. He has received six Prize
Paper Awards in the IEEE Transactions and conferences, the 2016
Outstanding Reviewer Award of IEEE TRANSACTIONS ON
POWER ELECTRONICS, the 2018 IEEE PELS Richard M. Bass
Outstanding Young Power Electronics Engineer Award, the 2019
IEEE PELS Sustainable Energy Systems Technical Achievement
Award, the 2020 IEEE Power & Energy Society Prize Paper Award,
and Highly Cited Researcher in the Web of Science in 2019-2020.

Stig Munk-Nielsen received the M.Sc. and
Ph.D. degrees from Aalborg University,
Aalborg, Denmark, in 1991 and 1997,
respectively.
He is currently Professor at the Department
of Energy Technology, Aalborg University.
His research interests include LV and MV
Si, SiC and GaN converters, packaging of
power
electronic
devices,
electrical
monitoring apparatus for IGBTs, failure
modes and device test systems. In the last
ten years, he has been involved or has managed 10 research projects.
Published 221 international power electronic papers being co-author
or author.



Authorized licensed use limited to: Aalborg Universitetsbibliotek. Downloaded on January 07,2021 at 09:05:28 UTC from IEEE Xplore.  Restrictions apply.
