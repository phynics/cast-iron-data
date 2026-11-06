+++
id = "ref/spell/cacophonous-call"
kind = "spell"
title = "Cacophonous Call"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "cacophonous_call", path = "json/spells2.json" },
]

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Bard", level = 2 },
  { class = "Skald", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, M (a scrap of sheet music)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "1 round/level"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 2: Bard, Skald
Casting time: 1 standard action
Components: V, S, M (a scrap of sheet music)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level
Saving throw: Will negates
Spell resistance: yes
Target: one creature
Subschool: Compulsion
Descriptors: mind-affecting
:::

**Sources:** Advanced Player's Guide pg 208

You fill your target's mind with a blaring cacophony of discordant sounds, making it hard for the
target to act and concentrate. The creature gains the nauseated condition for the duration of the
spell if it fails its Will save.

### Mass Cacophonous Call

**Sources:** Advanced Player's Guide pg 208

This spell functions as cacophonous call, except that it affects multiple creatures.
