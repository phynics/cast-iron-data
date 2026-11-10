+++
id = "ref/spell/hold-animal"
kind = "spell"
title = "Hold Animal"
aon = "SpellDisplay.aspx?ItemName=Hold%20Animal"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "hold_animal", path = "json/spells5.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/hold-person" },
]
[[sources]]
publication = "core-rulebook"
page = "296"

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Druid", level = 2 },
  { class = "Hunter", level = 2 },
  { class = "Mesmerist", level = 2 },
  { class = "Psychic", level = 2 },
  { class = "Ranger", level = 2 },
]
casting_time = "1 standard action"
components = "V, S"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Target", value = "one animal" },
]
duration = "1 round/level (d); see text"
saving_throw = "Will negates; see text"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 2: Druid, Hunter, Mesmerist, Psychic, Ranger
Casting time: 1 standard action
Components: V, S
Range: medium (100 ft. + 10 ft./level)
Duration: 1 round/level (d); see text
Saving throw: Will negates; see text
Spell resistance: yes
Target: one animal
Subschool: Compulsion
Descriptors: mind-affecting
:::

This spell functions like [hold person](ref/spell/hold-person), except that it affects an animal
instead of a humanoid.
