+++
id = "ref/spell/bless-weapon"
kind = "spell"
title = "Bless Weapon"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "bless_weapon", path = "json/spells12.json" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Paladin", level = 1 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "weapon touched" },
]
duration = "1 minute/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 1: Paladin
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: 1 minute/level
Saving throw: none
Spell resistance: no
Target: weapon touched
:::

**Sources:** PRPG Core Rulebook pg 250

This transmutation makes a weapon strike true against evil foes. The weapon is treated as having a
+1 enhancement bonus for the purpose of bypassing the DR of evil creatures or striking evil
incorporeal creatures (though the spell doesn't grant an actual enhancement bonus). The weapon also
becomes good-aligned, which means it can bypass the DR of certain creatures. (This effect overrides
and suppresses any other alignment the weapon might have.) Individual arrows or bolts can be
transmuted, but affected projectile weapons (such as bows) don't confer the benefit to the
projectiles they shoot.

In addition, all critical hit rolls against evil foes are automatically successful, so every threat
is a critical hit. This last effect does not apply to any weapon that already has a magical effect
related to critical hits, such as a keen weapon or a vorpal sword.
