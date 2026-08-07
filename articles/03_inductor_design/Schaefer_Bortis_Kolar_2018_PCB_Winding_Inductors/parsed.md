# source

<!-- FORMULA-WARNING -->
> **Формулы в этом файле недостоверны.** Текстовый слой PDF теряет дробные черты, радикалы и группировку степеней; знак интеграла приходит как `Z` или `R`, знак суммы -- как `P`. Формул вырезано: **26**, читать их в `formulas/` (картинки 300 dpi, перечень в `formulas/INDEX.md`).
<!-- /FORMULA-WARNING -->

> Автоматически извлечено из `source.pdf` скриптом `parse_pdf.py`
> Движок: pymupdf. Страниц: 9 из 9.
> Дата извлечения: 2026-08-07 06:43 UTC

Текст не редактировался. Формулы и таблицы могут быть искажены —
при сомнении сверяться с исходным PDF.

---

## [стр. 1]

© 2018 IEEE
Proceedings of the 19th IEEE Workshop on Control and Modeling for Power Electronics (COMPEL 2018),
Padova, Italy, June 25-28, 2018
Optimal Design of Highly Efficient and Highly Compact PCB Winding Inductors
J. Schäfer,
D. Bortis,
J. W. Kolar
Personal use of this material is permitted. Permission from IEEE must be obtained for all other uses, in any current or
future media, including reprinting/republishing this material for advertising or promotional purposes, creating new collective
works, for resale or redistribution to servers or lists, or reuse of any copyrighted component of this work in other works.

## [стр. 2]

Optimal Design of Highly Efficient and Highly
Compact PCB Winding Inductors
Jannik Sch¨afer, Dominik Bortis and Johann W. Kolar
Power Electronic Systems Laboratory
ETH Zurich
Physikstrasse 3, 8092 Zurich, Switzerland
Email: schaefer@lem.ee.ethz.ch
Abstract-In industrial power electronic systems, power density and costs are key design criteria. Therefore, very high
switching frequencies are commonly used in order to minimize
the volume of the inductive components. However, especially in
high-current applications, the well-known skin and proximity
effects as well as the fringing field around the air gaps of
inductors, impede the design of these components, as they are
usually all reducing the effective cross-sectional area of solid
inductor windings. Consequently, litz wire windings would have
to be used, which is often impossible, mainly due to cost reasons.
This paper introduces a new, simple and efficient approach on
how to integrate inductor windings directly into the PCB, by
mitigating the high-frequency losses due to a relocation of the
air gap. In this way, its fringing field can be used to partly
compensate the parasitic magnetic fields causing the skin and
proximity effects. Hence, very low production costs and high
power densities can be achieved. In a first step, simple design
guidelines are derived and verified by means of simulations.
Finally, a possible hardware implementation of the proposed
concept is presented.
Index Terms-PCB inductor, air gap relocation, magnetic field
compensation
I. INTRODUCTION
Inductors are used in a variety of electronic applications and
especially in the area of power electronic converter systems,
where they are usually employed as filter components in order
to attenuate the switching frequency output voltage ripple,
e.g. of buck converter topologies [1] [2]. Hence, the inductive
components need to be designed in such a way that they can
handle a certain required maximum output current, whereby
an appropriate copper cross-section of the winding needs to
be provided in order to limit the arising conduction losses
in the inductor winding. However, especially in high-power
low-voltage applications, these inductor currents can be huge
and therefore large copper cross-sections Acu, e.g. using wide
copper bars and solid conductor windings, are required. To
achieve a high power density, it is therefore important to
obtain a homogeneous current density throughout Acu, in order
to optimally use the employed copper material and therefore
maximize the effective copper cross-sectional area Acu,effof
the winding.
However, a homogeneous current density is difficult to
Hag
IL
Hskin+prox
Air Gap
Winding
Ferrite Core
Ieddy
Fig. 1. Parasitic magnetic fields Hskin+prox and Hag in a conventional
arrangement of a PCB winding inductor, which are inducing eddy currents
Ieddy in the conductor and therefore increase the total conduction losses.
achieve, since due to the high-frequency (HF) current components resulting from the switching frequency, different parasitic effects come into play, which deflect the current towards
the surface or edges of the conductor and thereby reduce the
effective Acu,eff. These parasitic HF effects can be divided
into three main components: First, the skin effect, which
characterizes the impact of the magnetic field Hskin of a
HF current in a conductor on its own conductivity, second,
the proximity effect, which describes the mutual influence
of the magnetic fields Hprox of multiple current carrying
conductors on their individual current distributions and lastly
the third component, which originates from the impact of the
fringing field Hag around an air gap of the magnetic circuit on
conductors in its near vicinity [3]. Hence, if Hag penetrates a
conductive material, it induces eddy currents according to the
well-known law of induction and therefore acts similar to the
aforementioned proximity effect (cf. Fig. 1).
These effects can be minimized in wire-wound inductors using
litz wire, where multiple insulated thin copper strands are
twisted in prescribed patterns, such that the flux linkages of
all strands are equalized. As a result, the current splits equally
among the individual wire strands and due to their much
smaller wire diameter the skin effect caused by Hskin and
the induced currents due to Hprox and Hag in each strand can
strongly be reduced [4]-[6].
Unfortunately, litz wire has some significant drawbacks
compared to solid copper conductors. On the one hand, the
copper fill factor is comparably poor, as a significant amount
of the available wire cross-sectional area is wasted due to
the spaces between the strands and the required insulation
of each individual strand. On the other hand, the allowable
978-1-5386-5541-2/18/$31.00 ©2018 IEEE

## [стр. 3]

current density in litz wire is strongly limited due to its
large thermal resistance orthogonal to the wire surface [7].
In cost driven applicatiosn, however, the most significant
downside of litz wire windings is their price, since the costs
per weight of litz wire are much higher than the ones of solid
conductors [8]. Furthermore, the wire wrapping process and
the termination of these windings are challenging and also
increase the manufacturing costs.
In industrial applications, solid conductor windings, and especially PCB integrated windings, are therefore preferred, as
they allow for much higher current densities (improved power
density) and a cheap and simple manufacturing of inductors.
However, as already mentioned, large conductive surfaces are
prone to induced eddy currents due to external magnetic fields.
For this reason, different approaches have been presented in
literature, which all try to minimize the external magnetic
fields penetrating the conductor. The most efficient approaches
use two different concepts: The first option is to reduce the
fringing field of the air gap by means of either using multiple
smaller air gaps (quasidistributed air gap, cf. Fig. 2a) or by
using a low permeability material (true distributed air gap,
cf. Fig. 2b) [9]. Another possibility is to place the air gaps
perpendicular (z-direction) to the conductor, such that the
main component of the resulting fringing field is heading into
x-direction and therefore does not penetrate the conductor
perpendicular to its surface, i.e. in z-direction. Consequently,
the HF losses due to the fringing field of the air gap can be
minimized, as long as the distance between the air gap and
the conductor is larger than a certain value [9].
However, the manufacturing of inductor cores with multiple
air gaps and/or low permeability material is difficult and
expensive, which is why a design with a single air gap is
usually preferred in industrial applications. Furthermore, in the
aforementioned considerations, the influence of the existing
perpendicular skin and proximity fields are usually neglected,
even though they lead to significant HF losses in a real
conductor. For this reason, in this paper these fields are taken
into account as well, in order to end up with an optimized inx
z
y
a)
IL
x
z
y
IL
Hag
x
z
y
c)
IL
Hag
b)
d)
Hag
low¹r
Fig. 2. Different air gap arrangements to reduce the conduction losses in PCB
windings; e.g. a) multiple air gaps placed in parallel, i.e. in x-direction, along
a straight conductor; b) distributed air gap using low permeability material. In
c) and d), single air gap arrangements along a straight and a circular conductor
are shown.
Hag
x
z
y
Hag
x
z
y
a)
b)
Iag,eq
IL
hcu
bw
IL
¹r>>1
Fig. 3. a) Single air gap arrangement with the fringing field Hag and b) its
equivalent circuit where the fringing field Hag is assumed to be induced by
an equivalent current Iag,eq.
ductor geometry that ensures an almost frequency-independent
current distribution and therefore optimal utilization of the
cross section of the conductor. Thus, minimal HF losses in
the windings and a high suitability for real implementations in
efficient, powerdense and cost driven applications are obtained.
In Section II, all aforementioned magnetic field components
are derived by means of analytical and numerical calculations
and based on these derivations, a simple field compensation
concept is introduced, which allows for partial active compensation of the skin and proximity fields in a straight conductor
using the fringing field of a single air gap placed perpendicularly to the conductor (cf. Fig. 2c). Hence, the AC resistance
can be kept almost at the level of the DC resistance even for
very high frequencies. In Section III, the concept is applied
to a more practice-oriented circular conductor arrangement
(cf. Fig. 2d) and simple design guidelines are provided. In
Section IV, the influence of multiple parallel PCB layers on
the applicability of the proposed concept is investigated in
detail and an exemplary practical implementation of a PCB
winding inductor is shown. Finally, Section V concludes the
findings of this paper.
II. FIELD COMPENSATION IN STRAIGHT CONDUCTORS
The main challenge in the design of a highly efficient highfrequency (HF) inductor winding is the minimization of its
AC resistance RAC, which is the same as striving for an AC
to DC resistance factor FR close to one:
FR = RAC
RDC
minimize
-----→FR,opt = 1.
(1)
Hence, assuming FR = 1 and according to
Pcond = RDCFRI2
rms =
Z
V
J(x, y, z)2
σ
dV,
(2)
the conduction losses in the winding do not change with
frequency, what inherently implies that the current distribution
J(x, y, z) in a conductor should be frequency-independent as
well. Thus, independent of the actual inductor geometry, the
AC current density JAC should be equal to its DC equivalent
JDC in order to minimize the AC-resistance RAC and therefore
also the conduction losses. However, this is usually difficult
to achieve, as various magnetic field components summarized
to⃗Heddy penetrate the conductor and induce eddy currents
according to
∇×⃗E = -µ0
∂⃗Heddy
∂t
,
(3)

## [стр. 4]

wherefore a current displacement and increased FR values
result.
In the following, the different field components contained in⃗
Heddy are analyzed based on the example arrangement of Fig.
3a, and their effects on the current distribution J(x, y, z) are
discussed.
The considered geometrical arrangement comprises an infinitesimally long straight conductor, surrounded by a ferrite
core with a single air gap perpendicularly arranged to the
top surface of the conductor, as illustrated in Fig. 3a. The
corresponding DC current density can be calculated according
to
JDC(x, z) =
IL
hcu · bw
·⃗ey,
(4)
where hcu denotes the thickness and bw the width of the
copper track. However, in order to simplify the calculation
of the various field components of⃗Heddy, it is assumed that
the thickness hcu of the conductor is smaller than the skin
depth of the considered frequency fsw, whereby even for
high-frequency currents a homogeneous current density in zdirection results. This assumption is usually valid for PCB
integrated inductor windings, where the copper thickness of
the PCB with 35 µm..70 µm is smaller than the skin depth.
Thus, an equivalent line current density Jline can be defined
according to
Jline(x) = hcu · JDC(x) = IL
bw
·⃗ey,
(5)
emulating a current sheet with hcu →0. In order to achieve
the desired FR = 1, the same constant line current density
obtained with DC currents should also be achieved for HF
currents, requiring zero time-varying magnetic field inside the
conductor, as otherwise a current displacement would result
(cf. (3)).
However, in the inductor arrangement at hand, there are always
Hag
x
H
Hskin
x
z
y
x
H
x
H
Hz,skin
Hz,ag
Hz,tot
x
J
dw
x
z
y
x
J
x
J
Jy(dw = 0.25bw)
bw
Jy(dw = 0.5bw)
Jy(dw = 0.75bw)
a)
b)
x=0
Fig. 4. a) Magnetic fields Hz,skin, Hz,ag and Hz,tot, where only their
components perpendicular to the conductor surface, i.e. in z-direction, are
considered. Additionally, Hz,skin corresponds to a homogeneous current
distribution in the conductor and Hz,tot = Hz,skin + Hz,ag. b) shows the
resulting HF current densities Jy for different distances dw between the air
gap and the conductor.
two main magnetic field components penetrating the conductor
in z-direction. On the one hand, the magnetic skin field
Hz,skin (cf. Fig. 4a), which originates from the current in the
conductor and can be calculated according to Ampere's Law
Hz,skin(x) =
Z
bw
2
-bw
2
Jline
2π(α -x)dα
(6)
=
IL
2πbw

ln

x + bw
2

-ln
bw
2 -x

·⃗ez.
On the other hand, the fringing field Hag around the air gap,
which can be derived according to [10], or for small air gaps
even easier based on Fig. 3b, where the fringing field is
assumed to be generated by an equivalent current Iag,eq ≈2IL
[11]. The z-component of this magnetic field can therefore be
calculated according to
Hz,ag(x) = IL
π ·
x
d2w + x2 ·⃗ez,
(7)
as shown in Fig. 4a. As can be noticed, both field components Hz,skin and Hz,ag are heading into opposite directions,
whereby a partial mutual compensation of these fields can
be observed. Consequently, the fringing field Hag of the air
gap counteracts the field of the skin effect Hskin, as the total
magnetic field perpendicular to the conductor can be reduced
Hz,tot(x) = Hz,skin(x) + Hz,ag(x).
(8)
However, as illustrated in Fig. 4b, the quality of the compensation, i.e. the distribution of the current density Jy, highly
depends on the distance dw between the conductor and the air
gap, as for very small values of dw, Hz,ag overcompensates
Hz,skin, whereby most of the current is attracted towards
the middle of the conductor (dominating proximity effect),
and for large values of dw an undercompensation results and
the current is pushed towards the edges of the conductor
(dominating skin effect). Hence, there is an optimum distance
dw,opt, where an almost homogeneous current distribution can
be achieved and therefore a very low FR value close to one
results.
There are different approaches to find this optimum value
of dw, as e.g. the finite element method (FEM), where the
geometric arrangement of Fig. 3a is simulated for different
values of dw and different frequencies fsw. The resulting AC
to DC resistance factors FR are shown in Fig. 5a, where two
different regions can be defined: First, the proximity effect
region for dw,norm < 0.5, where the fringing field of the air
gap pulls the current towards the center of the conductor and
second, the skin effect region for dw,norm > 0.5, where the
fringing field of the air gap cannot compensate the skin field
anymore and the current flows at the edges of the conductor
only. In Fig. 5b, these two regions are depicted in more detail
depending on the frequency fsw for different discrete distances
dw at 1⃝... 6⃝.
On the left side, the FR-values for three different dw,norm at
1⃝... 3⃝in the proximity region are shown. For low frequencies
fsw, the proximity losses are strongly increasing with fsw, as

## [стр. 5]

0.3
0.4
0.5
0.6
0.7
0.8
1
1
1.05
1.1
1.15
1.2
1.25
1.3
1.35
AC-DC Resistance Factor FR
fsw=10kHz
fsw=50kHz
fsw=100kHz
fsw=250kHz
fsw=500kHz
fsw=1MHz
0.9
Normalized Air Gap-Conductor Distance dw,norm
Optimal Air Gap Position
1
2
3
4
5
6
a)
 Skin Effect
Proximity
   Effect
0
200 400 600 800 1000
Frequency fsw (kHz)
1
1.1
1.2
1.3
AC-DC Resistance Factor FR
0
200 400 600 800 1000
Frequency fsw (kHz)
1
1.1
1.2
1.3
AC-DC Resistance Factor FR
Hag
Hskin
Proximity Effect
Jy
Jy
x
x
J
J
Skin Effect
1
2
3
4
5
6
b)
dw
Fig. 5. a) AC to DC resistance factor FR of a straight conductor for different
values dw,norm = dw
bw and different frequencies fsw. The optimal air gap
placement for all frequencies lies around dw,norm = 0.5, where below this
value the proximity effect increases FR and above the optimum the skin
effect becomes dominant. Both effects are illustrated in b) for three different
dw,norm values 1⃝, 2⃝, 3⃝and 4⃝, 5⃝, 6⃝, respectively.
the current distribution is getting more and more triangularly
shaped. However, the current is pulled towards a region with
a very low perpendicular magnetic field Hz,tot (cf. Fig. 4a),
which is why the losses do no longer significantly increase
with frequency, once all the current is in this "low-fieldregion".
On the right-hand side, the FR-values for the three different
dw,norm at
4⃝... 6⃝in the skin region are shown. As the
current is pushed towards the edges of the conductor, where
the highest magnetic fields occur, the conduction losses are
constantly increasing with frequency with the well-known
√fsw dependency.
However, between the two regions, where the optimal air gap
position can be found, the FR value is less than 1.1 even for
very high frequencies. Consequently, an almost homogeneous
current density can be achieved, where Hz,tot hardly affects
the current distribution. As a result, a loss factor FH2 can be
introduced
Ploss ∝
Z
V
H2
z,totdV →FH2 =
Z
V
H2
z,totdV,
(9)
as the HF losses are directly proportional to the penetrating
magnetic field, as long as the current distribution in the
winding does not change significantly [12]. This simple H2loss factor can be used to accurately predict the optimal air
gap position, without carrying out a time-consuming FEM
optimization. In addition, for very simple geometries, the
optimum air gap position can even be found analytically. For
the arrangement at hand, the H2-loss factor and the optimal
air gap position dw,opt can be calculated based on (6)-(8)
according to
FH2 =
Z
V
H2
z,totdV
minimize
-----→
∂
∂dw
FH2
!= 0
(10)
and
∂
∂dw
FH2 =
∂
∂dw
Z
V
H2
z,totdV
(11)
=
Z
V
2Hz,tot
∂
∂dw
Hz,totdV
→dw,opt = bw
2 .
Hence, the analytically derived optimal air gap position dw,opt
coincides with the optimal position found based on FEM
simulations (cf. Fig. 5a).
A possible practical implementation of a PCB winding inductor, using the proposed field compensation concept on straight
winding sections, is shown in Fig. 6a. However, this design
has significant drawbacks, as the end-winding sections are not
covered by the air gap, hence the skin and proximity fields are
not compensated anymore and the conduction losses in these
sections significantly increase. In addition, the ratio between
the winding length lws and the core area AC is comparably
poor compared to the circular arrangement shown in Fig. 6b.
Assuming the same total core cross section AC in both designs,
the ratio between the winding lengths can be calculated
according to
Lw(k) = lws
lwc
= 1 + k
√
πk
,
(12)
where k denotes the ratio between the length and the width
of the core cross section AC of Fig. 6a. Hence, the minimum
ratio between the winding lengths can be found to be
∂
∂k Lw(k)
!= 0
k=1
--→Lw(1) =
2
√π > 1.
(13)
Thus, even for the optimal value k = 1 (square cross section),
the winding length of the rectangular core lws is larger than
lwc. Consequently, the circular arrangement of Fig. 6b should
be used in practical applications, as in addition to the reduced
winding length, the circularly shaped winding and air gap
allow to compensate the skin and proximity fields along
the whole winding, whereby the aforementioned end-winding
losses can be avoided. However, the circular shape of the
conductor might influence the optimal air gap position, which
will be investigated in the following section.

## [стр. 6]

¹r>>1
Air Gap
End-
   Winding
AC
lws
AC
lwc
Air Gap
¹r>>1
a)
b)
Fig. 6. a) Practical implementation of a PCB winding inductor with a partially
straight winding, resulting in large end-winding losses and b) an improved
pot core arrangement with a circular winding with minimum length.
5
10
15
20
5
10
15
20
J (A/mm2)
J (A/mm2)
Radial Position (mm)
Radial Position (mm)
rag
5
10
15
20
40
30
0
10
20
J (A/mm2)
Radial Position (mm)
rag
FR(100kHz) = 1.43
FR(100kHz) = 1.04
FR(100kHz) = 1.25
JDC
JAC,comp
40
30
0
10
20
40
30
0
10
20
JDC
JAC,comp
JDC
JAC
a)
b)
c)
20mm
rag
zag
5mm
zag=0.4bw
zag=0.5bw
Fig. 7. Qualitative sketch of a circular PCB winding inductor arrangement (in
reality, the width of the outer shell would be much smaller) and three different
current distributions: a) DC current density JDC in a circular conductor and
its HF equivalent JAC without an air gap in its near vicinity. b) DC current
density and its HF counterpart JAC,comp with the air gap ideally positioned.
c) DC current density and its HF counterpart JAC,comp with the air gap
positioned in the optimal spot for a straight conductor (cf. (11)).
III. FIELD COMPENSATION IN CIRCULAR CONDUCTORS
Unlike in a straight conductor, the DC current density JDC
in circular conductors is not homogeneous anymore and can
be calculated according to
JDC(r) =
IL
r · hcu · ln

rin
rout
,
(14)
as shown in Fig. 7a. Hence, as already mentioned in the
previous section, the HF current density JAC should match
JDC as closely as possible in order to achieve a low FR value.
In the same figure, the current distribution JAC due to the
skin effect only, thus without an air gap in the near vicinity of
the conductor, is illustrated. The magnetic skin field Hz,skin
pushes the current towards the center of the inductor, whereby
an increased FR value results, even for comparably low frequencies (FR = 1.43 at 100 kHz). Therefore, the fringing field
Hz,ag of the air gap is again required to compensate Hz,skin
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1
0.3
0.4
0.5
0.6
0.7
0.8
0.9
Normalized Radial Position of Air Gap rag/rout
Normalized Vertical Position of Air Gap zag/bw
 1.1
FR = 1.5
 1.05
 1.25
 1.5
 2
 2.5
 3.5
 5
 1.1
 1.25
 1.5
FR = 2
FR = 2.5
FR = 1.5
Hag
bw
rin
rout
rag
zag
Fig. 8. AC to DC resistance factor FR for different normalized air gap
positions ( rag
rout , zag
bw ), a frequency of 500 kHz and a ratio of radii
rin
rout
of 0.2.
and to pull the current away from the center of the winding to
match JDC as accurately as possible. The compensating effect
of Hz,ag is shown for two different air gap locations in Fig.
7b and 7c, respectively.
In Fig. 7b, the air gap is located in the optimal position for this
circular geometry, whereby a very low value for FR(= 1.04)
results and JAC,comp hardly deviates from JDC.
In Fig. 7c, the air gap is placed at the position which would
be optimal for a straight conductor, hence in the middle
of the track with a distance zag of
bw
2
(11). However, this
location is far from optimal, as an almost homogeneous current
distribution is achieved, which does not correspond to JDC(r).
Consequently, the optimal air gap positions in straight and
circular conductors are different and need to be calculated
separately.
Once again, there are two different options to find the optimal
air gap position in a circular conductor.
Either the time-consuming FEM simulation, whose results are
shown in Fig. 8 for varying zag and rag values, where zag
denotes the distance between the conductor and the air gap
and rag the radial position of the air gap, or by using the
previously introduced H2-loss factor FH2, which is calculated
based on the magnetic skin field Hz,skin of the DC current
distribution JDC(r) and the fringing field Hz,ag around the
air gap according to
Jline(r) = JDC(r) · hcu =
IL
r · ln

rin
rout
,
(15)

## [стр. 7]

Hz,skin(r) =
rout
Z
rin
Jline
2π(r + α)
 α2 -r2
(α -r)2 E(k2) + K(k2)

dα,
k2 =
4αr
(α + r)2
(16)
and
Hz,ag(r) =
IL
π
q
(r + rag)2 + z2ag
·

r2
ag -r2 -z2
ag
(rag -r)2 + z2ag
E(k2) + K(k2)
!
,
k2 =
4ragr
(rag + r)2 + z2ag
,
(17)
where E(k2) and K(k2) denote the complete elliptic integrals
of the first and second kind. The results are shown in Fig.
9, whereby a very close match between the results of the
actual FR values of Fig. 8 and the H2-loss factors FH2
can be observed. Especially for locations (rag, zag) with the
lowest FR values, the curves are almost identical, which allows
for accurately predicting the optimal position (rag,opt, zag,opt)
within a fraction of the time it would take to simulate the
geometry in a FEM software.
The benefit of the significantly reduced calculation time of the
H2-loss factors cannot only be used for the previously shown
straight and circular conductor arrangements, as the principle
of calculating the optimal air gap position using the H2-loss
factor is very general and can be applied to all kind of winding
geometries, once the DC current distribution is known.
However, in order to simplify the usage of this concept in
practice, a general design guideline would be nice, which
reduces the computational effort for the inductor designer.
Fortunately, in the circular arrangement of Fig. 8, the optimal
air gap positions change with the ratio of radii only and do
not depend on their absolute dimensions, which is why the
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1
0.3
0.4
0.5
0.6
0.7
0.8
0.9
Normalized Radial Position of Air Gap rag/rout
Normalized Vertical Position of Air Gap zag/bw
 1.5
 1.5
 2.5
 2.5
 3.5
 3.5
5
7.5
10
20
FH2,n = 3.5
FH2,n = 5
FH2,n = 3.5
FH2,n = 7.5
FH2,n = 5
 1.05
Fig. 9. Calculated normalized H2-loss factor for the same arrangement as
shown in Fig. 8, in order to estimate the optimal air gap position (rag, zag).
0.2
0.4
0.6
0.8
1
0
0.3
0.4
0.5
0.6
0.7
0.8
1
0.9
0.2
Ratio of Radii rin/rout
Normalized Air Gap Positions (zag/bw), (rag/rout)
zopt: circular
zest: based on (11)
ropt: circular
rest: based on (11)
rag,est(straight)
rag,opt(circular)
zag,est(straight)
zag,opt(circular)
Fig. 10. Comparison between the estimated optimal air gap position based
on the calculations for a straight conductor (rag,est, zag,est) and the actual optimal position based on the calculations for a circular conductor
(rag,opt, zag,opt), for different ratios of radii
rin
rout .
desired general design guideline for circular conductors can
be calculated for all ratios of radii
rin
rout . The resulting optimal
air gap positions (rag,opt, zag,opt) are depicted in Fig. 10.
In order to illustrate the difference between the actual optimal
air gap position for a circular conductor and the simplified
calculation based on a straight conductor (11), the results of
both calculation methods are shown. For
rin
rout > 0.5, the
simplified calculation zag,est =
bw
2
and rag,est =
rin+rout
2
yields very good results, closely following the the optimum
zag,opt and rag,opt obtained from (16) and (17), as the DC
current density JDC(r) in the circular conductor is almost
homogeneous. However, for lower ratios of radii, the optimal
air gap position should be chosen according to the solid lines
depicted in Fig. 10, due to the inhomogeneity of JDC(r).
So far, only a single layer conductor has been considered.
However, in practice, inductor windings usually comprise
multiple turns and multiple layers in order to achieve a certain
required inductance. Therefore, it is crucial to investigate the
applicability of the proposed concept to multilayer windings,
in order to prove its suitability for practical applications. This
will be done in the following section based on a three layer
arrangement.
IV. MULTILAYER WINDING
The multilayer arrangement of Fig. 11 comprises three
PCB layers, which are all separated by thin FR4 layers (not
shown in the figure). In order to calculate the FR values
of the three different conductors, the perpendicular magnetic
fields in each layer have to be known. Thanks to the linearity of magnetoquasistatic field problems, the principle of
superposition can be applied, where the magnetic fields of
each source (conductors, air gap) are calculated independently
and superimposed in the end. However, the calculation of the
different field components is not trivial, as the complexity of
the field problem is increased due to the additional dimension

## [стр. 8]

in z-direction. Hence, in general, the perpendicular magnetic
field throughout the PCB is not constant anymore, whereby
a two-dimensional field problem would have to be solved. In
order to reduce the calculation complexity of the magnetic
field problem, it is assumed that the mutual distance dL
between the layers is much smaller than the width bw of the
copper tracks and therefore a constant z-component of the
magnetic field Hz,skin throughout the height of the PCB can
be presumed. However, in the multilayer arrangement at hand,
the total appearing parasitic magnetic field Hz,skin+prox in the
PCB is now induced by multiple individual layers. Thus, the
magnetic skin field Hz,skin,1 for example, which is induced
by the current IL in the top layer of the PCB, penetrates
not only the top layer itself, but also the two remaining
layers (middle and bottom) as proximity field Hprox,1. The
same holds true for Hz,skin,2 and Hz,skin,3, whereby the total
parasitic magnetic field in each layer can be calculated by
superposition according to
Hz,skin = Hz,skin,1 + Hz,skin,2 + Hz,skin,3.
(18)
Assuming the same DC current distribution JDC(r) in all
turns, the total skin field Hz,skin can therefore be calculated
based on (16), using the equivalent line current density
Jline(r) =
3
X
i=1
Jline,i(r) =
3 · IL
r · ln

rin
rout
.
(19)
Thus, the magnetic skin field in a three-layer winding is
equivalent to the magnetic field induced by a single conductor
carrying three times the inductor current IL.
For this reason, the FR value of each layer can be calculated
separately according to Fig. 5, as the magnetic flux in the
core and therefore the fringing field around the air gap Hag
is excited by N · IL = 3 · IL as well. However, as the
minimum distance between the different PCB layers is limited
rag
zag,1
5
10
15
20
Current Density J (A/mm2)
Radial Position (mm)
30
0
10
20
Top Layer
Middle Layer
Bottom Layer
2
3
1
zag,2 zag,3
dL
Fig. 11. Circular inductor arrangement with multiple turns on adjacent layers
and their respective current densities JAC.
0.3
0.4
0.5
0.6
0.7
0.8
1
1
1.05
1.1
1.15
1.2
1.25
1.3
1.35
AC-DC Resistance Factor FR
fsw=10kHz
fsw=50kHz
fsw=100kHz
fsw=250kHz
fsw=500kHz
fsw=1MHz
0.9
Normalized Air Gap-Conductor Distance zag,norm
zag,3
2 3
1
zag,1
zag,2
Bottom Layer
Top Layer
Middle Layer
 Skin Effect
Proximity
   Effect
dL
Fig. 12. FR values for each layer in a multilayer PCB winding for different
frequencies fsw and different air gap positions zag,norm = zag
bw .
by manufacturing constraints, they cannot all be placed in the
optimal position zag,opt. Hence, two out of the three layers are
either slightly under- or overcompensated as shown in Fig.
11. The non-ideal current densities of the two outer layers
slightly affect their FR values as illustrated in Fig. 12, where
the top layer 1⃝lies within the proximity effect region and
the bottom layer 3⃝in the skin effect region, respectively.
However, as long as the distance between layers dL is much
smaller than the widths bw of the copper tracks, the FR values
of the different layers are almost the same and the calculated
optimal air gap position of a single layer arrangement can also
be applied to multilayer windings.
It needs to be mentioned, that the quality of the compensation
highly depends on the ratio between dL and bw, as for large
dL values the simplified assumption of a constant vertical
magnetic field throughout the PCB is not valid anymore.
Hence, the full two-dimensional field problem needs to be
solved, which is however out of the scope of this paper.
Nevertheless, in most designs dL ≪bw is ensured and the
proposed field compensation concept achieves FR values close
to one, even for multilayer windings. Thus, very efficient high
frequency PCB winding inductors for all kinds of inductance
values can be designed.
In Fig. 13, an exemplary practical implementation of such an
inductor with a multilayer PCB winding is shown. It should be
pointed out that, in order to minimize the termination losses in
the inductor, it is crucial to terminate the winding in a coplanar
way, so that a homogeneous current density in the connecting
copper tracks is achieved. In addition, the transitions between
the layers should be done by means of through-hole vias
only, as the usage of blind and buried vias increases the
manufacturing costs of PCB windings significantly.
V. CONCLUSION
In this paper, a new method of designing highly efficient
high-frequency PCB inductor windings has been introduced,
where the fringing field of a single air gap can be used

## [стр. 9]

Coplanar
Terminals
Air Gap
      Vias
(through-hole)
Ferrite Core
Fig. 13. Practical implementation of a PCB winding inductor, where the
proposed field compensation concept is applied.
in such a way, that the existing skin and proximity fields
in a PCB inductor winding are largely compensated. Thus,
compared to state-of-the-art solutions, the fringing field of an
air gap is not avoided anymore, but rather used to actively
compensate adverse high-frequency effects ("turn enemies
into friends"). Furthermore, the difficult manufacturing of
multi-air-gap and low-permeability cores can be avoided, as
a certain magnetic fringing field is desired. Consequently,
cost-effective and efficient PCB inductor windings can be
designed based on the design guidelines shown in this paper.
Additionally, the proposed H2-loss factor calculation method
allows for a fast calculation of the optimal air gap position
for all different kinds of geometries. Thus, the proposed
field compensation concept is by far not limited to standard
inductor arrangements as the ones shown in this paper.
ACKNOWLEDGMENT
The authors would like to thank the Robert BOSCH GmbH
for supporting this work.
REFERENCES
[1] A. Consoli, F. Gennaro, C. C., and A. Testa, "A comparative study of
different buck topologies for high efficiency low voltage applications,"
in IEEE Power Electronics Specialists Conference (PESC), 1999.
[2] M. Forouzesh, Y. P. Siwakoti, and B. Lehman, "Step-up dc/dc converters:
A comprehensive review of voltage-boosting techniques, topologies, and
applications," in IEEE Transactions on Power Electronics, Vol. 32, No.
12, 2017.
[3] C. R. Sullivan, "Prospects for advances in power magnetics," in International Conference on Integrated Power Electronics Systems (CIPS),
2016.
[4] B. A. Reese and C. R. Sullivan, "Litz wire in the mhz range: Modeling
and improved designs," in Conference on Control and Modeling for
Power Electronics (COMPEL), 2017.
[5] C. R. Sullivan, "Layered foil as an alternative to litz wire: Multiple
methods for equal current sharing among layers," in Conference on
Control and Modeling for Power Electronics (COMPEL), 2014.
[6] M. Nigam and C. R. Sullivan, "Multi-layer folded high-frequency
toroidal inductor windings," in Applied Power Electronics Conference
and Exposition (APEC), 2008.
[7] R. Wrobel, S. Ayat, and J. L. Baker, "Analytical methods for estimating equivalent thermal conductivity in impregnated electrical windings
formed using litz wire," in Electric Machines and Drives Conference
(IEMDC), 2017.
[8] R. M. Burkart, "Advanced modeling and multi-objective optimization
of power electronic converter systems," Ph.D. dissertation, ETH Zurich,
2016.
[9] J. Hu and C. R. Sullivan, "Ac resistance of planar power inductors
and the quasidistributed gap technique," in IEEE Transactions on Power
Electronics, Vol. 16, No. 4, 2001.
[10] W. A. Roshen, "Fringing field formulas and winding loss due to an air
gap," in IEEE Transactions on Magnetics, Vol. 43, No. 8, 2007.
[11] P. Wallmeier and H. Grotstollen, "Magnetic shielding applied to highfrequency inductors," in IEEE Industry Application Society, Annual
Meeting, 1997.
[12] M. Leibl, "Three-phase pfc rectifier and high-voltage generator for x-ray
systems," Ph.D. dissertation, ETH Zurich, 2017.
