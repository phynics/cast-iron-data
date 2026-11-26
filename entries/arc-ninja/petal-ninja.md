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
features = [
  { anchor = "blossom-shower", level = 2 },
  { anchor = "burst-of-blossoms", level = 4 },
  { anchor = "sundial", level = 6 },
]
trades = [
  { replaces = "Ninja trick gained at 2nd level", feature = "ninja-tricks", levels = [2], by = ["blossom-shower"] },
  { replaces = "No trace", feature = "no-trace", by = ["burst-of-blossoms"] },
  { replaces = "uncanny dodge", feature = "uncanny-dodge", by = ["burst-of-blossoms"] },
  { replaces = "improved uncanny dodge", feature = "improved-uncanny-dodge", by = ["burst-of-blossoms"] },
  { replaces = "Light steps", feature = "light-steps", by = ["sundial"] },
  { alters = "Class skills" },
]
+++

Petal ninjas are a secretive clan of [ghoran](ref/race/ghoran) infiltrators, in touch with their
plantlike nature to the point where they can change their forms, allowing them access into places
that were previously impossible to reach.

Petal ninja is an archetype available only to ghorans.

## Class Skills {#class-skills}

A petal ninja gains Heal as a class skill, but does not gain Appraise as a class skill.

This alters the ninja's class skills.

## Blossom Shower (Ex) {#blossom-shower}

At 2nd level, as a standard action, a petal ninja can spend 1 ki point to create a
[burst](ref/misc/burst) of flower petals in a 15-foot radius centered on a point within 20 feet. A
blossom shower lasts for a number of rounds equal to half the petal ninja's level (minimum 1 round).

When activating a blossom shower, the petal ninja forgoes a number of sneak attack dice to determine
the shower's effects, as noted below. These sneak attack dice are unavailable for the duration of
the blossom shower and are regained when the effect ends. If an effect requires a saving throw, the
DC is equal to 10 + twice the number of sneak attack dice expended + the petal ninja's Charisma
modifier. The petal ninja can choose to create a lesser effect even if she expends more dice than
required. For example, she can expend 4 sneak attack dice, but impart the effect of 3 sneak attack
dice. The shower does not affect the petal ninja herself, apart from the
[concealment](ref/rule/concealment) granted by using 1 sneak attack die.

_1 Sneak Attack Die:_ Creatures within the radius gain concealment (20% miss chance).

_2 Sneak Attack Dice:_ As 1 sneak attack die, except each creature in the radius must succeed at a
Will save or be [dazzled](ref/misc/dazzled) for 1d6 rounds.

_3 Sneak Attack Dice:_ As 2 sneak attack dice, except creatures are [sickened](ref/misc/sickened) on
a failed save.

_4 Sneak Attack Dice:_ As 2 sneak attack dice, except creatures are
[fascinated](ref/misc/fascinated) on a failed save.

_5 Sneak Attack Dice:_ As 2 sneak attack dice, except creatures are [staggered](ref/misc/staggered)
on a failed save.

_6 Sneak Attack Dice:_ As 2 sneak attack dice, except creatures are [nauseated](ref/misc/nauseated)
on a failed save.

This replaces the ninja trick gained at 2nd level.

## Burst of Blossoms (Su) {#burst-of-blossoms}

At 4th level, a petal ninja gains the ability to transform into a cloud of blossoms as a standard
action. By spending 1 point from her ki pool, a petal ninja can take the form of a cloud of
blossoms, becoming insubstantial for 1 round, as _[gaseous form](ref/spell/gaseous-form)_. While
insubstantial she also gains a +4 circumstance bonus on Stealth checks. At 8th level, the duration
increases to a number of rounds equal to 1 plus the petal ninja's Charisma modifier.

This replaces no trace, uncanny dodge, and improved uncanny dodge.

## Sundial (Su) {#sundial}

At 6th level, the petal ninja gains the ability to change the lighting in a 30-foot-radius
[emanation](ref/misc/emanation) centered on herself as a move action. For every ki point she spends,
the [light levels](ref/rule/vision-and-light) change by one step (from darkness to dim light, normal
light, and bright light, and vice versa). This change remains in effect for 1 minute.

This replaces light steps.
