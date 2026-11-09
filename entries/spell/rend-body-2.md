+++
id = "ref/spell/rend-body-2"
kind = "spell"
title = "Rend Body II"
aon = "SpellDisplay.aspx?ItemName=Rend%20Body%20II"
source_ids = ["psychic-anthology"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "rend_body_2", path = "json/spells8.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/rend-body-1" },
]
[[sources]]
publication = "psychic-anthology"
page = "10"

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

### Rend Body II

This spell functions as per [rend body I](ref/spell/rend-body-1), but the target takes 1d8 points of
damage per caster level you have (maximum 10d8). This spell can be undercast.
