+++
id = "ref/spell/iron-spine"
kind = "spell"
title = "Iron Spine"
source_ids = ["legacy-of-the-first-world"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "iron_spine", path = "json/spells6.json" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Cleric", level = 4 },
  { class = "Magus", level = 3 },
  { class = "Oracle", level = 4 },
  { class = "Sorcerer", level = 3 },
  { class = "Warpriest", level = 4 },
  { class = "Witch", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, M/DF (cold iron ingot)"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Target", value = "one living creature" },
]
duration = "1 round/level"
saving_throw = "none"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 3: Arcanist, Magus, Sorcerer, Witch, Wizard\
4: Cleric, Oracle, Warpriest
Casting time: 1 standard action
Components: V, S, M/DF (cold iron ingot)
Range: medium (100 ft. + 10 ft./level)
Duration: 1 round/level
Saving throw: none
Spell resistance: yes
Target: one living creature
:::

**Sources:** Legacy of the First World pg 13

You launch an ingot of iron at the target. If you succeed at a ranged touch attack, the target's
skeleton or exoskeleton turns into jagged shards of cold iron. Whenever the target moves, it takes
1d6 points of piercing damage and is sickened for 1 round as metal spines stab into its flesh. This
damage is subject to [damage reduction](ref/rule/damage-reduction), but it overcomes damage
reduction as though it were a weapon of cold iron and magic. A creature affected by this spell can
choose to remain motionless to avoid taking damage. Creatures with DR/cold iron or DR/cold iron and
magic affected by this spell are nauseated instead of sickened. This spell has no effect on a
creature that has neither a skeleton nor a hard carapace.
