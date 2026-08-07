# Accurate Efficiency and Power Densities Optimization of Output Inductor of Buck Derived Converters

<!-- FORMULA-WARNING -->
> **Формулы в этом файле недостоверны.** Текстовый слой PDF теряет дробные черты, радикалы и группировку степеней; знак интеграла приходит как `Z` или `R`, знак суммы -- как `P`. Формул вырезано: **16**, читать их в `formulas/` (картинки 300 dpi, перечень в `formulas/INDEX.md`).
<!-- /FORMULA-WARNING -->

> Автоматически извлечено из `source.pdf` скриптом `parse_pdf.py`
> Движок: pymupdf. Страниц: 31 из 31.
> Дата извлечения: 2026-08-07 06:43 UTC

Текст не редактировался. Формулы и таблицы могут быть искажены —
при сомнении сверяться с исходным PDF.

---

## [стр. 1]

HAL Id: hal-04051084
https://hal.science/hal-04051084v1
Submitted on 28 Nov 2023
HAL is a multi-disciplinary open access archive
for the deposit and dissemination of scientific research documents, whether they are published or not.
The documents may come from teaching and research
institutions in France or abroad, or from public or private research centers.
L'archive ouverte pluridisciplinaire HAL, est destinée au dépôt et à la diffusion de documents scientifiques de niveau recherche, publiés ou non, émanant
des établissements d'enseignement et de recherche
français ou étrangers, des laboratoires publics ou
privés.
HAL Authorization
Accurate Efficiency and Power Densities Optimization of
Output Inductor of Buck Derived Converters
Hugot Pichon, Yves Lembeye, Jean-Christophe Crebier
To cite this version:
Hugot Pichon, Yves Lembeye, Jean-Christophe Crebier.
Accurate Efficiency and Power Densities Optimization of Output Inductor of Buck Derived Converters.
Applied Sciences, 2022, 12 (18), pp.9330.
⟨10.3390/app12189330⟩. ⟨hal-04051084⟩

## [стр. 2]

Citation: Pichon, H.; Lembeye, Y.;
Crebier, J.-C. Accurate Efficiency and
Power Densities Optimization of
Output Inductor of Buck Derived
Converters. Appl. Sci. 2022, 12, 9330.
https://doi.org/10.3390/
app12189330
Academic Editors: Pooya Davari,
Zbigniew Rymarski and
Zbigniew Kaczmarczyk
Received: 30 July 2022
Accepted: 10 September 2022
Published: 17 September 2022
Publisher's Note: MDPI stays neutral
with regard to jurisdictional claims in
published maps and institutional affiliations.
Copyright:
© 2022 by the authors.
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
applied
sciences
Article
Accurate Efficiency and Power Densities Optimization of
Output Inductor of Buck Derived Converters
Hugot Pichon
, Yves Lembeye
and Jean-Christophe Crebier *
G2Elab, Grenoble INP, CNRS, University Grenoble Alpes, 38000 Grenoble, France
* Correspondence: jean-christophe.crebier@g2elab.grenoble-inp.fr
Abstract: In this article, inductor loss models are developed based on the experimental characterization of off-the-shelf components. The modelling steps and techniques are described and validated. It
is shown that the model exhibits fairly good accuracy over a large range of ripple current frequency
and magnitude. Then, these models are used, as an illustration, in order to present the possible
optimization process of the tradeoff between switching frequency-current ripple magnitude and
output inductors value in the case of a Buck-derived converter. This optimization has shown that a
large current ripple may lead to minimized losses in some cases. The developed modelling technique
aims to represent Joules and iron losses, as well as DC and AC losses of inductors. It is not based
on physical behaviour description but on mathematical equations based on a set of experimental
characterizations. The modelling technique is not suitable for designing the component itself but is
useful for selecting the best component value in the manufacturer's series of components. Since it
remains difficult with the manufacturer datasheet to estimate AC losses accurately with respect to
frequency and ripple current magnitude, a specific characterization is carried out to complement the
available data.
Keywords: power electronics; design method; characterization method; ripple current; switching
frequency; power density; efficiency; design tradeoffs; off-the-shelf components
1. Introduction
Power converters are key players toward decarbonation of our modern societies
contributing, for example, to the effective usage of electrical energy in most motor drive
applications such as mobility, air conditioning, home appliances . . . For many years,
research and developments are focused on increasing the efficiency, power density and
reliability of power converters, working on materials, components, topologies and control
strategies. Nowadays, most power converters have reached excellent efficiency levels
such as in PV applications with converter efficiency ranging from 96 to 98% [1-3]. Also,
converters with very high-power densities are available. For example, three-phase Voltage
Source Inverters (VSI) have power densities above 30 kW/L [4]. Nonetheless, the quest to
improve further the tradeoff between efficiency and power density remains a specification
driver for the domain.
It is well admitted that the power density of power converters is mostly impacted
by cooling needs as well as energy storage needs. On one side, cooling is required to
remove the generated heat produced by the power converter under operation. The higher
the efficiency and/or the maximum operating temperature of components, the smaller
the cooling needs. The recent great progress on active devices, with the introduction of
Wide-Band Gap (WBG) materials and components, has introduced a shift toward higher
Figure Of Merits (FOM) and higher maximum operating temperature, opening the door for
drastic cooling needs reduction, even at higher switching frequencies [5,6]. On the other
side, energy storage in power converters is necessary to smooth and filter the voltage and
current waveforms chopped by the switching cells to pattern the power flow. Regarding
Appl. Sci. 2022, 12, 9330. https://doi.org/10.3390/app12189330
https://www.mdpi.com/journal/applsci

## [стр. 3]

Appl. Sci. 2022, 12, 9330
2 of 30
passive components, if significant progress has been reached toward better design, materials
and manufacturing technologies, a disruptive shift has still not been identified since the
introduction of ferrite materials.
It is well known that a key driver to increasing power density is to increase the
apparent switching frequencies of power converters. This can be obtained thanks to
multicell interleaved converters such as in [7,8]. Or it can be obtained more classically by
increasing the switching frequency of the power converter. If, with the introduction of WBG
devices, the increase in switching frequency can be performed at no cost in terms of extra
switching losses, on the passive components side, the quest for increasing the switching
frequency is not always a success in terms of efficiency. This is mostly due to skin effects
that increase Joules losses as well as extra core/iron losses as described in Section 3 of [9].
The impact of the frequency on the extra losses to be produced remains a difficult issue
to be precisely estimated during the design process. Indeed, the design methodologies
have a limited ability to estimate precisely the impact of switching frequency increase on
passive component losses. For power electronics (PE) converter designers, optimizing the
switching frequency with respect to efficiency remains a difficult task since no accurate
data or model, made available from the component manufacturers, is able to deliver a
representative estimate of the magnetic device losses with respect to the actual signal shape
and frequency applied to the component. As a consequence, many designers are reluctant
to increase switching frequency and/or the ripple voltage and current applied to passive
components because their high-frequency behaviour is not easy to forecast. In buck-derived
converters such as the chopper or the voltage source inverter (VSI) illustrated in Figure 1,
this may lead to a large value and size for the output inductor(s).

Figure 1. Classical Buck-derived converter topologies. (Left) a buck chopper and (right) a voltage
source inverter.
This paper is investigating the relevance to consider the design procedure only from
existing parts, trying to develop a full set of data and models directly from experiments
and characterization. Starting from "standardized" off-the-shelf components, the paper is
developing a modelling and design approach based on pre-characterized magnetic component series, allowing estimating their total losses properly for any switching frequency
and consequently any ripple current. For this purpose, the modelling technique is based
on experimental loss characterization on numerous components. From a set of measures,
completed with datasheets, a generic mathematical model is derived to express an equivalent series resistance for each component with respect to a set of fitted parameters. This
work is applied to an inductor series that is, first of all, studied to extend our knowledge
of their characteristics. In order to develop an accurate model, the step-by-step modelling
technique leads to a final characterization approach based on representative current waveforms applied to the device under test (DUT). In particular, large signals under variable
frequencies are applied in order, to sum up all possible losses induced in the DUT. For
this purpose, a particular set-up has been developed in order to measure the losses inside
the DUT in these conditions. All losses are then represented by their series equivalent
resistance which is parametrized with respect to the inductor value and the operating
switching frequency of the converter. The generic mathematical models are then applied

## [стр. 4]

Appl. Sci. 2022, 12, 9330
3 of 30
and implemented in the following parts of the paper to outline its benefits and to validate,
in real conditions its effectiveness.
In a second time, the paper describes the design optimization that can be carried
out thanks to the proposed modelling technique. The objective is to look for the optimal
trade-off between efficiency and power density, not only based on component value but
also on their actual behaviour. Existing series of components, sharing the same volume, the
same materials and the same technologies open up the opportunity to carry on a precise
and effective converter design benchmark, looking for the best compromise. Thanks to the
modelling technique numerous components and operating points are tested, looking for the
best component, minimizing losses and volume. For this purpose, at first, complementary
models are introduced in order to define the design and optimization framework. It is then
investigated which component is offering the best compromise, in terms of power density
versus efficiency from the modelling point of view. The ability to estimate inductor losses
accurately for any frequency and current ripple magnitude opens up the relevance to look
for the optimal device, leaving free to optimize the switching frequency and consequently
the inductor current ripple magnitude. In particular, it is made possible to explore a wider
range of design parameters, in a tentative to minimize chopper output inductor losses at
fixed volume, material and technology. For this purpose, a special care is given to compare
the designs with respect to a set of comparable specifications, including conducted EMI
constraints. The last section of the paper is dedicated to the experimental validation of
the approach, with efficiency measurements, based on the opposition method, in real
conditions for a set of optimal designs.
2. Data Acquisition and Model Construction
L
Main inductor, main inductor value
Rdc
Parasitic resistance of L (DC mode)
Rlr
Parasitic equivalent AC resistance of L (measured at low current ripple)
Rhr
Parasitic equivalent AC resistance of L (measured at high current ripple)
Isat
Saturation current (at 10% inductance decrease)
Pcalc
Calculated losses
Pmeasur
Measured losses
2.1. Quest for Magnetic Component Size Reduction
Single winding inductors are made out of two main parts, the magnetic core and
the winding. In power electronics, for high switching frequency operation, the magnetic
cores are mostly realized in ferrite materials while the windings are mostly made out of
copper wires. Under operation, both parts are producing losses, which have been widely
investigated and modelled in the literature [9-13]. Among them, the impact of the ripple
current, its frequency, its shape and its magnitude have drawn a significant interest [14].
Nonetheless, it remains today difficult to forecast properly what the losses are in magnetic
devices, especially the ones induced by the high-frequency part of the applied signals. In
most design procedures, the switching frequency and the ripple current are selected first
to keep reasonable AC losses. Then, the value for the inductor is derived from converter
specifications. Prototypes are then manufactured and characterized, based on allowed
volume and total losses. Nonetheless, using "reasonable" to qualify inductor losses is never
satisfactory for an engineer.
In the proposed approach, we are considering only off-the-shelf magnetic components, pre-designed, optimized and manufactured in volume. Manufacturers are producing
component series in which power electronics engineers can select the component they prefer. However, several important data are missing in most manufacturer datasheets, making
difficult the selection of the best device. In particular, component loss abacus or equivalent
models are missing. In this part, we are considering building a set of data and models, from
existing inductor series. These data will be later on used in converters' design optimization.
The characterization and modelling work has been carried out on three series of
inductors from Coilcraft manufacturers. Their datasheets are recalled in [15-17]. Some

## [стр. 5]

Appl. Sci. 2022, 12, 9330
4 of 30
relevant parameters are summarized in Table 1 below. These three series were chosen for
their advanced features such as low ESR, high-frequency working capacity, low volume
and their wide range of use. A wide range of inductance values can be seen in each series.
They are also declared by the manufacturer as using their most advanced technology.
Table 1. The main characteristics of the three inductor series considered in this work [15-17].
Manufacturer
Reference
Volume
(mm3)
Weight (g)
Inductor
Value Range
(µH)
DC Resistor
Range (mΩ)
Frequency
Range
(MHz)
MSS1210
1353
5.1-6.2
10-10,000
14-7390
4-0.2
MSS1260
777
2.8-3.3
1-1000
5.8-1295
>10-0.6
XGL6060
274
1.41-1.56
0.22-47
1.1-97
50-2
The three series pictured in Figure 2 are mapping a wide range of high-frequency
inductor values and current saturation as illustrated in the plot in Figure 3. With this set of
components, the power electronics designer has in its hands many options to design power
converters in the range of a few tens of volts and amps, leading to converters from tens to
hundreds of watts. Maximum energy density can be derived with Equations (1) and (2). In
the selected series, the volume energy density ranges from 0.2 kJ/L up to 0.35 kJ/L.
Ev = L × Isat2/V [J/L]
(1)
Ew = L × Isat2/W [J/kg]
(2)

Figure 2. Picture of the 3 inductor series considered in this work [15-17].
Looking at plots Figure 3, one can see that, globally, the maximum stored energy (in mJ)
is quite stable within a component series respectively 80, 180 and 500 mJ for series MSS1210,
MSS1260 and XGL6060. This points out that each device is individually designed and
optimized in a similar way for given material and technology. Also, it confirms that energy
density is quite dependent on the component volume of a given material and technology. In
other words, for a given series, defined by a volume, a material and a technology, the value
of the inductor is inversely proportional to the square of the saturation current. Regarding
the energy density itself, one can see that the two series exhibits similar densities while
the bigger series exhibits a fairly higher energy density. This might come from a different
material or technology or a different proportion between copper and core material.

## [стр. 6]

Appl. Sci. 2022, 12, 9330
5 of 30
Figure 3. Saturation current (at 90% nominal inductor value) versus inductor value for three Coilcraft
moulded inductor series. All data are extracted from [15-17].
Another important parameter made available by the manufacturer is the RDC, the
winding resistance in DC. Figure 4 below is providing a logarithm plot to present the
evolution of the RDC with respect to the inductor value for the three inductor series.
Figure 4. Evolution of the RDC series resistance of the inductors with respect to inductor value for
the three studied inductor series [15-17]. Also linearized RDC curves for each inductor series with
respect to inductor value.
In Figure 4, it is interesting to see that, no matter the component series, a relation may
be found between the series resistance RDC and the inductor value. A simple relationship
can be defined to link the DC series resistance of each inductor with its value as (3).
RDC = Kl × LPl
(3)
Looking at the evolution of the DC series resistance with respect to inductor value, it is
highly desirable to reduce the value of L, in a tentative to reduce the losses of the inductor

## [стр. 7]

Appl. Sci. 2022, 12, 9330
6 of 30
under operation. However, reducing the value of L without changing the switching
frequency induces an increase in the current ripple magnitude that may produce extra
AC losses in the windings and the core as it will be underlined later. To account for
this, important knowledge is missing, the evolution of equivalent series resistance of the
inductors with respect to the frequency and the magnitude of the ripple current. It is,
therefore, necessary to build this complimentary knowledge in order to identify for which
component series and for which inductor value, the power electronics designer will get the
best compromise in a converter design optimization.
2.2. Inductor Series Resistance Characterization and Modelling
The simplest model to represent magnetic component losses is based on the addition
of a series resistance with the inductor. Well parametrized, this series resistance is able to
represent the losses in the inductor with respect to the current flowing through the device.
In this part, we aim to identify a relationship between the series resistance of the inductor
and the inductor value itself. If this generic representation is possible at the inductor scale,
it will be possible to use it in the inductor component series. Considering the curves in
Figure 4, the value of RDC, can easily be derived with respect to L for any device of the
three series, applying linear regression. But it is well k-own that this DC resistance is not
representative of the actual resistor of the inductor for high-frequency currents. Skin effects
as well as proximity effects are affecting the current distribution in the wire, increasing
the apparent resistance. Also, core/iron losses are also generated when AC signals are
applied to the magnetic devices. In order to account for it, additional characterization must
be performed. The goal of the characterization test bench is to record the power losses
into the DUT with respect to realistic and/or representative current waveforms applied
to it. To do this, several characterization steps are considered. A first option can be to
measure the frequency dependence of the inductor resistance with an impedance analyser.
A second option can be to measure the actual losses in the inductor, applying a variable
ripple current over a wide frequency range and magnitude, more representative of the
actual large signals usually applied to the DUT while implemented in PE converters. The
following parts are investigating these two techniques, showing that the first one is not
sufficient to describe the characteristics of the tested inductor. It is shown that the most
accurate approach to characterize and model the inductor losses is based on a combination
of the two methods. Figure 5 presents the characterization and modelling approach used to
determine the mathematical model and parameters of the inductor losses. The characteristic
factors: RDC, Rlr and Rhr are going to be presented in the following parts.
2.2.1. Small Signal Loss Characterization and Modelling
A first characterization is made with an impedance analyser (Keysight E4990A +
Keysight 16047E from Keysight, Santa Rosa, CA, USA). A first frequency-dependent characteristic of the equivalent series resistance is obtained and depicted in Figure 6. Since the
characterization method with the impedance analyser is based on applying low-magnitude
HF currents, the obtained characteristic for the equivalent series resistance accounts mainly
for the winding resistance. The evolution of the series resistance of the characterized inductor with respect to the frequency is representative of the skin effects as well as the proximity
effects in the wire. If the skin effect is to be the major part of the frequency-dependent
resistor, this resistance is expected to evolve with the square root of the switching frequency,
as explained chapter 5.2 of [10]. As it can be seen in Figure 6, the evolution of the series
resistance appears not to be proportional to the square root of the frequency as it would be
the case if only skin effects were taken into account. This difference highlights the difficulty
to rely only on theoretical models to represent the behaviour of the inductor resistance
accurately with respect to the frequency. From this characterization, an equivalent inductor
value and frequency dependent resistor model Rlr can be derived by fitting the two parameters klr and Plr in Equation (4). In these parameters, "lr" accounts for "a low ripple"
current. This fit can be made by applying common exponential regression on the second

## [стр. 8]

Appl. Sci. 2022, 12, 9330
7 of 30
part of the curve. For the characterized inductor, the values for parameters klr and Plr are
respectively 210 and 1.5. As the principal factor frequency dependence in inductors are skin
effect and core losses, evolving respectively with the square root of the frequency [10,18]
and a power factor between one and two [11,12]. This resistance is a combination of several
physical effects with respect to the frequency, it is difficult to represent with theoretical
modelling technique without materials and winding knowledge.
Rlr( f ) = L × klr × f plr
(4)
Rtotal = R0 + L × klr f Plr
(5)

Figure 5. Characterization and modelling approach to derive the generic mathematical inductor
losses model and corresponding parameters with respect to inductor value.

## [стр. 9]

Appl. Sci. 2022, 12, 9330
8 of 30
Figure 6. Evolution of the series resistance of the MSS1210-473 47 µH inductor with respect to
frequency. Practical characterization in blue and equivalent model in dashed red.
2.2.2. Large Signal Loss Characterization and Modelling
In order to account for the impact of large signals on inductor losses, another type of
characterization is necessary. The objective is to apply a large current ripple to the inductors
to be characterized, with variable magnitude and frequency. Measuring the induced losses
will help derive a more representative model for the total losses taking place in the device
under high ripple current magnitude and variable frequency. For this purpose, the inductor is
now connected to a full-bridge inverter as depicted in Figure 7. This test bench configuration
is offering the opportunity to apply a voltage square wave to the Device Under Test (DUT)
that will in turns produce of triangular current waveform, very similar to the one taking
place in real conditions. If the applied voltage square wave is a pure AC signal, the resulting
triangular waveform will also be an AC signal with no DC part.


Figure 7. Bench topology for the inductor AC losses measurement under high ripple current and
variable frequency. (Left) the schematic, (Right) the low voltage "high" current full-bridge inverter
(30 V up to 5 A).
In fact, this test bench is producing an energy flow from the DC capacitor to the AC
inductor and vice versa. No power is dissipated by a load, except for the losses produced
by the circulation of power in the components. In this test bench, the total DC power
required to supply the full bridge inverter is measured, considering that most losses are
dissipated in the inductor. For this, the full-bridge inverter is always operating in Zero
Voltage Switching (ZVS) to minimize switching losses while active devices are oversized to
minimize conduction losses. Also, they are driven by gate drivers and a control board that
is supplied externally. In such a way, the measured losses are mainly the ones taking place
in the DUT.

## [стр. 10]

Appl. Sci. 2022, 12, 9330
9 of 30
In Figure 8a below, the blue curve with cross presents on the left the evolution of
the measured losses inside the inductor for a 1A ripple current over a frequency range
from 50 kHz to 150 kHz. In the same plot, the red curve with dots represents the losses
estimated with the equivalent series resistance obtained from the previous characterization
method. As it can be seen in Figure 8a, taking into account the measured equivalent series
resistance from Figure 5, it is not possible to derive the same amount of losses dissipated in
the inductor while performing the characterization test depicted in Figure 7. Indeed, in
the left of Figure 8 it appears that the inductor losses are significantly underestimated with
the model derived from the impedance analyser characterization. To take into account the
extra AC losses produced by the high ripple current with respect to the frequency, there
is a need to add an additional resistance to the model. For this purpose, the loss curve
is fitted by action on the two additional parameters khr and Phr in the Equation (6). The
resulting equivalent resistance is set to produce the same amount of losses with respect to
the frequency as is it shown in Figure 7, right. The total inductor resistance is now fully
described in Equation (7), also illustrated in Figure 8b.
Rhr( f ) = L × khr × f phr
(6)
Rtotal = R0 + L × klr f Plr + L × khr f Phr
(7)

(a)

(b)
Losses [W]
Figure 8. (a) Evolution of the power losses in the inductor under test for a frequency range from
50 kHz to 150 kHz. Left, comparison of the losses between the AC losses measure and the model
described with Equation (5). Right comparison of the losses between the measure and the model
described in Equation (7). (b) Equivalent impedance model of the inductor under test.

## [стр. 11]

Appl. Sci. 2022, 12, 9330
10 of 30
khr and Phr are obtained by cost function minimization coded in MATLAB with the
cost function calculated as ∑(Pmeasur -Pcalc)2. To calculate the Power losses Pcalc, the
losses caused by each individual harmonics are calculated independently and summed as
in Equation (8).
Pcalc = Pcalc =
N∗fsw
∑
f = fsw
Î௅L ( f )2 ∗Rtotal( f )
(8)
In order to check the validity of the model with respect to the ripple current magnitude,
another set of measures is conducted at 100 kHz frequency for ripple current ranging from
0.2 up to 2A. Figure 9 provides a set of curves showing in black the measured AC losses, in
blue the losses estimated with the impedance analyser modelling technique and in red the
model derived from the AC losses measurements. The bottom plot presents the relative
errors between the models. It is possible to see that the model derived from the AC losses
measurements is robust to ripple current frequency and magnitude variations. At low
ripple current magnitudes, the modelling errors are significant. This is certainly due to the
fact that losses are low and harder to measure accurately.
Figure 9. Evolution of losses into an MSS1210-473 47 µH inductor at 100 kHz over a ripple current
magnitude from 0.2 up to 2 A. The upper curve represents the losses into the inductor measured and
calculated with models of Equation (4) in blue and (6) in red. The bottom curves present the absolute
relative errors between the impedance analyser model and the AC loss model.
With this model, there is still a risk to make an estimation error since we did not
characterize the inductor losses when a strong DC current is applied in addition to the
ripple current. Indeed, the addition of the DC current plus the ripple current magnitudes
may exceed the saturation current magnitude. In this case, the inductor behaviour is no
more linear. In this paper, we are considering that the inductor is kept used in its linear
region, away from the saturation current. In this case, it is possible to consider that the
extra losses coming from the DC part of the current will only produce extra Joules losses
from the DC resistance of the inductor.
From this characterization procedure, it is now possible to extend it to the entire
inductor series from the selected manufacturer in order to develop models that can represent

## [стр. 12]

Appl. Sci. 2022, 12, 9330
11 of 30
the evolution of the losses of any inductor with respect to the applied frequency and ripple
current magnitude.
2.3. Characterization and Modelling Extension to Inductor Series
This characterization and modelling methods have been applied to three Coilcraft
inductor series named MSS1210, MSS1260 and XGL6060. The curves in Figure 10 show
the characterization results for a set of inductor values in each series. Red dashed lines are
presenting the modelled curves with the extraction of parameters listed in Table 2 hereafter.
The parameters Klr and Plr are equivalent and comparable to the logic shown in [11] as
the Klr (ki in [11]) is high for material that accepts low frequency as N87 and lower for
high-frequency materials. As well, Plr (α in [11]) is close to two for high frequency material.
These factors show that HF materials will brutally lose their interest at a given frequency
(when Rlr became predominant in front of Rhr).
Figure 10. Evolution of the losses produced by three inductors under test. Validation of the
Rdc + Rlr + Rhr model.
Table 2. Series resistance model parameters for the three manufacturer inductor series.
Inductor Series
Factor
MSS1210
MSS1260
XGL6060
Volume
 mm3
1
1353
777
274
RDC = Kl ∗LPl
Kl
1
430
700
710
Pl
1
0.915
0.915
0.915
Rlr = L ∗Klr ∗f Plr
Klr
1 × 10-3
210
88
0.3
Plr
1
1.5
1.55
1.9
Rhr = L ∗Khr ∗f Phr
Khr
1
67
45
134
Phr
1
1.049
1.089
1.028
The produced models are now ready to be used in converter design optimization. It is
important to notice that this model offers the possibility to identify the origins of losses. By
taking into account Rdc the part of the losses due to RMS currents is identified. Moreover,
with Rlr and Rhr the losses due to the high-frequen ripple current are extracted. This will
allow comparing and optimising inductor value, switching frequency, and ripple amplitude
into converters to minimize total losses.

## [стр. 13]

Appl. Sci. 2022, 12, 9330
12 of 30
2.4. Limits of the Model
This model is developed to assist designers in their choice of a magnetic component
inside a predefined, preselected series of components. Since it requires significant characterization work, the selection of component series must be performed prior to its detailed
characterization. This is the reason why the modelling technique developed here is mostly
applied in the paper to carry component value selection rather than component technology
selection. Of course, one can still explore and compare component technologies with this
modelling technique. Also, at this stage of the modelling development, this model does
not consider exceeding saturation limits nor the maximum frequency range, each time it
has an effect on the inductor value, out of the linear region. The more the inductor will
be used under the condition that exceeds linearity, the less the model will be efficient.
J. Kaiser & T. Dürbaum [19] presented an overview of the uses of saturable inductors. It is
complementary to this work as it relates results out of its scope.
3. Complementary Model Description
Cx1, Cx2
Values of the filtering capacitor
ECoss, ECiss
stored energy into parasitic capacitors
Isw
Switched current
IL
Current flowing through L
L
Value of the main inductors
L f ilter
Value of the filtering inductors considered as 1 inductor
Rlisn100
Total output resistance of the LISN (100 Ω)
tdt
Dead time
Vdrop
Voltage drop due to body diode
VDS
Drain-Source voltage
Vlisn
Voltage measured on one LISN resistor (50 Ω)
3.1. Design Frame Considerations
As introduced in Section 2, during power converter design, the selection of the optimal
inductor value relies on the operating conditions and the design specifications in terms
of targeted power density and efficiency. Playing with switching frequency and current
ripple magnitudes impacts on many other elements of the design. It is well known that
increasing the switching frequency may induce extra switching losses in active devices.
Also, increasing current ripples will increase RMS current, which in turn, will produce
extra conduction losses in all devices, including active devices. Nonetheless, as mentioned
in the introduction, it is believed here that thanks to the introduction of WBG devices, it
is today possible to increase RMS current and switching frequency without producing
extra losses in active devices compared to the state-of-the-art silicon-based active devices.
Nonetheless, for the purpose of validation and illustration, active device switching and
conduction losses must be taken into consideration in the design and optimization process
of a power converter. For this, a simple model is proposed in the following part.
Second, increasing switching frequency and inductor current ripples will have an
impact on the converter conducted EMI. In particular, differential mode conducted EMI
is strongly dependent on the input inductor size in most Buck-derived topologies such
as the well-known Voltage Source Inverter (VSI). It is therefore important to consider in
this work a max value for the current ripple exiting the converter. In other words, if the
optimization process of the inductor leads to a large ripple current, way above reasonable
limits, an extra-filtering stage will have to be considered and added to the comparison. An
important part is provided below to settle properly how EMI constraints are taken into
account for the selection of the optimal inductor value.
These design considerations are going now to be developed in order to be taken into
account for the selection of the optimal inductor value and then designing a buck-based
power converter.

## [стр. 14]

Appl. Sci. 2022, 12, 9330
13 of 30
3.2. Active Device Losses in the Converter
The losses of active components are partially frequency-dependent. These are called
switching losses.
There are a lot of complex models able to describe switching
losses [8,20-22]. For silicon MOSFET power devices operating under a very fast switching
transition, a simple one is to consider the switching losses with respect to the stored energy
into parasitic capacitor Coss. Since Coss is a nonlinear capacitor, special care must be paid
to estimate the energy stored in the Coss. From MOSFET manufacturer datasheets, one can
derive the total energy stored in Coss, using Equation (9). Considering that each time the
transistor switches ON, the entire energy stored into Coss is dissipated through the channel
of the device [20,22], then switching losses can be derived thanks to Equation (9) below.
This switching loss modelling technique is valid only if the MOSFET is switching very fast.
The transistor used to make the test bench being (SIS862DN-T1-GE3), the stored energy
in Coss can be extracted from the datasheet according to the curve pasted in Figure 11.
Parameters in Equation (12) are derived to fit Coss versus Vds. Transistor gate drivers are
also dissipating the loss function of the switching frequency. In the transistor datasheet, the
stored charge can be easily derived from tables and abacus. For hard switching operation,
both losses must be taken into consideration. For soft switching, only driver losses must
be considered.
Additional losses must be taken into consideration. When MOSFET-MOSFET switching transitions are considered, a short deadtime is nonetheless necessary to avoid short
circuit operation [20]. At each switching time, a dead time of 100 ns is applied between
off and on. This dead Time is necessary to prevent cross commutation in hard switch and
allows ZVS switching but causes body diode conduction [23,24] making extra losses. These
losses are considered in Equation (11).
ECoss =
Z Vmax
0
Coss(vDS)vDS dvDS
(9)
ECiss = Qiss × vGS
(10)
Ebody = tdt × Vdrop × Isw
(11)
Coss(VDS) = 760 -VDS
760 -400
760
+ exp-(VDS∗0.17-6.7)
(12)
Figure 11. Coss of the transistor SIS862DN-T1-GE3 versus Drain-source Voltage from Equation (12) in
red and from component datasheet [25] in bleu.

## [стр. 15]

Appl. Sci. 2022, 12, 9330
14 of 30
Equation (12) is a mathematical representation of the non-linear capacitor Coss, following its evolution with respect to Drain Source voltage across the MOSFET. It is illustrated
in Figure 11 below.
3.3. Setting the EMI Constraints
As mentioned above, a clear design frame must be defined in order to take into
account the impact of frequency and inductor ripple magnitude on conducted EMI. For
this purpose, it is defined that the output ripple current going out from the converter must
not exceed some limits. Taking into consideration conducted EMI regulations [26,27], in
a tentative to make it clear and simple to use in the inductor value selection process, it
has been defined that the current harmonics are going out of the power converter, flowing
into the two 50Ωresistors of a conducted EMI testing equipment, should not exceed
60 dBµV no matter the frequency considered. These choices are slightly different from the
regulations. Nonetheless, they are offering a realistic reference that eases the design and
optimization process. Figure 12 below presents the schematic of a typical differential mode
(DM) input filter circuit inserted between the converter itself and the LISN (Line Impedance
Stabilization Network) testing equipment considered for conducted EMI compliance.
Figure 12. Schematic of a VSI + its differential mode input filter for conducted EMI compliance + the
LISN resistors (LISN simplified representation in high frequency range).
In this schematic, a traditional differential mode filter topology is considered, with
symmetric input inductors L (one on the phase and one on the neutral) together with
Cx1 and Cx2 capacitors for DM current ripple filtering, between the converter and the
LISN, used for normative tests. In the upper-frequency range, above 100 kHz, the LISN
looks similar to a set of two 50 Ωresistors, from which, one can measure the current
flowing through. Setting the limit at 60 dBµV across each LISN resistor means that the
maximum current ripple harmonic must not exceed 2µA. If the input inductor current
ripple magnitude is higher, the Cx1 and Cx2 capacitors will have to be adjusted to filter the
current harmonics. If the Cx capacitor value exceeds 20 µF, extra L f ilter filtering inductors
will have to be inserted between Cx1 and Cx2 in order to increase the global filter order
as shown in Figure 13. A limit for Cx has been introduced because large Cx capacitors
have low resonant frequencies, preventing them from a satisfactory filtering over a large
frequency range.
The Equation (13) below presents the ideal attenuation with respect to the frequency
offered by a Cx capacitor filter topology, considering Cx equals Cx1 + Cx2.
Vlsin
IL
=
(Rlisn100/2)
1 + Cx × Rlisn100 × jω
(13)

## [стр. 16]

Appl. Sci. 2022, 12, 9330
15 of 30
Figure 13. Frequency domain representation of 1A magnitude at 83% duty cycle filtered by a Cx
capacitor of 40 µF or by a Cx1 -L -Cx2 filter (Cx1 = 20 µF, L = 3 µH, Cx2 = 20 µF) to meet the 60
dBµV limits using Equation (15) to calculate the value of L.
Please note that the LISN total resistor is 100 Ω, the sum of two 50 Ωresistors. However,
the probe is inserted across one of the two resistors, justifying the factor 2 in Equation (13) above.
Also, in Equations (13) and (14), IL is the current flowing in the inductors of the chopper.
Equation (14) below presents the ideal attenuation with respect to the frequency offered
by a Cx1 -L f ilter -Cx2 filter topology. The operation to select the minimum inductor value
for this filter is described in the following Section 3.3.2.
Vlsin
IL
=
(Rlisn100/2)
1 + jω
 Rlisn100Cx1 + Rlisn100Cx2
 -ω2

L f ilterCx2

-jω3

Rlisn100L f ilterCx1Cx2

(14)
3.3.1. Values of Filtering Components and Design Considerations
To be able to compare the different design optimization choices (frequency and ripple
associated with an input inductor) it has been chosen to use a 2 × 20 µF Cx capacitor filter
when sufficient or a 20 µF -X µH -20 µF for higher ripple current. The extra losses and
volume produced by the addition of L f ilter inductors will be taken into account during
design optimization.
3.3.2. Modelling of Additional Losses Resulting from Filtering
The implementation of the DM filter induces additional losses due to current flow
through additional capacitors and inductors. These passive components can also be represented by equivalent series resistance (ESR) to account for extra losses. Due to the evolution
of the filter depending on the frequency and the amplitude of the current ripple, it is
necessary to estimate these additional losses for each case. The current flowing through the
filtering inductors L f ilter is the full current filtered as described in Equation (15).
IL f ilter
IL
=
1
1 + Cx1
Cx2 -ω2L f ilterCx1
(15)

## [стр. 17]

Appl. Sci. 2022, 12, 9330
16 of 30
The minimal standard value of L matching the condition of switching frequency first
harmonic under 60 dBµV on two RSIL resistors from Equation (16) is then selected:
L f ilter >

IL×R
2Vmax(1+iωsw×R×Cx2) + 2
-ω2sw × Cx2

(16)
With Vmax = 1 mV = 60 dBµV.
The losses due to these components are calculated using the same process as the one
used for the output inductors L developed in Section 2.
3.3.3. Filtering Capacitor Losses Modelling
Filtering capacitors are usually high-quality components, with fairly low equivalent
series resistance (ESR). Nonetheless, large ripple currents may flow in these components
making it necessary to estimate their losses accurately. For this purpose, manufacturers
provide ESR of their capacitors. From their characteristics, it is possible to derive a representative ESR model. In our experiments, we are using ceramic capacitors from the manufacturer
Murata. Murata is providing accurate ESR curve for all its components from a web application [28]. In Figure 14 below are plotted a set of ceramic capacitors ESR versus frequency.
102
104
106
108
1010
frequency [Hz]
10-3
10-2
10-1
100
101
102
103
ESR of a 10uH 100V Ceramic Capacitor
manufacturer documentation
manual interpolation
Figure 14. Ceramic capacitor equivalent series resistance with respect to frequency. (Left), manufacturer data, (right), equivalent model representation for the series resistance with respect
to frequency.
Since the various ceramic capacitors have a comparable ESR, the model considered
here, will be the same for all capacitor values.
The chosen interpolation curve (in red) follows the mathematical variation of
Equation (17) below.
This curve has been manually fitted with Rc0
=
0.0012;
kc1 = 112; kc2 = 160E3. With kc1 and kc2 fixed to match the elbow.
ESR( f ) = Rc0 +
p
f
kc1
+ kc2
f
(17)
In order to derive losses in Cx capacitors, the RMS current in each component must
be derived. If no L f ilter is inserted, the current flowing through the capacitors Cx1 and Cx2
is the one flowing inside inductors L. Therefore IL = IC1. If L f ilter are inserted, the currents
flowing inside Cx1, Cx2 and L f ilter must be derived. IL f ilter is derived thanks to Equations (18)

## [стр. 18]

Appl. Sci. 2022, 12, 9330
17 of 30
and (19). Cx1 capacitor current is the difference between IL and IL f ilter. As well, Cx2 current is
expected to be the same as IL f ilter. These Equations are supposing an open output load.
Ic1
IL
=
C1
C2 -ω2LC1
1 + C1
C2 -ω2LC1
(18)
Ic2
IL
=
1
1 + Cx1
Cx2 -ω2LCx1
(19)
3.4. DC Resistance of the Converter
Due to the modularity of our test bench, there are a total of 10 connector's contacts
in series with the main current way causing a not negligible DC resistivity. A measure of
this total resistor has been made in DC with a shorted output at 3 A. the parasitic series
resistor has been measured as 60 mΩ(180 mV). Considering the 2 × 10 mΩdue to the
transistor (SIS862DN-T1-GE3) commended with a grid at 6.5 V. It is undoubtedly that the
conception of the test bench, by adding 40 mΩ, will result to overestimate the losses due to
RSM-current in regard to an optimal full soldered design.
3.5. Limits of the Models Considered in the Optimization Loop
The scalability of the models is discussed in this paragraph. Regarding the modelling
technique of inductors, its scalability is possible as long as the component usage remains
in the linear region with respect to inductor value. This means that the model will need
to be improved if the devices are used in the saturation region or with high switching
frequencies that significantly impact its behaviour. Regarding the other models considered
in the optimization loop, it was not our purpose to propose a universal modelling technique
for all components. In particular, our aim was mainly to implement and illustrate how
useful and effective the proposed modelling technique is for inductors. In this respect,
the simplicity of the loss model used for active components is not going without strong
limits. It is used here under specific conditions. The switching time in hard switch mode
is considered under 10 ns keeping switching losses low. When the DC supply voltage
becomes higher, it is rarely possible to force the switching time to be this low due to higher
grid capacitor and EMI considerations. To be able to use a complete model of converter
losses at a higher voltage or with cheaper components, the user should use a more accurate
model for active components [21,29].
4. Theoretical Optimization of Converter Inductor
Thanks to accurate losses modelling of inductor series together with input filter
components, it is now possible to look for the optimal trade-off in terms of switching
frequency and current ripples in the inductor while designing a buck-derived power
converter. It is a partial design optimization since only input inductors + input DM filter
are considered and selected in this paper. Nevertheless, it will be shown that it provides
interesting optimization results. Also, this design optimization procedure may take part in
a more global converter optimization work.
4.1. Frequency and Ripple Optimization for One Inductor Value
With the models that have been established in Sections 2 and 3 based on characterizations, a theoretical optimization of a symmetric DC to DC converters (two interleaved
choppers) is presented in this part. This optimization aims to minimizthe e losses at input
inductors + filter stage while keeping volume minimal. For this purpose, considered losses
include losses in inductors L, in Cx1 and Cx2 capacitors and in L f ilter inductors when applicable. As the losses due to Cx2 are not dominating (<<1%) and these losses should not
become significant no matter the frequency and current ripple in the inductor L, the losses
will be considered as if the converters were not interleaved. Also losses in the converter

## [стр. 19]

Appl. Sci. 2022, 12, 9330
18 of 30
due to transistors DC resistance, as well as switching losses due to hard switch modes and
transistors gates losses will be considered as described in Section 3. These losses will be
calculated for each combination of ripple current amplitude and switching frequency.
4.1.1. Losses in the Main Inductors
The following operating point is considered for the design optimization: Vin = 30 V,
Vout = 20 V, ⟨Iout⟩= 2.5 A. For a given inductor value of 47 µH, the losses in the output
inductors with respect to frequency are provided in Figure 15 below. One can see in the
plots the losses due to the DC current (left), the losses due to HF current harmonics (centre)
and the total losses in the inductors (right). It appears that no matter the type of losses,
they all decrease with respect to the frequency. Indeed, increasing the switching frequency
reduces the ripple current magnitude, which in turn reduces the RMS current value. This
has a direct impact on the DC losses. Looking at HF losses, on one side, increasing the
switching frequency increases ESR resistance (representing core losses and skin effects) but
it also reduces the magnitude of the current harmonics. All in all, the higher the switching
frequency, the lower the HF losses. Total losses are therefore decreasing with respect to
switching frequency.
Figure 15. Inductor losses calculated for the two MSS1210 inductors of bidirectional full bridge
converter working under 30 V input with 20 V output at 2.5 A.
4.1.2. Active Device Losses in the Converter
Considering Section 3.4, the energy of transistors switching has been extracted from
the datasheet of the transistors as illustrated in Table 3. This model might be quite simple
but is not subject to important variation and produces representative results as long as the
assumptions introduced in Section 3 are valid. At each switching period, this energy is lost
twice. Because at each commutation there are two switching events.
Table 3. Energies lost at each commutation due to Coss, Ciss and body diode conduction.
Parasitic Capacitor
Coss
Ciss
Transistor Body Diode
Voltage
30 V
6.5 V
0.7 V
Stored energy
287 nJ
81 nJ
70 ∗Isw nJ

## [стр. 20]

Appl. Sci. 2022, 12, 9330
19 of 30
Figure 16 presents the switching losses into the active devices caused by these three
factors in the case where a 47 µH inductor has been chosen. As expected, in the curve in
Figure 16, the active device losses are increasing with increasing switching frequency.
Figure 16. Switching losses made by the four transistors depending on the switching frequency in a
converter using two 47 uH main inductors.
4.1.3. Losses in the Differential Mode Filter
In Section 3 the modelling technique to derive the losses in the differential mode filter
with and without L f ilter was introduced. L f ilter inductor values are chosen for the XGL6060
component series and capacitors are paralleled 10 µF ceramic capacitors. In order to account
for capacitor derating with respect to the voltage rating, six 10 µF ceramic capacitors are
used to implement a 20 µF Cx capacitor (at 20 V). Figure 17 below presents the evolution
of the losses inside the DM filter with respect to the frequency for the operating point
defined above and for main inductor values L = 47 µH. In this particular case, the value
for the filter inductor L f ilter is adapted with respect to the ripple current flowing across the
main inductor L. This is the reason why there are different slopes in Figure 17. As can be
observed in Figure 17, the filter losses are also decreasing with respect to the frequency.
Figure 17. Losses caused by the two filtering inductors depending on the switching frequency in a
converter which 2 × 47 µH main inductors.

## [стр. 21]

Appl. Sci. 2022, 12, 9330
20 of 30
Increasing the frequency leads to reduced ripple current which in turn leads to reduced
HF losses in the filter.
4.1.4. Optimal Switching Frequency for the Specific Inductor
To finalize the design optimization with the operating point defined above and the
47uH inductor considered as a first example, all losses are computed. Figure 18 is presenting
the resulting total losses with respect to the frequency and the ripple current magnitude. As
expected, the losses are reducing with respect to the switching frequency up to a minimum
value. Then losses are rising again with respect to switching frequency. We can see that
for this specific inductor value the optimal operating point is a little bit over 1 A of current
ripples (>40% of the DC current in the example).
104
105
Switching Frequency
0
1
2
3
4
5
6
7
8
9
10
Total losses for the 50W 2X47µH converter
Evolution of the current ripple magnitude
Total losses
Current ripple
Figure 18. Calculated total losses into the full-bridge converter considering all losses modelled in
Section 3. These losses are considered for a 30 V to 20 V, 50 W converter equipped with 2 × 47 µH
main inductors.
From this first result, it appears that reducing the ripple current would lead to minimum losses. It is interesting to notice that quite reduced ripple current may not lead to
minimum losses in this particular case. Nonetheless, it is important to keep in mind that
the differences are not very important and could come from uncertainties. Let us now
investigate what design optimization we can reach if an entire inductor series is considered.
4.2. Application to the Three Sets of Inductors
With the example of a switching frequency optimization made with one specific 47 µH
inductor from Coilcarft MSS1210 series, it is now possible to apply this work to the three
series of inductors considered in this paperwork. This part will propose an optimization
result of the F-R-Oi (Frequency Ripple Output inductor) for the losses into the bidirectional
50 W, 30 V to 20 V converter.
4.2.1. Losses in the Main Inductors
Similar to Section 4.1.1, the losses in the main inductors have been calculated for each
series and are presented in Figure 19 with respect to switching frequency. Purple curves
represent the 47 µH values (as in Section 4.1). These curves show that due to the rising of
Rlr and Rhr with the frequency, there is a rise in the losses at low switching frequencies (left
side of each curve). The losses for each inductors value will decrease with the frequency
increase (leading to a reduction of the ripple current) down to losses due to RDC These
results are comparable to [18] as it shows the equilibrium between skin effect and losses
due to current ripples. However, the interesting part of each value is where the loss into
the inductor is lightly dependent on the Frequency-Ripple-Output inductor (F-R-Oi).

## [стр. 22]

Appl. Sci. 2022, 12, 9330
21 of 30
Figure 19. Losses into the main inductors, for multiple inductor values in the three series.
Decreasing the inductor value will decrease the losses at the same frequency if the
losses due to Rhr + Rlr are not prevalent.
4.2.2. Active Device Losses
As presented in Section 3, the active device losses are dependent on the switching frequency. It grows higher with the frequency (with the exception of full ZVS mode). For each
inductor value, a step due to ZVS mode is placed at a different frequency (see Figure 20), it
is explained by the fact that the ZVS appear at iso-ripple and not iso frequency. The rising
of the frequency will be opposed to the benefit of the F-R-Oi shown in Section 4.2.1.
Figure 20. Active device switching losses for a 50 W-30 V to 20 V converter with respect to the main
inductor value and the switching frequency.

## [стр. 23]

Appl. Sci. 2022, 12, 9330
22 of 30
4.2.3. Losses in the Input Filter
As presented in Section 3.3, the minimum filtering inductor value needed to comply
with the 60 dBµV has been calculated for each F-R-Oi value. Losses due to this filter have
been calculated accordingly. Thanks to the high quality of ceramic capacitors and their low
relative ESR, the prevalent part of the losses in the π filter is due to the RDC part of the filtering
inductors' ESR. The estimated losses inside the filter are presented in Figure 21. The steps on
each curve are the result of a decrease in value implying a decrease of RDC. While at the same
ripple, the value of the main inductor is low, the frequency is high. This means that the value
of the filtering inductor is lower, lowering the global losses. However, for an iso-frequency,
the lower the main inductor value is, the higher the value for the filter inductor.
Figure 21. Losses in the output filter depending on the main inductor values (coloured curves) with
respect to the switching frequency. The filtering inductor values are the minimum discrete standard
values complying with the 60 dBµV limits at LSIN resistors as proposed in Section 4.1.
4.2.4. Optimal F-R-Oi
From the three previous Sections 4.2.1-4.2.3 and according to Section 4.1.4, it is then
possible to calculate the total losses in the converter processing 50 W from 30 V to 20 V. It
includes the losses in the main inductors, the active components, the output filtering stage
and the parasitic DC resistance of the converter. With the values shown on Figure 22, it is
possible to conclude the theoretical optimal Frequency-Ripple-Output Inductor (F-R-Oi)
and compare the different off-the-shelf inductors and select the one that would offer the
best compromise.
Although the different series have different volumes, it is interesting to note that the
losses on the optimum are around the same value for the three inductors series. But the
lower the volume is, the lower the optimal inductor value is, and the higher the ripple
current is. The optimum can be found around a switching frequency of 100 kHz. Figure 23
presents the same result as the frequency is linked to the ripple current by the inductor
value. As the optimum switching frequency is around 100 kHz, the optimum ripple
current magnitude is around 1.25 A for an average current of 2.5A. Therefore, the optimal
ripple current magnitude seems to be located at about 50% of the average current in this
particular design case study. This is significantly higher than what the power electronic
design engineer considers, usually more in the range of 10 to 25%. It is even above the
standard recommendation of 20 to 40% proposed by manufacturers as in [30-32]. With
these considerations, for each series, an optimal working point has been found with a pair
of 22 µH inductors and losses extracted in Table 4.

## [стр. 24]

Appl. Sci. 2022, 12, 9330
23 of 30
Figure 22. Total mosses modelling results for the three inductor families. Total losses are represented
as a function of the switching frequency and the inductor values.
0
2
4
6
Current ripple
magnitude [A]
0
0.5
1
1.5
2
2.5
MSS1210
4.7uH
10uH
22uH
47uH
100uH
0
2
4
6
Current ripple
magnitude [A]
0
0.5
1
1.5
2
2.5
XGL6060
4.7uH
10uH
22uH
47uH
0
2
4
6
Current ripple
magnitude [A]
0
0.5
1
1.5
2
2.5
Total losses - current ripple representation
MSS1260
4.7uH
10uH
22uH
47uH
100uH
Figure 23. Model results for the three inductor families. Total losses are represented as a function of
the Current Ripple and the inductor values.
Table 4. Calculated losses at global optimums for each series and individual main inductor losses at
these optimums.
Serie
MSS1210
MSS1260
XGL6060
Optimal
total losses
1.38 W
1.44 W
1.28 W
Main
inductor losses
2 × 0.37 W
2 × 0.40 W
2 × 0.32 W
Before concluding this design and selection process, it is needed to check if the selected
inductor is able to handle the heat that will be produced under operation. For this purpose,
it is needed to check if, from a thermal point of view, the design compromise is feasible.

## [стр. 25]

Appl. Sci. 2022, 12, 9330
24 of 30
4.3. Thermal Considerations
Another dimensioning factor of magnetic devices is the thermal behaviour of the
component during operation. It is important to check that even if the design optimization
tends to minimize the losses in the components, still the produced heat does not induce
an operating temperature above limits. For this purpose, the Coilcraft® datasheet has
been analysed further in order to extract an approximation of the thermal resistance of
each inductor series. The link between DC current magnitude, the DC resistance of the
component and component temperature increase is used to estimate the thermal resistance
of each component. Figure 24 below presents the evolution of the DC losses with respect
to the value of the inductor for a temperature rise of 20 ◦C and 40 ◦C based on datasheets.
The curves are flat, validating that the total amount of allowed losses per inductor shape
(per inductor series) is constant. From these plots, one can derive the equivalent thermal
resistance using Equation (20) below easily. These thermal resistances are listed in Table 5.
Rth =
∆T
(I2 × Rdc)
(20)
0
500
1000
Inductance [uH]
0
0.2
0.4
0.6
0.8
1
1.2
1.4
1.6
1.8
2
MSS1210
0
100
200
300
400
Inductance [uH]
0
0.2
0.4
0.6
0.8
1
1.2
1.4
1.6
1.8
2
MSS1260
0
10
20
30
40
Inductance [uH]
0
0.2
0.4
0.6
0.8
1
1.2
1.4
1.6
1.8
2
XGL6060
+20°
+40°
Figure 24. Maximum losses allowed in the inductor for various inductor values and for two temperature rises. Data extracted from datasheets [15-17].
Table 5. Median thermal resistance of copper to the core in MSS1210, MSS1260 and XGL6060 series.
Series
MSS1210
MSS1260
MSS6060
Median of the thermal resistance Rth(◦C/W)
at +20◦
75
79
26
Median of the thermal resistance Rth(◦C/W)
at +40◦
80
83
29
It is interesting to note that the inductor series with the largest dimensions seems to
have a higher thermal resistance than the two others. This is somewhat strange and we
were not able to provide a justification for this.
With these thermal characteristics, it is possible to verify the thermal behaviour of
the magnetic component under the stress caused by the converter action. Under optimal
configuration, for the 50 W converter, each inductor's power loss and thermal rising are
presented in Table 6. These temperatures being under the manufacturer's limits, there is no
reason to dismiss one of these technologies during the optimization process.

## [стр. 26]

Appl. Sci. 2022, 12, 9330
25 of 30
Table 6. Thermal rising of a 22 µH selected during optimization process of the 50 W converter.
Series
MSS1210
MSS1260
MSS6060
Inductor losses (W)
0.37
0.40
0.32
Thermal rising (◦C)
27.8 to 29.6
31.6 to 33.2
8.3 to 9.3
To conclude this third part, the inductor model was successfully used to select the best
inductor value, together with the converter switching frequency in order to minimize the overall
losses. It was shown that, in the particular design and optimization case study considered here,
the selected inductor and switching frequency may lead to significant current ripple magnitude
in the inductors. This conclusion needs now to be validated with experiments.
5. Experimental Validation, Using Power-Cycling Converters
In this last part, the design optimization made in Section 4 will be illustrated and
analysed with an experimental test bench where the measures of the losses of a full converter
will be acquired and the search for the optimal operating point and design compared to the
model optimization results. Some configurations will be tested to discretize the result and
verify that the losses are in range with the calculation. Moreover, consolidated local and
global optimum configurations will be checked throughout the experimental results.
5.1. Validation Setup Presentation
5.1.1. Opposition Method
The test bench that will be used for the experimental validation of the design optimization is based on the opposition method. It is made out of two equivalent converters, one
feeding the other as illustrated in Figure 25. The first conversion unit is a DC to DC step
down converter with energy flowing from the source to the central capacitor. The second
one works as a step up converter sending back the energy from the central capacitor to the
source. Tow DM filters are also inserted between the two converter stages in order to take
the corresponding losses into account. A voltage source is used to supply power losses,
to maintain the voltage at the right level. Thanks to this test bench, measuring the power
delivered by the DC source and measuring the power transferred to the middle point DC
link, it is possible to derive the global efficiency of the two converters and from this to
derive the efficiency and the losses of each of them, making the assumption that the losses
are equally shared between the two conversion stages. A picture of the test bench is given
in Figure 26. For these study cases, the main inductors L are the ones named over each
result cur. Each Cx capacitors are 20 µF ceramic capacitores, and each filtering inductor is
taken from the XGL6060 series, chosen with Equation (16).

Figure 25. Schematic of the opposition method to characterize converter losses.

## [стр. 27]

Appl. Sci. 2022, 12, 9330
26 of 30

Figure 26. Picture of the test bench with the two TI controllers, one for each converter and in between
the two converters, one feeding the other.
5.1.2. Losses Measurement
To measure the losses, the source voltage is measured across the input capacitor
terminals noted V-in on the schematic Figure 25. the current consumption is measured
filtered by a second order filter to measure only the DC current as it represents the losses
dissipated in the converters under test. Regarding the measurement of the power flow, the
Vout DC voltage of the Cx2 capacitor is measured with a voltmeter and the current flowing
into the filtering inductor (on the left in the schematic Figure 25) is measured continuously
with an accurate ampere meter.
5.2. Experimental Losses Measure
A set of Frequency-Ripple-Output-Inductor (F-R-Oi) operating points have been
defined and characterized by the opposition method in order to check if they are actually
optimal. Losses have been measured for these points and are presented in Figures 27 and 28.
Figure 27 represents converter losses curves for the following operating point: step down
30 V to 20 V under <2.5 A> output current for various inductor values. These values have
been chosen to be compliant with the bench limits (switching frequency) and the limits
of inductors (saturation). These inputs have been validated by the simulation results as
Figure 28 presents the same curves for <1 A> output current. The model calculations and
measures are plotted and compared with respect to current ripples, keeping in mind that
for the same inductor value, frequency and ripple are linked. In the plots, dashed curves
with circles are coming from measurements whereas full lines are modelling results coming
from previous parts. Not all inductors have been measured since this is representing a lot
of operating points and measurement set-up.
These measures are highly sensitive to the output DC current level. This variable can
hardly be measured with better precision than 2% (50 mA in our case) and made it difficult
to set precisely the operating point. Combined with high RDC, this lack of precision is the
weakest spot of the measurement process. Nonetheless, the results provide that the model
calculations are in satisfactory accordance with the experimental results. Also, the different
curves prove the ability of the modelling and design optimization method to identify the
best inductor value and the minimum total losses with respect to ripple current magnitude
since both theoretical and experimental curves are pointing to the same optimal point.

## [стр. 28]

Appl. Sci. 2022, 12, 9330
27 of 30
Total losses [W]
Figure 27. Optimization results compared with experimental measurements (curves with circles).
For one converter processing, 50 W from 30 V to 20 V. Measure are carried out with back-to-back
method. The results are plotted with respect to current ripples into the main inductors.
Total losses [W]
Figure 28. Optimization results compared with experimental measurements (curves with circles).
For one converter processing, 20 W from 30 V to 20 V. Measures are carried out with the back-to-back
method. The results are plotted with respect to the current ripple magnitude into the main inductors.
In Figure 27, it appears clearly in the plot for XGL6060 that lowering the value for the
main inductor down to 10 µH, with a ripple current magnitude of about 80% of the average
output current is almost leading to the minimum total losses in the converter. In addition
to being the smaller component series, the smallest component in the series appears to be
the best compromise in terms of volume and total losses, keeping in mind that the output
filter has been taken into account.
Again, in Figure 27, it is clearly visible that there is always an inductor value which
is optimal for a significant ripple current magnitude, more in the range of 40 to 80%,
significantly larger than the ripple current magnitude usually considered in best practice
designs. This clearly outlines the interest to add knowledge on the inductor characteristics
in order to really explore the solution space and look for the best compromises. Using an

## [стр. 29]

Appl. Sci. 2022, 12, 9330
28 of 30
off-the-shelf component series. Implementing AC loss characterizations is a useful generic
work in order to later carry on multiple design optimizations.
In Figure 28, with a lower average output current, it is still possible to see that large
ripple currents are leading to optimal tradeoff for each component series. Also for this
specific operating point, the optimal design leads to large inductor values, one can still see
that XGL6060 components, which are the smallest, are leading to minimal total losses with
large ripple current magnitudes, in the range of 100% of the average output current. These
numerous experiments are validating the interest of the modelling method and the interest
of the design engineer to extend the knowledge of components from experiments in order
to carry on optimal design and tradeoffs.
The limits of the model are seen between Figures 27 and 28. As in Figure 28 the losses
are accurately modelled. However, due to the high DC current bias, in Figure 27, saturation
presses begin to appear. Therefore, the losses are lightly underestimated in this condition.
The more the saturation process is advanced the more the error is important, as it can be
seen comparing MSS1260-47 in yellow against MSS1260-22 in red.
5.3. Future Applications
This work has been fulfilled in order to be applied to the team's actual development.
It will have a direct interest in the development of DC-AC standard conversion cells (CSC)
for Power Converter Arrays (PCA) [33]. This optimisation method will help in selecting the
optimal AC side input inductors in multilevel converters. It can also be used in combination
with the analysis of different control strategies as zero voltage or current switching where
large di/dt is usually required as illustrated in [34-36]. Also, as mentioned above, it will
help to compare inductors technologies for future development. We expect that with
more accurate active component models, the scope of the work could be extended to a
higher-voltage converter. Finally, a high-frequency test bench will be necessary to extend
the proposed model to wide-bandgap converters as we expect small standardized parts
will gain in popularity with increased switching frequencies, and multicell conversion
techniques [37-39].
6. Conclusions
In this paper, two complementary parts have been developed in order to outline the
methodology to select the optimal inductor value from off-the-shelf component series. The
first part was dedicated to enlarging the knowledge available to carry on the inductor
value selection. For this purpose, a simple modelling method was proposed to derive a
generic and accurate mathematical model of the inductor total losses. It is based on the
definition of an equivalent series resistance, parametrized with respect to the inductor
value and the switching frequency of the converter. All parameters were derived using
experimental characterizations. The modelling technique was first introduced, step-by-step
and then applied to manufacturer components series. The second part of the paper was
dedicated to implementing this modelling technique, together with state-of-the-art models
for the other components, in order to carry on the selection of the best inductor value in a
representative case study. Thanks to the generic modelling approach and the parameters
derivation technique, the numerous inductor option, coming from three components series
were benchmarked. The best inductor value could be identified, leading to minimum
losses and minimum volume. An interesting conclusion came out of the design, related
to the ripple current magnitude, significantly above best practices. The model accuracy
was helpful in investigating design options with large ripple currents. The last part of
the paper was dedicated to the full validation of the modelling and design approach.
Based on opposition technique, the case study was implemented and total losses were
characterized. The measurement results were found in good accordance with the modelling
results, confirming that the modelling technique was accurate. Also, the whole modelling
and design approach has shown that a large ripple current magnitude can lead to optimal
designs in terms of efficiency and power density at the inductor level.

## [стр. 30]

Appl. Sci. 2022, 12, 9330
29 of 30
All in all, this paper, which is quite long, is presenting a full modelling and design
approach to select the best inductor value for buck-derived converter applications. It is
shown how the acquisition of complementary data from off-the-shelf components may
help in looking for the best component over a large panel of components and operating
conditions. The two parts in this paper are helping the reader to understand how powerful
the proposed modelling technique could be when applied in a design process, as well
as how a few extra parameters, made available by manufacturers, could help greatly in
representing the performances of their devices accurately.
Author Contributions: Conceptualization, H.P., J.-C.C. and Y.L.; methodology, H.P.; software, H.P.;
validation, H.P., J.-C.C. and Y.L.; formal analysis, H.P. and Y.L.; investigation, H.P.; resources, Y.L. and
J.-C.C.; data curation, H.P.; writing-original draft preparation, H.P. and J.-C.C.; writing-review
and editing, H.P., J.-C.C. and Y.L.; visualization, H.P., J.-C.C.; supervision, Y.L. and J.-C.C.; project
administration, Y.L. and J.-C.C.; funding acquisition, Y.L. and J.-C.C. All authors have read and
agreed to the published version of the manuscript.
Funding: This research received no external funding.
Conflicts of Interest: The authors declare no conflict of interest.
References
1.
Geetha, K. Full-Bridge Inverter with AC side Decoupling for Single-Phase Grid-Tied Inverter. In Proceedings of the 2021 IEEE
International Conference on Mobile Networks and Wireless Communications (ICMNWC), Tumkur, India, 3-4 December 2021;
pp. 1-6. [CrossRef]
2.
Chen, L.; Amirahmadi, A.; Zhang, Q.; Kutkut, N.; Batarseh, I. Design and Implementation of Three-Phase Two-Stage GridConnected Module Integrated Converter. IEEE Trans. Power Electron. 2014, 29, 3881-3892. [CrossRef]
3.
Shinjo, F.; Wada, K.; Shimizu, T. A Single-Phase Grid-Connected Inverter with a Power Decoupling Function. In Proceedings of
the 2007 IEEE Power Electronics Specialists Conference, Orlando, FL, USA, 17-21 June 2007; pp. 1245-1249. [CrossRef]
4.
Ye, Z.; Lei, Y.; Pilawa-Podgurski, R.C.N. The Cascaded Resonant Converter: A Hybrid Switched-Capacitor Topology with High
Power Density and Efficiency. IEEE Trans. Power Electron. 2020, 35, 4946-4958. [CrossRef]
5.
Huang, X.; Liu, T.; Li, B.; Lee, F.C.; Li, Q. Evaluation and applications of 600V/650V enhancement-mode GaN devices. In
Proceedings of the 2015 IEEE 3rd Workshop on Wide Bandgap Power Devices and Applications (WiPDA), Blacksburg, VA, USA,
2-4 November 2015; pp. 113-118. [CrossRef]
6.
Reusch, D.; Strydom, J. Evaluation of Gallium Nitride Transistors in High Frequency Resonant and Soft-Switching DC-DC
Converters. IEEE Trans. Power Electron. 2015, 30, 5151-5158. [CrossRef]
7.
Phung, T.H.; Nguyen, S.; Lamorelle, T.; Kerachev, L.; Andreta, A.; Lembeye, Y.; Crebier, J.C. Bidirectional AC to DC Isolated
Multi-Cell Converter. In Proceedings of the 2019 21st European Conference on Power Electronics and Applications (EPE '19
ECCE Europe), Genova, Italy, 3-5 September 2019; pp. 1-9. [CrossRef]
8.
Nie, J.; Yuan, L.; Gu, Q.; Sun, J.; Zhao, Z. A Coordinate and Distributed Control Scheme for Multilevel and Multi-Stage Medium
Voltage Solid State Transformer. In Proceedings of the 2018 International Power Electronics Conference (IPEC-Niigata 2018-ECCE
Asia), Niigata, Japan, 20-24 May 2018; pp. 2963-2968. [CrossRef]
9.
Mirjafari, M.; Balog, R.S. Survey of modelling techniques used in optimisation of power electronic components. IET Power
Electron. 2014, 7, 1192-1203. [CrossRef]
10.
Kazimierczuk, M. High-Frequency Magnetic Components; J. Wiley: Chichester, UK, 2009.
11.
Muhlethaler, J.; Biela, J.; Kolar, J.W.; Ecklebe, A. Improved Core-Loss Calculation for Magnetic Components Employed in Power
Electronic Systems. IEEE Trans. Power Electron. 2012, 27, 964-973. [CrossRef]
12.
Mühlethaler, J.; Kolar, J.W.; Ecklebe, A. Loss modelling of inductive components employed in power electronic systems. In
Proceedings of the 8th International Conference on Power Electronics-ECCE Asia, Jeju, Korea, 30 May-3 June 2011; pp. 945-952.
[CrossRef]
13.
Papamanolis, P.; Guillod, T.; Krismer, F.; Kolar, J.W. Minimum Loss Operation and Optimal Design of High-Frequency Inductors
for Defined Core and Litz Wire. IEEE Open J. Power Electron. 2020, 1, 469-487. [CrossRef]
14.
Chan, C.H.; Pong, M.H. Input current analysis of interleaved boost converters operating in discontinuous-inductor-curent mode.
In Proceedings of the PESC97. Record 28th Annual IEEE Power Electronics Specialists Conference. Formerly Power Conditioning
Specialists Conference 1970-71. Power Processing and Electronic Specialists Conference 1972, St. Louis, MO, USA, 27 June 1997;
Volume 1, pp. 392-398. [CrossRef]
15.
Datasheet from Coilcraft: Document 902-1, Shielded Power Inductors-MSS1210. Available online: https://www.coilcraft.com/
getmedia/f1a1bc5f-bdff-42f8-9ca8-1a0fb1d5094f/MSS1210.pdf (accessed on 1 June 2022).
16.
Datasheet from Coilcraft: Document 281-1, Shielded Power Inductors-MSS1260. Available online: https://www.coilcraft.com/
getmedia/febefb9b-60f9-4a2c-8525-9c396f34e363/mss1260.pdf (accessed on 1 June 2022).

## [стр. 31]

Appl. Sci. 2022, 12, 9330
30 of 30
17.
Datasheet from Coilcraft: Document 1621-1, Shielded Power Inductors-XGL6060. Available online: https://www.coilcraft.com/
getmedia/329fe97c-7311-4726-9bf3-37718f42b168/xgl6060.pdf (accessed on 1 June 2022).
18.
Sizikov, G.; Kolodny, A.; Fridman, E.G.; Zelikson, M. Frequency dependent efficiency model of on-chip DC-DC buck converters.
In Proceedings of the 2010 IEEE 26th Convention of Electrical and Electronics Engineers in Israel, Eilat, Israel,
17-20 November 2010; pp. 000651-000654. [CrossRef]
19.
Kaiser, J.; Dürbaum, T. An Overview of Saturable Inductors: Applications to Power Supplies. IEEE Trans. Power Electron. 2021, 36,
10766-10775. [CrossRef]
20.
Aubard, L.; Verneau, G.; Crebier, J.C.; Schaeffer, C.; Avenas, Y. Power MOSFET switching waveforms: An empirical model based
on a physical analysis of charge locations. In Proceedings of the 2002 IEEE 33rd Annual IEEE Power Electronics Specialists
Conference. Proceedings (Cat. No.02CH37289), Cairns, Australia, 23-27 June 2002; Volume 3, pp. 1305-1310. [CrossRef]
21.
Verneau, G.; Aubard, L.; Crebier, J.C.; Schaeffer, C.; Schanen, J.L. Empirical power MOSFET modeling: Practical characterization
and simulation implantation. In Proceedings of the Conference Record of the 2002 IEEE Industry Applications Conference. 37th
IAS Annual Meeting (Cat. No.02CH37344), Pittsburgh, PA, USA, 13-18 October 2002; Volume 4, pp. 2425-2432. [CrossRef]
22.
Tochigi, D.; Takashima, K.; Isobe, T.; Tadano, H.; Tomoyuki, M. Experimental Verification of a Model of Switching Transients
Considering Device Parasitic Capacitance for the Loss Estimation of Soft-switching Power Converters. In Proceedings of the 2019
IEEE 4th International Future Energy Electronics Conference (IFEEC), Singapore, 25-28 November 2019; pp. 1-7. [CrossRef]
23.
Yin, S.; Liu, Y.; Liu, Y.; Tseng, K.J.; Pou, J.; Simanjorang, R. Comparison of SiC Voltage Source Inverters Using Synchronous
Rectification and Freewheeling Diode. IEEE Trans. Ind. Electron. 2018, 65, 1051-1061. [CrossRef]
24.
Polenov, D.; Reiter, T.; Baburske, R.; Probstle, H.; Lutz, J. The influence of turn-off dead time on the reverse-recovery behaviour
of synchronous rectifiers in automotive DC/DC-converters. In Proceedings of the 2009 13th European Conference on Power
Electronics and Applications, Barcelona, Spain, 8-10 September 2009; pp. 1-8.
25.
Datasheet from Vishay: Document Number 68944: S17-1824-Rev. D, 11-Dec-17. Available online: https://www.vishay.com/
docs/68944/sis410dn.pdf (accessed on 1 June 2022).
26.
Crebier, J.C.; Ferrieux, J.P. PFC full bridge rectifiers EMI modeling and analysis-common mode disturbance reduction. IEEE Trans.
Power Electron. 2004, 19, 378-387. [CrossRef]
27.
Wang, S.; Lee, F.C.; Li, Q. Improved Balance Technique for Common-Mode Noise Suppression of PCB-Based PFC. IEEE Trans.
Power Electron. 2022, 37, 4174-4182. [CrossRef]
28.
Murata Simsurfing®. Available online: https://ds.murata.co.jp/simsurfing/mlcc.html?lcid=en-us&jis=false&md5=ec0a17df651
18905bbd37144f7eaf54c (accessed on 1 June 2022).
29.
Shen, Z.J.; Xiong, Y.; Cheng, X.; Fu, Y.; Kumar, P. Power MOSFET Switching Loss Analysis: A New Insight. In Proceedings of the
Conference Record of the 2006 IEEE Industry Applications Conference Forty-First IAS Annual Meeting, Tampa, FL, USA, 8-12
October 2006; pp. 1438-1442. [CrossRef]
30.
Texas Instrument: Application Report SLVA372C-November 2009-Revised January 2014. Available online: https://www.ti.
com/lit/an/slva372c/slva372c.pdf (accessed on 1 September 2022).
31.
Magnö Teknic: Application Note Number-MTAN17819: Inductor Selection Guide for Buck Converters-2019. Available
online: https://www.magnoteknik.com/download/Inductor%20Selection%20Guide%20for%20Buck%20Converters%20-%20
MTAN17819.pdf (accessed on 1 September 2022).
32.
Wurth Elektronik: ANP039: Power Inductors-8 Design Tips. Available online: https://www.we-online.com/catalog/media/o1
09038v410%20AppNotes_ANP039_PowerInductors8DesignTipps_EN.pdf (accessed on 1 August 2022).
33.
Andreta, A.; Lavado Villa, L.F.; Lembeye, Y.; Crebier, J.C. A Novel Automated Design Methodology for Power Electronics
Converters. Electronics 2021, 10, 271. [CrossRef]
34.
Ghosh, R.; Wang, M.X.; Mudiyula, S.; Mhaskar, U.; Mitova, R.; Reilly, D.; Klikic, D. Industrial Approach to Design a 2-kVa Inverter
for Google Little Box Challenge. IEEE Trans. Ind. Electron. 2018, 65, 5539-5549. [CrossRef]
35.
Bortis, D.; Neumayr, D.; Kolar, J.W. ηρ-Pareto optimization and comparative evaluation of inverter concepts considered for the
GOOGLE Little Box Challenge. In Proceedings of the 2016 IEEE 17th Workshop on Control and Modeling for Power Electronics
(COMPEL), Trondheim, Norway, 27-30 June 2016; pp. 1-5. [CrossRef]
36.
Neumayr, D.; Bortis, D.; Hatipoglu, E.; Kolar, J.W.; Deboy, G. Novel efficiency-Optimal Frequency Modulation for high power
density DC/AC converter systems. In Proceedings of the 2017 IEEE 3rd International Future Energy Electronics Conference and
ECCE Asia (IFEEC 2017-ECCE Asia), Kaohsiung, Taiwan, 3-7 June 2017; pp. 834-839. [CrossRef]
37.
Spichartz, M.; Staudt, V.; Steimel, A. Modular Multilevel Converter for propulsion system of electric ships. In Proceedings of the
2013 IEEE Electric Ship Technologies Symposium (ESTS), Arlington, VA, USA, 22-24 April 2013; pp. 237-242. [CrossRef]
38.
Xu, L.; Guerrero, J.M.; Lashab, A.; Wei, B.; Bazmohammadi, N.; Vasquez, J.; Abusorrah, A.M. A Review of DC Shipboard
Microgrids-Part I: Power Architectures, Energy Storage, and Power Converters. IEEE Trans. Power Electron. 2022, 37, 5155-5172.
[CrossRef]
39.
Stumpe, M.; Tünnerhoff, P.; Dave, J.; Schnettler, A.; Ergin, D.; Schön, A.; Würflinger, K.; Schettler, F. DC fault protection for
modular multi-level converter-based HVDC multi-terminal systems with solid state circuit breakers. IET Gener. Transm. Distrib.
2018, 12, 3013-3020. [CrossRef]
