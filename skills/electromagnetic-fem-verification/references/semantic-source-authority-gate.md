# Semantic Source-Authority Gate

Use this gate before generating CAD, excitations, mesh, or a report from any EM design contract. It prevents a hash-consistent but semantically unauthorized branch from becoming the active model.

## Authority order

1. Persisted user requirement or approved amendment.
2. Current canonical prompt/specification.
3. Canonical analytical result selected for the exact frequency/configuration.
4. Design contract.
5. FEM manifest.
6. Plan/CAD artifacts.
7. Reports and chat handoffs.
8. Memory, task labels, historical designs, and context notes.

A lower item cannot silently override a higher one. If the user amends topology in chat, persist the amendment in the project before promoting a new contract.

## Required semantic comparison

Build a table for every candidate configuration:

| Property | Prompt | Result | Contract | Manifest | Candidate CAD |
|---|---|---|---|---|---|
| Frequency/configuration key | | | | | |
| Converter topology | | | | | |
| Number of electrical windings | | | | | |
| Complete turns per continuous path | | | | | |
| Parallel physical paths | | | | | |
| Path continuity and allowed nodes | | | | | |
| Series/parallel connection and polarity | | | | | |
| Target L and tolerance | | | | | |
| Nominal gap hypothesis | | | | | |
| Current convention | | | | | |

Hash verification follows this table; it does not replace it.

## Turns, banks, and parallel cables

- `p` parallel cables that each traverse `N` complete turns form an `N`-turn winding with current split across `p` paths. They do not form `p*N` turns.
- Physical axial/radial banks may be parts of one continuous winding. Bank count is not winding count.
- Two electrically separate sections with `N1` and `N2` turns connected series-aiding require a coupled-winding model. Ideally `N_eq=N1+N2`, but acceptance uses `L_series=L1+L2+2M` and verified polarity.
- Two series-aiding 10-turn sections are therefore a 20-turn-equivalent hypothesis, not a geometric spelling of a 16-turn winding.
- Frequency configurations are alternatives unless the contract explicitly defines simultaneous operation.

## Conflict disposition

When the semantic table conflicts:

1. stop before CAD/mesh/solve;
2. identify the first unauthorized transition in the chain;
3. keep production results/contracts unchanged if they match the higher source;
4. mark the derived branch `rejected_not_source_authorized`;
5. disable its plan/CAD execution paths, not only its report wording;
6. preserve existing artifacts as rejected audit evidence rather than deleting them;
7. reclassify reusable lower-level evidence narrowly (for example, supplier STEP import and face probes may remain valid while turn-derived gap hypotheses are rejected);
8. add regression tests that prove the rejected CLI cannot create new artifacts.

## Session case: drossel1 turn-count correction

Canonical project files defined alternative single-winding configurations:

- 150 kHz: 16 turns, 12 continuous parallel cables, each cable traversing all 16 turns;
- 100 kHz: 24 turns, 9 continuous parallel cables, each cable traversing all 24 turns.

A context-only `2x10` note was incorrectly promoted into a draft. With series-aiding connection this represented 20 equivalent turns (`20^2/16^2=1.5625` at fixed `A_L`) and could not reuse the 16-turn gap or excitation. The correction kept canonical production analytics unchanged, rejected the 2x10 draft and gap hypotheses, disabled its plan/CAD CLI paths, and retained the core-only CAD solely as supplier-half assembly/face-probe evidence.

## Verification checklist

- [ ] Semantic comparison table complete before hash chain acceptance.
- [ ] Every topology-changing amendment is persisted and attributable.
- [ ] Turns are counted per complete continuous path.
- [ ] Parallel paths are not mistaken for extra turns.
- [ ] Physical banks are not mistaken for electrical sections.
- [ ] Frequency alternatives are not combined.
- [ ] Rejected branches cannot produce new plan/CAD/mesh/solve artifacts.
- [ ] Reusable evidence from a rejected branch is narrowly reclassified.
