+++
id = "ref/spell/caging-bomb-admixture"
kind = "spell"
title = "Caging Bomb Admixture"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "caging_bomb_admixture", path = "json/spells2.json" },
]

[fields]
kind = "spell"
school = "evocation"
descriptors = ["force"]
levels = [
  { class = "Alchemist", level = 6 },
  { class = "Investigator", level = 6 },
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
School: evocation
Level: 6: Alchemist, Investigator
Casting time: 1 standard action
Components: V, S
Range: personal
Duration: 1 round/level
Saving throw: none
Spell resistance: no
Target: you
Descriptors: force
:::

**Sources:** Ultimate Combat pg 225

Upon drinking an extract created with this formulae, you make a significant change to your magical
reserve that modifies the nature of all bombs you create and throw during this extract's duration.
This effect on your magical reserve has no effect on any discoveries that you use to modify your
bombs, but you can only have one admixture effect (formulae with the word "bomb admixture" in its
title) active at a time. If you drink another bomb admixture, the effects of the former bomb
admixture end and the new one becomes active.

When you throw a bomb and hit a direct target, it creates an invisible cubical prison composed of a
solid wall of force. The prison is as large as the splash area of the bomb that you threw, and traps
any creature that is entirely inside the area.

Creatures within the area are caught and contained unless any creature within the splash radius is
too big to fit inside, in which case the effect automatically fails. Teleportation and other forms
of astral travel provide means for escape, but the force walls extend into the Ethereal Plane,
blocking ethereal travel.

Like a [wall of force](ref/spell/wall-of-force), the cage created by the caging bomb admixture
resists [dispel magic](ref/spell/dispel-magic), although a
[mage's disjunction](ref/spell/mages-disjunction) still functions. The walls of the cage can be
damaged by spells as normal, except for [disintegrate](ref/spell/disintegrate), which automatically
destroys the cage. The walls of this cage can be damaged by weapons and supernatural abilities, but
the cage has a [hardness](ref/umr/hardness) of 20 and a number of hit points equal to 20 per
alchemist level. Contact with a [sphere of annihilation](ref/magic-artifact/sphere-of-annihilation)
or a [rod of cancellation](ref/magic-rod/rod-of-cancellation) instantly destroys this cage.

When using caging bomb admixture, an alchemist can only have one cage in effect at a time. If the
alchemist throws another bomb during the duration of caging bomb admixture, any other cage created
by the earlier admixture ends, and a new one is created. When the duration of the caging bomb
admixture ends, so does any remaining cage created by this admixture's effect.
