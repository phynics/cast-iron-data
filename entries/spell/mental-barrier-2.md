+++
id = "ref/spell/mental-barrier-2"
kind = "spell"
title = "Mental Barrier II"
aon = "SpellDisplay.aspx?ItemName=Mental%20Barrier%20II"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "mental_barrier_2", path = "json/spells14.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/mental-barrier-1" },
]
[[sources]]
publication = "occult-adventures"
page = "175"

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Psychic", level = 2 },
]
casting_time = "1 immediate action"
components = "V"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 round"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 2: Psychic
Casting time: 1 immediate action
Components: V
Range: personal
Duration: 1 round
Saving throw: none
Spell resistance: no
Target: you
:::

### Mental Barrier II

This spell functions as [mental barrier I](ref/spell/mental-barrier-1), but the shield bonus to AC
increases to +6. In addition, you take half damage from mind thrust I, II, and III (reduced to
one-quarter on a successful Will save). This spell can be undercast.
