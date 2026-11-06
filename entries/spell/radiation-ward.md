+++
id = "ref/spell/radiation-ward"
kind = "spell"
title = "Radiation Ward"
source_ids = ["heroes-of-the-darklands"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "radiation_ward", path = "json/spells8.json" },
]

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Alchemist", level = 2 },
  { class = "Arcanist", level = 2 },
  { class = "Cleric", level = 2 },
  { class = "Druid", level = 2 },
  { class = "Hunter", level = 1 },
  { class = "Oracle", level = 2 },
  { class = "Ranger", level = 1 },
  { class = "Shaman", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Warpriest", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "1 hour/level (D)"
saving_throw = "Fortitude negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 1: Hunter, Ranger\
2: Alchemist, Arcanist, Cleric, Druid, Oracle, Shaman, Sorcerer, Warpriest, Wizard
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: 1 hour/level (D)
Saving throw: Fortitude negates (harmless)
Spell resistance: yes (harmless)
Target: creature touched
:::

**Sources:** Heroes of the Darklands pg 15

A creature warded by this spell gains a +4 bonus on saving throws against radiation-based effects.
In addition, the warded creature is immediately aware when it enters an area of radiation, as well
as the radiation level (low, medium, high, or severe) suffusing the area.
