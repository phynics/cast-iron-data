+++
id = "ref/spell/restful-cloak"
kind = "spell"
title = "Restful Cloak"
source_ids = ["adventurers-armory-2"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "restful_cloak", path = "json/spells8.json" },
]
[[sources]]
publication = "adventurers-armory-2"
page = "21"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Healing"]
levels = [
  { class = "Cleric", level = 2 },
  { class = "Druid", level = 2 },
  { class = "Hunter", level = 2 },
  { class = "Occultist", level = 2 },
  { class = "Oracle", level = 2 },
  { class = "Paladin", level = 2 },
  { class = "Ranger", level = 2 },
  { class = "Shaman", level = 2 },
  { class = "Warpriest", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, F (cloak)"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 hour/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 2: Cleric, Druid, Hunter, Occultist, Oracle, Paladin, Ranger, Shaman, Warpriest
Casting time: 1 standard action
Components: V, S, F (cloak)
Range: personal
Duration: 1 hour/level
Saving throw: none
Spell resistance: no
Target: you
Subschool: Healing
:::

A cloak you are wearing transforms into a canvas tent large enough to hold four Medium creatures,
firmly pitched in a flat area adjacent to you (if there is no such area, this spell simply fails). A
creature regains 1 hit point for each hour it rests in the tent, in addition to any other benefits
of resting. Additionally, a fatigued creature resting within the tent for 1 hour loses the fatigued
condition, but a creature cannot recover from being fatigued more than once per casting of restful
tent. At the end of the spell's duration, the tent transforms back into a cloak. If the tent is
moved prior to the expiration of the spell's duration, the spell immediately ends.
