# source

> Автоматически извлечено из `source.pdf` скриптом `parse_pdf.py`
> Движок: pymupdf. Страниц: 13 из 13.
> Дата извлечения: 2026-08-07 06:43 UTC

Текст не редактировался. Формулы и таблицы могут быть искажены —
при сомнении сверяться с исходным PDF.

---

## [стр. 1]

2062
IEEE TRANSACTIONS ON POWER ELECTRONICS, VOL. 23, NO. 4, JULY 2008
Winding Capacitance Cancellation for
Three-Phase EMC Input Filters
Marcelo Lobo Heldwein, Member, IEEE, and Johann W. Kolar, Senior Member, IEEE
Abstract-Techniques have been presented in the literature
for canceling stray capacitances for inductors in single-phase
power filters. With the same aim, the alternatives provided by
three-phase systems are explored here. A thorough theoretical
analysis is presented, where pros and cons of parasitic capacitance cancellation networks are highlighted and improvements
are proposed. A systematic mathematical procedure to evaluate
impedances for different noise modes in three-phase circuits
is presented. The influence of parasitic effects is accessed and
asymmetric capacitance cancellation is proposed, facilitating
applications in switched power circuits. Experimental results are
shown demonstrating the effectiveness of the presented techniques
in an electromagnetic compatibility filtering application.
Index Terms-Parasitic capacitance cancellation, three-phase
power line filters, three-phase networks.
I. INTRODUCTION
D
RIVEN by cost reduction demands, the Power Electronics
industry has a major focus in the miniaturization of power
converters. This means that the same functionality must be guaranteed for electronic systems built within ever smaller spaces,
thus requiring electronic components with very much different
characteristics to cohabit in tightly confined areas [1]. The situation gets more complex because switching frequencies are
steadily increasing, thus higher frequency components are prone
to be observed in the electromagnetic field spectra generated in
the power converters. The results achieved in the last decades
have pushed the limits of available circuit topologies, materials,
components, modulation schemes and control strategies [2], [3].
These results have also compelled design engineers to achieve
a better understanding around the measures to be taken in order
to assure the electromagnetic compatibility (EMC) of such a
system within its electrical environment and inside the system itself (self-compatibility) [4]. As power electronics converters are
known to generate high conducted emission (CE) levels, efforts
in research are being performed to reduce these emissions at
their source, but also through line filters, the interfaces between
power grid and converters [4]-[6]. For high performance power
converter systems, these power filters are mostly low-pass circuits designed based on inductors and capacitors along with
resistors providing passive damping [6], [7]. Although passive
cancellation circuits [8] and active filters circuits [9]-[12] have
Manuscript received May 7, 2007; revised October 17, 2007. Published July 7,
2008 (projected). Recommended for publication by Associate Editor B. Ferreira.
M. L. Heldwein is with the Federal University of Santa Catarina-USFC,
Power Electronics Institute-INEP, Florianópolis 99040-970, Brazil (e-mail:
heldwein@inep.ufsc.br).
The authors are with the Power Electronic Systems Laboratory, Swiss Federal
Institute of Technology (ETH) Zurich, Zurich CH-8092, Switzerland (e-mail:
heldwein@ieee.org; kolar@pes.ee.ethz.ch).
Color versions of one or more of the figures in this paper are available online
at http://ieeexplore.ieee.org.
Digital Object Identifier 10.1109/TPEL.2008.924820
Fig. 1. Three-phase CM inductor illustration with an impedance curve showing
the parasitic parallel capacitance effect on the impedance magnitude for high
frequencies.
been lately also researched and some practical applications have
been reported [12], most of the power filters are still based on
passive elements [5], [6], [13], where inductors play a major role
in increasing series impedance for both, differential (DM) and
common mode (CM) emissions.
Inductors are heavy/bulky components, but are especially
useful in reducing CM currents once the utilization of capacitors between lines and protective earth (PE) is limited due to
earth leakage current limitations given in electric equipment
safety standards (e.g., EN 60950 series). Inductors to be used in
filters have been studied and theoretical models have been proposed [14]-[17]. All of these equivalent circuit models have in
common the connection of a parasitic capacitor in parallel with
the inductor, thus resulting in capacitive impedance beyond the
so-called self-resonance frequency (see Fig. 1). The observed
capacitance is a consequence of the physical arrangement of the
wires/turns (conductors), core body (showing low conductance)
and isolation coating/layers (dielectric). This capacitive behavior is a highly undesirable effect [18] since it might greatly
reduce the attenuation provided by a filter at high frequencies.
This effect gets worst if multiple winding layers are used in
the construction of the inductor [5], [15], [18] and as a result
inductor designs shall be limited to one or at most two layers,
thus reducing available window area occupation and increasing
the required total core material volume. If a planar design is
used the capacitive effect is even more pronounced due to
the wider conductive area in contrast with thinner dielectric
distances between layers [19].
To overcome the challenges imposed by parasitic elements
[18] specifically in the construction of inductors, thorough research is being done to improve magnetic materials [2] and,
lately, in methods to reduce parasitic elements through the use of
different circuit topologies in the filtering networks [19]-[24]. A
term called capacitance cancellation has been created to address
these techniques, which have the practical outcome of eliminating the parasitic capacitance effects observed from a perspective of CM, DM, or both in a filter inside a feasible frequency
0885-8993/$25.00 © 2008 IEEE

## [стр. 2]

HELDWEIN AND KOLAR: WINDING CAPACITANCE CANCELLATION
2063
Fig. 2. Network configurations used in the derivation of the relevant matrices: (a) general three-phase network; (b) configuration used for the definition of CM
impedance, and (c) configuration employed for the DM impedance definition.
range. CE are, in general, regulated up to 30 MHz, both in Europe (EN) and USA (FCC). Therefore, this is an upper bound
frequency, for which a designed inductor should behave as ideal
as possible.
This work aims on analyzing the possibility of applying capacitance cancellation networks to three-phase power line filters, since previous literature on this subject is limited to single
phase topologies, but the utility and costs of three-phase power
converters are prone to justify the utilization of extra components in the filters. Due to the lack of existing tools for the
analysis of three-phase networks, a procedure is presented (see
Section II), which uses the parameters of the networks' admittance matrices
and evaluates relevant impedances for CM
and DM. The derived equations are also employed in the search
for suitable capacitance cancellation networks, where some of
the presented results can be extended to single-phase networks.
Cancellation networks are proposed (see Section III) for threephase inductive networks, where the impact for CM and DM,
of the introduced components, is evaluated and the flexibility
provided by three-phase networks is exploited. A basic study
proposing the possibility of asymmetrical capacitance cancellation is presented in Section IV. Extra measures are taken to
improve the performance of such networks of higher frequencies of the spectrum. These are based on the study of the influence of other parasitic effects, such as non-ideal coupling factors
and winding resistances, which is done theoretically (see Section V) and experimentally as shown in the experimental results
presented in Section VI.
II. THE USE OF ADMITTANCE MATRICES TO ANALYZE
THREE-PHASE NETWORKS FOR EMC
A three-phase network consisting of linear and time invariant
elements, as displayed in Fig. 2(a), is completely defined by one
of its characteristic impedances (
, etc.) [25]. The
admittance matrix
, as defined in
(1)
is especially useful if networks are to be connected in parallel,
because the resulting matrix
of the parallel connection
of two networks defined by
and
is the direct sum of
them,
. Some of the capacitance cancellation
networks can be placed directly in parallel with the network of
inductors and for this reason the admittance matrix is thought
of being well suited for the present analysis, even though any
other form could be used.
The objective of this analysis is to search for equations to
evaluate impedances, which are relevant for the EMC assessment in three-phase circuit networks. That is here achieved by
deriving equivalent impedances from two perspectives, CM and
DM, which are based on the admittance matrix of the threephase network of interest.
A. Derivation of an Ideal CM Impedance
The circuit configuration presented in Fig. 2(b) is used to define the total CM impedance
presented by the network for
an ideal case, where the impedances outside the network are balanced with respect to the reference ground. From the inspection
of the circuit
(2)
where
, and
are the 3
3 square sub-matrices of
. From (2) the individual currents are defined by
(3)
If the network is symmetric, considering the polarities presented in Fig. 2(b), then
and
and
the equivalent CM impedance
presented by the network
can be evaluated through the sum of all elements of the sub-

## [стр. 3]

2064
IEEE TRANSACTIONS ON POWER ELECTRONICS, VOL. 23, NO. 4, JULY 2008
matrix
(4)
B. Derivation of the Ideal Series DM Impedances
Again, for the derivation of ideal DM impedances for the
three-phase network, the impedances outside the network are
considered balanced. The circuit for this derivation is shown in
Fig. 2(c), from where it is seen that three DM voltage sources are
placed in one end of the network while the currents of interest
are in the other end. The idea is to find the transfer impedance
from these variables assuming that the network is balanced.
From the circuit configuration of Fig. 2(c) it follows that:
(5)
From the definition of differential mode voltages, their sum
must equal zero
(6)
There can be infinity possibilities for this sum to hold true. A
general case is here assumed, where
(7)
Three DM impedances
are defined
where
(8)
The general solution for the three DM impedances is
(9)
If the network under consideration is symmetric, it follows
that
and
. Therefore, the DM impedances are
(10)
Fig. 3. Inductor networks with capacitance cancellation as proposed in
[19]-[23]: (a) cancellation relying on magnetic coupling and (b) cancellation
for two inductors not relying in magnetic coupling.
III. CAPACITANCE CANCELLATION FOR THREE-PHASE
INDUCTIVE NETWORKS
The results and analyses presented on this section are based
on some simplifications in the models for the inductors, namely:
1) a first order approximation, i.e., a lumped inductor in parallel
with a lumped capacitor, is adopted for the equivalent circuits,
which is valid in most situations up to 30 MHz; 2) the parallel
resistance is omitted since it plays neglectable role in the capacitance cancellation; 3) the influence of the series resistances is
here neglected; 4) some capacitance cancellation networks rely
on the magnetic coupling between two portions of an inductor's
windings, where a perfect coupling factor
1 is assumed; 5)
the lead inductances are disregarded because they can be seen
in series with the remaining networks, thus their connection can
be performed in a second step, and 6) the networks have balanced impedances. The influence of the series resistance and
the reduction of the coupling factors are studied in Section V.
The adopted simplifications are important in reducing the complexity of the equations and providing useful insight into the
involved phenomena.
Simple capacitance cancellation techniques for single-phase
systems are proposed in [19]-[23], from where a summary is
presented in Fig. 3. It is seen that the equivalent networks are
able to cancel the effects of the parallel connected capacitors
in both cases. Techniques suitable for three-phase networks are
presented in the following.
A. Capacitance Cancellation for Three-Phase CM Inductors
A three-phase CM inductor can be modeled as the six-port
network shown in Fig. 4(a) and for a CM analysis the three
inputs can be shortened as well as the output ports, thus the
six-port device is simplified to a two-port one [see Fig. 4(b)].
The final aim for the capacitance cancellation is that the parallel
capacitors
disappear and an equivalent network as in Fig. 5
results.
The admittance matrix
of the circuit of Fig. 5 is
(11)
In order to simplify the following analysis, an asymmetrical
capacitance cancellation network is employed as derived later
in this section, taking the coupling among different windings in

## [стр. 4]

HELDWEIN AND KOLAR: WINDING CAPACITANCE CANCELLATION
2065
Fig. 4. Three-phase CM inductor networks: (a) model of a three-phase CM
inductor, and; (b) equivalent CM network aiming for finding impedances
Y
(i = 1 . . . 3) that effectively cancel the effects of the parallel capacitors
C
.
Fig. 5. Desired final equivalent network for common mode components.
Fig. 6. Circuits employed for analyzing the impact of the coupling among different windings in a three-phase CM inductor employing the proposed capacitance cancellation technique.
a three-phase CM inductor into account. The objective of this
analysis is to evaluate if this coupling can be neglected for the
analysis of the capacitance cancellation techniques. Thus, the
circuits of Fig. 6 are employed.
Defining the coupling coefficients with
(12)
and an ideal CM impedance as
(13)
leads to the following solution for the circuit of Fig. 6 is (14),
shown at the bottom of the page.
The theoretical considerations were based on ideal coupling
among two halves of each inductor, thus
(15)
and (14) is simplified to
(16)
Equation (16) shows that the resulting impedance depends
on the coupling among different windings
, but does not
include any capacitive effect from the parallel capacitances.
Therefore, capacitance cancellation is achieved for all possible
values of
.
As seen with (14), the consideration of magnetic coupling
among different windings in a three-phase CM inductor leads
to large expressions. Furthermore, in an ideal case, this coupling does not influence the results achieved with the capacitance cancellation networks. For these reasons, the remaining
analysis considers no magnetic coupling among the different
windings. This assumption does not strongly influence the results, since the inter-winding magnetic coupling is reduced for
high frequencies due to lowering permeability of any employed
core material. This consideration is on the safe side since the
higher the coupling amongst the different windings the better
for the capacitance cancellation. An ideal magnetic coupling
1 between the halves of the windings is considered in
order to simplify the equations, but the influence of a non-ideal
coupling is studied in Section V. In order to differentiate the circuits where all inductors are considered coupled, dots are used,
whereas, if the coupling is just within specific inductors, their
coupling is marked with a line.
For a symmetric cancellation network,
and the admittance matrix
for the circuit
of Fig. 4(b) is defined by
(17)
where
(18)
(19)
(14)

## [стр. 5]

2066
IEEE TRANSACTIONS ON POWER ELECTRONICS, VOL. 23, NO. 4, JULY 2008
Fig. 7. Networks that achieve the capacitance cancellation for a three-phase CM inductor (for the equivalence of these networks refer to Appendix I).
The capacitance cancellation is achieved when
, from where:
(20)
Solving (20) for
and
leads to
(21)
This shows that the cancellation network can be achieved with
the series connection of a negative inductance with a value of
3/4
with a capacitor of 4
. The final circuit is illustrated
in Fig. 7, where
4
and
1. This is a very useful
result, since it shows that the inclusion of only three capacitors
(of usually small value) is able to cancel the negative effect of
the parallel capacitances.
For the case that one of the admittances
is set to zero,
for instance only
0, then two capacitors of 6
suffice
for canceling
as shown in
(22)
If two admittances are set to zero, for instance only
0,
then a single capacitor of 12
suffices
(23)
Equations (22) and (23) show that for the CM capacitance
cancellation of an ideal three-winding CM inductor it is not required that the network cancellation is done symmetrically, thus
a single capacitor connected to the center of one winding [see
Fig. 8(a)] might be enough. This effect can also be explained
by inspecting Fig. 8(b), where, for CM currents, the voltage is
the same in all three windings, and if a perfect coupling is assumed, the voltage at the center point of any winding should be
Fig. 8. Networks that provide parasitic capacitance cancellation in a threephase CM inductor: (a) symmetrical network, where C
= 4C
and (b)
single capacitor network.
the exactly the same, therefore the connection of capacitors between any of these points and the electric ground (PE) shall provide the same effect as long as the coupling factors are high and
the external impedances (connected in series with the inductors)
are approximately symmetrical and balanced. This might prove
useful for manufacturing reasons, since only one center point
must be accessed, but attention must be paid if mixed mode
noise [26], [27] is pronounced in the circuit and if the coupling
among the windings is low.
B. Capacitance Cancellation for Three-Phase DM Inductors
A network composed of three DM inductors is an important
building block for three-phase power filters and, unless some
special winding technique is used, three non-coupled inductors
are applied. The simplified model for the six-port network is
shown in Fig. 9. Two ways of achieving capacitance cancellation
for this network are presented in the following.
First Approach-No Magnetic Coupling Required: As the
capacitors and inductors are connected in parallel in the model
of Fig. 9, the inductances can be removed (the final network is
the sum of the admittances of both circuits) and the remaining

## [стр. 6]

HELDWEIN AND KOLAR: WINDING CAPACITANCE CANCELLATION
2067
Fig. 9. Model applied for the analysis of three DM inductors.
Fig. 10. Capacitive networks: (a) parallel capacitances and (b) DM capacitive
cancellation network.
network is built with the connection of capacitors
, as displayed in Fig. 10(a). The admittance matrix of this network
is
(24)
If the network of Fig. 10(b) is used for capacitance cancellation, it is left to know the value of capacitors
. The admittance matrix
of this network is
YX =
2sCdc
0
0
0
 sCdc
 sCdc
0
2sCdc
0
 sCdc
0
 sCdc
0
0
2sCdc
 sCdc
 sCdc
0
0
sCdc
sCdc
 2sCdc
0
0
sCdc
0
sCdc
0
 2sCdc
0
sCdc
sCdc
0
0
0
 2sCdc
:
(25)
And the final admittance matrix
is the sum of both
. As the networks are symmetric, the
DM impedances
can be evaluated from (10) and it follows:
where
(26)
Fig. 11. Final network for DM capacitance cancellation. The connection of
capacitors C
effectively cancels the effect of C
for DM currents, not relying
on magnetic couplings. For CM currents the final capacitance is increased three
fold, being a drawback of this type of network.
The aim of the capacitance cancellation in this case is to
achieve infinite DM impedance. This is fulfilled, by inspecting
(26), if
(27)
An important parameter for the evaluation of the final network is the impedance observed from CM, since the DM inductors have an impact on CM currents as well. The serial CM
impedance can be calculated with (4) leading to
(28)
From (27) and (28) it is seen that, with the inclusion of the six
capacitors
, the parallel capacitance
is cancelled for DM
currents, whereas for CM the final capacitance is increased three
times in value. This is clear from the inspection of Fig. 11, where
the CM analysis can be done by connecting input and output
ports respectively together and the equivalent capacitance is the
sum of all capacitors.
Second Approach-Relying on Magnetic Couplings: If the
inductors
of Fig. 12 are split in two, the same principle
as used in the CM cancellation section can be employed (see
Fig. 7) and the admittances
shall be derived.
The admittance matrix of the network of Fig. 12 is given by
(29)

## [стр. 7]

2068
IEEE TRANSACTIONS ON POWER ELECTRONICS, VOL. 23, NO. 4, JULY 2008
Fig. 12. Network used to find a suitable circuit to implement capacitance cancellation for DM inductors.
Fig. 13. Network to achieve capacitance cancellation for DM inductors used
in three-phase filters based on the magnetic coupling among two halves of each
inductor.
where
(30)
The only element that is desirable for the DM currents is
the inductance
, therefore the desired DM impedance
, evaluated through (10) and (29), is
(31)
Solving the system of equations formed by (29), (30), and
(31) it follows that
(32)
The idea of using a network similar to the one used for the CM
capacitance cancellation also works here. The final network is
presented in Fig. 13, where the capacitors
are added for
canceling the effects of
.
Fig. 14. Second network to achieve capacitance cancellation for DM inductors
used in three-phase filters based on a -configuration of the canceling capacitors.
Fig. 15. (a) Basic principle for symmetric capacitance cancellation and its
equivalent circuit. (b) Inductor applied at the input of a switching cell, where
its parasitic parallel capacitance increases switching losses of the cell.
What is left is the calculation of the impedance observed by
CM currents. This is calculated using (29) and (30) into (4),
leading to
(33)
which is the same impedance seen without the inclusion of the
capacitance cancellation network, therefore this approach does
not decrease the final CM impedance.
In the circuit of Fig. 13 the capacitors
are connected
in a
-configuration. From the
circuit transformation,
it is clear that a
-connection of capacitors with one third of
the value of the
-connected capacitors is fully equivalent to
the
-configuration. Therefore, the circuit of Fig. 14 is derived,
leading to canceling capacitors
defined as
(34)
IV. BRIEF DISCUSSION ON ASYMMETRICAL CANCELLATION
The networks presented in the previous section and in the literature [19]-[23] have as a characteristic that the final equivalent circuit is symmetric, since the connection of the canceling
networks is symmetric as in Fig. 15(a). For the case where the
inductor is used directly at the input of a switching cell [see
Fig. 15(b)], the switches
and
will present switching losses
which are approximately proportional to the parallel capacitance
, thus this capacitance is completely unwanted. If the
symmetrical capacitance cancellation networks are used, the effective parallel capacitance is increased. In fact it is doubled for
the circuit in Fig. 15(a), what means that the switching losses

## [стр. 8]

HELDWEIN AND KOLAR: WINDING CAPACITANCE CANCELLATION
2069
Fig. 16. Networks used to analyze the possibility of asymmetric parasitic capacitance cancellation: (a) proposed cancellation network and (b) desired equivalent circuit.
due to
would else double. This would require special attention of design engineers in the use of the cancellation techniques
and leads to the question: is it possible to implement a cancellation network (asymmetric [21], [29]), which does not increase
the capacitance to be switched?
To start with, the networks presented in Fig. 16 are used,
where the parameters
, and
are left undefined and a
mutual inductance with unitary magnetic coupling factor is considered
. The admittance matrices of the networks are used to derive the values.
The admittance matrix for the circuit in Fig. 16(a)
is
(35)
where
(36)
(37)
and
(38)
The admittance matrix for the circuit in Fig. 16(b)
is
(39)
where
(40)
(41)
(42)
The capacitance cancellation is achieved when
,
resulting in a four linearly independent equations system.
Solving this system leads to
and
(43)
Fig. 17. Normalized total capacitance KC =C required for the cancellation
of C
as a function of K .
Fig. 18. Normalized inductances and turns ratio required for the cancellation
of C
as a function of K .
(44)
For the design of such a network, a value is chosen for
and the other parameters follow. Although, there is a theoretical lower boundary for
, given by
1. This limit, in
practice, means that the original parallel capacitance
can not
be downsized from a perspective of switching losses. The total
amount of capacitance
used in the cancellation circuit has
its minimum at
2 (see Fig. 17), which is the case of symmetric cancellation. This means that for an asymmetric cancellation more capacitance must be used, but it brings the advantage
that the input capacitance
is large, thus providing more
effective filtering.
The implementation of such a technique is more involved,
since the splitting of the inductor is not done at its center point,
but depends strongly in the chosen ratio
. Fig. 18 illustrates
how the inductance must be divided in order to achieve capacitance cancellation, where it becomes clear that if a small
is
desirable, the inductor shall be divided in uneven parts. The required turns ratio
, assuming unitary magnetic coupling,
follows the line
.
V. STUDY ON THE INFLUENCE OF PARASITIC ELEMENTS
The previous sections have assumed close to ideal equivalent
circuits, but as the high frequency behavior of the components is
paramount for EMC, the influence of the main parasitic effects
must be considered. For that, the circuit of Fig. 19 is used, where
the stray resistances of the windings
, a non-ideal magnetic
coupling
and the stray inductance
are considered.
The calculation of the CM impedance is done with (4) and
of the DM impedance with (10), both applied to the admittance
matrix of the network of Fig. 19, which is not displayed due
to space constraints. The surfaces plotted in Fig. 20 provide insight into the influence of the non-ideal parameters. Fig. 20(a)
shows the CM impedance as a function of frequency and the

## [стр. 9]

2070
IEEE TRANSACTIONS ON POWER ELECTRONICS, VOL. 23, NO. 4, JULY 2008
Fig. 19. Circuit used for analyzing the influence of parasitic elements R ; L
and k
in the performance of the capacitance cancellation for a three-phase
CM inductor. Damping resistor R
is shown.
coupling factor
, from where it is seen that the resonance
frequency gets lower for low values of coupling and is infinite
for unitary coupling. The influence of the series resistances
has the same type of effect as lowering the magnetic coupling
[see Fig. 20(b)].
The use of the capacitance cancellation network leads to the
inclusion of
, what creates resonances at frequencies higher
than the self-resonance. It produces undesired resonances
in both, CM and DM, impedances and if these resonances
are under 30 MHz they might cause problems for conducted
emissions, otherwise they affect radiated emissions. These resonances can be damped with the help of a damping resistance
as observed in Fig. 20(c) and Fig. 21. The increase of the
inductor's series resistance
has a similar damping behavior,
but it considerably lowers the capacitance cancellation effect.
A similar study can be performed for the DM capacitance
cancellation techniques leading to similar results, but for the
sake of brevity these are here omitted.
VI. EXPERIMENTAL RESULTS
In order to verify the presented principles experiments are
performed. Two filter circuits, one comprising a single
stage
DM filter and another with a single-stage CM filter as shown in
Fig. 22, are used to verify the achievable insertion loss with the
application of some of the presented techniques. The filters are
built in a way that the capacitors included for capacitance cancellation
and
are easily removable, so that
the effects of their inclusion are clearly observed. The inductors are wound such that both halves of each winding are close
to each other, assuring high magnetic coupling. This is accomplished by winding the inductors in two layers, the first one containing the first winding-half and the second layer containing the
second one [23].
The first measurements were performed with an impedance
analyzer in order to evaluate the total parallel capacitance for
each of the inductors. The parallel capacitances were measured
with the technique described in [28]. For the CM inductor
Fig. 20. Influence of parasitic elements, where L
=
500 H and
C
=10 pF. (a) CM impedance as a function of the coupling factor k
with
R
= 0
 and L
= 0 H. (b) CM impedance as a function of the series
resistance R
with k
= 1 and L
= 0 H. (c) DM impedance as a function
of the damping resistance R
with k
= 1; R
= 0
 and L
= 100 nH.
the total measured parallel capacitance was 17.7 pF, while the
capacitance for the DM inductors had an average of 52 pF within
2% variation among the three inductors
.
A second set of experiments comprised measurements of
insertion loss (see Fig. 23) of the two filters, mounted on a
single printed circuit board, with a two-port network analyzer
HP4195A. CM insertion loss measurements are performed with
the first port connected between terminals
, and
together
and PE and the second port connected from
, and
to PE.
DM insertion loss is measured with the help of two insulation
transformers (input and output) from terminals
and
to

## [стр. 10]

HELDWEIN AND KOLAR: WINDING CAPACITANCE CANCELLATION
2071
Fig. 21. Influence of L
in the (a) DM and (b) CM impedances and the possibility of damping by inserting a resistor R
in series.
Fig. 22. Input filter circuits employed in the testing of capacitance cancellation
techniques. (a) CM filter structure employed in the experiments. (b) DM filter
used to test the capacitance cancellation.
terminals
and
. The insertion loss measurements are performed with both filters connected in series. Due to the limited
commercially available capacitance values, only approximate
values were used. This was relevant information also in order
to evaluate the sensitivity to the variation in capacitance.
Fig. 24(a) shows the insertion loss measurements for CM
when applying capacitance cancellation networks which employ: 1) upper trace-no capacitance cancellation network; 2)
middle trace-a single 220 pF capacitor connected to the center
of one of the windings as in (23), and 3) lower trace-three
68 pF capacitors as in (21), each connected to each one of the
windings. The effectiveness of the capacitance cancellation
networks is clearly observed since the resonance of the circuit
without cancellation at approximately 2 MHz is no longer
observed and an increasing gain in the insertion loss curves is
seen up to 30 MHz, where a difference of more than 20 dB is
seen from the configuration with three capacitors. The connection of a single capacitor is less effective due to low magnetic
coupling amongst the three windings. Thus, an appreciable
difference is noticed for frequencies higher than 15 MHz. The
worsening in the attenuation curve beyond the resonance at
Fig. 23. Insertion loss measurement setups. (a) Measurement setup for CM
insertion loss IL
. (b) DM insertion loss IL
measurement setup.
Fig. 24. Insertion loss measurements showing the application of capacitance
cancellation in the employed three-line power filters. (a) Filter CM insertion
loss illustrating the application of capacitance cancellation to a three-phase CM
choke. Shown are: measurement without capacitance cancellation; with three
cancellation capacitors (68 pF per winding), and with a single one (220 pF)
connected to one of the windings. (b) DM insertion loss measurement with and
without capacitance cancellation to three DM inductors (220 pF per inductor).
9.4 MHz is observed with and without cancellation, thus this
is a point were a resonance, which is not the self-resonance of
the inductor. The self-resonance frequency of the inductor is at
approximately 2 MHz as seen in Fig. 24(a).
The insertion loss curves for the DM capacitance cancellation are presented in Fig. 24(b) for a network as in Fig. 13. It
is observed that the results are not as expressive as in the CM
case. A deeper analysis proves that, depending on the complete
filter configuration, the cancellation of these capacitances might
not improve the situation considerably. This is due to the fact
that resonance frequencies are also influenced by the coupling
with other elements, such as other components of the CM filter,
and by different load and source impedances. Despite that, the

## [стр. 11]

2072
IEEE TRANSACTIONS ON POWER ELECTRONICS, VOL. 23, NO. 4, JULY 2008
Fig. 25. Insertion loss measurement for the DM filter when removing components C
; L
and R
from the PCB.
measurements with the DM capacitance cancellation show an
improvement in very high frequencies and an appreciable reduction of the resonance peak at 4 MHz.
The improvement observed in the DM insertion loss curves
is not substantial. Therefore, a measurement is performed only
with the three DM inductors, that means, removing components
and
from the printed circuit board. The result
is shown in Fig. 25, where it is seen that the cancellation works,
shifting the resonance frequency of the circuit from 1 MHz to
more than 3 MHz and improving the insertion loss by 17 dB at
10 MHz.
In order to understand the performance presented for the DM
cancellation, three simple simulations are done assuming unitary coupling among the halves of the winding of the inductor,
amounting for a total of 10 pF in parallel with 40
H. These
simulations are performed in order to study the influence of external couplings in the performance of the filter [18], [30], [31].
The canceling capacitor is four times larger (40 pF). The simulated circuits and respective results (attenuation from
to
)
are presented in Fig. 26. The first simulation [see Fig. 26(a)]
shows a simple filter configuration where a single capacitor (3
F) with its ESL (20 nH) is employed at the input and the results show an improvement of approximately 20 dB at 30 MHz.
In Fig. 26(b), a capacitor (1
F
10 nH) is included at the
output, thus forming a
-type filter and, again, 20 dB improvement is observed. At the third simulation [see Fig. 26(c)], a small
amount of coupling
0.05 is added between the filtering
inductor and the output capacitor's ESL. It is observed that the
resonances are shifted and the effect of the capacitance cancellation is only observed for higher frequencies, so that only approximately 6 dB improvement is achieved at 30 MHz. This result
alerts for the fact that, depending on the complexity of the filter,
the effects of capacitance cancellation might be lower than expected in practical filters and special care should be taken when
designing the filter layout.
VII. CONCLUSION
This work has presented a systematic way of evaluating
impedances (CM and DM) in three-phase networks to be used
in power line filtering. The alternatives provided by three-phase
networks have been explored to achieve winding parasitic
capacitance cancellation. Techniques have been presented for
three-phase inductive networks along with a comprehensive
theoretical analysis, where advantages and side-effects of the
networks have been highlighted and possible improvements
through damping resistances and use of different networks
have been proposed. The influence of common parasitic effects
Fig. 26. Simulation circuits and results (attenuation from u
to u ) for explaining the influence of coupling with external components in the performance
of parasitic capacitance cancellation. (a) Simple filter employing on capacitor
and the inductor with and without cancellation. (b) "Pi"-type filter. (c) "Pi"-type
circuit with coupling from the output capacitor to the inductor's winding.
was studied, from where the guidelines for a good design
can be derived. The possibility of asymmetrical capacitance
cancellation was proposed, which can improve the application
of these techniques for switched mode power circuits. With the
application of the proposed cancellation networks it is expected
that cheaper inductors can be used, since the magnetic component designer is able to use a core with fully winded window.

## [стр. 12]

HELDWEIN AND KOLAR: WINDING CAPACITANCE CANCELLATION
2073
Fig. 27. Considered networks.
Fig. 28. Equivalent circuits with magnetic coupling.
In order to prevent the elevation of the cost with capacitors it is
proposed that the small capacitors are integrated into the printed
circuit board whenever possible. A set of experimental results
attest the presented principles and prove that the analyzed techniques allow for improvements in the performance of an EMC
filter. From the results it is seen that the degree of improvement
is dependent on the circuit structure, since different source and
load impedances and coupling among filter stages considerably
change the influence of an inductor's parasitic capacitance.
Good layout techniques, other parasitic impedance cancellation
techniques and the reduction of capacitive and magnetic couplings are to be used along with the capacitance cancellation
techniques and shall allow for more compact, cheap and high
performance filtering for three-phase power converters.
APPENDIX I
EQUIVALENCE OF TWO-PORT NETWORKS
In order to simplify the expressions, impedances matrices
are here employed. The impedance matrices for the circuits of
Fig. 27 are given by
for the
network
(A1)
and for the
-network by
Z =
Y
+Y
Y
Y
+Y
Y
+Y
Y
Y
Y
Y
+Y
Y
+Y
Y
Y
Y
Y
+Y
Y
+Y
Y
Y
+Y
Y
Y
+Y
Y
+Y
Y
:
(A2)
If all elements of matrices
and
are the same, then the
networks are equivalent.
Another equivalence of interest is given for the networks depicted in Fig. 28. These are used in some of the capacitance cancellation networks, inductance cancellation networks and other
types of filters.
Considering the coupled inductor circuit, its impedance matrix is given by
(A3)
The non-coupled network presents the matrix
(A4)
Solving the equation given by
in order
to find equivalent networks results in
(A5)
REFERENCES
[1] J. A. Ferreira and v. J. D. Wyk, "Electromagnetic energy propagation
in power electronic converters: Toward future electromagnetic integration," Proc. IEEE, vol. 89, no. 6, pp. 876-889, Jun. 2001.
[2] F. C. Lee and P. Barbosa, "The state-of-the-art power electronics technologies and future trends," in Proc. IEEE PES Transm. Distrib. Conf.
Expo, 2001, vol. 2, pp. 1188-1193.
[3] B. K. Bose, "Energy, environment, and advances in power electronics,"
IEEE Trans. Power Electron., vol. 15, no. 4, pp. 688-701, Jul. 2000.
[4] R. Redl, "Electromagnetic environmental impact of power electronics
equipment," Proc. IEEE, vol. 89, no. 4, pp. 926-938, Jun. 2001.
[5] C. R. Paul, Introduction to Electromagnetic Compatibility, 2nd ed.
New York: Wiley, 2006.
[6] M. J. Nave, Power Line Filter Design for Switched-Mode Power Supplies.
New York: Van Nostrand Reinhold, 1991.
[7] R. W. Erickson and D. Maksimovic, Fundamentals of Power Electronics, 2nd ed.
Norwell, MA: Kluwer Academic, 2001.
[8] D. Cochrane, D. Y. Chen, and D. Boroyevic, "Passive cancellation of
common-mode noise in power electronic circuits," IEEE Trans. Power
Electron., vol. 18, no. 3, pp. 756-763, May 2003.
[9] L. LaWhite and M. F. Schlecht, "Active filters for 1-MHz power circuits with strict input/output ripple requirements," IEEE Trans. Power
Electron., vol. PE-2, no. 4, pp. 282-290, Oct. 1987.
[10] S. Ogasawara, H. Ayano, and H. Akagi, "An active circuit for cancellation of common-mode voltage generated by a pwm inverter," IEEE
Trans. Power Electron., vol. 13, no. 5, pp. 835-841, Sep. 1998.
[11] M. L. Heldwein, H. Ertl, J. Biela, and J. W. Kolar, "Implementation
of a transformer-less common mode active filter for off-line converter
systems," in Proc. 21st Annu. IEEE Appl. Power Electron. Conf. Expo,
Dallas, TX, Mar. 19-23, 2006, vol. 2, pp. 1230-1236.
[12] J. Dumas, B. Lanoue, and B. Tahhan, "Active analog power filters provide solutions for EMC and EMI," in Proc. 19th Annu. IEEE Appl.
Power Electron. Conf. Expo, 2004, vol. 2, pp. 675-680.
[13] S. Ye, W. Eberle, and Y.-F. Liu, "A novel EMI filter design method for
switching power supplies," IEEE Trans. Power Electron., vol. 19, no.
6, pp. 1668-1678, Nov. 2004.
[14] M. J. Nave, "On modeling the common mode inductor," in Proc. Int.
Symp. Electromagn. Compat., Cherry Hill, NJ, Aug. 12-16, 1991, pp.
452-457.
[15] A. Massarini, M. K. Kazimierczuk, and G. Grandi, "Lumped parameter models for single- and multiple-layer inductors," in Proc. 27th
Power Electron. Spec. Conf., Baveno, Italy, Jun. 23-27, 1996, vol. 1,
pp. 295-301.
[16] C. Mei, J. C. Balda, W. C. Waite, and K. Carr, "Analyzing commonmode chokes for induction motor drives," in Proc 33th Power Electron. Spec. Conf., Queensland, Australia, Jun. 23-27, 2002, vol. 3, pp.
1557-1562.
[17] D. Liu and X. Jiang, "High frequency model of common mode inductor for EMI analysis based on measurements," in Proc. IEEE Int.
Symp. Electromagn. Compat., Minneapolis, MN, Aug. 19-23, 2002,
pp. 462-465.
[18] S. Wang, F. C. Lee, D. Y. Chen, and W. G. Odendaal, "Effects of parasitic parameters on EMI filter performance," IEEE Trans. Power Electron., vol. 19, no. 3, pp. 869-877, May 2004.
[19] R. Chen, J. D. van Wyk, S. Wang, and W. G. Odendaal, "Improving
the characteristics of integrated EMI filters by embedded conductive
layers," IEEE Trans. Power Electron., vol. 20, no. 3, pp. 611-619, May
2005.
[20] R. Chen and J. D. van Wyk, "Planar inductor with structural winding
capacitance cancellation for PFC boost converters," in Proc. IEEE App.
Power Electron. Conf. Exp., 2005, vol. 2, pp. 1301-1307.

## [стр. 13]

2074
IEEE TRANSACTIONS ON POWER ELECTRONICS, VOL. 23, NO. 4, JULY 2008
[21] R. Chen, "Integrated EMI Filters for Switch Mode Power Supplies,"
Ph.D. dissertation, Virginia Tech., Blacksburg, 2004.
[22] S. Wang, R. Chen, J. D. van Wyk, F. C. Lee, and W. G. Odendaal,
"Developing parasitic cancellation technologies to improve EMI filter
performance for switching mode power supplies," IEEE Trans. Electromagn. Compat., vol. 47, no. 4, pp. 621-629, Nov. 2005.
[23] S. Wang, F. C. Lee, and J. D. van Wyk, "Design of inductor winding capacitance cancellation for EMI suppression," IEEE Trans. Power Electron., vol. 21, no. 6, pp. 1825-1832, Nov. 2006.
[24] T. C. Neugebauer and D. J. Perreault, "Parasitic capacitance cancellation in filter inductors," IEEE Trans. Power Electron., vol. 21, no. 1,
pp. 282-288, Jan. 2006.
[25] R. C. Dorf, The Electrical Engineering Handbook.
Boca Raton, FL:
CRC, 1992.
[26] S. Qu and D. Chen, "Mixed-mode EMI noise and its implications to
filter design in offline switching power supplies," IEEE Trans. Power
Electron., vol. 17, no. 4, pp. 502-507, Jul. 2002.
[27] M. Jin, M. Weiming, P. Qijun, K. Jun, Z. Lei, and Z. Zhihua, "Identification of essential coupling path models for conducted EMI prediction
in switching power converters," IEEE Trans. Power Electron., vol. 21,
no. 6, pp. 1795-1803, Nov. 2006.
[28] Q. Yu, T. W. Holmes, and K. Naishadham, "RF equivalent circuit modeling of ferrite-core inductors and characterization of core materials,"
IEEE Trans. Electromagn. Compat., vol. 41, no. 1, pp. 258-262, Feb.
2002.
[29] S. Wang and F. C. Lee, "Common-mode noise reduction for power
factor correction circuit with parasitic capacitance cancellation," IEEE
Trans. Electromagn. Compat., vol. 49, no. 3, pp. 537-542, Aug. 2007.
[30] S. Wang, F. C. Lee, and W. G. Odendaal, "Controlling the parasitic
parameters to improve EMI filter performance," in Proc. IEEE Appl.
Power Electron. Conf. Exp., 2004, vol. 1, pp. 503-509.
[31] S. P. Weber, E. Hoene, S. Guttowski, J. John, and H. Reichl, "Predicting
parasitics and inductive coupling in EMI-filters," in Proc. IEEE Applied
Power Electron. Conf. Exp., 2006, p. 4.
Marcelo Lobo Heldwein (S'99-M'08) received
the B.S. and M.S. degrees in electrical engineering
from the Federal University of Santa Catarina, Florianópolis, Brazil, in 1997 and 1999, respectively, and
the Ph.D. degree from the Swiss Federal Institute of
Technology (ETH), Zurich, Switzerland, in 2007.
He is currently a Postdoctoral Fellow at the Power
Electronic Institute (INEP), Federal Institute of Santa
Catarina. From 1999 to 2001, he was a Research Assistant with the Power Electronics Institute, Federal
University of Santa Catarina. From 2001 to 2003, he
was an Electrical Design Engineer with Emerson Energy Systems, São José
dos Campos, Brazil, and in Stockholm, Sweden. His research interests include
power factor correction techniques, static power converters, and electromagnetic
compatibility.
Dr. Heldwein is currently a member of the Brazilian Power Electronic Society
(SOBRAEP).
Johann W. Kolar (SM'04) received the Ph.D. degree
(with highest honors) from the University of Technology Vienna, Vienna, Austria.
Since 1984, he has been an Independent International Consultant in close collaboration with
the University of Technology Vienna in the fields
of power electronics, industrial electronics, and
high-performance drives. He has proposed numerous
novel PWM converter topologies and modulation
and control concepts, e.g., the VIENNA rectifier
and the three-phase ac-ac sparse matrix converter.
He was appointed Professor and Head of the Power Electronic Systems
Laboratory, Swiss Federal Institute of Technology (ETH), Zurich, Switzerland,
in February 2001. In 2006, the European Power Supplies Manufacturers
Association (EPSMA) awarded the Power Electronics Systems Laboratory of
ETH Zurich as the leading academic research institution in Europe. The focus
of his current research is on ac-ac and ac-dc converter topologies with low
effects on the mains, e.g., for power supply of telecommunication systems,
More-Electric-Aircraft, and distributed power systems in connection with fuel
cells. Further main areas of research are the realization of ultra-compact intelligent converter modules employing latest power semiconductor technology
(SiC), novel concepts for cooling and EMI filtering, multidomain/multiscale
modelling and simulation, pulsed power, bearingless motors, and Power
MEMS. He has published over 250 scientific papers in international journals
and conference proceedings and has filed more than 70 patents.
Dr. Kolar is a Member of the IEEJ and of the Technical Program Committees
of numerous international conferences in the field (e.g., Director of the Power
Quality Branch of the International Conference on Power Conversion and Intelligent Motion). From 1997 through 2000, he served as an Associate Editor of
the IEEE TRANSACTIONS ON INDUSTRIAL ELECTRONICS and since 2001 as an
Associate Editor of the IEEE TRANSACTIONS ON POWER ELECTRONICS. Since
2002, he has been an Associate Editor of the Journal of Power Electronics of the
Korean Institute of Power Electronics and a member of the Editorial Advisory
Board of the IEEJ Transactions on Electrical and Electronic Engineering. He
received the Best Transactions Paper Award of the IEEE Industrial Electronics
Society in 2005 and an Erskine Fellowship from the University of Canterbury,
New Zealand, in 2003.
