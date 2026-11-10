+++
id = "ref/spell/id-insinuation-4"
kind = "spell"
title = "Id Insinuation IV"
aon = "SpellDisplay.aspx?ItemName=Id%20Insinuation%20IV"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "id_insinuation_4", path = "json/spells5.json" },
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

### Id Insinuation IV

This functions as [id insinuation I](ref/spell/id-insinuation-1), except as noted above. In
addition, on the first round of the effect, you can select the result of each creature's confused
condition without having to roll, but this doesn't allow you to make any decisions about how that
result is applied. On the following rounds of the effect, the targets of this spell must roll twice
to determine their confused effect. You select which roll is used. This spell can be undercast.
