+++
id = "ref/spell/sunstalker"
kind = "spell"
title = "Sunstalker"
source_ids = ["adventurers-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "sunstalker", path = "json/spells10.json" },
]
[[sources]]
publication = "adventurers-guide"
page = "17"

[fields]
kind = "spell"
school = "illusion"
subschools = ["Glamer"]
descriptors = ["glamer"]
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Bard", level = 3 },
  { class = "Hunter", level = 3 },
  { class = "Ranger", level = 3 },
  { class = "Skald", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, M/DF"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "1 round/level"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 3: Arcanist, Bard, Hunter, Ranger, Skald, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M/DF
Range: touch
Duration: 1 round/level
Saving throw: Will negates (harmless)
Spell resistance: yes
Target: creature touched
Subschool: Glamer
Descriptors: glamer
:::

A touched creature becomes invisible (as per invisibility) as long as it is in direct sunlight (or
bright light shed by a [daylight](ref/spell/daylight) spell). If an action the target creature takes
causes the invisible creature to become visible but does not end the sunstalker spell's duration,
the creature can use this spell's magic to become invisible again as a standard action as long as it
stands in an area of sunlight (as defined above). The creature gains only concealment (20% miss
chance) in normal light.
