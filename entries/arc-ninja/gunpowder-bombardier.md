+++
id = "ref/arc-ninja/gunpowder-bombardier"
kind = "archetype"
title = "Gunpowder Bombardier"
aon = "ArchetypeDisplay.aspx?FixedName=Ninja%20Gunpowder%20Bombardier"
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
features = [
  { anchor = "gunpowder-bomb", level = 2 },
  { anchor = "explosive-impairment", level = 4 },
  { anchor = "delayed-explosive", level = 8 },
]
trades = [
  { replaces = "Ninja trick gained at 2nd level", feature = "ninja-tricks", levels = [2], by = ["gunpowder-bomb"] },
  { replaces = "Uncanny dodge", feature = "uncanny-dodge", by = ["explosive-impairment"] },
  { replaces = "Improved uncanny dodge", feature = "improved-uncanny-dodge", by = ["delayed-explosive"] },
  { alters = "Ki pool", feature = "ki-pool", by = ["gunpowder-bomb"] },
]
+++

[Ratfolk](ref/race/ratfolk) assassins and other ninjas with an affinity for gunpowder demonstrate
masterful control of bombs, using the explosives to inflict major damage or impair their foes.

## Gunpowder Bomb (Ex) {#gunpowder-bomb}

At 2nd level, a gunpowder bombardier can expend 1 ki point to throw a gunpowder bomb at a
[grid intersection](ref/rule/throw-splash-weapon) as a ranged attack against AC 5 with a range of 20
feet. The gunpowder bomb deals 1d6 points of bludgeoning damage to all creatures in a 10-foot-radius
[burst](ref/misc/burst), which can be increased to 20 feet by spending 1 additional ki point. A
creature in the bomb's radius can attempt a Reflex save (DC = 10 + half the gunpowder bombardier's
ninja level + her Dexterity modifier) for half damage. At 5th level and every 2 levels thereafter,
the bomb's damage increases by 1d6, to a maximum of 9d6 points of bludgeoning damage at 19th level.

This alters ki pool and replaces the ninja trick gained at 2nd level.

## Explosive Impairment (Su) {#explosive-impairment}

At 4th level, a gunpowder bombardier can imbue her gunpowder bombs with impairing effects. By
spending 1 additional ki point when she throws a gunpowder bomb, the gunpowder bombardier can cause
her bomb to inflict one of the following conditions, in addition to dealing its normal damage, for a
number of rounds equal to [half](ref/misc/fractions-and-rounding) her ninja level:
[dazzled](ref/misc/dazzled), [deafened](ref/misc/deafened), [entangled](ref/rule/entangled), or
[shaken](ref/misc/shaken). At 8th level, she adds [nauseated](ref/misc/nauseated) and
[stunned](ref/misc/stunned) to the list of conditions her bombs can inflict. A creature that
succeeds at the Reflex save to halve the damage also negates the condition inflicted by the
gunpowder bomb.

This replaces uncanny dodge.

## Delayed Explosive (Ex) {#delayed-explosive}

At 8th level, a gunpowder bombardier can plant a gunpowder bomb and delay its explosion. As a
standard action, the gunpowder bombardier can place a gunpowder bomb—adding effects as she would if
she were throwing the gunpowder bomb, and spending the requisite ki points—and specify a number of
rounds after which the bomb will detonate, up to a maximum number of rounds equal to the gunpowder
bombardier's ninja level. If the bomb is touched or moved by another creature, it detonates
immediately. The gunpowder bombardier can have only one delayed explosive active at a time; planting
another gunpowder bomb renders the previous bomb inert.

This replaces improved uncanny dodge.
