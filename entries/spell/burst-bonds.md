+++
id = "ref/spell/burst-bonds"
kind = "spell"
title = "Burst Bonds"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "burst_bonds", path = "json/spells2.json" },
]

[fields]
kind = "spell"
school = "evocation"
levels = [
  { class = "Inquisitor", level = 1 },
]
casting_time = "1 standard action"
components = "V"
range = "touch"
effects = [
  { label = "Target", value = "one object or creature restraining you" },
]
duration = "instantaneous"
saving_throw = "Fortitude half (object)"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 1: Inquisitor
Casting time: 1 standard action
Components: V
Range: touch
Duration: instantaneous
Saving throw: Fortitude half (object)
Spell resistance: yes
Target: one object or creature restraining you
:::

**Sources:** Advanced Player's Guide pg 208

You blast your restraints with divine wrath, dealing 1d6 points of damage per caster level to the
target object (maximum 5d6), ignoring [hardness](ref/umr/hardness) of 10 or less. A Fortitude save
halves the damage, although only magical restraints receive a saving throw.

You can also target a creature that is grappling or otherwise restraining you (such as by adhesive
or the swallow whole ability) with the spell. You don't need to make a touch attack to use burst
bonds against a creature, and you can cast this spell without making a concentration check while
grappled or pinned. The creature does not take damage as above. If you are grappled and your target
fails its save, you may make an immediate attempt to break the grapple (but not reverse it) as a
free action, with a +1 luck bonus to your CMB per caster level (maximum +5). If the target creature
fails its save and you are restrained by an ability that originally allowed a saving throw, burst
bonds allows a new saving throw with a +1 luck bonus per two caster levels (maximum +5).
