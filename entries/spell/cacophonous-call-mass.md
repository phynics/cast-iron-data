+++
id = "ref/spell/cacophonous-call-mass"
kind = "spell"
title = "Mass Cacophonous Call"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "cacophonous_call_mass", path = "json/spells2.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/cacophonous-call" },
]
[[sources]]
publication = "advanced-players-guide"
page = "208"

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Bard", level = 5 },
  { class = "Skald", level = 5 },
]
casting_time = "1 standard action"
components = "V, S, M (a scrap of sheet music)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature/level (all of which must be within 30 feet)" },
]
duration = "1 round/level"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 5: Bard, Skald
Casting time: 1 standard action
Components: V, S, M (a scrap of sheet music)
Range: close (25 ft. + 5 ft./2 levels)
Target: one creature/level (all of which must be within 30 feet)
Duration: 1 round/level
Saving throw: Will negates
Spell resistance: yes
Subschool: Compulsion
Descriptors: mind-affecting
:::

### Mass Cacophonous Call

This spell functions as [cacophonous call](ref/spell/cacophonous-call), except that it affects
multiple creatures.
