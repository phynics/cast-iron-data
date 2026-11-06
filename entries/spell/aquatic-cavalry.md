+++
id = "ref/spell/aquatic-cavalry"
kind = "spell"
title = "Aquatic Cavalry"
source_ids = ["ultimate-wilderness"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "aquatic_cavalry", path = "json/spells.json" },
]

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Summoning"]
levels = [
  { class = "Antipaladin", level = 2 },
  { class = "Druid", level = 2 },
  { class = "Hunter", level = 2 },
  { class = "Paladin", level = 2 },
  { class = "Ranger", level = 2 },
  { class = "Shaman", level = 2 },
  { class = "Summoner", level = 2 },
  { class = "Unchained Summoner", level = 2 },
]
casting_time = "1 round"
components = "V, S, DF"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Effect", value = "1 hippocampus plus 1 hippocampus/3 caster levels" },
]
duration = "1 hour/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 2: Antipaladin, Druid, Hunter, Paladin, Ranger, Shaman, Summoner, Unchained Summoner
Casting time: 1 round
Components: V, S, DF
Range: medium (100 ft. + 10 ft./level)
Duration: 1 hour/level (D)
Saving throw: none
Spell resistance: no
Effect: 1 hippocampus plus 1 hippocampus/3 caster levels
Subschool: Summoning
:::

**Sources:** Ultimate Wilderness pg 227

You summon a school of hippocampi (one plus one per 3 caster levels, to a maximum of six at 15th
level) to serve as combat-trained mounts. The hippocampi avoid combat if possible but defend
themselves if attacked. If any hippocampus attacks, the remaining duration of the spell changes from
1 hour per level to 1 round per level (so if a full 4 hours remained, the hippocampi last for only 4
more rounds).
