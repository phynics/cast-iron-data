+++
id = "ref/arc-ranger/divine-tracker"
kind = "archetype"
title = "Divine Tracker"
aon = "ArchetypeDisplay.aspx?FixedName=Ranger%20Divine%20Tracker"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "divine_tracker", path = "json/archetypes_ranger.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/ranger" },
]
[[sources]]
publication = "advanced-class-guide"
page = "108"

[fields]
kind = "archetype"
features = [
  { anchor = "favored-weapon", level = 1 },
  { anchor = "blessings", level = 4 },
]
trades = [
  { replaces = "Wild empathy", feature = "wild-empathy", by = ["favored-weapon"] },
  { replaces = "Hunter's bond", feature = "hunter-s-bond", by = ["blessings"] },
]
+++

Blessed by his deity, a divine tracker hunts down those he deems deserving of his retribution. His
weapon is likely to find purchase in his favored enemy.

## Alignment {#alignment}

A divine tracker's alignment must be within one step of his deity's, along either the law/chaos axis
or the good/evil axis.

## Favored Weapon {#favored-weapon}

At 1st level, a divine tracker becomes proficient with the favored weapon of his deity. If his
deity's favored weapon is unarmed strike, he instead gains
[Improved Unarmed Strike](ref/feat/improved-unarmed-strike) as a bonus feat. This ability replaces
wild empathy.

## Blessings (Su) {#blessings}

At 4th level, a divine tracker forms a close bond with his deity's ethos. He selects two warpriest
[domains](ref/ability/domains) from among the domains granted by his deity, and gains the minor
[blessings](ref/ability/blessings) of those domains. A divine tracker can select an alignment domain
(Chaos, Evil, Good, or Law) only if his alignment matches that domain. If a divine tracker isn't
devoted to a particular deity, he still selects two blessings to represent his spiritual
inclinations and abilities, subject to GM approval. The restriction on alignment domains still
applies. A divine tracker uses his ranger level as his warpriest level to determine the effect of
the blessing. At 13th level, a divine tracker gains the major blessing from both of his domains.
This ability replaces hunter's bond.
