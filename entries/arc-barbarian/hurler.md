+++
id = "ref/arc-barbarian/hurler"
kind = "archetype"
title = "Hurler"
aon = "ArchetypeDisplay.aspx?FixedName=Barbarian%20Hurler"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "hurler", path = "json/archetypes_barbarian.json" },
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
  { anchor = "skilled-thrower", level = 1 },
]
trades = [
  { replaces = "Fast movement", feature = "fast-movement", by = ["skilled-thrower"] },
]
+++

A raging barbarian is frightening enough in melee, but some become skilled at throwing objects at
their foes before closing in for the kill. A hurler has the following class feature.

## Skilled Thrower (Ex) {#skilled-thrower}

The hurler is skilled at throwing objects in combat. Increase the range increment of any thrown
weapon or object by 10 feet. This ability replaces fast movement.

## Rage Powers {#rage-powers}

The following rage powers complement the hurler archetype: [hurling](ref/ragepower/hurling),
[greater hurling](ref/ragepower/greater-hurling), [hurling charge](ref/ragepower/hurling-charge),
[lesser hurling](ref/ragepower/lesser-hurling), [strength surge](ref/ragepower/strength-surge), and
[surprise accuracy](ref/ragepower/surprise-accuracy).
