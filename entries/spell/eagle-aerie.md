+++
id = "ref/spell/eagle-aerie"
kind = "spell"
title = "Eagle Aerie"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "eagle_aerie", path = "json/spells13.json" },
]
[[sources]]
publication = "ultimate-magic"
page = "217"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Summoning"]
descriptors = ["good"]
levels = [
  { class = "Druid", level = 6 },
  { class = "Hunter", level = 6 },
  { class = "Summoner", level = 6 },
  { class = "Unchained Summoner", level = 6 },
]
casting_time = "1 round"
components = "V, S, DF"
range = "long (400 ft. + 40 ft./level)"
effects = [
  { label = "Effect", value = "summoned eagles" },
]
duration = "1 hour/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 6: Druid, Hunter, Summoner, Unchained Summoner
Casting time: 1 round
Components: V, S, DF
Range: long (400 ft. + 40 ft./level)
Duration: 1 hour/level
Saving throw: none
Spell resistance: no
Effect: summoned eagles
Subschool: Summoning
Descriptors: good
:::

You summon a flight of [giant eagles](ref/monster/eagle-giant-eagle) (one per three caster levels,
maximum of six) to ferry you and your allies across the skies. The eagles avoid combat if possible
but defend themselves if attacked; if the eagles attack, the remaining duration of the spell changes
from 1 hour per level to 1 round per level (so if the spell had 5 full hours left, the eagles remain
in combat for 5 rounds before the spell ends).
