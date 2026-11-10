+++
id = "ref/spell/age-resistance-greater"
kind = "spell"
title = "Greater Age Resistance"
aon = "SpellDisplay.aspx?ItemName=Age%20Resistance%2C%20Greater"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "age_resistance_greater", path = "json/spells.json" },
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
  { class = "Alchemist", level = 5 },
  { class = "Arcanist", level = 7 },
  { class = "Druid", level = 7 },
  { class = "Investigator", level = 5 },
  { class = "Occultist", level = 5 },
  { class = "Psychic", level = 7 },
  { class = "Sorcerer", level = 7 },
  { class = "Witch", level = 7 },
  { class = "Wizard", level = 7 },
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
Level: 5: Alchemist, Investigator, Occultist\
7: Arcanist, Druid, Psychic, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: personal
Target: you
Duration: 24 hours
Saving throw: none
Spell resistance: no
:::

### Greater Age Resistance

This spell functions as [lesser age resistance](ref/spell/age-resistance-lesser), except you ignore
all Strength, Dexterity, and Constitution penalties gained from middle age, old age, and venerable
age.
