+++
id = "ref/spell/life-conduit-improved"
kind = "spell"
title = "Improved Life Conduit"
aon = "SpellDisplay.aspx?ItemName=Life%20Conduit%2C%20Improved"
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
subschools = ["healing"]
levels = [
  { class = "Summoner", level = 3 },
  { class = "Unchained Summoner", level = 3 },
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
Level: 3: Summoner, Unchained Summoner
Casting time: 1 standard action
Components: V, S
Range: personal
Duration: 1 round/level
Saving throw: none
Spell resistance: no
Target: you
Subschool: healing
:::

### Improved Life Conduit

This spell functions like [life conduit](ref/spell/life-conduit), except you can transfer 2d6 hit
points as a swift action.
