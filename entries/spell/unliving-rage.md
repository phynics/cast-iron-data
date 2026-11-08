+++
id = "ref/spell/unliving-rage"
kind = "spell"
title = "Unliving Rage"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "unliving_rage", path = "json/spells11.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/rage" },
]

[fields]
kind = "spell"
school = "necromancy"
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Cleric", level = 2 },
  { class = "Mesmerist", level = 2 },
  { class = "Oracle", level = 2 },
  { class = "Sorcerer", level = 3 },
  { class = "Spiritualist", level = 3 },
  { class = "Warpriest", level = 2 },
  { class = "Witch", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Targets", value = "one willing undead creature per 3 levels, no two of which can be more than 30 ft. apart" },
]
duration = "concentration+ 1 round/level (D)"
saving_throw = "none"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 2: Cleric, Mesmerist, Oracle, Warpriest\
3: Arcanist, Sorcerer, Spiritualist, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: medium (100 ft. + 10 ft./level)
Duration: concentration+ 1 round/level (D)
Saving throw: none
Spell resistance: yes
Targets: one willing undead creature per 3 levels, no two of which can be more than 30 ft. apart
:::

**Sources:** Advanced Class Guide pg 198

This spell functions as [rage](ref/spell/rage), except it affects only undead creatures and bolsters
them with necromantic energy rather than emotion. Each affected creature gains a +2 profane bonus to
Strength and Charisma, a +1 profane bonus on Will saves, and a -2 penalty to AC. The effect is
otherwise identical to a barbarian's rage.
