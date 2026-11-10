+++
id = "ref/spell/contagion-greater"
kind = "spell"
title = "Greater Contagion"
source_ids = ["core-rulebook", "ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "contagion_greater", path = "json/spells12.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/contagion" },
]
[[sources]]
publication = "ultimate-magic"
page = "211"

[fields]
kind = "spell"
school = "necromancy"
descriptors = ["disease", "evil"]
levels = [
  { class = "Arcanist", level = 6 },
  { class = "Cleric", level = 5 },
  { class = "Druid", level = 5 },
  { class = "Hunter", level = 5 },
  { class = "Oracle", level = 5 },
  { class = "Sorcerer", level = 6 },
  { class = "Warpriest", level = 5 },
  { class = "Witch", level = 5 },
  { class = "Wizard", level = 6 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one living creature" },
]
duration = "instantaneous"
saving_throw = "Fortitude negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 5: Cleric, Druid, Hunter, Oracle, Warpriest, Witch\
6: Arcanist, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Target: one living creature
Duration: instantaneous
Saving throw: Fortitude negates
Spell resistance: yes
Descriptors: disease, evil
:::

### Greater Contagion

This spell functions as [contagion](ref/spell/contagion), except the victim cannot overcome the
disease without magic-making the required number of saves does not cure it. The DC to remove the
disease with magic is equal to the save DC + 5.
