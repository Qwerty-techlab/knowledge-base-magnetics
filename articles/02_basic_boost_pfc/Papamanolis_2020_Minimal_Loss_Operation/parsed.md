# untitled

> Автоматически извлечено из `source.pdf` скриптом `parse_pdf.py`
> Движок: pymupdf. Страниц: 20 из 20.
> Дата извлечения: 2026-08-07 06:43 UTC

Текст не редактировался. Формулы и таблицы могут быть искажены —
при сомнении сверяться с исходным PDF.

---

## [стр. 1]

© 2020 IEEE
IEEE Open Journal of Power Electronics, Vol. 1, pp. 469-487, November 2020
Minimum Loss Operation and Optimal Design of High-Frequency Inductors
for Defined Core and Litz Wire
P. Papamanolis,
T. Guillod,
F. Krismer,
J. W. Kolar
Personal use of this material is permitted. Permission from IEEE must be obtained for all other uses, in any current or
future media, including reprinting/republishing this material for advertising or promotional purposes, creating new collective
works, for resale or redistribution to servers or lists, or reuse of any copyrighted component of this work in other works.

## [стр. 2]

Received 17 August 2020; revised 14 September 2020; accepted 21 September 2020. Date of publication 29 September 2020;
date of current version 30 October 2020. The review of this article was arranged by Associate Editor Lijun Hang.
Digital Object Identifier 10.1109/OJPEL.2020.3027452
Minimum Loss Operation and Optimal Design
of High-Frequency Inductors for Defined Core
and Litz Wire
PANTELEIMON PAPAMANOLIS
(Student Member, IEEE), THOMAS GUILLOD
(Member, IEEE),
FLORIAN KRISMER
(Member, IEEE), AND JOHANN W. KOLAR
(Fellow, IEEE)
Power Electronic Systems Laboratory (PES) ETH Zurich, ETH Zurich Physikstrasse 3, 8092 Zurich, Switzerland
CORRESPONDING AUTHOR: PANTELEIMON PAPAMANOLIS (e-mail: papamanolis@lem.ee.ethz.ch)
ABSTRACT
This paper studies the loss-optimal design of a power inductor employed in a 2 kW, 400 V
input DC-DC converter. The design of an inductor is subject to a large number of design parameters and
the implications of the different design parameters on the losses are often not clearly traceable in a full
optimization, e.g., different current ripple amplitudes can lead to designs with similar losses, as larger ripple
amplitudes lead to increased AC core and winding losses but lower DC losses in the winding due to lower
inductance values and/or numbers of turns. In an effort to achieve a comprehensible description of the
implications of the key design parameters (switching frequency, fs, current ripple, r, number of turns, N)
on the losses, the remaining parameters, e.g., core (E55/28/21 N87) and type of conductor (litz wire), are
considered to be given. In a first step, the investigation is based on a simplified analytical model, which
is refined in a step-by-step manner, e.g., to consider core saturation. In a second step, the implications of
further critical aspects on the losses, e.g., temperatures of core and coil, are examined using a comprehensive
semi-numerical model. Surprisingly, the evaluation of the losses calculated in the fs-r domain reveals
that nearly minimum inductor losses are obtained for a current ripple that is inversely proportional to
the frequency, i.e., for a constant inductance, within a wide frequency range, from 200 kHz to 1 MHz.
Furthermore, the investigation reveals a decrease of the losses for increasing frequencies up to 375 kHz,
e.g., from 4.32 W at 80 kHz (r = 110 %) to 2.37 W at 375 kHz (r = 18 %). The detailed analysis related
to these results enables the compilation of a simple two-equation guide for the design of an inductor that
achieves close to minimum losses. In a next step, interesting trade-offs are identified based on a study of the
design space diversity, e.g., with respect to low cost and increased partial-load efficiency. The findings of this
work are experimentally verified, i.e., the losses of three different inductors are measured with an accurate
calorimetric method and at four different frequencies, ranging from 150 kHz to 700 kHz.
INDEX TERMS Inductor optimization, analytical model, calorimetric measurement, core losses, design
space diversity, ferrite, litz wire, minimum losses, performance factor, semi-numerical model, system design.
I. INTRODUCTION
Wide-bandgap semiconductors have lead to unprecedented
switching frequencies, fs, for power converters up to several
MHz, commonly using modulation strategies that allow for
soft transitions of the semiconductors (e.g., Triangular Current
Modulation, TCM) [1], [2]. This is motivated by the expected
increase in the power density on the system level, mainly due
to the decrease of the volume of the magnetic components
and/or the filtering requirements, e.g., with respect to the
EMI CISPR regulations. Literature confirms this trend [3],
nevertheless, only from a system-level perspective. Applicability of this expectation on the magnetic components directly
is not evident, and common misconceptions, according to
which magnetic components represent the bottleneck of the
complete systems, or that increasing frequency always leads
to smaller components, and/or that 50% of allowed relative
This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/
VOLUME 1, 2020
469

## [стр. 3]

PAPAMANOLIS ET AL.: MINIMUM LOSS OPERATION AND OPTIMAL DESIGN OF HIGH-FREQUENCY INDUCTORS
peak-to-peak current ripple, r, is approximately optimal, remain unanswered. Investigations on a system level are less
suitable to clarify the above, since designs with significantly
different design parameters can map to nearly same overall
performance values (e.g., efficiency, power density). This effect arises from different trade-offs and is referred to as design
space diversity [1]; by way of example, increased switching
frequencies may lead to smaller magnetic components but
larger cooling systems, due to increased switching losses.
Hence, individual component investigations are mandatory.
Such type of analysis has been previously conducted in
literature, but mostly with respect to the operation of mediumfrequency transformers. Specifically, using the Performance
Factor (PF = Btot fs), the optimal region of operation of a
transformer, with respect to the applied level and frequency
of the magnetic flux density is defined [4]-[7]. This is further
improved in [8], where the impact of the High-Frequency
(HF) copper losses is also considered. A more systematic and
detailed approach is presented in [9], [10]. However, these
considerations are not directly applicable to inductors, since
critical key design parameters differ. Specifically, inductor
designs feature an additional Low-Frequency (LF) core premagnetization component and also a different distribution of
the magnetic field inside the winding window, due to the
fringing-field caused by the air gap. The value of the inductance components of an inductor related to the stray field and
the field in the magnetic core is more critical compared to
transformers and, depending on the choice of fs and L, the
RMS value of the AC current component varies, whereas in
the case of the transformer it remains constant. Therefore,
individual analysis of power inductors is required.
Multiple references exist in literature solely focusing on
inductor optimization, divided into simple analytical models [11]-[14], semi-numerical and data-based models [15], the
most recent convex optimization geometric program formulation [16] and finite elements optimization [17], [18]. Nevertheless, all the above focus on the modeling and optimization procedures and not on understanding the actual optimal
operation of power inductors, which serves the main motivation behind this paper. Such knowledge is critical for the
evaluation of the validity of different optimization results, and
also for the parametrization of the optimization algorithms, in
order to become more computationally efficient, by accurately
focusing the main objectives and the investigated range of the
design space [19].
As the following considerations should allow to gain insight
into key parameter dependencies, the number of parameters
that take influence on the inductor losses are reduced to a minimum, cf. Fig. 1. Specifically, the magnetic core (N87 TDK -
E55/28/21) and the type of conductor (litz wire with single
strand diameter, dr, of 100 µm) are assumed as given. Moreover, the simple topology of a 2 kW DC-DC buck converter,
cf. Fig. 2(a) is considered, that is operated with constant input
and output voltages, and a sinusoidal instead of a triangular
shape of the AC current ripple, with the same peak value,
FIGURE 1. Compilation of typical degrees of freedom available in an
inductor design. This work focuses on the choice of two key parameters,
namely, switching frequency and current ripple, while ensuring an optimal
choice of the number of turns and the air gap length. Further design
parameters, e.g., magnetic core and type of conductor, are considered
given.
FIGURE 2. (a) Considered topology of a DC-DC buck converter;
(b) example of the considered sinusoidal waveform of the current ripple
instead of a triangular shape, for fs = 80 kHz switching frequency and
r = 110% relative peak-to-peak current ripple.
is assumed (cf. Fig. 2(b)), which typically results in a slight
overestimation of the core losses [20].
Moreover, the above considerations do not have an impact
on the generality of the findings, since similar magnetic excitations apply to typical AC-DC and DC-AC topologies,
i.e., triangular voltage-imposed flux density waveform, LF
current-imposed premagnetization. The implications of different core shapes on the core losses can be considered by
470
VOLUME 1, 2020

## [стр. 4]

a constant shape factor [21]. Finally, different ferrite materials exhibit similar loss characteristics, in different frequency
ranges, as shown in the performance factor graphs presented
in [22], [23].
With this, the paper can emphasize on the implications of
the remaining three design degrees of freedom, i.e.,
1) switching frequency, fs
2) relative peak-to-peak current ripple (or inductance),
r = 2IAC,pk
IDC
with IAC,pk =
Vo
4 fsL ,
(1)
3) number of turns, N,
on the losses. In Section II, the impact of critical nonlinearities, i.e., saturation of the magnetic core and varying
Steinmetz parameters for different magnetic flux waveform
characteristics (e.g., frequency, amplitude), is investigated using simple analytical equations. In addition, the optimal fs -r
operating area with regard to minimal inductor losses is inspected in detail, revealing a flat characteristic around the
minimum. In a second step, Section III proposes and evaluates
a detailed semi-numerical model in order to take the following
aspects, which have been omitted in Section II, into account.
r More accurate calculation of the copper AC resistance
(e.g., by detailed calculation of the magnetic field in the
core window);
r Impacts of fs, AC and DC flux densities, and core temperature on the core losses;
r Detailed thermal model;
r Placement of each turn in the coil (turn packaging).
Based on this, the initial findings from the analytical models
are confirmed. The results presented in Section III, which are
obtained for given core and single strand diameter, denote
the basis for further evaluation in Section IV, where different
design considerations are analyzed, i.e., distributed air gap,
different strand diameter of the litz wire, and different core
size. Section V presents a simple "two-equations" guide that
directly leads to quasi-optimal designs, and in Section VI the
design space diversity of inductors is investigated, which reveals potentially missed design opportunities, with respect to
quasi-optimal designs (i.e., up to +20% losses from the global
optima Pgl,opt, but at lower manufacturing cost and improved
partial load efficiency) [1], [9]. Finally, in Section VII, all
the above-mentioned findings are further confirmed through
experimental verification.
II. ANALYTICAL MODEL AND BASIC DESIGN PRINCIPLES
Table 1 lists the specifications of the considered DC-DC buck
converter, which have their origin in typical specifications of
commercial solar inverters; the output to input voltage ratio of 0.5 has been selected in order to consider maximum
current ripple. The considered ambient temperature, Tamb, at
60 ◦C corresponds to a commonly considered maximum case
temperature of a converter [24]. In addition, in Table 2, the
main geometrical and electrical parameters of the considered
inductor are presented. The N87 ferrite core material of TDKEPCOS is a commonly used low-cost material that features
TABLE 1. Main Specification
TABLE 2. Main Design Parameters
minimum losses for core temperatures between 80
◦C and
90 ◦C and achieves a high performance factor [22] in the considered operating range. The chosen E55/28/21 core allows
for a thermally valid operation in an wide range of fs and r.
For this model, a distributed air gap on the centered limb is
considered, since, for this special case, an analytical solution
exists for the magnetic field distribution inside the core window [25]. Finally, the selected litz wire with a single strand
diameter of dr = 100 µm is a good compromise between low
losses and cost in the investigated ranges of fs and r.
A. NONSATURABLE CORE, CONSTANT STEINMETZ
PARAMETERS
In a first step, the analysis neglects the presence of magnetic
flux density saturation, the frequency and flux density dependence of the Steinmetz parameters, and the influence of the
core DC premagnetization on the core losses. Even though
this approach is of limited accuracy, its results enable the
deduction of first conclusions with regard to suitable values
of fs, r, and N.
The inductor losses are split into copper and core losses.
The copper losses feature DC and AC components,
PCu,tot = RDCI2
DC
  
PCu,DC
+ c0RDC
I2
AC,pk
2



PCu,AC
, RDC = Nlavg
σkf Aw
N
,
(2)
VOLUME 1, 2020
471

## [стр. 5]

PAPAMANOLIS ET AL.: MINIMUM LOSS OPERATION AND OPTIMAL DESIGN OF HIGH-FREQUENCY INDUCTORS
where c0 considers skin and proximity effects [25],
c0 =
⎧
⎨
⎩
1 + 1
12

kfwwdr
δ2

2
∀dr < 3.17δ,
1
δ

dr
4 + 8(kfww)2
3dr

∀dr ≥3.17δ.
(3)
In (3), δ and ww denote the skin depth and the width of the
core window, respectively.
The magnetic flux density can be separated into a currentimposed DC component and a voltage-imposed AC component,
BDC = LIDC
NAc
,
BAC =
Vo
4 fsNAc
.
(4)
Since the implications of BDC on the core losses are neglected
in this Section, only BAC contributes to the core losses, which,
for sinusoidal waveforms, are calculated with the Steinmetz
Equation (SE) [27],
Pcore = VckSE f α
s Bβ
AC = VckSE f α-β
s
 Vo
4NAc
β
.
(5)
With (2) and (5) the total inductor losses are
Ptot = PCu,tot + Pcore = c1N2 + c2N-β
(6)
with
c1 = PCu,tot
N2
=

32 f 2
s I2
DCL2 + c0V 2
o

lavg
32σAwkf f 2s L2
,
(7)
c2 = Pcore
N-β = Vc f α-β
s
kSE
 Vo
4Ac
β
.
(8)
For dPtot/dN = 0, the optimal number of turns,
Nopt =
β
2
c2
c1

1
2+β
,
(9)
results, which enables the derivation of the optimum ratio
between core and copper losses, with respect to minimum
total losses, as often stated in literature [28], [29],
Pcore
PCu,tot

N=Nopt
= 2
β .
(10)
The minimum total losses for given inductance and switching
frequency are
Ptot,opt = Ptot(Nopt) = c3
c4 f 2
s L2 + 1
L2

β
2+β
f
2(α-2β)
2+β
s
,
(11)
with
c3 = (2 + β)
⎡
⎣

kSEV 2β
o Vc
2Aβ
c
2 
c0lavg
512Awkfσβ
β
⎤
⎦
1
2+β
, (12)
c4 = 32I2
DC
c0V 2o
.
(13)
According to (11) and for constant frequency, the total losses
for N = Nopt monotonically decrease for increasing inductance and, for L →∞,2 converge to
Ptot,opt( fs)

L→∞= Pconv( fs) = c3c
β
2+β
4
f
2(α-β)
2+β
s
.
(14)
The resulting non-zero value of Pconv( fs) is related to the
fact that both, copper losses and core losses, cannot approach
zero, since IDC and BAC are constant (independent of L -
assuming constant N) and greater than zero. In addition, the
copper losses increase for increasing N and the core losses
decrease for increasing N, cf. (2) and (5). Thus, for L →∞,
the optimal number of turns converges to a finite value greater
than zero, too, in order to maintain Pcore/PCu,tot = 2/β ≈
Pcore/PCu,DC,
lim
L→∞Nopt = Nconv = c5 f
α-β
2+β
s
,
(15)
c5 =
⎛
⎜⎝
2-1-2βσAwkfkSEβ

Vo
Ac

β
Vc
I2
DClavg
⎞
⎟⎠
1
2+β
.
(16)
In contrast, the value of Pconv( fs) monotonically decreases
for increasing frequency, given that α < β applies, and converges to zero for fs →∞, cf. (14). The reason for this result
can be explained based on the decrease of the voltage time
area due to the increase of fs, which enables a decrease of
the core losses. This, in turn, is accompanied by a decrease of
the copper losses in order to maintain Pcore/PCu,tot = 2/β. Accordingly, also Nopt approaches zero for fs →∞(to approach
zero copper losses).3
Fig. 3(a) depicts an fs-r contour plot of the total losses
(including losses due to skin and proximity effects) for the
parameters listed in Tab. 2 and an extended range of operating
points, i.e.,
50 kHz ≤fs ≤1 MHz and 1% ≤r ≤500%,
(17)
to obtain a more complete picture.4 Fig. 3(a) confirms the
findings described above:
1) For a given frequency, minimum total losses result for
L →∞(corresponding to r →0);
2) The value of Pconv( fs), i.e., the total losses for r →0,
decreases for increasing frequency.
B. SATURABLE CORE, CONSTANT STEINMETZ
PARAMETERS
For L approaching infinity and N approaching the finite value
Nconv, the current-imposed DC flux component approaches
infinity, cf. (4). This is not realistic, due to saturation of the
magnetic core. In the following, the magnetic flux density
2L →∞is theoretically evaluated by assuming infinite permeability of the
ferrite core and an air gap that approaches zero.
3For the analysis, a non-integer number of turns is allowed.
4The maximum ripple in a practical system with MOSFET semiconductors
may not exceed the value needed for quasi-lossless switching, i.e., approximately 200%.
472
VOLUME 1, 2020

## [стр. 6]

FIGURE 3. Contour plots of the total losses, for the fs-r-plane defined
with (17) and four distinct cases: (a) no saturation limit, constant
Steinmetz parameters; (b) saturation limit of 360 mT, constant Steinmetz
parameters; (c) and (d) saturation limit of 360 mT, operating-point
dependent Steinmetz parameters; (c) only considers the implications of
BAC and fs on kSE, α, and β; (d), in addition, takes the impact of BDC on the
Steinmetz parameters into account.
FIGURE 4. Investigation of the optimal ripple (or inductance), ropt (or Lopt),
for two different frequencies, i.e., (a) 20 kHz, and (b) 375 kHz. For both
frequencies, the cases of magnetic flux density going to infinity and
limited at 360 mT are depicted.
saturation limit of the considered ferrite core, Bsat, is set to
360 mT.
In order to get an understanding of the implications of the
magnetic flux density saturation limit on the optimal ripple
value, Fig. 4 presents the characteristics of the losses, the
optimal number of turns for given r and fs, and the flux densities with respect to ripple and for two different frequencies
of 20 kHz and 375 kHz.5 It can be observed that, due to
BDC + BAC ≤Bsat, a clear loss minimum, Pmin, results for a
given frequency, which appears at a ripple ropt that is slightly
less but close to rsat, i.e., the ripple where the theoretically calculated magnetic flux density is equal to the saturation magnetic flux density. Below this ripple there is a steep increase of
N, in order to limit the magnetic flux density. The difference
between ropt and rsat arises, because in this limited interval
the decrease of the AC copper losses, PCu,AC, for decreasing
r, together with the decrease of Pcore due to the increase of N,
outweigh the increase of the DC resistance, RDC. A theoretical
verification of the impact of PCu,AC on ropt has been conducted
by applying PCu,AC = 0 in (2), which yields
Ptot = Pmin ∀r ≥rsat
⇔
PCu,AC = 0.
(18)
Even though this result is mainly of theoretical value, it confirms that ropt < rsat can only result for PCu,AC > 0.,6 With
increasing frequency, the values of rsat and ropt decrease and,
in addition, ropt approaches rsat, e.g., at 375 kHz, ropt ≈rsat
applies.
The fs-r contour plot of the total losses that considers
the saturation limit is shown in Fig. 3(b). Four regions are
highlighted. Region 1⃝corresponds to thermally valid designs
that are not limited by saturation and can acquire their corresponding optimal number of turns. Region 2⃝corresponds to
designs that are limited by saturation. The trajectory of rsat,
which is approximately equal to the trajectory of ropt, delimits
the two regions. Regions 3⃝, 4⃝correspond to thermally invalid designs due to excessive AC copper/core losses and DC
copper losses, respectively.
No analytical solution has been found for ropt, however, an
analytical expression can be derived for rsat and, using (1),
for Lsat. Subsequently, Lopt ≈Lsat is considered, based on the
assumption that ropt is close to rsat. Starting with (4),
Btot = BDC + BAC = Bsat ⇒N = 4 fsLIDC + Vo
4 fsAcBsat
(19)
applies for N. Furthermore, N needs to be equal to Nopt, cf. (9),
in order to obtain minimum losses. The equation N = Nopt
can be solved with respect to L based on the assumption
that B2
DC ≫B2
AC applies,7 which is a valid assumption in the
5The frequency value of 20 kHz is considered only in this section for better
understanding of the analysis, nevertheless, it is a non-optimal frequency for
the considered core material and, thus, for the rest of the analysis is omitted.
6In addition, and in anticipation of the results discussed in Section III the
finding (18) will contribute to the reason why the loss optimum computed
with the detailed inductor model is rather flat within a relatively wide range
of r.
7By applying (4) to B2
DC ≫B2
AC, the inequality 16( fsLIDC)2 ≫V 2
o results. With this, and for the assumption of a negligible impact of highfrequency losses due to skin and proximity effects (c0 = 1), the expression
32( fsLIDC)2 + c0V 2
o , which appears in the course of the derivation of (20),
can be replaced by 32( fsLIDC)2.
VOLUME 1, 2020
473

## [стр. 7]

PAPAMANOLIS ET AL.: MINIMUM LOSS OPERATION AND OPTIMAL DESIGN OF HIGH-FREQUENCY INDUCTORS
FIGURE 5. Ratio of AC to DC copper losses with respect to switching
frequency and for L = Lsat ≈Lopt. The cases with and without consideration
of the AC proximity losses are depicted.
considered frequency range. With this,
Nopt ≈
⎛
⎜⎝
σAwkfkSEβ

Vo
Ac

β
Vc f α-β
s
21+2βI2
DClavg
⎞
⎟⎠
1
2+β
(20)
and
Lsat ≈c6 f
α-β
2+β
s
  
Lsat,a
-
Vo
4 fsIDC



Lsat,b
≈Lopt,
(21)
c6 =
A
2
2+β
c
Bsat

2-1-2βσAwkfkSEβV β
o Vc

1
2+β
I
4+β
2+β
DC l
1
2+β
avg
(22)
result.
Compared to the numerically derived value of Lsat, (21)
results in a maximum deviation of 0.64% at fs = 100 kHz
and converges to zero for increasing frequency. At higher
frequencies, the first term, Lsat,a, becomes dominant and, in
a double-logarithmic representation,
log(Lsat,a) = log(c6) + α -β
2 + β log( fs),
(23)
log(Lsat,a) is directly proportional to log( fs). By way of example, for the settings listed in Table 2 (α = 1.30, β = 2.59),
(α -β)/(2 + β) = -0.28 results, which, in terms of decibel,
corresponds to a change of Lsat,a( fs) by -5.6 dB/decade.
According to the findings related to (18), Lopt ≈Lsat is valid
if the AC copper losses have a negligible impact on the DC
losses, i.e., for a low ratio of AC to DC copper losses. At L =
Lsat, this ratio is obtained based on (2) and (20),
PCu,AC,sat ( fs)
PCu,DC,sat ( fs)100% ≈c0
32

Vo
fsLsatIDC
2
100%.
(24)
For the considered specifications, the result, marked with (i)
in Fig. 5, shows that the AC copper losses are less than 15% of
the DC copper losses within the complete range of considered
frequencies, and the calculated relative error between Pmin and
Ptot(rsat) is less than 1%. Nevertheless, even for the extreme
case previously considered of 20 kHz evaluation revealed that
FIGURE 6. Contour plot of the values of the Steinmetz parameters α, β
with respect to the amplitude and the frequency of the applied AC
magnetic flux density. The values are extracted using local Least Mean
Square (LMS) fitting of the Steinmetz Equation on measured loss-data at
80 and a DC premagnetization equal to 0 mT (cf. Section III). Additionally,
a trajectory is highlighted that corresponds to the optimal designs, Lopt, of
E55/28/21 core depicted in Fig. 3(c), Fig. 7.
the relative error between Pmin and Ptot(rsat) drops below 8%
already for an AC to DC copper ratio equal to 50%.
Finally, since the condition PCu,AC ≪PCu,DC at Lsat for
fs ∈[50 kHz, 1000 kHz] is validated, the optimal losses and
number of turns, that correspond to each Lopt - fs pair can be
directly calculated using (15) and (14), respectively. Comparison between the estimated ones through (15) and (14) and
the ones using a brute-force evaluation approach returns an
absolute maximum error below 1% that converges towards
zero with increasing frequency, for both values.
C. STEINMETZ PARAMETERS DEPENDENT ON fS AND BAC
Since the Steinmetz parameters are obtained from an exponential fitting to measured core losses of the employed
material, they are only valid within a limited range of operation. In order to increase the accuracy of the computed
core losses, the employed Steinmetz parameters need to be
adapted to the operating point, which, with regard to core
losses, is mainly characterized by the magnetic flux density
(frequency, amplitude of AC component, DC bias) and the
core temperature. Fig. 6(a), (b) depicts the values of α and
β with respect to fs and BAC for the N87 material, Tcore =
80 ◦C, and BDC = 0. The values are obtained with local Least
Mean Square (LMS) fittings of the Steinmetz Equation (SE)
to measured losses (cf. Section III). It can be seen that α < β
applies for most combinations of fs and BAC, except for high
frequencies, where the two parameters show approximately
equal values; for f > 350 kHz even α > β applies at some
474
VOLUME 1, 2020

## [стр. 8]

FIGURE 7. Loss-optimal designs over frequency using the analytical model
for three distinct cases, i.e., i. no AC proximity losses and constant
Steinmetz parameters, ii. with AC proximity losses and constant Steinmetz
parameters, iii. with AC proximity losses and Steinmetz parameters that
take into consideration the impact of AC magnetic flux density and
switching frequency for a constant temperature of 80◦C and BDC = 0 mT.
regions. The white regions in Fig. 6 correspond to regions
where the resulting loss density is outside the limits of interest,
i.e., 0.5 kW/m3 < pcore < 1000 kW/m3. It should be noted
that that these two maps change for different values of Tcore
and BDC.
Fig. 3(c) shows a contour plot of the losses that results
for (6) if the impact of the frequency and the AC magnetic
flux density on the Steinmetz parameters is considered. The
contour plot reveals a significantly flat region of low losses
between 200 kHz and 1000 kHz. Since the characteristic
properties of the losses along the minimum-loss trajectory
marked with Lopt are of particular interest, Fig. 7 presents
a direct comparison of Ptot, L, N, BDC, BAC, and Btot along
these trajectories in Fig. 3(b) and Fig. 3(c), i.e., for constant
and for operating-point dependent Steinmetz parameters (with
respect to fs, BAC). In addition, the minimum-loss trajectory
of Fig. 3(c) is also plotted in Fig. 6. According to Fig. 7, deviations between the results appear for fs > 200 kHz. There, the
minimum losses are nearly constant with respect to frequency
if the Steinmetz parameters are adapted to the operating-point.
A view on Fig. 6(a) reveals that the characteristic of α along
the optimal trajectory experiences a sharp rise from 1.6 to
2.2 (approaching the value of β) around 200 kHz, and, at
300 kHz, enters the region where α ≈β applies. With this,
Fig. 7 confirms the findings related to (14), (20), and (21),
that the minimum losses, the optimal inductance, and the optimal number of turns are independent of frequency given that
FIGURE 8. Comparison of the main performance characteristics of the two
trajectories Lopt and Lsat depicted in Fig. 3(d).
α = β applies. Moreover, the result confirms that the optimal
designs are all limited by saturation.
D. STEINMETZ PARAMETERS DEPENDENT ON fS, BAC, BDC
DC flux premagnetization has, potentially, a strong impact
on the core losses of commonly employed magnetic core
materials [30]. Fig. 3(d) depicts the contour plot of the core
losses for DC premagnetization being considered. Compared
to Fig. 3(c), an increase of the losses is observed in low-loss
regions, e.g., at fs = 500 kHz and r = 10%. Furthermore, for
given frequency, the minimum-loss trajectory, ropt, yields a
higher ripple than the trajectory rsat. In order to investigate
the reason for this result, Fig. 8 details the characteristics
of losses, inductance, and flux densities along the two trajectories, which reveals a substantial decrease of BDC, from
approximately 300 -350 mT at L = Lsat to 150 mT at L =
Lopt. Furthermore, the losses increase only slightly when L increases from Lopt to Lsat, with a maximum deviation of 23.4%
at 1 MHz and an average deviation of 12.6%. Accordingly,
also the core losses and the total copper losses remain approximately similar, in order to maintain a loss ratio of 2 over β.
Since the AC copper losses even increase for increasing ripple
(the ratio PCu,AC/PCu,DC reaches values between 20% and
30%, as shown with curve (iii) in Fig. 5), the loss reduction
achieved by decreasing the inductance from Lsat to Lopt only
stems from the reduction of the DC premagnetization, BDC,
that enables a reduction of the core losses.
E. MAIN OBSERVATIONS AND THE THREE QUASI-OPTIMAL
RANGES
According to the above findings, optimal inductor designs feature a monotonically decreasing current ripple amplitude with
increasing frequency that leads to an approximately constant
inductance value. Moreover, designs with peak flux densities
near saturation feature losses that are close to the optimum
VOLUME 1, 2020
475

## [стр. 9]

PAPAMANOLIS ET AL.: MINIMUM LOSS OPERATION AND OPTIMAL DESIGN OF HIGH-FREQUENCY INDUCTORS
FIGURE 9. Relative deviation from the optimal number of turns as a
function of β. The gray area denotes the range of N that leads to an
increase of the total losses of less than 20%.
(for given frequency). The total losses decrease for increasing
frequency, reaching a global loss minimum approximately at
the point where the Steinmetz parameters α and β are equal.
Around this point the total losses are relatively flat, with respect to all three design degrees of freedom: N, r, and fs. In
this regard, a range can be defined for each of the three degrees
of freedom in order to identify inductor designs that feature
almost minimum losses.
1) FLAT RANGE A - NUMBER OF TURNS
In case of flat range A, the ripple and the switching frequency
are kept constant, and N is changed, starting from the optimal
value, Nopt. The derivation starts with the total losses (6),
which can be expressed as a function of the optimal number
of turns (9), and while assuming already a loss ratio of 2
over β,
Ptot(N)
Ptot,opt
=
2
2 + β

β
2
 N
Nopt
2
+
 N
Nopt
-β
.
(25)
Expression (25) enables the calculation of N for a defined
acceptable increase of the total inductor losses (with respect
to the minimum inductor losses). However, no closed form
solution is found and (25) needs to be solved numerically,
instead. Fig. 9 presents the boundaries of flat range A for an
accepted loss increase of 20%, i.e., Ptot(N)/Ptot(Nopt) = 1.2,
and 2 < β < 3. The region enclosing the applicable range of
N, Nq,opt,min < N < Nq,opt,max, is split into the two regions 1⃝
and 2⃝. Region 1⃝results in better performance at partial load
and region 2⃝results in better performance in case of overload
operation. This will be further discussed in Section VI, where
the design space diversity of the inductor is investigated. The
depicted boundaries can be approximated by means of LMS
fitting,
Nq,opt,min ≈(0.6343 + 0.0505β) Nopt,
(26)
Nq,opt,max ≈(1.4835 -0.0610β) Nopt
(27)
(the error between numerical and approximated results is less
than 0.2% for 2 < β < 3). Please note that (26) and (27) are
of universal character, i.e., not limited to the settings listed in
Tables 1 and 2.
2) FLAT RANGE B - RIPPLE
This flat range considers changing ripple, constant frequency,
and optimal number of turns (at each individual operating
point); the corresponding trajectories are vertical lines in the
contour plots shown in Fig. 3. Fig. 4 illustrates respective
examples for f = 20 kHz and f = 375 kHz and, in case of
f = 375 kHz, reveals low total losses, close to the respective
minima, within a relatively wide range of r. In addition, the
impact of the DC bias on the core losses increases this range
towards higher ripple values, due to the decreasing core losses,
which provides a certain compensation of the increasing AC
copper losses, cf. Section II-D.
3) FLAT RANGE C - ALONG Lopt TRAJECTORY
The last flat range is along the trajectory of optimal inductance, Lopt, highlighted in Fig. 3, and depends entirely on the
relationship between α and β. For ferrite N87, this trajectory
can be split into the two ranges listed below, cf. Fig. 8.
r 50 kHz < fs < 150 kHz: α ∈[1.3, 1.6], β ∈[2.6, 2.7];
with (14), Ptot,opt ∝f -0.60
s
. . . f -0.43
s
≈1/√fs results;
r 250 kHz < fs < 850 kHz:
α ≈β ≈2
applies,
i.e.,
with (14), Ptot,opt remains approximately constant.
The second range corresponds to flat range C and is an
unchanged optimal design, since the inductance value and the
number of turns remain approximately constant as well.
III. SEMI-NUMERICAL ANALYSIS
This Section revisits the analysis of Section II, using a detailed
semi-numerical model in order to clarify that the drawn conclusions remain true if previously disregarded effects, in particular due to elevated temperatures of core and coil, are taken
into consideration. For this, the analyzed range is slightly
modified to the more practical range
40 kHz ≤fs ≤1 MHz and 2% ≤r ≤200%.
(28)
The employed ElectroMagnetic-Thermal (EMT) coupled inductor model is entirely implemented in MATLAB [31] and
provides the capabilities listed below.
r Core losses are calculated with the improved General
Steinmetz Equation (iGSE) [32]. The Steinmetz parameters are extracted by means of interpolation, using premeasured loss values, that take the implications of AC
magnetic flux density, frequency, core temperature, and
DC premagnetization into consideration [33]. The losses
of the employed core material, N87, have been measured
using the method proposed in [34].
r AC copper losses in the HF litz wire are determined
according to [35] with the magnetic field in the core
window being computed with the mirroring method [15].
r The thermal model, which is based on [28] and extended
according to [33], considers the heat dissipation mechanisms of conduction, convection, and radiation in order
to compute the surface temperatures of coil and core and
the hot-spot temperature inside the coil.
The EMT model implements an iterative procedure to take
the implications of elevated temperatures on core and copper
losses into account, i.e., the losses and the temperatures are
computed in a subsequent manner until both, losses and temperatures, reach convergence. The employed EMT modeling
476
VOLUME 1, 2020

## [стр. 10]

FIGURE 10. Air-gap length, flux density, and losses for different numbers of turns and two selected operating points: (a) fs = 80 kHz, r = 110%,
(b) fs = 375 kHz, r = 18%. Local minima, Pmin, and flat ranges A (cf. II-E1) are marked for both cases. The dashed trajectory denoted as trend corresponds
to application of (25).
approach has been experimentally verified in several converter
designs, e.g., [36], [37].
For the analysis, and unless otherwise specified, the following considerations apply:
1) The cooling of the component is entirely based on natural convection and no forced air-flow is considered.
2) The core has a single air gap per core limb (instead of
the distributed air gap assumed in Section II to simplify
the analysis), since this denotes a more common type of
realization.
A. OPTIMIZATION WITH RESPECT TO N
For each operating point characterized with fs and r, the
number of turns is optimized with respect to the losses and,
under the assumption of a constant fill factor, this is expected
to lead to an approximately equal share between the core and
copper losses. Fig. 10 reveals air-gap lengths, flux densities,
and losses with respect to N for the two selected operating
points fs = 80 kHz, r = 110% and fs = 375 kHz, r = 18%
(the global loss minimum); these two operating points serve
as basis for the further analysis and are referred to with OP1
and OP2, respectively.
The designs are limited by saturation in case of low N and
by impractically large air gap values at high N, whereas the
maximum air-gap lengths are limited to 30% of the height of
the core window. Due to the varying fill factor, which results
from the packaging of the turns, local optima exist.
Despite the varying fill factor, the applicability of (25) and
(26), (27) is also confirmed by direct comparison with the
peaks of the bars. Specifically, using i. for the case of 80 kHz
a β of 2.63,8, Nopt equal to 22 and Ptot,opt equal to 4.32 W, and
ii. for the case of 375 kHz a β of 2.28,9 Nopt equal to 18 and
Ptot,opt equal to 2.37 W the analytical solutions of flat range A
are denoted as trend. The analytically derived margins of the
quasi optimal operation using (26), (27) are [16.9, 29.1] and
[13.5, 24.2] turns, respectively. Finally, the ratio between the
core and copper losses varies around the theoretical 2/β from
0.2 to 2.2. Direct comparison between the two optimizations
depicted in Fig. 10(a),(b) confirms the initial conclusion, that
at higher frequency and lower ripple, the total losses decrease
substantially.
B. OPTIMIZATION WITH RESPECT TO fS AND r
Applying the presented local optimization with respect to the
number of turns to all the points of (28), the contour plots
of Fig. 11 result. Starting from Fig. 11(a) the total losses of
each operating point of the optimization are presented. This
contour is the equivalent of the analytically calculated result
presented in Fig. 3(d). Even though, a direct comparison of
the two contour plots reveals a similar trend with respect
to loss-minimal operation, also significant deviations of the
absolute losses can be observed. The main reasons for this
difference are, the lower achieved fill factor, the more accurate
estimation of the magnetic field inside the winding window,
using the mirroring method, and the impact of the temperature on the core losses. Introduced noise, mainly apparent
8The value corresponds to a core temperature of 89◦C AC magnetic flux
density peak value of 80.2 mT and a DC premagnetization of 146 mT.
9The value corresponds to a core temperature of 77◦C AC magnetic flux
density peak value of 20.9 mT and a DC premagnetization of 233 mT.
VOLUME 1, 2020
477

## [стр. 11]

PAPAMANOLIS ET AL.: MINIMUM LOSS OPERATION AND OPTIMAL DESIGN OF HIGH-FREQUENCY INDUCTORS
FIGURE 11. Contour plot of (a) total losses, (b) core losses, and (c) total copper losses, for the fs -r-plane defined in (28). In (a), two trajectories are
highlighted: ropt, which corresponds to the minimum losses for changing frequency, and r375, which corresponds to a changing ripple, a constant
frequency of 375 kHz, and an optimum number of turns. The global optimum, Pgl,opt = 2.4 W, occurs at fs = 375 kHz, r = 18% and is marked with a red
star.
in Fig. 11(b), (c), results from the turn's packaging and the
measured core loss data.
Fig. 11 also presents the global optimum, Pgl,opt = 2.4 W,
which corresponds to OP2, and two critical trajectories, i.e.,
the trajectory of minimum losses for changing frequencies,
marked with ropt, and the trajectory of changing ripple, constant frequency ( f = 375 kHz), and optimal N, marked with
r375.
In the course of a closer inspection of Fig. 11(a), four
characteristic regions are identified.
r Region 1⃝is delimited by two dashed white lines, which
illustrate the frequency-dependent changes of the two
boundaries of the flat range B for a maximum increase
of the losses by 20% [for a given frequency and with
respect to the losses at ropt( fs)]. The designs within this
region are most suitable for realization.
r Region
2⃝corresponds to suboptimal designs, which
are thermally valid, nevertheless, generate unnecessarily
high losses.
r Regions 3⃝and 4⃝include invalid designs that will heat
above the defined thermal limit, i.e., all temperatures
must remain less than 125◦C. Region
3⃝is limited by
AC (copper and core) losses and region 4⃝by DC copper
losses, cf. Figs. 11(b), (c).
Fig. 12 presents the contours of the corresponding hot-spot
temperature inside the coil, Ths, the peak magnetic flux density, and the optimal number of turns, respectively. The hotspot temperature follows a trend that is identical to the trend
of the total losses shown in Fig. 11(a) and remains less than
100 ◦C for f > 100 kHz and an assumed ambient temperature
of 60 ◦C. According to Fig. 12(b), designs with peak flux
densities ranging from 140 mT to 360 mT can result in optimal
operation. This confirms the finding that, for increasing ripple,
the decrease of the DC flux bias leads to a decrease of the
core losses, which can compensate the increase of the AC
copper losses within flat range B. Fig. 12(c) highlights the
fact that with increasing frequency and/or ripple the optimal
number of turns decreases in order to lower the impact of the
AC copper losses on the total losses. In case of low ripple
values, the designs are limited by saturation, leading to a steep
increase of the optimal number of turns for decreasing ripple.
Finally, Fig. 12(c) also highlights the realized inductors and
the operating points for experimental verification presented in
Section VII.
C. INVESTIGATION OF ropt
Fig. 13 presents the losses and the inductors' characteristic
values (L, N, B, and Jrms) along the ropt( fs) trajectory. The
region of low losses, close to the global minimum of 2.4 W, is
very flat and starts at 200 kHz. Based on this, operation above
200 kHz to 300 kHz may not provide us with additional benefits on a system level, since the remaining converter losses,
e.g., switching losses of semiconductors, will keep increasing.
The graphs of Lopt and B in Fig. 13 confirm the finding
of the analysis of Section II that, with respect to decreasing
ripple, the flat range B extends to saturation limited designs.
Fig. 14 presents a comparison of the optimal designs to the
designs limited by saturation with respect to frequency and
Fig. 15(a) depicts the corresponding Steinmetz parameters
for the saturation limited designs, which confirm monotonically decreasing losses in case of α < β and constant losses
for α ≈β.
Close inspection of the flat region C at frequencies above
the frequency featuring the global minimum reveals constant
values of Nopt, Lopt, and AC copper losses and slowly increasing core losses. From (5), an increase of the core losses with
increasing fs is expected, since α > β applies in this region,
cf. Fig. 15(a). With regard to the analysis of the AC copper
losses, the factors Fr and Gr, used to compute the implications
of skin and proximity effects in round wires [35], first need to
be investigated. Fig. 16 depicts Fr( fs) and Gr( fs) and reveals
that, for dr = 100 µm, the losses due to skin effect, PCu,skin, are
negligible in the considered frequency range (Fr ≈0.5) and
Gr is proportional to f 2
s . In addition, the AC magnetic field
inside the winding window is proportional to IAC,pk, which for
constant L is inversely proportional to fs, cf. (1). Based on the
assumption that the proximity losses dominate the AC copper
478
VOLUME 1, 2020

## [стр. 12]

FIGURE 12. Contour plots of (a) hot-spot temperature inside the coil,
(b) peak magnetic flux density, and (c) optimal number of turns. The
presented values are used to compute the losses in Fig. 11.
losses (at 375 kHz the ratio between AC to DC resistance is
equal to 20.4),
PCu,AC ≈RDC Gr

∝f 2
H2
AC,pk
  
∝f -2
= const.
(29)
applies, which explains the constant AC copper losses at high
frequencies observed in Fig. 13.
The ratio between the copper and core losses fluctuates
around the theoretical optimal of 2/β, for fs > 50 kHz. This
is attributed to small fluctuations of the fill factor and the
integer number of turns. However, according to Fig. 13, 2/β
does not apply for 40 kHz < fs < 50 kHz and the optimal
ratio of copper to core losses is found to be approximately
1/β, instead. This result is linked to the copper fill factor,
kf, that results for technically possible arrangements of the
conductors inside the core window for different values of N.
Fig. 17 illustrates optimal fittings of litz wire with round cross
section and for N ranging from 21 to 36 (due to half-plane
symmetry only half of the E-core is shown and, in addition,
FIGURE 13. Losses and characteristic values of the corresponding inductor
designs along the trajectory ropt shown in Fig. 11(a). The result reveals the
flat range C, which starts at 200 kHz. The gray regions shown in the graphs
of Lopt and B denote suboptimal designs according to flat range B that
feature an increase of the total losses by less than 20%.
the area occupied by the coilformer is highlighted). It can be
observed that kf ranges from 16.6% to 24.5%.
At higher frequencies, the optimal number of turns is close
to 20 and the fill factor is approximately constant. However,
at lower frequencies, Nopt increases and the inductor design
enters the region of Fig. 17(c), where the wire diameter, dwire,
is constant (and comparably small, in order to accommodate
three layers of conductors in the core window). Thus, kf is
proportional to N,
kf = NAwire
Aw
,
(30)
where Awire is the copper cross-section area of the conductor.
With this,
RDC =
Nlavg
σkfAwire
(31)
results, which gives total losses of
Ptot = c7N + c2N-β,
(32)
c7 =

32 f 2
s I2
DCL2 + c0V 2
o

lavg
32σAwire f 2s L2
,
(33)
VOLUME 1, 2020
479

## [стр. 13]

PAPAMANOLIS ET AL.: MINIMUM LOSS OPERATION AND OPTIMAL DESIGN OF HIGH-FREQUENCY INDUCTORS
FIGURE 14. Comparison of the designs along the ropt trajectory to the
designs that are marginally limited by saturation in Fig. 11(a).
FIGURE 15. Steinmetz parameters α and β and core losses density, pcore,
that correspond to the optimal designs along the ropt trajectory of (a) the
E55/28/21 core of Fig. 11(a) and (b) the E47/20/16 core of Fig. 19(c).
and, at the optimal number of turns, leads to a ratio of core to
copper losses of
Pcore
PCu,tot

N=Nopt
= 1
β .
(34)
D. TRAJECTORY OF CONSTANT FREQUENCY, r375
Fig. 18 presents the losses and the inductor properties along
the trajectory marked with r375 in Fig. 11(a), i.e., for a
constant frequency of f = 375 kHz. Compared to the losses
computed with the analytical model in Section II and presented in Fig. 4(b), substantial differences between the absolute values of the losses are observed that mainly arise from
the operating-point dependent Steinmetz parameters. Yet, the
trends and the absolute values of the ripple are almost identical
and two main findings of the previous Section can be verified.
Firstly, the total losses decrease for increasing L (decreasing
r) and L ≤Lsat ≈Lopt. This is attributed to the AC copper
losses, where the decrease of IAC,pk (and hence the HAC,pk)
dominates the minor increase of the optimal number of turns,
i.e., Nopt, which remain constant for 18% < r < 34% and
FIGURE 16. The factors for modeling AC losses due to proximity and skin
effects, Gr and Fr, plotted against frequency and for two different single
strand diameters of a litz wire, dr = 100 µm and dr = 300 µm.
FIGURE 17. Turn packaging for an E55/28/21 core with coil former and
round conductors, for N ∈[21, 36].
decrease only slightly for 34% < r < 50% (the value of Gr
remains constant, due to consideration of constant frequency).
Secondly, in accordance to the findings of Section II-E2, the
value of BDC increases for increasing L (decreasing r) and,
with this, also the core losses slightly increase, which compensates the increase of the AC copper losses within flat range B,
11% < r < 46%.
E. MAIN FINDINGS
With the proposed semi-numerical model, the main findings
of Section II, namely optimal region of operation and main
design trends, are confirmed, despite the different levels of
detail of the employed models. The main difference lies in
the absolute value of the total losses, which could lead to a
thermally invalid design, if only the analytical approach is
considered. In Section V, a direct comparison between the two
models is conducted and the obtained result further confirms
the above findings.
IV. VALIDATION WITH FURTHER DESIGNS
In order to confirm the generality of the above findings, three
different cases, for same specifications of Table 1, are investigated with the EMT inductor model used in Section III:
480
VOLUME 1, 2020

## [стр. 14]

FIGURE 18. Detailed investigation of the losses and inductor properties
determined with the EMT inductor model along the trajectory of varying
ripple and constant frequency of fs = 375 kHz, r375, in Fig. 11(a). Flat
range B, 11% < r < 46%, is highlighted.
1) Distributed air gap;
2) Litz wire strand diameter of 300 µm
3) Core E47/20/16 (smaller than E55/28/21).
A. DISTRIBUTED AIR GAP
For the analysis of the distributed air gap, seven symmetrically
distributed air gaps at the center core-limb are considered. The
contour plot of the total losses is depicted in Fig. 19(a). The
basic observations are the following:
r The impact of the distributed air gap on the global loss
minimum, the vicinity of the loss-optimal region, and the
optimal frequency is relatively low; specifically, Pgl,opt
decreases from 2.4 W to 2.2 W and fs changes from
375 kHz to 350 kHz.
r Compared to Fig. 11(a), the flat range B is wider, e.g.,
in comparison to the example analyzed in Section III-D,
cf. Fig. 18, 10% < r < 64% applies at fs = 375 kHz,
which is due to reduced HF AC copper losses arising
from the proximity effect. Accordingly, ropt increases
from 20% to 28% and the upper boundary of region
2⃝of Fig. 11(a), i.e., a thermal limit of the inductor, is
shifted towards higher ripple value.
On an inductor component level, the additional complexity
resulting from the manufacturing of a core with distributed air
gap is unfounded. Nevertheless, on a system level, increased
ripple leads to less hard-switching semiconductor losses and,
thus, can be beneficial. However, this conclusion may not be
valid in case of solid or foil conductors.
B. LITZ WIRE STRAND DIAMETER 300 µm
In case the litz wire strand diameter is increased, the absolute
value of the losses increases. Interestingly, also the global
optimum moves to higher frequencies (cf. Fig. 19(b)). This
is mainly related to the value of Gr, depicted in Fig. 16. For
a copper wire with a diameter of 300 µm and frequencies
greater than 500 kHz, Gr is proportional to √fs. As a result, (29) is not constant and the AC copper losses decrease
for increasing frequency (the increase of Fr is of minor importance). Hence, the global optimum does not entirely depend on
the core losses; in case of dr = 300 µm, it is shifted to 1MHz,
however, the minimum losses are found to be almost constant
for 300 kHz < fs < 1MHz (below 10% deviation). Finally,
the upper boundary of region
2⃝in Fig. 11(a) is shifted towards lower ripple values, due to poor HF performance and
related thermal limitations.
C. CORE E47/20/16
The last case analyzed is the next smaller E-core of the series
of TDK-EPCOS, E47/20/16, cf. Fig. 19(c). For this analysis,
forced cooling of 4m/s air-speed is considered, since consideration of natural convection would significantly limit the
valid operating area. With this air-speed and for given losses,
the core temperatures are similar to the previously calculated
temperatures for the E55/28/21 core.
Compared to Fig. 11(a), three characteristic differences are
observed:
r Due to the smaller cross-sectional areas of core window
and core, the current and flux densities increase, leading to increased losses, e.g., Pgl,opt rises from 2.4 W to
3.51 W.
r The loss minimum is shifted towards higher ripple values, because the reduced volume leads to a decrease of
the component's energy storage capability, rendering a
lower inductance more suitable or, with regard to saturation, necessary.
r The optimal frequency is shifted to a higher value of
650 kHz. This is directly related to the increased optimal ripple, which leads to an increase of BAC,pk and, in
turn, extends the frequency range where α < β applies
towards higher frequencies, cf. Fig. 15(b).
V. FAST DESIGN GUIDE
According to Section III, the results of the detailed models
confirm the results of the analytical model. The main difference are different absolute values of copper and core losses.
Thus, a guide using analytical equations is proposed.
For a given frequency, the inductor is close to the optimal
design for the following settings:
r L* is chosen according to (21), in order to set the maximum magnetic flux density to the saturation magnetic
VOLUME 1, 2020
481

## [стр. 15]

PAPAMANOLIS ET AL.: MINIMUM LOSS OPERATION AND OPTIMAL DESIGN OF HIGH-FREQUENCY INDUCTORS
FIGURE 19. Contour plot of the total losses for three selected cases: (a) distributed air gap, (b) litz wire strand diameter of 300 µm, and (c) core
E47/20/16. In each plot, the trajectory of ropt(fs) and the global optima, Pgl,opt, are highlighted.
FIGURE 20. Comparison of losses and inductor properties for optimal
designs, determined with a grid-search approach, and designs derived
using the proposed "two-equation" guide. All designs are evaluated with
the semi-numerical model.
flux density;
L* = c6 f
α-β
2+β
s
-
Vo
4 fsIDC
,
(35)
r N* is chosen according to (9), in order to achieve a ratio
of core to copper losses of 2/β;
N* =
β
2
c2
c1

1
2+β
.
(36)
Fig. 20 presents a comparison of the designs obtained with
this design guide, evaluated using the EMT inductor model,
and the optimal designs that result from the EMT inductor
model detailed in Fig. 13. Even though, the two approaches
return different inductance values, similar losses result for
frequencies up to 500 kHz, which is related to the flat characteristic of the loss minimum. Between 40 kHz and 375 kHz,
the maximum deviation between the two approaches is equal
to 17.8% and occurs at 120 kHz.
If the operating frequency is not known in advance, the PF
can be used to identify the optimal frequency range of the
inductor with respect to minimum losses. The PF is defined
for a given constant core loss density, pcore = Pcore/Vc,
PF = BAC fs.
(37)
The consideration of the classical PF, instead of modified versions that consider HF AC losses, is based on the assumption
that losses due to the proximity effect are low at the global
optimum. Hence, the copper losses are constant with respect
to frequency and the CUT performance depends entirely on
the performance of the core.
In combination with (5),
BAC = c7
f
α
β
s
,
c7 =
 pcore
kSE
 1
β
⇒
PF ∝f
β-α
β
s
(38)
results, i.e., the PF increases for increasing frequency if α <
β applies (and α is approximately constant). Furthermore, the
PF peaks approximately at the frequency where α starts to
rise significantly, which is close to the frequency where α = β
applies. The PF data of N87 ferrite material for four different
loss densities, ranging from 50 mW/cm3 to 300 mW/cm3, is
depicted in Fig. 21. For pcore = 50 mW/cm3, the PF peaks at
285 kHz, which is close to optimal frequency calculated for in
Section III for the inductor realized with the E55/28/21 core
(there, pcore ≈30 mW/cm3 applies), even though, the impact
of the DC bias on the PF is not considered. For increased loss
density, PF peaks at a higher frequency, which confirms the
shift of Pgl,opt of E47/20/16 to a higher frequency.
Please note that the proposed guide does not ensure thermal
validity, which needs to be verified in a final step.
VI. DESIGN SPACE DIVERSITY
According to the results of the previous Sections, the total
losses are close to the minimum within relatively wide ranges
of N, r, and fs, cf. Section II-E. In order to narrow the space
482
VOLUME 1, 2020

## [стр. 16]

FIGURE 21. Performance Factor (PF) of N87 ferrite material for four
different loss densities, i.e., 50 mW/cm3, 100 mW/cm3, 200 mW/cm3,
300 mW/cm3. The peak value of the PF for each value is highlighted.
of suitable designs, further criteria can be taken into account,
e.g., partial-load efficiency and cost.
Fig. 22 depicts the design space diversity plot, i.e., the characteristic values of all possible designs, for the design settings
of Table 2 and total losses of less than 1.2 × Popt,gl, by taking
all three design degrees of freedom into account ( fs, r, and
N). Each y-axis represents the value of an individual variable
and, depending on the background color, they are assigned to
one of the three groups listed below.
1) Input design variables (light gray)
2) Internally computed variables (gray)
3) Main objectives (dark gray)
The newly defined main objectives are the relative component cost of the inductor, computed with respect to the
minimum cost, and the inductor's efficiencies η20%, η50%, and
η100%, which result if the buck converter is operated with an
output power of 20%, 50%, and 100% of the rated power,
respectively. The cost is calculated according to [38], which
corresponds to a minimum order quantity of 15'000 pieces.
The result presented in Fig. 22 reveals that wide ranges
of fs, r, and N lead to almost minimum losses under full
load conditions, however, with respect to cost and partial-load
efficiencies, significant performance differences are observed.
In order to further investigate this, the multi-objective optimization problem is solved in a grid-search approach by
minimizing a cost function,
fcost,obj,i = w1
P100%,i
max(P100%) + w2
P50%,i
max(P50%)+
+ w3
P20%,i
max(P20%) + w4
costi
max(cost),
∀i ∈N ∨i ≤n,
(39)
where i refers to a dedicated design of the calculated design
space (which itself comprises of n results),
w = [w1, w2, w3, w4]
(40)
denotes the user-defined optimization weights, and the four
objectives are the total losses at full load (P100%,norm), 50%
load (P50%„norm) and 20% load (P20%„norm) and the cost per
component.
Four different scenarios are investigated:
r Scenario 1: w = [1.0, 0.0, 0.0, 0.0], i.e., minimum
losses at full load.
r Scenario 2: w = [0.247, 0.593, 0.16, 0.0]; this is
based on the weighted European efficiency for solar inverters [26],
ηEu = 0.03 η5% + 0.06 η10% + 0.13 η20%
+ 0.10 η30% + 0.48 η50% + 0.20 η100%.
(41)
r Scenario 3: w = [0.0, 0.2, 0.2, 0.6], i.e., low cost
(higher priority) and low partial load losses (lower priority).
r Scenario 4: Worst case performance with respect to the
additional main objectives (based on programmed logic
script).
The first scenario shows that exclusive optimization for
high efficiency at full load leads to missed opportunities,
since both, partial load efficiency and cost, can be improved.
Furthermore, with reference to the weights of (41), full load
efficiency is of limited importance.
The second scenario follows the efficiency distribution
of (41) and achieves a substantial improvement of the partial
load efficiencies at the expense of a relatively low increase
of the losses at full load, from 2.4 W to 2.72 W. This result
is achieved with an increased number of turns and the design
enters region
1⃝in Fig. 9. Thus, the ratio of core to copper
losses is less than 2/β for operation under full load. This
ratio increases for decreasing output power, due to constant
core losses and decreasing copper losses, which explains the
improved partial-load efficiencies, cf. Section II-E1. Furthermore, a decreased cost results, which is unexpected, since
scenario two does not take cost into consideration. This particular result is related to the fact that copper is an important
cost driver and the coincidence that, in the presented case, the
increased number of turns leads to a reduced fill factor and,
thus, reduced copper mass. Due to this, a very similar result is
obtained for the third scenario, i.e., increased number of turns,
N > Nopt, to improve partial-load efficiency and decreased fill
factor to lower the cost.
The fourth scenario demonstrates the missed opportunities
of a bad design, even though, it features approximately similar
frequency and losses as the design of scenario 2.
Based on the results of scenarios 2, 3 and in order to achieve
improved partial-load efficiency and acceptable full-load efficiency, the design guide of Section V is used for the optimal
frequency of 375 kHz and for the parameters of Table 2,
nevertheless, this time N is optimized for a partial load of 50%
using (9) (L is optimized for the nominal power using (21)).
The resulting design, referred as Guide50%,opt, is depicted in
Fig. 22.
VOLUME 1, 2020
483

## [стр. 17]

PAPAMANOLIS ET AL.: MINIMUM LOSS OPERATION AND OPTIMAL DESIGN OF HIGH-FREQUENCY INDUCTORS
FIGURE 22. Design space diversity plot for the inductor, computed based on the settings summarized with Tables 1 and 2 and for maximum total losses
of 1.2Pgl,opt, cf. Fig. 11(a). The highlighted lines refer to: i. the four scenarios discussed in Section VI, ii. a quasi-optimal design at 375 kHz obtained using
the proposed guide of Section V for L* at full load and N* at 50% partial load.
FIGURE 23. Constructed Devices Under Test (DUTs) for the verification of
the findings of Section III. The DUTs employ an E55/28/21 core and litz
wires with single-strand diameter of 100 µm. The number of turns and
inductances of the DUTs are (a) N = 16, L = 57 µH, (b) N = 19, L = 200 µH,
(c) N = 30, L = 350 µH.
VII. EXPERIMENTAL VERIFICATION
For the verification of the above-mentioned findings, three
Devices Under Test (DUTs) are built, using the E55/28/21
N87 core and litz wire with a strand diameter of 100 µm,
cf. Fig. 23. The components differ with regard to N and L:
r DUT1: N = 16, L = 57 µH;
r DUT2: N = 19, L = 200 µH;
r DUT3: N = 30, L = 350 µH.
With this, the selected designs cover wide ranges of frequency (150 kHz to 700 kHz) 10 and ripple, cf. Fig. 12(c), to
enable a thorough experimental verification of the discussed
results. Specifically, DUT1 and DUT2 refer to designs with
approximately optimal number of turns, however, in case of
DUT1 the AC copper losses and in case of DUT2 the DC
copper losses dominate the total copper losses. Finally, DUT3
is a suboptimal design, limited by saturation, with dominating
DC copper losses. According to the measured impedances of
the DUTs, depicted in Fig. 24,
and with a maximum test
10The value of 700 kHz is set as the maximum frequency, since no further
improvements are expected above that frequency. Furthermore, the material
approaches the maximum limit of its useful operating region (recommended
maximum frequency according to [22] is 500 kHz).
FIGURE 24. Measured phases and magnitudes of the impedances of the
realized DUTs using a 4294 A impedance analyzer (by Agilent [39]). All
three DUTs feature self-resonance frequencies well below the maximum
operating frequency of 700 kHz.
frequency of 700 kHz, all three components are evaluated well
below their self-resonance frequencies.
As opposed to the core losses, the measurement of the
copper losses, in case of high frequency effects (i.e., proximity
losses), is a challenging task, hence, the total losses of the
designed DUTs are measured. Since the modeled core losses
result from measured data, cf. Section III, the copper losses
can be determined by subtracting the core losses from the total
losses.
For the measurement of the total losses, a calorimetric
setup, depicted in Fig. 25(a), is used [40], [41]. It consists of
an inner calorimeter chamber and an outer reference chamber, which is used to ensure steady ambient conditions during the experiment. The calorimeter chamber accommodates
the DUT and a heating device, i.e., a resistor, an attached
heat sink, and fans, to ensure a homogeneous temperature
inside the chamber. The employed setup enables measurements at a defined ambient temperature without the need
484
VOLUME 1, 2020

## [стр. 18]

FIGURE 25. (a) Calorimeter setup used to measure the total losses
generated by the Device Under Test (DUT) at the desired ambient
temperature. (b) Losses of the heating device and temperature of the
calorimeter chamber during the course of two consecutive experiments at
150 kHz and 300 kHz using DUT3, cf. Fig. 23(c). The losses generated by the
heating device during the three phases of steady-state are highlighted.
for pre-calibrations [40], [41]. The accuracy of the calorimeter has been assessed by means of reference loss measurements conducted with a 1k power film resistor (RCH series by Vishay [42]), and two multimeters for measuring
DC voltage and current (voltage: Fluke 233 [43], current:
Fluke 175 [44]).11 A consecutive measurement of four different losses, i.e., 2 W →5 W →2 W →5 W, reveals maximum and average deviations of 54 mW and 35 mW, respectively, between the calorimetric and the electric measurement.
For all four operating points, the resulting deviations, between
the two measurement methods, lie within the uncertainty
range of the employed multimeters.
For the excitation of the DUTs two sources are employed.
The first source is a DC supply that provides the DC current,
i.e., 10 A (cf. Table 1), and the second source is a linear
amplifier that provides the AC voltage (up to 3 MHz). The
two sources are connected in parallel and decoupled with two
filters.
Fig. 25(b) presents the temperature inside the chamber during an experiment in order to illustrate the measurement procedure by way of example. Initially, the DUT is idle and the
temperature-controlled heater increases the temperature inside the chamber to a defined value. After the system reaches
steady state, the DUT is operated and the heater reduces its
power to maintain a constant temperature. Once at steady
state, the difference between the heating power before and
after the excitation of the DUT corresponds to the losses of
the DUT.
11During this measurement, DUT1 was placed together with the resistor, in
order to emulate the air-flow of the real experiments.
FIGURE 26. Comparison between the losses estimated using the EMT
model (cf. Section III) and the losses using the calorimetric setup of
Fig. 25(a), for the three DUTs of Fig. 23, at a reference (ambient)
temperature of 60◦C. The measurement of the two operating points at 150
kHz and 300 kHz of DUT3 is shown in Fig. 25(b).
For the experimental verification of the findings of
Sections II and III, the EMT model is exactly parameterized
according to the corresponding DUT, e.g., the number of
strands of the litz wire and the positions of the conductors
(inside the core window and on the winding head). The measurements are conducted at a temperature of Tref = 60 ◦C.
Fig. 26 presents the comparison of measured and calculated
total losses for four different operating points per DUT. For
the twelve measured operating points, the maximum deviation between calculated and measured results is 12.7% (for
DUT1 and fs = 300 kHz) and the average absolute deviation
is 4.85%, i.e., well below 20%, which is a commonly accepted
uncertainty value for multi-domain component models. With
this, the experimental results confirm the findings of this work.
VIII. CONCLUSION
In this work, the optimal operation of power inductors in
common topologies, i.e., buck/boost switched converters, is
analyzed. For the analysis and in order to achieve a comprehensible discussion of the various couplings and effects in
inductors, the magnetic core (E55/28/21) and the employed
litz wire (100 µm strand diameter) are fixed. The implications
of the remaining design degrees of freedom, fs, r, and N,
are investigated with focus on the losses and optimal trends
are identified. The analysis is done in two steps, initially
with simplified analytical models and, subsequently, with a
detailed semi-numerical multi-domain model. The link from
the simplified to the detailed model is provided through a stepby-step introduction of different nonlinear effects (e.g., core
saturation, impacts of frequency, AC magnetic flux density,
and DC bias on the core losses). Experimental results confirm
the theoretical findings. The experiments are conducted with
VOLUME 1, 2020
485

## [стр. 19]

PAPAMANOLIS ET AL.: MINIMUM LOSS OPERATION AND OPTIMAL DESIGN OF HIGH-FREQUENCY INDUCTORS
an accurate calorimetric method, three different inductors, and
within a wide frequency range (150 kHz to 700 kHz).
Around the identified global loss optimum, a very flat characteristic of the losses is observed with respect to all three
degrees of freedom. This property enables further potential
opportunities with respect to reduced losses at partial load
(e.g., 20% and 50% of rated load) and reduced cost, which
come at the expense of an increase of the full-load losses
by 15% to 20%. Furthermore, the obtained results enable the
compilation of a simple two-equation guide to achieve designs that feature almost minimal losses for a given frequency.
The total losses of the designs obtained using the proposed
guide compared to the designs optimized using the detailed
semi-numerical model feature a maximum deviation of 17.8%
within a wide frequency range (40 kHz to 375 kHz).
REFERENCES
[1]
J. W. Kolar, D. Bortis, and D. Neumayr, "The ideal switch is not
enough," in Proc. IEEE 28th Int. Symp. Power Semicond. Devices ICs.,
2016, pp. 15-22.
[2]
Z. Liu, F. C. Lee, Q. Li, and Y. Yang, "Design of GaN-based MHz
totem-pole PFC rectifier," IEEE Trans. Emerg. Sel. Topics Power Electron., vol. 4, no. 3, pp. 799-807, Sep. 2016.
[3]
Z. Liu, B. Li, F. C. Lee, and Q. Li, "Design of CRM AC/DC converter
for very high-frequency high-density WBG-based 6.6kW bidirectional
on-board battery charger," in Proc. IEEE Energy Convers. Congr. Expo.
(ECCE USA), 2016, pp. 1-8.
[4]
S. A. Mulder, "Fit formulae for power loss in ferrites and their use in
transformer design," in Proc. Int. Conf. Power Convers. Intell. Motion,
1993, pp. 345-359.
[5]
T. M. Undeland, J. Lode, R. Nilssen, W. P. Robbins, and N. Mohan,
"A single-pass design method for high-frequency inductors," IEEE Ind.
Appl. Mag., vol. 2, no. 5, pp. 44-51, Sep.-Oct. 1996.
[6]
M. Bogs and W. Holubarsch, "Design principles for high frequency
power transformer materials," Le J. de Physique IV, vol. 7, no. C1,
pp. 117-118, 1997.
[7]
F. Forest, E. Laboure, T. Meynard, and M. Arab, "Analytic design method based on homothetic shape of magnetic cores for highfrequency transformers," IEEE Trans. Power Electron., vol. 22, no. 5,
pp. 2070-2080, Sep. 2007.
[8]
A. J. Hanson, J. A. Belk, S. Lim, C. R. Sullivan, and D. J. Perreault,
"Measurements and performance factor comparisons of magnetic materials at high frequency," IEEE Trans. Power Electron., vol. 31, no. 11,
pp. 7909-7924, Nov. 2016.
[9]
M. Mogorovic and D. Dujic, "Sensitivity analysis of medium-frequency
transformer designs for solid-state transformers," IEEE Trans. Power
Electron., vol. 34, no. 9, pp. 8356-8367, Sep. 2019.
[10] T. Guillod and J. W. Kolar, "Medium-frequency transformer scaling
laws: derivation, verification, and critical analysis," CPSS Trans., vol. 5,
no. 1, pp. 18-34, 2020.
[11] J. Biela and J. W. Kolar, "Pareto-optimal design and performance mapping of telecom rectifier concepts," in Proc. Int. Conf. Power Convers.
Intell. Motion, 2010, pp. 1-13.
[12] A. Stupar, T. Friedli, J. Miniböck, M. Schweizer, and J. W. Kolar,
"Towards a 99 percent efficient three-phase buck-type PFC rectifier for
400 V DC distribution systems," in Proc. IEEE Appl. Power Electron.
Conf. Expo., 2011, pp. 505-512.
[13] Q. Li, M. A. E. Andersen, and O. C. Thomsen, "Research on power
factor correction boost inductor design optimization - efficiency vs.
power density," in Proc. IEEE Energy Convers. Congr. Expo. (ECCE
Asia), 2011, pp. 728-735.
[14] U. Badstuebner, A. Stupar, and J. W. Kolar, "Sensitivity of telecom dcdc converter optimization to the level of detail of the system model," in
Proc. IEEE Appl. Power Electron. Conf. Expo., 2011, pp. 585-592.
[15] J. Muhlethaler, M. Schweizer, R. Blattmann, J. W. Kolar, and A. Ecklebe, "Optimal design of LCL harmonic filters for three-phase PFC
rectifiers," IEEE Trans. Power Electron., vol. 28, no. 7, pp. 3114-3125,
Jul. 2013.
[16] A. Stupar, J. A. Taylor, and A. Prodic, "Posynomial models of inductors for optimization of power electronic systems by geometric programming," in Proc. Workshop Control Model. Power Electron., 2016,
pp. 1-8.
[17] K. Watanabe et al., "Optimization of inductors using evolutionary algorithms and its experimental validation," IEEE Trans. Magn., vol. 46,
no. 8, pp. 3393-3396, Aug. 2010.
[18] T. Sato et al., "3-D optimization of ferrite inductor considering hysteresis loss," IEEE Tans. Magn., vol. 49, no. 5, pp. 2129-2132, May 2013.
[19] K. Booth and J. Bandler, "Space mapping for codesigned magnetics:
Optimization techniques for high-fidelity multidomain design specifications," IEEE Power Electron. Mag., vol. 7, no. 2, pp. 47-52, Jun. 2020.
[20] J. Leicht, A. Moses, and S. Zurek, "Hysteresis loss component under
non-sinusoidal flux waveforms," in proc. 18th Int. Symp. Soft Magn.
Mater. J. Magnetism Magn. Mater., vol. 320, no. 20, 2008, pp. e608 -
e610.
[21] T. Komma, "Allgemein gültiger Entwurfsalgorithmus für magnetische
Komponenten in Schaltnetzteilen mit unterschiedlichen Topologien und
Schaltfrequenzen bis 2 MHz," Ph.D. dissertation, Dresden Univ. Technol., 2004.
[22] "EPCOS Data Book 2013 - Ferrites and Accessories," Accessed: Sep.
1, 2020. [Online]. Available: https://www.tdk-electronics.tdk.com/
download/519704/069c210d0363d7b4682
d9ff22c2ba503/ferritesand-accessories-db-130501.pdf
[23] "Soft Ferrites and Accessories - Data Handbook 2013 - Ferroxcube,"
Accessed: Sep. 1, 2020. [Online]. Available: https://www.ferroxcube.
com/en-global/download/download/11
[24] D. Bortis, D. Neumayr, and J. W. Kolar, "ηρ-Pareto optimization
and comparative evaluation of inverter concepts considered for the
GOOGLE Little Box Challenge," in Proc. IEEE Workshop Control
Model. Power Electron., 2016, pp. 1-5.
[25] M. Leibl, "Three-phase PFC rectifier and high-voltage generator for Xray systems," Ph.D. dissertation, Dep. Info. Technol. Elect. Eng. (DITET), Power Electro. Sys. Lab. (PES), ETH Zurich, Switzerland, 2017.
[26] R. Hotopp, "Private photovoltaic power generation systems in parallel
grid operation: Planning, installation, operation, profitability." Expert
advice on renewable energies (in German). RWE Energie, 1991.
[27] E. C. Snelling, Soft Ferrites, Properties Applications. London, U.K.:
Butterworths, 2nd edition, 1988.
[28] V. C. Valchev and A. Van den Bossche, Inductors Transformers Power
Electron. Boca Raton, FL, USA: CRC Press, 2005.
[29] W. G. Hurley and W. H. Wölfle, Transformers Inductors Power Electron.: Theory, Des. Appl. Hoboken, NJ, USA: John Wiley & Sons, Inc.,
Wiley, 2013.
[30] J. Muhlethaler, J. Biela, J. W. Kolar, and A. Ecklebe, "Core losses under
the DC bias condition based on Steinmetz parameters," IEEE Trans.
Power Electron., vol. 27, no. 2, pp. 953-963, Feb. 2012.
[31] "MATLAB v. 9.5," (MathWorks Inc, Natick Massachusetts, United
States). [Online]. Available: https://www.mathworks.com
[32] Jieli Li, T. Abdallah, and C. R. Sullivan, "Improved calculation of core
loss with nonsinusoidal waveforms," in Proc. IEEE Ind. Appl. Conf.,
vol. 4, 2001, pp. 2203-2210.
[33] R. Burkart, "Advanced modeling and multi-objective optimization of
power electronic converter systems," Ph.D. dissertation, ETH Zurich,
Switzerland, 2016.
[34] M. Mu, Q. Li, D. J. Gilham, F. C. Lee, and K. D. T. Ngo, "New
core loss measurement method for high-frequency magnetic materials,"
IEEE Trans. Power Electron., vol. 29, no. 8, pp. 4374-4381, Aug. 2014.
[35] J. Ferreira, "Analytical computation of AC resistance of round and
rectangular litz wire windings," IEE Proc. B - Electric Power Appl.,
vol. 139, no. 1, p. 21-25, Jan. 1992.
[36] M. Antivachis, D. Wu, D. Bortis, and J. W. Kolar, "Analysis of doublebridge inverters for drive systems with open-end winding motors," IEEE
Trans. Emerg. Sel. Topics Power Electron. - Early Access, 2020.
[37] M. Antivachis, J. A. Anderson, D. Bortis, and J. W. Kolar, "Analysis
of a synergetically controlled two-stage three-phase DC/AC buck-boost
converter," IEEE CPSS Trans. Power Electron. Appl., vol. 5, no. 1,
pp. 34-53, Mar. 2020.
[38] R. Burkart and J. W. Kolar, "Component cost models for multi-objective
optimizations of switched-mode power converters," in Proc. IEEE Energy Convers. Congr. Expo. (ECCE USA), 2013, pp. 2139-2146.
[39] "Agilent 4294A - Precision Impedance Analyzer 40 Hz to 110 MHz,"
Accessed: Jun. 17, 2020). [Online]. Available: http://literature.cdn.
keysight.com/litweb/pdf/5968-3808E.pdf
486
VOLUME 1, 2020

## [стр. 20]

[40] T. Kleeb, B. Dombert, S. Araújo, and P. Zacharias, "Loss measurement
of magnetic components under real application conditions," in Proc.
Eur. Conf. Power Electron. Appl., pp. 1-10, 2013.
[41] P. Papamanolis, F. Krismer, and J. W. Kolar, "Minimum loss operation
of high-frequency inductors," in Proc. IEEE Appl. Power Electron.
Conf. Expo., 2018, pp. 1756-1763.
[42] "Power Resistor, for mounting onto a heatshink thick film technology,"
Accessed: Jun. 14, 2020. [Online]. Available: https://www.vishay.com/
docs/50006/rch.pdf
[43] "Fluke 233 remote display digital multimeter," Accessed: Jun.
14,
2020.
[Online].
Available:
https://www.fluke.com/en/product/
electrical-testing/digital-multimeters /fluke-233
[44] "Fluke 175 true-RMS digital multimeter," Accessed: Jun. 14, 2020.
[Online].
Available:
https://www.fluke.com/en/product/electricaltesting/digital-multimeters /fluke-175
[45] M. S. Rylko, B. J. Lyons, J. G. Hayes, and M. G. Egan, "Revised
magnetics performance factors and experimental comparison of highflux materials for high-current DC-DC inductors," IEEE Trans. Power
Electron., vol. 26, no. 8, pp. 2112-2126, Aug. 2011.
[46] W.-J. Gu and R. Liu, "A study of volume and weight vs. frequency
for high-frequency transformers," in Proc. 24th IEEE Power Electron.
Specialists Conf., 1993, pp. 1123-1129.
[47] "Ferrite magnetic design tool," Accessed: Jan. 13, 2020. [Online].
Available:
https://www.tdk-electronics.tdk.com/en/180490/designsupport/design-too ls/ferrite-magnetic-design-tool
[48] P. Papamanolis, T. Guillod, F. Krismer, and J. W. Kolar, "Transient
calorimetric measurement of ferrite core losses up to 50MHz," IEEE
Trans. Power Electron. - Early Access, 2020.
[49] J. Muhlethaler, J. W. Kolar, and A. Ecklebe, "A novel approach for 3D
air gap reluctance calculations," in Proc. 8th Int. Conf. Power Electron.,
2011, pp. 446-452.
[50] J. W. Kolar, F. Krismer, Y. Lobsiger, J. Muhlethaler, T. Nussbaumer,
and J. Minibock, "Extreme efficiency power electronics," in Proc. Int.
Conf. Integr. Power Electron. Syst., 2012, pp. 1-22.
PANTELEIMON PAPAMANOLIS (Student Member, IEEE) studied electrical engineering at the
National Technical University of Athens (NTUA),
Athens, Greece, with majors in energy conversion
and electric power systems. In 2014, he continued
his M.Sc. studies at ETH Zrich in robotics, systems
and control. Since 2016, he is working toward the
Ph.D. degree at Power Electronic Systems Laboratory, ETH Zurich, Zurich, Switzerland, focusing
on the modeling, optimization, and measurement
of magnetic components and on three-phase ac/dc
rectifier converters for EV charging applications.
THOMAS GUILLOD (Member, IEEE) received
the M.Sc. degree in electrical engineering and information technology from ETH Zurich, Zurich,
Switzerland, in 2013, with a focus on power
electronics, numerical analysis, and field theory.
In 2013, he joined the Power Electronic Systems Laboratory, ETH Zurich, as a Ph.D. Student
and, in 2018, as a Postdoctoral Researcher. His
current research interests include medium-voltage
converters, high-frequency magnetic components,
design and optimization methods, and numerical
modeling methods.
FLORIAN KRISMER (Member, IEEE) received
the Dipl.-Ing. (M.Sc.) degree in electrical engineering with specialization in automation and control
technology from the Vienna University of Technology, Vienna, Austria, in 2004, and the Ph.D.
degree in electrical engineering from the Department of Information Technology and Electrical
Engineering, ETH Zurich, Zurich, Switzerland, in
2010. He is currently a Research Associate with
Power Electronic Systems Laboratory (PES), ETH
Zurich, where he has cosupervised Ph.D. students
and has continued with his research in the field of power electronics. He is the
author or coauthor of numerous conference and peer-review publications. Dr.
Krismer is the recipient of two awards for his publications. His research interests include the analysis, design, and general optimization of power converter
systems, e.g., the weight optimization of a bidirectional dc-dc converter
for an airborne wind turbine. Furthermore, he conducts research related to
the filtering of conducted electromagnetic emissions and collaborated in the
littlebox-challenge with respect to the hardware realization.
JOHANN W. KOLAR (Fellow, IEEE) received the
M.Sc. degree in industrial electronics and control
engineering and the Ph.D. degree in electrical engineering (summa cum laude/promotio sub auspiciis
praesidentis rei publicae) from the Vienna University of Technology, Vienna, Austria, in 1997 and
1999, respectively. Since 1984, he has been working as Independent Researcher and International
Consultant in close collaboration with the Vienna
University of Technology, in the fields of power
electronics, industrial electronics, and high performance drive systems. He is currently a Full Professor and the Head of the
Power Electronic Systems Laboratory, Swiss Federal Institute of Technology
(ETH) Zurich, Switzerland. He has proposed numerous novel pulsewidth
modulation converter topologies, modulation and control concepts, multiobjective power electronics design procedures, etc. and has supervised 70+
Ph.D. students. He has authored or coauthored 900+ scientific papers in
international journals and conference proceedings, four book chapters, and
has filed 190+ patents. He has presented 30+ educational seminars at leading international conferences and has served as IEEE PELS Distinguished
Lecturer from 2012 through 2016. Dr. Kolar is the recipient of 36 IEEE
Transactions and Conference Prize Paper Awards, the 2014 IEEE Power Electronics Society R. David Middlebrook Achievement Award, the 2016 IEEE
William E. Newell Power Electronics Award, the 2016 IEEE PEMC Council
Award, and two ETH Zurich Golden Owl Awards for excellence in teaching.
He has initiated and/or is the Founder of four ETH Spin-off companies.
The focus of his current research is on ultra-compact and ultra-efficient SiC
and GaN converter systems, ANN-based power electronics components and
systems design, solid-state transformers, power supplies on chip, as well as
ultra-high speed and ultra-light weight drives, bearingless motors, and energy
harvesting.
VOLUME 1, 2020
487
