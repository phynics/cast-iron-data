+++
id = "ref/spell/undeath-to-death"
kind = "spell"
title = "Undeath to Death"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "undeath_to_death", path = "json/spells11.json" },
]

[fields]
kind = "spell"
school = "necromancy"
levels = [
  { class = "Arcanist", level = 6 },
  { class = "Cleric", level = 6 },
  { class = "Inquisitor", level = 6 },
  { class = "Oracle", level = 6 },
  { class = "Sorcerer", level = 6 },
  { class = "Spiritualist", level = 6 },
  { class = "Warpriest", level = 6 },
  { class = "Wizard", level = 6 },
]
casting_time = "1 standard action"
components = "V, S, M/DF (diamond powder worth 500 gp)"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Area", value = "several undead creatures within a 40-ft.-radius burst" },
]
duration = "instantaneous"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 6: Arcanist, Cleric, Inquisitor, Oracle, Sorcerer, Spiritualist, Warpriest, Wizard
Casting time: 1 standard action
Components: V, S, M/DF (diamond powder worth 500 gp)
Range: medium (100 ft. + 10 ft./level)
Duration: instantaneous
Saving throw: Will negates
Spell resistance: yes
Area: several undead creatures within a 40-ft.-radius burst
:::

**Sources:** PRPG Core Rulebook pg 363

This spell functions like [circle of death](ref/spell/circle-of-death), except that it destroys
undead creatures as noted above.
