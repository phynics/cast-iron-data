+++
id = "ref/spell/endure-elements-communal"
kind = "spell"
title = "Communal Endure Elements"
aon = "SpellDisplay.aspx?ItemName=Endure%20Elements%2C%20Communal"
source_ids = ["core-rulebook", "ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "endure_elements_communal", path = "json/spells4.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/endure-elements" },
]
[[sources]]
publication = "ultimate-combat"
page = "228"

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Adept", level = 1 },
  { class = "Alchemist", level = 1 },
  { class = "Arcanist", level = 1 },
  { class = "Bloodrager", level = 1 },
  { class = "Cleric", level = 1 },
  { class = "Druid", level = 1 },
  { class = "Hunter", level = 1 },
  { class = "Investigator", level = 1 },
  { class = "Oracle", level = 1 },
  { class = "Paladin", level = 1 },
  { class = "Psychic", level = 1 },
  { class = "Ranger", level = 1 },
  { class = "Shaman", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Spiritualist", level = 1 },
  { class = "Summoner", level = 1 },
  { class = "Unchained Summoner", level = 1 },
  { class = "Warpriest", level = 1 },
  { class = "Wizard", level = 1 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "24 hours"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 1: Adept, Alchemist, Arcanist, Bloodrager, Cleric, Druid, Hunter, Investigator, Oracle, Paladin, Psychic, Ranger, Shaman, Sorcerer, Spiritualist, Summoner, Unchained Summoner, Warpriest, Wizard
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: 24 hours
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
Target: creature touched
:::

### Communal Endure Elements

This spell functions like [endure elements](ref/spell/endure-elements), except you divide the
duration in 1-hour increments among the creatures touched.
