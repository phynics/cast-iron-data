+++
id = "ref/spell/aura-of-inviolate-ownership"
kind = "spell"
title = "Aura of Inviolate Ownership"
source_ids = ["melee-tactics-toolbox"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "aura_of_inviolate_ownership", path = "json/spells.json" },
]
[[sources]]
publication = "melee-tactics-toolbox"
page = "30"

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Cleric", level = 3 },
  { class = "Inquisitor", level = 3 },
  { class = "Oracle", level = 3 },
  { class = "Paladin", level = 3 },
  { class = "Warpriest", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Targets", value = "one creature/level, no two of which can be more than 30 ft. apart" },
]
duration = "1 round/level"
saving_throw = "Fortitude negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 3: Cleric, Inquisitor, Oracle, Paladin, Warpriest
Casting time: 1 standard action
Components: V, S, DF
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level
Saving throw: Fortitude negates (harmless)
Spell resistance: yes (harmless)
Targets: one creature/level, no two of which can be more than 30 ft. apart
:::

This spell wards the attended items of all creatures it targets (items held, securely fastened to
their person, or in containers on their person), enhancing each creature's grip and protecting items
from loss or theft. The DC of Sleight of Hand checks to remove items warded by the spell is
increased by 20, and affected creatures gain a +20 bonus to their CMDs against disarm and steal
combat maneuvers.
