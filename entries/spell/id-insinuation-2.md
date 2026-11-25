+++
id = "ref/spell/id-insinuation-2"
kind = "spell"
title = "Id Insinuation II"
aon = "SpellDisplay.aspx?ItemName=Id%20Insinuation%20II"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "id_insinuation_2", path = "json/spells5.json" },
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
subschools = ["compulsion"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Psychic", level = 3 },
]
casting_time = "1 standard action"
components = "S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Targets", value = "two creatures" },
]
duration = "concentration+ 1 round"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 3: Psychic
Casting time: 1 standard action
Components: S
Range: close (25 ft. + 5 ft./2 levels)
Duration: concentration+ 1 round
Saving throw: Will negates
Spell resistance: yes
Targets: two creatures
Subschool: compulsion
Descriptors: mind-affecting
:::

### Id Insinuation II

This functions as [id insinuation I](ref/spell/id-insinuation-1), except as noted above. In
addition, on the first round of the effect, the targets of this spell must roll twice to determine
the result of their confused condition. You select which roll is used. This spell can be undercast.
