+++
id = "ref/spell/hunters-howl"
kind = "spell"
title = "Hunter's Howl"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "hunters_howl", path = "json/spells5.json" },
]
[[sources]]
publication = "advanced-players-guide"
page = "228"

[fields]
kind = "spell"
school = "necromancy"
descriptors = ["emotion", "fear", "mind-affecting"]
levels = [
  { class = "Hunter", level = 1 },
  { class = "Ranger", level = 1 },
]
casting_time = "1 standard action"
components = "V, S"
range = "20 ft."
effects = [
  { label = "Area", value = "20-ft.-radius burst" },
]
duration = "1 round/level"
saving_throw = "Will negates"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 1: Hunter, Ranger
Casting time: 1 standard action
Components: V, S
Range: 20 ft.
Duration: 1 round/level
Saving throw: Will negates
Spell resistance: no
Area: 20-ft.-radius burst
Descriptors: emotion, fear, mind-affecting
:::

With a single primal howl, you strike fear in your opponents. Until the end of the spell's duration,
you treat those affected by it as if they were your [favored enemy](ref/ability/favored-enemy),
gaining a +2 bonus on weapon attack and damage rolls against them, and a +2 bonus on Bluff,
Knowledge, Perception, Sense Motive, and Survival checks against them. If an affected creature is
already one of your favored enemies, it is shaken instead. This is a mind-affecting fear effect.
