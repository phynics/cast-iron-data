+++
id = "ref/arc-barbarian/breaker"
kind = "archetype"
title = "Breaker"
aon = "ArchetypeDisplay.aspx?FixedName=Barbarian%20Breaker"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "breaker", path = "json/archetypes_barbarian.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/barbarian" },
]
[[sources]]
publication = "advanced-players-guide"
page = "78"

[fields]
kind = "archetype"
features = [
  { anchor = "destructive", level = 1 },
  { anchor = "battle-scavenger", level = 3 },
]
trades = [
  { replaces = "Fast movement", feature = "fast-movement", by = ["destructive"] },
  { replaces = "Trap sense", feature = "trap-sense", by = ["battle-scavenger"] },
]
+++

While most barbarians are skilled at breaking things, some find the need to destroy their
surroundings an almost uncontrollable urge when in the middle of a _rage._ These barbarians are a
danger not only to their foes, but also to the very environment around them. A breaker barbarian has
the following class features.

## Destructive (Ex) {#destructive}

Whenever the breaker barbarian makes a melee attack that targets an unattended object or makes a
[sunder](ref/rule/sunder) combat maneuver, she adds [half](ref/misc/fractions-and-rounding) her
barbarian level (minimum +1) on the damage roll. This ability replaces fast movement.

## Battle Scavenger (Ex) {#battle-scavenger}

At 3rd level, the breaker barbarian suffers no penalty on attack rolls when using an
[improvised weapon](ref/misc/improvised-weapons) or a weapon with the [broken](ref/misc/broken)
condition. In addition, she gains a +1 bonus on damage rolls with improvised or broken weapons for
every three levels beyond 3rd. This ability replaces trap sense.

## Rage Powers {#rage-powers}

The following rage powers complement the breaker archetype:
[ground breaker](ref/ragepower/ground-breaker), [smasher](ref/ragepower/smasher), and
[strength surge](ref/ragepower/strength-surge).
