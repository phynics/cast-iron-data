+++
id = "ref/spell/dance-of-a-thousand-cuts"
kind = "spell"
title = "Dance of a Thousand Cuts"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "dance_of_a_thousand_cuts", path = "json/spells3.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/dance-of-a-hundred-cuts" },
]
[[sources]]
publication = "ultimate-magic"
page = "216"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Bard", level = 4 },
  { class = "Skald", level = 4 },
]
casting_time = "1 standard action"
components = "V"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 round/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 4: Bard, Skald
Casting time: 1 standard action
Components: V
Range: personal
Duration: 1 round/level
Saving throw: none
Spell resistance: no
Target: you
:::

### Dance of a Thousand Cuts

This spell functions as [dance of a hundred cuts](ref/spell/dance-of-a-hundred-cuts), except you
also gain the benefits of haste.
