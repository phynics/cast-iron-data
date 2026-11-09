+++
id = "ref/spell/id-insinuation-3"
kind = "spell"
title = "Id Insinuation III"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "id_insinuation_3", path = "json/spells5.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/id-insinuation-1" },
]
[[sources]]
publication = "occult-adventures"
page = "173"

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Psychic", level = 2 },
]
casting_time = "1 standard action"
components = "S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "concentration+ 1 round"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 2: Psychic
Casting time: 1 standard action
Components: S
Range: close (25 ft. + 5 ft./2 levels)
Duration: concentration+ 1 round
Saving throw: Will negates
Spell resistance: yes
Target: one creature
Subschool: Compulsion
Descriptors: mind-affecting
:::

### Id Insinuation III

This functions as [id insinuation I](ref/spell/id-insinuation-1), except as noted above. In
addition, on the first 2 rounds of the effect, the targets of this spell must roll twice to
determine the result of their confused conditions. You select which roll is used. This spell can be
undercast.
