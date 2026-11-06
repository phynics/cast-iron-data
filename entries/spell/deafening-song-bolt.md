+++
id = "ref/spell/deafening-song-bolt"
kind = "spell"
title = "Deafening Song Bolt"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "deafening_song_bolt", path = "json/spells3.json" },
]

[fields]
kind = "spell"
school = "evocation"
descriptors = ["sonic"]
levels = [
  { class = "Bard", level = 5 },
  { class = "Skald", level = 5 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "up to 3 creatures, no two of which can be more than 30 ft. apart" },
]
duration = "instantaneous"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 5: Bard, Skald
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: instantaneous
Saving throw: none
Spell resistance: no
Target: up to 3 creatures, no two of which can be more than 30 ft. apart
Descriptors: sonic
:::

**Sources:** Advanced Player's Guide pg 214

Three notes you sing or perform become tangible bolts of arcane energy that shriek across the
battlefield. Each bolt requires a ranged touch attack to hit and deals 3d10 points of sonic damage,
deafening the target for 1d6 rounds. The bolts may be fired at the same or different targets, but
all must be fired simultaneously.
