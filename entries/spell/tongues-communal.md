+++
id = "ref/spell/tongues-communal"
kind = "spell"
title = "Communal Tongues"
aon = "SpellDisplay.aspx?ItemName=Tongues%2C%20Communal"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "tongues_communal", path = "json/spells10.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/tongues" },
]
[[sources]]
publication = "ultimate-combat"
page = "247"

[fields]
kind = "spell"
school = "divination"
levels = [
  { class = "Alchemist", level = 4 },
  { class = "Arcanist", level = 4 },
  { class = "Bard", level = 3 },
  { class = "Cleric", level = 5 },
  { class = "Investigator", level = 4 },
  { class = "Mesmerist", level = 3 },
  { class = "Oracle", level = 5 },
  { class = "Psychic", level = 4 },
  { class = "Skald", level = 3 },
  { class = "Sorcerer", level = 4 },
  { class = "Summoner", level = 4 },
  { class = "Unchained Summoner", level = 4 },
  { class = "Warpriest", level = 5 },
  { class = "Witch", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, M/DF (a clay model of a ziggurat)"
range = "touch"
effects = [
  { label = "Targets", value = "creatures touched" },
]
duration = "10 minutes/level"
saving_throw = "Will negates (harmless)"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 3: Bard, Mesmerist, Skald\
4: Alchemist, Arcanist, Investigator, Psychic, Sorcerer, Summoner, Unchained Summoner, Witch, Wizard\
5: Cleric, Oracle, Warpriest
Casting time: 1 standard action
Components: V, M/DF (a clay model of a ziggurat)
Range: touch
Duration: 10 minutes/level
Saving throw: Will negates (harmless)
Spell resistance: no
Targets: creatures touched
:::

### Communal Tongues

This spell functions like [tongues](ref/spell/tongues), except you divide the duration in 10-minute
intervals among the creatures touched.
