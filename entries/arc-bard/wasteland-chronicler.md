+++
id = "ref/arc-bard/wasteland-chronicler"
kind = "archetype"
title = "Wasteland Chronicler"
aon = "ArchetypeDisplay.aspx?FixedName=Bard%20Wasteland%20Chronicler"
source_ids = ["people-of-the-wastes"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "wasteland_chronicler", path = "json/archetypes_bard2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/bard" },
]
[[sources]]
publication = "people-of-the-wastes"
page = "25"

[fields]
kind = "archetype"
features = [
  { anchor = "wasteland-knowledge", level = 1 },
  { anchor = "wasteland-specialist", level = 3 },
]
trades = [
  { replaces = "Bardic knowledge", feature = "bardic-knowledge", by = ["wasteland-knowledge"] },
  { replaces = "Inspire competence", feature = "bardic-performance", power = "inspire competence", by = ["wasteland-specialist"] },
]
+++

Some explore the farthest reaches of desolate wastelands, seeking to unlock the mysteries found
there and meet the inhabitants of such regions, and chronicle their findings. The wasteland
chronicler has discovered a connection to the wastelands and can use his performance to guide
himself and others through these regions safely.

## Wasteland Knowledge (Ex) {#wasteland-knowledge}

A wasteland chronicler adds [half](ref/misc/fractions-and-rounding) his level (minimum 1) as a bonus
on Knowledge (geography), Knowledge (local), Knowledge (nature), Knowledge (planes), and Survival
checks.

This replaces bardic knowledge.

## Wasteland Specialist (Ex) {#wasteland-specialist}

At 3rd level and every 5 levels thereafter, the wasteland chronicler gains the benefits of the
[favored terrain](ref/ability/favored-terrain) ranger class feature, but the wasteland chronicler
can choose only cold, desert, mountain, or swamp from the ranger's favored terrain list. In
addition, the wasteland chronicler adds half his level (minimum 1) as a bonus on Diplomacy checks to
influence the attitude of wasteland dwellers.

If the wasteland chronicler has the favored terrain ability from any other classes, the levels from
these different sources stack for the purposes of improving the bonuses of selected favored terrains
and choosing new favored terrains.

This replaces inspire competence.
