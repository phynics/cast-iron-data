+++
id = "ref/arc-barbarian/drunken-brute"
kind = "archetype"
title = "Drunken Brute"
aon = "ArchetypeDisplay.aspx?FixedName=Barbarian%20Drunken%20Brute"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "drunken_brute", path = "json/archetypes_barbarian.json" },
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
  { anchor = "raging-drunk", level = 1 },
]
trades = [
  { replaces = "Fast movement", feature = "fast-movement", by = ["raging-drunk"] },
]
+++

Barbarians are known for their ability to consume potent drink, but drunken brutes turn drinking
into a combat tactic, using the potent liquor to fuel their rage and grant them additional powers. A
drunken brute has the following class feature.

## Raging Drunk (Ex) {#raging-drunk}

While raging, the drunken brute can drink a potion, or a tankard of ale or similar quantity of
alcohol, as a move action that does not provoke attacks of opportunity. A potion has its normal
effect, while an alcoholic drink allows the barbarian to maintain her rage that round without
expending a round of rage for the day (instead of the alcohol's normal effects). For each alcoholic
drink consumed while raging, the barbarian is [nauseated](ref/misc/nauseated) for 1 round when her
rage expires, in addition to the normal fatigue that follows a rage. Tireless rage does not negate
this nauseated condition but the internal fortitude rage power does. This ability replaces fast
movement.

## Rage Powers {#rage-powers}

The following rage powers complement the drunken brute archetype:
[boasting taunt](ref/ragepower/boasting-taunt),
[good for what ails you](ref/ragepower/good-for-what-ails-you),
[internal fortitude](ref/ragepower/internal-fortitude),
[liquid courage](ref/ragepower/liquid-courage),
[moment of clarity](ref/ragepower/moment-of-clarity), [roaring drunk](ref/ragepower/roaring-drunk),
and [staggering drunk](ref/ragepower/staggering-drunk).
