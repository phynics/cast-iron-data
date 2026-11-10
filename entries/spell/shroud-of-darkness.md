+++
id = "ref/spell/shroud-of-darkness"
kind = "spell"
title = "Shroud of Darkness"
aon = "SpellDisplay.aspx?ItemName=Shroud%20of%20Darkness"
source_ids = ["inner-sea-temples"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "shroud_of_darkness", path = "json/spells9.json" },
]
[[sources]]
publication = "inner-sea-temples"
page = "13"

[fields]
kind = "spell"
school = "evocation"
descriptors = ["darkness"]
levels = [
  { class = "Antipaladin", level = 4 },
  { class = "Arcanist", level = 5 },
  { class = "Bard", level = 5 },
  { class = "Cleric", level = 5 },
  { class = "Inquisitor", level = 5 },
  { class = "Mesmerist", level = 4 },
  { class = "Oracle", level = 5 },
  { class = "Shaman", level = 5 },
  { class = "Skald", level = 5 },
  { class = "Sorcerer", level = 5 },
  { class = "Warpriest", level = 5 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 standard action"
components = "V, S, M/DF (a pinch of black sand)"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Targets", value = "one creature/3 levels, no two of which can be more than 30 ft. apart" },
]
duration = "1 round/level (D)"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 4: Antipaladin, Mesmerist\
5: Arcanist, Bard, Cleric, Inquisitor, Oracle, Shaman, Skald, Sorcerer, Warpriest, Wizard
Casting time: 1 standard action
Components: V, S, M/DF (a pinch of black sand)
Range: medium (100 ft. + 10 ft./level)
Duration: 1 round/level (D)
Saving throw: Will negates
Spell resistance: yes
Targets: one creature/3 levels, no two of which can be more than 30 ft. apart
Descriptors: darkness
:::

With a dark incantation and a gesture of your hand over your eyes, you cause a shroud of darkness to
descend upon the targets of this spell. The subjects treat the light level as two steps lower than
normal for the duration of this spell. Bright light becomes dim light, normal light becomes
darkness, and areas of dim light and darkness become supernaturally dark (as darkness, but even
creatures with [darkvision](ref/rule/darkvision) cannot see).
