+++
id = "ref/spell/bestow-planar-infusion-3"
kind = "spell"
title = "Bestow Planar Infusion III"
source_ids = ["planar-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "bestow_planar_infusion_3", path = "json/spells12.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/bestow-planar-infusion-1" },
]

[fields]
kind = "spell"
school = "evocation"
levels = [
  { class = "Arcanist", level = 1 },
  { class = "Cleric", level = 1 },
  { class = "Inquisitor", level = 1 },
  { class = "Magus", level = 1 },
  { class = "Medium", level = 1 },
  { class = "Occultist", level = 1 },
  { class = "Oracle", level = 1 },
  { class = "Psychic", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Summoner", level = 1 },
  { class = "Unchained Summoner", level = 1 },
  { class = "Warpriest", level = 1 },
  { class = "Witch", level = 1 },
  { class = "Wizard", level = 1 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "1 hour/level"
saving_throw = "Fortitude negates (harmless)"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 1: Arcanist, Cleric, Inquisitor, Magus, Medium, Occultist, Oracle, Psychic, Sorcerer, Summoner, Unchained Summoner, Warpriest, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: 1 hour/level
Saving throw: Fortitude negates (harmless)
Spell resistance: yes
Target: creature touched
:::

### Bestow Planar Infusion III

**Sources:** Planar Adventures pg 39

This functions as [bestow planar infusion I](ref/spell/bestow-planar-infusion-1), except that the
touched creature gains the greater infusion of the current plane.
