+++
id = "ref/misc/spread"
kind = "rule"
title = "Spread"
source_ids = ["core-rulebook", "pathfinder-91-battle-of-bloodmarch-hills"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "spread", path = "json/misc.json" },
]

[fields]
kind = "none"
+++

### Burst, Emanation, Spread

**Sources:** PRPG Core Rulebook pg 214\
Most spells that affect an area function as a burst, an emanation, or a spread. In each case, you
select the spell's point of origin (this is always a grid intersection) and measure its effect from
that point.

A **burst** spell affects whatever it catches in its area, including creatures that you can't see.
It can't affect creatures with total [cover](ref/rule/cover) from its point of origin (in other
words, its effects don't extend around corners). The default shape for a burst effect is a sphere,
but some burst spells are specifically described as cone-shaped. A burst's area defines how far from
the point of origin the spell's effect extends.

An **emanation** spell functions like a burst spell, except that the effect continues to radiate
from the point of origin for the duration of the spell. Most emanations are cones or spheres.

A **spread** spell, often a cloud or fog spell, extends out like an emanation but can turn corners.
You select a grid intersection, and the spell spreads out a given distance in all directions. The
effect can extend around corners and into areas that you can't see. Figure distance by actual
distance traveled, taking into account turns the spell effect takes. When determining distance for
spread effects, count around walls, not through them. As with movement, do not trace diagonals
across corners. You must designate the point of origin for such an effect, but you need not have
[line of effect](ref/rule/aiming-a-spell) to all portions of the effect.

### Larger Creatures

**Sources:** Pathfinder \#91: Battle of Bloodmarch Hills pg 72\
The rules for many character options in the Pathfinder RPG Core Rulebook and other Pathfinder RPG
products often assume that creatures are Medium or Small. In the case of a handful of spells with
areas that feature a "radius emanation centered on you" such as
[antimagic field](ref/spell/antimagic-field), [aura of doom](ref/spell/aura-of-doom), and
[zone of silence](ref/spell/zone-of-silence), this can result in an area that is effectively useless
when coming from a Large or larger caster. As an optional rule, when a creature casts an emanation
or burst spell with the text "centered on you," treat the creature's entire space as the spell's
point of origin, and measure the spell's area or effect from the edge of the creature's space. For
instance, an _[antimagic field](ref/spell/antimagic-field)_ cast by a fire giant would extend 10
feet beyond his space (effectively increasing the emanation's radius by 5 feet).
