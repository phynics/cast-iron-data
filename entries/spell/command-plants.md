+++
id = "ref/spell/command-plants"
kind = "spell"
title = "Command Plants"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "command_plants", path = "json/spells12.json" },
]
[[sources]]
publication = "core-rulebook"
page = "257"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Druid", level = 4 },
  { class = "Hunter", level = 3 },
  { class = "Ranger", level = 3 },
  { class = "Shaman", level = 4 },
]
casting_time = "1 standard action"
components = "V"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Targets", value = "up to 2 HD/level of plant creatures, no two of which can be more than 30 ft. apart" },
]
duration = "1 day/level"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 3: Hunter, Ranger\
4: Druid, Shaman
Casting time: 1 standard action
Components: V
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 day/level
Saving throw: Will negates
Spell resistance: yes
Targets: up to 2 HD/level of plant creatures, no two of which can be more than 30 ft. apart
:::

This spell allows you some degree of control over one or more plant creatures. Affected plant
creatures can understand you, and they perceive your words and actions in the most favorable way
(treat their attitude as friendly). They will not attack you while the spell lasts. You can try to
give a subject orders, but you must win an opposed Charisma check to convince it to do anything it
wouldn't ordinarily do. (Retries are not allowed.) A commanded plant never obeys suicidal or
obviously harmful orders, but it might be convinced that something very dangerous is worth doing.

You can affect a number of plant creatures whose combined level or HD do not exceed twice your
level.
