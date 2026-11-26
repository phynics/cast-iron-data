+++
id = "ref/arc-investigator/lepidstadt-inspector"
kind = "archetype"
title = "Lepidstadt Inspector"
aon = "ArchetypeDisplay.aspx?FixedName=Investigator%20Lepidstadt%20Inspector"
source_ids = ["advanced-class-origins"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "lepidstadt_inspector", path = "json/archetypes_investigator.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/investigator" },
]
[[sources]]
publication = "advanced-class-origins"
page = "15"

[fields]
kind = "archetype"
features = [
  { anchor = "interrogation", level = 1 },
  { anchor = "keen-mind", level = 3 },
  { anchor = "perceptive-tracking", level = 3 },
  { anchor = "relentless-pursuit", level = 5 },
]
trades = [
  { replaces = "Trapfinding", feature = "trapfinding", by = ["interrogation"] },
  { replaces = "Trap sense", feature = "trap-sense", by = ["keen-mind"] },
  { replaces = "poison resistance", feature = "poison-resistance", levels = [2, 5, 8], by = ["keen-mind"] },
  { replaces = "poison immunity", feature = "poison-resistance", levels = [11], by = ["keen-mind"] },
  { replaces = "Swift alchemy", feature = "swift-alchemy", by = ["relentless-pursuit"] },
  { replaces = "investigator talent gained at 5th level", feature = "investigator-talent", levels = [5], by = ["relentless-pursuit"] },
]
+++

The ability of investigators trained at the University of Lepidstadt to get to the bottom of a
mystery is legendary, and troubled settlements throughout the region often send petitions to the
university requesting the aid of a formally trained inspector when some mystery threatens the
community as a whole. These inspectors are tasked with assuming nothing and asking difficult and
unpopular questions as necessary to get to the truth behind a problem. Inspectors are well-prepared
to deal with mystical threats, but they are also mindful that what some claim are supernatural
problems may well be just the result of more mundane threats such as bandits, wild beasts, or public
hysteria.

## Interrogation (Ex) {#interrogation}

A Lepidstadt inspector is a master of harrying others until they cooperate with his investigations,
and knows instinctively when the answers he receives are falsehoods. He adds 1/2 his class level
(minimum 1) to Intimidate checks made to influence a creature's attitude and to Sense Motive checks.
This ability replaces trapfinding.

## Keen Mind (Ex) {#keen-mind}

At 3rd level, a Lepidstadt inspector's strong, analytical mind resists attacks and hazards that
would muddy his clear thoughts. He gains a +1 bonus on Perception checks and Will saves. These
bonuses increase to +2 at 9th level and +3 at 15th level. This ability replaces trap sense, poison
resistance, and poison immunity.

## Perceptive Tracking (Ex) {#perceptive-tracking}

At 3rd level, a Lepidstadt inspector must take the
[perceptive tracking](ref/invtalent/perceptive-tracking) talent as his investigator talent. He
doesn't need to be trained in Perception to do so.

## Relentless Pursuit (Ex) {#relentless-pursuit}

At 5th level, a Lepidstadt inspector can learn enough about a suspect through observation that he
can deduce the most effective way to deal with the subject. Once per day, if a Lepidstadt inspector
finds a creature's tracks using perceptive tracking, he gains a +2 bonus on Bluff, Knowledge,
Perception, Sense Motive, and Survival checks against or about that creature, as well as on weapon
attack and damage rolls against that creature. These bonuses last until the Lepidstadt inspector
selects a new subject for relentless pursuit. This ability replaces swift alchemy and the
investigator talent gained at 5th level.
