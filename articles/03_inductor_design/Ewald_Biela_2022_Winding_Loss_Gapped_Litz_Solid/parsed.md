# source

<!-- FORMULA-WARNING -->
> **Формулы в этом файле недостоверны.** Текстовый слой PDF теряет дробные черты, радикалы и группировку степеней; знак интеграла приходит как `Z` или `R`, знак суммы -- как `P`. Формул вырезано: **54**, читать их в `formulas/` (картинки 300 dpi, перечень в `formulas/INDEX.md`).
<!-- /FORMULA-WARNING -->

> Автоматически извлечено из `source.pdf` скриптом `parse_pdf.py`
> Движок: pymupdf. Страниц: 14 из 14.
> Дата извлечения: 2026-08-07 06:43 UTC

Текст не редактировался. Формулы и таблицы могут быть искажены —
при сомнении сверяться с исходным PDF.

---

## [стр. 1]

ETH Library
Analytical winding loss and
inductance models for gapped
inductors with Litz or solid wires
Journal Article
Author(s):
Ewald, Thomas
; Biela, Jürgen
Publication date:
2022-12
Permanent link:
https://doi.org/https://doi.org/10.3929/ethz-b-000556102
Rights / license:
In Copyright - Non-Commercial Use Permitted
Originally published in:
IEEE Transactions on Power Electronics 37(12), https://doi.org/10.1109/TPEL.2022.3187155
This page was generated automatically upon download from the ETH Zurich Research Collection.
For more information, please consult the Terms of use.

## [стр. 2]

TRANSACTIONS ON POWER ELECTRONICS
1
Analytical winding loss and inductance models for
gapped inductors with Litz or solid wires
Thomas Ewald, Student Member, IEEE, J¨urgen Biela, Senior Member, IEEE,
Email: ewald@hpe.ee.ethz.ch, jbiela@ethz.ch
Abstract-In gapped inductors, the fringing field of the air
gaps causes additional eddy current losses in the windings and
an increase of the inductance. Since this impact of the fringing
field is very significant, calculating the additional eddy current
losses and the inductance increase is important in the design of
inductors. This paper proposes analytical formulas to accurately
calculate the inductance and the additional eddy current losses in
gapped inductors with solid round wire and Litz wire windings.
The analytical formulas are verified by measurements, showing
that the proposed models are accurate over a wide frequency
range.
Index Terms-Magnetic Components, Inductance, Winding
Losses, Magnetic Field, Fringing field
I. INTRODUCTION
C
OMMONLY, state of the art inductor design unites
comprehensive multiobjective optimization and virtual
prototyping, to avoid costly and time-consuming design procedures and redesigns. For this purpose, accurate and fast,
and at best analytical models are required for two things, that
are particularly important: Calculating the correct inductance
value is necessary to ensure the converter system operating
at its desired point of operation. In addition, the winding
losses determine the size of the component. In case of gapped
inductors, the non-homogeneous magnetic field (fringing field)
in the core window caused by the air gap(s), has a significant
impact on both, the inductance value and the winding losses.
This makes it necessary to consider the fringing field in the
inductance and winding loss calculation.
Analytical inductance calculation is typically based on magnetic equivalent circuits [1] to consider the impact of a finite
permeability and the increasing effective cross-section of the
air gap due to the fringing effect. Hereby, considering the air
gap fringing field takes place either by empirical correction
factors [2]-[5], where general validity is not given, or by
the Schwarz-Christoffel (SC) transformation [6], [7]. The SC
approaches show increasing errors for larger air gaps, which
was already recognized, but not correctly attributed, in [8].
On the other hand, winding loss calculation is based on
determining the frequency-dependent eddy current losses [9],
[10], which requires a 2D field calculation in case of gapped
core windows. This can be performed either with FEM [9],
or analytically [11]. Since this paper is focussed on analytical
modelling, literature references to numerical, semi-numerical,
and empirical models are omitted.
Simple analytical methods, e.g. [12], [13], are not available for gapped core windows. In the case of gapped core
windows, the mirroring method is often used to compute
the field [14], [15], which in combination with point-wise
evaluation of the resulting magnetic field formulation leads
to elevated computation times and adds complexity to the
model. Analytical expressions are not given. An accurate
analytical magnetic field formulation is presented in [16],
where a system of coefficients must be solved numerically and
numerical integration is used to obtain the losses per individual
conductor. However, numerical integration adds significant
computational effort to the model and makes implementation
complicated. Analytical formulas for the fringing field are
given in [17], [18], however, only the fringing field losses are
derived based on approximate formulas, whereas the proximity
and the skin effect losses are ignored (the question, if the loss
components are orthogonal is not addressed). Furthermore, all
modelling approaches for winding losses result in 2D perunit-length losses or inductance values, so an additional length
scaling model is necessary to obtain the total losses. In the case
of a gapped inductor, considering the 3D geometry is crucial,
since the fringing field of the air gaps is locally affecting the
winding losses differently.
The first goal of this paper is to derive a comprehensive
set of formulas for calculating the winding losses in gapped
inductors with solid round or Litz wire, where the skin, the
proximity, and the fringing effect are taken into account.
This results in closed-form winding loss formulas that are
comparable in complexity to known loss models neglecting the
fringing field [12], [13]. In contrast to mentioned literatur, this
paper proposes formulas for the actual losses by considering
the complete inductor geometry, instead of the losses per
unit length. The presented formulas are not applicable to foil
conductors, because foil conductors act as eddy current shields
a)
b)
Fig. 1.
Inductors wound on an ETD 59/31/22 core a) with high-frequency
Litz wire and b) with solid round wire and an additional coil former.

## [стр. 3]

TRANSACTIONS ON POWER ELECTRONICS
2
a)
hg
...
x
dx,o
dx,i
dw
u1 v1
uM
...
hw
y
z
dleg
rleg
u2
As
rectangular air gap region
x
leg
a
z
y
...
dx,i
rleg
x
y
z
xw,i
dx,c
xw,o
xc,i
xc,o
b)
dw
x
leg
d
z
leg
d
y
c)
d)
leg
b
Fig. 2. a) 2D core window of an E/ER/ETD type inductor. As is the rotational axis of symmetry. b) Top view of a ER/ETD type inductor with circular centre
leg used for the derivation of the length scaling. c) Top view of a E type inductor with rectangular centre leg. d) Simplified 2D core window, considering the
whole winding as a unified conductor block.
and must be modelled accordingly [19].
In addition, expressions for the inductance are derived since
the magnetic field is analytically calculated. These expressions
correctly predict the inductance value of a gapped inductor,
where the magnetic energy in the air gap, the core, and the core
window (2D fringing field and 1D layer field) are considered.
Even though methods for the inductance calculation exist,
the models proposed in this paper have notable advantages,
since they are physically connected to the Maxwell equations
and offer higher accuracy (a comparison with models from
literature and a discussion is provided in this paper).
The paper is organized as follows: In sec. II the geometry
of the considered inductor is introduced, and geometrical
parameters are given. Sec. III-V present analytical formulas
for calculating the inductance and the frequency-dependent
resistance of gapped inductors. The formulas consider the
magnetic fringing field of the air gap(s), which affects both,
inductance and resistance. In addition, an extension of the formulas to geometries with rectangular centre legs is proposed
in sec. VI. Hereby, the final formulas are provided, which
can be implemented directly using the geometrical parameters
given in sec. II - the derivations of the equations are moved to
the appendix. Finally, sec. VII verifies the model with FEM
simulations and measurements performed on two prototype
inductors, and discusses the results.
a)
b)
c)
x
d
dt
v1
u2
u3
v2
d
ra
ra
ri
ri
ra
α
ra
v1
u2
u3
v2
x
d
dt
d
ds
ri
ra
}
Ns
d
Fig. 3.
a) Depiction of the cross section of a Litz wire. b) Ideal case
of a winding arrangement of solid round wires. c) Orthocyclic winding
arrangement of solid round wires.
II. GEOMETRY OF THE INDUCTOR
The inductor that is considered in this paper is an E/ER/ETD
type inductor. The core is commercially available and the
centre leg is gapped for energy storage.
For modelling purposes, the inductor geometry is separated
into a 2D core window (cf. Fig. 2a and d) and the corresponding 1D length scaling, which is determined by the
center leg cross section (cf. Fig. 2b and c). The 2D core
window is divided into M = NEFC+1 non-conductive layers
(NCR) and NEFC equivalent foil conductors (EFC, copper
shaded in Fig. 2a), in alternating order. The EFC represent the
winding layers, where the winding is either solid round wire
or Litz wire. In each individual EFC there are Nn conductors
vertically aligned, where Nn is the number of conductors in
the n-th EFC. From that it follows that the total number
of conductors is N = PNEFC
n=1 Nn. All EFC have the same
width d (wich is also the wire diameter), the NCR next to the
centre leg (e.g. bobbin) is considered with dx,i, the distances
between the conductors are dt, and the distance between
the outermost conductor and the limb is dx,o. Moreover, for
a simpler modelling approach, Fig. 2d) shows the 2D core
window with a unified conductor block (copper shaded).
The air gaps are considered as separate regions (blue
rectangle in Fig. 2a), with the individual height hg. In case of
multiple gaps, Ng is the number of gaps, which are assumed
to be placed evenly along the centre leg surface (y-axis) with
symmetry to the x-axis (cf. app. A).
Fig. 3b) and c) show how to derive the distances d and dt
for an idealized winding and an orthocyclic winding. In case
of the idealized winding, d = 2ri, and dt = 2(ra -ri). In
case of an orthocyclic winding, α is 60◦. Hence, d = 2ri, and
dt =
√
3ra -2ri. Here, ra and ri are the radii of the copper
wire with and without insulation, respectively. In case of Litz
wire, d = 2ri is the diameter of the bundle without outer
insulation (cf. Fig. 3a), ds is the individual strand diameter,
and Ns is the number of strands in the bundle.
III. INDUCTANCE AND WINDING LOSS FORMULAS
This section provides analytical formulas to effectivly calculate the increased winding loss caused by the skin, proximity,
and fringing effect, as well as the increased inductance due

## [стр. 4]

TRANSACTIONS ON POWER ELECTRONICS
3
to the air gap's fringing field. Thereby, the derivations of the
different equations are given in the appendix, and referenced in
the respective text passage to obtain a compact presentation of
the models. The formulas in their presented form are all valid
for cores with circular centre legs (ER/ETD), and in sec. VI an
extension of the formulas to cores with rectangular centre legs
(E) is provided. Two slightly different models are proposed in
the following.
The first, called the compact model, assumes the winding to
be tightly packed (orthocyclic) and the number of conductors
to be the same in every EFC, so that the distance between conductive (EFC) and non-conductive layers dt becomes zero, and
the individual layers can be regarded as a unified conductor
(UC, copper shaded in Fig. 2d). This assumption is justified
in most applications.
The second model, called layer model, derives the magnetic
energy and the winding losses for each layer separately. This
model yields more accurate results, if there is a significantly
larger distance dt between the winding layers, which would
lead to errors in the compact model. In addition, this model
does not assume that the individual layers contain the same
number of conductors.
Both models combine a reluctance model for the inductance
of the core and the air gap (without fringing) with a model
for the magnetic energy in the core window, that is stored in
the 2D fringing field. The individual inductances are summed,
based on the fact that the inductance depends linearly on the
magnetic energy. Thereby, the partial inductance of the air gap
(and the core) is (cf. app. B)
Lg = µ0|kµ|2N 2
N 2g h2g

Vg + Ve
µ∗r

(1)
where kµ is given in (20). For cores with a high relative
permeability kµ ≈1 results. Note, that the partial inductance
of the air gap(s) may be complex, if the relative permeability
is complex (cf. app. A). The volume of the gap(s) is
Vg =
πd2
leg
4
Nghg
(2)
and the volume of the core Ve is either given, or Ve = leAe,
where Ae is the effective core cross-section.
IV. COMPACT MODEL
This model is derived based on Fig. 2d). The 1D magnetic
field increases linearly along the x-axis in the winding block
and is constant everywhere else in the core window. The
additional air gap fringing field is modelled with the 2D
solution of Maxwell's partial differential equations (PDE) in
Cartesian coordinates. This makes it possible to obtain compact analytical formulas for the calculation of the additional
fringing inductance and the eddy current losses caused by the
fringing field.
A. Inductance
As mentioned, the total inductance L is determined by
summing individual energy contributions, namely of the air
gap(s) and the core Lg, and the core window. Hereby, the
energy in the core window is theoretically further divided into
the energy stored in the fringing field Lf and the energy in the
1D field between the layers L1D. The typical contribution of
Lf to the overall inductance value is difficult to quantify, as
it strongly depends on the geometry. In [6], [7] it contributes
between 6 % to 41 %. However, the contribution of L1D of
the 1D layer field is in the low percentage range for a gapped
inductor, which makes it justifiable to neglect L1D. For the
sake of completeness, it is derived in app. D and can be added
to (3). The total inductance is then
L = Lg + Lf
(3)
As shown in app. D, the partial inductance Lf of the air gap
fringing field can be calculated by the formula
Lf = 2πhw
µ0
∞
X
k=1
ck(xw,i, xw,o)|Ck|2 + dk(xw,i, xw,o)|Dk|2
(4)
with xw,i and xw,o depicted in Fig. 2d),
Ck = -
2µ0kµN
pkhw (1 -e-2pkdw) si

pk
hg
2

Dk = Ck e-2pkdw
(5)
where si(x) = sin(x)/x, pk = 2πkNg/hw, and
ck(x1, x2) =

-e-2pk(x-u1) (2pkx + 1)
4
x2
x1
dk(x1, x2) =
e2pk(x-u1) (2pkx -1)
4
x2
x1
(6)
B. Resistance of solid round wire
The effective AC resistance of the inductor, as derived in
app. E and G, is:
R = RDC

FR + GR
LUC
µ0VUC

(7)
Here,
LUC = µ0πN 2
hw
x2
c,o + 2xc,ixc,o -3x2
c,i
6
+ 2πhw
µ0
∞
X
k=1
ck(xc,i, xc,o)|Ck|2 + dk(xc,i, xc,o)|Dk|2
(8)
is the partial inductance of the unified conductor block, the
coefficients Ck and Dk are given in (5), the functions ck and
dk are given in (6), and
FR = 1
2 Re
αI0(α)
I1(α)

GR = π2d2 Re
αI1(α)
I0(α)

α = (1 + j) d
2δ
(9)
are based on [20]. The function Iν is the modified Bessel
function of the first kind and the ν-th order. In there, δ, ω,

## [стр. 5]

TRANSACTIONS ON POWER ELECTRONICS
4
σ, and µ0 are the skin depth, angular frequency, conductivity,
and vacuum permeability, respectively. Furthermore,
RDC = 4N (xc,o + xc,i)
σd2
is the DC resistance of the winding and
VUC = πhw
 x2
c,o -x2
c,i

(10)
is the volume of the unified conductor block (cf. Fig. 2d).
C. Resistance of Litz wire
In case of Litz wire, the formula for the effective AC
resistance of the inductor is (cf. app. H and J):
R = R′
DC

F ′
R + G′
R
 LUC
µ0VUC
+
1
2π2d2

(11)
with LUC (8), Ck and Dk (5), ck and dk (6). Moreover,
F ′
R = 1
2 Re
α′I0(α′)
I1(α′)

G′
R = π2d2
sN 2
s Re
α′I1(α′)
I0(α′)

α′ = (1 + j) ds
2δ
R′
DC = 4N (xc,o + xc,i)
σd2sNs
(12)
and VUC is given in (10).
The compact model typically underestimates the additional
losses caused by the fringing field, which is caused by the
fact that the magnetic energy between layers is considered
in the field averaging. The expected error increases with the
insulation distance dt, which makes (7) and (11) only viable
for comparatively small insulation distances.
Further note, that in this context app. G and J derive the
loss components R1D and Rf separately, which might be
interesting in some applications, and is used in sec. VII to
show the impact of the individual components on the total
losses of the inductor.
V. LAYER MODEL
This model is derived based on the geometry in Fig. 2a)
and Fig. 3b) & c). The 1D magnetic layer field is assumed
to increase linearly inside each EFC, but is constant in the
NCR between the EFC. For larger distances dt this is more
accurate, since the non-zero distances have a significant impact
on the magnetic field averaging used in this paper, which
slightly affects the inductance and can cause significant errors
in the resistance calculation with the compact model. The air
gap fringing field is modelled with the 2D solution of the
Maxwell equations in Cartesian coordinates. However, due to
the discontinuous function of the 1D layer field, all formulas
must be evaluated per layer, resulting in more complicated
formulas.
A. Inductance
Since with this model the inductane for each layer (NCR
and EFC) is described, the inductance is given as the sum of
the partial inductances of the air gap(s) (1) and the partial
inductances of the individual layers (14), derived in app. C:
L = Lg +
M
X
m=1
L(NCR)
m
+
NEFC
X
n=1
L(EFC)
n
(13)
Here, (13) considers the magnetic energy stored in the air gaps,
in the fringing field of the air gaps, and in the winding layers,
which makes it different than (3), and e.g. [7], where the
contribution of the 1D layer field is ignored. The contribution
of the partial layer inductances is typically a bit higher than
(4). From app. C, the partial inductance of the m-th NCR and
the n-th EFC is:
L(NCR)
m
= 2πhw
µ0

B2
m,0dm
dm
2 + um

+
∞
X
k=1
ck(um, um + dm)|Ck|2 + dk(um, um + dm)|Dk|2

L(EFC)
n
= 2πhw
µ0

C2
n,0d3

d + 4vn
3

+ 2Cn,0Dn,0d2
2d
3 + vn

+ D2
n,0d
d
2 + vn

+
∞
X
k=1
ck(vn, vn + d)|Ck|2 + dk(vn, vn + d)|Dk|2

(14)
where the functions ck and dk are given in (6), and the
coefficients Ck and Dk are given in (5), and
Cn,0 = -µ0Nn
2dhw
Dn,0
(n=m)
=
Bm,0 = µ0
hw
NEFC
X
i=m
Nm
The parameter dm in (14) refers to the width of the m-th NCR
and is either dx,i, dt, or dx,o.
B. Resistance of solid round wire
The total effective AC resistance of the inductor, as derived
in app. E and F, is:
R =
NEFC
X
n=1
RDC,n

FR + GR
L(EFC)
n
µ0Vn
!
(15)
with L(EFC)
n
from (14), FR and GR from (9), the DC resistance of the n-th layer
RDC,n = 4Nn (2vn + d)
σd2
and its volume
Vn = πdhw (2vn + d)
(16)
C. Resistance of Litz wire
In case of Litz wire, the total effective AC resistance, as
derived in app. H and I, is given as
R =
NEFC
X
n=1
R′
DC,n

F ′
R + G′
R

L(EFC)
n
µ0Vn
+
1
2π2d2
!!
(17)

## [стр. 6]

TRANSACTIONS ON POWER ELECTRONICS
5
with L(EFC)
n
from (14), F ′
R and G′
R from (12), the DC
resistance of the n-th layer
R′
DC,n = 4Nn (2vn + d)
σd2sNs
and its volume Vn given in (16).
VI. EXTENSION TO RECTANGULAR CENTRE LEGS
To consider rectangular centre legs, a different length scaling of the layer is required. In order to make use of the
already obtained results from app. C, a coefficient krect is
defined, that establishes a relation between the circumferences
C of a rectangle and a circle. In the following it is assumed,
that the geometry has a rectangular cross-section with width
bleg = dleg and depth aleg, as given in Fig. 2c). Then,
krect = Crect
Ccirc
= 4
π

1 + aleg -bleg
4rx

where rx is the geometric mean radius of the respective
layer to the origin (e.g. rx = v1+d/2 for the first EFC, cf.
Fig. 2a). Every layer that is considered in the calculation (NCR
and EFC) must be adjusted by its respective coefficient. The
coefficients are used to scale the partial inductances of the
core window, (4), (8), and (14), and the resistances, (7), (11),
(15), and (17). Note, that in the resistance formulas, terms
that contain any partial indcutance must not be scaled, to
avoid double-scaling. In addition, the volume of the air gap is
different for a rectangular centre leg:
Vg = blegalegNghg
which must be replaced in (1). This procedure was successfully
applied and verified in [19].
VII. VERIFICATION
The models are verified in two steps. First, FEM simulations
are conducted to show the models accuracy by comparing the
analytical derivations with a 2D axis-symmetric FEM model in
sec. VII-A. In a second step, measurements are performed with
prototype inductors, which are compared to analytical results
of the winding losses and the inductance values in sec. VII-B.
If not stated otherwise, the layer model is used for verification
purposes.
TABLE I
FE MODELS WITH SOLID ROUND (FE 1) AND LITZ WIRE (FE 2)
FE 1
FE 2
Description
ETD 59/31/22 ETD 29/16/10
Core type
dx,i
1
1 mm Dist. centre leg to 1. EFC
hg
2
2 mm Air gap height
NEFC
3
1
# of EFC
Nn
35
11
# of cond. per EFC
d
0.8
1.65 mm Cond. thickness
dt
0.4
-mm Inter-layer distance
Ns
-
37
# of strands
ds
-
0.1 mm Strand diameter
A. Verification with FEM
The inductance and the resistance factor R/RDC are studied
over a wide frequency range. Two finite element models are
set up, one with solid round wire, and one with Litz wire. The
geometrical specifications of the FE models are given in Tab. I
and are based on commercially available cores. To obtain
comparable results, the frequency range for both FE models
is adjusted, so that the parameter sweep covers the range of
∆from 0.1 to 10, where ∆= d/δ is the relation of the
respective wire/strand diameter to the skin depth. The assumed
temperature is 20 ◦C. Fig. 4 shows the results. The error of
the proposed models arising at high frequencies originates
from the fact, that the underlying model for the magnetic
field in the core window (outside the conductors) neglects any
high-frequency effects due to the current displacement in the
conductors. However, the magnitude of the error is shown to be
comparatively low. The results prove, that the model predicts
the losses of the inductor accurate even at high frequencies.
Fig. 4a) compares the proposed inductance models with
FEM simulations of inductor 1 (FE 1) from Tab. I. It is
shown, that the inductance decreases in FEM simulations at
high frequencies. This effect is caused by the inhomogeneous
magnetic field inside the conductors, which is not considered
in the inductance calculation. This effect is usually negligible
in round or Litz wires, since their typical design criterium is
∆≤1. However, the overall change of the inductance value
at ∆= 10 is -6.2 %, which is not negligible. A model for
the analytical compensation of this effect is retained for future
a)
0.1
1
10
3.25
3.35
3.45
3.55
-6.2 %
1.9 %
-1.1 %
∆
L in mH
FEM vs. ∆
FEM ∆=10
L
ALN 2
b)
0.1
1
10
100
101
102
103
∆
R/RDC
FEM
R
Rf
R1D
c)
0.1
1
10
∆
R/RDC
FEM
R
Rf
R1D
Fig. 4. Comparison of the proposed models with 2D axis-symmetric FEM simulations. a) Model FE 1 from Tab. I: L refers to (13), ALN2 is the inductance
according to manufacturer's data. b) FE 1 from Tab. I: Resistance factor R/RDC of the total resistance R (15), and of the partial resistances Rf (38) and R1D
(37). The frequency ranges from 66.5 Hz to 665 kHz. c) FE 2 from Tab. I: R/RDC of the total resistance R for Litz wire (17), and the partial resistances Rf
(41) and R1D (40). The frequency ranges from 4.26 kHz to 42.6 MHz.

## [стр. 7]

TRANSACTIONS ON POWER ELECTRONICS
6
publication.
Fig. 4b) compares the proposed resistance models with
FEM simulations of FE 1 from Tab. I. The results show,
that the proposed model predicts the winding losses accurately. Nevertheless, since the inductance model overestimates
the inductance by neglecting the counteracting effect of the
conductor's magnetic field, the resistance model consequently
overestimates the winding losses. The maximum error is
14.2 % at ∆= 10, the average error is 1.8 %. In addition, the
partial resistance factors based on the newly proposed fringing
field model (38) and the existing 1D model (37) are plotted,
to show the individual contributions to the calculation.
Fig. 4c) shows the comparison of the proposed models with
FEM simulations of inductor 2 (FE 2) from Tab. I. Here,
the maximum error occurs at ∆= 5 and is 14.9 %. The
average error is 3.5 %. In addition, the individual contributions
are shown with the resistance increase caused by the air gap
fringing field (41) and the 1D field assumption (40).
B. Verification with measurements
Two prototype inductors are made with the commercial
core, as specified in Tab. II and shown in Fig. 1, made
from Epcos N87 ferrite. Inductor 1 (IND 1) has a solid
round wire winding with an additional bobbin, the Litz wire
winding of inductor 2 (IND 2) is wound directly around the
centre leg without an additional bobbin. The measurements are
performed at room temperature. The resistance measurements
are done with an impedance analyzer Keysight E4990A. To
avoid variations, the impedance analyzer was configured to
take the average of five values per frequency point. In addition, multiple frequency sweeps were performed. Regarding
measurement accuracy, it can be concluded that the overall
measurement error is below 1 % between 1 kHz and 1 MHz,
according to the manufacturer's data sheet and the inductor
specifications. The inductance is measured with a power choke
tester DPG10 from ed-k (step voltage method).
The calculated inductances of both inductors are compared
to the measured values given in Tab. III, along with the
calculated error. For comparison, the inductance resulting from
TABLE II
INDUCTORS WITH SOLID ROUND (IND 1) AND LITZ WIRE (IND 2)
IND 1
IND 2
Description
ETD 59/31/22 ETD 59/31/22
Core type
hg
2
2 mm Air gap height
NEFC
3
3
# of EFC
Nn
21
16
# of cond. per EFC
d
1
2.3 mm Conductor (bundle) diameter
Ns
-
60
# of strands
ds
-
0.25 mm Strand diameter
Cres
29.6
42.7 pF
Measured capacitance
the AL value is given, which is very accurate. However, this
is not surprising, since the manufacturer measures this value
as well. Nevertheless, for custom cores the AL-value is not
available. The comparison with (1) shows, that neglecting the
fringing field yields significant errors of approximately -25 %.
The stray capacitance of the inductor is determined via a
measurement of the first resonant frequency fres = ωres/2π as
Cres = 1/(ω2
resL) (measured with a floating core) and added to
the analytical impedance model:
Z =

(R + jωL)-1 + jωCres
-1
(18)
Note, that in the above equation the inductance may be
complex (cf. app. A). Then,
jωL = jω (L′ -jL′′) = jωL′ + Rc
(19)
which means, that the imaginary part of the inductance resembles a core loss resistor Rc = ωL′′ depending on the frequency
and the imaginary part of the relative permeability.
TABLE III
COMPARSION OF CALCULATED AND MEASURED INDUCTANCE VALUES
Inductor
L meas.
L (13)
L (3)
L (1)
ALN2
IND 1
1.23 mH
1.28 mH
1.29 mH
0.92 mH
1.23 mH
(Err.)
-
3.9 %
4.0 %
-25.6 %
0 %
IND 2
745 µH
740 µH
740 µH
531 µH
717 µH
(Err.)
-
-0.7 %
-0.7 %
-28.7 %
-3.8 %
a)
103
104
105
106
100
102
104
106
∆= 1
∆= 5
f in Hz
R/RDC
Measurement
Re {Z1}
Re {Z2}
Rf
Rc
R1D
b)
103
104
105
106
100
102
104
106
∆= 1
f in Hz
R/RDC
Measurement
Re {Z1}
Re {Z2}
Rf
Rc
R1D
Fig. 5. Comparison of the proposed models with measurements performed with an impedance analyzer. a) Calculated resistance factor R/RDC of IND 1:
Z1 refers to (18) computed with (13) and (15), Z2 is computed with the compact models (3) and (7), in addition the partial resistances Rf (38) and R1D
(37), and Rc (19), which is the core resistor. b) R/RDC of IND 2: Z1 is computed with (13) and (17), the compact models (3) and (11) are used to compute
Z2, and the partial resistances are calculated using (41), (40), and (19). Note, that the partial resistance R1D is equivalent to models from literature [12],
[13], which neglect the presence of an air gap. It is noteable, that the neglection of an air gap results in significant underestimation of the overall resistance
increase vs. frequency.

## [стр. 8]

TRANSACTIONS ON POWER ELECTRONICS
7
Fig. 5a) compares the calculated resistance factor of IND 1
with the measured values. Up to a relation of the wire diameter
and the skin depth of ∆= 5 (f = 106 kHz), the results match
the measurement well. The average error for ∆≤5 of (15)
is 2.6 % and the average error of (7) in the same frequency
range is 1.2 %.
Fig. 5b) compares the calculated resistance factor of IND 2
with Litz wire to the measured values. Again, the results match
well. However, the calculated error is notably higher. The
average error of (17) for ∆≤1 (f = 68 kHz) is 9.7 % and the
average error of (11) in the same range is 9.7 % as well. Note,
that the Litz wire winding was assumed to be orthocyclic with
comparatively thin outer insulation, which led to a calculated
value of dt ≈0. Hence, (17) and (11) yield the same results.
The error over the full depicted range is 11.9 %.
Overall, the prediction of the effective resistance is very
accurate for IND 1 up to 106 kHz (∆= 5), and the predicted
effective resistance of a Litz wire winding (IND 2) is accurate
up to at least 68 kHz (∆= 1). Since Litz wire is specifically
used in scenarios where ∆< 1, this proves the model's accuracy. As Fig. 5a) shows a notable deviation above 100 kHz,
it needs to be evaluated whether the results can be used to
validate the model, which is done in sec. VII-C.
C. Deviation of measurements and analytical model
Fig. 5a) shows an increased error at frequencies above
100 kHz, which is not reproducible with FEM simulations
(cf. sec. VII-A). This leads to the conclusion that this error
is caused either by an erroneuous capacitance or by miscalculated core losses. Nevertheless, the model can already be
considered validated in the frequency range below 100 kHz
(cf. sec. VII-B). In the following, the error is examined more
closely for the frequency ranges below and above 100 kHz.
Generally, the impedance analyzer predicts the amplitude
and phase of the devices under test (DUT) accurately (error
less than 1 % according to manufacturer's data sheet, depends
on the design). Exceptions might be the frequency range
around the resonant frequency (which is not the desired operating point), where the measured current is low (extracted from
measurement at res. freq.: 31 µA), and very low frequencies,
where the reactive part is comparatively small (below 100 Hz,
barely measureable phase angle). The measured values of
amplitude and phase must be interpreted physically with an
equivalent circuit model. In this paper, this is done according
to (18).
The measured resistance is in fact the real part of the
measured impedance. It contains the winding loss, core loss,
and the capactitance. The capacitance plays a role in the frequency range around the resonant frequency and its influence
can be modelled accurately with the measured capacitance
Cres. Below 1/10 of the resonant frequency (slightly below
100 kHz in Fig. 5) the capacitance can typically be neglected.
Characterization of the core loss is a bit more complicated: An
N87 core was selected, which is manufactured to have low
core losses below 100 kHz (this can be concluded from the
imaginary part of the permeability vs. frequency, cf. Fig. 7).
Furthermore, the data sheet of the material gives the core
losses at 100 kHz to be around 0.23 W (25 mT, 25 ◦C) for
the core under test. For the DUT (IND 1), a flux density
of 25 mT would require an exciting current of 0.66 A, which
would lead to expected winding losses of 5.5 W at 100 kHz.
Hence, the relation of the core losses to the winding losses
is approximately 4 % at 100 kHz. The actual value of the flux
density extracted from the measurement is 25 µT (no data is
given for such a low excitation in the data sheet). Since the
winding losses scale with the squared current, the core losses
scale with the squared flux density in first approximation, and
current and flux density have a linear relation (assuming no
saturation), the relation of winding and core losses should not
change for changing excitation. Eventually, it can be concluded
that capacitance and core losses can be neglected below a
frequency of 100 kHz in case of IND 1.
For frequencies far above 100 kHz, the manufacturer does
not provide accurate data for the core losses, and capacitive effects become dominant. Therefore, the frequency range above
100 kHz is not considered for the verification of the model.
Eventually, a different method to characterize the total inductor
losses in the higher frequency range (above 100 kHz in this
case, depending on the material and the DUT specifications) is
necessary, since the impedance analyzer measurement misses
the opportunity to separate the relevant loss mechanisms.
For this purpose, the authors of [21], [22] combine different
measurement methods (e.g. the B-H loop measurement [23]
for core loss characterization) to separate winding and core
losses.
D. Motivation of the proposed inductance model
Since the proposed inductance models in this paper, i.e. (3)
and (13), require more complicated calculations than existing
models from literature, it is compared to those models, in order
to show that its use will produce more accurate and reliable
results. In comparison, simple empirical formulas, e.g. [4],
[20], offer a practical and easy to use way to incorporate
the air gap fringing paths into the inductance calculation.
However, the scope of application of empirical models in
terms of geometrical restrictions cannot be defined. This raises
the question of the reliability of the results obtained with
those models. Physically proven concepts, e.g. [6], [7], have
the advantage of having a clear relation to the Maxwell
equations. However, it was found that models based on the
SC transformation tend to underestimate the reluctance when
the air gap becomes larger compared to the core window
height and the width of the centre leg. This observation is
based on the fact that the magnetic potential on the edge
of the ferromagnetic material is assumed to be linear in the
derivation of the equations, which is an approximation that
depends strongly on the geometrical relations of the centre
leg width and height, and the air gap height.
A study was performed, where the proposed model (13)
and the models from mentioned literature were compared to
a FEM model based on the parameters of Tab. I, but with
infinite relative permeability so that the air gap reluctance is
simultaneously the overall reluctance. A circular centre leg
was assumed, so from [7] the correction factor σr for circular

## [стр. 9]

TRANSACTIONS ON POWER ELECTRONICS
8
1
1.5
2
2.5
3
0
10
20
hg in mm
E in %
Proposed model
Ref. [7]
Ref. [4]
Fig. 6. Relative error of different inductance models compared to an FEM
study with infinite relative permeability.
centre legs was used - on the model presented in [4] this
has no impact. The results are shown in Fig. 6 as the relative
error E = 100(L/LFEM -1)%. There, it can be seen that the
empirical formula of [4] accurately predicts the inductance for
any air gap size. However, as mentioned, formulas of this kind
lack the physical derivations, hence, it is not possible to state
general validity. The model from [7] shows increasing errors
for larger are gap sizes, where the sizes are still well in the
range of actually manufactured cores. An error of 15 % was
also reported in [8] for an air gap of 3.18 mm, using [7]. This
matches the results from Fig. 6 well. Finally, even though (13)
slightly underestimates the inductance, it can be stated that the
proposed formula accurately predicts the inductance for any
air gap size.
VIII. CONCLUSION
This paper derives a detailed analytical model for the
magnetic field inside the core window of gapped inductors.
The magnetic field model is used to develop analytical models
for the inductance and, based on existing models, for the
winding losses in solid round wire windings or Litz wire. The
resulting formulas allow to predict the increased inductance
and winding losses, caused by skin, proximity, and fringing
effects, while considering a finite permeability, and cores with
circular or rectangular centre legs. The resulting model is
capable of predicting the inductance of a prototype inductor
within 4 % and the winding losses within 10 %, which is
validated by measurements.
APPENDIX A
MODEL DERIVATION IN CARTESIAN COORDINATES
In the following, derivations for a closed-form formulation
of the magnetic field in the core window are presented. The
analytical solution is obtained by directly solving the Maxwell
equations. The following assumptions are applied:
1) The core material is ideal: µr →∞
2) Magneto-quasi-static calculations: ∇×⃗H =⃗J
3) Harmonic time dependency: d/dt →jω
4) The core window is infinitly long in z-direction
5) The current density in the conductors is spatially constant
Note, that assumption 1) is applied only while solving the PDE
in the core window, otherwise the permeability is taken into
account, cf. Eq. (20). Furthermore, assumption 4) is applied
for deriving the 2D fields, and later dropped for the quasi3D integration of the fields around the circumference of the
soleniodal winding. Note, that the magnetic field in the core
window is assumed to be unaffected by the eddy currents in the
conductors. This is a necessary assumption to obtain analytical
solutions. An iterative procedure to incorporate the interactions
between magnetic field and eddy currents is described for
example in [10].
The magnetic field strength in the air gap, for a ferromagnetic core material with finite permeability µr, is:
Hg = kµ
N ˆI
Nghg
with
kµ =
1
1 +
le
µrNghg
(20)
where it is assumed that the average magnetic flux densities,
in the core and inside the air gaps respectively, are the same
and spatially constant (only a y-component, independent of the
position). Here, the effective magnetic path length le is known
(either given by the manufacturer or calculated accordingly
[24]).
In (20), the relative permeability of the core may be complex. In that case µr = µ′
r -jµ′′
r [25], where µ′
r and µ′′
r are
the real and the imaginary part of the complex permeability.
Fig. 7 shows the complex permeability as a function of the
frequency for the material N87. In case of a complex relative
permeability, the inductance becomes complex:
L = L′ -jL′′
where L′ and L′′ are the real and imaginary part of the
inductance.
The magnetic field and flux density in the core window
depend on the position (x, y). The current, the current density,
and the magnetic potential are defined to have only components in z-direction, since they are perpendicular to the
magnetic field. The magnetic potential is obtained by solving
the Laplace and the Poisson equation in the NCR and in the
EFC:
∇2⃗A(NCR) = 0
∇2⃗A(EFC) = -µ0Jn
(21)
where Jn = Nn ˆI/(dhw) is the spatially constant current
density of the n-th EFC. Expressions for the magnetic potential
103
104
105
106
100
102
104
f in Hz
µr
µ′
r
µ′′
r
Fig. 7.
Real and imaginary part, µ′
r and µ′′
r respectively, of the complex
permeability of the material N87, extracted from the manufacturer's data sheet
for B = 25 mT (small signal excitation) and T = 25 ◦C.

## [стр. 10]

TRANSACTIONS ON POWER ELECTRONICS
9
that satisfy (21) in the m-th NCR and the n-th EFC are:
A(NCR)
z,m
= Bm,0 ˆI(x-um)
+
∞
X
k=1

Ck e-pk(x-u1) +Dk epk(x-u1)
ˆI cos(pky)
A(EFC)
z,n
= Cn,0 ˆI(x-vn)2 + Dn,0 ˆI(x-vn)
+
∞
X
k=1

Ck e-pk(x-u1) +Dk epk(x-u1)
ˆI cos(pky)
(22)
where um and vn denote the x-references of the respective
layer, so that u1 = dleg/2 (cf. Fig. 2). The magnetic potential
is composed of two components: The terms indicated by 0
represent the magnetic field and satisfy the Laplace/Poisson
equation in the respective layer, as well as Ampere's law
for an air gap in the centre leg and ideal core material (the
MMF is absorbed by the air gap). The sum terms indicated
by k satisfy the Laplace equation. To satisfy Ampere's law,
magnetic field's y-component on the boundary between air
gap(s) and core window is assumed to be (20) and is used as
boundary condition to solve the PDE inside the rectangular
core window. This procedure is already used in the literature
[16], [26].
The flux density components for the NCR and the EFC are
calculated with⃗B = ∇×⃗A:
Bx = -
∞
X
k=1
pk

Ck e-pk(x-u1) +Dk epk(x-u1)
ˆI sin(pky)
B(NCR)
y,m
= -Bm,0 ˆI
+
∞
X
k=1
pk

Ck e-pk(x-u1) -Dk epk(x-u1)
ˆI cos(pky)
B(EFC)
y,n
= -(2Cn,0(x-vn) + Dn,0) ˆI
+
∞
X
k=1
pk

Ck e-pk(x-u1) -Dk epk(x-u1)
ˆI cos(pky)
(23)
The expressions for the magnetic field (23) are used in the following to derive the necessary coefficients, based on Gauss's
law, which states that the magnetic field and the flux density
must be continuous at adjacent boundaries, if the relative
permeability is the same in both layers. This is approximately
true for air and any conductive, non-ferromagnetic material
(e.g. copper).
To satisfy the boundary conditions of the magnetic flux
density Bx(x, -hw/2) = Bx(x, hw/2) = 0, it follows, that
pk = 2πkNg
hw
Since eq. (23) for the y-component of the flux density must
satisfy Ampere's law for an arbitrary number of k (also zero),
the coefficient Bm,0 for the m-th NCR is given as:
Bm,0 ˆI = µ0 ˆI
hw
NEFC
X
i=m
Nm
⇒
Bm,0 = µ0
hw
NEFC
X
i=m
Nm
where ˆI is the peak amplitude of the sinusoidal current.
Substituting (22) into (21) directly yields:
Cn,0 ˆI = -µ0Jn
2
⇒
Cn,0 = -µ0Nn
2dhw
Lastly, the solution for the coefficients Dn,0 is obtained with
the fact, that the y-component of the flux density at the
boundary of the m-th NCR and the n-th EFC (n = m, x = vn)
must be continuous:
Dn,0
(m=n)
=
Bm,0
The spatial coefficients (indicated by k) are obtained by solving the boundary value problem (core window) in rectangular
coordinates. The air gap field (20), which is known at the
boundary between the air gap and core window, is decomposed
into a Fourier series, as shown in [16] and [27]. This yields
(Ck -Dk) ˆI = -2µ0kµN ˆI
pkhw
si

pk
hg
2

 Ck e-pkdw -Dk epkdw ˆI = 0
(24)
where si(x) = sin(x)/x. Reformulating (24) yields:
Ck = -
2µ0kµN
pkhw (1 -e-2pkdw) si

pk
hg
2

Dk = Ck e-2pkdw
APPENDIX B
PARTIAL AIR GAP INDUCTANCE
The partial inductance of the air gap (including the core),
neglecting any fringing, is derived from the magnetic energy
that is stored in the gap (and the core), and the volume of the
gaps (and the core). In case of a finite permeability, which
may also be complex, µr denotes the relative permeability of
the core. Then, the partial inductance is:
Lg = VgBgH∗
g
ˆI2
+ VeBcH∗
c
ˆI2
= µ0
ˆI2 |Hg|2

Vg + Ve
µ∗r

(25)
where H is the magnetic field strength, B is the magnetic
flux density, V is the volume, and ˆI is the current (amplitude
value). Moreover, the index g denotes variables associated with
the air gap(s), and the index c denotes variables of the core.
It is assumed that Bg = µ0Hg, Bc = Bg, and H∗
c = B∗
c/µ0µ∗
r.
Furthermore, Vg is given in (2) and the core volume Ve is
assumed to be known. Substituting (20) into (25) yields (1).
Hereby, the magnetic field in the air gap(s) is assumed to be
homogeneous and constant, thus independent of the (x, y)-
position inside the air gap region (cf. Fig. 2a).
APPENDIX C
PARTIAL MAGNETIC LAYER ENERGY AND INDUCTANCE
For the calculation of the magnetic energy, an accurate
length scaling for each layer is used, according to Fig. 2b):
W =
1
2µ0
ZZZ
x |⃗B|2 dx dy dz
(26)
For this purpose, the coordinate system is changed to polar
coordinates and the integration in z-direction is replaced by
integration along the circumference (note x in the integrand).

## [стр. 11]

TRANSACTIONS ON POWER ELECTRONICS
10
With (23), the analytical expressions of the magnetic flux
density in the m-th NCR and in the n-th EFC are given.
Performing the integration yields the magnetic energy in the
m-th NCR and the n-th EFC, respectively:
W (NCR)
m
= πhw ˆI2
µ0

B2
m,0dm
dm
2 + um

+
∞
X
k=1
ck(um, um + dm)|Ck|2 + dk(um, um + dm)|Dk|2

W (EFC)
n
= πhw ˆI2
µ0

C2
n,0d3

d + 4vn
3

+ 2Cn,0Dn,0d2
2d
3 + vn

+ D2
n,0d
d
2 + vn

+
∞
X
k=1
ck(vn, vn + d)|Ck|2 + dk(vn, vn + d)|Dk|2

Here, the parameter dm refers to the width of the m-th NCR
and is either dx,i, dt, or dx,o, the coefficients Ck and Dk
are given in (5), and the functions ck(x1, x2) and dk(x1, x2)
are given in (6). There, the coordinates x1 and x2 enclose
the considered layer, with x2 > x1, and the origin of the
core window u1, defined according to Fig. 2. The partial layer
inductance is
L = 2W
ˆI2
(27)
eventually leading to (14).
An important finding here is, that the contributions of
the 1D layer field and the 2D air gap fringing field to
the magnetic energy are separated in the end result (the
terms indicated by 0 and the infinite sum indicated by k),
because all terms containing an integral along y-direction over
cos(pky), sin(pjy) sin(pky), or cos(pjy) cos(pky) vanish in
the integration over y in the limits from -hw/2 to hw/2, due to
the orthogonality of the trigonometric functions. This means
that these contributions can be considered separately, e.g. by
two separate formulas:
W = W1D + Wf
(28)
where W1D and Wf denote the 1D layer field and the 2D air
gap fringing field, respectively.
APPENDIX D
SEPARATED LAYER AND FRINGING INDUCTANCES
As shown in the previous section, the magnetic energy,
and therefore the partial inductance caused by the 1D layer
field and the air gap fringing field are separable. Hence, the
magnetic energy in the core window Wf, that is caused by the
2D fringing field, is:
Wf = πhw ˆI2
µ0
∞
X
k=1
ck(xw,i, xw,o)|Ck|2 + dk(xw,i, xw,o)|Dk|2
(29)
where the functions ck and dk, given in (6), consider the xdimension of the complete core window. Substituting (29) into
(27) eventually leads to (4).
Since (29) considers the 2D air gap fringing field, but not
the 1D layer field, the magnetic energy of the latter one is
calculated additionally as:
W1D = µ0
2
πN 2 ˆI2
hw

x2
c,o
6
+ xc,ixc,o
3
+ x2
c,i
2
-x2
w,i
!
(30)
where (31) and (32) are added, which consider the magnetic
energy contributions from the UC, and the NCR between the
centre leg and the UC. The 1D magnetic field between the UC
and the outer limb is zero, hence, no magnetic energy from the
field is stored there. The individual contributions are derived
as follows: A 1D magnetic flux density is assumed in the UC
(dt = 0) in Fig. 2d), which is defined according to (23), where
the x-dependent 1D magnetic flux density is given as:
B(UC)
y
= µ0N ˆI
hw
 x-xc,i
xc,o-xc,i
-1

Calculating the magnetic energy according to (26) yields
W (UC) = µ0
2
πN 2 ˆI2
hw
x2
c,o + 2xc,ixc,o -3x2
c,i
6
(31)
Furthermore, again using (23), the x-independent 1D magnetic
flux density in the NCR between centre leg and the UC is given
as
B(NCR)
y
= -µ0N ˆI
hw
Hence, the energy contribution WNCR of the NCR between
centre leg and the UC, using again (26), is:
W (NCR) = µ0
2
πN 2 ˆI2
hw
 x2
c,i -x2
w,i

(32)
The inductance L1D caused by the 1D layer field is then given
by substituting (30) into (27).
APPENDIX E
EFFECTIVE AC RESISTANCE CALCULATION
In the following, the effective AC resistance is calculated
based on formulas from [20], which results in models comparable to known models [12], [13]. A general formula for the
power loss of a round conductor carrying a sinusoidal current ˆI
(amplitude), and exposed to a spatially homogeneous external
magnetic field ˆHext of the same frequency, is:
P =
ˆI2
σπd2 Re
αI0(α)
I1(α)

+ 2π ˆH2
ext
σ
Re
αI1(α)
I0(α)

(33)
where Iν is the modified Bessel function of the first kind of
order ν, σ is the conductivity of the material, d is the diameter
of the wire, and α is given in (9). Formula (33) can be rewritten
in terms of the DC resistance of the wire RDC = 4/σπd2, such
that
P = 1
2RDCFR ˆI2 + 1
2RDCGR ˆH2
ext
(34)
where FR and GR are unitless factors to take into account the
additional losses caused by the skin effect and an external
magnetic field
ˆHext (proximity losses), both given in (9).
The squared external magnetic field amplitude ˆH2
ext can be
expressed in terms of its spatial r.m.s. value ˆH2
rms, that can

## [стр. 12]

TRANSACTIONS ON POWER ELECTRONICS
11
be derived from the stored magnetic energy in a volume of
consideration in the core window:
ˆH2
ext = ˆH2
rms = Lp ˆI2
µ0Vp
(35)
where Vp is the considered volume and Lp is its partial inductance. Substituting (35) into (34), and dividing the result by
ˆI2/2 (r.m.s. value of the current) yields a compact expression
for the effective AC resistance:
R = RDC

FR + GR
Lp
µ0Vp

(36)
APPENDIX F
AC RESISTANCE - LAYER MODEL
The expressions for the partial magnetic energy of each
layer, previously obtained in app. C, are substituted into (27)
to obtain the partial inductance L(EFC)
n
of the n-th EFC, given
in (14). Substituting the partial inductance into (36) results in
the resistance of the n-th EFC:
Rn = RDC,n

FR + GR
L(EFC)
n
µ0Vn
!
where RDC,n is the DC resistance of the respective layer and
Vn is its volume. Eventually, the sum over all NEFC EFC
yields the total resistance of the inductor, leading to (15).
APPENDIX G
AC RESISTANCE - COMPACT MODEL
In app. C it is shown, that the magnetic energy contributions
of the 1D layer field and of the 2D fringing field can be split
into two components: The energy stored in the 1D field W1D
and the energy stored in the 2D fringing field of the air gap(s)
Wf (28). Moreover, if it is assumed that the winding is tightly
packed (orthocyclic) and the number of conductors is the same
in every EFC, the individual layers can be regarded as a unified
conductor (UC, copper shaded in Fig. 2d). App. D derives
compact formulas for the magnetic energy contributions for
WUC and Wf under these assumptions. Substituting the respective terms of the magnetic energy into (36) yields
R = RDC

FR + GR
2
µ0
WUC
VUC ˆI2

|
{z
}
R1D
+ RDCGR
2
µ0
Wf
VUC ˆI2
|
{z
}
Rf
where RDC is the DC resistance of the winding and VUC is
the volume of the unified conductor block (cf. Fig. 2d). The
separable loss component R1D, caused by the skin effect and
the external 1D magnetic layer field, is considered by
R1D = RDC

FR + GR
πN 2
hw
x2
c,o + 2xc,ixc,o -3x2
c,i
6VUC
!
(37)
which is equivalent to known 1D models for solid round wire,
e.g. [12]. Here, (31) is used for W1D to obtain the compact
formula for the effective inductor resistance, neglecting the air
gap fringing field. The formula for the effective AC resistance
caused by the air gap fringing field, using (29), is then:
Rf = RDCGR
2πhw
µ2
0VUC
∞
X
k=1
ck(xc,i, xc,o)|Ck|2 + dk(xc,i, xc,o)|Dk|2
(38)
Note, that here the functions ck and dk consider the core
window area from xc,i to xc,o (copper shaded layer in Fig. 2d).
Eventually, this leads to the total effective AC resistance of the
inductor presented in (7).
APPENDIX H
EFFECTIVE AC RESISTANCE - LITZ WIRE
A comprehensive survey and comparison of winding loss
models for Litz wire can be found in [28]. There, it is shown
that an additional loss term must be added to (33) to consider
the internal proximity effect of the Litz wire. An expression
for the total losses caused by the skin, external, and internal
proximity effect, can be derived in a similar way as for solid
round wire. It is made use of the fact, that internal and external
proximity effects are orthogonal [13], hence:
ˆH2
ext = ˆH2
rms + ˆH2
int
Then, the squared averaged internal magnetic field, which is
the same for all wires, is given as:
ˆH2
int =
4
d2π
ZZ
A
rH2
i (r) dA =
ˆI2
2π2d2
Additionally, formula (33) must be adapted to Litz wire, which
consists of Ns strands of the much thinner individual diameter
ds, bundled together (cf. Fig. 3a). The power loss of an
individual strand is
Ps =
ˆI′2
σπd2s
Re
α′I0(α′)
I1(α′)

+ 2π ˆH2
ext
σ
Re
α′I1(α′)
I0(α′)

where α′ is adjusted for the Litz wire strand diameter, according to (12). Note, that the current through each strand
is ˆI′ =
ˆI/Ns, since the individual strands are connected in
parallel. The losses of the bundle are P = NsPs. Then, with
the DC resistance of the Litz wire (bundle) R′
DC = 4/Nsσπd2
s,
the power loss is again given as
P = 1
2R′
DCF ′
R ˆI2 + 1
2R′
DCG′
R

ˆH2
rms + ˆH2
int

with F ′
R and G′
R given in (12). Finally, following the same
step as in app. E, the effective AC resistance for Litz wire is
R = R′
DC

F ′
R + G′
R
 Lp
µ0Vp
+
1
2π2d2

(39)
APPENDIX I
AC RESISTANCE - LAYER MODEL - LITZ WIRE
The effective AC resistance of Litz wire is obtained from
(39), where the partial inductance of the layer is obtained the
same way as in the previous section, app. F, for solid round
wire. Hence,
Rn = R′
DC,n

F ′
R + G′
R

L(EFC)
n
µ0Vn
+
1
2π2d2
!!

## [стр. 13]

TRANSACTIONS ON POWER ELECTRONICS
12
with the volume of the respective layer Vn and the DC
resistance of the n-th Litz wire layer R′
DC,n. As for solid round
wire, the sum over all NEFC EFC yields the total resistance
of the inductor, leading to (17).
APPENDIX J
AC RESISTANCE - COMPACT MODEL - LITZ WIRE
In case of Litz wire, the same steps are performed as in
app. G, but (39) is used as a starting point. This results in
R1D = R′
DC

F ′
R + G′
R

1
2π2d2
+ πN 2
hw
x2
c,o + 2xc,ixc,o -3x2
c,i
6VUC

(40)
which is then equivalent to 1D models for Litz wire, e.g. [13],
[29], and the impact of the air gap fringing field
Rf = R′
DCG′
R
2πhw
µ2
0VUC
∞
X
k=1
ck(xc,i, xc,o)|Ck|2 + dk(xc,i, xc,o)|Dk|2
(41)
The effective AC resistance of the inductor is the sum of both
presented in (11), where R′
DC is the DC resistance of the Litz
winding and VUC is the volume of the winding.
ACKNOWLEDGMENT
The authors would like to express their acknowledgment
to the Baechli AG, Switzerland, and Innosuisse, Switzerland
(Appl. No.: 32328.1 IP-ENG), for providing financial support
for this project.
REFERENCES
[1] J. Cale, S. D. Sudhoff, and Li-Quan Tan, "Accurately modeling EI core
inductors using a high-fidelity magnetic equivalent circuit approach,"
IEEE Transactions on Magnetics, vol. 42, no. 1, pp. 40-46, Jan. 2006.
[2] A. Van den Bossche, V. Valchev, and T. Filchev, "Improved approximation for fringing permeances in gapped inductors," in Record of the
37th Industry Applications Conf.
IEEE, 2002.
[3] E. Stenglein and M. Albach, "The reluctance of large air gaps in ferrite
cores," in 18th European Conf. on Power Electronics and Applications
(EPE ECCE Europe).
IEEE, Sep. 2016.
[4] C. McLyman, Transformer and Inductor Design Handbook. CRC Press,
2017.
[5] A. F. Hoke and C. R. Sullivan, "An improved two-dimensional numerical
modeling method for e-core transformers," in APEC. Seventeenth Annual IEEE Applied Power Electronics Conference and Exposition (Cat.
No.02CH37335), vol. 1, 3 2002.
[6] A. Balakrishnan, W. T. Joines, and T. G. Wilson, "Air-gap reluctance and
inductance calculations for magnetic circuits using a schwarz-christoffel
transformation," IEEE Transactions on Power Electronics, vol. 12, no. 4,
pp. 654-663, July 1997.
[7] J. Muehlethaler, J. W. Kolar, and A. Ecklebe, "A novel approach for
3d air gap reluctance calculations," in 8th International Conference on
Power Electronics (ECCE Asia), May 2011.
[8] I. Kovaˇcevi´c-Badst¨ubner, R. Burkart, C. Dittli, J. W. Kolar, and A. Musing, "A fast method for the calculation of foil winding losses," in 17th
European Conf. on Power Electronics and Applications (EPE ECCE
Europe), Sep. 2015.
[9] C. R. Sullivan, "Computationally efficient winding loss calculation with
multiple windings, arbitrary waveforms, and two-dimensional or threedimensional field geometry," IEEE Transactions on Power Electronics,
vol. 16, no. 1, pp. 142-150, Jan. 2001.
[10] M. Albach, "Two-dimensional calculation of winding losses in transformers," in 31st Annu. Power Electronics Specialists Conf.
IEEE,
Jun. 2000.
[11] M. Albach and H. Rossmanith, "The influence of air gap size and winding position on the proximity losses in high frequency transformers,"
in 2001 IEEE 32nd Annual Power Electronics Specialists Conference
(IEEE Cat. No.01CH37230).
IEEE, 2001.
[12] J. A. Ferreira, "Improved analytical modeling of conductive losses in
magnetic components," IEEE Transactions on Power Electronics, vol. 9,
no. 1, pp. 127-131, Jan 1994.
[13] J. Ferreira, "Analytical computation of AC resistance of round and
rectangular litz wire windings," IEE Proceedings B (Electric Power
Applications), vol. 139, no. 1, p. 21, 1992.
[14] J. Muehlethaler, J. W. Kolar, and A. Ecklebe, "Loss modeling of
inductive components employed in power electronic systems," in 8th
Int. Conf. Power Electronics, May 2011, pp. 945-952.
[15] D. Leuenberger and J. Biela, "Accurate and computationally efficient
modeling of flyback transformer parasitics and their influence on converter losses," in 17th European Conference on Power Electronics and
Applications (EPE ECCE Europe).
IEEE, Sep. 2015.
[16] P. Wallmeier, N. Frohleke, and H. Grotstollen, "Improved analytical
modeling of conductive losses in gapped high-frequency inductors," in
33rd IEEE Industry Applications Society Conf. (IAS), vol. 2, Oct. 1998,
pp. 913-920.
[17] W. A. Roshen, "Fringing field formulas and winding loss due to an air
gap," IEEE Transactions on Magnetics, vol. 43, no. 8, pp. 3387-3394,
Aug. 2007.
[18] A. V. den Bossche and V. C. Valchev, "Improved calculation of winding
losses in gapped inductors," Journal of Applied Physics, vol. 97, no. 10,
May 2005.
[19] T. Ewald and J. Biela, "Frequency-dependent inductance and winding
loss model for gapped foil inductors," Transactions on Power Electronics, 2022.
[20] M. Albach, Induktivit¨aten in der Leistungselektronik. Springer Vieweg,
Wiesbaden, 2017.
[21] Y. Han, G. Cheung, A. Li, C. R. Sullivan, and D. J. Perreault, "Evaluation of magnetic materials for very high frequency power applications,"
in Power Electronics Specialists Conference.
IEEE, jun 2008.
[22] S. Mukherjee, Y. Gao, and D. Maksimovic, "Reduction of AC winding
losses due to fringing-field effects in high-frequency inductors with
orthogonal air gaps," Transactions on Power Electronics, vol. 36, no. 1,
pp. 815-828, jan 2021.
[23] J. Muehlethaler, J. Biela, J. W. Kolar, and A. Ecklebe, "Core losses under
the dc bias condition based on steinmetz parameters," IEEE Transactions
on Power Electronics, vol. 27, no. 2, 2 2012.
[24] E. Snelling, Soft ferrites: properties and applications.
NewnesButterworth, 1969.
[25] M. Kazimierczuk, High Frequency Magnetic Components.
John Wiley
& Sons, Ltd, 2013.
[26] T. Ewald and J. Biela, "Analytical eddy current loss model for foil
conductors in gapped cores," 23th European Conference on Power
Electronics and Applications (EPE ECCE Europe), Oct. 2021.
[27] W. F. Trench, "Elementary differential equations," Faculty Authored and
Edited Books and CDs, no. 8, 2013.
[28] Q. Meng, "Survey and comparison of different 1D and 2D analytical
models of HF losses in Litz Wire," in 22nd European Conference on
Power Electronics and Applications (EPE ECCE Europe), Sep. 2020.
[29] M. Bartoli, N. Noferi, A. Reatti, and M. Kazimierczuk, "Modelling litzwire winding losses in high-frequency power inductors," in 27th Power
Electronics Specialists Conf. (PESC).
IEEE, 1996.

## [стр. 14]

TRANSACTIONS ON POWER ELECTRONICS
13
Thomas Ewald (Student Member, IEEE) studied
electrical engineering with focus on Energy Conversion Technology at Technical University of Munich
(TUM) in Germany. He received his B.Sc. and M.Sc.
degree from TUM in 2015 and 2018, respectively.
In 2017, he wrote his Master's Thesis at BMW
AG in the R&D department for electrical drive
components. In his Master's thesis he developed an
analytical model for simulating transient processes
in both, permanent magnet and electrically excited
synchronous machines. Since November 2019 he
is a Ph.D. student at the Laboratory for High Power Electronic Systems
(HPE) at ETH Zurich, working on analytical inductor models and automated
optimization processes.
J¨urgen Biela (Senior Member, IEEE) received the
Diploma (hons.) degree from Friedrich-Alexander
Universit¨at Erlangen-N¨urnberg, Erlangen, Germany,
in 1999, and the Ph.D. degree from the Swiss Federal
Institute of Technology (ETH), Z¨urich, Switzerland,
in 2006. In 2000, he joined the Research Department, Siemens A&D, Erlangen, and in 2002, he
joined the Power Electronic Systems Laboratory,
ETH Z¨urich, as a Ph.D. Student focusing on electromagnetically integrated resonant converters, where
he was a Postdoctoral Fellow from 2006 to 2010.
Since 2010, he has been an Associate Professor, and since 2020, a Full
Professor of high-power electronic systems with ETH Zurich.
