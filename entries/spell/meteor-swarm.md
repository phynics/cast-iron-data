+++
id = "ref/spell/meteor-swarm"
kind = "spell"
title = "Meteor Swarm"
aon = "SpellDisplay.aspx?ItemName=Meteor%20Swarm"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "meteor_swarm", path = "json/spells14.json" },
]
[[sources]]
publication = "core-rulebook"
page = "313"

[fields]
kind = "spell"
school = "evocation"
descriptors = ["fire"]
levels = [
  { class = "Arcanist", level = 9 },
  { class = "Sorcerer", level = 9 },
  { class = "Wizard", level = 9 },
]
casting_time = "1 standard action"
components = "V, S"
range = "long (400 ft. + 40 ft./level)"
effects = [
  { label = "Area", value = "four 40-ft.-radius spreads, see text" },
]
duration = "instantaneous"
saving_throw = "none or Reflex half, see text"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 9: Arcanist, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S
Range: long (400 ft. + 40 ft./level)
Duration: instantaneous
Saving throw: none or Reflex half, see text
Spell resistance: yes
Area: four 40-ft.-radius spreads, see text
Descriptors: fire
:::

Meteor swarm is a very powerful and spectacular spell that is similar to fireball in many aspects.
When you cast it, four 2-foot-diameter spheres spring from your outstretched hand and streak in
straight lines to the spots you select. The meteor spheres leave a fiery trail of sparks.

If you aim a sphere at a specific creature, you may make a ranged touch attack to strike the target
with the meteor. Any creature struck by a sphere takes 2d6 points of bludgeoning damage (no save)
and takes a -4 penalty on the saving throw against the sphere's fire damage (see below). If a
targeted sphere misses its target, it simply explodes at the nearest corner of the target's space.
You may aim more than one sphere at the same target.

Once a sphere reaches its destination, it explodes in a 40-foot-radius spread, dealing 6d6 points of
fire damage to each creature in the area. If a creature is within the area of more than one sphere,
it must save separately against each. Despite stemming from separate spheres, all of the fire damage
is added together after the saves have been made, and fire resistance is applied only once.
