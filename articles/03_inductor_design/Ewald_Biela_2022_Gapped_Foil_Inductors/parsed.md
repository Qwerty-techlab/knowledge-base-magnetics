# source

<!-- FORMULA-WARNING -->
> **Формулы в этом файле недостоверны.** Текстовый слой PDF теряет дробные черты, радикалы и группировку степеней; знак интеграла приходит как `Z` или `R`, знак суммы -- как `P`. Формул вырезано: **25**, читать их в `formulas/` (картинки 300 dpi, перечень в `formulas/INDEX.md`).
<!-- /FORMULA-WARNING -->

> Автоматически извлечено из `source.pdf` скриптом `parse_pdf.py`
> Движок: pymupdf. Страниц: 12 из 12.
> Дата извлечения: 2026-08-07 06:43 UTC

Текст не редактировался. Формулы и таблицы могут быть искажены —
при сомнении сверяться с исходным PDF.

---

## [стр. 1]

ETH Library
Frequency-dependent inductance
and winding loss model for gapped
foil inductors
Journal Article
Author(s):
Ewald, Thomas
; Biela, Jürgen
Publication date:
2022-10
Permanent link:
https://doi.org/https://doi.org/10.3929/ethz-b-000544650
Rights / license:
In Copyright - Non-Commercial Use Permitted
Originally published in:
IEEE Transactions on Power Electronics 37(10), https://doi.org/10.1109/tpel.2022.3169620
This page was generated automatically upon download from the ETH Zurich Research Collection.
For more information, please consult the Terms of use.

## [стр. 2]

TRANSACTIONS ON POWER ELECTRONICS
1
Frequency-dependent inductance and winding loss
model for gapped foil inductors
Thomas Ewald, Student Member, IEEE, J¨urgen Biela, Senior Member, IEEE,
Email: ewald@hpe.ee.ethz.ch, biela@ethz.ch
Abstract-For comprehensively optimizing high-frequency foil
inductors, calculating the increased inductance and the additional
eddy current losses due to a two-dimensional magnetic fringing
field caused by air gaps in the centre leg is mandatory. This
paper proposes an analytical model that accurately calculates
the inductance and the additional eddy current losses in gapped
inductors with foil windings. The analytical field expressions are
combined into closed-form winding loss and inductance formulas and verified by measurements. Furthermore, the frequency
dependency of the inductance due to the shielding effect of the
foil conductors is being discussed.
Index Terms-Magnetic components, Inductance, Winding
losses, Magnetic field, Fringing effect, Shielding effect
I. INTRODUCTION
M
AGNETIC component design is often based on multidomain models [1] and comprehensive multi-objective
optimization [2], to avoid numerous redesigns and keep development time and cost low. Here, accurate mathematical models are crucial. Since several thousand designs are typically
calculated during the optimization, models that offer a small
computational effort combined with reasonable accuracy are
required.
Considering the design of inductors, besides the winding
losses also the inductance must be determined, taking into
account high-frequency (HF) effects. While the correct inductance is crucial for the operation of the converter system,
the losses determine the design, not only of the component,
but also of the (cooling) system. High-frequency effects,
such as the frequency-dependent non-homogeneous magnetic
field distribution in the core window have an impact on the
winding losses but also on the inductance. The magnetic field
distribution in the core window is influenced by the current
in the conductors (including skin, proximity, shielding effects)
and the air gaps in the legs (fringing effect).
A. Winding loss calculation in foil conductors
Winding loss calculation in general is a challenging task
when a non-ideal magnetic field distribution, deviating from
the classical 1D assumption [3], must be considered. Hence,
in many cases the field is assumed to be 1D, even when an
air gap is present [4]-[6], and the field significantly deviates
from the 1D simplification. However, when foil conductors
are considered, calculating the 2D magnetic field in the
core window of gapped inductors is mandatory, because foil
conductors are particularly sensitive to the air gap fringing
field [7].
For considering a 2D magnetic field distribution, different
per-unit-length winding loss models including an air gap fringing field have been presented. For example, [7], [8] propose
semi-numerical models, where numerical or iterative field
calculations are performed before the actual loss calculation.
In those models, a numerical field calculation is necessary
to consider the impact of the conductor current on the 2D
magnetic field. However, the numerical evaluation results in
extensive execution times, which makes the models usable
only to a limited extent in the context of optimizations. [9]
considers the attenuation of the 2D magnetic field only in the
first conductor and ignores further conductors, which results
in an inaccurate loss calculation. [10], [11] replaces all the
individual foil conductors in the winding as one solid copper
block. With this simplification the actual position of the individual conductors is neglected, introducing errors in the model.
Since fast and flexible analytical models are required, other
empirical, numerical, or iterative field calculation methods
given in the literature are not considered in this paper - please
refer to [12] for a more comprehensive listing of winding loss
models.
Since the mentioned modelling approaches for the winding
loss calculation result in two-dimensional per-unit-length loss
densities, a length scaling model to consider the actual length
of the winding turns is necessary to obtain the total losses.
In the case of gapped inductors, comprehensive modelling of
the 3D geometry of the winding is crucial, since the fringing
field of the air gaps is locally influencing the magnetic field.
Therefore, simple approaches like the typical mean-length-ofa-turn [13] are not sufficiently accurate.
a)
b)
Fig. 1. a) Inductor with an ETD 59/31/22 core with circular centre leg. b)
Inductor with an E 65/32/27 core with rectangular centre leg.

## [стр. 3]

TRANSACTIONS ON POWER ELECTRONICS
2
B. Inductance calculation
With the 2D magnetic field formulation in the core window
and the air gap, it is also possible to accurately calculate
the inductance. However, no approach can be found in the
literature, that comprehensively models the winding losses and
the inductance of gapped foil wound inductors based on a 2D
magnetic field. The reason is, that many 2D magnetic field
models use the mirroring method to calculate the magnetic
field in the core window (e.g. [7]), which would require
numerical integration to obtain the magnetic energy.
Hence, the calculation of the inductance of gapped inductors
is usually performed separately with reluctance networks of
which the inductance is derived. To consider the influence
of air gaps, correction factors for the air gap reluctance
are proposed in [14]-[17]. The shielding effect of the foils,
which is closely related to the inhomogeneous current density
distribution in the foil conductors is known [8], [18], but
generally ignored in all inductance models mentioned above.
This effect decreases the inductance up to 20 % depending on
the frequency and therefore counteracts the fringing effect, as
will be shown in this paper.
C. Proposed comprehensive modelling
So far, in existing literature no computationally efficient and
at the same time sufficiently accurate models are proposed for
calculating the winding losses of gapped foil inductors. Furthermore, the shielding effect of foil conductors is ignored in
the inductance calculation. Consequently, this paper proposes a
new, computationally efficient, and accurate 2D magnetic field
formulation and derives the winding losses and the inductance
in a quasi-3D model from this 2D magnetic field formulation.
This model considers the fringing effect of the air gaps, the
skin effect, the proximity effect, as well as the shielding effect
of the foils. This results in a comprehensive modelling of the
winding losses and the inductance of gapped foil inductors,
which is usable in optimization routines.
The paper is organized as follows: Section II proposes
an analytical model predicting the two-dimensional, nonhomogeneous magnetic field in the core window considering
an arbitrary number of air gaps. Section III derives expressions
for accurately calculating the inductance and the winding
losses of circular symmetric inductors by introducing an
accurate length scaling for the 2D models. The adaptation of
the model to cores with rectangular centre legs and a finite
and complex relative permeability of the core is presented
in section IV. The proposed model is verified with FEM
simulations and measurements, and the results are discussed
in section V.
II. H-FIELD IN 2D CARTESIAN COORDINATES
The following derivations aim for a closed form formulation
of the magnetic field and the current density in the core window and the conductors. The analytical solution is obtained by
directly solving the Maxwell equations. There, the following
assumptions are applied:
1) Core window infinitly long in z-direction: →2D
b)
d)
c)
a)
u1
x
leg
d
leg
a
leg
d
z
z
leg
b
x
y
z
lg
Jz
Bx
(NC)
Bx
(C)
Hy
(NC)
Hy
(C)
x
v1
u2
dx,i
dt
df
Rotational axis of symmetry
lg
hf
dleg
dx,o
dx,i
df
dt
x
Rectangular air gap region
Fig. 2. a) 2D front view of a foil wound E-core inductor, including parameter
definition of the 2D model. b) Zoomed section of the core window. c) Top
view of an ETD-Core with circular centre leg. d) Top view of an E-Core with
rectangular centre leg.
2) Magneto-quasi-static calculations: ∇×⃗H =⃗J
3) Harmonic time dependency: d/dt →jω
4) The core material is ideal: µr →∞
5) Conductors fill the core window from yoke to yoke
In the following, the fields are derived in 2D Cartesian
coordinates. For the sake of brevity, this paper briefly shows
the results of the derivations already performed in [12]. The
procedure in this paper is to derive the fields in 2D, and to
apply a quasi-3D length scaling in section III. This procedure
is typical, especially in the winding loss calculation. Errors
induced by this procedure are negligible, as shown in [13].
A. Geometrical definitions
The geometry of a 2D core window with foil conductors,
including the definition of variables used in the model, is
shown in Fig. 2. The window is divided into N rectangular
conductors C (copper shaded in Fig. 2), M = N+1 nonconductive regions (NC), and the rectangular air gap region
(orange rectangle in the centre leg). The conductors have the
width df, the non-conductive region next to the centre leg
(e.g. bobbin) is considered with dx,i, the distance between
the conductors is dt, and the distance between the outermost
conductor and the core limb is dx,o. The conductors have the
height hf. The air gap has the length lg and the centre leg
width is dleg. The origin of the coordinate system is in the
middle of the centre leg. The air gaps are assumed to be placed
periodically along the y-axis, with symmetry to the x-axis. The
number of distributed air gaps is denoted with Ng.
B. Magnetic flux density in the core window
The current, the current density, and the magnetic vector
potential are defined to have only components in z-direction.
The magnetic field is perpendicular to the magnetic vector
potential so that it has only components in the xy-plane. Using
the general relation between electric field and magnetic vector
potential [19] and interpreting the current density as⃗J = σ⃗E

## [стр. 4]

TRANSACTIONS ON POWER ELECTRONICS
3
in all regions, with σ = 0 in the non-conductive regions and
σ̸ = 0 in the conductors, results in:⃗
J = σ⃗E = -jωσ
⃗
A + 1
jω ∇ϕ

|
{z
}⃗
F
(1)
Here,⃗F denotes the modified vector potential, that replaces
the magnetic vector potential. As shown in [20], the gradient
of the electric potential ∇ϕ inside the conductors has only
a z-component, which is constant and can be identified with
the voltage drop along the conductor. The modified vector
potential is obtained by solving the Laplace and the diffusion
equation in the non-conductive regions and the conductors,
respectively. This yields:
∇2⃗F (NC) = 0
∇2⃗F (C) = γ2⃗F (C)
(2)
where γ2 = jωσµ. Here, the modified vector potential in the
m-th non-conductive region and the n-th conductor is [12]:
F (NC)
z
= Cm,0(x-um)
+
∞
X
k=1

Cm,k e-pk(x-um) +Dm,k epk(x-um) cos(pky)
pk
F (C)
z
= Mn,0 e-γ(x-vn) +Nn,0 eγ(x-vn)
+
∞
X
k=1

Mn,k e-ξk(x-vn) +Nn,k eξk(x-vn) cos(pky)
pk
(3)
Substituting (3) into (2), it can be concluded that ξ2
k = γ2+p2
k.
um and vn denote the reference coordinate of the respective
region (see Fig. 2b). The coefficients indicated with index
0 are called the spatially independent coefficients and the
coefficients indicated with index k are called the spatial coefficients. Note, that parts of the solution (all parts containing
spatially independent coefficients) are similar to Dowell's
model [3], whereas the parts containing the spatially dependent
coefficients are added to the model to consider (multiple) air
gaps, and are originally derived in [10].
The flux density components for the non-conductive regions
and the conductors are calculated with⃗B = ∇×⃗F. This results
in:
B(NC)
x
= -
∞
X
k=1

Cm,k e-pk(x-um)
+ Dm,k epk(x-um) 
sin(pky)
B(C)
x
= -
∞
X
k=1

Mn,k e-ξk(x-vn)
(4)
+ Nn,k eξk(x-vn) 
sin(pky)
B(NC)
y
= -Cm,0
+
∞
X
k=1

Cm,k e-pk(x-um) -Dm,k epk(x-um)
cos(pky)
B(C)
y
= γ

Mn,0 e-γ(x-vn) -Nn,0 eγ(x-vn)
+
∞
X
k=1
αk

Mn,k e-ξk(x-vn) -Nn,k eξk(x-vn)
cos(pky)
where αk = ξk/pk. To satisfy the boundary conditions of the
magnetic flux density Bx(x, -hf/2) = Bx(x, hf/2) = 0 it
follows that pk = 2πkNg/hf, since the air gaps are placed
symmetrically and periocically along the y-axis.
Finally, the magnetic field in the rectangular air gap region
(see Fig. 2a) is
Hg = NI
Nglg
(5)
and the magnetic flux density Bg = µ0Hg. The separation
between the magnetic field inside the air gap region and the
core window is possible because the additional fringing field
in the core window can be regarded as a result of additional
reluctance paths around the air gaps, that reduce the total
reluctance of the magnetic circuit.
C. Coefficients
The following expressions are taken from [12]. The coefficients Cm,0 for the non-conductive regions are given by:
Cm,0 = µ0(M -m)I
hf
(6)
where I is the amplitude of the sinusoidal current. The solution
for the coefficients Mn,0 and Nn,0 is:
Mn,0 = Cn+1,0 -Cn,0 eγdf
2γ sinh γdf
Nn,0 = Cn+1,0 -Cn,0 e-γdf
2γ sinh γdf
(7)
For the spatial coefficients, a system of equations with in
total 4N+2 linearly independent equations can be found for
calculating all coefficients Cm,k, Dm,k, Mn,k, and Nn,k for
each k. For the linear set of equations Kkck = bk the system
matrix Kk is given in (9), with αk = ξk/pk, and
ck =

C1,k
D1,k
M1,k
N1,k
· · ·
D(N+1),k

bk =
h
-2µ0NglgHg
hf
sinc

k Nglg
hf

0
· · ·
0
i
(8)
with the normalized sinc-function and Hg from (5). With the
solution for all coefficients, the 2D magnetic field in the core
window and with (1) the 2D current density in the conductors
are fully described.
III. LENGTH SCALING OF THE MODEL
In the following, an accurate length scaling for the 2D Hfield model from the previous section is developed. For this
purpose, a polar system is assumed and the integration in zdirection is replaced by an integration along the circumference.
The reason for the integration instead of multiplication with
the (individual) turn length is, that the integration in polar
coordinates weighs the contribution of each region in the
2D-plane with increasing x (r in polar coordinates) more
accurately. This is especially important in the regions close
to the air gaps.

## [стр. 5]

TRANSACTIONS ON POWER ELECTRONICS
4
Kk =


1
-1
0
· · ·
0
e-pkdx,i
epkdx,i
-1
-1
0
0
· · ·
0
e-pkdx,i
-epkdx,i
-αk
αk
0
0
· · ·
0
0
0
e-ξkdf
eξkdf
-1
-1
0
· · ·
0
0
0
αk e-ξkdf
-αk eξkdf
-1
1
0
· · ·
0
0
0
0
0
e-pkdt
epkdt
-1
-1
...
0
0
0
0
e-pkdt
-epkdt
-αk
αk
...
...
...
0
· · ·
0
0
e-pkdx,o
-epkdx,o


(9)
A. Winding losses and effective resistance
The winding loss is generally determined as [19, sec. 6.9]:
P = 1
2
ZZZ
x⃗E⃗J∗dx dy dz
(10)
where⃗J∗denotes the complex conjugate of⃗J. Regarding the
integration, all terms containing an integral along y-direction
over sin(pky) or cos(pky) vanish. In addition, all those
integrals containing sin(pjy) sin(pky) or cos(pjy) cos(pky)
for j̸
= k also vanish, due to the orthogonality of the
trigonometric functions. With the equations (1) and (3), the
winding losses of the n-th conductor are:
Pn = πω2σhf

ζ1,n,0|Mn,0|2 + ζ2,n,0|Nn,0|2
+ ℜ

ζ3,n,0Mn,0N ∗
n,0

+
∞
X
k=1
ζ1,n,k|Mn,k|2
+ ζ2,n,k|Nn,k|2 + ℜ

ζ3,n,kMn,kN ∗
n,k
	 
(11)
where γ′ = ℜ{γ}, γ′′ = ℑ{γ}, ξ′
k = ℜ{ξk}, ξ′′
k = ℑ{ξk},
and
ζ1,n,0 = -(2γ′(vn + df) + 1) e-2γ′df -2γ′vn -1
4γ′2
ζ2,n,0 = (2γ′(vn + df) -1) e2γ′df -2γ′vn + 1
4γ′2
ζ3,n,0 = (j2γ′′(vn + df) + 1) e-j2γ′′df -j2γ′′vn -1
2γ′′2
ζ1,n,k = -(2ξ′
k(vn + df) + 1) e-2ξ′
kdf -2ξ′
kvn -1
8p2
kξ′2
k
ζ2,n,k = (2ξ′
k(vn + df) -1) e2ξ′
kdf -2ξ′
kvn + 1
8p2
kξ′2
k
ζ3,n,k = (j2ξ′′
k(vn + df) + 1) e-j2ξ′′
k df -j2ξ′′
kvn -1
4p2
kξ′′2
k
The total winding losses are obtained by summing up the
individual losses:
P =
N
X
n=1
Pn =
N
X
n=1

Pn,0 +
∞
X
k=1
Pn,k
!
= P1D + Pgap (12)
The expressions (11) and (12) reveal, that the winding losses
can be separated into two parts, where P1D consists of all
terms indicated with 0 and Pgap contains the infinite sum of
terms indicated by the index k. The partial losses denoted with
P1D are equivalent to [3] and consider the loss contribution of
the skin and the layer proximity effect (hence the abbreviation
'1D' for 1D layer field), whereas Pgap accounts for the
additional losses due to the air gap fringing field.
Likewise, the resistance can be separated into two parts,
considering the resistance caused by the 1D layer field (resistance increase due to skin and layer proximity effect) and the
air gap field, respectively. The frequency-dependent winding
resistance is obtained by dividing (12) by the squared current
amplitude:
R = 2P
I2 = R1D + Rgap
(13)
This is the total frequency-dependent effective resistance of the
inductor, including skin, proximity, and fringing effects. The
factor of 2 in the nominator is caused by the fact, that (10)
considers the effective value, whereas the current is considered
as the amplitude.
B. Magnetic energy and inductance
In addition to the frequency-dependent winding losses the
frequency-dependent inductance of the inductor is derived in
this paper. In general, the magnetic energy is [19, sec. 6.9]:
W = 1
2
ZZZ
x⃗B⃗H∗dx dy dz
(14)
By using (4) the magnetic energy in the m-th non-conductive
region and in the n-th conductor is given as:
W (NC)
m
= πhf
µ0
(um + dNC)2 -u2
m
2
|Cm,0|2
+
∞
X
k=1
β1,m,k|Cm,k|2 + β2,m,k|Dm,k|2

W (C)
n
= πhf
µ0

η1,n,0|Mn,0|2 + η2,n,0|Nn,0|2
+ ℜ

η3,n,0Mn,0N ∗
n,0

+
∞
X
k=1
η1,n,k|Mn,k|2
+ η2,n,k|Nn,k|2 + ℜ

η3,n,kMn,kN ∗
n,k
	 
(15)

## [стр. 6]

TRANSACTIONS ON POWER ELECTRONICS
5
where dNC is either dx,i, dt, or dx,o,
β1,m,k = -(2pk(um + dNC) + 1) e-2pkdNC -2pkum -1
4p2
k
β2,m,k = (2pk(um + dNC) -1) e2pkdNC -2pkum + 1
4p2
k
and
η1,n,0 = |γ|2ζ1,n,0
η1,n,k =

p2
k + |ξk|2
ζ1,n,k
η2,n,0 = |γ|2ζ2,n,0
η2,n,k =

p2
k + |ξk|2
ζ2,n,k
η3,n,0 = -|γ|2ζ3,n,0
η3,n,k =

p2
k -|ξk|2
ζ3,n,k
The energy stored in the air gap, which contributes the most
to the overall inductance, is given as
Wg =
µ0πd2
legNglg
8
|Hg|2
which is equal to (14) evaluated in the air gap region with the
constant magnetic field from (5). As mentioned, it is assumed
that the magnetic field in the air gap is constant and the
additional fringing field is fully accounted for by (15).
The inductance of the component is finally derived from the
total magnetic energy stored in the core window and in the air
gap:
L = 2
I2

Wg +
M
X
m=1
W (NC)
m
+
N
X
n=1
W (C)
n
!
(16)
Per definition, this is the inductance of the inductor, assuming
infinite permeability of the core. The presented model (16)
extends existing inductance models from the literature by a
frequency-dependency, which is caused by the shielding effect
of the foils.
IV. MODEL FOR A FINITE PERMEABILITY AND
RECTANGULAR CENTRE LEGS
The presented model is derived for circular centre legs and
an infinite relative permeability. In the following, corrections
considering rectangular centre legs and a finite, complex
permeability are introduced.
A. Rectangular centre legs
To consider centre legs with rectangular cross-sections, an
appropriate length scaling of the 2D models is required. This
can be achieved by multiplying the 2D fields from section II
with the lengths of the straight winding sections in Cartesian
coordinates. In addition, the four corners of the winding could
be considered with (11) for dleg = 0.
Instead, another approach is pursued, in order to avoid
additional derivations and to make use of the already obtained
results from section III. A coefficient krect is defined, which
links the circumferences Crect of a rectangle with side lengths
aleg and bleg to the circumference Ccirc of a circle. Hence, it
is assumed that the geometry has a rectangular cross-section
with width bleg = dleg and depth aleg, as given in Fig. 2d). It
follows:
krect = Crect
Ccirc
= 4
π

1 + aleg -bleg
4x

(17)
101
102
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
Fig. 3.
Real part µ′
r and imaginary part µ′′
r of the complex permeability
of the material N87, extracted from the manufacturer's data sheet [21] for
B = 25 mT (small signal excitation) and T = 25 ◦C.
where x is either um or vn, and aleg and bleg are given in
Fig. 2d). Every region that is considered in the calculation
must be adjusted by its respective coefficient. Since the radius
of the curvature is assumed to be much greater than the thickness of the individual regions, using the inner circumference
of each region for the correction is justifiable. krect is used
to scale the winding losses given in (11) and the magnetic
energy in (15). This way, no additional derivations must be
performed and the results of the previous sections can be used
to calculate the winding losses and the inductance of inductors
with rectangular centre legs as well. There is no notable error
induced by this procedure, as shown later in section V-A.
In addition to the length scaling, the magnetic energy stored
in the air gap in (16) must be replaced with
Wg = µ0blegalegNglg
2
|Hg|2
which is the squared constant magnetic field from (5) integrated over the volume of the air gaps with rectangular crosssection.
B. Finite and complex permeability
Typically, in winding loss calculation µr →∞is assumed.
However, the field strength of the air gap's H-field is significantly impacted by a lower relative permeability, as later
shown in section V-A. Hence, the relative permeability is
introduced in the following.
It is assumed that µr = µ′
r -jµ′′
r [22], where µ′
r is the real
part and µ′′
r is the imaginary part of the complex permeability.
Fig. 3 shows the complex permeability as function of the
frequency for the material N87. The curves are extracted from
the data sheet [21].
Furthermore, the effective magnetic path length through the
core is known and denoted with le. This quantity is usually
given by the manufacturer of the core or can be derived from
the core geometry as described in [23]. With le, the magnetic
field is [13]:
Hg = kµ
NI
Nglg
with
kµ =
1
1 +
le
µrNglg
(18)
where it is assumed that the average magnetic flux densities,
in the core and in the air gaps are the same and constant (c.f.
Fig. 2a) →rectangular air gap region). Then, (18) replaces
(5) in the derivations in section II to account for the finite
permeability in the field calculations. Note, that the relative

## [стр. 7]

TRANSACTIONS ON POWER ELECTRONICS
6
permeability in (18) can be complex. Furthermore, the phase
angles of the flux density in the core and in the air gap must
be the same, with consideration of the complex permeability.
To validate the previous simplification, a 2D FEM simulation was performed with the parameters from Tab. II. The
average magnetic flux densities Bc (core) and Bg (air gap
without fringing field - c.f. Fig. 2a) rectangular air gap region)
were calculated with
B = 1
A
ZZ
A
ˆB dA
where ˆB is the true and spatially inhomogeneous flux density
distribution in the region of consideration. The results of the
FEM simulation are Bc = 12.42 mT and Bg = 12.33 mT,
whereas (18) results in 12.33 mT, hence, the assumption is
valid in this context. In general, this assumption can be
applied, if the centre leg diameter is greater than the air gap
length.
In addition, the magnetic energy in the core has to be taken
into account, especially for a low µr. The magnetic energy in
the core, using its effective volume Ve, is:
Wc = Ve
2 BcH∗
c = µ0Ve|Hg|2
2µ∗r
(19)
The magnetic energy (19) must be added to (16). Note, that by
considering the complex permeability, (16) and (19) become
complex.
V. MODEL VERIFICATION
The verification of the models is performed in two steps.
First, numerous FEM simulations are conducted to identify
potential error sources in detail by comparing the analytical
derivations with a 2D circular symmetric FEM model in
section V-A. In a second step, measurements are performed,
which are compared to analytical results of the winding loss
and the inductances in section V-B. In addition, Tab. I presents
a pseudo-algorithm to explain the required steps, that must be
followed to calculate the winding losses and the inductance
with the proposed models.
100
101
102
Ng = 1
Ng = 2
Ng = 3
P in mW
Model
2D FEM
101
102
103
104
105
106
4
4.25
4.5
4.75
5
Ng = 1
Ng = 2
Ng = 3
f in Hz
L in µH
Model
2D FEM
Fig. 4.
Proposed winding loss and inductance models compared to 2D
rotationally symetrical FEM (marked with ⋆in the respective color) vs.
frequency with constant and real-valued relative permeability, for different
numbers of air gaps. The inductance decreases notably at higher frequencies
due to the shielding effect.
TABLE I
CALCULATION OF R AND L WITH THE PROPOSED MODELS
In: Geometrical parameters - ω, N, Ng, hg, hf, dleg, dx,i, df, dt, dx,o.
1: function CALC R AND L
2:
% Determine air gap field (relative permeability):
3:
Hg ←Eq. (5) or (18)
4:
% Coefficients, independent of the air gap field:
5:
Bm,0, Cn,0, Dn,0 ←Eqs. (6), (7)
6:
% Coefficients, based on the air gap field:
7:
Cn,k, Dn,k, Mn,k, Nn,k ←Eqs. (8), (9)
8:
% Compute winding losses and resistance:
9:
P ←Eq. (12), if necessary Eq. (17)
10:
R ←Eq. (13)
11:
% Compute magnetic energy and inductance:
12:
W ←Eq. (15), if necessary Eqs. (17), (19)
13:
L ←Eq. (16)
102
103
104
105
106
3.5
4.0
4.5
5.0
µr
L in µH
Model
FEM
102
103
104
105
106
5
10
15
20
µr
P in mW
Model
FEM
Fig. 5.
Comparison of proposed model results with 2D circular symmetrical
FEM simulations for a fixed frequency, Ng = 1, and hg = 1 mm. Left:
Inductance with varying relative permeability - Right: Winding losses with
varying relative permeability.
At this point it should be noted, that the length scaling of
the model, as derived in section III, is only valid for the special
case of P-Core inductors. In general, it must be assumed that
every core has a so-called 'outside window portion' (OW)
[24], where no limb and no core yokes are present. In this
portion of the winding, the magnetic field is not modelled
properly with the proposed model. However, the error is shown
to be comparatively small in [12] (≤2 %). In [25], correction
factors for the reluctance of the OW paths are proposed, which
can be incorporated into the model for the spatial coefficients
in (8) to increase the accuracy.
A. Verification of the model via FEM
In the following, the equations for the inductance and the
winding losses, derived in section III, are verified with FEM
simulations. In addition, a variation of the relative permeability
is investigated. Rotationally symmetrical as well as full 3D
models are used. Because in reality there is a gap between
the conductors and the core yokes, the actual core window
height (hw) is different from the conductor height (hf) in
the FEM simulations. The conductor height in the analytical
calculations and in the FEM simulations are set to the same
value. All geometrical specifications of the FEM model are
given in Tab. II. Note, that all simulations are conducted at
a fixed operating frequency and the conductor thickness is
derived as the optimum thickness for minimum winding losses

## [стр. 8]

TRANSACTIONS ON POWER ELECTRONICS
7
for this frequency according to [26]. The temperature is set to
100 ◦C.
Fig. 4 compares the analytical results to the results obtained
with a rotationally symmetrical FEM model. It is shown, that
the analytical expressions (12) and (16) match well over a
wide frequency range for different numbers of air gaps. The
constant overestimation of the inductance is less than 1 %.
It is notable, that the inductance decreases significantly with
frequency, especially in the case of a single air gap. Due to
the fact, that magneto-quasi-static simulations are performed
with a real-valued and constant relative permeability, this
can only be explained by the magnetic shielding of the foil
conductors: As the frequency increases, eddy currents arise in
the conductors, creating a magnetic field opposite to the air
gap field, which attenuates the air gap field in the conductors.
This effect counteracts the fringing field of the air gaps,
resulting in an overall lower stored magnetic energy in the
core window and consequently in a lower inductance. The
change of inductance in Fig. 4b) is therefore fully caused by
a change in magnetic energy in the core window. Analytical
inductance models known from literature typically neglect the
shielding effect of foil conductors [16].
Since a parametric study of varying finite permeability is
difficult in reality, the respective error is investigated with FEM
TABLE II
PARAMETERS OF THE 2D CIRCULAR SYMMETRIC FEM MODEL
Operating point
I
2
A
Peak sinusoidal current
f
10
kHz
Operating frequency
Geometrical specifications
µr
5000
Relative permeability of the core
lc
97
mm
Effective magnetic path length
Vc
22 700
mm3
Effective magnetic volume
N
5
Number of foil conductors
hf
26.6
mm
Conductor height
hw
29.6
mm
Core window height
dleg
12.2
mm
Center leg diameter
dx,i
1
mm
Distance center leg first conductor
dw
8.65
mm
Core window width
df
440
µm
Conductor thickness
dt
440
µm
Insulation thickness
simulations. Fig. 5b) and c) show the results of the proposed
model computed for a varying finite permeability and of the
FEM model. For µr > 1000 the model results show very
good agreement with the FEM simulations. Below µr = 1000,
the results still match, however, recognizable errors especially
in the winding loss calculation occur (-27 % at µr = 100).
Cases, where the relative permeability is below 100, are not
considered, since with such a low permeability typically no
air gaps are used.
Lastly, two 3D FEM models were simulated with the
parameters of Tab. II (rectangular center leg with bleg = dleg,
aleg = 20 mm). The results are shown in Fig. 6. The average
errors are 2.5 % for the winding loss calculation and 2.1 %
for the inductance calculation in Fig. 6a), and 5.4 % for the
winding loss calculation and 1.6 % for the inductance calculation in Fig. 6b). Note, that the proposed model overestimates
the indutance, especially at low frequencies, with the highest
error of 2.2 %.
B. Verification by measurements
Two inductors based on commercially available cores -
IND 1: ETD 59/31/22 [27] and IND 2: E 65/32/27 [28],
as specified in Tab. III and shown in Fig. 1 - are made
of the material N87 [21]. The winding is composed of foil
conductors, that are wound around the centre leg without
bobbin. The parameter values of the winding are obtained
from measurements of the actual copper foil and the built
inductors. The impedance measurement is performed with an
Impedance Analyzer Keysight E4990A. The measurements
were performed at room temperature.
The impedance of the inductor calculated from the proposed
winding loss and inductance models is given as:
Z =

(R1D + Rgap + jωL)-1 + jωCres
-1
(20)
where Cres = 1/((2πfres)2Lres) is the static stray capacitance
of the inductor obtained from a (floating core) measurement
of the first resonant frequency fres. Since the inductance
is assumed to be frequency-dependent, Lres is analytically
calculated instead of using a static inductance, which could
100
101
102
103
P in mW
Eq. (9)
3D FEM
100
101
102
103
P in mW
Eq. (9)
3D FEM
a)
101
102
103
104
105
106
4.25
4.5
4.75
5.0
f in Hz
L in µH
Eq. (12)
3D FEM
b)
101
102
103
104
105
106
8.5
9
9.5
10
f in Hz
L in µH
Eq. (12)
3D FEM
Fig. 6. Results of a 3D FEM simulation. a) Inductor with circular center leg according to Tab. II. b) Inductor according to Tab. II, but with rectangular center
leg with bleg = dleg and aleg = 20 mm. The impact of the shielding effect on the inductance is notable.

## [стр. 9]

TRANSACTIONS ON POWER ELECTRONICS
8
{
s
R
c
R
1D
R
gap
R
res
C
res
C
′
L
′′
L
j
-
′
L
1D
R
gap
R
a)
b)
Fig. 7. Circuit diagram of the inductor used in this paper and assumed by
the impedance analyzer by (20).
be obtained from a static inductance measurement. Since L in
(20) is complex (consider section IV-B):
jωL = jω (L′ -jL′′) = Rc + jωL′
where L′ and L′′ are the real and imaginary parts of the inductance, ωL′ denotes the reactance of the RL series equivalent
circuit, and
Rc = ωL′′
describes the core losses. A circuit diagram of the inductor
which is used in this paper to identify the individual lumped
parameters, and which is also assumed by the impedance
analyzer internally, is shown in Fig. 7.
The resistance, obtained as ℜ{Z} from (20), is compared
with measurement results in Fig. 8a) and Fig. 8b). For
reference, the plots show R1D, Rgap, Rc, and their sum
Rs = Rgap+R1D+Rc separately to elaborate the individual
contributions of the resistance components to the inductor
impedance.
To verify the inductance calculation procedure, the inductance obtained as ℑ{Z}/ω from (20) is compared to measured
values obtained from the imaginary part of the measured
impedance in Fig. 8c) and Fig. 8d). For reference, the DC
inductance from the AL-value and the inductance L from (16)
are depicted.
To compare the measurements with the calculated values,
it should be noted that the model is sensitive to parameter
variations of dx,i, since this parameter defines the distance
of the foils to the air gap and the fringing field. In order to
examine this impact more closely, calculations with the model
are evaluated. IND 1 is considered, the frequency is set to
10 kHz (at very low frequencies there is no impact, because
there is no shielding effect), and the model parameters are
taken from Tab. III. If it is assumed that the distance dx,i
TABLE III
MODEL PARAMETERS OF THE TWO TEST CASE INDUCTORS
IND 1
IND 2
C
56.6
90.0
pF
Measured capacitance
N
18
18
Number of conductors
lg
2
3
mm
Air gap height
hf
40
40
mm
Conductor height
dleg
22.1
mm
Center leg diameter
aleg
27.4
mm
Center leg diameter
bleg
20.0
mm
Center leg diameter
dx,i
350
450
µm
See Fig. 2
df
100
100
µm
Conductor thickness
deviates from 350 µm by ±150 µm, a variation in resistance
of -8.7 % / 9.9 % and a variation in inductance of 1.4 % / -1.5 %
can be observed, respectively. If the original value of dx,i
is changed from 350 µm to 2 mm and again a variation of
150 µm is assumed, variations in resistance of -5.0 % / 5.5 %
and variation in inductance of 0.6 % / -0.6 % can be observed.
C. Discussion of the results
The results in Fig. 8a) and b) indicate, that at least one major
effect influencing the effective resistance of the inductors is not
considered correctly in the modelling. This becomes evident at
frequencies above 300 kHz. Given the results of section V-A,
the error appears due to either the capacitance or the core
loss modelling. Above 300 kHz, the relative permeability
increases significantly, as shown in Fig. 3, causing the core
losses to increase as well. However, the chosen approach to
take the core losses into account could be less accurate in
the high-frequency range. Furthermore, the significant change
of the complex permeability for frequencies above 300 kHz
[29] influences not only the losses but also the inductance.
Therefore, at the first resonant frequency, which was measured
at 2.37 MHz for IND 1 and 1.90 MHz and IND 2, respectively,
the inductance may have changed significantly, leading to an
erroneous estimation of the capacitance Cres.
The comparison of the effective layer resistance R1D, equivalent to [3] and the air gap resistance Rgap reveals that the air
gap fringing field has a huge impact on the overall resistance.
The reason can be found in the comparatively large expansion
of the conductors in y-direction, which is much larger than
the expansion in x-direction. Hence, the magnetic field can
extend inside the foil in y-direction relatively unhindered,
resulting in a significant increase of eddy currents and thus,
the effective resistance. This fact supports the hypothesis, that
foil conductors perform poorly in the vicinity of air gaps [7].
The average error of the calculated resistance compared to
the measurement in Fig. 8a) for frequencies from 1 kHz to
300 kHz is -14.0 % (in the range of -14.5 % to -13.2 %),
and the error of the calculated resistance in the same frequency
range in Fig. 8b) is between -4.5 % and 6.2 % and the
average error is 2.2 %. In this frequency range, the additional
core losses and capacitive effects are not significant and the
comparison of the proposed model with the measurements
is possible. As indicated by the results of section V-A, the
calculation of accurate results with the proposed winding loss
and inductance models is not limited to a certain frequency
range. The errors in Fig. 8 depends on additional effects,
such as the capacitance, or dimensional and frequency effects
in the core, such as a strongly inhomogeneous flux density
distribution.
Special attention should be paid to the inductance model
that is proposed in this paper. Fig. 8c) and Fig. 8d) show,
that the measured inductance decreases significantly with the
frequency. Since the inductance is directly proportional to the
real part of the complex permeability [29], which does not
change in the relevant frequency range as shown in Fig. 3, this
change is not caused by a change of the relative permeability.
Overall, the model matches the measured inductance well.
As already established in section V-A, the inductance model

## [стр. 10]

TRANSACTIONS ON POWER ELECTRONICS
9
103
104
105
106
10-2
100
102
f in Hz
R1 in Ω
Measured
ℜ{Z}
Rs
Rgap
Rc
R1D
103
104
105
106
10-2
100
102
f in Hz
R2 in Ω
Measured
ℜ{Z}
Rs
Rgap
Rc
R1D
a)
102
103
104
105
106
75
90
105
f in Hz
L1 in µH
Measured
ℑ{Z}/ω
L
ALN2
b)
102
103
104
105
106
75
90
105
f in Hz
L2 in µH
Measured
ℑ{Z}/ω
L
ALN2
Fig. 8. Comparison of the calculated inductance and effective resistance and an impedance measurement of IND 1 in a) and the same for IND 2 in b).
TABLE IV
COMPARISON OF DIFFERENT INDUCTANCE CALCULATION METHODS:
ERROR IN PERCENT COMPARED TO THE MEASURED INDUCTANCE FOR
DIFFERENT FREQUENCIES
f in Hz
25
103
104
105
25
103
104
105
IND 1
IND 2
M1
5.8
5.9
7.1
8.1
5.9
3.4
2.4
2.4
M2
-25.3
-15.9
-8.4
-4.0
-28.5
-19.1
-12.6
-9.4
M3
3.6
16.6
27.0
33.0
2.5
16.0
25.3
30.0
M4
13.9
28.1
39.6
46.2
17.5
33.0
43.8
49.1
M5
4.9
18.0
28.6
34.7
0.7
14.0
23.2
27.7
tends to slightly overestimate the inductance, which is reflected
also in the measurements. However, since the AL-value from
the manufacturer's datasheet also shows this offset, the error is
possibly subject to manufacturing tolerances (e.g. the relative
permeability of the core is lower than the value given by the
manufacturer, the air gap is slightly larger, etc...). On the other
hand, the AL-value and the measurement match well in the
case of IND 2 (Fig. 8d), whereas the proposed model shows
inaccuracies, especially at low frequencies. Here, the model
inaccuracies may be introduced by the correction factor for
rectangular centre legs, which does not consider edge effects
where the conductors are tightly bent around the core edges,
as explained in section III.
For comparison with the proposed model, different methods
from literature are used to compute the inductance. The
methods are the standard procedure using a reluctance network
of the core [30] without considering the fringing effect or
the shielding effect (M2), the method by McLyman [14] to
empirically consider the fringing effect (M3), the SchwarzChristoffel approach [17] to analytically consider the 3D
fringing effect (M4), and the manufacturers AL-value (M5).
The proposed model is denoted with M1. The relative error of
each method compared to the measurement results is shown
in Tab. IV. As expected, all modelling approaches except
for M1 show significant errors at high frequencies, since
they all neglect the shielding effect. However, the results are
unexpected, because M4, which is expected to be accurate
at low frequencies, shows a significant error. It is found that
model M4 shows errors of this magnitude for comparatively
large air gaps, which is especially the case with IND 2. The
same is true for the empirical correction factor of M3. This can
be verified using the manufacturers AL-value. Both models
tend to overestimate the inductance for comparatively large
air gaps but are relatively accurate for small air gaps.
Nevertheless, the measurements show that the proposed
model is accurate in the complete recommended operating
frequency range of the material, especially considering the
shielding effect of the foil conductors and the decreased
inductance, that comes with it. The average error of the
proposed model for all considered cases in Tab. IV is 5.1 %.
D. Additional notes on the measurements
To avoid variations of the measured values, the Impedance
Analyzer was configured to measure 5 values per frequency
point and take the average of those values. In addition,
multiple frequency sweeps were performed. The capacitance
was measured with a floating core.
Regarding measurement accuracy, errors must be expected.
From [31], it can be concluded that the overall measurement
error is below 1 % between 1 kHz and 1 MHz and below
5 % as long as f > 20 Hz, when measuring the impedance
with the given inductor specifications. In addition, since the
impedance is mostly inductive, the resistance measurement is
prone to higher errors. Therefore, the results of the resistance
measurement are shown in a narrower frequency range (1 kHz
and 1 MHz) only, to keep the error as low as possible.
All measurements are performed with sinusoidal smallsignal excitation. Therefore, the relative permeability of the

## [стр. 11]

TRANSACTIONS ON POWER ELECTRONICS
10
core material is modelled as frequency-dependent only. In
reality, the permeability depends non-linearly on the operating point, considering DC-bias, saturation, and the dynamic
position in the B-H loop during operation, as well as the
temperature. Larger deviations of the actual winding resistance compared to the calculated winding resistance must be
expected [32], since the proposed modelling approach is not
capable of capturing these effects. It is therefore recommended
to use different models [33] to account for the additional core
losses.
VI. CONCLUSION
This paper derives an analytical model for the magnetic field
inside the core window of gapped inductors with foil windings.
The resulting expressions allow to analytically calculate the
inductance and the total winding losses, caused by skin,
proximity, and fringing effects. The resulting model is capable
of precisely predicting the expected winding losses and the
inductance of a gapped inductor with foil windings over a
wide frequency range, considering especially the influence of
the air gaps. The average error is below 15 %.
In addition, it is shown, that the inductance of a gapped
inductor with foil windings is frequency-dependent, which is
caused by the shielding effect of the foil conductors. As a
result, the inductance decreases by appr. 20 % compared to
the DC value, which is also proven by measurements. The
proposed model considers this effect and shows improved
accuracy compared to existing inductance models for gapped
inductors, with an average error of 5 % over a wide frequency
range.
ACKNOWLEDGMENT
The authors would like to express their acknowledgment
to the Baechli AG, Switzerland, and Innosuisse, Switzerland
(Appl. No.: 32328.1 IP-ENG), for providing financial support
for this project.
REFERENCES
[1] J. Biela, J. W. Kolar, A. Stupar, U. Drofenik, and A. M. Musing,
"Towards virtual prototyping and comprehensive multi-objective optimisation in power electronics," in Int. Exhib. & Conf. for Power Electronics
Intelligent Motion Power Quality (PCIM), May 2010.
[2] J. Muehlethaler, "Modeling and multi-objective optimization of inductive power components," Ph.D. dissertation, Eidgen¨ossische Technische
Hochschule (ETH) Z¨urich, 2012.
[3] P. L. Dowell, "Effects of eddy currents in transformer windings," in
Proc. of the Institution of Electrical Engineers, vol. 113, no. 8, Aug.
1966, pp. 1387-1394.
[4] M. Bartoli, A. Reatti, and M. Kazimierczuk, "Minimum copper and core
losses power inductor design," in Conf. Rec. of the 31st Ind. App. Conf.
(IAS).
IEEE, 1996.
[5] A. Rahimi-Kian, A. Keyhani, and J. Powell, "Minimum loss design of
a 100 kHz inductor with litz wire," in Conf. Rec. of the 32nd Ind. App.
Conf. (IAS).
IEEE, 1997.
[6] M. Kazimierczuk and H. Sekiya, "Design of AC resonant inductors using
area product method," in Energy Conversion Congress and Exposition.
IEEE, Sep. 2009.
[7] D. Leuenberger and J. Biela, "Semi-numerical method for loss calculation in foil windings exposed to an air gap field," in Proc. Int. Power
Electronics Conference (IPEC), May 2014.
[8] I. Kovaˇcevi´c-Badst¨ubner, R. Burkart, C. Dittli, J. W. Kolar, and A. Musing, "A fast method for the calculation of foil winding losses," in 17th
European Conf. on Power Electronics and Applications (EPE ECCE
Europe), Sep. 2015.
[9] A. Van den Bossche and V. Valchev, "Eddy current losses and inductance of gapped foil inductors," in 28th Annu. Conf. IEEE Industrial
Electronics Society (IECON), Nov. 2002.
[10] P. Wallmeier, N. Frohleke, and H. Grotstollen, "Improved analytical
modeling of conductive losses in gapped high-frequency inductors," in
33rd IEEE Industry Applications Society Conf. (IAS), vol. 2, Oct. 1998,
pp. 913-920.
[11] W. Zhang and T. M. Jahns, "Analytical 2-d slot model for predicting
ac losses in bar-wound machine windings due to armature reaction," in
IEEE Transportation Electrification Conf. and Expo. (ITEC), Jun. 2014.
[12] T. Ewald and J. Biela, "Analytical eddy current loss model for foil
conductors in gapped cores," 23th European Conference on Power
Electronics and Applications (EPE ECCE Europe), Aug. 2021.
[13] W. G. Hurley and W. H. W¨olfle, Transformers and Inductors for Power
Electronics - Theory, Design and Applications.
John Wiley & Sons,
Ltd, 2013.
[14] C. McLyman, Transformer and Inductor Design Handbook. CRC Press,
2017.
[15] A. Van den Bossche, V. Valchev, and T. Filchev, "Improved approximation for fringing permeances in gapped inductors," in Record of the
37th Industry Applications Conf.
IEEE, 2002.
[16] A. Balakrishnan, W. T. Joines, and T. G. Wilson, "Air-gap reluctance and
inductance calculations for magnetic circuits using a schwarz-christoffel
transformation," IEEE Transactions on Power Electronics, vol. 12, no. 4,
pp. 654-663, July 1997.
[17] J. Muehlethaler, J. W. Kolar, and A. Ecklebe, "A novel approach for
3d air gap reluctance calculations," in 8th International Conference on
Power Electronics (ECCE Asia), May 2011.
[18] L. O. Fichte, S. Lange, T. Steinmetz, and M. Clemens, "Shielding
properties of a conducting bar calculated with a boundary integral
method," Advances in Radio Science, vol. 3, pp. 119-123, may 2005.
[19] J. D. Jackson, Klassische Elektrodynamik.
DE GRUYTER, 2013.
[20] M. Albach, Induktivit¨aten in der Leistungselektronik. Springer Vieweg,
Wiesbaden, 2017.
[21] Ferrites and Accessories - SIFERRIT Material N87, TDK, Sep. 2017.
[22] M. Kazimierczuk, High Frequency Magnetic Components.
John Wiley
& Sons, Ltd, 2013.
[23] E. Snelling, Soft ferrites: properties and applications.
NewnesButterworth, 1969.
[24] J. Muehlethaler, J. W. Kolar, and A. Ecklebe, "Loss modeling of
inductive components employed in power electronic systems," in 8th
Int. Conf. Power Electronics, May 2011, pp. 945-952.
[25] A. F. Hoke and C. R. Sullivan, "An improved two-dimensional numerical
modeling method for e-core transformers," in APEC. Seventeenth Annual IEEE Applied Power Electronics Conference and Exposition (Cat.
No.02CH37335), vol. 1, 3 2002.
[26] W. Hurley, E. Gath, and J. Breslin, "Optimizing the AC resistance
of multilayer transformer windings with arbitrary current waveforms,"
IEEE Transactions on Power Electronics, vol. 15, no. 2, pp. 369-376,
mar 2000.
[27] Ferrites and Accessories - ETD 59/31/22, TDK, May 2017.
[28] Ferrites and Accessories - E 65/32/27, TDK, Apr. 2018.
[29] T. P. Todorova, A. V. den Bossche, and V. C. Valchev, "A procedure for
the extraction of intrinsic AC conductivity and dielectric constant of n87
mn-zn ferrite samples based on impedance measurements and equivalent
electrical circuit modeling," IEEE Transactions on Power Electronics,
vol. 33, no. 12, pp. 10 723-10 735, Dec. 2018.
[30] V. C. Valchev and A. V. den Bossche, Inductors and Transformers for
Power Electronics.
CRC Press, Taylor & Francis Group, 2005.
[31] Keysight E4990A Impedance Analyzer, Keysight, 2018.
[32] B. X. Foo, A. L. F. Stein, and C. R. Sullivan, "A step-by-step guide
to extracting winding resistance from an impedance measurement," in
Applied Power Electronics Conference and Exposition (APEC).
IEEE,
Mar. 2017.
[33] K. Venkatachalam, C. Sullivan, T. Abdallah, and H. Tacca, "Accurate
prediction of ferrite core loss with nonsinusoidal waveforms using only
steinmetz parameters," in Workshop on Computers in Power Electronics.
IEEE, Jun. 2002.

## [стр. 12]

TRANSACTIONS ON POWER ELECTRONICS
11
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
