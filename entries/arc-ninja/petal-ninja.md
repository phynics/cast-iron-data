+++
id = "ref/arc-ninja/petal-ninja"
kind = "archetype"
title = "Petal Ninja"
aon = "ArchetypeDisplay.aspx?FixedName=Ninja%20Petal%20Ninja"
source_ids = ["wilderness-origins"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "petal_ninja", path = "json/archetypes_ninja.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/ninja" },
]
[[sources]]
publication = "wilderness-origins"
page = "13"

[fields]
kind = "archetype"
replaces = ["Ninja trick gained at 2nd level", "No trace", "uncanny dodge", "improved uncanny dodge", "Light steps"]
+++

Petal ninjas are a secretive clan of [ghoran](ref/race/ghoran) infiltrators, in touch with their
plant-like nature to the point where they can change their forms, allowing them access into places
that were previously impossible to reach.

**Prerequisites:** Ghoran

**Gained class skills:** heal

**Lost class skills:** app

**Blossom Shower (Ex)**

**Action:** Ability

**Gained:** At 2nd Level

**Replaces:** Ninja trick gained at 2nd level

**Standard:** A petal ninja can spend 1 ki point to create a [burst](ref/misc/burst) of flower
petals in a 15-foot radius centered on a point within 20 feet. A blossom shower lasts for a number
of rounds equal to half the petal ninja's level (minimum 1 round).

When activating a blossom shower, the petal ninja forgoes a number of sneak attack dice to determine
the shower's effects, as noted below. These sneak attack dice are unavailable for the duration of
the blossom shower and are regained when the effect ends. If an effect requires a saving throw, the
DC is equal to 10 + twice the number of sneak attack dice expended + the petal ninja's Charisma
modifier. The petal ninja can choose to create a lesser effect even if she expends more dice than
required. For example, she can expend 4 sneak attack dice, but impart the effect of 3 sneak attack
dice. The shower does not affect the petal ninja herself, apart from the concealment granted by
using 1 sneak attack die.

|Sneak Attack Dice|Effect|
| --- | --- |
|1|Creatures within the radius gain [concealment](ref/rule/concealment) (20% miss chance).|
|2|As 1 sneak attack die, except each creature in the radius must succeed at a Will save or be [dazzled](ref/misc/dazzled) for 1d6 rounds.|
|3|As 2 sneak attack dice, except creatures are [sickened](ref/misc/sickened) on a failed save.|
|4|As 2 sneak attack dice, except creatures are [fascinated](ref/misc/fascinated) on a failed save.|
|5|As 2 sneak attack dice, except creatures are [staggered](ref/misc/staggered) on a failed save.|
|6|As 2 sneak attack dice, except creatures are [nauseated](ref/misc/nauseated) on a failed save.|

**Burst of Blossoms (Su)**

**Flavor:** A petal ninja gains the ability to transform into a cloud of blossoms.

**At 8th Level:** The duration increases to a number of rounds equal to 1 plus the petal ninja's
Charisma modifier.

**Gained:** At 4th Level

**Replaces:** No trace, uncanny dodge, improved uncanny dodge

**Standard:** By spending 1 point from her ki pool, a petal ninja can take the form of a cloud of
blossoms, becoming insubstantial for 1 round, as [gaseous form](ref/spell/gaseous-form). While
insubstantial she also gains a +4 circumstance bonus on Stealth checks.

**Sundial (Su)**

**Gained:** At 6th Level

**Move:** The petal ninja can change the lighting in a 30-foot-radius
[emanation](ref/misc/emanation) centered on herself. For every ki point she spends, the
[light levels](ref/rule/vision-and-light) change by one step (from darkness to dim light, normal
light, and bright light, and vice versa). This change remains in effect for 1 minute.

**Replaces:** Light steps
