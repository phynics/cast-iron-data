+++
id = "ref/arc-fighter/titan-fighter"
kind = "archetype"
title = "Titan Fighter"
aon = "ArchetypeDisplay.aspx?FixedName=Fighter%20Titan%20Fighter"
source_ids = ["giant-hunters-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "titan_fighter", path = "json/archetypes_fighter2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/fighter" },
]
[[sources]]
publication = "giant-hunters-handbook"
page = "21"

[fields]
kind = "archetype"
features = [
  { anchor = "giant-weapon-wielder", level = 1 },
  { anchor = "incredible-heft", level = 3 },
  { anchor = "unstoppable-momentum", level = 5 },
]
trades = [
  { replaces = "The fighter's 1st level bonus feat", feature = "bonus-feats", levels = [1], by = ["giant-weapon-wielder"] },
  { replaces = "Armor training", feature = "armor-training", by = ["incredible-heft"] },
  { replaces = "Weapon training", feature = "weapon-training", by = ["unstoppable-momentum"] },
]
+++

Titan fighters make use of enormous weapons others can barely lift. Titan fighters have the
following class features.

## Giant Weapon Wielder (Ex) {#giant-weapon-wielder}

At 1st level, a titan fighter can wield two-handed melee weapons intended for creatures one size
category larger than himself, treating them as two-handed weapons. He takes an additional -2 penalty
on attack rolls when using an oversized two-handed weapon. This ability replaces the fighter's 1st
level bonus feat.

## Incredible Heft (Ex) {#incredible-heft}

At 3rd level, a titan fighter becomes more skilled at wielding weapons intended for creatures one
size category larger than himself. The penalty on attack rolls for using such weapons is reduced by
1, including when using oversized two-handed weapons. At 7th level and every 4 levels thereafter,
this penalty is reduced by another 1 (minimum 0). This ability replaces armor training.

## Unstoppable Momentum (Ex) {#unstoppable-momentum}

At 5th level, a titan fighter gains a +1 bonus on combat maneuver checks and to CMD while wielding a
weapon sized for a creature of a larger size category. At 9th level and every 4 levels thereafter,
this bonus increases by 1. When wielding oversized weapons, the titan fighter can attempt to
[bull rush](ref/rule/bull-rush), [drag](ref/rule/drag), [overrun](ref/rule/overrun),
[reposition](ref/rule/reposition), and [trip](ref/rule/trip) creatures up to two sizes categories
larger than himself. This ability replaces weapon training.
