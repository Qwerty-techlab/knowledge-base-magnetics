# Improved Core Loss Calculation for Magnetic Components Employed in Power Electronic Systems

> Автоматически извлечено из `source.pdf` скриптом `parse_pdf.py`
> Движок: pymupdf. Страниц: 9 из 9.
> Дата извлечения: 2026-08-07 06:43 UTC

Текст не редактировался. Формулы и таблицы могут быть искажены —
при сомнении сверяться с исходным PDF.

---

## [стр. 1]

© 2011 IEEE
Proceedings of the 26th Annual IEEE Applied Power Electronics Conference and Exposition (APEC 2011), Ft. Worth, TX, USA,
March 6-10, 2011.
Improved Core Loss Calculation for Magnetic Components Employed in Power Electronic Systems
J. Mühlethaler
J. Biela
J. W. Kolar
A. Ecklebe
This material is posted here with permission of the IEEE. Such permission of the IEEE does not in any way imply IEEE
endorsement of any of ETH Zurich's products or services.  Internal or personal use of this material is permitted.  However,
permission to reprint/republish this material for advertising or promotional purposes or for creating new collective works for
resale or redistribution must be obtained from the IEEE by writing to pubs-permissions@ieee.org.  By choosing to view this
document, you agree to all provisions of the copyright laws protecting it.

## [стр. 2]

Improved Core Loss Calculation for Magnetic
Components Employed in Power Electronic Systems
J. M¨uhlethaler∗, J. Biela†, J. W. Kolar∗, and A. Ecklebe‡
∗Power Electronic Systems Laboratory, ETH Zurich, Email: muehlethaler@lem.ee.ethz.ch
†Laboratory for High Power Electronic Systems, ETH Zurich
‡ABB Switzerland Ltd., Corporate Research, Baden-D¨attwil, Switzerland
Abstract-In modern power electronic systems, voltages across
inductors/transformers generally show rectangular shapes, as the
voltage across an inductor/transformer can be positive, negative
or zero. In the stage of zero applied voltage (constant flux) core
losses are not necessarily zero. At the beginning of a period
of constant flux, losses still occur in the material. This is due
to relaxation processes. A physical explanation about magnetic
relaxation is given and a new core loss modeling approach that
takes such relaxation effects into consideration is introduced.
The new loss model is called i2GSE and has been verified
experimentally.
Index Terms-Core Losses, Ferrite, Steinmetz, Relaxation,
Dual Active Bridge.
I. INTRODUCTION
In modern power electronic systems, voltages across inductors/transformers generally show rectangular shapes, as illustrated in Fig. 1. The voltage across an inductor / transformer
can be positive, negative or zero. This results in the flux in
the core ramping up, ramping down or remaining constant.
Core losses need to be determined for the design of inductive components. The most used equation that characterizes
core losses is the power equation [1]
Pv = kf α ˆBβ
(1)
where
ˆB is the peak induction of a sinusoidal excitation
with frequency f, Pv is the time-average power loss per unit
volume, and k, α, β are material parameters. The equation
is called the Steinmetz Equation (after Charles P. Steinmetz).
The material parameters k, α, and β are accordingly referred
to as the Steinmetz parameters. They are valid for a limited
frequency and flux density range. The major drawback of
the Steinmetz Equation is that it is only valid for sinusoidal
excitation. This is a huge drawback, because, as stated above,
in power electronic applications the material is usually exposed
to non-sinusoidal flux waveforms.
To overcome this limitation, and determine losses for a
wider variety of waveforms, different approaches have been
developed. The approaches can be classified into the following
categories:
1) Improvements of the Steinmetz Equation (1): for instance, the analysis in [2] is motivated by the fact that the
loss due to domain wall motion has a direct dependency
of dB/dt. As a result, a modified Steinmetz Equation
is proposed. In [3] the approach is further improved and
t
T
vL
iL
T / 2
I
II
III
Fig. 1.
Typical voltage/current waveform of magnetic components employed
in power electronic systems. Phase I: positive voltage; phase II: zero voltage;
phase III: negative voltage.
in [4] a method how to deal with minor hysteresis loops
is presented and some minor changes on the equation
are made. The approach of [2], [3], and [4] leads to the
improved Generalized Steinmetz Equation (iGSE)
Pv = 1
T
Z T
0
ki
dB
dt

α
(∆B)β-α dt
(2)
where ∆B is peak-to-peak flux density and
ki =
k
(2π)α-1 R 2π
0
| cos θ|α2β-αdθ
.
(3)
The parameters k, α, and β are the same parameters as
used in the Steinmetz Equation (1). By use of the iGSE
losses of any flux waveform can be calculated, without
requiring extra characterization of material parameters
beyond those for the Steinmetz Equation.
2) Calculation of the losses with a loss map that is based on
measurements. This loss map stores the loss information
for different operating points, each described by the flux
density ripple ∆B, the frequency f, the temperature T,
and a DC bias HDC (e.g. in [5]-[7]).
3) Methods to determine core losses based on breaking up
the total loss into loss components, i.e. hysteresis losses,
classical eddy current losses, and residual losses [8].
4) Hysteresis models such as Preisach and Jiles-Atherton
used for calculating core losses.
In the categories 1 and 2 a loss energy is assigned to each
section of the voltage / current waveform as illustrated in Fig.
1 (e.g. via an equation as (2) or via a loss map), and these
978-1-4244-8085-2/11/$26.00 ©2011 IEEE
1729

## [стр. 3]

losses are summed-up to calculate the power loss occurring in
the core. This approach is e.g. implemented in [9].
In most of the previous publications, the phase where the
voltage across the magnetic component is zero has not been
discussed. It has been implicitly assumed that no losses occur
when the flux remains constant. However, as measurements
show, this is not a valid simplification. At the beginning of a
period of constant flux, losses still occur in the material. In
the publication [10] about core loss modeling, a loss increase
during zero voltage periods has been observed, however, no
explanation or modeling approach is given.
This work shows that this loss increase is due to relaxation
processes inside the magnetic core material. Furthermore, a
new model is introduced that considers relaxation effects
when calculating core losses. A core loss measurement test
setup has been built to analyze core losses under general flux
waveform excitations. The test system is presented in Section
II. In Section III a brief introduction to magnetic relaxation
is given. In Section IV, V, and VI a new loss model is
derived that substantially improves core loss calculation by
taking relaxation processes into consideration. In Section VII
an easy-to-follow example is given to illustrate how the new
model can be applied. Before concluding the work, in Section
VIII a short discussion of the behavior of different materials
is given.
II. TEST SETUP TO MEASURE CORE LOSSES
In order to perform core loss measurements, the best measurement technique has to be selected first. In [11] different
methods are compared. The B-H Loop Measurement has been
evaluated as the most suitable. Amongst other advantages,
this technique offers rapid measurement (compared to other
methods, e.g. calorimetric measurements), copper losses are
not measured, and a good accuracy. The principle is as follows:
two windings are placed around the Core Under Test (CUT).
The sense winding (secondary winding) voltage v is integrated
to sense the core flux density B
B(t) =
1
N2 · Ae
Z t
0
v(τ)dτ
(4)
where N2 is the number of sense winding turns and Ae is the
effective core cross section of the CUT. The current in the
excitation winding (primary winding) is proportional to the
magnetic field strengths H
H(t) = N1 · i(t)
le
(5)
where N1 is the number of excitation winding turns and le
is the effective magnetic path length of the CUT. The loss
per unit volume is then the enclosed area of the B-H loop,
multiplied by the frequency f
P
V = f
I
HdB.
(6)
The selected approach is widely used [4], [6]. The built
test system consists of a power stage, a power supply, an
oscilloscope and a heating chamber. It is controlled by a
Fig. 2.
Test setup (a) photograph, (b) simplified schematic.
MATLAB program running on the oscilloscope under Microsoft Windows. In Fig. 2 a photograph (a) and the simplified
schematic (b) of the power stage are shown. The power stage
is capable of a maximal input voltage of 450 V, output current
of 25 A and a switching frequency of up to 200 kHz. The test
setup allows application of a general rectangular voltage shape
across the CUT that leads to a triangular and / or trapezoidal
current shape including a DC bias (if desired).
The reader is referred to [12] for more information about
the test setup, including a detailed accuracy analysis of the
loss measurement.
III. RELAXATION PROCESSES IN MAGNETIC MATERIALS
As already mentioned in the introduction, during the phase
of constant flux (where the voltage across the magnetic component is zero) losses still occur in the core material. A literature
survey led to the conclusion that this is due to relaxation
processes in the magnetic core material. In this section, first
measurements are presented that illustrate magnetic relaxation.
Further, an attempt to theoretically explain the effect is given,
and, with it, the resulting shape of a B-H loop for trapezoidal
flux waveform is analyzed.
A. Measurement Results
According to (2), the energy loss would only depend on
the magnitude and the slope of the flux, and, consequently,
there should be no loss during periods of constant flux (zero
voltage). Measurements on waveforms as illustrated in Fig.
3(a) have been performed to investigate this. Fig. 4 shows
1730

## [стр. 4]

Fig. 3.
(a) Voltage and flux density waveforms. (b) B-H loop to illustrate
magnetic relaxation under trapezoidal flux shape condition.
0
10
20
30
40
50
60
0
1
2
3
4
5
6
7
t1[µs]
E [µJ]
∆B = 50mT, t2 = 10µs
∆B = 100mT, t2 = 10µs
∆B = 100mT, t2 = 5µs
τ
Fig. 4.
Measurement results measured on ferrite EPCOS N87 (R42,
B64290L22X87 [13]). It is further illustrated how τ according to (18) can
be extracted.
the corresponding measurement results. The CUT is made of
ferrite EPCOS N87 (size R42). According to (2), the duration
of t1 should not influence the loss energy per cycle, but, as
can be seen, increasing t1 has a substantial influence on the
loss energy per cycle. In particular, a change in t1 at low
values of t1 influences the dissipated loss. For larger values
of t1, the core material has time to reach its equilibrium state
and no increase in losses can be observed when t1 is further
increased.
It has been confirmed that this effect is not due to an impact
of the measurement setup (e.g. small exponential change of
current due to voltage drop over the inductor in the zero
voltage time intervals).
Concluding, at the beginning of the phase of constant
flux (where the voltage across the magnetic component is
zero) losses still occur because of relaxation processes in
the magnetic core material. Next, a brief introduction about
magnetic relaxation is given.
B. Theory of Relaxation Effects
There are basically three physical loss sources: (static) hysteresis losses, eddy-current losses, and a third loss component
which is often referred to as residual losses. Hysteresis losses
are linear with the frequency f (rate-independent B-H loop).
Eddy-current losses occur because of an induced current due
to the changing magnetic field, and are strongly depend on
the material conductivity and the core geometry. The residual
losses are, according to [8], due to relaxation processes: if
the thermal equilibrium of a magnetic system changes, the
system progressively moves towards the new thermal equilibrium condition. When the magnetization changes rapidly,
as for example is the case in high-frequency or pulsed field
applications, such relaxation processes become very important.
The Landau-Lifshitz Equation qualitatively describes the
dynamics of the magnetic relaxation process. The equation
follows directly from equating the rate of change of the angular
momentum L to the torque M×H reduced by a frictional term
that is directed opposite to the direction of motion [8]:
dM
dt = γM × H -ΛM × (M × H)/M 2,
(7)
where γ = ge/2mc is the magnetomechanical ratio M/L, M
is the magnetization vector, H the magnetic field vector, and Λ
is called the relaxation frequency. It describes how the system
progressively moves towards the new thermal equilibrium. The
equilibrium is achieved by rearranging the magnetic domain
structures to reach states of lower energy. The relaxation
process limits the speed of flux change, hence the B-H loops
becomes rate-dependent. Several physical processes are contributing simultaneously to magnetic relaxation. The interested
reader is referred to [8], [14], [15] for more information.
Concluding, due to magnetic relaxation, the magnetization
may change even when the applied field is constant (the magnetization is delayed). Consequently, a residual energy loss still
occurs in the period of a constant applied field. Furthermore,
the shape of the hysteresis loop is changed depending on the
rate of change of the applied field (rate-dependent loop). An
analysis of the impact of magnetic relaxation to a trapezoidal
flux shape now follows.
C. Shape of B-H Loop for Trapezoidal Flux Waveforms
A B-H loop under trapezoidal flux waveform condition has
been measured to gain a better comprehension of why the
losses increase when the duration of the zero voltage period
is increased. The CUT is a toroid core R42 made of ferrite
EPCOS N87. In Fig. 3(a) the flux waveform, and in Fig. 3(b)
the corresponding B-H loop are plotted. The B-H loop always
traverses counterclockwise. The different instants (cf. numbers
in Figure 3(a) and (b)) are now discussed step-by-step:
1731

## [стр. 5]

1) A constant voltage at the CUT primary winding results
in a time linear flux increase.
2) The CUT primary voltage is set to zero; as a consequence the flux is frozen (dB/dt = 0). However, the
material has not yet reached its thermal equilibrium. The
magnetic field strength H declines to move towards the
new thermal equilibrium and therewith reaches a state of
lower energy. This can also be observed in the current
(the current declines accordingly).
3) This point is reached approximately 24 µs after point 2.
It is the point of the new thermal equilibrium.
4) This point is reached approximately 200 µs after point
3. The demagnetization in the zero voltage period is due
to the small voltage drop over the on-resistance of the
MOSFETs and copper resistance of the inductor primary
winding. This demagnetization follows a completely
different time constant than the demagnetization due to
relaxation losses (cf. the approximately same distance
2-3 and 3-4, but the completely different time scale). At
point 4 a negative voltage is applied to the CUT. The
small buckle in the B-H loop is due to small capacitive
currents at the switching instant.
The period between point 2 and 3 obviously increases the
area of the B-H loop, and therewith increases the core losses.
The loop area increases as a function of the duration t1. After
the thermal equilibrium is reached (in the above example after
approximately 24 µs) the loss increase becomes (almost) zero.
More measurements are presented to find a method to include
this effect into an existing core loss model in the next section.
IV. MODEL DERIVATION 1: TRAPEZOIDAL FLUX
WAVEFORM
Losses can be calculated with (2), without requiring extra
characterization of material parameters beyond the parameters
for the Steinmetz Equation. The Steinmetz parameters are
often given by core manufacturers, hence core loss modeling
is possible without performing extensive measurements. However, the approach has some drawbacks. First, it neglects the
fact that core losses may vary under DC bias condition. This
is discussed in [12], where a graph showing the dependency of
the Steinmetz parameters (α, β and k) on premagnetization is
introduced. With it, losses can be calculated via the Steinmetz
Equation (1) or the iGSE (2) using appropriate Steinmetz
parameters. Another source of inaccuracy is that relaxation
effects are not taken into consideration. As approach (2) is very
often discussed in literature and often applied for designing
magnetic components, improving this method would have the
most practical use. Furthermore, in [16] it has been evaluated
as the most accurate state-of-the-art loss model based on
Steinmetz parameters. For this two reasons, in the following,
the iGSE will be extended to consider relaxation losses as
well.
Plotting the losses with logarithmic axes, where the x-axis
represents the frequency, and the y-axis represents the power
loss, leads to an approximately straight line. This is because
the losses follow a power function, as e.g. the law stated in (1)
4000
8000
12000
16000
20000
10
-2
10
-1
10
0
dB/dt [T/s]
P [W]
∆B = 100mT, t1 = 0
∆B = 100mT, t1 = 60µs
∆B = 200mT, t1 = 0
∆B = 200mT, t1 = 60µs
Fig. 5.
Core Loss (ferrite N87; measured on R42 core), T = 25 ◦C.
is. The parameter α of (1) represents the slope of the curve
in the plot. In Fig. 5 such plots are given for few operating
points. Instead of the frequency f, dB/dt has been used as
x-axis, which, for symmetric triangular or trapezoidal flux
waveforms, is directly proportional to the frequency f. The
time t1 is defined as in Fig. 3 (t1 = 0 leads to a triangular flux
waveform). It is very interesting to note that when a long zero
voltage phase is added between two voltage pulses (having a
flux waveform as given in Fig. 3) the loss still follows a power
function. The same conclusion can be made when keeping
dB/dt constant and varying ∆B, hence, the use of a power
function with variable ∆B is justified as well.
It should be pointed out that when having a zero voltage
interval (t1̸ = 0) the average power loss decreases (cf. Fig.
5). There is no discrepancy with the observation in Fig. 4,
where an energy loss per cycle increase has been observed.
When having a zero voltage interval the energy loss per cycle
increases, but the period increases as well and leads to a lower
average power loss.
The approach of (2) will now be extended by taking
relaxation effects into consideration. This is done by adding
a new additional term that represent the relaxation effect of a
transition to zero voltage. As can be seen in Fig. 4, the loss
energy can be modeled with the exponential equation
E = ∆E

1 -e-t1
τ

,
(8)
where ∆E is the maximum loss energy increase (which
occurs, when the magnetic material has enough time to reach
the new thermal equilibrium), τ is the relaxation time that
has to be further determined, and t1 is the duration of the
constant flux (zero applied voltage) phase. The exponential
behavior is typical for relaxation processes. Measurements
have shown that τ can be considered as a constant parameter
for different operating points. ∆E is a function of ∆B and
dB(t)/dt, where ∆B and dB(t)/dt define the flux density
waveform before a transition to zero voltage as illustrated in
Fig. 6. As mentioned before, and illustrated in Fig. 5, the losses
1732

## [стр. 6]

dB(t)/dt
B
t
∆B
Fig. 6.
Definition of dB(t)/dt and ∆B.
with and without zero voltage phase follow a power function.
Consequently, the losses due to relaxation must follow a power
function as well. Because τ is constant and the energy in all
operating points follow the same law stated in (8), the energy
∆E has to follow a power function as well1 (with variables
∆B and dB(t)/dt). As a consequence, the following power
function can be defined for ∆E:
∆E = kr
d
dtB(t)

αr
(∆B)βr,
(9)
where αr, βr, and kr are new model parameters that have to be
determined empirically. The relaxation losses of a transition
to zero voltage can be determined according to the antecedent
flux density slope dB(t)/dt and the antecedent flux density
peak-to-peak value ∆B. Accordingly, when the flux density
reaches and remains at zero as occurs e.g. in a buck converter
that is operating in discontinuous conduction mode, relaxation
losses have to be taken into consideration as well. However,
the losses may (slightly) differ in this situation because the
antecedent flux density is DC biased. This DC level of the
antecedent flux density has not been part of investigation of
the present work and could be investigated as part of a future
work.
Concluding, (2) has been extended by an additional term
that describes the loss behavior for a transient to constant flux.
This leads to a new model
Pv = 1
T
Z T
0
ki
dB
dt

α
(∆B)β-α dt +
n
X
l=1
Prl,
(10)
where Prl represents the power loss density due to the lth of
n transients to zero voltage. Each transient to zero voltage is
calculated according to
Prl = 1
T kr
d
dtB(t)

αr
(∆B)βr 
1 -e-t1
τ

.
(11)
V. MODEL DERIVATION 2: TRIANGULAR FLUX
WAVEFORM
Often in power electronics, one has a period of zero
voltage applied to a magnetic component winding, e.g. in the
transformer of a bidirectional isolated DC-DC converter with
Dual Active full Bridges (DAB). A DAB will be presented in
Section VII as an example to illustrate the model. In this case,
(10) can directly be used to improve the loss model.
1Power loss and energy loss are coupled by a time factor. Because τ is
constant, this factor is the same for all operating points and the function
structure remains.
Fig. 7.
Triangular flux density waveform.
iGSE
Measured Values
i2GSE
Upper Loss Limits
P [W]
Fig. 8.
Core loss duty cycle dependency. ∆B = 0.1 T, f = 20 kHz.
However, another frequently occurring waveform is a triangular flux waveform in which the flux slope changes to
another nonzero value. This case is illustrated in Fig. 7. When
assuming a duty cycle of 50 % (D = 0.5), directly after
switching to the opposite voltage the flux slope reverses, the
material has hardly time to move towards the new thermal
equilibrium. As a consequence, no notable loss increase is
expected and thus this case is well described by the iGSE (2).
However, when the duty cycle goes to smaller values, once
each period, a high flux slope is followed by a very slow
flux change. Assuming D to be infinitely small, a switch to
a constant flux happens. Consequently, in this case the iGSE
(2) is not accurate and the relaxation term has to be added. In
all operating points where D > 0 and D < 0.5 (or D > 0.5
and D < 1), a behavior that is in-between these two cases is
expected. In other words, only part of the relaxation term has
to be added.
In Fig. 8 the calculated and measured core losses as a
function of the duty cycle are plotted. One calculation has
been performed based on the iGSE (2) which, according to the
above discussion, represents the lower limit of possible losses
(as no relaxation effects are taken into account). It should
be noted that two sets of Steinmetz parameters have been
used for the calculation of the iGSE. The reason is that the
Steinmetz parameters are only valid in a limited dB/dt range,
and the dB/dt in this experiment is varying in a wide range.
This explains the sharp bend of the iGSE curve at D = 0.15
(change of Steinmetz parameter). Another calculation has been
1733

## [стр. 7]

made always including the full relaxation loss term and which
represents the upper loss loss limit. In other words, it can be
said that losses are expected to have values between the line
representing the upper loss limit and the line representing the
lower loss limit (iGSE). According to the previous discussion,
the real losses are closer to the lower loss limit for D close
to 0.5, and losses closer to the upper loss limit for D close to
zero. This has been confirmed by measurements as can be seen
in Fig. 8. Other operating points showed the same behavior.
Based on the above discussion, the new approach can be
further improved to be also valid for triangular flux waveforms.
Basically, (10) can be rewritten as
Pv = 1
T
Z T
0
ki
dB
dt

α
(∆B)β-α dt +
n
X
l=1
QrlPrl,
(12)
where Qrl has to be further defined. In the case of a switch
to zero voltage, Qrl needs to have the value 1. Furthermore,
it has to have a structure so that (12) fits the measurement
points of a duty cycle measurement, such as illustrated in Fig.
8. The following function has been chosen:
Qrl = e
-qr

dB(t+)/dt
dB(t-)/dt
,
(13)
where dB(t-)/dt represents the flux density before the
switching, dB(t+)/dt the flux density after the switching, and
qr is a new material parameter. For a triangular waveform, as
illustrated in Fig. 7, (13) can be rewritten (for D ≤0.5)
Qrl = e
-qr
∆B
(1-D)T
∆B
DT
= e-qr
D
1-D .
(14)
In the case of the material Epcos N87 qr = 16 has been found,
the resulting loss curve is plotted in Fig. 8. Before giving an
illustrative example in Section VII, the new model will be
summarized and the steps to extract the model parameters will
be given.
VI. NEW CORE LOSS MODEL: THE i2GSE
A new loss model that substantially increases the expected
accuracy when core losses are modeled has been introduced.
We call this new model the improved-improved Generalized
Steinmetz Equation i2GSE. The name has been chosen because it is an improved version of the iGSE [4]. The power
loss density can be calculated with
Pv = 1
T
Z T
0
ki
dB
dt

α
(∆B)β-α dt +
n
X
l=1
QrlPrl,
(15)
where Prl is calculated for each voltage change according to
Prl = 1
T kr
d
dtB(t)

αr
(∆B)βr 
1 -e-t1
τ

,
(16)
Qrl is a function that further describes the voltage change and
is
Qrl = e
-qr

dB(t+)/dt
dB(t-)/dt
,
(17)
and α, β, ki, αr, βr, kr, τ, and qr are material parameters.
Now, the steps to extract the model parameters are given:
1) First, the parameters ki, α, and β are extracted. The core
is excited with a rectangular voltage waveform that leads
to a symmetric triangular flux waveform. Measurements
at three operating points are performed, then (15) is
solved for the three parameters. For triangular flux
waveform we have Pn
l=1 QrlPrl = 0 (no phase of zero
applied voltage). In Table I the measurement results and
the corresponding parameters are given. These parameters could be extracted directly from the data sheet as
well, as explained in [4].
2) The parameter τ can be read from Fig. 4 with
∆E
τ
= dE
dt ,
(18)
where dE/dt represents the slope of the energy increase
directly after switching to zero voltage. This is illustrated
in Fig. 4. τ = 6 µs has been extracted for the material
N87.
3) The parameters kr, αr, and βr are extracted by performing measurements at three operating points with
t1 large enough to let the material reach the thermal
equilibrium. Then, (9) is solved for the three parameters.
In Table I the measurement results and the corresponding
parameters are given.
4) The parameter qr has to be selected such that (15) fits
the measurement points of a duty cycle measurement,
as illustrated in Fig. 8.
All model parameters are summarized in Table I. Extracting
the parameters is sometimes difficult and measurements have
to be performed very carefully. One error source is a possible
current decrease due to a voltage drop over the inductor
winding during "zero" voltage phase. This can be avoided by
choosing a high amount of primary turns. This increases the
inductance value and the current is kept more constant (by
choosing a high amount of primary turns the winding copper
resistance increases as well, however, the inductance value
increases quadratically while the resistance value increases
linearly).
TABLE I
MEASUREMENT RESULTS AND MODEL PARAMETER OF MATERIAL
EPCOS N87.
Operating Point
Loss Density
Model Parameters
(∆B; f)
[kW/m3]
(0.1 T; 20 kHz)
5.98
ki = 8.41
(0.1 T; 50 kHz)
16.2
α = 1.09
(0.2 T; 50 kHz)
7.28
β = 2.16
(∆B; dB(t)/dt)
[J/m3]
(0.1 T; 4 kT/s)
0.068
kr = 0.0574
(0.1 T; 20 kT/s)
0.13
αr = 0.39
(0.2 T; 20 kT/s)
0.32
βr = 1.31
τ = 6 µs
qr = 16
VII. EXAMPLE OF HOW TO USE THE NEW MODEL
In the previous section, a new core loss modeling approach
was introduced. This section shows now an easy-to-follow
1734

## [стр. 8]

Fig. 9.
DAB schematic (a) and waveforms (b) with specifications given in
Table II.
TABLE II
SPECIFICATIONS OF DAB TRANSFORMER
VDC = V1 = V2
42 V
f
50 kHz
N=N1=N2
20
Effective Magnetic Length le
103 mm
Effective Magnetic Cross Section Ae
95.75 mm2
Core
EPCOS N87, R42
(B64290L22X87) [13]
example that illustrates how to calculate core losses of a transformer employed in a bidirectional isolated DC-DC converter
with Dual Active full Bridges (DAB) [16], [17]. In Fig. 9(a)
the simplified schematic and in Table II the specifications of
the transformer are given. The shape of the core influences
the core losses, however, this is not the scope of the present
work, hence a simple toroid is considered as the transformer
core. Phase-shift modulation has been chosen as modulation
method: primary and secondary full bridge switch with 50 %
duty cycle to achieve a rectangular voltage v1 and v2 across
the primary and secondary transformer side, respectively. The
waveforms are illustrated in Fig. 9(b), including the magnetic
flux density Bµ of the transformer core. A phase shift γ between v1 and v2 results in a power transfer. When the voltages
v1 and v2 are opposed (which is the case in phase tγ), the full
voltage drop is across the transformer leakage inductance and
the magnetic flux density Bµ remains unchanged.
Only the magnetic flux density Bµ time behavior has
been considered for designing the transformer, i.e. no winding losses or leakage inductance have been calculated. The
value of the leakage inductance is very important for the
functionality, however, it is not discussed here. Therefore,
no statement about feasibility is made, the circuit should
only represents solely a simple and easy-to-follow illustrative
magnetic example.
The losses are calculated according to the i2GSE (15). The
results are then compared with measurement results. The peak
flux density in the core can be calculated with [16]
ˆB = 1
2
VDC
NAe
T
2 -tγ

(19)
and its time derivative with
dB
dt =











VDC
NAe
for t ≥0 and t < T
2 -tγ,
0
for t ≥T
2 -tγ and t < T
2 ,
-VDC
NAe
for t ≥T
2 and t < T -tγ,
0
for t ≥T -tγ and t < T.
(20)
Calculating the losses according to (15) leads to the following expression as a function of tγ
P =T -2tγ
T
ki
VDC
NAe

αVDC
NAe
T
2 -tγ
 
β-α
Aele
+ Aele
n
X
l=1
QrlPrl,
(21)
where P2
l=1 QrlPrl represents the two transients to zero
voltage. There are two switching instants to zero voltage, each
with Qrl = 1. The values for Prl then have to be determined:
it is for each transient
Prl = 1
T kr
VDC
NAe

αrVDC
NAe
T
2 -tγ
 
βr 
1 -etγ
τ

.
(22)
The losses have been calculated according to the new approach, and have been compared to a calculation using the
classic iGSE (2) and with measurement results. Open-circuit
(no load) measurements have been performed to validate the
new model: the primary winding is excited to achieve a flux
density as illustrated in Fig. 9(b). Measurements for different
values of tγ have been performed, at constant frequency f and
voltage VDC. The new model and measurement results match
very well as shown in Fig. 10.
In [16] different state-of-the-art core loss calculation approaches are compared using a very similar example. The
iGSE (2) showed the best agreement with measurements, but
for increasing zero voltage periods tγ, the calculated core
losses start deviating from the measured core losses. The
reason becomes clear with the new approach i2GSE and the
calculation can be improved.
VIII. MEASUREMENTS ON DIFFERENT MATERIALS
The approach has been confirmed on different materials,
including on VITROPERM 500F from VAC (measured on
W452 core). The model parameters are given in Table III.
Measurements show promise that the approach is applicable
for all material types, however, this remains to be confirmed
as part of a future work.
1735

## [стр. 9]

Measured Values
i2GSE
iGSE
Fig. 10.
Loss calculation and loss measurement comparison of the DAB
example.
TABLE III
MODEL PARAMETER OF MATERIAL VITROPERM 500F (VAC).
α
1.88
β
2.02
ki
137 · 10-6
αr
0.76
βr
1.70
kr
139 · 10-6
τ
9 µs
qr
4
IX. CONCLUSION AND FUTURE WORK
The Steinmetz Equation (1) and its extension iGSE (2) are
relatively accurate models to describe core losses. However,
some core loss mechanisms cannot be described with an equation of only three parameters. The Steinmetz parameters alone
are insufficient to fully describe core losses. This publication
together with the work presented in [12] tries to show new
approaches of how core losses could be better determined.
However, a few new model parameters are necessary.
As experimentally verified, core losses are not necessarily
zero when zero voltage is applied across a transformer or
inductor winding after an interval of changing flux density.
A short period after switching the winding voltage to zero,
still losses occur in the material. This is due to magnetic
relaxation. A new loss modeling approach has been introduced
and named the improved-improved Generalized Steinmetz
Equation, i2GSE. The i2GSE needs five new parameters to
calculate new core loss components. Hence, in total eight
parameters are necessary to accurately determine core losses.
The approach should be verified for different materials,
applications, etc. Furthermore, a DC level of the antecedent
flux density has not been part of this investigation of the
present work and could be considered as part of a future work.
ACKNOWLEDGEMENT
The authors would like to thank ABB Switzerland Ltd. for
giving them the opportunity to work on this very interesting
project.
REFERENCES
[1] E. C. Snelling, Soft Ferrites, Properties and Applications. 2nd edition,
Butterworths, 1988.
[2] J. Reinert, A. Brockmeyer, and R. De Doncker, "Calculation of losses
in ferro- and ferrimagnetic materials based on the modified Steinmetz
equation," IEEE Transactions on Industry Applications, vol. 37, no. 4,
pp. 1055-1061, 2001.
[3] J. Li, T. Abdallah, and C. R. Sullivan, "Improved calculation of core loss
with nonsinusoidal waveforms," in Industry Applications Conference,
2001. 36th IEEE IAS Annual Meeting., vol. 4, pp. 2203-2210, 2001.
[4] K. Venkatachalam, C. R. Sullivan, T. Abdallah, and H. Tacca, "Accurate
prediction of ferrite core loss with nonsinusoidal waveforms using only
Steinmetz parameters," in Proc. of IEEE Workshop on Computers in
Power Electronics, pp. 36-41, 2002.
[5] S. Iyasu, T. Shimizu, and K. Ishii, "A novel iron loss calculation
method on power converters based on dynamic minor loop," in Proc. of
European Conference on Power Electronics and Applications, pp. 20162022, 2005.
[6] T. Shimizu and K. Ishii, "An iron loss calculating method for AC
filter inductors used on PWM inverters," in Proc. of 37th IEEE Power
Electronics Specialists Conference (PESC), pp. 1-7, 2006.
[7] K. Terashima, K. Wada, T. Shimizu, T. Nakazawa, K. Ishii, and
Y. Hayashi, "Evaluation of the iron loss of an inductor based on
dynamic minor characteristics," in Proc. of European Conference on
Power Electronics and Applications, pp. 1-8, 2007.
[8] J. B. Goodenough, "Summary of losses in magnetic materials," IEEE
Transaction on Magnetics, vol. 38, pp. 3398-3408, Sept. 2002.
[9] J. Liu, T. G. W. Jr., R. C. Wong, R. Wunderlich, and F. Lee, "A
method for inductor core loss estimation in power factor correction
applications," in Proc. of Applied Power Electronics Conference and
Exposition (APEC), 2002.
[10] C. R. Sullivan, J. H. Harris, and E. Herbert, "Core loss predictions for
general PWM waveforms from a simplified set of measured data," in
Proc. of Applied Power Electronics Conference and Exposition (APEC),
pp. 1048-1055, 2010.
[11] B. Carsten, "Why the magnetics designer should measure core loss; with
a survey of loss measurement techniques and a low cost, high accuracy
alternative," in Proc. of PCIM, pp. 163-179, 1995.
[12] J. M¨uhlethaler, J. Biela, J. W. Kolar, and A. Ecklebe, "Core losses under
DC bias condition based on Steinmetz parameters," in Proc. of the
IEEE/IEEJ International Power Electronics Conference (ECCE Asia),
pp. 2430-2437, 2010.
[13] Ferrites and Accessories, Edition 2007. EPCOS AG.
[14] G. Bertotti, Hysteresis in Magnetism. Academic Press, Inc., 1998.
[15] S. Chikazumi, Physics of Ferromagnetism.
Oxford University Press,
1997.
[16] I. Villar, U. Viscarret, I. Etxeberria-Otadui, and A. Rufer, "Global loss
evaluation methods for nonsinusoidally fed medium-frequency power
transformers," IEEE Transactions on Industrial Electronics, vol. 56,
pp. 4132-4140, Oct. 2009.
[17] F. Krismer and J. W. Kolar, "Accurate power loss model derivation of a
high-current dual active bridge converter for an automotive application,"
IEEE Transactions on Industrial Electronics, vol. 57, no. 3, pp. 881 -
891, 2010.
1736
