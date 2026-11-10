+++
id = "ref/spell/hold-monster-mass"
kind = "spell"
title = "Mass Hold Monster"
aon = "SpellDisplay.aspx?ItemName=Hold%20Monster%2C%20Mass"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "hold_monster_mass", path = "json/spells5.json" },
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
  { class = "Arcanist", level = 9 },
  { class = "Psychic", level = 9 },
  { class = "Sorcerer", level = 9 },
  { class = "Witch", level = 9 },
  { class = "Wizard", level = 9 },
]
casting_time = "1 standard action"
components = "V, S, M/DF (one hard metal bar or rod, which can be as small as a three-penny nail)"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Targets", value = "one or more creatures, no two of which can be more than 30 ft. apart" },
]
duration = "1 round/level (d); see text"
saving_throw = "Will negates; see text"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 9: Arcanist, Psychic, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M/DF (one hard metal bar or rod, which can be as small as a three-penny nail)
Range: medium (100 ft. + 10 ft./level)
Targets: one or more creatures, no two of which can be more than 30 ft. apart
Duration: 1 round/level (d); see text
Saving throw: Will negates; see text
Spell resistance: yes
Subschool: Compulsion
Descriptors: mind-affecting
:::

### Mass Hold Monster

This spell functions like [hold person](ref/spell/hold-person), except that it affects multiple
creatures and holds any living creature that fails its Will save.
