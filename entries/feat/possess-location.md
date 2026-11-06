+++
id = "ref/feat/possess-location"
kind = "feat"
title = "Possess Location"
source_ids = ["pathfinder-28-the-infernal-syndrome"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "possess_location", path = "json/feat12.json" },
]

[fields]
kind = "feat"
feat_types = ["Monster"]
prerequisites = "Cha 16, any evil outsider with 8 or more Hit Dice."
+++

## Possess Location (Monster)

**Sources:** Pathfinder \#28: The Infernal Syndrome pg 57

A fiend learns to disperse its essence over an area, gaining mastery over features and structures
there and tainting the place with its wickedness.\
**Prerequisites:** Cha 16, any evil outsider with 8 or more Hit Dice.

Once per day, as a full-round action, a fiend may attempt to possess a structure or small area (like
a pool, grove, or ruin) of a diameter equal to 10 feet per Hit Die. This area is spherical, so a
fiend possessing a particularly large structure might only have power over a certain number of
rooms. An area receives no save against fiendish possession unless creatures or magical items occupy
the space, in which case the area makes a Will save equal to 10 + half the fiend's Hit Dice + the
fiend's Charisma modifier using the stats of the occupant with the highest Will save. An area within
the effects of a [hallow](ref/spell/hallow) spell cannot be possessed. A fiend possessing an area
operates similarly to one using the [Possess Creature](ref/feat/possess-creature) feat, but can only
be spent on location [possession actions](ref/rule/possession-actions).

Should a possessed location be destroyed, the fiend is ejected, retakes its original form in a space
adjacent to the area it previously possessed, and is [stunned](ref/misc/stunned) for 1 round.
[Dispel evil](ref/spell/dispel-evil) (or [dispel chaos](ref/spell/dispel-chaos) or
[dispel law](ref/spell/dispel-law), depending on the fiend) can eject a fiend, but the caster must
succeed at a caster level check with a DC equal to 10 + the HD of the possessing fiend + the fiend's
Cha modifier. [Banishment](ref/spell/banishment) and [dismissal](ref/spell/dismissal) immediately
eject a fiend from an object if it fails to make its saving throw against the spell's effects.
