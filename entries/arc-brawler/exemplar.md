+++
id = "ref/arc-brawler/exemplar"
kind = "archetype"
title = "Exemplar"
aon = "ArchetypeDisplay.aspx?FixedName=Brawler%20Exemplar"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "exemplar", path = "json/archetypes_brawler.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/brawler" },
]
[[sources]]
publication = "advanced-class-guide"
page = "86"

[fields]
kind = "archetype"
features = [
  { anchor = "call-to-arms", level = 1 },
  { anchor = "inspiring-prowess", level = 3 },
  { anchor = "field-instruction", level = 5 },
]
trades = [
  { replaces = "Unarmed strike", feature = "unarmed-strike", by = ["call-to-arms"] },
  { replaces = "close weapon mastery", feature = "close-weapon-mastery", by = ["call-to-arms"] },
  { replaces = "Maneuver training", feature = "maneuver-training", by = ["inspiring-prowess"] },
  { replaces = "AC bonus", feature = "ac-bonus", by = ["inspiring-prowess"] },
  { replaces = "Brawler's strike", feature = "brawler-s-strike", by = ["field-instruction"] },
]
+++

A versatile soldier who inspires her companions with her fighting prowess, an exemplar is at home on
the front lines of battles anywhere.

## Call to Arms (Ex) {#call-to-arms}

At 1st level, an exemplar can expend a use of martial flexibility to rouse her allies into action.
All allies within 30 feet are no longer [flat-footed](ref/rule/flat-footed), even if they are
surprised. Using this ability is a move action. At 6th level, the exemplar can use it as a swift
action instead. At 10th level, she can use it as a free action. At 12th level, she can use it as an
immediate action. This ability replaces unarmed strike and close weapon mastery.

## Inspiring Prowess (Ex) {#inspiring-prowess}

At 3rd level, an exemplar gains the ability to use certain bardic performances. She can use this
ability for a number of rounds per day equal to 3 + her Charisma modifier; this increases by 1 round
per brawler level thereafter. The exemplar's effective bard level for this ability is equal to her
brawler level - 2. At 3rd level, the exemplar can use
[inspire courage](ref/performance/inspire-courage). At 11th level, the exemplar can use
[inspire greatness](ref/performance/inspire-greatness). At 15th level, the exemplar can use
[inspire heroics](ref/performance/inspire-heroics). Instead of the Perform skill, she activates this
ability with impressive flourishes and displays of martial talent (this uses visual components).
This ability otherwise functions as bardic performance; feats and other effects that affect bardic
performance (such as the [Extra Performance](ref/feat/extra-performance) feat) apply to it. This
ability replaces maneuver training and AC bonus.

## Field Instruction (Ex) {#field-instruction}

At 5th level, as a standard action an exemplar can grant a teamwork feat to all allies within 30
feet who can see and hear her. This teamwork feat must be one the exemplar knows or has gained with
the martial flexibility ability. Allies retain the use of this teamwork feat for 3 rounds + 1 round
for every 2 brawler levels. If the granted teamwork feat is one gained from martial flexibility,
this duration ends immediately if the exemplar loses access to that feat. Allies don't need to meet
the prerequisites of this teamwork feat. The exemplar can use this ability once per day at 5th
level, plus one additional time per day at 9th, 12th, and 17th level. This ability otherwise counts
as the cavalier's tactician class feature; feats and other effects which affect tactician (such as
[Practiced Tactician](ref/feat/practiced-tactician)) apply to it. This ability replaces brawler's
strike.
