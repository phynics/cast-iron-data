+++
id = "ref/spell/drain-construct"
kind = "spell"
title = "Drain Construct"
source_ids = ["people-of-the-wastes"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "drain_construct", path = "json/spells13.json" },
]

[fields]
kind = "spell"
school = "necromancy"
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Witch", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one construct" },
]
duration = "1 round/level (D)"
saving_throw = "Will negates"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 2: Arcanist, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level (D)
Saving throw: Will negates
Spell resistance: no
Target: one construct
:::

**Sources:** People of the Wastes pg 28

You weaken a target construct, temporarily sapping its animating force and limiting its normal
functionality. If the construct fails its saving throw, for the duration of this spell, it loses any
[damage reduction](ref/rule/damage-reduction) and [fast healing](ref/umr/fast-healing) it had and
its base speed is reduced by half. Additionally, the construct takes a -4 penalty to Strength while
this spell is in effect. This penalty increases by 2 for every 3 caster levels beyond 3rd (maximum
-14). If the construct is normally immune to magic, this spell's sapping effect is less penetrating
and the construct receives a +4 bonus on its saving throw.
