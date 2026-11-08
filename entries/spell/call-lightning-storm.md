+++
id = "ref/spell/call-lightning-storm"
kind = "spell"
title = "Call Lightning Storm"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "call_lightning_storm", path = "json/spells2.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/call-lightning" },
]

[fields]
kind = "spell"
school = "evocation"
descriptors = ["electricity"]
levels = [
  { class = "Druid", level = 3 },
  { class = "Hunter", level = 3 },
  { class = "Occultist", level = 3 },
  { class = "Shaman", level = 3 },
]
casting_time = "1 round"
components = "V, S"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Effect", value = "one or more 30-ft.-long vertical lines of lightning" },
]
duration = "1 minute/level"
saving_throw = "Reflex half"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 3: Druid, Hunter, Occultist, Shaman
Casting time: 1 round
Components: V, S
Range: medium (100 ft. + 10 ft./level)
Duration: 1 minute/level
Saving throw: Reflex half
Spell resistance: yes
Effect: one or more 30-ft.-long vertical lines of lightning
Descriptors: electricity
:::

### Call Lightning Storm

**Sources:** PRPG Core Rulebook pg 252

This spell functions like [call lightning](ref/spell/call-lightning), except that each bolt deals
5d6 points of electricity damage (or 5d10 if created outdoors in a stormy area), and you may call a
maximum of 15 bolts.
