+++
id = "ref/spell/unlife-current"
kind = "spell"
title = "Unlife Current"
source_ids = ["aquatic-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "unlife_current", path = "json/spells6.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/life-current" },
]
[[sources]]
publication = "aquatic-adventures"
page = "61"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Healing"]
descriptors = ["water"]
levels = [
  { class = "Cleric", level = 3 },
  { class = "Druid", level = 3 },
  { class = "Hunter", level = 3 },
  { class = "Oracle", level = 3 },
  { class = "Paladin", level = 3 },
  { class = "Ranger", level = 3 },
  { class = "Shaman", level = 3 },
  { class = "Warpriest", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Area", value = "current or portion of current" },
]
duration = "1 round"
saving_throw = "Will half"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 3: Cleric, Druid, Hunter, Oracle, Paladin, Ranger, Shaman, Warpriest
Casting time: 1 standard action
Components: V, S, DF
Range: medium (100 ft. + 10 ft./level)
Duration: 1 round
Saving throw: Will half
Spell resistance: yes
Area: current or portion of current
Subschool: Healing
Descriptors: water
:::

### Unlife Current

This functions as [life current](ref/spell/life-current) except you infuse the current with negative
energy, so it heals undead and harms living creatures.
