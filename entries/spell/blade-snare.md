+++
id = "ref/spell/blade-snare"
kind = "spell"
title = "Blade Snare"
source_ids = ["inner-sea-gods"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "blade_snare", path = "json/spells12.json" },
]

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Bloodrager", level = 3 },
  { class = "Druid", level = 3 },
  { class = "Hunter", level = 3 },
  { class = "Magus", level = 3 },
  { class = "Ranger", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 round/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 3: Arcanist, Bloodrager, Druid, Hunter, Magus, Ranger, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S
Range: personal
Duration: 1 round/level
Saving throw: none
Spell resistance: no
Target: you
:::

**Sources:** Inner Sea Gods pg 230

This spell creates an invisible magic field that does not stop weapons (whether manufactured or
natural) from moving toward you, but impedes their motion when they are retracted. When you are hit
with a melee attack, attempt a caster level check against your opponent's CMD. If your check
succeeds, your opponent's attacking weapon or body part becomes caught in the field, as if magically
affixed to your body. If your check fails, your opponent may retract its weapon.

If your opponent's melee weapon becomes trapped in the field, the opponent may release the weapon
and move away from you. If your opponent attacked with a part of its body (such as a fist, a horn, a
tail, etc.) or it attacked with a weapon but refuses to release it, your opponent gains the grappled
condition. Because you are not using any part of your body to maintain control over your opponent,
you do not gain the grappled condition.

Once an opponent's weapon is snared, you may attempt a new caster level check against that
opponent's CMD on each of your subsequent turns to maintain the grapple. This is a standard action,
during which you may make any of the usual grappling actions, but if you choose to pin the opponent,
you gain the grappled condition as well. On your opponent's turn, it may try to retract its weapon
or limb by attempting a combat maneuver check or Escape Artist check, the DC of which is equal to
the spell's saving throw.

While blade snare is active, you may make melee attacks and cast spells as normal, though you may
not make ranged weapon attacks; the magic field thwarts such attacks. You may not snare more than
one limb or weapon in the field at a time. If you already have an opponent's weapon or limb stuck in
the field and you are hit by a second melee attack, you must choose which weapon or limb to snare.
The other limb or weapon is unaffected by the spell.
