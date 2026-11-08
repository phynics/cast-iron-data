+++
id = "ref/spell/rend-body-3"
kind = "spell"
title = "Rend Body III"
source_ids = ["psychic-anthology"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "rend_body_3", path = "json/spells8.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/rend-body-1" },
]

[fields]
kind = "spell"
school = "evocation"
levels = [
  { class = "Psychic", level = 5 },
]
casting_time = "1 full-round action"
components = "S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "instantaneous"
saving_throw = "Fortitude partial (see text)"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 5: Psychic
Casting time: 1 full-round action
Components: S
Range: close (25 ft. + 5 ft./2 levels)
Duration: instantaneous
Saving throw: Fortitude partial (see text)
Spell resistance: yes
Target: one creature
:::

### Rend Body III

**Sources:** Psychic Anthology pg 10

This spell functions as per [rend body I](ref/spell/rend-body-1), but the target takes 1d8 points of
damage per caster level you have (maximum 15d8), and if a limb is ripped from its body, the target
is sickened for as long as the bleed damage persists. This spell can be undercast.
