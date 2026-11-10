+++
id = "ref/spell/feather-step-mass"
kind = "spell"
title = "Mass Feather Step"
aon = "SpellDisplay.aspx?ItemName=Feather%20Step%2C%20Mass"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "feather_step_mass", path = "json/spells4.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/feather-step" },
]
[[sources]]
publication = "advanced-players-guide"
page = "221"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Bard", level = 3 },
  { class = "Druid", level = 3 },
  { class = "Hunter", level = 3 },
  { class = "Psychic", level = 3 },
  { class = "Ranger", level = 3 },
  { class = "Skald", level = 3 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature/level, no two of which can be more than 30 ft. apart" },
]
duration = "10 minutes/level"
saving_throw = "Fortitude negates (harmless)"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 3: Bard, Druid, Hunter, Psychic, Ranger, Skald
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Target: one creature/level, no two of which can be more than 30 ft. apart
Duration: 10 minutes/level
Saving throw: Fortitude negates (harmless)
Spell resistance: yes
:::

### Mass Feather Step

As [feather step](ref/spell/feather-step), except this spell affects multiple creatures.
