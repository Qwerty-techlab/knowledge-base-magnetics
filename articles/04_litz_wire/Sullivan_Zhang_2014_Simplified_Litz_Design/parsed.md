# source

> Автоматически извлечено из `source.pdf` скриптом `parse_pdf.py`
> Движок: pymupdf. Страниц: 8 из 8.
> Дата извлечения: 2026-08-07 06:43 UTC

Текст не редактировался. Формулы и таблицы могут быть искажены —
при сомнении сверяться с исходным PDF.

---

## [стр. 1]

Simplified Design Method for Litz Wire
Charles R. Sullivan
Thayer School of Engineering at Dartmouth
Hanover, NH, USA
Email: charles.r.sullivan@dartmouth.edu
Richard Y. Zhang
Dept. Elec. Eng. & Comp. Sci., M.I.T.
Cambridge, MA, USA
Email: ryz@mit.edu
Abstract-A simplified approach to choosing number and diameter of strands in litz wire is presented. Compared to previous
analyses, the method is easier to use. The parameters needed are
only the skin depth at the frequency of operation, the number
of turns, the breadth of the core window, and a constant from a
table provided in the paper. In addition, guidance is provided
on litz wire construction-how many strands or sub-bundles
to combine at each twisting operation. The maximum number
of strands to combine in the first twisting operation is given
by a simple formula requiring only the skin depth and strand
diameter. Different constructions are compared experimentally.
I. INTRODUCTION
Litz wire has become an essential tool for power electronics,
enabling low-resistance high-current conductors at frequencies
up to hundreds of kHz. But applying litz wire effectively is
not easy. Simple approaches, such as tables of recommended
strand diameter by frequency, can backfire, in some cases
leading to higher resistance than a simple solid-wire or foil
winding, and almost always leading to higher cost and loss
than could be achieved with more careful design. However,
the literature on more sophisticated analysis and design approaches can be intimidating, with recommended approaches
including Bessel functions [1]-[5], combinations of Bessel
functions [6] or iterative application of them [7]; as well as
complex permeability models [8], [9], among others [10]. Even
the relatively simple approach in [11] requires a formula with
ten terms raised to various powers. Furthermore, these methods
generally only help with choosing the number of strands, and
offer little guidance on the details of construction-the number
of strands that should be combined at each step of twisting.
(For example, 120-strand litz wire could be constructed as
12×10, as 8×5×3, or as 3×5×8.)
This paper offers a simplified approach to choosing the
number and diameter of litz-wire strands, and shows that it
is equivalent to the more complex approaches in other work.
The approach can easily be implemented with a spreadsheet
but is also simple enough for hand calculations. Its simplicity
makes it useful for practicing engineers, and also makes it
easier for practitioners and researchers to gain insight into the
design problem and loss phenomena. The paper also offers a
simple rule-based approach to choosing the construction once
the number and diameter of strands has been chosen.
II. INSTRUCTIONS FOR USING THE METHOD
For fast reference, this section provides step-by-step instructions for the basic method, as applied to a layer-wound
transformer, and the following section extends the method to
gapped inductors. The theoretical basis and justification for
the method are discussed later, in Section IV. Fig. 1 outlines
the complete process.
A. Choosing number and diameter of strands
The four steps in the process to choose the number and
diameter of strands correspond to the first four boxes in Fig. 1.
1) Compute skin depth: The skin depth is given as
δ =
√
ρ
πfµ0
(1)
where ρ is the resistivity of the conductor (1.72 × 10-8Ω·m
for copper at room temperature, or 2×10-8Ω·m at 60◦C), f is
the frequency of a sinusoidal current in the winding, and µ0 is
the permeability of free space (4 × 10-7π H/m). Using MKS
units for all variables in this equation results in skin depth in
meters. For non-sinusoidal currents and combinations of dc
and ac current, the same formula for skin depth (1) can be
used if the frequency is replaced by the effective frequency
introduced in [11] and reviewed in Appendix A.
2) Winding parameters: The winding parameters needed
for the calculation, b and Ns, are illustrated in Fig. 2 for some
common winding geometries. b is the breath of the winding,
across the face where one winding faces another, and Ns is the
number of turns in the section of the winding in question. In
simple windings without interleaving, Ns is simply the number
of turns in the winding being designed (Ns = N). With
interleaving, it is the number of turns counting from a zero
field surface to the face between the primary and secondary.
The zero-field surface is either against a high-permeability
core, or at the center of a winding in a symmetrical interleaved
design.

  


		
 
  
	
!"#
"		
$
 





#" % &
'
"



	 
	
 
 



  %  &  (

% &(
'

) 



*
"
	
+
'

*
*




	
(+$  
	

Fig. 1.
Flowchart of the litz wire design method. Optional extensions for
non-sinusoidal waveforms and for gapped inductors are in [ ], in green.

## [стр. 2]

TABLE I
PARAMETERS FOR ECONOMICAL LITZ-WIRE DESIGNS. k IS USED IN (2).
Strand AWG size
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
Strand diameter (mm)
0.202
0.180
0.160
0.143
0.127
0.113
0.101
0.090
0.080
0.071
0.063
0.056
0.050
0.045
0.040
0.035
0.032
Economical FR
1.06
1.07
1.09
1.11
1.13
1.15
1.18
1.22
1.25
1.30
1.35
1.41
1.47
1.54
1.60
1.64
1.68
k (mm-3)
130
203
318
496
771
1.2k
1.8k
2.8k
4.4k
6.7k
10k
16k
24k
36k
54k
79k
115k
3) Recommended number of strands: The next step is to
calculate a recommended number of strands for each of the
strand diameters being considered, using
ne = k δ2b
Ns
(2)
where k is a constant for each strand diameter, given in Table I.
In the table, k is given in units of mm-3, so b and δ should
also be in units of mm, such that a unitless value of ne results.
The recommended values of ne given by (2) should be taken
as general indications not precise prescriptions. Values of n as
much as 25% above or below ne can still be good choices.
4) Final strand diameter and number selection: From (2)
a range of good design options for different strand diameters
is produced. To select one of these, first check whether the
designs given by (2) fit in the window space available. A
rough first approximation for this calculation is to assume
that the total area of actual copper, NnAs, where N is the
number of turns, n is the number of strands, and As is the
cross sectional area of a single strand, must be less than 25
to 30% of the window area available for that winding. If the
number of strands recommended does not fit in the window,
one may consider using the largest number that fits instead,
but if this requires reducing the number of strands by more
than about 25%, using one of the designs that does fit will
have almost as good performance at significantly lower cost.
When the number of strands is chosen as ne, the ac
resistance factor is as given in Table I. From this information













































Fig. 2.
Examples of how the winding breadth b and the number of turns
per section are defined for some common winding geometries. Each section
shown has a number of turns Ns; depending on whether the different sections
of a given winding (primary P or secondary S) are in parallel or series, the
total number of turns N for that winding may be equal to Ns or equal to
product of Ns and the number of sections. Note that Ns may be different for
the primary and secondary windings.
and a simple calculation of dc resistance, it is straightforward
to compile a table of the ac resistance of the economical and
effective designs for each of the strand diameters considered,
providing a range of possible tradeoffs between loss and cost.
Given a loss (and thus ac resistance) spec, one can choose the
lowest cost design meeting that spec from the table.
If the number of strands to be used deviates from the values
given by (2), either because space constraints or availability
of the wire, the ac resistance factor for any number of strands
can be calculated by
FR = Rac
Rdc
= 1 + (πnNs)2 d6
s
192 · δ4b2
(3)
where n is the number of strands actually used and ds is the
strand diameter. Note that ensuring the right units are used
in this formula is simply a matter of making sure all of the
lengths (ds, δ, and b) are all in the same units (e.g., all in
mm). The accuracy and scope of applicability of this formula
is discussed in Section IV.
Winding designers often follow a rule regarding "circular
mils per amp" or "amps per square mm." If this is a concern,
see Appendix B for further guidance.
B. Choosing construction
If a large number of strands is simply twisted together,
rather than constructed with multiple levels of twisting (sometimes called "true litz" construction), there can be a bundlelevel skin-effect problem: the high-frequency current will
preferentially flow in the surface strands, while the inner
strands are underutilized [11]. The construction needed to
avoid this problem can be determined as follows.
The approximate maximum recommended number of single
strands to be twisted together in the first step is
n1,max = 4δ2
d2s
(4)
where δ is the skin depth for a solid conductor given by (1)
and ds is the diameter of an individual strand.
If the total number of strands, n is less than n1,max, then
all the strands can be simply twisted in one operation without
problems from bundle-level skin effect. If n > n1,max, then
multiple twisting operations may improve performance. The
first twisting step should combine n1,max or fewer strands.
Subsequent operations should only combine 3, 4, or 5 bundles
from preceding operations.
For example, with ds = δ/4, n1,max = 64. For n ≤64, a
single simple twisting operation is all that is needed. For larger
numbers of strands, multiple operations are needed. The first
operation can combine up to 64 strands. The next operation
can combine up to 5 of the 64-strand bundles to make litz wire
with up to 320 total strands. Then up to 5 of those 320 strand

## [стр. 3]

(5×64) bundles can be combined to make litz wire with up
to 1600 strands (5×5×64). Other numbers of strands can be
created or approximated by using any number up to 64 in the
first step, and 3, 4, or 5 in the subsequent steps.
The value of n1,max given by (4) is conservative. Adhering
to this limits guarantees avoiding problems, as discussed further in conjunction with the experimental results in Section VI.
III. GAPPED INDUCTORS
Gapped inductors have a strong field near the gap, which
can induce large losses in any conductors placed in that region.
Spacing the winding away from the gap is a well established
technique to address this problem. The optimal positioning
of the wire away from the gap, and rigorous optimization of
litz wire in this case is developed in [12]-[15], for which
software is available for download or to run online at [16].
Rather than trying to improve on that work, which provides
true optimized designs, the objective here is to provide a much
simpler analysis that can be used to choose a reasonable litz
stranding with less effort.
With a winding configuration such as that shown in Fig. 3,
the same equation for a good number of strands to choose,
(2), can be used, but with b replaced by an effective value,
beff= π
(
0.693 · r1 + 0.307 · r0.91
2
· r0.09
1
)
(5)
where r1 and r2 are the inner and outer radii of the winding
region as shown in Fig. 3.
As can be seen from (5), the effective value of b is a weak
function of r2 in Fig. 3. As a result, the outer edge of the
winding region does not need to be a semicircle as shown
in Fig. 5. r2 can be replaced with an approximate average
distance from the gap to the outer edge of the winding and
used in (5). This average distance can be roughly estimated
or can be more systematically calculated based on making the
winding area of the annular region between r1 and r2 in Fig. 3
equal to that of the real winding shape.
Note that in inductors that carry ac and dc current, another
good option is to use a semicircular litz-wire winding in
parallel with another winding that only carries dc current (or
low-frequency current) [10], [17]. In such a case, the design
method presented here can be used to design the litz winding
stranding.
For an ungapped inductor on a low permeability core, a
rough approximation is the use the perimeter of the winding
for b.


Fig. 3. Winding spaced away from an inductor air gap by a radius r1.
IV. BASIS OF THE METHOD
A. Loss calculation
The basis of the loss calculation used here is a direct
calculation of the eddy currents and resulting loss induced
in a cylinder subjected to a uniform transverse magnetic
field. One approach to that calculation is to derive the exact
analytical solution for a single isolated cylinder immersed in a
uniform field extending infinitely far away from the cylinder.
This results in a Bessel function solution [1]-[5]. This is an
exact solution for a single wire with nothing near it, but is
only an approximation when wires are closer together [7],
[9], [10], [18], and is usually no better than the seemingly
less sophisticated Dowell method [19] when wires are tightly
packed together as in a winding [18], [20]. Fortunately, the
discrepancy between actual behavior and the Bessel-function
solution is only at high frequencies, where ds > δ, outside the
range of good design practice. Thus, for design, the Bessel
function approach is adequate.
However, in the useful design range where ds ≤δ, and
the Bessel function formulation is accurate, it is also overkill.
The formula can be greatly simplified by taking only the first
terms of a series expansion of the Bessel function solution.
Alternatively, an identical formula can be derived directly
from a simple physical analysis of the eddy currents induced
in a cylinder with a uniform transverse field, by assuming
that the field penetrates the cylinder uniformly without being
significantly reduced by the self-shielding effect of the eddy
currents. Because the skin effect is the manifestation of such
self-shielding behavior, the assumption of a field uniformly
penetrating the cylinder is valid for ds < δ. Thus, such a
simple analysis is valid over the same range of ds/δ in which
the Bessel function approach works well, which is also the
range of interest for design. Since the Bessel function approach
is more complex and offers no advantage in the range of
interest, we use the simplified formulation.1
The simplified formulation for the eddy-current loss in a
cylinder for ds ≤δ is given in [21] and is also derived in
more detail in [22] as
P(t) = πℓd4
c
64ρ
(dB
dt
)2
(6)
For a sinusoidal waveform, the time average value of the
squared derivative of B(t) is ω2 ˆB2/2, where ω is the radian
frequency and ˆB is the peak amplitude of the field, so the
time-average loss becomes
P = πℓd4
cω2 ˆB2
128ρ
(7)
as it is presented in [21]. These formulations are valid for any
field shape. For a winding configuration that results in a field
strength that linearly increases as the winding builds up and
is constant across the breadth (a 1-D field), this results in an
ac resistance factor [11]
FR = 1 + π2µ2
0N 2n2ω2d6
c
768ρ2b2
(8)
1An additional reason to avoid the Bessel function formulation is that many
researchers have been fooled into thinking that it is an exact wideband solution
for a winding, when it is in fact only exact for widely spaced wires, the
opposite extreme compared to tightly packed wires in winding.

## [стр. 4]

Here, we suggest a slight reformulation of (8) which makes
it incrementally, but perhaps significantly, simpler and easier
to use. From (1),
2
δ2 = ωµ0
ρ .
(9)
Substituting results in
FR = Rac
Rdc
= 1 + (πnN)2 d6
s
192 · δ4b2
(10)
In addition to being simpler, (10) has the advantage that
is it easy to see how the dimensions work: the numerator
and denominator both have dimensions of length to the sixth
power. Moreover, because (3) is based on direct physical
analysis of a cylindrical conductor, it avoid errors associated
with approximating round conductors as square or rectangular.
As discussed above, it is valid when ds < δ and for a 1D field geometry. The implications of these assumptions and
alternatives for other situations are discussed in Section V.
B. Choosing number and diameter of strands
Finding a way to calculate the ac resistance factor FR is
only the first step towards choosing a design. Even with a
target value for FR chosen, there are many combinations of
number and diameter of strands that could be used to achieve
the same value of FR. One design approach would be to hold
the number of strands fixed and find the optimum diameter;
another would be to hold the diameter fixed and find the
optimum number of strands. Both of these are analyzed in [11].
An approach that is better linked to real-world applications
is to hold the loss fixed and find the minimum cost design.
This problem was addressed in a complex way in [23], but
the results can be condensed to a simple table of the most
economically efficient value of FR for a given strand diameter
(Table I). By plugging values of FR from the table into (3),
and solving for the effective and economical recommended
number of strands ne, we obtain
ne = δ2b
√
192(FR -1)
πNd3s
(11)
To simplify the application of this formula, we can precompute
k =
√
192(FR -1)
πd3s
(12)
and tabulate the k values for use in the very simple formula
ne = k δ2b
N
(13)
Because the values of FR from [23] are based on cost data
that is now more than a decade old, new cost data was compared to the model, and the parameters for the cost curve-fit
function in [23] were adjusted slightly to k1 = 6×10-26 m-6
and k2 = 2.7 × 10-9 m-2. The values in Table I are based
on these new parameters. The cost data used was incomplete
and users may wish to adapt the parameters and recalculate
the table based on pricing offered by their suppliers, using (4)
and (5) in [23] and (12) above.
Values of n near those provided by (13) will provide
reasonable ac resistance factors (as shown in Table I), and will
give a good economical tradeoff between cost of litz wire and
ac resistance. Calculating the number of strands for different
diameters (and thus different values of k) gives a range of
options from low-cost designs with a small number of lowcost large-diameter strands to high-performance designs with
a much larger number of much finer strands.
C. Construction
Given a choice for the number and diameter of strands, the
sequence of twisting operations still must be selected. The
goal is to construct the wire such that the current flowing
in each strand will be approximately equal. The primary
effects that could lead to unequal current between strands
would be proximity effect and skin effect at the bundle level.
Bundle-level proximity effect is current circulating between
different strands, and bundle-level skin effect is current flowing
in the strands near the surface of a bundle (or sub-bundle)
while strands running down the center are underutilized [11].
Bundle-level proximity effect is combatted simply by twisting,
and the design criterion that results is just that the pitch of
twisting must be small compared to the overall length of wire,
or to the length of wire exposed to a given field strength.
Bundle-level skin effect, on the other hand, is not impacted
by simple twisting, and must be combatted by construction
techniques that transpose strands between different radial
positions in the bundle over the length. This is primarily
done by using multi-level construction: first twisting together
n1 strands of magnet wire, and then twisting together n2 of
those sub-bundles, followed optionally by additional stages of
twisting. One approach to avoiding skin effect to to make sure
that, at each stage, no more than five strands or sub-bundles
are twisted together. A group of five or fewer has no strand
in the center, whereas a group of seven has six around the
outside and one in the center. A group of six doesn't work as
neatly as a group of seven, but is likely to fall into a similar
configuration with one in the center.
For example, to make a 100-strand bundle, one could start
by twisting five magnet wires together, then twist five of those
lowest-level sub-bundles together, and finally twist four of
those larger sub-bundles together to get a bundle of 100 strands
with no skin effect beyond the strand-level skin effect that is
made negligible by using strands much smaller than a skin
depth. This would be designated as 4/5/5 if the twisting at
each level was in the same direction ("bunching operations"),
or as 4×5×5 if the twisting alternated directions at each level
("cabling operations").
By only combining strands or sub-bundles in groups of 3,
4, or 5, one can completely avoid bundle-level skin effect for
any of the bundling levels. However, this approach results in
a large number of operations which increases the cost, and
also increases the dc resistance, as each operation introduces
a few percent increase in length to the actual strand path.
Fortunately, such an extreme approach is rarely necessary. In a
typical scenario, bundle-level skin effect is not an issue for the
first steps of the construction. For example, a typical design
might use strand diameters of one quarter of a skin depth.
A construction that started with twisting together seven such
strands would not have any problems with skin effect, because
the overall diameter of that first sub-bundle would only be 3/4

## [стр. 5]

of a skin depth. Skin effect does not become significant until
the diameter is at least two skin depths.
The procedure in Section II-B for choosing a construction
is based on first, calculating the maximum number of strands
for which the bundle diameter is less than two skin depths,
and using that as n1,max, the maximum number of strands for
the first operation. This avoids bundle-level skin effect at the
first level. Each subsequent operation is constrained to use 3,
4, or 5 sub-bundles, and thus avoids any further bundle-level
skin effect.
The calculation of the number of strands for which the
bundle diameter is less than two skin depths is complicated by
the fact that we need to know the skin depth not in a solid conductor, but in a medium comprising copper strands separated
by thin insulation and airspace. As a rough approximation, we
adopt the straightforward approach taken in [6] of using the
average conductivity for this composite medium. Under this
assumption, the effective skin depth for the bundle is
δeff=
δ
√
Fp,litz
(14)
where Fp,litz is the litz packing factor, defined as the ratio of
the total copper cross-sectional area in the bundle (nπd2
s/4) to
the area of the overall bundle (πd2
b/4). The ratio of the bundle
diameter to effective skin depth is
db
δeff
= db
δ
√
Fp,litz = db
δ
√
nπd2s/4
πd2
b/4 =
ds
δ√n
(15)
Setting this ratio equal to 2 for the maximum allowable
number of strands in the first twisting operation (n1,max)
results in
n1,max = 4δ2
d2s
(16)
where δ is the skin depth for a solid conductor given by (1)
and ds is the diameter of an individual strand.
D. Gapped Inductors
The effect of the gap fringing field on litz wire near it can
be described by the average value of B2 in the region of the
winding [22]. To make an approximate calculation of that field,
we assume the winding is spaced away from the gap a distance
r1, and that its shape is as shown in Fig. 3, or that that shape is
a reasonable approximation. The assumption that the winding
is spaced away from the gap limits the applicability of this
analysis, but spacing the winding way from the gap is usually
a good idea.
For this analysis, we analyzed the geometry in Fig. 3 in
rectangular coordinates rather than considering the curvature
of the wire around the center post, both to simplify the
mathematical analysis and to simplify the application of the
method by reducing the number of input variables. In this
case, the field lines are semicircles around the gap, with field
strength
B(r) = µ0I
πr
(17)
in the region between the gap and the winding. Inside the
winding, this is reduced by a factor equal to the fraction of
the winding area outside of the radius at which the field is
being evaluated, such that
B(r) = µ0I
πr
(r2
2 -r2)
(r2
2 -r2
1)
(18)
Averaging B2 over the winding area, and comparing to the
spatial average of the squared field in the one dimensional
case
⟨B2⟩= µ2
0I2
3b2
(19)
we can find a value of beffthat gives the same value of ⟨B2⟩
as the field in (18) when used in (19):
beff=
π(r2
2 -r2
1)1.5
r2
2
√
ln r2
r1 + r2
1
r2
2 -r4
1
4r4
2 -0.75
(20)
Because (20) is overly complicated for the theme of this paper,
we found a curve fit for it (5) with parameters optimized to
minimize the maximum percentage error at any point in the
region of r2/r1 up to 100. The fit has less than 1% error over
this range.
In Section III it is stated that (5) can provide adequate
accuracy even when the outer boundary of the winding is
not a semicircle. To test this, we ran a 2-D finite-element
simulation of a PQ35/35 core with a 1 mm centerleg gap and
a winding that fills the winding window except for a 5 mm
radius semicircular region near the gap. An equivalent of r2
was calculated as 11 mm based on matching the actual winding
area to the area of a semicircular region between r1 = 5 mm
and r2. The calculated value of beff= 20.77 mm results in an
estimate of ⟨B2⟩14% higher than the simulated value. This is
adequate accuracy for an approximate analysis, considering the
fact that the winding actual winding region is a significantly
different shape (the window is 25 mm × 8.8 mm).
V. DISCUSSION AND ALTERNATIVES
The basic analysis provided here is accurate for 1-D overall
field geometries and for frequencies where ds ≤δ. It is more
accurate than Dowel's approximation, because it is not based
on approximating round wires with "equivalent" foil, but is
instead based on a direct calculation of loss in the actual round
wire shape. However, it starts to overestimate loss for higher
frequencies, beyond where ds ≈2δ. This is not a problem for
design work, because good designs won't use combinations of
strand diameters and frequencies that get into that region.
The primary limitation is the restriction to a 1-D field
as with transformer geometries like those shown in Fig. 2,
or to gapped inductors using the formulation developed in
Section IV-D and presented in Section III. For arbitrary field
shapes, and for situations in which different windings have
different waveform shapes, the approach in [24] provides a
rigorous optimization of litz wire cost and loss for arbitrary
geometries and waveforms, albeit one requiring more complex
software.
As discussed above, the restriction of strand diameter
smaller than a skin depth is not a problem for design work,
as good designs of litz wire will use strands smaller than a
skin depth, often by a factor of 4 or more. Occasionally it is
useful to estimate ac resistance for a much higher frequency.

## [стр. 6]

For example, if a waveform has high-frequency harmonics,
the optimization might provide a design for which ds < δ
for the fundamental, but not for the harmonics. Correcting
the loss estimate for the harmonics is rarely essential, but
is sometimes of interest. In these cases, it is shown in [7],
[9], [10], [18], [20] that neither the Dowell approach nor
the Bessel function approach yields an accurate solution,
with the exception of the iterative Bessel function approach
described in [7]. It is shown in [20] that a curve-fit approach
can offer higher accuracy; a similar, simpler, lower-accuracy
formulation is provided in [10]. These formulations can be
applied directly to estimate loss from a calculated 1-D field
or a 2- or 3-D field from simulation or calculation, or can
be reformulated as a complex permeability for use in finite
element simulations [8], [9]. A computationally streamlined
approach for finding a wideband model that gives accurate
loss estimation based on these approaches is provided in [25],
where a 2-D magnetostatic field analysis is combined with loss
models to yield a frequency-dependent resistance matrix that
can be used to calculate loss for any set of current waveforms
in a multi-winding component.
Note that the restriction to a 1-D field geometry only refers
to the overall field shape, not to the local phenomena as the
wires interact with the field and incur loss. The actual 2-D
circular shape of the wires is used in the loss calculation.
The assumption of a linearly increasing field through the
winding is an approximation, but for litz wire, it is actually
a better approximation than assuming a stepwise layer-bylayer increase in field, as the field gradually increases as one
moves up through the strands of a litz-wire layer. Simulations
and measurements consistently confirm the validity of this
approach.
One aspect of wire construction that is not addressed here
is the choice of the twisting pitch. In general, a wide range
of pitches can work well, and the choice of pitch may be
left to the litz wire manufacturer based primarily on practical
considerations. Numerical simulations of the effects of pitch
reported in [26] provide more insight into the effects of pitch
and may lead to more specific guidance. A possible concern
in this regard is turns that are close to an air-gap. Such a turn
might be subject to a strong field just through a fraction of one
twist of the wire. The twisting of litz wire works to reduce
proximity effect when voltage induced by the flux through one
half twist is canceled by the same flux going through the next
half twist, linked in the opposite sense [26]. If the flux at the
next half twist is much lower because it is not as close to the
gap, this principle is undermined.
VI. EXPERIMENTAL MEASUREMENTS
The ac winding resistance formulation upon which the
strand number and diameter design method is based (8) is
already well validated, but very little work has been published
examining the effect of litz construction on bundle-level skin
effect, so we concentrate on experiments to validate the construction recommendations in Section II-B, and in particular
(4).
One valuable data source is [6] which includes measurements of ac resistance without external proximity effect, and
furthermore compares two constructions with the same total
number of strands (245) and with the same strand diameter (0.1 mm). This makes it possible to see the effect of
bundle construction. The two constructions measured were
7×35/(0.1 mm) and 4×(61 or 62)/(0.1 mm). Of these, only
the second follows the construction guidelines in Section II-B;
the first violates these by combining more than 5 bundles
in the second operation. And, confirming this guideline, the
7×35/(0.1 mm) construction exhibits worse performance when
the two are compared in [6].
The number of strands in the lowest-level bundle, n1, is 61
or 62 for the 4×(61 or 62)/(0.1 mm) construction measured
in [6]. From (4), this would be permissible for a frequency
of 29 kHz or lower. The data in [6] confirms that this wire
has no deviation from ideal behavior below 29 kHz; but it
also shows very little deviation from ideal behavior at higher
frequencies, which may indicate that the configuration of the
61 or 62 strand bundle includes some transposition. Thus, [6]
provides one data point for which following the guidelines in
Section II-B would avoid any problems, but it falls short of
clearly demonstrating the importance of specifically limiting
the number of strands in the first level of construction to the
value in (4).
To more fully examine the effect of construction on bundlelevel skin effect, we constructed three litz wires, each with
125 strands of AWG 34 (0.16 mm) magnet wire. One was
simply twisted (125/(0.16 mm)), one used a cabling operation
to combine 5 bundles, each with 25 strands (5×25/(0.16 mm)),
and the final construction attempted to avoid all bundle-level
skin effect by combine five strands or bundles at each step
(5 × 5 × 5/(0.16 mm)). We constructed these by hand using
basic ropemaking equipment [27] in order to ensure we knew
the exact sequence of operations. The three constructions are
shown in Fig. 4.
Measurements of dc resistance for a 2 m length yield
14.307 mΩ(5 × 5 × 5/(0.16 mm)), 14.35 mΩ(5 ×
25/(0.16 mm)), and 14.46 mΩ(125/(0.16 mm). These are 5
to 6% higher than the theoretical resistance for 125 straight
strands of AWG 34 wire in parallel, a result of the increased
length from twisting and possibly also imperfect termination
Fig. 4. Three constructions for 125 strands of 0.16 mm diameter magnet wire:
Top: simply twisted (125/(0.16 mm)); middle: 5 × 25/(0.16 mm); bottom:
5 × 5 × 5/(0.16 mm).

## [стр. 7]

or strand breakage, resulting in fewer than 125 strands actually
conducting.
Measurements of ac resistance are shown in Fig. 5. The
measurements are for the same 2 m lengths, laid out in a
serpentine (zig-zag) pattern with approximately 8 cm spacing
to minimize proximity effect and inductance. The measurements use an Agilent 4294A impedance analyzer with a Kelvin
clip test fixture with short leads (about 10 cm). The results
clearly show that the 5 × 5 × 5 construction provides the best
performance, that 5×25 provides the second-best performance,
and simply twisted 125-strand wire ranks last, consistent with
our predictions.
Quantitatively, (4) indicates that n1 = 25 is fine up to
25 kHz. The measured resitance for the 5×25 construction first
becomes clearly worse than the 5×5×5 construction between
30 and 40 kHz, consistent with (4). The 125-strand simply
twisted wire is only guaranteed to avoid bundle-level skin
effect up to about 5.5 kHz based on (4), but no degradation in
performance is distinguishable from noise until above about
25 kHz. In this case, the wire works better than would be
expected in the 6 kHz to 25 kHz range.
In summary, the data show that:
• Following the construction guidelines in Section II-B
always yielded good results.
• The performance improves as the construction approaches
ideal litz, combining no more than 5 strands or bundles
in any given operation, but more strands can be safely
combined in the first operation if the maximum number
given by (4) is not exceeded.
• Of the three constructions evaluated, two worked well to
higher frequencies than would be predicted by (4), but
one showed performance degradation just above the safe
frequency predicted based on (4). Thus, it appears that (4)
is a valid worst-case calculation but some bundles work
better than it predicts.
The fact that (4) is overly conservative for some samples and
not for others can be explained by the fact that simply twisted
a bunch comprising a large number of wires can easily result
   1
  10
 100
1000
 1
10
frequency (kHz)
ac resistance factor Rac/Rdc


5x5x5/(0.16 mm)
5x25/(0.16 mm)
125/(0.16 mm)
Fig. 5. Measured ac resistance factor of three constructions for 125 strands
of 0.16 mm diameter magnet wire. The three types are simply twisted
(125/(0.16 mm)); a construction with simple twisting of 25 strands followed
by a cabling operation 5×25/(0.16 mm); and "true litz" 5×5×5/(0.16 mm).
in a complex and somewhat random structure, rather than the
ideal of a single strand that goes the full length down the
center, followed by successive concentric helical shells. The
125 strands that were simply twisted were first looped on two
hooks 3 meters apart, and then one hook was twisted while
the other was held fixed. There was no attempt to position the
wires in a specific configuration at either end, and the positions
of the strands in the bundle could easily be very different at the
two ends. The randomization of the strand positions worked
reasonably well in this case, and the resulting wire performed
well at up to 25 kHz. However, this is not a good way to
guarantee good performance, and attempting to better control
the production might yield worse results.
To illustrate the behavior that can occur with a more
controlled construction, the simulation tool described in [26]
was used to simulate the same three constructions, but with
the 25 and 125 strand simply twisted bundles having an ideal
structure in which all the strands stay at the same radius
throughout the length. The results are shown in Fig. 6. These
results more clearly confirm (4), with the simply-twisted and
5×25 constructions deviating from the ideal 5×5×5 construction at the expected 5.5 and 25 kHz frequencies, respectively.
The deviations are much more dramatic than those in Fig. 5,
consistent with our explanation that the simply twisted bundles
include some random radial transposition.
Based on the experimental and simulation results it is recommended to use the procedure in Section II-B to determine
a construction that can guarantee consistently achieving good
results. Note that in many cases, this will yield a recommendation to use a construction that is considerably simpler than
might be required if the strictest guideline (to never combine
more than 5 strands) was followed.
VII. CONCLUSION
Previous literature on litz wire provides complex methods
for choosing the number and diameter of strands for litz wire,
but does not address the details of construction. This paper
presents a simplified approach to choosing the stranding, and
provides, for the first time, a straightforward guide to choosing
   1
  10
 100
1000
 1
10
frequency (kHz)
ac resistance factor Rac/Rdc


5x5x5/(0.16 mm)
5x25/(0.16 mm)
125/(0.16 mm)
Fig. 6.
Numerically simulated ac resistance factor for the same nominal
constructions of 125 strand litz wire as in Fig. 5. The simulation method used
is described in [26].

## [стр. 8]

the construction. Experiments and numerical simulations are
consistent with the construction guidelines provided.
APPENDIX A
EFFECTIVE FREQUENCY
Replacing the frequency in (1) with an effective frequency,
as explained in detail in the appendix of [11] can be used
to apply the optimization method presented here (and similar
optimization methods for other types of windings) to nonsinusoidal waveforms, including waveforms with ac and dc
components. The effective frequency is defined as
feff=
rms
{
di(t)
dt
}
2πIrms
(21)
Note that to account for dc, the rms value used should be
inclusive of the dc component, i.e., Irms =
√
I2ac,rms + I2
dc.
A very helpful reference for rms values and rms values of
derivatives is Table II of [28]. Note, however, that the optimum
thickness formulas given in that table are only valid for
foil windings, not for round wire, because of the different
constraints that apply, whereas (21) is more broadly applicable.
APPENDIX B
NOTE ON CURRENT DENSITY
Traditionally, rules for maximum current density have provided useful guidance for wire selection; these are usually
stated in A/mm2 or "circular mils" per ampere. At dc or low
frequency, the power dissipation per unit volume of copper can
be calculated from the current density. For example, at 650
circular mils per amp (3.04 A/mm2), using the resistivity of
copper at 60◦C, the power dissipation density is 184 mW/cm3
in the copper, or overall in a winding with a packing factor of
0.5, 92 mW/cm3. How much temperature rise this results in
depends on, among other things, the surface area to volume ratio of the component. Such rules were established for 50/60 Hz
components, and then applied without adjustment to highfrequency components for power electronics. The result often
worked because loss density was much higher (sometimes by
a factor of 3 or more because of proximity effect losses), but
the surface area to volume ratio was also much higher for the
smaller high-frequency components. However, a well-designed
high-frequency winding will not have such severe proximityeffect losses. Thus, one can take advantage of the high surface
area to volume ratio and run much higher current densities.
When a bobbin is underfilled, this increases the surface area
to volume ratio, and allows still higher current densities.
A good design procedure is to establish an allowable total
dissipation in an given winding based on a thermal model
(e.g., [29]) or test, and then model losses that ensure they stay
below that limit. In any case, in comparing two designs with
similar surface area, a design with lower winding dissipation
is preferred, even if it has higher nominal current density.
REFERENCES
[1] J. A. Ferreira, "Analytical computation of ac resistance of round and
rectangular litz wire windings," IEE Proceedings-B Electric Power
Applications, vol. 139, no. 1, pp. 21-25, Jan. 1992.
[2] --, "Improved analytical modeling of conductive losses in magnetic
components," IEEE Trans. on Pow. Electr., vol. 9, no. 1, pp. 127-31,
Jan. 1994.
[3] J. Acero, P. J. Hernandez, J. M. Burd´ıo, R. Alonso, and L. Barragdan,
"Simple resistance calculation in litz-wire planar windings for induction
cooking appliances," IEEE Trans. on Magnetics, vol. 41, no. 4, pp. 12801288, 2005.
[4] J. Acero, R. Alonso, J. M. Burdio, L. A. Barragan, and D. Puyal,
"Frequency-dependent resistance in litz-wire planar windings for domestic induction heating appliances," IEEE Trans. on Pow. Electr., vol. 21,
no. 4, pp. 856-866, 2006.
[5] C. Carretero, J. Acero, and R. Alonso, "Tm-te decomposition of power
losses in multi-stranded litz-wires used in electronic devices," Progress
In Electromagnetics Research, vol. 123, pp. 83-103, 2012.
[6] H. Rossmanith, M. Doebroenti, M. Albach, and D. Exner, "Measurement
and characterization of high frequency losses in nonideal litz wires,"
IEEE Trans. on Pow. Electr., vol. 26, no. 11, pp. 3386-3394, 2011.
[7] M. Albach, "Two-dimensional calculation of winding losses in transformers," in IEEE Pow. Electr. Spec. Conf, vol. 3.
IEEE, 2000, pp.
1639-1644.
[8] Xi Nan and C. R. Sullivan, "An equivalent complex permeability model
for litz-wire windings," in Fortieth IEEE Industry Applications Society
Annual Meeting, 2005, pp. 2229-2235.
[9] D. C. Meeker, "An improved continuum skin and proximity effect model
for hexagonally packed wires," Journal of Computational and Applied
Mathematics, vol. 236, no. 18, pp. 4635-4644, 2012.
[10] A. van den Bossche and V. Valchev, Inductors and Transformers for
Power Electronics.
Taylor and Francis Group, 2005.
[11] C. R. Sullivan, "Optimal choice for number of strands in a litz-wire
transformer winding," IEEE Trans. on Pow. Electr., vol. 14, no. 2, pp.
283-291, 1999.
[12] J. Hu and C. R. Sullivan, "Optimization of shapes for round-wire highfrequency gapped-inductor windings," in Proceedings of the 1998 IEEE
Industry Applications Society Annual Meeting, 1998, pp. 900-906.
[13] --, "Analytical method for generalization of numerically optimized
inductor winding shapes," in IEEE Pow. Electr. Spec. Conf., 1999.
[14] C. R. Sullivan, J. McCurdy, and R. Jensen, "Analysis of minimum cost
in shape-optimized litz-wire inductor windings," in IEEE Pow. Electr.
Spec. Conf, 2001.
[15] R. Jensen and C. R. Sullivan, "Optimal core dimensional ratios for
minimizing winding loss in high-frequency gapped-inductor windings,"
in IEEE Applied Power Electronics Conference, 2003, pp. 1164 -1169.
[16] "Dartmouth power electronics and magnetic components group web
site," http://power.engineering.dartmouth.edu.
[17] C. Schaef and C. Sullivan, "Inductor design for low loss with complex
waveforms," in IEEE Applied Power Electronics Conference, 2012.
[18] Xi Nan and C. R. Sullivan, "An improved calculation of proximityeffect loss in high-frequency windings of round conductors," in IEEE
Pow. Electr. Spec. Conf, 2003.
[19] P. Dowell, "Effects of eddy currents in transformer windings," Proceedings of the IEE, vol. 113, no. 8, pp. 1387-1394, Aug. 1966.
[20] Xi Nan and C. R. Sullivan, "Simplified high-accuracy calculation of
eddy-current loss in round-wire windings," in IEEE Pow. Electr. Spec.
Conf, 2004.
[21] E. C. Snelling, Soft Ferrites, Properties and Applications, 2nd ed.
Butterworths, 1988.
[22] C. R. Sullivan, "Computationally efficient winding loss calculation with
multiple windings, arbitrary waveforms, and two- or three-dimensional
field geometry," IEEE Trans. on Pow. Electr., vol. 16, no. 1, pp. 142-50,
2001.
[23] --, "Cost-constrained selection of strand wire and number in a litzwire transformer winding," IEEE Trans. on Pow. Electr., vol. 16, no. 2,
pp. 281-288, Mar. 2001.
[24] J. D. Pollock, T. Abdallah, and C. R. Sullivan, "Easy-to-use CAD tools
for litz-wire winding optimization," in IEEE Applied Power Electronics
Conference, 2003.
[25] D. R. Zimmanck and C. Sullivan, "Efficient calculation of winding loss
resistance matrices for magnetic components," in IEEE Workshop on
Control and Modeling for Power Electronics (COMPEL), 2010.
[26] R. Y. Zhang, C. R. Sullivan, J. K. White, and J. G. Kassakian, "Realistic
litz wire characterization using fast numerical simulations," in IEEE
Applied Power Electronics Conference (APEC), 2014.
[27] Lacis,
"Leonardo
rope
machine."
[Online].
Available:
http://www.lacis.com/catalog
[28] W. Hurley, E. Gath, and J. Breslin, "Optimizing the ac resistance
of multilayer transformer windings with arbitrary current waveforms,"
IEEE Trans. on Pow. Electr., vol. 15, no. 2, pp. 369-76, Mar. 2000.
[29] W. G. Odendaal and J. A. Ferreira, "A thermal model for high-frequency
magnetic components," IEEE Trans. on Ind. Appl., vol. 35, no. 4, pp.
924-931, 1999.
