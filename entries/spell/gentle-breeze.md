+++
id = "ref/spell/gentle-breeze"
kind = "spell"
title = "Gentle Breeze"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "gentle_breeze", path = "json/spells13.json" },
]

[fields]
kind = "spell"
school = "evocation"
descriptors = ["air"]
levels = [
  { class = "Arcanist", level = 1 },
  { class = "Druid", level = 1 },
  { class = "Hunter", level = 1 },
  { class = "Shaman", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Witch", level = 1 },
  { class = "Wizard", level = 1 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature or object" },
]
duration = "1 hour (D)"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 1: Arcanist, Druid, Hunter, Shaman, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 hour (D)
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
Target: one creature or object
Descriptors: air
:::

**Sources:** Advanced Class Guide pg 183

You create a light wind that blows only against the target, from a direction of your choice. The
breeze grants the target a +2 circumstance bonus on saves against very hot conditions, severe heat,
and saves against clouds, vapors, and gases (such as cloudkill, stinking cloud, and inhaled
poisons). There must be air present to use this spell.
