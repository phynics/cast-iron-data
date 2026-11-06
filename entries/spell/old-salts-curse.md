+++
id = "ref/spell/old-salts-curse"
kind = "spell"
title = "Old Salt's Curse"
source_ids = ["advanced-race-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "old_salts_curse", path = "json/spells7.json" },
]

[fields]
kind = "spell"
school = "necromancy"
descriptors = ["curse"]
levels = [
  { class = "Druid", level = 5 },
  { class = "Hunter", level = 5 },
  { class = "Mesmerist", level = 4 },
  { class = "Witch", level = 5 },
]
casting_time = "1 standard action"
components = "V, S, M (a flask of seawater)"
range = "touch"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "permanent"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 4: Mesmerist\
5: Druid, Hunter, Witch
Casting time: 1 standard action
Components: V, S, M (a flask of seawater)
Range: touch
Duration: permanent
Saving throw: Will negates
Spell resistance: yes
Target: one creature
Descriptors: curse
:::

**Sources:** Advanced Race Guide pg 79

> _[Humans](ref/race/human) have access to the following spells._

You inflict a curse of the roiling sea upon the target, making it permanently sickened. Anytime the
target is on or in the water more than a mile from shore, it also becomes staggered with
seasickness. This curse cannot be dispelled, though [remove curse](ref/spell/remove-curse) or
[break enchantment](ref/spell/break-enchantment) can negate it.
