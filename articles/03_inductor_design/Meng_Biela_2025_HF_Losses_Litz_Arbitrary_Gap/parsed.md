# Analytical Models for HF-Losses of Litz Wire in Inductors With Arbitrary Winding and Gap Arrangements

> Автоматически извлечено из `source.pdf` скриптом `parse_pdf.py`
> Движок: pymupdf. Страниц: 14 из 14.
> Дата извлечения: 2026-08-07 06:43 UTC

Текст не редактировался. Формулы и таблицы могут быть искажены —
при сомнении сверяться с исходным PDF.

---

## [стр. 1]

ETH Library
Analytical Models for HF-Losses of
Litz Wire in Inductors with Arbitrary
Winding and Gap Arrangements
Journal Article
Author(s):
Meng, Qingchao; Biela, Jürgen
Publication date:
2025
Permanent link:
https://doi.org/https://doi.org/10.3929/ethz-c-000783521
Rights / license:
Creative Commons Attribution 4.0 International
Originally published in:
IEEE Open Journal of Power Electronics 6, https://doi.org/10.1109/ojpel.2025.3604564
This page was generated automatically upon download from the ETH Zurich Research Collection.
For more information, please consult the Terms of use.

## [стр. 2]

Received 8 July 2025; accepted 27 August 2025. Date of publication 1 September 2025;
date of current version 16 September 2025. The review of this article was arranged by Associate Editor M. Jung.
Digital Object Identifier 10.1109/OJPEL.2025.3604564
Analytical Models for HF-Losses of Litz Wire in
Inductors With Arbitrary Winding and
Gap Arrangements
QINGCHAO MENG
AND JÜRGEN BIELA
(Senior Member, IEEE)
Laboratory for High Power Electronic Systems (HPE), ETH Zürich, 8092 Zürich, Switzerland
CORRESPONDING AUTHOR: QINGCHAO MENG (e-mail: meng@hpe.ee.ethz.ch)
ABSTRACT
Dueto 2D fields in the core window of inductors (e.g. the fringing field caused by core gaps)
large errors can occur in the winding loss calculation, when the assumptions, that the H-field is parallel to
the winding layers and constant along the field line, used for transformers are applied. Numerical methods,
e.g. FEM, are accurate but are very time consuming for calculating the losses of litz wire windings and
therefore cannot be integrated in converter optimisation routines, which require a fast execution due to the
large number of evaluations. To overcome this limitation, this paper proposes a fast and accurate loss model
for litz wire winding in inductors with arbitrary winding and gap arrangements. The application range of
the proposed model covers inductors using cores with single and discrete gaps, and iron powder cores with
distributed gaps. The proposed method is numerically and experimentally validated to be more accurate than
state-of-the-art methods as e.g. the mirror image method and up to 1000 times faster than the semi-numerical
method i.e. the square-field-derivative method with better or equivalent accuracy.
INDEX TERMS Eddy current losses, inductors, litz wire, magnetic fields.
I. INTRODUCTION
Inductors are key components in power electronic systems.
These are often made of a single winding and ferrite cores
with a single or multiple air gaps as shown in Fig. 2(a)-2(d).
The air gaps can be replaced by fictitious current sources for
calculating the winding losses [1]. Alternatively, iron powder
can be used as core material, which is made of iron particles
mixed with isolating binder, which creates a large number of
very small air gaps distributed around the core window. Thus,
distributed gaps can be considered as kind of a high number
of "discrete" gaps. Similar to the gaps in ferrite cores, the
distributed gaps in iron powder cores can also be replaced
by fictitious current sources, so that both core material types
result in a magnetic equivalent structure, where the winding
is surrounded by an ideal core boundary plus fictitious current sheets as shown in Fig. 1. For this equivalent structure,
which can model inductors with arbitrary gap arrangements,
including single, multiple and distributed air gaps, a winding
loss model is presented in this paper. As shown in Fig. 1,
the fictitious current sheets for ferrite cores are not as high
as the window, and the ones for iron powder cores generate
significant a H-field component, that is not parallel to the
winding layers. Therefore, the 1D field assumption in [2], [3],
[4], [5], [6] for transformers (cf. Fig. 2(e)):
r H-field is parallel to the winding layers
r H-field is constant along the field lines
r H-field increases linearly across winding layers
is therefore not suitable.
As shown in Fig. 2(a)-2(d), the H-field inside the window
of inductors with ferrite cores is concentrated near the air
gap(s). Such a field is called fringing field. In Fig. 4 the
H-field inside the window of inductors with iron powder cores
is shown. Compared to the H-field in a transformer as shown
in Fig. 2(e), the H-field in the window of inductors with both
core types does not fulfill the 1D field definition, and are
therefore called 2D fields in this paper. Due to high-frequency
(HF) effects and the 2D fringing field around gap(s) in the
core, litz wire (LW) made of fine enamelled strands, which are
twisted to prevent bundle-level HF effects [7], are frequently
used to reduce the HF-losses. However, due to the complex
© 2025 The Authors. This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/
1534
VOLUME 6, 2025

## [стр. 3]

FIGURE 1. Illustration for transforming the ferrite cores with air gaps and
iron powders cores with distributed gaps to the same structure: ideal core
boundary with fictitious current sheets.
geometry of LW and the 2D field, accurately predicting the
HF losses in LW is challenging. Using 1D field loss models as
e.g. presented in [2], [3], [4], [5], [6] could result in more than
40% error for calculating the winding losses for an inductor
as shown in Fig. 10 and Fig. 11 a. In some special cases
such as in MV applications, a certain insulation distance must
be applied between the windings and the core due to the
isolation requirements as presented in [8] and the error of the
1D field loss models can be up to 100%. Therefore, 2D field
models have been developed for inductors with a single gap
and round wires [9], [10], [11]. However, these models are
very time consuming for LWs with hundreds or thousands of
strands, as the H-field and the losses need to be calculated for
each strand. To overcome this problem, more computationally
efficient 2D field models have been presented in [12], [13],
[14], [15]. However, in [12] and [13] the H-field generated by
the winding itself is not considered, which results in relatively
large errors. The models presented in [14] and [15] are limited
to inductors with a single gap in the center leg and ideal
winding layers (i.e. all winding layers are as high as the core
window). However, in optimised inductor designs the discrete
gaps as shown in Fig. 2(c), arranging the winding away from
the gap(s) as shown in Fig. 2(b), and also the iron powder
cores with distributed gaps as shown in Fig. 4 c are frequently
used for reducing the HF winding losses ([16], [17], [18],
[19]). For calculating the losses in such inductors, the mirror
image method (MIM) presented in [20] and [21] is often used.
There, each gap is replaced by a fictitious current source with
the equivalent MMF of that gap. The LW is usually lumped to
a solid wire and the H-field at the center point of the solid wire
rather than each strand is used for the loss calculation [20], to
avoid difficulties in obtaining the exact coordinates of each
strand and long calculation time. However, the H-field at the
center point of the solid wire does not accurately represent the
average field for each strand, and therefore results in relatively
large errors.
For calculating the winding losses more accurately, the
semi-numerical method SFD (space field derivative) presented in [7] can be used. However, it is relatively slow since
the field is calculated with FEM, so that it cannot be integrated
into the converter optimization routines, where the winding
losses need to be calculated numerous times. As alternative, AI based models as presented in [22], [23], [24] show
promising results for predicting the HF winding losses. However, a large amount of data, including numerous 2D/3D FEM
simulation results, which require tremendous time and computation resources, are needed to train the AI-based models.
Furthermore, due to a lack of physical background, the application range of AI-based models is typically not very clear,
which could result in unpredictable errors. Therefore, these
AI-based models are rarely used in the converter optimization
routines.
To overcome the mentioned problems of the existing calculation approaches, a novel, versatile, accurate, and computationally efficient analytical H-field and HF-loss model for LW
winding in inductors is presented in this paper. The proposed
model is based on the space harmonic method (SHM) and the
turn-wise spatial RMS value of the H-field (TS-RMS). The
application range of this model covers inductors with arbitrary
winding and gap arrangements, including single, distributed,
discrete, vertical gaps, as well as combinations of such gaps.
This model is validated by numerical and experimental results
and it is shown that the proposed model is more accurate than
the state-of-the-art models MIM, and more computationally
efficient than SFD. Therefore, this model is ideal for the converter optimization routines.
This paper is organised as follows. First, the loss calculation
and why the TS-RMS value of the H-field is required are
presented in Section II. In Section III, a short introduction of
the space harmonics method and the TS-RMS value of the
H-field for inductors with gapped ferrite cores and iron powder cores is presented. Furthermore, the model limitations are
also discussed in Section III. Thereafter, the proposed model
is validated numerically and experimentally in Sections IV
and V. Finally, Section VI concludes the paper.
II. LOSS CALCULATION
The HF winding losses can be categorized into losses caused
by the skin and the proximity effect. The skin effect losses
are caused by the H-field of the conductor itself and are
independent of the external H-fields. The equation for losses
per unit length (p.u.l) caused by the skin effect (PS) is derived
in [11], [25] and is given by:
PS = 1
2
ˆI2RDCF( f ),
F( f ) = 1
2Re

αrs
I0(αrs)
I1(αrs)

, α = 1 + j
δ
(1)
where I0 and I1 are modified Bessel functions of the first kind,
δ =
1
√π f σμ0 and σ are the skin depth and the conductivity of
copper, μ0 is the vacuum magnetic permeability, and rs is the
strand radius.
The losses caused by the proximity effect depend on the Hfield through the conductor. Due to the fringing field caused by
the air gap and the single winding arrangement in inductors,
the H-field through the winding is 2D. Therefore, the equation
VOLUME 6, 2025
1535

## [стр. 4]

MENG AND BIELA: ANALYTICAL MODELS FOR HF-LOSSES OF LITZ WIRE IN INDUCTORS WITH ARBITRARY WINDING
FIGURE 2. The field distribution in the core window and current density distribution in LW on the cross section of inductors with ferrite cores and
different gap and winding arrangements. (a) and (b) Inductors with single gap in the middle leg and layered winding and optimized winding. (c) Inductor
with discrete (3) gaps in the center leg. (d) Inductor with a single gap in the center and outer legs. (e) Transformer with simple layered winding. The
window width and height of inductors a-c and d are 5 mm and 8 mm and 5 mm and 8.4 mm. The gap length of inductors a-b, c and d is 0.8 mm, 3 × 0.3
mm and 2 × 0.4 mm. The core thickness of all inductors is 2 mm. The number and diameter of strands of all LWs are 19 and 0.3 mm. The current
amplitude in each turn is 10A.
for the proximity effect losses caused by the 2D H-field (2) as
presented in [26] is used.
PP =nsG( f )H2
n,RMS = nsG( f )

H2
x,RMS + H2
y,RMS

G( f ) = 2π
σ Re

αrs
I1(αrs)
I0(αrs)

H2
n,RMS = 1
S

|⃗Hn|2dS
(2)
As shown in (2) the TS-RMS value Hx,RMS and Hy,RMS are
needed for calculating the losses PP caused by the 2D H-field,
which is presented in the following section.
III. FIELD CALCULATION
In [26], the method for calculating the TS-RMS value of the
H-field based on the space harmonic method (SHM) for transformers with arbitrary winding arrangements is presented.
The conditions for applying the SHM method are:
r Winding is enclosed by a closed rectangular core
boundary
r Core boundary is ideal (μr = ∞)
r Total MMF within the core boundary must be zero
However, the SHM method cannot be directly applied to
inductors with gapped ferrite or iron powder cores due to the
following reasons:
r Due to air gaps in the ferrite cores, the core boundary is
not closed
r Due to the distributed gaps, the core boundary surrounded by iron powder cores is not ideal (effective
μr < 100)
r Due to the single winding arrangement, the total MMF
within the core boundary is not zero
To overcome the limitations caused by the inductor geometries, this paper focusses on how to apply the SHM method
for calculating the TS-RMS value of H-field for inductors
with gapped ferrite and iron powder cores, as presented in the
following sections.
A. FERRITE CORE WITH GAPS
For inductors with gapped ferrite cores, air gaps are typically
replaced by "fictitious" current sources. However, the impact
of the shape and location of the fictitious current sources
on the H-field and winding losses is missing. Compared to
using a round conductor to replace the gap in the MIM, a
better replacement of the gap is a current sheet, which is
infinitely thin and as long as the air gap. Since the SHM
is derived for rectangular conductors, the gaps are replaced
by very thin current bars instead of infinite thin ones in this
paper. However, using a current bar with a thickness of wg
reduces the distance between the winding and air gap(s) by
wg. This results in an overestimated H-field value as well as
losses. To reduce the error caused by thickness wg, wg needs
to be as small as possible. However, the thinner the current bar
is, the higher becomes the gradient of the H-field within the
current bar, (cf. Fig. 3(a1)). Since a double Fourier series for
accurately describing H-fields with higher gradients requires
more harmonics as shown in Fig. 3(c), a proper thickness of
the equivalent current bar wg needs to be selected, so that
the TS-RMS value of the H-field can be accurately calculated
with a reasonable number of harmonics and calculation time.
To quantitatively determine the thickness of the current bars,
wg is changed with respect to the window width ww. The
discrepancy of Hn,RMS between the inductor with a single gap
in Fig. 3(b) versus the inductor with current bars with different
width ratio wg/ww is shown in Fig. 3(c). The discrepancy
converges to around 0.28% as wg/ww approaches below 1%
(see Fig. 3(d)). As shown in Fig. 3(c), the convergence curves
for wg/ww ratio below 1% remain the same, therefore, the
required number of harmonics does not increase with decreasing wg/ww ratio. Furthermore, the error of Hn,RMS of all turns
converges to below 0.5%, when more than 25 harmonics are
considered. As the results in Fig. 3(c) and 3(d) are valid for
inductors, of which the required number of harmonics for
calculating Hn,RMS depends mainly on the wg/ww ratio, the
thickness must be selected so that the wg/ww ratio is much
smaller than the gap length to winding height ratio (lg/hw).
1536
VOLUME 6, 2025

## [стр. 5]

FIGURE 3. a1)-a3) Comparison of H-field calculated by the proposed
model (SHM), MIM and SFD. b) Convergent curve of TS-RMS value Hn,RMS
calculated by the proposed model with wg = 0.01ww for each turn
compared to the 2D FEM with gapped ferrite cores. c) Convergent curve for
Hn,RMS of all turns compared to the 2D FEM with an equivalent current bar
with thickness wg = (0.5% ∼10%)ww d) Error of the Hn,RMS calculated by
the proposed model of all turns vs. wg/ww ratio compared to the 2D FEM
results for the inductor shown in c) and the loss portion of each turn. The
loss portion are calculated at  = 1. e) The absolute error of total losses
for each turn calculated with the proposed model, MIM and SFD.
Therefore, in this paper the thickness of the equivalent current
bars is selected so that wg ≤0.01 × ww & wg/ww ≪lg/hg.
In addition to the thickness wg, the MMF of each equivalent
current bar also needs to be accurately calculated. As the permeability of ferrite core is very high (μr > 1000), the H-field
in the core can be neglected. Therefore, the total MMF of the
winding NI is distributed only to the gaps as given by:
ng

n=1
Hgnlgn = NI
(3)
There, ng is the number of gaps, Hgn is the average H-field
through the nth gap, N is the number of turns, and lgn is the
gap length of the nth gap. In most applications, the gap lengths
are usually identical. Therefore, it is assumed that the average
H-fields through all gaps are identical (Hg1 = Hg2 · · · = Hgn)
in this paper.
B. IRON POWDER CORES
As the saturation flux density of iron powder cores is higher
than the one of ferrite cores and no fringing field occurs,
iron powder cores are frequently used in the frequency range
where the core losses are not that critical. Due to the distributed gap, the effective relative permeability of iron powder
cores is very low (usually in the range of 10 to 100).
Therefore, the core cannot be considered ideal anymore. Consequently, the current in the resulting images is no longer
equal to the current in the original conductors. Furthermore,
the field pattern is also not periodic anymore in the 2D plane,
and cannot be described by a double Fourier series. In other
words, the SHM cannot directly be used to calculate the
H-field in the window surrounded by a core with low permeability.
In addition, the MMF of the core is not zero due to the
distributed gaps in the core, which affects the H-field distribution across the winding significantly as shown in Fig. 4. Using
the cross-section on a 2D plane (Fig. 4(a)), which is infinitely
extended in the z direction, to calculate the field and losses
results in large errors compared to the 3D FEM simulations
for windings with pot or EE cores as shown in Fig. 4(b)-4(d).
To solve this problem, the core with distributed gaps can be
replaced by ideal cores and equivalent current bars as shown
in Fig. 5.
Both inductors with pot and EE cores have the same cross
section as shown in Fig. 5. Based on the H-field distribution
in the core, the cross section of the both core types can be
separated into 8 sections as shown in Fig. 5(b), where 8 current bars are needed to replace the core sections. The H-field
through each core section can be calculated by the flux density
distribution in the core. According to Ampere's law, the sum
of MMF for each core section is equal to the total MMF NI as
given by:
M1 + 2(M2 + M3 + M4) + M5 = NI
(4)
As the permeability is considered to be constant everywhere
in the core, i.e. B = μH, (5) can be derived based on (4).
S5
S1
l1 + 2
	S5
S2
l2 + S5
S3
l3 + S5
S4
l4

+ l5

H5 = NI
(5)
There, l1 ∼l5 are the lengths of the equivalent current bars
and S1 ∼S5 are the effective cross-section areas perpendicular to the flux. Note that the areas S1, S3, and S5 are usually
identical for EE cores, thus, equation (5) can be simplified to:
[l1 + 2 (2l2 + l3 + 2l4) + l5] H5 = NI
(6)
By contrast, the areas S1, S3, and S5 are not equal for pot cores
as shown in Fig. 4(b). The equations for calculating the area
S1-S5 for EE and pot cores are given in the appendix. Finally,
the average H-field (H1 -H8) and MMF (M1 -M8) for each
core section can be derived based on given core dimensions.
VOLUME 6, 2025
1537

## [стр. 6]

MENG AND BIELA: ANALYTICAL MODELS FOR HF-LOSSES OF LITZ WIRE IN INDUCTORS WITH ARBITRARY WINDING
FIGURE 4. 3D effect of inductors with pot and EE iron powder core, of which the permeability is equal to 10. a) H-field distribution on the cross section
calculated by FEM on a 2D plane that is infinitely extended in the z direction. b) H-field distribution of an inductor with a pot core calculated by 2D FEM
with axis symmetry. c) H-field distribution of an inductor with EE core calculated by 3D FEM. d) Normalised Hn,RMS for each turn for inductors in a) and b)
and for the cross section inside the core window (IW) and outside the core winding (OW) in c).
FIGURE 5. (a) H-feild in an iron powder core. (b) Replace the iron powder
core in a) with current bars with equivalent MMF and an ideal core. The
core are divided into 8 sections and each section is replaced by the an
equivalent current bar attached on an ideal core section.
Note that the thickness of each current bar is equal to 1/100 of
the window width.
C. MODEL LIMITATIONS
Due to limitations of the SHM, the proposed field and loss
model can be applied only to cores with rectangular core
windows, including E, U, P, ETD, UR, etc. shaped cores.
Toroidal cores are not included. As the static H-field is used
in the loss calculation, the proposed model is accurate in the
frequency range, where the penetration ratio is smaller than
2 ( = ds/δ < 2). The proposed model can be applied also
at higher frequencies, but there typically higher errors occur.
Furthermore, at large excitation currents, which significantly
reduce the relative permeability of the gapped ferrite cores
(μr,c), the ferrite core cannot be considered as an ideal core
anymore and need to be replaced by current bars with an
equivalent MMF. In this case, the MMF contributed by the
core (MMFc) also needs to be considered in the MMF equation (3), which becomes:
ng

n=1
Hgnlgn + MMFc = NI
(7)
FIGURE 6. Field comparison for IW and OW cross section in two different
inductors. a1) and b1) The field distribution on the cut plane (highlighted
in magenta) for the inductor with single gap in the center leg and the
inductor with a single gap in all legs. a2) and b2) The H-field (Hn)
distribution along the inner and out turn path of inductors shown in a1)
and b1), the start point and direction is also given in a1) and b1). As the
H-field of the outer turn path in a1) is equal to almost zero, only the
H-field along the inner path is shown in a2).
The
method
for
calculating
MMFc
is
explained
in
appendix B. For non-sinusoidal input currents, the method
presented in [27] can be used. There, non-sinusoidal
currents
are
decomposed
into
different
harmonics
by
using a Fourier series. The winding losses for each
harmonic can be calculated by using the proposed model.
By summing up the winding losses for each harmonic,
the winding losses for non-sinusoidal currents can be
calculated.
1538
VOLUME 6, 2025

## [стр. 7]

FIGURE 7. Calculation procedure of the total winding losses. The
highlighted boxes are for calculating the TS-RMS value of the H-field.
For E-and U-shaped cores, the field and the losses for winding sections inside (IW) and outside the core window (OW)
can vary significantly depending on the winding and gap arrangements. For inductors with the following arrangements:
r Windings are close to the gap
r Distance between windings and gaps for IW and OW
winding sections is identical
r Number and location of the gap are identical in the IW
and the OW winding sections
the field and the loss differences for IW and OW winding
sections are very small (PIW /POW -1 < 5%) as shown in
Fig. 6(a1) and 6(a2). Therefore, the total winding losses of
such inductors can be calculated by scaling the losses of the
IW winding section with the turn length.
However, as can be seen in Fig. 6(b1) and 6(b2), the H-field
distribution in the IW and the OW winding section can be significantly different for inductors with a single gap in all core
legs. Since there are 3 gap(s) in the IW winding section and
only one gap in the OW winding section. The field amplitude
along the inner and the outer turn path of the IW winding
section is much higher than the field amplitude for the OW
winding section. For such inductors, the field and the losses
FIGURE 8. a1)-a3) Comparison of H-field calculated by the proposed
model, MIM and FEM for inductors with iron powder cores (μr = 10). Only
half of the cross section is shown as it is symmetric to the midline. The
window height and width are 29.8 mm and 9.3 mm. The core thickness is
6.1 mm. The number and diameter of the strands in all LWs are 37 and
0.4 mm. The winding losses of a3 are calculated in axis symmetric, hence,
a pot core is considered in the losses calculation in a1. b) Convergent
curve of the Hn,RMS for each turn and for all turns. The number of
harmonics of the red point is used to calculate Hn,RMS in c). c) Hn,RMS and
field ratio at different permeability 1 ≤μr ≤104. The field ratio is equal to
Hn,RMS(μr )/Hn,RMS(μr = 1) -1.
must be calculated separately for IW and OW winding sections, since scaling only the losses for the IW winding section
with the turn length overestimates the total losses. However,
the field and the loss calculation for the OW winding section
are beyond the scope of this paper.
IV. NUMERICAL VALIDATION
In this section, the H-field and the loss model are validated
with 2D FEM results. The calculation procedure for the field
and the losses is shown in Fig. 7. The highlighted steps are
for the calculation of the TS-RMS value of the H-field. The
H-field and loss model are validated separately for inductors
with ferrite cores and gaps and for inductors with iron powder
cores. For comparison, the state-of-the-art models MIM and
SFD are used, as both models can also be applied for inductors
with different core materials, winding, and gap arrangements.
A. FIELD MODEL VALIDATION
The field model is validated first for inductors with ferrite
cores and gaps. The validation is conducted based on the inductor setup shown in Fig. 2(a). As shown in Fig. 3(a1)-3(a3),
the H-field distribution is calculated by the proposed model,
the MIM as well as the FEM. Furthermore, the value Hn,RMS
for turns 1-8 is compared to the 2D FEM simulation with a
gap as shown in Fig. 3(b). The error of all turns converges
VOLUME 6, 2025
1539

## [стр. 8]

MENG AND BIELA: ANALYTICAL MODELS FOR HF-LOSSES OF LITZ WIRE IN INDUCTORS WITH ARBITRARY WINDING
FIGURE 9. (a)-(d). Error for total winding losses of the proposed model, the MIM and the SFD model compared to the 2D FEM results for inductors with
ferrite cores and gap(s) shown in Fig. 2(a)-2(d).
FIGURE 10. a) Total winding losses for different gap length to window
height ratio lg/hw. b) Error compared to the FEM results
(Error = (Pmodel/PFEM -1) × 100%) versus gap length to window height
ratio lg/hw. Both diagrams are calculated based on the inductor setup in
Fig. 2(a) at frequency  = 1. The ratio lg/hw is changed from 0.0125 to 1,
and the gap length is changed from 0.1 mm to 8 mm.
FIGURE 11. a) Error of total losses p.u.l calculated by the proposed model,
MIM, SFD, and 1D field model at μr = 10, compared to 2D FEM results
with axis symmetry for inductor case shown in Fig. 8 a1-a3. b) Error of
total losses at different permeability 1 ≤μR ≤103 at  = 1.3 (point with
the highest error highlighted by red frame in a).
to a value close to zero when more than 20 harmonics are
considered. Based on the error curves in Fig. 3(b) and 3(d), it
can be concluded that the proposed field model, which uses a
current bar with a thickness less than 1% of the window width
to replace the gap, is very accurate compared to the 2D FEM
results. As it is important to estimate the temperature at the
hot spot to avoid overheating of the winding, an accurate loss
estimation for turns close to the gap is required. As shown in
Fig. 3(d), the turns close to the gap (turn 2 and 3) contribute
more than 70% of the total winding losses. The error of the
proposed model for estimating the losses in turn 2 and 3 is
around 2%, which is much smaller than the error of the MIM
(10%) and the SFD model (> 60%). Therefore, the proposed
model is more accurate in estimating the losses of turns close
to the gap than the other two models. The large loss error for
each turn in MIM and SFD is explained in Section IV-B.
In Fig. 8 the proposed field model for inductors with an iron
powder core is evaluated. As can be seen in Fig. 8(a1), the core
with low permeability is replaced with 8 different current bars
with a thickness of 1% of the window width and ideal core
boundaries. The H-field distribution calculated by the proposed model is very close to the 2D FEM results. By contrast,
the H-field distribution of the MIM is significantly different
compared to the 2D FEM results as shown in Fig. 8(a2). The
reason is, that MMF of the core, where the H-field is not zero
due to the distributed air gaps of the core, is not considered
in the MIM. The TS-RMS value of each single turn and all
turns is compared to the FEM results as shown in Fig. 8(b).
The largest error of the field value Hn,RMS of each single
turn converges to about 12%, since replacing the cores by
the current bars with homogenous current density is not ideal
due to the non homogenous H-field distribution in the core.
Nevertheless, the error of the field value Hn,RMS of all turns
converges close to zero when more than 20 harmonics are
considered. Furthermore, the field value Hn,RMS of all turns
is calculated for different core permeability μr from 1 to 104.
Since the field value Hn,RMS converges to a constant already
around μr = 1000 (cf. Fig. 8(c)), the H-field values Hn,RMS
at μr > 1000 are all equal to the one at μr = 1000. As can
be seen in Fig. 9, the field value Hn,RMS changes rapidly from
1 to 10, and the field value Hn,RMS increases around 10% at
μr = 10 compared to the one at μr = 1. Beyond μr = 10,
the H-field value converges to a constant value, and increases
only by 1.6% at μr = 104 compared to the one at μr = 10.
Therefore, the impact of the permeability of the iron powder
core (10 < μ < 100) on the H-field calculation is very small
(< 1.6%) and can be neglected.
B. LOSS MODEL VALIDATION
In this section the total losses p.u.l are validated based on 2D
FEM results for inductors with ferrite cores and different gap
arrangements and for inductors with iron powder cores. Four
inductors with ferrite cores but with different gap arrangements as shown in Fig. 2(a)-2(d) are used for the validation.
The loss error of the proposed model, and the other two
1540
VOLUME 6, 2025

## [стр. 9]

models based on MIM and SFD compared to the 2D FEM
results are shown in Fig. 9(a)-9(d). The error of the MIM
is the largest one among the 3 methods, as the air gap(s) is
replaced by round conductors and the field in the center of
each turn does not represent the average field of the turn,
as in inductors the 2D field does not change linearly across
the winding layer. The error of the proposed model is sightly
smaller than the one of the SFD model, as with the SFD model
the RMS value of the field over the complete winding block
rather than over each turn is used, and the field in different
turns varies significantly. Therefore, using a single RMS value
over the winding block results in a relatively large error for the
losses of each turn and also a slightly larger error compared
to the proposed model for the losses of all turns. The error
of the proposed model is smaller than 7% for all considered
inductor setups shown in Fig. 2, which is the lowest among
these 3 methods.
To further evaluate the application range of the proposed
model, the model is also evaluated for different gap length.
As can be seen in Fig. 10(a), the losses calculated by the
proposed model, the MIM, the SFD and the 1D field model
are compared to the FEM results for inductors with a gap
length from 1.25% to 100% of the window height. The losses
calculated by the MIM model are a constant value, since the
H-field calculated by MIM is only related to the center point
coordinate of the gap and each turn, and does not depend
on the gap length or the turn diameters, as can be seen in
the field equation presented in [20] and [21]. Therefore, the
MIM cannot determine the impact of the gap length on the
HF-losses of the winding. The 1D field model has the worst
accuracy at lg/hw < 0.1 with an error up to -25%, since the
fringing field caused by the air gap is not considered. In the 1D
field models [2], [3], [4], [5], [6], the average H-field value for
each layer (Havg = (Hle f t + Hright )/2) is used for calculating
the proximity effect losses. Furthermore, the H-field values on
the layer boundaries (H1D = NI/hw), i.e. Hle f t and Hright, are
independent of the gap lengths and depend only on the total
current involved in the field path NI and the window height
hw. In contrast, the length of the equivalent current bar can
be adapted to the gap length in the proposed model, and the
impact of the gap length on the winding losses can be well
determined. As can be seen in Fig. 10(b), the change of the gap
length has no impact on the accuracy of the proposed model
when the gap length is smaller than 20% of the window height,
which covers the most cases. At lg/hw > 0.2, the error of the
proposed model varies from -1% to the maximum value 1%
at lg/hw = 0.6. The accuracy of the proposed model changes
only by 2%, when the gap length lg changes from about 1% to
100% of the winding height. Hence, the proposed model can
be used for different gap lengths.
The proposed model is also validated for inductors with
iron powder cores. As there are no gaps in such inductors and
no special winding arrangements can be used to reduce the
losses, only a single inductor (Fig. 8(a)) is used for validation.
The loss errors of the proposed model, the MIM, the SFD, and
the 1D field model are presented in Fig. 11(a). The errors of
FIGURE 12. a) Calculation time vs. number of turns and number of
harmonics for the proposed model. b) Comparison of the calculation time
for the MIM and proposed model, where 25 harmonics are considered.
Using less than 10 harmonics in the calculation can results in more than
20% error in the calculation of Hn,RMS for each turn, however, the
calculation time can be reduced more than 30% compared to using 25
harmonics.
FIGURE 13. Coils and cores used in the experimental validation. The
parameters of the coil and the core are shown in Table 2 and Table 3.
the MIM and the 1D field model are higher than 40% and are
much higher than those of the proposed and the SFD model.
The reason is, that the MMF in the core is not considered in
the field calculation of the MIM/1D field model, what results
in a large error in the field as well as in the loss calculation.
The error of the SFD model is the lowest among these 4
methods, as the field calculation with FEM is more accurate
than the proposed model. The maximum error of the proposed
model for the total losses is around minus;5% which is slightly
larger than the one of the SFD method (3.5%). Due to the less
accurate field estimation in each turn, the loss error in a single
turn of the proposed model is up to 20%, which is still much
lower than the one of the MIM (up to -80%) and the SFD
model (up to 450%). Furthermore, the proposed model can
also be used for inductors based on iron powder cores with
different permeabilities. As shown in Fig. 11(b), the error of
the total winding losses at  = 1.3 is 2.5% at μr = 1 and
converges to -6% when μr increases to infinite.
C. CALCULATION TIME
The proposed model is not only accurate but also computationally efficient. The loss models for inductors with gapped
ferrite and iron powder cores use the same field model to
VOLUME 6, 2025
1541

## [стр. 10]

MENG AND BIELA: ANALYTICAL MODELS FOR HF-LOSSES OF LITZ WIRE IN INDUCTORS WITH ARBITRARY WINDING
TABLE 1. Measurement Conditions
calculate the TS-RMS value of the H-field, which requires
more than 95% of the calculation time for the winding loss
calculation. Therefore, the calculation time of the winding
losses for inductors with both core types is approximately
equal to the time for calculating the H-field value Hn,RMS.
By using the algorithm developed in [26], the calculation
time of the proposed model is determined for inductors with
up to 50 turns and with up to 50 harmonics on a computer
with a 4 core CPU of 3.85 GHz, as shown in Fig. 12(a).
The calculation time for Hn,RMS increases rapidly with the
number of harmonics, since the calculation time of Hx,RMS
and Hy,RMS increases with m4, as presented in [26]. However,
the calculation time almost linearly increases with the number
of turns as shown in Fig. 12(b), since the field calculation is
performed turn-wise. To compare the calculation time fairly,
all 3 methods are performed on the same computer, the calculation time of the MIM and the proposed model with 25
harmonics are presented in Fig. 12(b). The proposed model
uses almost twice the time of the MIM for the same number
of turns, however is still around 20-50 times faster than SFD,
of which the calculation time of the H -field by using 2D FEM
is more than 2 s.
V. EXPERIMENTAL VALIDATION
In the experimental validation, the winding resistance measured by an impedance analyzer is compared to the one
calculated by the proposed model. However, to accurately
measure the winding resistance the following requirements
must be satisfied:
1) LW causes substantial HF-losses at a frequency that is
far below the first resonant frequency of the inductor
2) Winding resistance should be high enough to be accurately measured by an impedance analyzer
3) Q factor of the inductor should be low, so that the winding resistance can be accurately measured
4) Impact of core losses on the measured winding resistance for inductors with iron powder cores must be
eliminated
To meet the first and the second requirement, a LW with a
relatively large strand diameter (0.2 mm) and a low number of
strands (60) is used (cf. LW1 in Table 2). However, such a LW
is not commonly used in inductors operated at above 100 kHz.
Therefore, in addition to the LW with 0.2 mm strand diameter,
a LW made of 420 strands with a diameter of 0.071 mm,
which is more common for medium frequency inductors, is
TABLE 2. Litz Wire and Coil Parameters
TABLE 3. Core Parameters
TABLE 4. Inductor Parameters
also used (cf. LW3 in Table 2). Requirements 1 and 3 both
can be fulfilled by reducing the inductance, which can be realized by increasing the gap length, what reduces the effective
permeability, and by reducing the number of turns. Therefore,
the available ferrite cores with the largest gap length and iron
powder cores with the lowest effective permeability are used
in the experiment. However, achieving a small inductance
value by reducing the number of turns results also in a small
winding resistance and a low measurement accuracy. Thus,
a trade-off is made in this paper, in which the minimum DC
winding resistance is kept between 32 m to 37 m, so that
the measurement error is below 10% at lower frequencies
according to [28]. The winding length (between 3.3 m and
3.8 m) can be calculated based on the DC resistance per meter
of the selected LW. To match the winding length, relatively
large ferrite cores ETD 59/31/22 with a single and 3 gaps in
the center leg and a pair of iron powder cores E65/32/27 are
used. The detailed winding and core parameters are given in
Table 2 and 3, based on which three inductors as shown in
Fig. 16(a)-(c) are built. The measurement conditions are listed
in Table 1. The measurement accuracy and the impact of the
core losses are discussed in the following.
1542
VOLUME 6, 2025

## [стр. 11]

FIGURE 14. a) The calculated measurement error for impedance analyzer
EImp and the total measurement error, including EImp and the error caused
by the fixture Ef calculated based on [28] are compared to the
measurement error Es calculated by the software provided by the
manufacturer. The measurement error ECom for phase angle compensation
at 6 different frequency ranges is also given. b) The measured AC
resistance without the phase angle compensation Rw is compared to the
AC resistance with the phase angle compensation Rt including and
excluding the ESR (Rt -RC) of the capacitors connected in series with the
inductor.
A. MEASUREMENT ACCURACY
The quality factor Q of inductors 1-4, as shown in Table (4)
are still very high, despite the measures made for reducing the
inductance. High quality factors result in a phase angle that is
close to 90◦, between the measured current and voltage, what
results in a large error range (e.g. the maximum error range
shown in Fig. 14(a) is -40% ≤Emea = EImp + E f ≤40%,
where Emea, EImp and E f are the total measurement error and
the measurement error caused by the impedance analyzer and
by the fixture). To further evaluate the measurement error,
a phase angle compensation study, which is similar to the
method presented in [29], is used. The phase angle of the
inductor is compensated to a value less than 88.5◦by connecting a film capacitor in series, to reduce the measurement
error to less than 5%. As the equivalent series resistance
(ESR) of the capacitor RC is between 10 m and 100 m,
RC must be subtracted from the measured real part of the
impedance. As shown in Fig. 14(b), the directly measured
winding resistance is very close to the one determined with
the phase compensation, in which RC is subtracted. Therefore,
the directly measured winding resistance is accurate enough to
validate the winding loss models.
B. WINDING RESISTANCE EXTRACTION
As shown in Fig. 15(a), the measured real part of impedance
Re{Z} contains not only the winding resistance Rw, but also
the ESR for the core losses Rcore. Due to very low loss density
and low voltage excitation (Vin ≤0.5 V), the core losses of
inductors 1, 2 and 3 with ferrite cores can be neglected in
the measured frequency range. However, the core losses of
inductor 3 with iron powder cores cannot be neglected. The
core losses of iron powder cores could be equivalent to or even
larger than the winding losses, as shown in Fig. 15, where
the core resistance is around 2 times the winding resistance
at 100 kHz. To subtract the core losses, an inductor (inductor
5) with the same core as inductor 3 but with LW2, of which
the strand diameter is only 40 μm so that almost no HF losses
are generated up to 100 kHz, is used. Furthermore, to keep the
FIGURE 15. a) The equivalent circuit and vector diagram of the inductor
under test, where Rw is the winding resistance, Rcore is the ESR of the core
losses, and L is the inductance. The phase of the input voltage is
considered to be 0. b) The amplitude and phase angle of the flux density
for inductor 3 and 5 based on measured impedance and equation (8).
c) The discrepancy of the amplitude and the phase angle of flux density in
inductor 3 and 5. d) The measured real part Re{Z} of impedance for
inductor 5, DC resistance of LW2 RDC,LW2, and the ESR of the core losses
Rcore = Re{Z} -RDC,LW2.
same core losses as in case of inductor 3, the flux density⃗B
in the core (as given by (8)) is kept the same as for inductor
3 at each frequency based on [30]. This can be achieved by
using the same input voltage Vin, the same number of turns
N and the same core cross section area Ac as for inductor 3.
Due to a very low excitation current of the impedance analyser
(Iin < 20mA), the core temperature variation caused by the
heat dissipation of the different windings in inductors 3 and 5
can be neglected.
B =
jωL
Rwc + jωL
-Vin
jωAcN
(8)
As shown in Fig. 15(b) and 15(c), the amplitude and the phase
angle of the flux density of inductor 3 and 5 are not identical
in the low frequency range ( f < 1 kHz), due to the different
winding resistance. Nevertheless, with increasing frequency,
the reactance jωL becomes much larger than the resistance
Rwc, so that the phase angle θ is nearly equal to 90◦and VL
is almost equal to Vin for both inductor 3 and 5, as shown
in Fig. 15(a). Therefore, the flux density through the core
for inductor 3 and 5 is almost identical at relatively high
frequencies ( f > 1 kHz), as shown in Fig. 15(b) and 15(c).
Consequently, the ESR of the core losses Rcore in inductor 5
can be considered to be equal to the one for inductor 3 at f >
1kHz. As the AC winding resistance of inductor 5 is almost
equal to the DC winding resistance up to 100 kHz, the ESR of
the core losses can then be calculated by Re{Z} -RDC,LW 2,
as shown in Fig. 15(d). Finally, the winding resistance of
inductor 3 can be extracted.
C. MEASUREMENT RESULTS
The winding resistance calculated by the proposed model for
inductors 1-4 is compared to the measured one, as shown in
VOLUME 6, 2025
1543

## [стр. 12]

MENG AND BIELA: ANALYTICAL MODELS FOR HF-LOSSES OF LITZ WIRE IN INDUCTORS WITH ARBITRARY WINDING
FIGURE 16. Experimental verification of the proposed model. a)-d) Comparison of the AC resistance calculated by the proposed model (New) to the one
calculated by MIM and SFD model, and to the measured AC resistance for 4 inductors as given on the top of each figure. The core and coil used to build
the inductors can be found in Fig. 13. e)-h) The error compared to the measurement for the proposed, MIM, and SFD model. The error is calculated by
(RAC,model/RAC,Measurement -1) × 100%. The error for the frequency points smaller than the frequency limit at the green line is considered to be unaffected
by the parasitic capacitance.
Fig. 16(a)-(d). Due to the parasitic capacitance, the measured
real part of the impedance is no longer equal to the winding
resistance above a certain frequency limit, and increases much
faster than the winding resistance with the frequency. This
results in a rapid change to negative values of errors, as shown
in 16(e)-(h), where the error curves drop quickly, when the
penetration ratio  is larger than the frequency value marked
by the green line. In the following, all three models are compared to the measurement results within this frequency value.
3D FEM simulations, as shown in Fig. 16(a)-(d), are used to
calculate the RMS value of the H -field for the winding block
used in the SFD model. The calculation time of the 3D FEM
is from 45 s to 133 s for very coarse meshes, on a computer
with a 4-core 3.2 GHz CPU.
The errors of the proposed model for inductor 1 with a
single gap, is less than 4%, which is smaller than the MIM
(6%) and slightly higher than the SFD model (3%). However,
for inductor 2 with 3 gaps in the middle leg, only the error of
the proposed model is less than 10%, whereas the max error
of the other two models is about 13%. The maximum error of
the proposed model for inductor 3 is smaller than 5%, which is
slightly better than the SFD model, but much smaller than the
MIM with more than 20% error. For inductor 4, the proposed
model is the most accurate one with an error less than 8%,
whereas the error of MIM and SFD is up to 14% and 10%,
as shown in Fig. 16(h). It can be concluded that the proposed
model is more accurate than the MIM, especially for inductors
with iron powder cores. The proposed models has a better or
similar accuracy as the the SFD model for all inductor types
shown in Fig. 16. However, the proposed model is 1000 times
faster than the SFD model for inductors, where a 3D FEM is
needed.
Furthermore, as can be seen in Fig. 16(a)-16(c), the AC resistance of inductor 1-3, which are made by the same LWs and
similar winding arrangements, decreases with the increasing
number of the air gaps. The reason is that by breaking a single
air gap into multiple air gaps evenly results in a less concentrated fringing H-field, which reduces the amplitude of the
H-field through the windings as well as the proximity effect
losses. The fringing H-field becomes more homogeneous and
the proximity effect losses can be further reduced, when the
air gaps is split into a infinite number of air gaps distributed
around the core boundary as in iron powder core.
VI. CONCLUSION
In this paper, an accurate and fast analytical loss model is
presented, which can be applied to inductors based on ferrite
cores with single and discrete gaps and iron power cores.
Also arbitrary winding arrangements can be considered. By
numerical and experimental validation for various inductor
setups, the proposed model is more accurate than the MIM
and is as accurate as the SFD model but up to 1000 times
faster. By varying the gap length and permeability, it has
been proven that the proposed model is very robust against
the change of gap length, and the error changes less than
10% when the effective permeability changes from μr = 1 to
infinity. Furthermore, the proposed model estimates the losses
of the turns close to the gap(s) with less than 3% error (cf.
Fig. 3(e)), which is much lower than the error of the MIM
(> 10%) and the SFD model (> 60%) and is helpful for computing the hotspot temperature and prevent overheating in the
winding. Therefore, the proposed model can be integrated into
the converter optimisation routines and improve the inductor
and converter designs.
1544
VOLUME 6, 2025

## [стр. 13]

APPENDIX A
DIMENSION OF E AND POT CORES
Calculation of the length of each core section used in equivalent MMF calculation (for pot and E iron powder cores).
l1 = h1
(9)
l2 = l4 = l6 = l8 = πr1/2
(10)
l3 = l5 = w2
(11)
The effective cross section area that the flux passes through
for each core section for pot core shown in Fig. 4(b), which
is used for numerical validation of the proposed model, is
equal to:
S1 = πr2
2
(12)
S3 =
1
r3 -r2
 r3
r2
2πrh2dr = π(r2 + r3)h2
(13)
S5 = π(r2
4 -r2
3)
(14)
As the flux concentrates to the half part closer to the core
window at the corner core section (2,4,6 and 8 in Fig. 17(a))
as can be seen in Fig. 4(b) and 4(c), the effective cross section
of these corner core sections are equal to:
S2 = S8 = S1 + S3
4
(15)
S4 = S6 = S3 + S5
4
(16)
Note that (15)-(16) are valid for both pot and E cores. The
effective cross section areas of different core sections for E
cores, where the cross-sections perpendicular to the flux in
different core sections are not identical, are equal to:
S1 = w1tc
(17)
S3 = h2tc
(18)
S5 = w3tc
(19)
APPENDIX B
MMF CALCULATION FOR GAPPED FERRITE CORES
INCLUDING SATURATION EFFECT
The permeability of the ferrite core decreases at higher currents/flux densities. Therefore, the H-field as well as the MMF
through the core are not zero anymore and need to be considered in the MMF calculation for the air gaps (cf. (7)). A
simple inductor as shown in Fig. 18(a) is taken as an example
for presenting a method for calculating the MMF contributed
by the core (MMFc). The magnetic circuit for this simple
inductor can be modelled as shown in Fig. 18(b). Thus, the
total MMF (NI) is equal to:
NI = φ(Rg + Rc)
(20)
where Rg and Rc are the reluctance of the air gap and the
core. With the reluctance method, the reluctance of the core
FIGURE 17. a) 3D geometry of an EE core. b) Top view of a pot core.
FIGURE 18. a) Illustration of a simple inductor. b) Magnetic circuit of the
inductor in a. c) B -H curve and relative permeability of core material N87
based on data sheet [31]. d) The curves of function f1 and f2 in (22) and
(23). The value of φ and Rc at the cross point is the solution for (20) at a
given NI.
can be expressed by:
NI
φ -Rg = Rc(μc)
(21)
There, the permeability of air μa is constant and does not
change with the flux density. However, the permeability of the
core depends on the H-field in the core, so that the reluctance
of the core Rc changes with the flux density. To calculate Rc,
the terms on both sides of (21) can be treated as two functions
of φ as given by:
f1(φ) = NI
φ -Rg = NI
φ -
lg
μaAg
(22)
f2(φ) = Rc(μc) =
lc
μcAc
= Hc(Bc)lc
BcAc

φ
(23)
where Hc(Bc) is the H-field through the core, which can be
obtained based on the B -H curves given by the material
data sheet, as for example shown in Fig. 18(c) (for N87).
VOLUME 6, 2025
1545

## [стр. 14]

MENG AND BIELA: ANALYTICAL MODELS FOR HF-LOSSES OF LITZ WIRE IN INDUCTORS WITH ARBITRARY WINDING
Variable lc and lg are the effective magnetic path and gap
length. Variable Ac and Ag are the effective cross-section area
of the core and the gap. As the flux φ through the core and
the air gap(s) is assumed to be identical, solving equation (21)
is equivalent to finding the crossing point of function f1(φ)
and f2(φ). Consequently, the curves for f1 and f2 v.s. flux
φ and the flux density in the core Bc = φ/S are plotted as
shown in Fig. 18(d). With the value Bc at the crossing point,
the H-field value through the core Hc can be determined based
on the B -H curve of the material (cf. Fig. 18(c)), and the
MMF contributed by the core (MMFc = Hclc) can then be
calculated.
REFERENCES
[1] A. V. D. Bossche and V. C. Valchev, Inductors and Transformers for
Power Electronics. Boca Raton, FL, USA: CRC Press, 2005.
[2] J. A. Ferreira, "Skin and proximity effect losses in transformer and
inductor windings," in Electromagnetic Modelling of Power Electronic
Converters. New York, NY, USA: Springer, 1989, pp. 83-85.
[3] J. A. Ferreira, "Analytical computation of AC resistance of round
and rectangular Litz wire windings," IEE Proc.-B, vol. 139, no. 1,
pp. 21-25, 1992.
[4] M. Bartoli, N. Noferi, A. Reatti, and M. K. Kazimierczuk, "Modeling Litz-wire winding losses in high-frequency power inductors," in
Proc. 27th Annu. IEEE Power Electron. Specialists Conf., 2020, vol. 2,
pp. 1690-1696.
[5] F. Tourkhani and P. Viarouge, "Accurate analytical model of winding
losses in round Litz wire windings," IEEE Trans. Magn., vol. 37, no. 1,
pp. 538-543, Jan. 2001.
[6] R. P. Wojda and M. K. Kazimierczuk, "Winding resistance of Litzwire and multi-strand inductors," IET Power Electron., vol. 5, no. 2,
pp. 257-268, 2012.
[7] C. R. Sullivan, "Computational efficient winding loss calculation with
multiple windings, arbitrary waveforms, and two-dimensional or threedimensional field geometry," IEEE Trans. Power Electron., vol. 16,
no. 1, pp. 142-150, Jan. 2001.
[8] H. Li, P. Yao, Z. Gao, and F. Wang, "Medium voltage converter inductor
insulation design considering grid requirements," IEEE Trans. Emerg.
Sel. Topics Power Electron., vol. 10, no. 2, pp. 2339-2350, Apr. 2022.
[9] P. Wallmeier, N. Frohleke, and H. Grotstollen, "Improved analytical
modeling of conductive losses in gapped high-frequency inductors," in
Proc. Conf. Rec. IEEE Ind. Appl. Conf. 33rd IAS Annu. Meeting, 1998,
pp. 913-920.
[10] M. Albach and H. Rossmanith, "The influence of air gap size and winding position on the proximity losses in high frequency transformers," in
Proc. IEEE 32nd Annu. Power Electron. Specialists Conf., 2001, vol. 3,
pp. 1485-1490.
[11] M. Albach, "Die verluste in luftspulen," in Induktivitäten in der Leistungselektronik Spulen, Trafos und Ihre Parasitären Eigenschaften.
Wiesbaden, Germany: Springer, 2017, pp. 71-141.
[12] W. A. Roshen, "High-frequency fringing fields loss in thick rectangular and round wire windings," IEEE Trans. Magn., vol. 44, no. 10,
pp. 2396-2401, Oct. 2008.
[13] W. A. Roshen, "Fringing field formulas and winding loss due to an air
gap," IEEE Trans. Magn., vol. 43, no. 8, pp. 3387-3394, Aug. 2007.
[14] T. Ewald and J. Biela, "Analytical winding loss and inductance models
for gapped inductors with Litz or solid wires," IEEE Trans. Power
Electron., vol. 37, no. 12, pp. 15127-15139, Dec. 2022.
[15] A. Stadler, R. Huber, T. Stolzke, and C. Gulden, "Analytical calculation
of copper losses in Litz-wire windings of gapped inductors," IEEE
Trans. Magn., vol. 50, no. 2, Feb. 2014, Art. no. 7001804.
[16] J. Schäfer, D. Bortis, and J. W. Kolar, "Novel highly efficient/compact
automotive PCB winding inductors based on the compensating air-gap
fringing field concept," IEEE Trans. Power Electron., vol. 35, no. 9,
pp. 9617-9631, Sep. 2020.
[17] S. Mukherjee, Y. Gao, and D. Maksimovi´c, "Reduction of AC winding
losses due to fringing-field effects in high-frequency inductors with
orthogonal air gaps," IEEE Trans. Power Electron., vol. 36, no. 1,
pp. 815-828, Jan. 2021.
[18] J. Hu and C. R. Sullivan, "Optimization of shapes for round-wire highfrequency gapped-inductor windings," in Proc. Conf. Rec. IEEE Ind.
Appl. Conf. 33rd IAS Annu. Meeting, 1998, vol. 2, pp. 907-912.
[19] J. Hu and C. R. Sullivan, "AC resistance of planar power inductors
and the quasidistributed gap technique," IEEE Trans. Power Electron.,
vol. 16, no. 4, pp. 558-567, Jul. 2001.
[20] J. Muhlethaler, J. W. Kolar, and A. Ecklebe, "Loss modeling of inductive components employed in power electronic systems," in Proc. 8th
Int. Conf. Power Electron., 2011, pp. 645-952.
[21] M. Jaritz, S. Blume, and J. Biela, "Design procedure of a 14.4 kV,
100 kHz transformer with a high isolation voltage (115 kV)," IEEE
Trans. Dielectrics Elect. Insul., vol. 24, no. 4, pp. 2094-2104, 2017.
[22] A. Khan, V. Ghorbanian, and D. Lowther, "Deep learning for magnetic field estimation," IEEE Trans. Magn., vol. 55, no. 6, Jun. 2019,
Art. no. 7202304.
[23] T. Guillod, P. Papamanolis, and J. W. Kolar, "Artificial neural network
(ANN) based fast and accurate inductor modeling and design," IEEE
Open J. Power Electron., vol. 1, pp. 284-299, 2020.
[24] H. Sun, M. Yang, Z. Lin, N. Wang, A. Sangwongwanich, and H. Wang,
"Small power Litz wire ferrite inductor loss model based on neural
network," in Proc. IEEE 4th China Int. Youth Conf. Elect. Eng., 2023,
pp. 1-6.
[25] M. Albach, "Two-dimensional calculation of winding losses in transformers," in Proc. IEEE 31st Annu. Power Electron. Specialists Conf.,
2000, vol. 3, pp. 1639-1644.
[26] Q. Meng and J. Biela, "Fast analytical loss model for Litz wire in
transformers with arbitrary winding arrangements," IEEE Trans. Power
Electron., vol. 40, no. 2, pp. 3302-3312, Feb. 2025.
[27] W. G. Hurley and W. H. Woelfle, Transformers and Inductors for Power
Electronics: Theroy, Design and Application. Hoboken, NJ, USA:
Wiley, 2013.
[28] Keysight, "Data sheet of e4990a impedance analyzer," 2022. Accessed:
May 20, 2025. [Online]. Available: https://www.keysight.com/ch/de/
assets/7018-04256/data-sheets/5991-3890.pdf
[29] M. Mu, Q. Li, D. J. Gilham, F. C. Lee, and K. D. T. Ngo, "New
core loss measurement method for high-frequency magnetic materials,"
IEEE Trans. Power Electron., vol. 29, no. 8, pp. 4374-4381, Aug. 2014.
[30] Magnetics, "2025 magnetics powder cores catalog," 2025. Accessed:
Jun. 12, 2025. [Online]. Available: https://www.mag-inc.com/Design/
Technical-Documents/Powder-Core-Documents.aspx
[31] TDK, "Data sheet of ferrite material N87," 2025. Accessed: May
20, 2025. [Online]. Available: https://www.tdk-electronics.tdk.com/
download/528882/71e02c7b9384de1331b3f625ce4b2123/pdf-n87.pdf
QINGCHAO MENG received the B.Sc. degree
in electrical engineering from Jilin University,
Changchun, China, in 2014, and the M.Sc. degree
in electrical engineering from Technical University
Berlin, Berlin, Germany, in 2024. In his master's
thesis, he worked on the winding loss calculation
and the FEM simulation for medium frequency
transformers. From 2017 to 2019, he was with
the Startup company enbreeze GmbH, Berlin. He
developed a measurement and remote monitoring
system for a small wind turbine of 15 kW. Since
2019, he has been with the Laboratory for High-Power Electronic System
with ETH Zurich, working on the loss modeling of litz wires.
JÜRGEN BIELA (Senior Member, IEEE) received
the Diploma (Hons.) from Friedrich-Alexander
Universität Erlangen-Nürnberg, Erlangen, Germany, in 1999, and the Ph.D. degree from the Swiss
Federal Institute of Technology (ETH) Zürich,
Zürich, Switzerland, in 2006. In 2000, he joined
Research Department, Siemens A&D, Erlangen. In
2002, he joined Power Electronic Systems Laboratory, ETH Zürich, as Ph.D. Student focusing on
electromagnetically integrated resonant converters.
From 2006 to 2010, he was a Postdoctoral Fellow
with Power Electronic Systems Laboratory. Since 2010, he has been an
Associate Professor. Since 2020, he has been a Full Professor of high-power
electronic systems with ETH Zürich.
1546
VOLUME 6, 2025
