+++
id = "ref/spell/age-resistance"
kind = "spell"
title = "Age Resistance"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "age_resistance", path = "json/spells.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/age-resistance-lesser" },
]
[[sources]]
publication = "ultimate-magic"
page = "205"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Alchemist", level = 3 },
  { class = "Arcanist", level = 4 },
  { class = "Druid", level = 4 },
  { class = "Hunter", level = 4 },
  { class = "Investigator", level = 3 },
  { class = "Occultist", level = 3 },
  { class = "Psychic", level = 4 },
  { class = "Red Mantis Assassin", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Witch", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "24 hours"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 3: Alchemist, Investigator, Occultist\
4: Arcanist, Druid, Hunter, Psychic, Red Mantis Assassin, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: personal
Duration: 24 hours
Saving throw: none
Spell resistance: no
Target: you
:::

### Age Resistance

This spell functions as [lesser age resistance](ref/spell/age-resistance-lesser), except you ignore
the Strength, Dexterity, and Constitution penalties gained at middle and old age.
