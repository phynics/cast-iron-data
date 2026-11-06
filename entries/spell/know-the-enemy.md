+++
id = "ref/spell/know-the-enemy"
kind = "spell"
title = "Know the Enemy"
source_ids = ["ultimate-magic", "mythic-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "know_the_enemy", path = "json/spells6.json" },
]

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

**Sources:** Ultimate Magic pg 226

You commune with the divine, reflecting on one type of creature you encountered in the last day. You
may make a Knowledge check regarding that creature type with a +10 insight bonus.

### Mythic Know the Enemy

**Sources:** Mythic Adventures pg 99\
The insight bonus increases to +15 plus your tier. If the check is successful, you gain a +5 insight
bonus on your next attack roll or saving throw against a creature of that type, as long as the roll
occurs within 24 hours of casting the spell.
