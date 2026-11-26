+++
id = "ref/arc-bard/faith-singer"
kind = "archetype"
title = "Faith Singer"
aon = "ArchetypeDisplay.aspx?FixedName=Bard%20Faith%20Singer"
source_ids = ["healers-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "faith_singer", path = "json/archetypes_bard.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/bard" },
]
[[sources]]
publication = "healers-handbook"
page = "19"

[fields]
kind = "archetype"
features = [
  { anchor = "faithful" },
  { anchor = "devout-spell-knowledge", level = 2 },
]
trades = [
  { replaces = "Versatile performance", feature = "versatile-performance", by = ["devout-spell-knowledge"] },
]
+++

Faith singers show their faith in their deity with songs or other appropriate performances.

## Faithful {#faithful}

Like a cleric, a faith singer must worship a deity, and his alignment must be within one step of his
deity's alignment (_Pathfinder RPG Core Rulebook_ 166).

## Devout Spell Knowledge (Su) {#devout-spell-knowledge}

At 2nd level, a faith singer can select one [domain](ref/ability/domains) from among those belonging
to his deity. Once per day as a [spell-like ability](ref/umr/spell-like-abilities) using his bard
level as his caster level, he can cast the 1st-level domain spell while giving a bardic performance.
At 6th level, and every 4 bard levels thereafter, he can similarly cast the next-higher domain spell
as a [spell-like ability](ref/umr/spell-like-abilities) (to a maximum of the 5th-level domain spell
at bard level 18th). He can use each spell-like ability only once per day.

This ability replaces versatile performance.
