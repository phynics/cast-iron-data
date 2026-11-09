+++
id = "ref/spell/unholy-ice"
kind = "spell"
title = "Unholy Ice"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "unholy_ice", path = "json/spells11.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/holy-ice" },
]
[[sources]]
publication = "ultimate-magic"
page = "245"

[fields]
kind = "spell"
school = "transmutation"
descriptors = ["cold", "evil", "water"]
levels = [
  { class = "Cleric", level = 5 },
  { class = "Oracle", level = 5 },
  { class = "Warpriest", level = 5 },
]
casting_time = "1 standard action"
components = "V, S, M (a flask of unholy water or 5 pounds of powdered silver worth 25 gp)"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Effect", value = "wall of ice or flying ice javelins (see text)" },
]
duration = "1 minute/level, instantaneous, or until expended (see text)"
saving_throw = "Reflex negates or none (see text)"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 5: Cleric, Oracle, Warpriest
Casting time: 1 standard action
Components: V, S, M (a flask of unholy water or 5 pounds of powdered silver worth 25 gp)
Range: medium (100 ft. + 10 ft./level)
Duration: 1 minute/level, instantaneous, or until expended (see text)
Saving throw: Reflex negates or none (see text)
Spell resistance: yes
Effect: wall of ice or flying ice javelins (see text)
Descriptors: cold, evil, water
:::

This spell functions as [holy ice](ref/spell/holy-ice), except it is made of frozen unholy water
rather than holy water.
