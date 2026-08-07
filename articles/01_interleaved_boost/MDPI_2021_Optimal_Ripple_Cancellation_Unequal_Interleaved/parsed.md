# Differential Evolution Based Algorithm for Optimal Current Ripple Cancelation in an Unequal Interleaved Power Converter

<!-- FORMULA-WARNING -->
> **Формулы в этом файле недостоверны.** Текстовый слой PDF теряет дробные черты, радикалы и группировку степеней; знак интеграла приходит как `Z` или `R`, знак суммы -- как `P`. Формул вырезано: **22**, читать их в `formulas/` (картинки 300 dpi, перечень в `formulas/INDEX.md`).
<!-- /FORMULA-WARNING -->

> Автоматически извлечено из `source.pdf` скриптом `parse_pdf.py`
> Движок: pymupdf. Страниц: 17 из 17.
> Дата извлечения: 2026-08-07 06:42 UTC

Текст не редактировался. Формулы и таблицы могут быть искажены —
при сомнении сверяться с исходным PDF.

---

## [стр. 1]

mathematics
Article
Differential Evolution Based Algorithm for Optimal Current
Ripple Cancelation in an Unequal Interleaved Power Converter
Julio C. Rosas-Caro 1,*
, Pedro M. García-Vite 2
, Alma Rodríguez 1,3
, Abraham Mendoza 1
,
Avelina Alejo-Reyes 1, Erik Cuevas 3
and Francisco Beltran-Carbajal 4


Citation: Rosas-Caro, J.C.;
García-Vite, P.M.; Rodríguez, A.;
Mendoza, A.; Alejo-Reyes, A.;
Cuevas, E.; Beltran-Carbajal, F.
Differential Evolution Based
Algorithm for Optimal Current
Ripple Cancelation in an Unequal
Interleaved Power Converter.
Mathematics 2021, 9, 2755. https://
doi.org/10.3390/math9212755
Academic Editor: Nicu Bizon
Received: 28 September 2021
Accepted: 21 October 2021
Published: 29 October 2021
Publisher's Note: MDPI stays neutral
with regard to jurisdictional claims in
published maps and institutional affiliations.
Copyright: © 2021 by the authors.
Licensee MDPI, Basel, Switzerland.
This article is an open access article
distributed
under
the
terms
and
conditions of the Creative Commons
Attribution (CC BY) license (https://
creativecommons.org/licenses/by/
4.0/).
1
Facultad de Ingenieria, Universidad Panamericana, Alvaro del Portillo 49, Zapopan 45010, Mexico;
anrodriguez@up.edu.mx or alma.rvazquez@academicos.udg.mx (A.R.); amendoza@up.edu.mx (A.M.);
aalejo@up.edu.mx (A.A.-R.)
2
Tecnologico Nacional de Mexico, Instituto Tecnologico de Ciudad Madero,
Av. 1o. de Mayo s/n Col. Los Mangos, Ciudad Madero 89440, Mexico; pedro.gv@cdmadero.tecnm.mx
3
Departamento de Electrónica, Universidad de Guadalajara, CUCEI, Av. Revolución 1500,
Guadalajara 44430, Mexico; erik.cuevas@cucei.udg.mx
4
Departamento de Energía, Universidad Autónoma Metropolitana, Unidad Azcapotzalco,
Mexico City 02200, Mexico; fbeltran@azc.uam.mx
*
Correspondence: crosas@up.edu.mx; Tel.: +52-33-1918-1065
Abstract: This paper proposes an optimal methodology based on the Differential Evolution algorithm
for obtaining the set of duty cycles of a recently proposed power electronics converter with input
current ripple cancelation capability. The converter understudy was recently introduced to the
state-of-the-art as the interleaved connection of two unequal converters to achieve low input current
ripple. A latter contribution proposed a so-called proportional strategy. The strategy can be described
as the equations to relate the duty cycles of the unequal power stages. This article proposes a third
switching strategy that provides a lower input current ripple than the proportional strategy. This is
made by considering duty cycles independently of each other instead of proportionally. The proposed
method uses the Differential Evolution algorithm to determine the optimal switching pattern that
allows high quality at the input current side, given the reactive components, the switching frequency,
and power levels. The mathematical model of the converter is analyzed, and thus, the decision
variables and the optimization problem are well set. The proposed methodology is validated through
numerical experimentation, which shows that the proposed method achieves lower input current
ripples than the proportional strategy.
Keywords: Differential Evolution; metaheuristic algorithms; optimization; DC-DC Converter
1. Introduction
Power electronics converters are essential in many fields of applications. Particularly,
DC-DC power converters range from a few watts in battery-powered portable devices [1-3]
to several kilowatts when employed in power systems [4,5]. Portable electronics devices
usually operate at high frequencies in order to reduce their physical sizes [2]. This research
focuses on a DC-DC step-up power converter. This kind of converter can be employed
in renewable energy sources with low D.C. power generation, such as photovoltaic and
hydrogen-based fuel cell sources that provide a few tens of volts [6]. DC-DC converters are
constituted by a combination of solid-state switches and reactive components that process
the input power to feed a resistive load, usually at different voltage levels. The switches are
driven by a binary commanding function q(t) at a fixed frequency. The reactive components
capacitors (C) and inductors (L) are employed to store the energy coming from the source
and then deliver such energy to the load.
Among the features specified in a high voltage-gain DC-DC converter is the voltage
gain; this can be defined as the output voltage ratio to the input voltage and is independent
Mathematics 2021, 9, 2755. https://doi.org/10.3390/math9212755
https://www.mdpi.com/journal/mathematics

## [стр. 2]

Mathematics 2021, 9, 2755
2 of 17
of the reactive components. Another important specification is the input current quality,
which is analyzed in terms of the switching ripple. This is the article's main focus, and it
is related to current drawn from the source; having a high input current quality means
that a pure (or almost pure) D.C. is extracted, without A.C. ripple or variation. This is an
ideal condition since the ripple naturally appears due to the commutation process of the
switches. Several topologies that provide high input current quality have recently appeared
in the literature [7-10]. With the modification of a conventional boost converter presented
in [11], it is possible to have a reduced input current ripple by adding extra components.
More complex configurations with both capabilities have also been proposed.
This paper focuses on a recently proposed converter [12], made by the interleaved
connection of two unequal power stages, the classical boost converter [13] and a modified
(resonant version of the) three-switch high-voltage TSHV converter [14].
The interleaved interconnection of classical boost power stages is a proven technology [15]. It leads to a special situation in which the input current ripple is zero (for D = 0.5);
in this zero-ripple situation, the input current ripple (high-frequency variation) of one
power stage cancels perfectly with the other one (for example, in a two-phases converter),
and the input current of the entire converter is a pure D.C. signal. However, this happens
only in a particular operation point; for different duty cycles (D̸ = 0.5), the ripple must
be evaluated.
The contribution made in [12] was not only the interconnection of two unequal power
stages. The interconnection, along with a particular PWM strategy (in which duty cycles of
power stages were opposite or complementary), made it possible to choose the zero-ripple
point or zero ripple duty cycle (it can be D = 0.5 or any other). Another contribution related
to this converter was reported in [16], in which a different PWM strategy, and design
procedure, were introduced. In ref. [16], the duty cycles of power stages are proportional
instead of complementary to each other, allowing a better operation of the converter and
reducing the input current ripple of the entire converter.
This article proposes a third PWM strategy for the discussed converter. In this case,
duty cycles of the unequal power stages are independent of each other, and this makes
it possible to further reduce the input current ripple of the entire operating range of the
converter without changing the hardware (physical components) of the circuit. Having
independent duty cycles brings a particular challenge; an infinite number of combinations
of duty cycles provide a specific voltage gain. This challenge is solved by using the
Differential Evolution DE algorithm. The DE algorithm is used to select the combination of
duty cycles that comply with the required output voltage, and at the same time, minimizes
the input current ripple of the converter. The proposed methodology is validated through
numerical experimentation, which shows that the proposed method achieves a better result
(lower input current ripple) than the proportional strategy for a predefined operation range.
Optimization algorithms are widely used in the electrical engineering field [17-22].
Other related approaches that use metaheuristic algorithms, particularly for DC-DC converters, have been recently proposed. These methods include the Harris Hawks Optimization (HHO) algorithm, which is applied for tuning the parameters of two PID controllers
used in a buck converter by minimizing the maximum overshoot [18]. In addition, a hybrid
method was proposed in [19] that uses the Firefly (F.A.) and Particle Swarm Optimization
(PSO) algorithms to adjust the parameters of the PID controller used in a buck converter.
Furthermore, the same problem of tuning parameters of the PID controller in a DC-DC
buck converter was managed by a hybrid strategy that integrated the Whale Optimization
Algorithm and Simulated Annealing to enhance the transient response of the converter [20].
Similar approaches were proposed in [21,22] to face the parameter tuning problem in the
PID controllers of converters of this type.
2. Converter Configuration
The interconnection of two or more power stages or cells is a common practice to
build more complex converters, and the proposition of new topologies is a very active

## [стр. 3]

Mathematics 2021, 9, 2755
3 of 17
research field. There are many composed topologies; for example, the interleaved boost
converter [15]. Despite the large number of different combinations, a large portion belongs
to two main configurations. Considering two individual power cells (Cell 1 and Cell 2) with
the voltage gain represented by the functions g1(d1) and g2(d2), respectively, two possible
configurations can be obtained (see Figure 1). The first configuration shown in Figure 1a is
the cascaded interconnection; the output of the first power stage is the input of the second
one. The second configuration is the input-parallel output-series, in which power stages
are connected in parallel at the input, and in series at the output.

(a)

(b)
1
1
(
)
g d
in
v
1
C
1L
out
v
R
1
Li
1v
2
2
(
)
g d
2
C
2L
2
Li
2v
ini
1
1
(
)
g d
in
v
1
C
1L
out
v
R
1
Li
1v
2
2
(
)
g
d
2
C
2
L
2
Li
2v
ini
Figure 1. Two common configurations of two power cells to obtain high voltage gain: (a) cascaded
configuration; (b) input-parallel output-series configuration.
The independent variables d1 and d2 are the duty cycles corresponding to each converter. Figure 1a shows a cascaded connection where the output voltage vo is the input
voltage times the product of the individual gains. In contrast, in Figure 1b, the value of
vo is the voltage times the summation of the individual gains of each power stage. The
common feature of both configurations is that the source current is diverted into the two
cells through its corresponding input inductor. Good examples of both configurations
can be found in [16] for a photovoltaic application and in [23] adapted for DC-source
renewable generation.
In the second case, the input-parallel output-series configuration, it is true that:
iin(t) = iL1(t) + iL2(t)
(1)
The proposed methodology is applied to a power converter belonging to the inputparallel output-series configuration [12,22].
3. Converter Understudy
In order to apply the proposed methodology, the mathematical model of the selected
power converter is first derived. Figure 2 shows the converter understudy, initially proposed in [12]. The converter is composed of two cells in an input-parallel output-series
connection, following the configuration presented in Figure 1b.

## [стр. 4]

Mathematics 2021, 9, 2755
4 of 17
2s
2L
in
v
3
C
1s
1
C
1L
ou
v
R
1
Li
2
Li
1
D
2
D
3
D
3L
ini
oi
2
C
1v
2v

Figure 2. Configuration of the converter under study.
The cells that build the selected converter are: (i) A boost converter [13] composed of
switch S1, diode D1, inductor L1, and capacitor C1. (ii) A modified (resonant version of the)
three-switch high-voltage TSHV [14] converter constituted by the rest of the devices, that
is, switch S2, diode D2, inductors L2 and L3, and capacitors C2 and C3; note that diode D3
has been added to block negative current through L3.
The load resistor R is fed by the summation of the individual output voltage of each
cell, that is, vC1 for the boost converter and vC3 for the modified TSHV converter; therefore,
the instantaneous output voltage vo(t) is determined by (2).
vo(t) = vC1(t) + vC3(t)
(2)
It is worth mentioning that there are other hybrid topologies, such as [24], but the
structure of Figure 2, driven by two independent transistors, makes it possible to perform
the input current ripple cancelation, as will be explained.
3.1. Mathematical Model of the Power Converter
Transistors are the manipulated devices that allow power processing through the
reactive components. Therefore, in the selected topology, two switching functions are
independently operated, which are defined as (3).
qj(t) =
 1
→
Sj
is
closed
0
→
Sj
is
open
(3)
with j = 1, 2 corresponding to switches S1 and S2. Since there are two switching functions
that are independently controlled, four possible combinations are obtained.
For practical realization, the switching functions of (3) can be implemented in digital
or analog fashion in the well-known pulse-width modulation (PWM) technique, which
consists of commutating the transistor at constant frequency F.S., and hence, at constant
period TS = 1/FS. Assuming that qj(0) = 1, the transition occurs at t = dTS, as illustrated in
Figure 3.

Figure 3. Graphical representation of the switching functions qj(t) as a PWM technique.

## [стр. 5]

Mathematics 2021, 9, 2755
5 of 17
The ratio of the time during which the transistor is active (on-state) to the time when
it is inactive (off-state) is called the duty cycle dj(t) and is equivalent to the average value of
the switching function, as (4) indicates.
dj(t) = 1
TS
t+TS
Z
t
qj(τ)dτ
(4)
Note that dj(t) is usually taken as a function of time. It represents the manipulated
variable that can vary from one switching period to another during the transient response
when a closed-loop is implemented [25].
3.2. Equivalent Circuits
In the converter understudy, the input current depends on the inductor's current, and
the action of the switching functions drives the inductor's current.
The best case to minimize the input current (see Figure 4) is when transistors switch
complementarily, which means when S1 is open, S2 is closed, and vice versa. This strategy
was originally proposed in [12] and consisted of commutating between the equivalent
circuits of Figure 4a,b. All switching states are summarized in Table 1.

(a)
(b)

(c)
(d)
2s
2
L
in
v
3
C
1s
1
C
1L
out
v
R
1
Li
2
Li
1
D
2
D
3
D
3
L
ini
oi
2
C
1v
2v
{
}
1
2
,
1,0
q q =
2s
2
L
in
v
3
C
1s
1
C
1L
out
v
R
1
Li
2
Li
1
D
2
D
3
D
3L
ini
oi
2
C
1v
2v
{
}
1
2
,
0,1
q q =
2s
2L
in
v
3
C
1s
1
C
1L
out
v
R
1
Li
2
Li
1
D
2
D
3
D
3L
ini
oi
2
C
1v
2v
{
}
1
2
,
1,1
q q =
2s
2L
in
v
3
C
1s
1
C
1L
out
v
R
1
Li
2
Li
1
D
2
D
3
D
3L
ini
oi
2
C
1v
2v
{
}
1
2
,
0,0
q q =
Figure 4. Equivalent circuits for the various commutation states: (a) state: q1, q2 = {1,0}, current through L1 increases
whereas that which runs through L2 decreases; (b) state: q1, q2 = {0,1}, opposite to the state in (a); (c) state: q1, q2 = {1,1}, both
inductors' currents increase; and (d) state: q1, q2 = {0,0}, both inductors' currents decrease.
Table 1. State.
S_1
S_1
Circuit
0
0
a
0
1
b
1
0
c
1
1
d

## [стр. 6]

Mathematics 2021, 9, 2755
6 of 17
Average Model of the Converter
The instantaneous voltage vx(t) across an inductor Lx is defined as:
vx(t) = Lx
dix(t)
dt
(5)
Since, in power electronics converters, the voltage across an inductor during a commutation state, as well as the inductance, is constant, it can be observed that the derivative is
constant, and the current changes (rises or falls) linearly. For a positive voltage of vx(t), the
current ix increases with a constant slope, whereas the current decreases with a constant
slope for negative values of vx(t). This consideration is usually called small ripple approximation or linear ripple approximation [13], and it is justified considering that passive
components are correctly chosen for this purpose.
Therefore, due to the commutation action, the inductor currents possess a triangularshaped waveform.
From the circuits of Figure 4a,b and following the average model theory, it is possible
to write the inductor voltage along the entire switching period, as in (6) and (7).
diL1
dt
= d1
vin
L1
+ (1 -d1)vin -vC1
L1
(6)
diL2
dt
= d2
vin
L2
+ (1 -d2)vin -vC2
L2
(7)
The steady state can be calculated by considering that if the derivatives in (6) and (7)
are zero, the capacitors' voltages are found to be:
VC1 =
vin
(1 -D1)
(8)
VC2 =
vin
(1 -D2)
(9)
It is worth noting that the variables are capitalized in order to denote the average
values of the steady state or equilibrium.
4. Existing Methods
This article proposes a modulation strategy for a converter for which two modulation
strategies have been used; we can call them (i) the complementary strategy, proposed
in [12], and (ii) the proportional strategy, proposed in [16].
4.1. The Complementary Strategy
The complementary strategy, proposed in [12], consists of defining the duty cycles, as
shown in (10) and (11).
D1 = (1 -D)
(10)
D2 = D
(11)
Important waveforms related to the complementary strategy can be appreciated in
Figure 5.
Taking (2), (8), and (9) into account, the voltage gain (Gcomp = Vo/Vin) for the complementary strategy can be calculated as (12).
Gcomp =
1
D(1 -D)
(12)

## [стр. 7]

Mathematics 2021, 9, 2755
7 of 17
Figure 5. Graphical representation of the switching functions qj(t): complementary PWM technique.
For the proposed strategy presented in [12], it is easy to find the average current
through inductors, as shown in (13) and (14):
IL1 = 1
D Io
(13)
IL2 =
1
(1 -D) Io
(14)
where the output current Io = Vo/R. Moreover, from the equivalent circuits for q1,q2 = {1,0}
and q1,q2 = {0,1}, the current ripples in each inductor can be readily quantified, as shown in
(15) and (16).
∆iL1 = Vin
L1
(1 -D)
FS
(15)
∆iL2 = Vin
L2
(D)
FS
(16)
Following (1), the input current ripple can be expressed as shown (17) and (18).
∆iin = ∆iL1 + ∆iL2
(17)
However, the inductor current ripples have a phase displacement of 180◦(see Figure 5);
in other words, they always have different signs, for which the input current ripple can be
expressed as the difference among (15) and (16), and not their summation. Therefore, the
input current ripple is defined as:
∆iin =

Vin
FS
 D
L2
-1 -D
L1

(18)
From (18), it is easy to solve for D to obtain a zero-current ripple at the converter's input.
This strategy can fully cancel the current ripple at a preestablished operating point. However, as the converter moves away from such a point, the input current increases undesirably.
4.2. Proportional Modulation Strategy
The strategy described above is able to draw a D.C. pure current from the power
source. The proportional strategy, proposed in [16], also makes it possible to perform the
zero-ripple operation for a particular operation point, but converters usually operate not
only on a specific operation point but into an operating range. It was shown in [16] that
both strategies provide the same performance in the zero ripple operation points. Still, in
different operation points, the proportional strategy provided a smaller input current ripple.
That means, for a predefined operation range, the proportional strategy performs better.

## [стр. 8]

Mathematics 2021, 9, 2755
8 of 17
Considering (2), (8), and (9) the voltage gain G can be expressed as (19) and (20) for
duty cycles D1 and D2.
G =
1
(1 -D1) +
1
(1 -D2)
(19)
G =
2 -D1 -D2
1 -D1 -D2 + D1D2
(20)
Equations (19) and (20) apply for the converter in all different strategies.
It is evident that the desired voltage gain G1 can be obtained with an infinite number
of combinations of duty cycles employed in (19) and (20). The strategy proposed in [16]
assigns a proportional relationship, as shown in (21) and (22).
D1 = kD
(21)
D2 = D
(22)
where the factor k is a constant value, determined during the design process as a function
of the inductors in the following manner:
k = L1
L2
(23)
Considering (20)-(22), the voltage gain can be expressed as (24).
Gk =
2 -D -kD
1 -D + D + kD2
(24)
As it was presented in [16], the input current ripple can be analyzed in two different
cases; let's consider d* as the duty cycle in which the input current ripple is zero (as in [16]).
The input current ripple is expressed differently when d < d* and when d > d*. Figure 6
shows important waveforms of the operation: (i) in the case for d < d*, and (ii) in the case
for d > d*. Figure 6 shows the graphical representation of both cases.

(a)







  (b)
Figure 6. (a) D1 = 30%, D2 = 50%; (b) D1 = 30%, D2 = 70%.
Although the input current ripple behaves slightly differently in both cases, the input
current ripple can be defined as the maximum ripple during the operation. Then, the
largest vale is provided by the calculation in both cases [16].
It is worth mentioning that a PID controller still may control the voltage gain of the
converter to achieve the desired output voltage. The discussed algorithms are designed to
decide the proportions of duty cycles or of voltage gain in individual power stages of the
composing converter. The design of the PID controller can still be based on an optimization
algorithm [18-21].

## [стр. 9]

Mathematics 2021, 9, 2755
9 of 17
5. Differential Evolution Algorithm
Differential Evolution (D.E.) [26-31] is a search method that is widely recognized in
the evolutionary community and has proven its effectiveness and robustness in finding
global solutions. The DE algorithm is a classic and popular method that is extensively
used to solve complex optimization problems. Its low complexity and high performance
have made it widely used for applications in different fields such as image processing,
operation research, electronics engineering, mechanical engineering, manufacturing design,
power engineering, and many others [30,31]. Although other sophisticated evolutionary
methods have been recently proposed, the D.E. algorithm still maintains its prestige in the
metaheuristic community, mainly because of its low computational cost and effectiveness
even in constrained and high-dimensional optimization problems [29].
The DE technique considers different operators in its search strategy that allow the
particles to improve as they evolve in each generation. The DE method process involves
three basic operators, which are mutation, crossover, and selection. These operators are
part of the algorithm search process and will be described in detail in this section.
5.1. Mutation
The mutation process generates a mutant vector that results from combining the information from three different vectors, xr1, xr2, and xr3, taken randomly from the population.
The combination of these vectors considers the scaled difference between two of the three
vectors. Then, this difference is added to the third vector. The mathematical representation
of the mutation operator is described as:
v = xr3 + F(xr1 -xr2)
(25)
Each vector represents an individual from the population given in the presented
equation, while every element of the vector represents one dimension of the optimization
problem. The scale factor F from the same equation controls the difference between the
vector xr2 and the vector xr3. According to the authors of the D.E. algorithm, the scale factor
can take values within the interval [0, 2]. The scale factor is also known as the differential
weight since it regulates the difference (xr1-xr2).
5.2. Crossover
The crossover operator combines the information from one individual with the information from the mutant vector. This mechanism gives diversity to the population and,
therefore, prevents the algorithm from stagnating in suboptimal solutions. The combination consists of randomly taking elements from the mutant vector and elements from one
individual from the population with the aim of building a test vector u. The crossover
operation includes a crossover probability Pcross that adjusts the contribution of the mutant
vector in the generation of the test vector. The crossover probability strongly influences the
effectiveness of the D.E. method in finding promising solutions. Therefore, it is considered
a parameter to be adjusted by selecting values within the interval [0, 1]. The crossover
operator definition is expressed as (26).
uj =
(
vij
r(0, 1) ≤Pcross
xij
otherwise
(26)
5.3. Selection
The selection operator is the last stage in the D.E. method's flow of operations. The
objective of the selection method is to determine whether an individual in the population
is replaced by the test vector generated with the mutation and crossover operators. The
replacement of the individual with the test vector is carried out based on the evaluation of
the quality of both solutions. The individual who is selected through this evaluation process

## [стр. 10]

Mathematics 2021, 9, 2755
10 of 17
becomes part of a new generation of individuals. In this way, this mechanism ensures that
individuals evolve by selecting only the best particles to be part of a new population.
The selection mechanism contemplates the fitness value of the test vector u and the
fitness value of the individual xi. The selection follows a simple rule; if the fitness value
of the individual is worse than the fitness value of the test vector, then the individual is
replaced by the test vector. Otherwise, no replacement is made. Thus, the selection can be
formulated as:
xi =
(
u,
f (u) ≤f (xi)
xi,
otherwise
(27)
6. The Proposed Strategy
The proposed strategy considers two independent duty cycles, in contrast to the
former two strategies, namely the complementary strategy [12] defined in (10) and (11),
and the proportional strategy [16] defined by (21) and (22). Equations (2), (8), and (9) still
define the output voltage, which can also be expressed as (19) and (20). However, in this
case, there is not a particular equation that relates both duty cycles.
The strategy can be defined as (28) and (29).
D1 = kdD
(28)
D2 = D
(29)
where the factor kd is not a constant value, as in (21) and (22), but is instead a variable that
has to be found at the same time as D1 and D2.
The problem can be defined as an optimization problem. The objective is to minimize
the input current ripple while, at the same time, finding the duty cycles D1 and D2. Finding
D1 and D2 is equivalent to finding D and kd (see (28) and (29)). An important restriction
of the problem is the need to comply with a required amount of voltage gain. The input
current ripple can be defined as the largest of Equations (30) and (31).
∆ig1 =
Vin
kL f sL2
(kL -kdD -kLkdD)
(30)
∆ig2 =
Vin
kL f sL2
(1 -D -kLD)
(31)
where kL represents the relations among inductors (same as (23) for [16]), which must be
provided to the optimization problem.
An optimizer is ideal for this problem since the input current ripple is variable, and
their minimum value depends on the operating condition. The optimizer can minimize
the input current ripple without the need for a particular desired value (or setpoint) for
the ripple.
6.1. The Objective Function
The optimization problem is formulated according to the objective function defined in
(32). This objective function minimizes the higher value of the input current ripple. This
means that it evaluates Equations (30) and (31) and considers the highest value of the two
current ripple calculations to change parameters D and kd in order to decrease this value.
min
D,kd∈Rf (D, kd) =
(
∆ig1,
∆ig1 > ∆ig2
∆ig2,
otherwise
(32)
The above equation is subject to:
Vout
Vg
≤
2 -D -kdD
(1 -kdD)(1 -D) ≤Vout
Vg
+ δ
(33)

## [стр. 11]

Mathematics 2021, 9, 2755
11 of 17
0 ≤D ≤1
(34)
0 ≤kd ≤1
(35)
The objective function is subject to some constraints given by Equations (33)-(35).
Equations (34) and (35) define the range of possible values that parameters D and kd can
adopt. On the other hand, Equation (33) restricts the value of the output voltage. It ensures
that the desired voltage gain is satisfied. Equation (33) also contemplates a tolerance in the
output voltage, which is 1% of the estimated voltage gain. The solution obtained by the
proposed method must accomplish three such restrictions in order to consider the solution
as a feasible one.
6.2. Computational Procedure
The proposed strategy considers the implementation of the Differential Evolution
algorithm to find the optimal values of the parameters D and kd, which control the duty
cycle of the hybrid switched-capacitor boost converter. Currently, the optimal operation of
this type of converter is given by a specific duty cycle, which is obtained from a dependent
relationship between parameters D and kd. The dependency between these parameters
limits a further reduction in the input current ripple. Therefore, this article proposes a
different strategy to find the optimal switching pattern that allows high quality at the
input current side, thereby providing the reactive components with the required switching
frequency and power levels.
The optimization algorithm considers the set of values D and kd as a possible solution.
Thus, a population of possible solutions is created so that every individual i from the
population is defined as (36).
xi = {D, kd}
(36)
The population size is determined by the parameter N, which must be set at the
beginning of the search process. Additionally, every individual from the population is
initialized, by assigned random values, to the set {D, kd}. Then, each individual's fitness
value is calculated employing the objective function, which determines the input current
ripple. The assigned values to the set {D, kd} must satisfy the required gain both in the
initialization phase and throughout the algorithm search process. Therefore, the objective
function includes a constraint that identifies the particles that do not meet this requirement.
The identified solutions that violate this constraint are penalized by increasing their fitness
values. This mechanism avoids unfeasible solutions, and, at the same time, it guides the
search towards the space of feasible solutions. In that sense, to include the penalization,
the fitness function is rewritten as (37).
f itness = min
xi∈R2 f (xi) + h
(37)
From the above equation, the penalty function "h" is responsible for increasing the
fitness value of the particles that have violated the restriction. The mathematical expression
of this function is given by (38).
h = aC

Vout
Vg
-
2xi1 -xi2xi1
(1 -xi1xi2)(1 -xi1)

(38)
Here, a is a constant factor that controls the penalization degree of every unfeasible
solution. Whenever there is an unfeasible solution, the activation function C sets its value
to one to perform the penalty function. Otherwise, the penalty function is switched off.
The definition of the activation function can be expressed as (39).
C =
(
0,
2-xi1-xi2xi1
(1-xi2xi1)(1-xi1) ≥Vout
Vg
1,
otherwise
.
(39)

## [стр. 12]

Mathematics 2021, 9, 2755
12 of 17
The general structure of the D.E. method consists of initializing the population and
evaluating its fitness value. Then, the mutation operation is performed for each particle
to generate its mutant vector. After that, the crossover operation is also applied to every
candidate solution to create its test vector. Finally, the test vectors are evaluated in terms of
the fitness function. The best fitness between every particle and its respective test vector is
considered as the selection criterion to determine the set of individuals that will remain for
the next generation. This routine continues repeating for a specific number of generations,
denoted as Gmax. After all, the best solution found up to this point will represent the values
of parameters D and kd. The described procedure is summarized in Algorithm 1.
Algorithm 1 The general structure of the D.E. method
1. Initialize parameters Pcross, a, N, Gmax
2. Initialization of the population
3. Evaluation of the population in the fitness function
4. For each particle
5.
Creation of the mutant vector v
6.
Creation of the test solution u
7.
Selection of the best-found solution between u and xi
8. End for
9. Update the global-best so far
10. If the maximum number of generations has not been achieved
11.
Go to step 4
12. Else
13.
End the search
14. End if-else
7. Results
A simulation framework was implemented to validate the performance of the proposed method. The experiment contemplated a variable-voltage energy source that provided the required voltage to the converter. The converter input voltage varied from 28 V
to 40 V, which caused the voltage gain to range from 5 to 7.15.
On the other hand, some D.E. algorithm parameters needed to be set, such as the factor
a, the crossover probability Pcross, the number of generations Gmax, and the population
N (the number of individuals). This configuration was carried out by observing the
performance of the D.E. method for different combinations of values. Since the D.E.'s
performance is evaluated considering the achieved input current ripple ∆ig, a sensitivity
test was implemented to choose the best parameter configuration for reducing the input
current ripple. Different combinations of parameter values were set to execute the algorithm
for finding the input current ripple. For the crossover probability, we used the values of
0.1, 0.2, and 0.3. The constant factor a was considered with the values of 1, 10, and 100. The
population size included in the test was 20, 30, and 50 individuals. Finally, the maximum
number of generations was 100, 200, and 300. After several tests, the parameter combination
that best decreased the input current ripple was used in the numerical experiments. These
settings are listed in Table 2.
Table 2. Parameters of the D.E. method.
Crossover probability Pcross
0.2
Constant factor a
10
Population size N
50
Maximum number of generations Gmax
300

## [стр. 13]

Mathematics 2021, 9, 2755
13 of 17
Furthermore, the converter of interest involved several parameters that needed to be
configured, namely the inductor constant factor, the input voltage, the inductance, and the
switching frequency. Table 3 reports the stated parameters, whose values were assigned
considering the standard specifications for this kind of converter.
Table 3. Parameters of the hybrid switched-capacitor boost converter.
Input voltage Vg
28-40 V
Switching frequency fS
50 kHz
Inductor factor kL
0.4
Inductor L
200 µH
Numerical experiments were carried out to compare the proposed method's performance against the proportional strategy. Only the proportional strategy was considered
since it was previously proven that the proportional strategy achieves a lower input current
ripple compared to the complementary strategy for a defined operating range; if the proposed strategy provides superior performance compared to the complementary strategy, it
can be considered the best strategy.
This test considered several operating points to demonstrate the robustness of the
proposed approach. Every operating point represented a different input voltage to the
converter, which varied from 28 V to 40 V. Thus, the experiments considered 44 operating
points in which the proposed method and the traditional strategy were simulated to obtain
44 input current ripples, one for every operating point.
Furthermore, the values of the parameters described in tables a and b were used in
the experiments. Both methods were simulated under the same conditions to guarantee
that the comparison was fair. The best-achieved outcomes from the proposed technique,
considering 30 independent executions (due to its stochasticity nature), are reported in
Table 4. Likewise, the former strategy results are listed in the same Table, where the best
input current ripple ∆ig attained between both techniques is emphasized in boldface.
Table 4. Optimal parameter values and the input current ripple obtained from the numerical experiments considering the
former strategy and the proposed method.
Former Strategy
Proposed Method
G
D
kd
∆ig
D
kd
∆ig
5.00
0.7218
0.4000
0.0526
0.7215
0.4054
0.0502
5.05
0.7254
0.4000
0.0770
0.7246
0.4079
0.0715
5.10
0.7289
0.4000
0.1003
0.7279
0.4111
0.0937
5.15
0.7323
0.4000
0.1224
0.7313
0.4134
0.1154
5.20
0.7357
0.4000
0.1441
0.7341
0.4162
0.1336
5.25
0.7389
0.4000
0.1641
0.7373
0.4186
0.1533
5.30
0.7421
0.4000
0.1837
0.7404
0.4194
0.1722
5.35
0.7452
0.4000
0.2022
0.7431
0.4230
0.1882
5.40
0.7483
0.4000
0.2205
0.7460
0.4252
0.2056
5.45
0.7513
0.4000
0.2377
0.7488
0.4268
0.2219
5.50
0.7542
0.4000
0.2540
0.7514
0.4298
0.2369
5.55
0.757
0.4000
0.2694
0.7544
0.4295
0.2527
5.60
0.7598
0.4000
0.2845
0.7569
0.4334
0.2665
5.65
0.7625
0.4000
0.2987
0.7597
0.4359
0.2816
5.70
0.7652
0.4000
0.3126
0.7622
0.4356
0.2944
5.75
0.7678
0.4000
0.3257
0.7646
0.4378
0.3063
5.80
0.7704
0.4000
0.3386
0.7669
0.4411
0.3174
5.85
0.7729
0.4000
0.3507
0.7694
0.4424
0.3299
5.90
0.7753
0.4000
0.3619
0.7720
0.4435
0.3421
5.95
0.7777
0.4000
0.3730
0.7742
0.4463
0.3523

## [стр. 14]

Mathematics 2021, 9, 2755
14 of 17
Table 4. Cont.
Former Strategy
Proposed Method
G
D
kd
∆ig
D
kd
∆ig
6.00
0.7801
0.4000
0.3839
0.7764
0.4470
0.3626
6.05
0.7823
0.4000
0.3935
0.7785
0.4491
0.3713
6.10
0.7846
0.4000
0.4034
0.7807
0.4506
0.3809
6.15
0.7868
0.4000
0.4127
0.7828
0.4517
0.3898
6.20
0.789
0.4000
0.4218
0.7852
0.4537
0.4001
6.25
0.7911
0.4000
0.4302
0.7869
0.4554
0.4067
6.30
0.7932
0.4000
0.4384
0.7890
0.4555
0.4152
6.35
0.7952
0.4000
0.4460
0.7910
0.4571
0.4229
6.40
0.7972
0.4000
0.4534
0.7930
0.4579
0.4303
6.45
0.7992
0.4000
0.4608
0.7948
0.4608
0.4372
6.50
0.8011
0.4000
0.4675
0.7971
0.4589
0.4459
6.55
0.803
0.4000
0.4740
0.7986
0.4625
0.4504
6.60
0.8049
0.4000
0.4805
0.8004
0.4646
0.4569
6.65
0.8067
0.4000
0.4864
0.8022
0.4648
0.4629
6.70
0.8085
0.4000
0.4922
0.8043
0.4641
0.4703
6.75
0.8103
0.4000
0.4979
0.8057
0.4678
0.4739
6.80
0.812
0.4000
0.5029
0.8076
0.4667
0.4803
6.85
0.8137
0.4000
0.5080
0.8094
0.4689
0.4859
6.90
0.8154
0.4000
0.5129
0.8111
0.4678
0.4911
6.95
0.817
0.4000
0.5173
0.8124
0.4722
0.4943
7.00
0.8186
0.4000
0.5216
0.8140
0.4726
0.4988
7.05
0.8202
0.4000
0.5258
0.8157
0.4719
0.5034
7.10
0.8218
0.4000
0.5300
0.8172
0.4751
0.5073
7.15
0.8233
0.4000
0.5336
0.8189
0.4758
0.5122
In Table 4, the best parameter combination values (D, kd) obtained from both strategies
are reported. Additionally, it shows the obtained input current ripple ∆ig using those
values for every voltage gain G. From the Table, a close inspection demonstrates that the
lowest input current ripple was reached by the proposed approach for all the experiments.
These results are a consequence of the proposed optimization method's search process,
which was able to find the optimal values for the duty cycles in such a way that these values
led to a decrease in the input current ripple without a change in the required voltage gain.
The comparison between the proposed method and the former strategy, in terms of
the input current ripple obtained from the numerical experiments, is reported in Figure 7.
Figure 7a-d can be visually analyzed to observe the extent to which the proposed
method outperformed the former strategy. For every voltage gain from 5 V to 7.15 V, the
statistics show the obtained input current ripple considering both approaches, revealing
that the proposed technique found the best parameter combination to further reduce the
input current ripple.
In summary, the proposed method proved its efficiency in finding the best parameter combination to decrease the input current ripple and maintain the required voltage
gain. The experimental results support the proposed strategy, in which a different mathematical model that considers independent duty cycles, and the implementation of the
D.E. method to optimize the parameter values, achieved better results than the traditional strategy without modifying the converter at a hardware level, instead only making
software modifications.

## [стр. 15]

Mathematics 2021, 9, 2755
15 of 17
(a)

(b)

(c)

(d)
Figure 7. Input current ripple obtained from the former strategy and the proposed method: (a) for
voltage gain from 5.00 V to 5.50 V; (b) for voltage gain from 5.55 V to 6.00 V; (c) for voltage gain from
6.05 V to 6.50 V; and (d) for voltage gain from 6.65 V to 7.15 V.

## [стр. 16]

Mathematics 2021, 9, 2755
16 of 17
8. Conclusions
A novel strategy for reducing the input current ripple of the hybrid switched-capacitor
boost converter is proposed in this article. This work aims to optimize the duty cycles of
the converter by generating a new model that considers independent duty cycles. However,
finding the optimal values for duty cycles when they are independent is not an easy task.
Therefore, the proposed strategy includes the implementation of the Differential Evolution
algorithm to find the best value combination for the switching pattern to reach high quality
at the input current side while satisfying the required voltage gain.
The main objective of the proposed method is to improve the traditional strategy used
to reduce the input current ripple. This former strategy considers dependent duty cycles,
limiting the possibility of further decreasing the input current ripple and increasing the
input current's quality. Furthermore, the proposed approach does not make any changes
to the converter at a hardware level. Instead, it only makes software changes.
The proposed method's performance and the former strategy were compared under
several experiments, which considered different input voltage values to the converter. The
experiments demonstrate that the proposed technique outperforms the former strategy
by obtaining a lower input current ripple for all operating points without affecting the
required voltage gain.
In future work, an enhanced version of the D.E. algorithm or a different, more recent
algorithm can be included. In addition, several swarm-based algorithms can be implemented in order to compare their performances and analyze which could be the best option
for finding the optimal duty cycle values. The analysis can be from the perspective of the
swarm-based methods and their effectiveness when applied to this kind of constrained
optimization problem. Furthermore, if new PWM strategies are reported for the converter
understudy, a comparison against this strategy can be performed.
Author Contributions: J.C.R.-C. and P.M.G.-V. contributed to the conceptualization of the article,
from the power electronics point of view; F.B.-C., E.C. and A.M. contributed to the methodology;
E.C., A.R. and A.A.-R. contributed to the software, validation, and formal analysis; P.M.G.-V., A.R.
and J.C.R.-C. wrote the draft and prepared the manuscript. All authors have read and agreed to the
published version of the manuscript.
Funding: J.C.R.-C. would like to thank Universidad Panamericana, for their support through the program "Fomento a la Investigación UP 2021" and the project "Estrategias de reducción de variaciones
por conmutación y energía almacenada, y optimización en el diseño de convertidores de energía
eléctrica", grant number: UP-CI-2021-GDL-01-ING.
Institutional Review Board Statement: Not applicable.
Informed Consent Statement: Not applicable.
Data Availability Statement: Not applicable.
Acknowledgments: The authors would like to thank Universidad Panamericana, Tecnologico Nacional de Mexico (Instituto Tecnologico de Ciudad Madero), Universidad de Guadalajara, and
Universidad Autónoma Metropolitana.
Conflicts of Interest: The authors declare no conflict of interest.
References
1.
Arias, M.B.; Bae, S. Design Models for Power Flow Management of a Grid-Connected Solar Photovoltaic System with Energy
Storage System. Energies 2020, 13, 2137. [CrossRef]
2.
Hou, D.; Lee, F.C.; Li, Q. Very High Frequency IVR for Small Portable Electronics with High-Current Multiphase 3-D Integrated
Magnetics. IEEE Trans. Power Electron. 2017, 32, 8705-8717. [CrossRef]
3.
Ahsanuzzaman, S.M.; Prodi´c, A.; Johns, D.A. An Integrated High-Density Power Management Solution for Portable Applications
Based on a Multioutput Switched-Capacitor Circuit. IEEE Trans. Power Electron. 2016, 31, 4305-4323. [CrossRef]
4.
Kurdkandi, N.V.; Nouri, T. Analysis of an efficient interleaved ultra-large gain DC-DC converter for DC microgrid applications.
IET Power Electron. 2020, 13, 2008-2018. [CrossRef]

## [стр. 17]

Mathematics 2021, 9, 2755
17 of 17
5.
Liu, T.; Yang, X.; Chen, W.; Xuan, Y.; Li, Y.; Huang, L.; Hao, X. High-Efficiency Control Strategy for 10-kV/1-MW Solid-State
Transformer in PV Application. IEEE Trans. Power Electron. 2020, 35, 11770-11782. [CrossRef]
6.
Youn, H.S.; Yun, D.H.; Lee, W.S.; Lee, I.O. Study on Boost Converters with High Power-Density for Hydrogen-Fuel-Cell Hybrid
Railway System. Electronics 2020, 9, 771. [CrossRef]
7.
Balog, R.S.; Krein, P.T. Coupled-Inductor Filter: A Basic Filter Building Block. IEEE Trans. Power Electron. 2013, 28, 537-546.
[CrossRef]
8.
Nag, S.S.; Mishra, S.; Joshi, A. A Passive Filter Building Block for Input or Output Current Ripple Cancellation in a Power
Converter. IEEE J. Emerg. Sel. Top. Power Electron. 2016, 4, 564-575. [CrossRef]
9.
Cheng, M.; Pan, C.; Teng, J.; Luan, S. An Input Current Ripple-Free Flyback-Type Converter with Passive Pulsating Ripple
Canceling Circuit. IEEE Trans. Ind. Appl. 2017, 53, 1210-1218. [CrossRef]
10.
Kim, S.; Do, H. Soft-Switching Step-Up Converter with Ripple-Free Output Current. IEEE Trans. Power Electron. 2016, 31,
5618-5624. [CrossRef]
11.
Al-Saffar, M.A.; Ismail, E.H. A high voltage ratio and low stress DC-DC converter with reduced input current ripple for fuel cell
source. Renew. Energy 2015, 82, 35-43. [CrossRef]
12.
Rosas-Caro, J.C.; Mancilla-David, F.; Mayo-Maldonado, J.C.; Gonzalez-Lopez, J.M.; Torres-Espinosa, H.L.; Valdez-Resendiz, J.E. A
Transformer-less High-Gain Boost Converter with Input Current Ripple Cancelation at a Selectable Duty Cycle. IEEE Trans. Ind.
Electron. 2013, 60, 4492-4499. [CrossRef]
13.
Erickson, R.; Maksimovic, D. Fundamentals of Power Electronics, 2nd ed.; Springer: New York, NY, USA; Philadelphia, PA, USA, 2001.
14.
Dongyan, Z.; Pietkiewicz, A.; Cuk, S. A three-switch high-voltage converter. IEEE Trans. Power Electron. 1999, 14, 177-183.
[CrossRef]
15.
Wang, C. Investigation on Interleaved Boost Converters and Applications. Ph.D. Thesis, Virginia Polytechnic Institute and State
University, Blacksburg, VA, USA, 2009.
16.
Soriano-Rangel, C.A.; Rosas-Caro, J.C.; Mancilla-David, F. An Optimized Switching Strategy for a Ripple-Canceling Boost
Converter. IEEE Trans. Ind. Electron. 2015, 62, 4226-4230. [CrossRef]
17.
Wan, W.; Bragin, M.A.; Yan, B.; Qin, Y.; Philhower, J.; Zhang, P.; Luh, P.B. Distributed and Asynchronous Active Fault Management
for Networked Microgrids. IEEE Trans. Power Syst. 2020, 35, 3857-3868. [CrossRef]
18.
Ekinci, S.; Hekimo˘glu, B.; Demirören, A.; Kaya, S. Harris Hawks Optimization Approach for Tuning of FOPID Controller in
DC-DC Buck Converter. In Proceedings of the 2019 International Artificial Intelligence and Data Processing Symposium (IDAP),
Malatya, Turkey, 21-22 September 2019; pp. 1-9.
19.
Ekinci, S.; Hekimo˘glu, B.; Eker, E.; Sevim, D. Hybrid Firefly and Particle Swarm Optimization Algorithm for PID Controller
Design of Buck Converter. In Proceedings of the 2019 3rd International Symposium on Multidisciplinary Studies and Innovative
Technologies (ISMSIT), Ankara, Turkey, 11-13 October 2019; pp. 1-6.
20.
Hekimo˘glu, B.; Ekinci, S. Optimally Designed PID Controller for a DC-DC Buck Converter via a Hybrid Whale Optimization
Algorithm with Simulated Annealing. Electrica 2020, 8, 19-27. [CrossRef]
21.
Izci, D.; Ekinci, S.; Hekimo˘glu, B. A novel modified Lévy flight distribution algorithm to tune proportional, integral, derivative
and acceleration controller on buck converter system. Trans. Inst. Meas. Control 2021, 8, 014233122110365. [CrossRef]
22.
Izci, D.; Hekimo˘glu, B.; Ekinci, S. A new artificial ecosystem-based optimization integrated with Nelder-Mead method for PID
controller design of buck converter. Alex. Eng. J. 2021, 8. [CrossRef]
23.
Walker, G.R.; Sernia, P.C. Cascaded DC-DC converter connection of photovoltaic modules. IEEE Trans. Power Electron. 2004, 19,
1130-1139. [CrossRef]
24.
García-Vite, P.M.; del Rosario Rivera-Espinosa, M.; Alejandre-López, A.; Castillo-Gutiérrez, R.; González-Rodríguez, A.;
Hernández-Angel, F. Analysis and implementation of a step-up power converter with input current ripple cancelation. Int. J.
Circuit Theory Appl. 2018, 47, 1338-1357. [CrossRef]
25.
Karthikeyan, M.; Elavarasu, R.; Ramesh, P.; Bharatiraja, C.; Sanjeevikumar, P.; Mihet-Popa, L.; Mitolo, M. A Hybridization of Cuk
and Boost Converter Using Single Switch with Higher Voltage Gain Compatibility. Energies 2020, 13, 2312. [CrossRef]
26.
Ogata, K. Moder Control Engineering; Prentice Hall: Hoboken, NJ, USA, 2010.
27.
Storn, R.; Price, K. A Simple and Efficient Heuristic for global Optimization over Continuous Spaces. J. Glob. Optim. 1997, 11,
341-359. [CrossRef]
28.
Simon, D. Evolutionary Optimization Algorithms; Wiley: Hoboken, NJ, USA, 2013.
29.
Erik, C.; Rodriguez, A. Metaheuristic Computation with MATLAB, 1st ed.; Taylor & Francis: Boca Raton, FL, USA, 2020.
30.
Das, S.; Suganthan, P.N. Differential Evolution: A Survey of the State-of-the-Art. IEEE Trans. Evol. Comput. 2011, 15, 4-31.
[CrossRef]
31.
Pant, M.; Zaheer, H.; Garcia-Hernandez, L.; Abraham, A. Differential Evolution: A review of more than two decades of research.
Eng. Appl. Artif. Intell. 2020, 90, 103479.
