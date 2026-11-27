+++
id = "ref/arc-cavalier/circuit-judge"
kind = "archetype"
title = "Circuit Judge"
aon = "ArchetypeDisplay.aspx?FixedName=Cavalier%20Circuit%20Judge"
source_ids = ["path-of-the-hellknight"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "circuit_judge", path = "json/archetypes_cavalier.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/cavalier" },
]
[[sources]]
publication = "path-of-the-hellknight"
page = "32"

[fields]
kind = "archetype"
features = [
  { anchor = "circuit", level = 1 },
  { anchor = "sentence", level = 1 },
  { anchor = "double-jeopardy", level = 12 },
]
trades = [
  { replaces = "Tactician", feature = "tactician", by = ["circuit"] },
  { replaces = "greater tactician", feature = "greater-tactician", by = ["circuit"] },
  { replaces = "master tactician", feature = "master-tactician", by = ["circuit"] },
  { replaces = "Challenge", feature = "challenge", by = ["sentence"] },
  { replaces = "Demanding challenge", feature = "demanding-challenge", by = ["double-jeopardy"] },
]
+++

A circuit judge claims a specific region, becoming an expert in the local laws and, perhaps,
becoming a fearsome executioner.

## Circuit (Ex) {#circuit}

At 1st level, a circuit judge chooses a single community. While in that community or within 25 miles
of it, she adds [half](ref/misc/fractions-and-rounding) her cavalier level (minimum 1) on
Intimidate, Knowledge (local), and Sense Motive skill checks (as well as any other law-related skill
checks, at the GM's discretion). Whenever she advances in level, the range within which she gains
this bonus expands by another 25 miles—50 miles at 2nd level, 75 miles at 3rd level, and so forth.
This bonus on Intimidate checks increases by 2 when she enters a community within this area that she
hasn't visited for 1 week or more.

At 9th level and 17th level, the circuit judge can select another community within the range in
which she gains this ability's bonus. She can measure from that community (as well as previous
communities) to determine whether she gains this ability's bonus on the relevant skill checks.

This ability replaces tactician, greater tactician, and master tactician.

## Sentence (Ex) {#sentence}

Once per day as a swift action, the circuit judge can choose one target within sight to sentence.
The circuit judge gains the potential for a variety of bonuses related to that target. The circuit
judge chooses the form of these benefits from the following list of inquisitor
[judgments](ref/ability/judgments): destruction, justice, protection, purity, or smiting.

The benefits of these judgments apply only to the circuit judge and the target—the protection
judgment's bonus to Armor Class, for example, applies only to attacks made by the sentenced target
(not any creature who attacks the circuit judge while the judgment is active). Treat the circuit
judge's level as her inquisitor level for the purposes of determining how these judgments increase
in power. The circuit judge can use this ability twice per day at 1st level, plus two additional
times per day for every 3 cavalier levels beyond 1st, to a maximum of 14 times per day at 19th
level. She can switch her sentence as a swift action, but doing so expends an additional daily use
of this ability.

Sentencing a foe requires much of the circuit judge's concentration. The circuit judge takes a -2
penalty to her Armor Class, except against attacks made by the target of her sentence.

The sentence remains in effect either until the target is dead or unconscious or until the combat
ends. Sentences are considered challenges for the purposes of the effects listed in the challenge
section describing the cavalier's [order](ref/ability/orders).

This ability replaces challenge.

## Double Jeopardy (Ex) {#double-jeopardy}

At 12th level, whenever a circuit judge sentences a foe, she can gain the benefits of two inquisitor
judgments against the foe instead of one. Using this ability does not expend a daily use of
sentence.

This ability replaces demanding challenge.
