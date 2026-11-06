+++
id = "ref/spell/escaping-ward"
kind = "spell"
title = "Escaping Ward"
source_ids = ["advanced-race-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "escaping_ward", path = "json/spells4.json" },
]

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Bard", level = 2 },
  { class = "Hunter", level = 2 },
  { class = "Inquisitor", level = 2 },
  { class = "Magus", level = 2 },
  { class = "Ranger", level = 2 },
  { class = "Skald", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 round/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 2: Arcanist, Bard, Hunter, Inquisitor, Magus, Ranger, Skald, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S
Range: personal
Duration: 1 round/level
Saving throw: none
Spell resistance: no
Target: you
:::

**Sources:** Advanced Race Guide pg 68

> _[Halflings](ref/race/halfling) have access to the following spell._

This ward grants you extra maneuverability when you avoid attacks against larger foes. While
affected by this spell, when you are attacked and missed by a creature that is at least one size
category larger than you, you can, as an immediate action, move up to 5 feet away from the attacking
creature. You can increase this movement by 5 feet for every 5 caster levels. This movement does not
provoke attacks of opportunity.
