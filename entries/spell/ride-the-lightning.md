+++
id = "ref/spell/ride-the-lightning"
kind = "spell"
title = "Ride the Lightning"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "ride_the_lightning", path = "json/spells8.json" },
]

[fields]
kind = "spell"
school = "evocation"
descriptors = ["electricity"]
levels = [
  { class = "Arcanist", level = 9 },
  { class = "Sorcerer", level = 9 },
  { class = "Wizard", level = 9 },
]
casting_time = "1 swift action"
components = "V, S"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 round/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 9: Arcanist, Sorcerer, Wizard
Casting time: 1 swift action
Components: V, S
Range: personal
Duration: 1 round/level (D)
Saving throw: none
Spell resistance: no
Target: you
Descriptors: electricity
:::

**Sources:** Ultimate Magic pg 235

You may transform into lightning as a standard action and instantly travel in a straight line to a
distance of up to 120 feet, rematerializing in the new location as a free action. This movement does
not provoke attacks of opportunity. Creatures in this line take 10d6 points of electrical damage and
are staggered for 1 round (a successful Reflex save halves the damage and negates the staggered
condition, [spell resistance](ref/rule/spell-resistance) applies). Objects in your path are damaged
as well, with combustible objects being set ablaze and metals with low melting points melted. If
your path is interrupted by a barrier or otherwise deflected, you materialize short of your final
destination in the nearest open space; targets in the line to that point take damage as normal. You
are immune to electricity while this spell lasts.
