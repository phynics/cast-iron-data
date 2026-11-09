+++
id = "ref/spell/life-conduit-improved"
kind = "spell"
title = "Improved Life Conduit"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "life_conduit_improved", path = "json/spells6.json" },
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
  { class = "Summoner", level = 1 },
  { class = "Unchained Summoner", level = 1 },
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
Level: 1: Summoner, Unchained Summoner
Casting time: 1 standard action
Components: V, S
Range: personal
Duration: 1 round/level
Saving throw: none
Spell resistance: no
Target: you
Subschool: Healing
:::

### Improved Life Conduit

This spell functions like [life conduit](ref/spell/life-conduit), except you can transfer 2d6 hit
points as a swift action.
