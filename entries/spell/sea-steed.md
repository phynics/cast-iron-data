+++
id = "ref/spell/sea-steed"
kind = "spell"
title = "Sea Steed"
source_ids = ["ultimate-wilderness", "animal-archive"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "sea_steed", path = "json/spells15.json" },
]

[fields]
kind = "spell"
school = "transmutation"
subschools = ["Polymorph"]
levels = [
  { class = "Druid", level = 2 },
  { class = "Hunter", level = 2 },
  { class = "Paladin", level = 2 },
  { class = "Ranger", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "touch"
effects = [
  { label = "Target", value = "a creature you are mounted upon" },
]
duration = "10 minutes/level (D)"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 2: Druid, Hunter, Paladin, Ranger
Casting time: 1 standard action
Components: V, S, DF
Range: touch
Duration: 10 minutes/level (D)
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
Target: a creature you are mounted upon
Subschool: Polymorph
:::

**Sources:** Ultimate Wilderness pg 234, Animal Archive pg 25

The target adapts to life in the water, gaining piscine scales that cover its body and growing fins
in place of feet. It gains the aquatic subtype, the amphibious quality, and a swim speed equal to
its base speed before it came under the effect of this spell. While under the effects of this spell,
the target's base speed is reduced by 10 feet (minimum 10 feet).
