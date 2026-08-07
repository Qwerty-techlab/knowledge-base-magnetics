# source

<!-- FORMULA-WARNING -->
> **Формулы в этом файле недостоверны.** Текстовый слой PDF теряет дробные черты, радикалы и группировку степеней; знак интеграла приходит как `Z` или `R`, знак суммы -- как `P`. Формул вырезано: **24**, читать их в `formulas/` (картинки 300 dpi, перечень в `formulas/INDEX.md`).
<!-- /FORMULA-WARNING -->

> Автоматически извлечено из `source.pdf` скриптом `parse_pdf.py`
> Движок: pymupdf. Страниц: 17 из 17.
> Дата извлечения: 2026-08-07 06:43 UTC

Текст не редактировался. Формулы и таблицы могут быть искажены —
при сомнении сверяться с исходным PDF.

---

## [стр. 1]

General rights
Copyright and moral rights for the publications made accessible in the public portal are retained by the authors and/or other copyright
owners and it is a condition of accessing publications that users recognise and abide by the legal requirements associated with these rights.

 Users may download and print one copy of any publication from the public portal for the purpose of private study or research.
 You may not further distribute the material or use it for any profit-making activity or commercial gain
 You may freely distribute the URL identifying the publication in the public portal

If you believe that this document breaches copyright please contact us providing details, and we will remove access to the work immediately
and investigate your claim.





Downloaded from orbit.dtu.dk on: Jul 30, 2026
Investigation and Modeling of DC Bias Impact on Core Losses at High Frequency
Sanusi, Bima Nugraha; Zambach, Mathias; Frandsen, Cathrine; Beleggia, Marco; Jørgensen, Anders;
Ouyang, Ziwei
Published in:
IEEE Transactions on Power Electronics
Link to article, DOI:
10.1109/TPEL.2023.3249106
Publication date:
2023
Document Version
Peer reviewed version
Link back to DTU Orbit
Citation (APA):
Sanusi, B. N., Zambach, M., Frandsen, C., Beleggia, M., Jørgensen, A., & Ouyang, Z. (2023). Investigation and
Modeling of DC Bias Impact on Core Losses at High Frequency. IEEE Transactions on Power Electronics, 38(6),
7444 - 7458. https://doi.org/10.1109/TPEL.2023.3249106

## [стр. 2]

1
Investigation and Modeling of DC Bias Impact on
Core Losses at High Frequency
Bima Nugraha Sanusi, Student Member, IEEE, Mathias Zambach, Cathrine Frandsen, Marco Beleggia,
Anders Jørgensen, and Ziwei Ouyang, Senior Member, IEEE
Abstract-This paper aims to study the core losses behavior at high frequency (MHz range) with superimposed DC
bias in ferrite. Inductive compensation method is employed
in the measurement circuit to reduce sensitivity to phase
errors. An addition to the circuit is proposed in this work
to make easier DC bias generation. Furthermore, a detailed
measurement accuracy consideration is also discussed. The
tested MnZn ferrite has a nominal relative permeability
of 1500 and 800, which was tested at frequency from 500
kHz to 3 MHz. The measurement results are explained
thoroughly with three controlling parameters: excitation
frequency, peak AC flux density, and DC bias. There
are several important findings. First, a higher DC bias
creates higher losses at the same frequency and AC flux
density. Secondly, at the same DC bias and AC flux
density, higher frequency generates a lower relative losses
increase. This second point has not been seen in previous
literature and is elaborated more in Section III.B. Thirdly,
the measurement result shows how DC bias increases the
hysteresis loop area and coercivity. The first and third
findings confirm the the existing literature findings. As a
final step, an improved Steinmetz Premagnetization Graph
and Artificial Neural Network are used to create core loss
prediction model. The measurement data and the built
model can be accessed online for use by other magnetics
designer.
Index Terms-core losses, core losses measurement, core losses
modeling, DC bias, high frequency
I. INTRODUCTION
It is increasingly necessary to know core losses with reasonable accuracy in the intended application. This is to avoid
overheating on the one hand and oversizing on the other. There
are two steps in understanding the core losses. The first is
measuring the core losses to know the behaviour of the core.
The second is modeling the core losses to predict what losses
are going to occur under a certain condition. The designer
may skip the first step by relying on the published core losses
B. N. Sanusi and Z. Ouyang are with the Department of Electrical
Engineering, Danmarks Tekniske Universitet, Kgs. Lyngby, 2800, Denmark.
M. Zambach and C. Frandsen are with DTU Physics. M. Beleggia and A.
Jørgensen are with DTU Nanolab. A part of this manuscript was presented at
the APEC 2022 and EPE 2022 conference. This work was supported by Danmarks Frie Forskningsfond Project under Grant 9041-00231B. (Corresponding
Author: Ziwei Ouyang, ziou@dtu.dk)
The online dataset is available on https://dx.doi.org/10.21227/7khj-bd03
Manuscript received Month DD, 2022; revised Month DD, 2022.
data from the manufacturer. However, the intended application
may have different core geometry, excitation waveform, and
operating condition than the published data. This will have an
impact on the core losses prediction accuracy. The modeling
stage aims to predict the core losses based on a set of measurement data. With accurate measurement and modeling, the
designer can find the optimal point in the magnetic component
design.
Magnetism is an inherently quantum mechanical property of matter [1]. It makes the core losses mechanism in
magnetic material very complex. Design engineers normally
acknowledge two main sources of core losses: hysteresis loss
and eddy current loss [2], [3]. One can calculate hysteresis losses by minimizing the magnetic energy of a system
with magnetocrystalline anisotropy under the influence of an
applied field [1]. However, the manufacturing process alters
the shape and microscopic structure of a magnetic core [4],
thereby influencing the hysteresis behavior and complicating
the problem significantly. Eddy current loss can be seen at
two levels. Firstly, at the bulk level, eddy currents will form
to counter the magnetic flux through the core cross section.
Secondly, at the grain level, the nonuniform magnetization
creates eddy current around the domain walls. The grain level
phenomenon is also called excess eddy current losses [5], [6].
There are numerous ways to model the magnetic core losses.
They can be classified as the following.
• Hysteresis loop based: the dissipated energy per cycle is
determined from the hysteresis loop area. The Preisach
[7], [8] and Jiles-Atherton models are examples of this.
The approach is accurate but requires many parameters
and accurate hysteresis loop measurement.
• Steinmetz Equation (SE) [9] based: core losses per volume is modeled by the power equation. From there stems
various models [10]-[14], which attempt to improve the
loss prediction accuracy under different excitation.
• Loss map based: core losses are obtained by interpolation
of measurement results data. The loss map can accommodate different flux density, frequency, etc. The examples
are given in [15], [16]. The approach is practical but relies
heavily on measurement data.
• Loss separation based: the total power losses are constructed by calculating separately the hysteresis loss and
eddy current loss and summing them. The calculation
uses basic core geometry and material properties, such
as conductivity and coercivity. This approach was demonstrated in [3], [17]. It is useful when extensive measurement data is not available.
This article has been accepted for publication in IEEE Transactions on Power Electronics. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/TPEL.2023.3249106
© 2023 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission.

See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Danmarks Tekniske Informationscenter. Downloaded on March 03,2023 at 04:10:17 UTC from IEEE Xplore.  Restrictions apply.

## [стр. 3]

2
The SE based model is the most adopted approach by magnetics designer. This is due to the practicality of power formulae.
However, measurement data is necessary for this approach.
Core loss measurement techniques can be classified into
calorimetric and electric method. Calorimetric method works
based on the energy conservation law. The core losses creates
heat. The heat is measured in the form of temperature rise.
From temperature rise and thermal properties, the core losses
can be estimated. This method is well known. A recent work
[18] uses the transient principle to reduce measurement time.
The major drawback of this method is the difficulty to separate
winding loss. The electric method can avoid this drawback. It
works by measuring the induced voltage and excitation current. The induced voltage measurement automatically excludes
the winding losses. Therefore, this method is chosen in this
paper.
Methods such as [12], [13], [19] can be used to predict
core losses with any excitation waveform. However, their
validity needs to be re-investigated. Those models work under
the assumption of non-changing Steinmetz parameters. Unfortunately, the Steinmetz parameters can change at higher
frequency [20], [21] or in the presence of DC bias [22]-[24].
Figure 1 shows the change in magnetic core temperature when
DC bias flux is applied. There is also a missing experimental
verification for core losses under square wave excitation at
higher frequency. Recent reports in [18], [25] measure losses
only under sine wave excitation. The authors in [26]-[29]
measure losses with square wave excitation only up to 500
kHz. Therefore, this paper aims to provide more insight to
core losses by providing comprehensive measurement results
and analysis in the frequency range and magnetic materials
which have not been presented before.
The focus of the present work is to investigate magnetic
core losses under square wave excitation with DC bias. The
frequency of interest is up to 3 MHz. The DC bias impact
will be quantified and the current core losses model will be
extended or modified to incorporate the impact. Behaviour
in different core material is also investigated. Through the
end, we will see if the current losses model still matches
experimental measurement. The parameter shift, if there's any,
will also be analyzed.
Fig. 1: Magnetic core temperature comparison: without DC bias (left)
and with DC bias (right). The spot temperature is capturing the core
temperature, while the box temperature is showing the current sense
resistor temperature.
II. CORE LOSSES MEASUREMENT SETUP
A. Measurement Principle
The main difficulty in measuring core losses with electric
method is that ferrites generally have low losses compared to
the stored energy. This creates the phase angle ϕ between
vDUT and i (indicated in Fig. 2) close to 90◦, since the
impedance of magnetizing inductor Lm,DUT is much smaller
than the equivalent core loss resistance RFe,DUT. The relative
power error caused by the phase discrepancy ∆ϕ for sinusoidal
excitation is given by Eqn. 1, which was derived in [30]. It is
virtually impossible to eliminate ∆ϕ in an actual measurement
setup. Therefore, a more effective solution to limit the power
error is to control tan(ϕ).

∆P
P
 = |tan(ϕ)| · |∆ϕ|
(1)
The mutual inductance neutralization [31] or inductive cancellation [26] technique can bring tan(ϕ) to a more feasible
region. However, this method requires a very accurate compensating inductance or capacitance. This is not easy to design.
A more recent improvement of this cancellation concept [27]
allows a less strict compensation requirement. This is called
partial cancellation concept and is done by introducing the
cancellation factor k, which will be explained below. The same
concept is adopted in this work but with the addition of DC
bias injection.
The core losses measurement circuit is shown in Fig.2. Rp
and Lp represent the winding resistance and stray inductance,
respectively, on the primary side. On the secondary side,
they are represented by Rs and Ls. Lm is the magnetizing
inductance. A DC blocking capacitance CDC is necessary to
avoid saturation in the magnetic core. Current sensing is done
by measuring voltage across the resistor Rsense. However,
due to component non-ideality, a parasitic inductance Lsense
will also be present. Parasitic capacitances from measurement
devices are shown by Cdiff.
Although having low winding resistance and stray inductance (Rp,Lp,Rs,Ls) is desirable, it should not affect measurement accuracy, since the electrical method will exclude
the voltage drop on these elements. High winding resistance
and stray inductance on the primary side may limit the circuit
operation due to their voltage drop, rendering a higher input
voltage requirement to get the desired ˆB excitation. On the
secondary side, Rs and Ls will create extra voltage drop if
the current flowing is non-negligible. The Rs in particular will
create the error due to non-zero average power. Therefore, it
should be kept as low as possible. More details is given in the
next subsection.
As the focus of this work is core loss under square wave
excitation with DC bias, a half bridge circuit is used to
generate the excitation. With a symmetric 50 % duty cycle in
the half bridge, Vin/2 will appear at CDC. Then, a controllable
DC current source (such as [32]) is placed in parallel to CDC
to generate the DC bias. The DC current IDC will flow on top
of the AC component, creating HDC excitation in the magnetic
core. It is important to use an isolated DC current source here
because CDC nodes are floating. In terms of sequence, the DC
This article has been accepted for publication in IEEE Transactions on Power Electronics. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/TPEL.2023.3249106
© 2023 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission.

See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Danmarks Tekniske Informationscenter. Downloaded on March 03,2023 at 04:10:17 UTC from IEEE Xplore.  Restrictions apply.

## [стр. 4]

3
current is turned on after the AC excitation has reached steady
state, in this case 1 ms is the interval between half bridge turn
on and the DC turn on. Afterwards, 100 ms interval is given
before any measurement is acquired, to make sure the DC bias
and AC excitation have reached steady state. The sequence is
the repeated for every measured operating point.
In principle, the compensation element (reference in Fig.
2) must be chosen to have magnetizing inductance Lm,ref as
close as possible to Lm,DUT, and much lower core losses
compared to the DUT. However, when measuring low losses
core, it is difficult to find a magnetic core with much negligible
core losses, compared to DUT. Therefore, we chose to make
the reference element by air core inductor which does not
have core losses, hence no parallel resistance to Lm,ref. A
photo of the real life implementation is given in Appendix A.
Meanwhile, for the mismatching Lm, the cancellation factor
in Eqn. 3 will compensate for it when calculating the loss
in Eqn. 2. Therefore, an exact matching between Lm,ref and
Lm,DUT is not necessary.
Based on the measurement circuit, the core losses can be
calculated by Eqn. 2, where Tsw is the switching period.
For a square wave excitation, the cancellation factor k is
calculated by Eqn. 3, where Vref,pp is the peak-to-peak value
of reference element induced voltage (vref), and VDUT,pp is
the peak-to-peak value of DUT induced voltage (vDUT). This
factor represents the percentage of cancelled reactive voltage
to the total reactive voltage. Alternatively, it can be seen that
the partial cancellation mechanism creates a virtual voltage
vcomp = vDUT -vref/k to replace the initial vDUT. As a
result, the phase shift between vcomp and measured current
(imeas) can be kept minimum, even when the reference element
value Lm,ref has a mismatch with Lm,DUT. Therefore, the
measurement error can be minimized.
PFe =
1
Tsw
 Z Tsw
0
vDUT · imeas dt -1
k
Z Tsw
0
vref · imeas dt
!
(2)
k = Vref,pp
VDUT,pp
(3)
B. Voltage Measurement
Differential voltage probes are used for the voltage measurement because of the floating measurement position. We
chose 25 MHz active differential probe from Testec [33]. An
additional benefit of the differential probe is the low parasitic
capacitance. In this case, it has an equivalent capacitance of
2.75 pF, which is lower compared to 10 pF of common passive
probes. One typical drawback is the measurement delay and
rise time. Therefore, the differential probes are calibrated
to generate identical waveform as measured by a 200 MHz
passive probe, before any measurements are performed. A
comparison of the waveforms is shown in Fig. 3. The postprocessing step will compensate the time delay based on the
calibration data, hence minimizing the voltage reading error.
Voltage measurements (vref and vDUT) are influenced by
the parasitic capacitances. In the DUT, intra and inter-winding
capacitances are minimized by using only 1 turn for primary
and secondary winding, and keeping enough distance between
both windings. This effort is shown in the photos in Appendix
A. Therefore, DUT's parasitic capacitances can be neglected
in this work. The reference air core needs more winding
turns and closer distance between primary and secondary. It
makes the parasitic capacitances non-negligible. In particular,
Cw,ref and Cs,ref will influence the voltage reading. Those
capacitances cause extra current flow which makes a voltage
drop on secondary Rs,ref. This voltage drop is included in the
voltage measurement and will affect the power calculation.
The work in [27], which introduces the partial cancellation
concept, did not provide a clear derivation and calculation
of the error caused by those parasitic elements. Therefore,
this work also tried to complete the error analysis. The full
derivation of measurement error factor (∆P/P) is presented
in Appendix B. To estimate the error, the main and parasitic
component values in Fig. 2 need to be defined. Most of them
are tied to the hardware, therefore will be constant, except
RFe,DUT which changes with the operating points, since it
represents the core losses. This value can be calculated by
Eqn. 4 where VDUT,rms is the rms voltage of DUT and PFe is the
calculated core losses. The assumed worst case values of the
relevant parameters are listed in Tab. I. These values will create
an overestimation of the error because they combine the worst
cases which may not happen at the same time. For example,
RFe,DUT ≈250Ωat 1 MHz 10 mT excitation, and lower at
higher frequency, but the same value is used to calculate error
at 5 MHz. In Tab. I the values represent the extreme cases,
which may not be touched in this experiment. Nevertheless, it
shows the robustness of this method with regards to parasitic
capacitances.
RFe,DUT = V 2
DUT,rms
PFe
(4)
The expected error results are given in Fig. 4 - 6 for three
different source of parasitic capacitances. When calculating the
effect of one capacitance, the others are kept at their nominal
value, given in Tab. I. There is a linear relationship between the
capacitance value and the error percentage. It can be seen that
the inter-winding capacitance Cw,ref brings the highest error
to measurement. Nevertheless, the expected total error is still
less than 5%.
TABLE I: Nominal parasitic components value considered for error
calculation
Parameters
Value
Cdiff,nom
2.75 pF
Cw,ref,nom
50 pF
Cp,ref,nom,Cs,ref,nom
10 pF
Rp,ref,Rs,ref
200 mΩ
Lp,ref,Ls,ref
80 nH
Rp,DUT,Rs,DUT
100 mΩ
Lp,DUT,Ls,DUT
40 nH
Lm,DUT
500 nH
RFe,DUT
2000 Ω
ω
2 · π · [1...5] MHz
k
[0.7...0.8]
This article has been accepted for publication in IEEE Transactions on Power Electronics. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/TPEL.2023.3249106
© 2023 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission.

See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Danmarks Tekniske Informationscenter. Downloaded on March 03,2023 at 04:10:17 UTC from IEEE Xplore.  Restrictions apply.

## [стр. 5]

4
Fig. 2: Electrical circuit of the core losses measurement system. DUT means the magnetic device under test and ref means the reference
or compensation element. Magnetic core losses is represented by RFe,DUT
Fig. 3: Voltage measurement comparison: passive probe (reference)
and two differential probes. About 10 ns time delay is observed while
the gradient is identical.
Fig. 4: Error of PFe measurement as a function of the probe
capacitance (Cdiff)
Fig. 5: Error of PFe measurement as a function of the intra-winding
capacitance (Cp and Cs). Symmetry is assumed between primary and
secondary.
Fig. 6: Error of PFe measurement as a function of the inter-winding
capacitance (Cw,ref)
C. Current Measurement
Current sensing is a critical part of the measurement system.
Shunt resistor is chosen over current probe such as [34] mainly
due to the DC current measuring capability and bandwidth
requirement. The shunt resistor needs to have high precision
with low stray inductance. Metal foil chip resistor from
Susumu PRL series is used in this work. The shunt resistor
This article has been accepted for publication in IEEE Transactions on Power Electronics. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/TPEL.2023.3249106
© 2023 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission.

See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Danmarks Tekniske Informationscenter. Downloaded on March 03,2023 at 04:10:17 UTC from IEEE Xplore.  Restrictions apply.

## [стр. 6]

5
has Rsense = 0.1 Ωand Lsense = 1 nH as the nominal values,
which is shown in Fig. 7. In this work's frequency of interest
range (500 kHz - 3 MHz) the deviation of Rsense and Lsense
from the nominal value is less than 10 %. The shunt voltage
is measured by the voltage probe, which brings the parasitic
capacitance Cprobe. Its nominal value is 9.5 pF for the RTZP10 from Rohde & Schwarz [35], which is used in this
work. Passive probe can be used because the negative side
is connected to ground. In addition, it provides high enough
bandwidth, which is 200 MHz in this case.
The last step in current measurement is to transform the
measured voltage into current. The stray inductance Lsense
and voltage probe capacitance Cprobe make the transformation
less straightforward. The measured voltage vcurrent needs to be
filtered by transfer function as shown in Eqn. 5. The difference
in measured voltage and calculated current is shown in Fig. 8.
It can be seen that almost zero current is flowing through
Cprobe. Meanwhile, there is a small phase shift between the
voltage measurement (vcurrent) and the real current (itotal).
Hence, this approach anticipates the phase discrepancy brought
by the shunt stray inductance, if we use the post-processed
itotal in calculating the core losses.
i(s) = vcurrent(s)

1
s · Lsense + Rsense
+ s · Cprobe

(5)
Fig. 7: Current shunt equivalent resistance and inductance
Fig. 8: Current measurement comparison: directly measured voltage
and calculated current
D. Other Accuracy Consideration
Several other sources of error that can affect the measurement are also listed below.
• Oscilloscope time resolution limit: a 0.1 ns resolution
means an uncertainty of 0.108◦at 3 MHz frequency.
Assuming tan(ϕ) = 1 and using Eqn. 1, this translates
to power error of 0.19 % .
• Oscilloscope vertical (ADC) resolution: an 8 bit ADC
is used in this work. When capturing the waveform, the
vertical scale should be adjusted to make the waveform
cover more than 75% of vertical window (10 divisions),
hence maximizing ADC resolution usage.
• Core temperature is assumed to be at room temperature
(25◦C - 30◦C). This is ensured by short excitation period
(100 ms) and enough interval between measurement
points, e.g 10 s. Hence, core losses variation due to
changing core temperature is avoided.
• Current shunt resistance drift: the shunt resistor [36] has
a temperature coefficient of ±50 ppm / ◦C. This means
that a 100◦C temperature increase will shift resistance by
5 mΩ, which translates to 0.5% error for Rsense = 0.1 Ω.
E. Setup Verification
The setup is verified by testing toroid core under sine wave
excitation. This is done by replacing the DC source and halfbridge circuit with a power amplifier which is controlled
by a signal generator. Then, the measurement results are
compared with datasheet values. The measured cores are PC50
R22.1/13.7/7.9 and PC200 R15.8/8.9/4.7 from TDK. Fig. 9
shows the comparison result. The measurement point is given
together with its uncertainty range, which is derived from 10
measurement captures.
Measurement results match the datasheet values up to 1
MHz for PC50 material. However, for PC200 material, there
is a discrepancy and the measurement gives higher losses than
datasheet values. This discrepancy can happen in real practice
[37], [38], especially as the frequency goes higher. There can
be two reasons for this. First, the material production tolerance,
like the permeability level, can have up to 25% difference
which affect the core loss too. The second is how the datasheet
values are generated. In the industry, the B-H analyzer from
[39] is often used to measure core loss to fulfill IEC6204443 standard. The SY-8219 variant of the machine is generally
not very precise for measurement above 1 MHz. Furthermore,
this equipment normally does not have compensation element,
like in this paper, which makes measurement sensitive to phase
delay errors. Nevertheless, the analysis of core loss behavior in
the next sections will be based on the results from the current
setup, not the datasheet value. Hence, having the same zero
reference for the analysis. The discrepancy shown here should
not change the behavior analysis result.
F. System Architecture
The final step in setting up the measurement system is to
make the test automation. The benefit of automation is not
only reducing the manual labor, but also ensuring the measurement repeatability. The measurement system architecture
This article has been accepted for publication in IEEE Transactions on Power Electronics. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/TPEL.2023.3249106
© 2023 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission.

See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Danmarks Tekniske Informationscenter. Downloaded on March 03,2023 at 04:10:17 UTC from IEEE Xplore.  Restrictions apply.

## [стр. 7]

6
Fig. 9: Comparison between datasheet values and measurement
results with sinusoid excitation. Crosses with error bars demonstrate
measurement results, and lines demonstrate datasheet values. Different materials and frequency are represented by different colors.
is shown in Fig. 10. The circuit block in the middle is detailed
previously in Fig. 2. The PC runs a Python program which
controls the measurement sequence. The measured waveforms
from oscilloscope are then sent back to the PC to be processed.
Signal
Generator
Oscilliscope
DC
Supply
PC
DC
Load
Fig. 10: Architecture of losses measurement system. Blue lines show
commands, while green lines show measurement data flow.
III. EXPERIMENTAL INVESTIGATION
This work aims at measuring and analyzing core losses
under square wave excitation from frequency of 500 kHz up
to 3 MHz. The frequency range is motivated by state-of-theart commercially available MnZn ferrite for power electronics
application [40]-[42]. The measurements were performed on
two magnetic cores with different relative permeability (µr)
level. They are listed in Tab. II along with their detailed properties. Ve, Ae, and le mean the magnetic core volume, effective
cross section, and mean magnetic path length, respectively.
The complete measured inductance values are presented in
Appendix A.
The measurement setup was discussed in the previous
section and, in the end Eqn. 2 and Eqn. 3 are used to calculate
the core losses. The magnetic flux density (BDUT) is defined
in Fig. 11 and can be calculated using Eqn. 6 for the AC
component and Eqn. 7 - Eqn. 8 for the DC component. Nexc
means the number of turns of excitation winding in the DUT
and Ns means the number of turns of sensing winding in the
DUT. vDUT(t) is the measured induced voltage on DUT. Care
must be taken when calculating Eqn. 3, due to the voltage
overshoot at the edge of square wave. The voltage value at
the steady-state (flat) area of square wave should be used to
calculate the cancellation factor in Eqn. 3. The voltage spike
in Fig. 11 is caused by the parasitic capacitance of the sensing
winding and voltage probe. It can influence the measurement
result, but, as shown in subsection II-B, the added error should
be minimum.
Furthermore, it should be acknowledged that Eqn. 7 may not
hold true at all condition. This is due to the hysteretic properties of magnetic materials [43], which makes BDC(HDC) also
depends on ˆB. However, if it is assumed that the material in
this work operates in the linear region, Eqn. 7 can still be used.
Whenever in doubt, the B to H conversion factor is given in
all figures so readers can compare directly in HDC.
BDUT(t) =
1
Ns · Ae
Z t
0
vDUT(t) dt
(6)
BDC = µ0 · µr · HDC
(7)
HDC = Nexc · IDC
le
(8)
Fig. 11: Sensed DUT voltage (vDUT) and the calculated flux density
(BDUT). This example is taken from core sample B at 1 MHz
switching frequency
TABLE II: Core Under Test
Parameters
Core A
Core B
Core Material
PC50
PC200
Core Geometry
R 22.1/13.7/7.9
ER 14.5/6
Ve
1763 mm3
334 mm3
Ae
32.6 mm2
17.6 mm2
le
54.2 mm
19 mm
Initial µr
1500
800
Bsat at 25◦C
490 mT
480 mT
Intended fsw
0.3 - 1 Mhz
1 - 3 Mhz
A. DC Bias Impact on Loss Curve
The first step to understand the effect of DC bias is to look
at the loss curve. Fig. 12 and Fig. 13 show the losses density
against peak AC flux density ( ˆB) for core A and B, while
Fig. 14 and Fig. 15 show the losses density against switching frequency (fsw). The diamond points in the figures are
measurement points while the line is the result of regression.
This article has been accepted for publication in IEEE Transactions on Power Electronics. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/TPEL.2023.3249106
© 2023 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission.

See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Danmarks Tekniske Informationscenter. Downloaded on March 03,2023 at 04:10:17 UTC from IEEE Xplore.  Restrictions apply.

## [стр. 8]

7
Fig. 12: Core losses density (Pv) versus flux density ( ˆB) measured
on test core A with different DC flux bias (BDC) and frequency. 1
mT of BDC translates to 0.53 A/m of HDC
Fig. 13: Core losses (Pv) versus flux density ( ˆB) measured on test
core B with different DC flux bias (BDC) and frequency. 1 mT of
BDC translates to 0.99 A/m of HDC
The influence of DC bias (BDC) on Pv vs ˆB can be seen
in Fig. 12 and Fig. 13. At low DC bias the losses increase is
relatively small. However, after the DC bias reaches a certain
value, the losses increase starts to be significant. For example,
at 500 kHz and ˆB = 50mT in core A the losses increase at
33 mT bias is only 5.3 % but, at 62 mT bias the increase
becomes 20 % and at 94 mT 51.4 %. For core B at 1 MHz
and ˆB = 50mT the trend is similar but at a different level.
With 25 mT bias, the increase is 15.1 % but with 79 mT it
becomes 75 %.
At a single frequency, the measured losses points still follow
a straight regression line in logarithmic scale, even after DC
bias is applied. This suggests that Pv ∝ˆBβ relation still hold
with DC bias. It is also observed that there is a slight shift
in the regression line slope. This may suggest a shift in the
β parameter. We also see this slope shift is less pronounced
in core B, compared to core A. A more detailed modeling is
presented in section IV.
Fig. 14 and Fig. 15 show the influence of DC bias (BDC) on
Pv vs fsw curve. A similar observation can be found where,
again, as the DC bias increases, the loss density also increases.
For test core A, the DC bias seems to offset the loss density
curve, as can be seen in Fig. 14. Although not very obvious,
Fig. 14: Core losses (Pv) versus operating (switching) frequency (fsw)
measured on test core A with different DC flux bias (BDC) and AC
peak flux density ( ˆB). 1 mT of BDC translates to 0.53 A/m of HDC.
Fig. 15: Core losses (Pv) versus operating (switching) frequency (fsw)
measured on test core B with different DC flux bias (BDC) and AC
peak flux density ( ˆB). 1 mT of BDC translates to 0.99 A/m of HDC
we can also observe the Pv ∝f α
sw relation. The shift in α
parameter is not likely for core A, since the curve gradient
stays almost the same. Meanwhile for core B, the measurement
result suggest a shift in the α parameter. The reason is that
the DC bias not only offsets the curve, but also changes the
regression line slope in Fig. 15. At fsw > 2MHz, the DC bias
effect becomes less predictable in core B. At 3 MHz, the loss
increase is almost unnoticeable. This can be caused by the
newfound characteristic of the magnetic core, which will be
elaborated in the next section.
B. Relative Core Losses Increase
This subsection will try to answer when the DC bias starts
to have significant effect to the core losses. It is also chosen
to quantify the DC bias using B field instead of H field.
This selection enables magnetic core performance comparison
across different permeability value. Although, at the beginning
of this section it was noted that Throughout this subsection, the
relative core losses increase (Pv,rel) is calculated by dividing
the losses at a certain DC bias with the losses at no bias
condition, as shown in Eqn. 9.
This article has been accepted for publication in IEEE Transactions on Power Electronics. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/TPEL.2023.3249106
© 2023 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission.

See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Danmarks Tekniske Informationscenter. Downloaded on March 03,2023 at 04:10:17 UTC from IEEE Xplore.  Restrictions apply.

## [стр. 9]

8
Pv,rel = PFe,DC
PFe,0
= EFe,DC(fsw, ˆB, BDC) · fsw
EFe,0(fsw, ˆB) · fsw
(9)
Figure 16 shows for core A when the DC bias impact
becomes significant. The sum of AC and DC component of
B field is taken as the X axis to show if there is a relation
between peak flux density and the relative losses increase.
The increase starts to become significant, i.e. more than 20
%, when the total B is above 100 mT. This can be seen by
looking at the measurement points upper envelope. However,
for BDC < 50 mT, the increase stays low even when the sum
is above 100 mT. It means the DC bias magnitude still plays
a role in determining the increase.
Furthermore, different operating frequency brings different
impact. The higher frequency seems to create lower relative
increase, as can be seen by comparing 1 MHz and 500 kHz
points in Fig. 16. This behavior indicates that EFe,0 and
EFe,DC in Eqn. 9 are a function of frequency too. If it's not,
Pv,rel would show the same value at different frequency. This
is in line with the well known Steinmetz Equation where the
loss Pv ∝f α
sw and α > 1. On the other hand, explaining the
physical origin of this behavior would require deep analysis
into micro-magnetism topic, which is beyond the scope of this
paper.
A similar observation can be found in Fig. 17 where data
points are plotted only against the AC component ˆB. It also
shows that the relative increase (Pv,rel) becomes higher as ˆB
increases, which can be caused by bigger hysteresis loop area
increase at higher ˆB.
In test core B the trend and relationship is less straightforward. Figure 18 shows the relation between total B field
and the relative losses increase. The measurement points are
more widespread than core A. Contrary to core A behaviour,
the relative loss increase is lower as the total flux increases,
for a certain BDC and fsw. This trend applies to all tested
frequency and DC bias for core B. The DC bias magnitude
also determines the relative increase and here the loss gain
is more pronounced, e.g. at 1 MHz the Pv,rel is close to two
when ˆB + BDC is around 100 mT and BDC = 78 mT. This
is a steep increase and designers should take care of it when
designing the magnetic components.
Meanwhile, the impact of frequency is quite similar to
core A. The higher frequency creates a lower relative loss
increase. When data points are plotted only against the AC
component ˆB, Fig. 19 is obtained. It also shows that the
relative increase (Pv,rel) becomes lower as ˆB increases. This
behaviour is different from core A.
The same data in Fig. 18 can also be presented in a different
way as in Fig. 20. The B ratio of AC and DC components
( ˆB/BDC) is plotted against loss increase. This is done to check
if a different characteristics of the core losses can be seen.
Nevertheless, a similar observation is found. The BDC is the
main controlling factor for Pv,rel. The ˆB/BDC ratio plays a
smaller role, although it still has an impact, i.e. higher ratio
makes lower loss increase. This observation reflects a complex
physics behind the core losses phenomenon.
Fig. 16: Relative core losses (Pv,rel) versus peak total flux density
( ˆB + BDC) at different DC bias and frequency for test core A. 1 mT
of BDC translates to 0.53 A/m of HDC.
Fig. 17: Relative core losses (Pv,rel) versus peak AC flux density ( ˆB)
at different DC bias and frequency for test core A. 1 mT of BDC
translates to 0.53 A/m of HDC
Fig. 18: Relative core losses (Pv,rel) versus peak total flux density
( ˆB + BDC) at different DC bias and frequency for test core B. 1 mT
of BDC translates to 0.99 A/m of HDC.
This article has been accepted for publication in IEEE Transactions on Power Electronics. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/TPEL.2023.3249106
© 2023 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission.

See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Danmarks Tekniske Informationscenter. Downloaded on March 03,2023 at 04:10:17 UTC from IEEE Xplore.  Restrictions apply.

## [стр. 10]

9
Fig. 19: Relative core losses (Pv,rel) versus peak AC flux density ( ˆB)
at different DC bias and frequency for test core B. 1 mT of BDC
translates to 0.99 A/m of HDC.
Fig. 20: Relative core losses (Pv,rel) versus flux density ratio ( ˆB/BDC)
at different DC bias and frequency for test core B. 1 mT of BDC
translates to 0.99 A/m of HDC
C. Impact on B-H Curve
Apart from measuring core losses, we can also measure the
magnetic material B-H loop using the same setup. The B field
is calculated using Eqn. 6 from voltage measurement and H
field using Eqn. 8 but with instantaneous current instead of
DC current. The B-H loop area reflects the hysteresis loss
components of a magnetic core. The area equals to the lost
energy per magnetization cycle. Although possible, it is hard to
calculate the hysteresis losses accurately, given the delays and
parasitic in the setup. Hence, the analysis in this subsection is
more of a qualitative nature.
First, we look at the classical behaviour of B-H loop for
different material at changing frequency. Figure 21 and 22
present the loop for core A and B respectively. From literature
and previous works [22], [29], [44], it is expected that the BH loop area increases as frequency increases. This is seen in
both core A and B. In core A the major area increase appears
near the peak B point, both at positive and negative. This is
when the reversal of magnetic domain magnetization begins.
As switching frequency increases, the delay in magnetization
reversal makes the B value falls slower [1], compared to the
switching period. In core B, the situation is similar except
with a slightly different B-H loop shape. The area increase
also appears in core B. On the other hand, core B exhibits
lower coercivity when frequency increases. It is a different
case compared to core A, where the coercivity stays almost the
same at both frequencies. Coercivity can be seen near B ≈0.
Hence, it shows a different behavior of magnetic material with
different relative permeability level.
Secondly, we look at the DC bias impact on B-H loop.
Figure 23 and 24 present the curve change for core A and B
respectively. The first effect is the shift of µr, as can be seen
by the B-H curve slope. For test core A, increasing DC bias
makes µr value lower. Meanwhile, for core B, increasing DC
bias brings the opposite effect. The second effect is the B-H
loop area increase, which leads to the loss increase found in the
previous subsection. The area increase can be observed in two
places. One place is near the magnetization reversal or peak B
point. The second place is found by looking at the coercivity
(Hc). In both Fig. 23 and Fig. 24 we can see the increase
in Hc (equals to ∆H when B = 0). This behaviour can be
explained by the minor loop behaviour of magnetic materials
[45]. Unfortunately, there is not enough literature which can
bridge the magnetism behaviour from the micro to macro level
to explain this thoroughly. Nevertheless, the observation on
B -H loop agrees with the loss increase finding due to added
DC bias.
Area increase
Area increase
Fig. 21: B-H loop at different frequency for test core A. No DC bias
applied.
IV. MODELING DC BIAS ON CORE LOSS
This section does not try to propose a whole new model to
predict core losses. Instead, we will see if the available models
can still accurately predict core losses from the measurement
results generated in this work, particularly this means incorporating the impact of DC bias in core losses prediction. Out
of many previously proposed core losses modeling [8], [10],
[13], [24], [28], the method in [24] and one similar to [46] will
be used in the following analysis. The two methods represent
two different nature of modeling approach. The first one is
This article has been accepted for publication in IEEE Transactions on Power Electronics. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/TPEL.2023.3249106
© 2023 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission.

See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Danmarks Tekniske Informationscenter. Downloaded on March 03,2023 at 04:10:17 UTC from IEEE Xplore.  Restrictions apply.

## [стр. 11]

10
Area increase
Fig. 22: B-H loop at different frequency for test core B. No DC bias
applied.
Fig. 23: B-H loop at different DC bias for test core A. Only the AC
component is plotted.
based more on a traditional formula method with multiple
parameters, while the latter is based more on machine learning
approach.
A. Empirical formula: iGSE with SPG
The main advantage of using analytical formula in modeling
core losses is getting the insight into the physics behind the
losses mechanism. The explicit formula shows the user which
parameters are affecting the core losses. Hence, giving some
understanding of the core losses behaviour.
Since in power electronics the flux (B) waveform is commonly not sinusoidal, the established improved Generalized
Steinmetz Equation (iGSE) method [13] can be adopted to
calculate the core losses. However, this modeling does not
include DC bias effect. Therefore, it needs to be modified
with other techniques. The Steinmetz Premagnetization Graph
Fig. 24: B-H loop at different DC bias for test core B. Only the AC
component is plotted.
(SPG) method [24] can incorporate the DC bias effect without
changing the original equation so, it is used in this work. The
iGSE formula when applied to triangular flux waveform is
reduced to the form in Eqn. 10. Then, with SPG method,
the α, β, and ki will be modified following Eqn. 11 which
incorporates the dependency on DC bias (BDC).
The appropriate coefficients of SPG matrix (first term of
right hand side in Eqn. 11) needs to be found in order to
extract the dependency. This is done by solving a curve fitting
problem. A least square error algorithm has been implemented
that fits the calculated curve with measured data by minimizing
the relative error. Despite the 4th order polynomial used here,
the order can be varied if the curve fitting result does not
generate a good prediction accuracy. In this work, the 4th
order proves to be sufficient. The coefficients in Eqn. 12)
can also be found by curve fitting, but more measurement
data, especially at different frequency, will be needed. This is
because in SPGi method (explained below), the α parameter,
which determines the frequency influence, also changes with
BDC. Common computing software such as Matlab or Octave
has some built-in application to perform the curve fitting task.
Pv,iGSE,tri = ki · (2f)α · (∆B)β
(10)


α
β
ki

=


α0
0
0
0
0
β0
pβ1
pβ2
pβ3
pβ4
ki0
pki1
pki2
pki3
pki4

·


1
BDC
B2
DC
B3
DC
B4
DC


(11)


α
β
ki

=


α0
pα1
pα2
pα3
pα4
β0
pβ1
pβ2
pβ3
pβ4
ki0
pki1
pki2
pki3
pki4

·


1
BDC
B2
DC
B3
DC
B4
DC


(12)
This article has been accepted for publication in IEEE Transactions on Power Electronics. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/TPEL.2023.3249106
© 2023 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission.

See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Danmarks Tekniske Informationscenter. Downloaded on March 03,2023 at 04:10:17 UTC from IEEE Xplore.  Restrictions apply.

## [стр. 12]

11
Following the mentioned procedure, the SPG dependency
graph can be obtained. This is shown in Fig. 25 and Fig. 26 for
core A and B, respectively. The data points are measurement
result and the line is curve-fitting result. For core A, the α
and β parameters stay relatively constant over the whole BDC
range. Meanwhile, ki fluctuates smoothly at low BDC and
increases quite steeply after BDC > 50 mT. This observation
aligns with the analysis in subsection III-B, where the relative
losses gain rises quickly after a certain BDC values.
For core B, the ki increases steadily from low BDC and
shows an almost linear relation to BDC. The β parameters
has a slight decline from low to mid BDC, while α shows
a decreasing trend towards higher BDC. The conventional
SPG prediction cannot capture the α shift because Eqn. 11
assumes a constant α value. This assumption may not hold true
anymore after seeing the measurement result in Fig. 18 and
20. Therefore, a new formulation of SPG matrix can be built
by replacing the zeros in Eqn. 11 with pαi. The new formula
is given in Eqn. 12. With this new modification, a better fitting
for core B will be achieved. This new modification is denoted
as SPGi in Fig. 26 and proven to give more accurate loss
prediction.
After having the SPG coefficients matrix, Eqn. 10 is used
to calculate the core losses in the presence of DC bias.
The results are shown in Fig. 28 and Fig. 29 for core A
and B, respectively, with several different ˆB and fsw values.
The measurement points are also shown to compare the loss
prediction and measurement. The iGSE + SPG method appears
to be reasonably accurate in the whole BDC range for core A.
The accuracy at low ˆB (30 mT) is better than at high ˆB (60
mT) in core A. For core B, this method loses accuracy at high
ˆB and high fsw, as can be seen in Fig. 29. However, with
the proposed SPGi modification, the accuracy is improved.
The maximum error at 2 MHz is reduced from 14% to 6.7%,
while the maximum overall error is down from 25% to 20
%. It's worth to note that this maximum error happens at low
ˆB and fsw value, where a small deviation means higher error
percentage. Meanwhile for core A, the overall maximum error
is only 8.8%.
Fig. 25: Steinmetz Pre-magnetization Graph for test core A. The ki
value is scaled down by 104 to increase graph readability. The data
points are measurement result and the line is curve-fitting result.
SPG
SPGi
Fig. 26: Steinmetz Pre-magnetization Graph for test core B. The ki
value is scaled down by 104 to increase graph readability. The data
points are measurement result and the line is curve-fitting result.
B. Machine Learning: ANN
Artificial Neural Network (ANN) is the most popular
implementation of supervised machine learning methods. It
has the ability to predict values (regression) or categories
(classification) from labeled training data (input-output pairs).
In power electronic systems, ANN has been used for control
strategies [47], [48], fault diagnosis [49], and also component
design [38]. Here, ANN will be used to create a core loss
prediction model. The core loss is nonlinearly co-related to
the excitation frequency, amplitude, and DC bias, which can
be hardly captured by the traditional equation-based methods.
Hence, the ANN is expected to help in this case.
The selected ANN structure is shown in Fig. 27, which
can be classified as Multilayer Perceptron (MLP) type. The
ANN features a two-layer feed-forward network with sigmoid
hidden neurons (in the hidden layer) and linear output neurons
(in the output layer). Since the only output variable in this
problem is the core losses (Pv), only one neuron is in the
output layer. Meanwhile, the number of neurons in the hidden
layer can be tuned. A too low number will make value
prediction not accurate, while a too high number can lead to
overfitting [50]. In this work 10 hidden layer neurons prove
to be sufficient. The network will be trained with LevenbergMarquardt back-propagation algorithm [51], [52] in Matlab
platform. The ANN for core A and B are trained separately,
with 777 measurement samples for core A and 918 samples
for core B. The splitting between the training set and the test
set is 80% and 20% in all cases.
After the ANN is built and trained, it is tested to predict
core losses with arbitrary inputs. The result is plotted in
Fig. 28 and 29 as a curve. The real measurement points
are also plotted to compare it with the ANN prediction. The
test core A prediction by ANN shows a good performance
as can be seen in Fig. 28. At 60 mT and 500 kHz it even
gives a better matching than SPG method. For core B, the
result is less satisfactory. Although the ANN gives better
prediction at 60 mT and 2 MHz, it displays an overfitting
behaviour at 60 mT / 1 MHz and 30 mT / 2 MHz condition.
Nevertheless, the deviation still falls in the reasonable range.
The overall maximum error for core A and B are 27% and
37%, respectively. Again, these maximum errors happen at
This article has been accepted for publication in IEEE Transactions on Power Electronics. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/TPEL.2023.3249106
© 2023 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission.

See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Danmarks Tekniske Informationscenter. Downloaded on March 03,2023 at 04:10:17 UTC from IEEE Xplore.  Restrictions apply.

## [стр. 13]

12
low Pv range where it's sensitive to small deviation. If the 30
mT / 500 kHz and 30 mT / 1 MHz series are excluded, the
overall maximum errors become 11.6% and 10.9% for core A
and B. The average errors when the trained model is tested
with dataset in Fig. 28 and Fig. 29 are 7.2 % for core A and 6.7
% for core B. The ANN shows a rather simple yet powerful
approach to core losses modeling.
Hidden
Layer
Output
Layer
Output
Variables
Input
Variables
Fig. 27: Structure of ANN for core losses estimation with three inputs,
one output, one hidden layer, and one output layer
Measured
ANN Estimated
SPG Estimated
Fig. 28: Core loss density (Pv) estimation of test core A. The scatter
points are measurement data while the curves are prediction result
from SPG method (solid lines) and ANN method (dashed lines).
Measured
ANN Estimated
SPG Estimated
SPGi Estimated
Fig. 29: Core loss density (Pv) estimation of test core B. The scatter
points are measurement data while the curves are prediction result
from SPG method (solid lines) and ANN method (dashed lines).
V. CONCLUSION
This paper investigates magnetic core losses under square
wave excitation with superimposed DC bias. The frequency of
interest is from 500 kHz up to 3 MHz and the tested material is
MnZn ferrite with nominal relative permeability (µr) of 1500
and 800 which are the state-of-the-art for power electronics
application. Chapter II describes the core losses measurement
setup. The mutual inductance neutralization method is used to
minimize the measurement error. The measurement results are
presented in chapter III. The DC bias essentially generates an
offset to the loss curve, creating higher losses. It was also seen
that there is a shift in Steinmetz parameter, especially β, after
bias is applied. Nevertheless, the proportionality Pv ∝ˆBβ
and Pv ∝f α
sw still hold. Chapter IV attempts to model
the core losses behaviour by using two different approach:
Steinmetz Premagnetization Graph (SPG) and Artificial Neural
Network (ANN). The SPG method modifies the Steinmetz
parameter using a polynomial function of the DC bias and the
model has a maximum error percentage of 25% in our test.
With the proposed SPGi modification, this error is brought
down to 20%. Meanwhile, the ANN method relies on neurons
which were trained by the measurement data beforehand. The
ANN model has a maximum error percentage of 37% in
our test. In a nutshell, this paper clarifies ferrite core losses
behaviour in the mentioned frequency range and quantitatively
analyzes the possible models. As a further step, the models
and measurement data can be expanded, as in [46], [53], and
shared to be used with other magnetic designers.
APPENDIX A
MEASUREMENT SETUP AND DUT IMPLEMENTATION
The real life setup of the measurement system is shown
in Fig. 30. A high-frequency GaNFET half-bridge is used as
the square-wave generator. The circuit is able to generate up
to 100 V amplitude at 5 MHz switching frequency. IDC is
implemented using a current controlled DC e-load.
Fig. 30: Implemented core loss measurement setup
This article has been accepted for publication in IEEE Transactions on Power Electronics. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/TPEL.2023.3249106
© 2023 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission.

See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Danmarks Tekniske Informationscenter. Downloaded on March 03,2023 at 04:10:17 UTC from IEEE Xplore.  Restrictions apply.

## [стр. 14]

13
Meanwhile, the DUTs for measurement are shown in
Fig. 31. Single turn windings are used to minimize parasitic
capacitance. The magnetizing and leakage inductance values
are given in Fig. 32 and 33, along with the reference / compensation element's values. This shows the range of inductance
used in this work and justifies the parameters used in error
calculation in Section II-B. The shaded area represents the
range of frequency where the DUT is tested.
Fig. 31: Photos of DUTs: core A (a) and core B (b). The specifications
are given in Tab. II.
Fig. 32: Measured magnetizing and stray inductance of DUT core A
Fig. 33: Measured magnetizing and stray inductance of DUT core B
APPENDIX B
ERROR DUE TO CAPACITANCES
The derivation of errors due to the parasitic capacitances
are given below. The considered circuit is shown in Fig. 34,
which is then simplified to Fig. 35 with part of the equivalent
circuit in Fig. 36. The error is calculated by finding the value
of ∆P. It is based on Pact and Pmeas calculation.
∆P = Pmeas -Pact
Pact
Pact =
1
Tsw
 Z Tsw
0
vFe(t) · iFe(t) dt
!
= 1
2 · Re[VFe · I∗
Fe] = 1
2 · V 2
F e
RFe
Pmeas =
1
Tsw
(
Z Tsw
0
vDUT(t) · i(t) dt1
k
Z Tsw
0
vref(t) · i(t) dt)
= 1
2 · Re[VDUT · I∗] -1
k · 1
2 · Re[Vref · I∗]
The required phasor variables are derived in the following.
VDUT =
1/jωCdiff
1/jωCdiff + jωLs,DUT + Rs,DUT
· VFe
I =
VFe
Zp,DUT
[VDUT · I∗] =
V 2
F e
ωCdiff · Zs,DUT · Zp,DUT
-π/2 -θZs,dut + θZp,dut
k = Lm,ref
Lm,DUT
C2 = Cs + Cd
Z1 = Rp,ref + jωLp,ref
Z2 = Rs,ref + jωLs,ref
Z∆1 = Z1 · Z2 + Z1 · jωLm,ref + Z2 · jωLm,ref
jωLm,ref
Z∆2 = Z1 · Z2 + Z1 · jωLm,ref + Z2 · jωLm,ref
Z2
Z∆3 = Z1 · Z2 + Z1 · jωLm,ref + Z2 · jωLm,ref
Z1
Vref = I ·
Z4 · Z6
Z4 + Z5 + Z6
[Vref · I∗] =
V 2
F e
Z2
p,DUT
·
Z4 · Z6
Z4 + Z5 + Z6
This article has been accepted for publication in IEEE Transactions on Power Electronics. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/TPEL.2023.3249106
© 2023 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission.

See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Danmarks Tekniske Informationscenter. Downloaded on March 03,2023 at 04:10:17 UTC from IEEE Xplore.  Restrictions apply.

## [стр. 15]

14
Fig. 34: Considered circuit for calculating the error caused by the
parasitic capacitance elements
Fig. 35: Considered circuit after the simplification of the reference
elements. Dashed blue boxes show the equivalent impedance definition.
REFERENCES
[1] Stephen Blundell, Magnetism in Condensed Matter, 1st ed. UK: Oxford
University Press, 2014.
[2] E. C. Snelling, Soft Ferrites, Properties and Application, 2nd ed.
England: Butterworths, 1988.
[3] W. Roshen, "Ferrite core loss for power magnetic components design,"
IEEE Transactions on Magnetics, vol. 27, no. 6, 11 1991.
[4] R. M. Bozorth, Ferromagnetism.
IEEE, 1993.
[5] H.
J.
Williams,
W.
Shockley,
and
C.
Kittel,
"Studies
of
the
Propagation Velocity of a Ferromagnetic Domain Boundary," Phys.
Fig. 36: Equivalent circuit of the elements in dashed orange box.
Rev., vol. 80, no. 6, pp. 1090-1094, 12 1950. [Online]. Available:
https://link.aps.org/doi/10.1103/PhysRev.80.1090
[6] G. Bertotti, "General properties of power losses in soft ferromagnetic
materials," IEEE Transactions on Magnetics, vol. 24, no. 1, pp. 621-630,
1988.
[7] I. D. Mayergoyz and G. Friedman, "Generalized Preisach model of
hysteresis," IEEE Transactions on Magnetics, vol. 24, no. 1, pp. 212217, 1988.
[8] I. D. Mayergoyz, "Dynamic Preisach models of hysteresis," IEEE
Transactions on Magnetics, vol. 24, no. 6, pp. 2925-2927, 1988.
[9] C. P. Steinmetz, "On the Law of Hysteresis," Transactions of the
American Institute of Electrical Engineers, vol. IX, no. 1, 1 1892.
[10] M. Albach, T. Durbaum, and A. Brockmeyer, "Calculating core losses in
transformers for arbitrary magnetizing currents a comparison of different
approaches," in PESC Record. 27th Annual IEEE Power Electronics
Specialists Conference.
IEEE, 1996.
[11] J. Reinert, A. Brockmeyer, and R. De Doncker, "Calculation of losses
in ferro- and ferrimagnetic materials based on the modified Steinmetz
equation," IEEE Transactions on Industry Applications, vol. 37, no. 4,
2001.
[12] Jieli Li, T. Abdallah, and C. Sullivan, "Improved calculation of core
loss with nonsinusoidal waveforms," in Conference Record of the 2001
IEEE Industry Applications Conference. 36th IAS Annual Meeting (Cat.
No.01CH37248).
IEEE, 2001.
[13] K. Venkatachalam, C. Sullivan, T. Abdallah, and H. Tacca, "Accurate
prediction of ferrite core loss with nonsinusoidal waveforms using only
Steinmetz parameters," in 2002 IEEE Workshop on Computers in Power
Electronics, 2002. Proceedings.
IEEE, 2002.
[14] J. Muhlethaler, J. Biela, J. W. Kolar, and A. Ecklebe, "Improved
Core-Loss Calculation for Magnetic Components Employed in Power
Electronic Systems," IEEE Transactions on Power Electronics, vol. 27,
no. 2, 2 2012.
[15] T. Shimizu and S. Iyasu, "A Practical Iron Loss Calculation for AC Filter
Inductors Used in PWM Inverters," IEEE Transactions on Industrial
Electronics, vol. 56, no. 7, pp. 2600-2609, 2009.
[16] S. Iyasu, T. Shimizu, and K. Ishii, "A novel iron loss calculation method
on power converters based on dynamic minor loop," in 2005 European
Conference on Power Electronics and Applications, 2005, pp. 9 pp.-
P.10.
[17] W. A. Roshen, "A Practical, Accurate and Very General Core Loss
Model for Nonsinusoidal Waveforms," IEEE Transactions on Power
Electronics, vol. 22, no. 1, pp. 30-40, 2007.
[18] P. Papamanolis, T. Guillod, F. Krismer, and J. W. Kolar, "Transient
Calorimetric Measurement of Ferrite Core Losses up to 50 MHz," IEEE
Transactions on Power Electronics, vol. 36, no. 3, 3 2021.
[19] A. Van den Bossche, V. Valchev, and G. Georgiev, "Measurement
and loss model of ferrites with non-sinusoidal waveforms," in 2004
IEEE 35th Annual Power Electronics Specialists Conference (IEEE Cat.
No.04CH37551).
IEEE, 2004.
[20] W. G. Hurley, T. Merkin, and M. Duffy, "The Performance Factor
for Magnetic Materials Revisited: The Effect of Core Losses on the
Selection of Core Size in Transformers," IEEE Power Electronics
Magazine, vol. 5, no. 3, 9 2018.
[21] B. N. Sanusi and Z. Ouyang, "Magnetic Core Losses under Squarewave Excitation and DC Bias in High Frequency Regime," in 2022
IEEE Applied Power Electronics Conference and Exposition (APEC).
IEEE, 3 2022, pp. 633-639.
[22] A. Brockmeyer, "Experimental evaluation of the influence of DCpremagnetization on the properties of power electronic ferrites," in Proceedings of Applied Power Electronics Conference. APEC '96.
IEEE,
1996.
[23] C. Baguley, B. Carsten, and U. Madawala, "The Effect of DC Bias
Conditions on Ferrite Core Losses," IEEE Transactions on Magnetics,
vol. 44, no. 2, 2 2008.
[24] J. Muhlethaler, J. Biela, J. W. Kolar, and A. Ecklebe, "Core Losses
Under the DC Bias Condition Based on Steinmetz Parameters," IEEE
Transactions on Power Electronics, vol. 27, no. 2, 2 2012.
[25] A. J. Hanson, J. A. Belk, S. Lim, C. R. Sullivan, and D. J. Perreault,
"Measurements and Performance Factor Comparisons of Magnetic Materials at High Frequency," IEEE Transactions on Power Electronics,
vol. 31, no. 11, 11 2016.
[26] M. Mu, Q. Li, D. J. Gilham, F. C. Lee, and K. D. Ngo, "New core
loss measurement method for high-frequency magnetic materials," IEEE
Transactions on Power Electronics, vol. 29, no. 8, pp. 4374-4381, 2014.
[27] D. Hou, M. Mu, F. C. Lee, and Q. Li, "New high-frequency core
loss measurement method with partial cancellation concept," IEEE
This article has been accepted for publication in IEEE Transactions on Power Electronics. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/TPEL.2023.3249106
© 2023 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission.

See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Danmarks Tekniske Informationscenter. Downloaded on March 03,2023 at 04:10:17 UTC from IEEE Xplore.  Restrictions apply.

## [стр. 16]

15
Transactions on Power Electronics, vol. 32, no. 4, pp. 2987-2994, 4
2017.
[28] E. Stenglein and T. Durbaum, "Core Loss Model for Arbitrary Excitations With DC Bias Covering a Wide Frequency Range," IEEE
Transactions on Magnetics, vol. 57, no. 6, 6 2021.
[29] E. Stenglein, M. Albach, and T. Durbaum, "Separation of Magnetic
Flux Density Trajectories into Subloops for the Prediction of Hysteresis
Loss," in 2020 22nd European Conference on Power Electronics and
Applications (EPE'20 ECCE Europe).
IEEE, 9 2020.
[30] F. Dong Tan, J. Vollin, and S. Cuk, "A practical approach for magnetic
core-loss characterization," IEEE Transactions on Power Electronics,
vol. 10, no. 2, 3 1995.
[31] C. Baguley, U. Madawala, and B. Carsten, "A New Technique for Measuring Ferrite Core Loss Under DC Bias Conditions," IEEE Transactions
on Magnetics, vol. 44, no. 11, 11 2008.
[32] L. Itech Electronic Co., "Programmable DC Electronic Load Series
IT8800."
[33] Testec GmbH, "Instruction Manual TT-SI 9001 / TT SI 9002."
[34] Tektronix Inc., "P6022 Current Probe Instruction Manual."
[35] Rohde & Schwarz, "RT-Zxx Standard Passive Probes Specification."
[36] Susumu, "Metal foil low resistance chip resistors - PRL series."
[37] P. Papamanolis, T. Guillod, F. Krismer, and J. W. Kolar, "Minimum Loss
Operation and Optimal Design of High-Frequency Inductors for Defined
Core and Litz Wire," IEEE Open Journal of Power Electronics, vol. 1,
2020.
[38] T. Guillod, P. Papamanolis, and J. W. Kolar, "Artificial Neural Network
(ANN) Based Fast and Accurate Inductor Modeling and Design," IEEE
Open Journal of Power Electronics, vol. 1, 2020.
[39] Iwatsu Electric Co. Ltd., "B - H Analyzer SY-8218 / SY-8219."
[40] Ferroxcube Ltd., "Datasheet: 3F46," 2016.
[41] Hitachi
Metals
Ltd.,
"Soft
Ferrites,"
2020.
[Online].
Available:
http://www.hitachi-metals.co.jp/e/products/elec
[42] TDK Corp., "High-Frequency, Low-Loss Ferrite Material PC200," 2020.
[Online]. Available: https://product.tdk.com/info/en/products/ferrite
[43] E. Stenglein, B. Kohlhepp, D. Kubrich, M. Albach, and T. Durbaum,
"GaN-Half-Bridge for Core Loss Measurements Under Rectangular AC
Voltage and DC Bias of the Magnetic Flux Density," IEEE Transactions
on Instrumentation and Measurement, vol. 69, no. 9, 9 2020.
[44] M. Lancarotte, C. Goldemberg, and A. d. A. Penteado, "Estimation of
FeSi Core Losses Under PWM or DC Bias Ripple Voltage Excitations,"
IEEE Transactions on Energy Conversion, vol. 20, no. 2, 6 2005.
[45] D. Jiles, "A self consistent generalized model for the calculation of
minor loop excursions in the theory of hysteresis," IEEE Transactions
on Magnetics, vol. 28, no. 5, 9 1992.
[46] H. Li, S. R. Lee, M. Luo, C. R. Sullivan, Y. Chen, and M. Chen,
"MagNet: A Machine Learning Framework for Magnetic Core Loss
Modeling," in 2020 IEEE 21st Workshop on Control and Modeling for
Power Electronics (COMPEL).
IEEE, 11 2020.
[47] T. Dragicevic and M. Novak, "Weighting Factor Design in Model
Predictive Control of Power Electronic Converters: An Artificial Neural Network Approach," IEEE Transactions on Industrial Electronics,
vol. 66, no. 11, 11 2019.
[48] Q. Xu, T. Dragicevic, L. Xie, and F. Blaabjerg, "Artificial IntelligenceBased Control Design for Reliable Virtual Synchronous Generators,"
IEEE Transactions on Power Electronics, vol. 36, no. 8, 8 2021.
[49] F. Filippetti, G. Franceschini, C. Tassoni, and P. Vas, "Recent developments of induction motor drives fault diagnosis using AI techniques,"
IEEE Transactions on Industrial Electronics, vol. 47, no. 5, 2000.
[50] S. Skansi, Introduction to Deep Learning: From Logical Calculus to
Artificial Intelligence.
Springer Nature, 2018.
[51] M. Hagan and M. Menhaj, "Training feedforward networks with the
Marquardt algorithm," IEEE Transactions on Neural Networks, vol. 5,
no. 6, 1994.
[52] M. Hagan, H. B. Demuth, M. H. Beale, and O. De Jesus, Neural Network
Design, 2nd ed.
Martin Hagan, 2014.
[53] E. Dogariu, H. Li, D. Serrano Lopez, S. Wang, M. Luo, and M. Chen,
"Transfer Learning Methods for Magnetic Core Loss Modeling," in 2021
IEEE 22nd Workshop on Control and Modelling of Power Electronics
(COMPEL).
IEEE, 11 2021.
Bima Nugraha Sanusi (Student Member, IEEE)
received the B.Sc. degree in electrical engineering
from Bandung Institute of Technology (ITB), Bandung, Indonesia in 2015, and the M.Sc. degree in
electrical engineering and information technology
from the Swiss Federal Institute of Technology
(ETH), Zurich, Switzerland in 2018. He is currently working toward the Ph.D. degree with the
power electronics group at Technical University of
Denmark (DTU), Kongens Lyngby, Denmark. His
current research interests include high frequency
power conversion, integrated magnetics design, magnetic losses measurement
and modeling, and highly compact DC-DC converter. He worked as a model
based system engineer at FPT Motorenforschung AG and research assistant
at High Power Electronics laboratory ETH Zurich in between his education.
Bima was the recipient of ABB Jurgen Dormann Foundation scholarship while
he was with ITB Bandung and received the Master Scholarship Program from
ETH Zurich.
Mathias Zambach received a B.Sc. of Science
degree in Medicine from the Copenhagen University
in 2015 and a B.Sc. of Science degree in Engineering
from the Technical University of Denmark in 2018.
He obtained the M.Sc. of Science in Engineering,
in the field of Physics and Nanotechnology, from
the Technical University of Denmark in 2020 and is
currently working toward the Ph.D. degree with the
Magnetism and Quantum Materials group, Technical
University of Denmark, Kongens Lyngby, Denmark.
He has a broad background in physics and nanotechnology and his current research interests include static and dynamic
susceptibility of magnetic nanoparticles, losses and heating mechanisms
in magnetic nanoparticles, and design of magnetic particles for composite
magnetic materials for high-frequency inductor cores.
Cathrine Frandsen is a professor in the Department
of Physics, Technical University of Denmark (DTU).
Her research interest includes magnetic nanoparticles, magnetization and electron spin investigation.
Marco Beleggia is an associate professor in the
National Centre for Nano-Fabrication and Characterization, Technical University of Denmark (DTU).
His research interest includes Transmission Electron
Microscopy, electron beams, and nanoscale imaging.
This article has been accepted for publication in IEEE Transactions on Power Electronics. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/TPEL.2023.3249106
© 2023 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission.

See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Danmarks Tekniske Informationscenter. Downloaded on March 03,2023 at 04:10:17 UTC from IEEE Xplore.  Restrictions apply.

## [стр. 17]

16
Anders Michael Jørgensen received his M.Sc.
degree from the Technical University of Denmark
in 1998. During the M.Sc. study he spent a year
(1995-1996) at University of Virginia on a Fullbright
scholarship. He received the Ph.D. degree from the
Technical University of Denmark (DTU) Kongens
Lyngby in 2003. He was a Post.Doc. at DTU MIC
between 2003 and 2006, working on advanced microfabrication and multidomain integration. From
2006 to 2009 he worked in two start-up companies
within photovoltaics. In 2009 he joined the core
facility, DTU Nanolab (named DTU Danchip at the time) as Head of Customer
Support and in 2014 he was promoted to Deputy Director, a title he currently
holds. He is the author of more than 30 papers and has contributed to the book
Microsystem Engineering of Lab-on-a-Chip Devices (VCH-Wiley, Weinheim,
2003). He holds 3 international patents. His current research interests are
within advanced micro and nanofabrication and characterization. His work
focuses on establishing new research facilities with specialty cleanrooms and
unique tool sets as part of DTU Nanolab.
Ziwei Ouyang (S'07, M'11, SM'17) received his
PhD degree from Technical University of Denmark
(DTU) in 2011. Since from April 2016, he has been
appointed as an associate professor at DTU. He has
been appionted as head of study in MSc Electrical
Engineering since 2021. His research areas focus
on switch mode power supply, magnetics modeling
and integration, energy storage system, and wireless
charging etc. He is an IEEE senior member. He
has more than 110 high impact IEEE journal and
conference publications, and 9 international patents.
He received 2021 IEEE Transactions on Power Electronics First Place Prize
Paper Award, and several Best Paper Awards in IEEE sponsored international
conferences.
This article has been accepted for publication in IEEE Transactions on Power Electronics. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/TPEL.2023.3249106
© 2023 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission.

See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Danmarks Tekniske Informationscenter. Downloaded on March 03,2023 at 04:10:17 UTC from IEEE Xplore.  Restrictions apply.
