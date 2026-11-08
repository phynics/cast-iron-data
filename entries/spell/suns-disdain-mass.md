+++
id = "ref/spell/suns-disdain-mass"
kind = "spell"
title = "Mass Sun's Disdain"
source_ids = ["adventurers-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "suns_disdain_mass", path = "json/spells16.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/suns-disdain" },
]

[fields]
kind = "spell"
school = "transmutation"
descriptors = ["curse"]
levels = [
  { class = "Arcanist", level = 5 },
  { class = "Bloodrager", level = 5 },
  { class = "Cleric", level = 5 },
  { class = "Inquisitor", level = 5 },
  { class = "Oracle", level = 5 },
  { class = "Shaman", level = 5 },
  { class = "Sorcerer", level = 5 },
  { class = "Warpriest", level = 5 },
  { class = "Witch", level = 5 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 standard action"
components = "V, S, M/DF (a piece of glass)"
range = "long (400 ft. + 40 ft./level)"
effects = [
  { label = "Target", value = "one creature/level, no two of which can be more than 30 ft. apart" },
]
duration = "permanent"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 5: Arcanist, Bloodrager, Cleric, Inquisitor, Oracle, Shaman, Sorcerer, Warpriest, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M/DF (a piece of glass)
Range: long (400 ft. + 40 ft./level)
Target: one creature/level, no two of which can be more than 30 ft. apart
Duration: permanent
Saving throw: Will negates
Spell resistance: yes
Descriptors: curse
:::

### Mass Sun's Disdain

**Sources:** Adventurer's Guide pg 17

This spell functions like [sun's disdain](ref/spell/suns-disdain), except that it can affect
multiple creatures.
