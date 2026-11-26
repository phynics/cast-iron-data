+++
id = "ref/arc-barbarian/pack-rager"
kind = "archetype"
title = "Pack Rager"
aon = "ArchetypeDisplay.aspx?FixedName=Barbarian%20Pack%20Rager"
source_ids = ["monster-codex"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "pack_rager", path = "json/archetypes_barbarian.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/barbarian" },
]
[[sources]]
publication = "monster-codex"
page = "92"

[fields]
kind = "archetype"
features = [
  { anchor = "bonus-feat", level = 2 },
  { anchor = "raging-tactician", level = 7 },
]
trades = [
  { replaces = "Rage powers gained at 2nd, 6th, 10th, 14th, and 18th level", feature = "rage-powers", levels = [2, 6, 10, 14, 18], by = ["bonus-feat"] },
  { replaces = "Damage reduction", feature = "damage-reduction", by = ["raging-tactician"] },
]
+++

Barbarian rages can be a thing of savage beauty, exhibiting a lethal grace. While such uncontrolled
displays of carnage often disregard group tactics, there are those barbarians whose rages inspire
and spur on their allies during the ferocious dance of death.

## Bonus Feat {#bonus-feat}

At 2nd level and every 4 levels thereafter, the pack rager can take a bonus teamwork feat. This
teamwork feat must also be a combat feat. This ability replaces the rage powers gained at 2nd, 6th,
10th, 14th, and 18th level.

## Raging Tactician {#raging-tactician}

At 7th level, while a pack rager is raging, she grants a single teamwork feat she knows to all
allies within 30 feet who can see and hear her. She chooses the feat at the start of the rage, and
cannot change it during the rage. An ally who moves more than 30 feet away from the raging pack
rager loses access to the feat, but regains it again each time he moves back within 30 feet of the
raging pack rager. Allies do not need to meet the prerequisites of these teamwork feats.

At 13th level, the pack rager chooses two teamwork feats when she enters a rage, and grants her
allies the use of both of those feats when they are within 30 feet of her.

At 16th level, the pack rager grants these teamwork feats as long as her allies are within 60 feet
of her.

At 19th level, the pack rager chooses three teamwork feats when she enters a rage, and grants her
allies the use of all three feats when they are within 60 feet of her.

This ability replaces the [damage reduction](ref/rule/damage-reduction) class feature.
