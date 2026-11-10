+++
id = "ref/spell/dark-light"
kind = "spell"
title = "Dark-Light"
aon = "SpellDisplay.aspx?ItemName=Dark-Light"
source_ids = ["kobolds-of-golarion"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "dark_light", path = "json/spells3.json" },
]
[[sources]]
publication = "kobolds-of-golarion"
page = "26"

[fields]
kind = "spell"
school = "evocation"
descriptors = ["light"]
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Cleric", level = 3 },
  { class = "Druid", level = 3 },
  { class = "Hunter", level = 3 },
  { class = "Oracle", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Warpriest", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, M/DF (a pinch of Darklands earth)"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Target", value = "all living creatures without light sensitivity in a 20-ft.-radius burst" },
]
duration = "instantaneous"
saving_throw = "Fortitude partial"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 3: Arcanist, Cleric, Druid, Hunter, Oracle, Sorcerer, Warpriest, Wizard
Casting time: 1 standard action
Components: V, S, M/DF (a pinch of Darklands earth)
Range: medium (100 ft. + 10 ft./level)
Duration: instantaneous
Saving throw: Fortitude partial
Spell resistance: yes
Target: all living creatures without light sensitivity in a 20-ft.-radius burst
Descriptors: light
:::

You evoke a powerful light that affects all sighted creatures that do not posses light sensitivity.
Those that succeed on their saves are dazzled for 1 round per level; those who fail are blinded for
the same duration.
