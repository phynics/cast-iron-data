+++
id = "ref/spell/fire-sneeze"
kind = "spell"
title = "Fire Sneeze"
source_ids = ["goblins-of-golarion"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "fire_sneeze", path = "json/spells4.json" },
]
[[sources]]
publication = "goblins-of-golarion"
page = "28"

[fields]
kind = "spell"
school = "evocation"
descriptors = ["air", "fire"]
levels = [
  { class = "Alchemist", level = 2 },
  { class = "Arcanist", level = 2 },
  { class = "Druid", level = 2 },
  { class = "Hunter", level = 2 },
  { class = "Investigator", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, M (hot pepper soaked in oil)"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 round + 1 round/2 levels"
saving_throw = "Reflex half"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 2: Alchemist, Arcanist, Druid, Hunter, Investigator, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M (hot pepper soaked in oil)
Range: personal
Duration: 1 round + 1 round/2 levels
Saving throw: Reflex half
Spell resistance: yes
Target: you
Descriptors: air, fire
:::

This spell causes you to begin sneezing gouts of fire that can not only set creatures ablaze but
also drop them flat on their backs. Once you cast this spell, you must sneeze each round as a
standard action-you can take no other standard action as long as this spell is in effect, nor can
you take full-round actions. Each time you sneeze, you produce a 10-foot-long cone of fire and wind.
All creatures caught in this cone take 2d6 points of fire damage - a successful Reflex save halves
this damage. Any creature that fails to resist this spell with a Reflex save must immediately make a
DC 12 Fortitude save or be knocked prone by the blast of wind associated with the sneeze.
