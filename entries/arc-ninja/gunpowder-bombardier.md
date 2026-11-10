+++
id = "ref/arc-ninja/gunpowder-bombardier"
kind = "archetype"
title = "Gunpowder Bombardier"
source_ids = ["heroes-from-the-fringe"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "gunpowder_bombardier", path = "json/archetypes_ninja.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/ninja" },
]
[[sources]]
publication = "heroes-from-the-fringe"
page = "30"

[fields]
kind = "archetype"
replaces = ["Ninja trick gained at 2nd level", "Uncanny dodge", "Improved uncanny dodge"]
alters = ["Ki pool"]
replaces_features = ["uncanny-dodge", "improved-uncanny-dodge"]
alters_features = ["ki-pool"]
+++

[Ratfolk](ref/race/ratfolk) assassins and other ninjas with an affinity for gunpowder demonstrate
masterful control of bombs, using the explosives to inflict major damage or impair their foes.

**Gunpowder Bomb (Ex)**

**Ability:** A gunpowder bombardier can expend 1 ki point to throw a gunpowder bomb at a
[grid intersection](ref/rule/throw-splash-weapon) as a ranged attack against AC 5 with a range of 20
feet. The gunpowder bomb deals 1d6 points of bludgeoning damage to all creatures in a 10-foot-radius
[burst](ref/misc/burst), which can be increased to 20 feet by spending 1 additional ki point. A
creature in the bomb's radius can attempt a Reflex save (DC = 10 + half the gunpowder bombardier's
ninja level + her Dexterity modifier) for half damage.

**Alters:** Ki pool

**Gained:** At 2nd Level

**Replaces:** Ninja trick gained at 2nd level

At 5th level: The damage 2d6.

At 7th level: The damage 3d6.

At 9th level: The damage 4d6.

At 11th level: The damage 5d6.

At 13th level: The damage 6d6.

At 15th level: The damage 7d6.

At 17th level: The damage 8d6.

At 19th level: The damage 9d6.

**Explosive Impairment (Su)**

**At 4th Level:** A gunpowder bombardier can imbue her _gunpowder bombs_ with impairing effects. By
spending 1 additional ki point when she throws a _gunpowder bomb,_ the gunpowder bombardier can
cause her bomb to inflict one of the following conditions, in addition to dealing its normal damage,
for a number of rounds equal to [half](ref/misc/fractions-and-rounding) her ninja level:
[dazzled](ref/misc/dazzled), [deafened](ref/misc/deafened), [entangled](ref/rule/entangled), or
[shaken](ref/misc/shaken).

**At 8th Level:** She adds [nauseated](ref/misc/nauseated) and [stunned](ref/misc/stunned) to the
list of conditions her bombs can inflict.

**Replaces:** Uncanny dodge

**Special:** A creature that succeeds at the Reflex save to halve the damage also negates the
condition inflicted by the _gunpowder bomb._

**Delayed Explosive (Ex)**

**Gained:** At 8th Level

**Replaces:** Improved uncanny dodge

**Special:** If the bomb is touched or moved by another creature, it detonates immediately. The
gunpowder bombardier can have only one delayed explosive active at a time; planting another
_gunpowder bomb_ renders the previous bomb inert.

**Standard:** A gunpowder bombardier can plant a _gunpowder bomb_ and delay its explosion. She can
place a _gunpowder bomb_ - adding effects as she would if she were throwing the _gunpowder bomb,_
and spending the requisite ki points - and specify a number of rounds after which the bomb will
detonate, up to a maximum number of rounds equal to the gunpowder bombardier's ninja level.
