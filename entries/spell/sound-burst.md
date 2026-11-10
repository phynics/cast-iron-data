+++
id = "ref/spell/sound-burst"
kind = "spell"
title = "Sound Burst"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "sound_burst", path = "json/spells9.json" },
]
[[sources]]
publication = "core-rulebook"
page = "346"

[fields]
kind = "spell"
school = "evocation"
descriptors = ["sonic"]
levels = [
  { class = "Bard", level = 2 },
  { class = "Cleric", level = 2 },
  { class = "Occultist", level = 2 },
  { class = "Oracle", level = 2 },
  { class = "Skald", level = 2 },
  { class = "Warpriest", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, F/DF (a musical instrument)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Area", value = "10-ft.-radius spread" },
]
duration = "instantaneous"
saving_throw = "Fortitude partial"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 2: Bard, Cleric, Occultist, Oracle, Skald, Warpriest
Casting time: 1 standard action
Components: V, S, F/DF (a musical instrument)
Range: close (25 ft. + 5 ft./2 levels)
Duration: instantaneous
Saving throw: Fortitude partial
Spell resistance: yes
Area: 10-ft.-radius spread
Descriptors: sonic
:::

You blast an area with a tremendous cacophony. Every creature in the area takes 1d8 points of sonic
damage and must succeed on a Fortitude save to avoid being stunned for 1 round. Creatures that
cannot hear are not stunned but are still damaged.
