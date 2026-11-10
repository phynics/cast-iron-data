+++
id = "ref/spell/eldritch-fever"
kind = "spell"
title = "Eldritch Fever"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "eldritch_fever", path = "json/spells4.json" },
]
[[sources]]
publication = "ultimate-magic"
page = "218"

[fields]
kind = "spell"
school = "necromancy"
descriptors = ["curse", "disease", "evil"]
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Inquisitor", level = 3 },
  { class = "Psychic", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Witch", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "instantaneous"
saving_throw = "Fortitude negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 3: Arcanist, Inquisitor, Psychic, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: instantaneous
Saving throw: Fortitude negates
Spell resistance: yes
Target: one creature
Descriptors: curse, disease, evil
:::

The target gains the [eldritch ague spellblight](ref/rule/minor-spellblights).
