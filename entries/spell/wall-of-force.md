+++
id = "ref/spell/wall-of-force"
kind = "spell"
title = "Wall of Force"
aon = "SpellDisplay.aspx?ItemName=Wall%20of%20Force"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "wall_of_force", path = "json/spells11.json" },
]
[[sources]]
publication = "core-rulebook"
page = "365"

[fields]
kind = "spell"
school = "evocation"
descriptors = ["force"]
levels = [
  { class = "Arcanist", level = 5 },
  { class = "Magus", level = 5 },
  { class = "Occultist", level = 5 },
  { class = "Psychic", level = 5 },
  { class = "Sorcerer", level = 5 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 standard action"
components = "V, S, M (powdered quartz)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Effect", value = "wall whose area is up to one 10-ft. square/level" },
]
duration = "1 round/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 5: Arcanist, Magus, Occultist, Psychic, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M (powdered quartz)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level (D)
Saving throw: none
Spell resistance: no
Effect: wall whose area is up to one 10-ft. square/level
Descriptors: force
:::

A wall of force creates an invisible wall of pure force. The wall cannot move and is not easily
destroyed. A wall of force is immune to [dispel magic](ref/spell/dispel-magic), although a
[mage's disjunction](ref/spell/mages-disjunction) can still dispel it. A wall of force can be
damaged by spells as normal, except for [disintegrate](ref/spell/disintegrate), which automatically
destroys it. It can be damaged by weapons and supernatural abilities, but a wall of force has
[hardness](ref/umr/hardness) 30 and a number of hit points equal to 20 per caster level. Contact
with a [sphere of annihilation](ref/magic-artifact/sphere-of-annihilation) or
[rod of cancellation](ref/magic-rod/rod-of-cancellation) instantly destroys a wall of force.

Breath weapons and spells cannot pass through a wall of force in either direction, although
[dimension door](ref/spell/dimension-door), [teleport](ref/spell/teleport), and similar effects can
bypass the barrier. It blocks ethereal creatures as well as material ones (though ethereal creatures
can usually circumvent the wall by going around it, through material floors and ceilings). Gaze
attacks can operate through a wall of force.

The caster can form the wall into a flat, vertical plane whose area is up to one 10-foot square per
level. The wall must be continuous and unbroken when formed. If its surface is broken by any object
or creature, the spell fails.

Wall of force can be made permanent with a [permanency](ref/spell/permanency) spell.
