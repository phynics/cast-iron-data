+++
id = "ref/spell/last-azlantis-defending-sword-mass"
kind = "spell"
title = "Mass Last Azlanti's Defending Sword"
source_ids = ["arcane-anthology"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "last_azlantis_defending_sword_mass", path = "json/spells6.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/last-azlantis-defending-sword" },
]

[fields]
kind = "spell"
school = "evocation"
descriptors = ["force"]
levels = [
  { class = "Arcanist", level = 9 },
  { class = "Sorcerer", level = 9 },
  { class = "Wizard", level = 9 },
]
casting_time = "1 standard action"
components = "V, S, F (a miniature platinum sword worth 250 gp)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Effect", value = "up to one sword per 3 levels" },
]
duration = "1 round/level (D)"
saving_throw = "none"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 9: Arcanist, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, F (a miniature platinum sword worth 250 gp)
Range: close (25 ft. + 5 ft./2 levels)
Effect: up to one sword per 3 levels
Duration: 1 round/level (D)
Saving throw: none
Spell resistance: yes
Descriptors: force
:::

## Last Azlanti's Defending Sword

**Sources:** Arcane Anthology pg 9

You create a sword of force that functions as [mage's sword](ref/spell/mages-sword) except as
described here. The sword does not receive the additional +3 enhancement bonus a mage's sword
receives, and deals 3d6 points of force damage. You cannot command the sword. Until the sword is
triggered, it hovers in your space without interfering with your actions. While hovering in this
way, the sword attempts to defend you from incoming attacks, granting you a +4 shield bonus to your
AC. The first time a foe within close range damages you or forces you to attempt a saving throw that
you fail, the sword is triggered and begins attacking that target as described in mage's sword for
the duration of the spell. This ends the shield bonus. You cannot direct the sword to defend against
a new target once it has begun to attack. If its target moves beyond the sword's range, the sword
returns to you and hovers until the target is again within range. The sword's return does not
restore the spell's shield bonus to AC.

### Mass Last Azlanti's Defending Sword

**Sources:** Arcane Anthology pg 9

This spell functions as [Last Azlanti's defending sword](ref/spell/last-azlantis-defending-sword),
except you can create one sword per 5 caster levels, each of which must defend a different creature
within range.
