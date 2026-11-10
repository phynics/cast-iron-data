+++
id = "ref/spell/cats-grace-mass"
kind = "spell"
title = "Mass Cat's Grace"
aon = "SpellDisplay.aspx?ItemName=Cat%27s%20Grace%2C%20Mass"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "cats_grace_mass", path = "json/spells2.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/cats-grace" },
]
[[sources]]
publication = "core-rulebook"
page = "252"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Arcanist", level = 6 },
  { class = "Bard", level = 6 },
  { class = "Druid", level = 6 },
  { class = "Hunter", level = 6 },
  { class = "Magus", level = 6 },
  { class = "Psychic", level = 6 },
  { class = "Skald", level = 6 },
  { class = "Sorcerer", level = 6 },
  { class = "Summoner", level = 4 },
  { class = "Unchained Summoner", level = 6 },
  { class = "Wizard", level = 6 },
]
casting_time = "1 standard action"
components = "V, S, M (pinch of cat fur)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Targets", value = "one creature/level, no two of which can be more than 30 ft. apart" },
]
duration = "1 minute/level"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 4: Summoner\
6: Arcanist, Bard, Druid, Hunter, Magus, Psychic, Skald, Sorcerer, Unchained Summoner, Wizard
Casting time: 1 standard action
Components: V, S, M (pinch of cat fur)
Range: close (25 ft. + 5 ft./2 levels)
Targets: one creature/level, no two of which can be more than 30 ft. apart
Duration: 1 minute/level
Saving throw: Will negates (harmless)
Spell resistance: yes
:::

### Mass Cat's Grace

This spell functions like [cat's grace](ref/spell/cats-grace), except it affects multiple creatures.
