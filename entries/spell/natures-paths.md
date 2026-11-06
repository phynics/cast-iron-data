+++
id = "ref/spell/natures-paths"
kind = "spell"
title = "Nature's Paths"
source_ids = ["villain-codex", "heroes-of-the-wild"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "natures_paths", path = "json/spells7.json" },
]

[fields]
kind = "spell"
school = "divination"
levels = [
  { class = "Bard", level = 1 },
  { class = "Druid", level = 1 },
  { class = "Hunter", level = 1 },
  { class = "Inquisitor", level = 1 },
  { class = "Ranger", level = 1 },
  { class = "Shaman", level = 1 },
  { class = "Witch", level = 1 },
]
casting_time = "1 standard action"
components = "V, S, M/DF (a smooth stone)"
range = "touch"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "8 hours (D)"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 1: Bard, Druid, Hunter, Inquisitor, Ranger, Shaman, Witch
Casting time: 1 standard action
Components: V, S, M/DF (a smooth stone)
Range: touch
Duration: 8 hours (D)
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
Target: one creature
:::

**Sources:** Villain Codex pg 164, Heroes of the Wild pg 31

The target instinctively knows the shortest, easiest, and fastest way through the wilderness. For
the purpose of determining overland speed, the target treats any trackless terrain as though there
were a trail or road, and any terrain with a road or trail as though there were a highway. Up to one
creature per caster level traveling with the target can also benefit from the effect. The spell
functions only outdoors and does not function in magically altered terrain.
