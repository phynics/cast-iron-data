+++
id = "ref/spell/darkvision-communal"
kind = "spell"
title = "Communal Darkvision"
source_ids = ["core-rulebook", "ultimate-combat", "ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "darkvision_communal", path = "json/spells3.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/darkvision" },
]
[[sources]]
publication = "ultimate-combat"
page = "226"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Alchemist", level = 2 },
  { class = "Antipaladin", level = 2 },
  { class = "Arcanist", level = 2 },
  { class = "Hunter", level = 3 },
  { class = "Investigator", level = 2 },
  { class = "Medium", level = 2 },
  { class = "Occultist", level = 2 },
  { class = "Psychic", level = 2 },
  { class = "Ranger", level = 3 },
  { class = "Red Mantis Assassin", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, M (either a pinch of dried carrot or an agate)"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "1 hour/level"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 2: Alchemist, Antipaladin, Arcanist, Investigator, Medium, Occultist, Psychic, Red Mantis Assassin, Sorcerer, Wizard\
3: Hunter, Ranger
Casting time: 1 standard action
Components: V, S, M (either a pinch of dried carrot or an agate)
Range: touch
Duration: 1 hour/level
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
Target: creature touched
:::

### Communal Darkvision

This spell functions like [darkvision](ref/spell/darkvision), except you may divide the duration in
1-hour intervals among the creatures touched.
