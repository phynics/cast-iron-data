+++
id = "ref/spell/aggressive-thundercloud-greater"
kind = "spell"
title = "Greater Aggressive Thundercloud"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "aggressive_thundercloud_greater", path = "json/spells.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/aggressive-thundercloud" },
]
[[sources]]
publication = "advanced-class-guide"
page = "172"

[fields]
kind = "spell"
school = "evocation"
descriptors = ["electricity"]
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Druid", level = 4 },
  { class = "Hunter", level = 4 },
  { class = "Magus", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Witch", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S, M/DF (a piece of a tree struck by lightning)"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Effect", value = "5-ft.-diameter sphere" },
]
duration = "1 round/level"
saving_throw = "Reflex negates and Fortitude negates (see text)"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 4: Arcanist, Druid, Hunter, Magus, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M/DF (a piece of a tree struck by lightning)
Range: medium (100 ft. + 10 ft./level)
Effect: 5-ft.-diameter sphere
Duration: 1 round/level
Saving throw: Reflex negates and Fortitude negates (see text)
Spell resistance: yes
Descriptors: electricity
:::

### Greater Aggressive Thundercloud

This spell functions as [aggressive thundercloud](ref/spell/aggressive-thundercloud), except it
deals 6d6 points of electricity damage to any creature it strikes. The first creature damaged by the
cloud is also stunned for 1 round (Fortitude negates); this is a sonic effect.
