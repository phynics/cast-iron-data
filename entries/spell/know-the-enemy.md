+++
id = "ref/spell/know-the-enemy"
kind = "spell"
title = "Know the Enemy"
aon = "SpellDisplay.aspx?ItemName=Know%20the%20Enemy"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "know_the_enemy", path = "json/spells6.json" },
]
[[sources]]
publication = "ultimate-magic"
page = "226"

[fields]
kind = "spell"
school = "divination"
levels = [
  { class = "Cleric", level = 1 },
  { class = "Hunter", level = 1 },
  { class = "Inquisitor", level = 1 },
  { class = "Oracle", level = 1 },
  { class = "Paladin", level = 1 },
  { class = "Ranger", level = 1 },
  { class = "Warpriest", level = 1 },
]
casting_time = "1 minute"
components = "V, S, DF"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "instantaneous"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 1: Cleric, Hunter, Inquisitor, Oracle, Paladin, Ranger, Warpriest
Casting time: 1 minute
Components: V, S, DF
Range: personal
Duration: instantaneous
Saving throw: none
Spell resistance: no
Target: you
:::

You commune with the divine, reflecting on one type of creature you encountered in the last day. You
may make a Knowledge check regarding that creature type with a +10 insight bonus.
