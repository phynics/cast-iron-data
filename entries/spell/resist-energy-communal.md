+++
id = "ref/spell/resist-energy-communal"
kind = "spell"
title = "Communal Resist Energy"
source_ids = ["core-rulebook", "ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "resist_energy_communal", path = "json/spells8.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/resist-energy" },
]

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Adept", level = 2 },
  { class = "Alchemist", level = 2 },
  { class = "Arcanist", level = 2 },
  { class = "Bloodrager", level = 2 },
  { class = "Cleric", level = 2 },
  { class = "Druid", level = 2 },
  { class = "Hunter", level = 1 },
  { class = "Inquisitor", level = 2 },
  { class = "Investigator", level = 2 },
  { class = "Occultist", level = 2 },
  { class = "Oracle", level = 2 },
  { class = "Paladin", level = 2 },
  { class = "Psychic", level = 2 },
  { class = "Ranger", level = 1 },
  { class = "Shaman", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Spiritualist", level = 2 },
  { class = "Summoner", level = 2 },
  { class = "Unchained Summoner", level = 2 },
  { class = "Warpriest", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "10 minutes/level"
saving_throw = "Fortitude negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 1: Hunter, Ranger\
2: Adept, Alchemist, Arcanist, Bloodrager, Cleric, Druid, Inquisitor, Investigator, Occultist, Oracle, Paladin, Psychic, Shaman, Sorcerer, Spiritualist, Summoner, Unchained Summoner, Warpriest, Wizard
Casting time: 1 standard action
Components: V, S, DF
Range: touch
Duration: 10 minutes/level
Saving throw: Fortitude negates (harmless)
Spell resistance: yes (harmless)
Target: creature touched
:::

### Communal Resist Energy

**Sources:** Ultimate Combat pg 242

This spell functions like [resist energy](ref/spell/resist-energy), except you divide the duration
in 10-minute intervals among the creatures touched.
