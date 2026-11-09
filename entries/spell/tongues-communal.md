+++
id = "ref/spell/tongues-communal"
kind = "spell"
title = "Communal Tongues"
source_ids = ["core-rulebook", "ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "tongues_communal", path = "json/spells10.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/tongues" },
]
[[sources]]
publication = "ultimate-combat"
page = "248"

[fields]
kind = "spell"
school = "divination"
levels = [
  { class = "Adept", level = 3 },
  { class = "Alchemist", level = 3 },
  { class = "Arcanist", level = 3 },
  { class = "Bard", level = 2 },
  { class = "Cleric", level = 4 },
  { class = "Inquisitor", level = 2 },
  { class = "Investigator", level = 3 },
  { class = "Medium", level = 2 },
  { class = "Mesmerist", level = 2 },
  { class = "Oracle", level = 4 },
  { class = "Psychic", level = 3 },
  { class = "Shaman", level = 4 },
  { class = "Skald", level = 2 },
  { class = "Sorcerer", level = 3 },
  { class = "Spiritualist", level = 3 },
  { class = "Summoner", level = 3 },
  { class = "Unchained Summoner", level = 3 },
  { class = "Warpriest", level = 4 },
  { class = "Witch", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, M/DF (a clay model of a ziggurat)"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "10 minutes/level"
saving_throw = "Will negates (harmless)"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 2: Bard, Inquisitor, Medium, Mesmerist, Skald\
3: Adept, Alchemist, Arcanist, Investigator, Psychic, Sorcerer, Spiritualist, Summoner, Unchained Summoner, Witch, Wizard\
4: Cleric, Oracle, Shaman, Warpriest
Casting time: 1 standard action
Components: V, M/DF (a clay model of a ziggurat)
Range: touch
Duration: 10 minutes/level
Saving throw: Will negates (harmless)
Spell resistance: no
Target: creature touched
:::

### Communal Tongues

This spell functions like [tongues](ref/spell/tongues), except you divide the duration in 10-minute
intervals among the creatures touched.
