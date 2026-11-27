+++
id = "ref/arc-bard/juggler"
kind = "archetype"
title = "Juggler"
aon = "ArchetypeDisplay.aspx?FixedName=Bard%20Juggler"
source_ids = ["ranged-tactics-toolbox"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "juggler", path = "json/archetypes_bard2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/bard" },
]
[[sources]]
publication = "ranged-tactics-toolbox"
page = "7"

[fields]
kind = "archetype"
features = [
  { anchor = "fast-reactions", level = 1 },
  { anchor = "combat-juggling", level = 2 },
  { anchor = "evasion", level = 2 },
]
trades = [
  { replaces = "Bardic knowledge", feature = "bardic-knowledge", by = ["fast-reactions"] },
  { replaces = "lore master", feature = "lore-master", by = ["fast-reactions"] },
  { replaces = "Versatile performance", feature = "versatile-performance", by = ["combat-juggling"] },
  { replaces = "Well-versed", feature = "well-versed", by = ["evasion"] },
  { replaces = "soothing performance", feature = "bardic-performance", power = "soothing performance", by = ["evasion"] },
  { replaces = "His normal weapon proficiencies", feature = "weapon-and-armor-proficiencies" },
]
+++

Jugglers are masters of manipulating objects, most famously by keeping multiple objects in the air
simultaneously. They often incorporate this talent into acting, comedy, or dance. Adventuring
jugglers find their abilities translate well into the use of thrown weapons.

## Weapon and Armor Proficiencies {#weapon-and-armor-proficiencies}

A juggler is proficient with all simple weapons, plus martial thrown weapons. This replaces his
normal weapon proficiencies. A juggler is not proficient with shields.

## Fast Reactions (Ex) {#fast-reactions}

At 1st level, a juggler gains [Deflect Arrows](ref/feat/deflect-arrows) as a bonus feat. At 5th
level, he gains [Snatch Arrows](ref/feat/snatch-arrows) as a bonus feat. The juggler doesn't need to
meet the prerequisites for these feats. The juggler can use the ability granted by these feats an
additional time each round at 11th level (with a -5 penalty on his second attack roll) and at 17th
level (with a -10 penalty on his third attack roll). This ability replaces bardic knowledge and lore
master.

## Combat Juggling (Ex) {#combat-juggling}

At 2nd level, a juggler can hold and wield (in other words, "juggle") up to three items or weapons
in his hands. The juggler must be able to hold and wield an object in one hand in order to juggle
it. This ability doesn't grant the juggler additional attacks, though it does allow him to use
different weapons as part of a [full attack](ref/rule/full-attack). As long as he is juggling fewer
than three objects, the juggler is considered to have a free hand (for the purposes of drawing a
weapon, using somatic components, using Deflect Arrows, and so on). At 6th level and every 4 levels
thereafter, the maximum number of objects the juggler can juggle increases by one, to a maximum of
seven objects at 18th level.

If the juggler is affected by any action or condition that would require a
[concentration](ref/rule/concentration) check while he is juggling, he must attempt a Sleight of
Hand check to continue juggling and avoid losing concentration. The check's DC is the same as a
concentration check, treating the spell level as twice the number of objects being juggled. If the
juggler fails his Sleight of Hand check, he drops all juggled objects but one, determined randomly.
This ability replaces versatile performance.

## Evasion (Ex) {#evasion}

At 2nd level, a juggler gains [evasion](ref/ability/evasion), as the [rogue](ref/class/rogue) class
feature of the same name. At 12th level, he gains [improved evasion](ref/talent/improved-evasion),
as the rogue advanced talent. This ability replaces well-versed and soothing performance.
