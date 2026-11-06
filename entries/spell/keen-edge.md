+++
id = "ref/spell/keen-edge"
kind = "spell"
title = "Keen Edge"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "keen_edge", path = "json/spells6.json" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Bloodrager", level = 3 },
  { class = "Inquisitor", level = 3 },
  { class = "Magus", level = 3 },
  { class = "Occultist", level = 3 },
  { class = "Red Mantis Assassin", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Targets", value = "one weapon or 50 projectiles, all of which must be together at the time of casting" },
]
duration = "10 minutes/level"
saving_throw = "Will negates (harmless) (object)"
spell_resistance = "yes (harmless) (object)"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 3: Arcanist, Bloodrager, Inquisitor, Magus, Occultist, Red Mantis Assassin, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: 10 minutes/level
Saving throw: Will negates (harmless) (object)
Spell resistance: yes (harmless) (object)
Targets: one weapon or 50 projectiles, all of which must be together at the time of casting
:::

**Sources:** PRPG Core Rulebook pg 303

This spell makes a weapon magically keen, improving its ability to deal telling blows. This
transmutation doubles the threat range of the weapon. A threat range of 20 becomes 19-20, a threat
range of 19-20 becomes 17-20, and a threat range of 18-20 becomes 15-20. The spell can be cast only
on piercing or slashing weapons. If cast on arrows or crossbow bolts, the keen edge on a particular
projectile ends after one use, whether or not the missile strikes its intended target. Treat
shuriken as arrows, rather than as thrown weapons, for the purpose of this spell.

Multiple effects that increase a weapon's threat range (such as the keen special weapon property and
the [Improved Critical](ref/feat/improved-critical) feat) don't stack. You can't cast this spell on
a natural weapon, such as a claw.
