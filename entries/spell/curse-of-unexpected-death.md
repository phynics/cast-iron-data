+++
id = "ref/spell/curse-of-unexpected-death"
kind = "spell"
title = "Curse of Unexpected Death"
source_ids = ["pathfinder-89-palace-of-fallen-stars"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "curse_of_unexpected_death", path = "json/spells3.json" },
]

[fields]
kind = "spell"
school = "necromancy"
descriptors = ["curse", "death"]
levels = [
  { class = "Cleric", level = 4 },
  { class = "Oracle", level = 4 },
  { class = "Shaman", level = 5 },
  { class = "Warpriest", level = 4 },
  { class = "Witch", level = 5 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "living creature touched" },
]
duration = "1 minute/level (see text)"
saving_throw = "Fortitude partial (see text)"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 4: Cleric, Oracle, Warpriest\
5: Shaman, Witch
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: 1 minute/level (see text)
Saving throw: Fortitude partial (see text)
Spell resistance: yes
Target: living creature touched
Descriptors: curse, death
:::

**Sources:** Pathfinder \#89: Palace of Fallen Stars pg 74

> _Clerics of [Zyphus](ref/faith/zyphus) have access to the following spell._

You curse one living creature with a chance of instant and unexpected death. When you cast this
spell, your hand seethes with eerie gray fire. You must succeed at a melee touch attack to touch the
target, at which time the fire buries itself within the target's body and disappears. On the round
you touch the creature and once per minute thereafter, roll 1d100. On a result of 01-05, the spell
is triggered and the creature takes 8d6 points of damage + 1 point per caster level; the creature
can attempt a saving throw to reduce the damage to 2d6 points of damage + 1 point per caster level.
On a result of 06-100, nothing happens.

Once the spell is triggered or if the duration expires before it triggers, the magic ends and no
further 1d100 rolls are made. If the target has [spell resistance](ref/rule/spell-resistance), a
caster level check is made when you succeed at the touch attack. A creature can be affected by only
one instance of this spell at a time. The untriggered spell can be removed with
[dispel magic](ref/spell/dispel-magic), [remove curse](ref/spell/remove-curse), or similar effects.
