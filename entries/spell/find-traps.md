+++
id = "ref/spell/find-traps"
kind = "spell"
title = "Find Traps"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "find_traps", path = "json/spells4.json" },
]
[[sources]]
publication = "core-rulebook"
page = "281"

[fields]
kind = "spell"
school = "divination"
levels = [
  { class = "Cleric", level = 2 },
  { class = "Inquisitor", level = 2 },
  { class = "Medium", level = 2 },
  { class = "Occultist", level = 2 },
  { class = "Oracle", level = 2 },
  { class = "Psychic", level = 2 },
  { class = "Warpriest", level = 2 },
  { class = "Witch", level = 2 },
]
casting_time = "1 standard action"
components = "V, S"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 minute/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 2: Cleric, Inquisitor, Medium, Occultist, Oracle, Psychic, Warpriest, Witch
Casting time: 1 standard action
Components: V, S
Range: personal
Duration: 1 minute/level
Saving throw: none
Spell resistance: no
Target: you
:::

You gain intuitive insight into the workings of traps. You gain an insight bonus equal to 1/2 your
caster level (maximum +10) on Perception checks made to find traps while the spell is in effect. You
receive a check to notice traps within 10 feet of you, even if you are not actively searching for
them. Note that find traps grants no ability to disable the traps that you may find.
