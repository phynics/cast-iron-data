+++
id = "ref/spell/life-conduit-greater"
kind = "spell"
title = "Greater Life Conduit"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "life_conduit_greater", path = "json/spells6.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/life-conduit" },
]
[[sources]]
publication = "ultimate-combat"
page = "234"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Healing"]
levels = [
  { class = "Summoner", level = 5 },
  { class = "Unchained Summoner", level = 5 },
]
casting_time = "1 standard action"
components = "V, S"
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
School: conjuration
Level: 5: Summoner, Unchained Summoner
Casting time: 1 standard action
Components: V, S
Range: personal
Target: you
Duration: 1 round/level
Saving throw: none
Spell resistance: no
Subschool: Healing
:::

### Greater Life Conduit

This spell functions like [life conduit](ref/spell/life-conduit), except you can transfer 3d6 hit
points as a swift action.
