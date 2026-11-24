+++
id = "ref/arc-fighter/weapon-master"
kind = "archetype"
title = "Weapon Master"
aon = "ArchetypeDisplay.aspx?FixedName=Fighter%20Weapon%20Master"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "weapon_master", path = "json/archetypes_fighter2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/fighter" },
]
[[sources]]
publication = "advanced-players-guide"
page = "109"

[fields]
kind = "archetype"
features = [
  { anchor = "weapon-guard", level = 2 },
  { anchor = "weapon-training", level = 3 },
  { anchor = "reliable-strike", level = 5 },
  { anchor = "mirror-move", level = 9 },
  { anchor = "deadly-critical", level = 13 },
  { anchor = "critical-specialist", level = 17 },
  { anchor = "unstoppable-strike", level = 19 },
]
trades = [
  { replaces = "Bravery", feature = "bravery", by = ["weapon-guard"] },
  { replaces = "Armor training 1, 2, 3, and 4", feature = "armor-training", levels = [3, 7, 11, 15], by = ["weapon-training"] },
  { replaces = "Weapon training 1", feature = "weapon-training", levels = [5], by = ["reliable-strike"] },
  { replaces = "Weapon training 2", feature = "weapon-training", levels = [9], by = ["mirror-move"] },
  { replaces = "Weapon training 3", feature = "weapon-training", levels = [13], by = ["deadly-critical"] },
  { replaces = "Weapon training 4", feature = "weapon-training", levels = [17], by = ["critical-specialist"] },
  { replaces = "Armor mastery", feature = "armor-mastery", by = ["unstoppable-strike"] },
]
+++

Devoted to the perfection of a single weapon, the weapon master's meditations upon his favored
weapon border on the obsessive, but none can deny his consummate skill. The weapon master must
select a single type of weapon (such as longsword or shortbow). All of his abilities apply to that
weapon type.

## Weapon Guard (Ex) {#weapon-guard}

At 2nd level, a weapon master gains a +1 bonus to CMD against [disarm](ref/rule/disarm) and
[sunder](ref/rule/sunder) attempts while wielding his chosen weapon. This bonus also applies on
saves against any effect that targets his chosen weapon (for example, _[grease](ref/spell/grease),
[heat metal](ref/spell/heat-metal), [shatter](ref/spell/shatter),
[warp wood](ref/spell/warp-wood)_). The bonus increases by +1 for every four levels beyond 2nd. This
ability replaces bravery.

## Weapon Training (Ex) {#weapon-training}

At 3rd level, a weapon master gains a +1 bonus on attack and damage rolls with his chosen weapon.
The bonus improves by +1 for every four levels beyond 3rd. This ability replaces armor training 1,
2, 3, and 4.

## Reliable Strike (Ex) {#reliable-strike}

At 5th level, a weapon master may reroll an attack roll, critical hit confirmation roll, miss chance
check, or damage roll as an immediate action. He must accept the second roll even if it is worse. He
can use this ability once per day at 5th level, plus one additional time per day for every five
levels beyond 5th. This ability replaces weapon training 1.

## Mirror Move (Ex) {#mirror-move}

At 9th level, a weapon master gains his weapon training bonus as an insight bonus to AC when
attacked by his chosen weapon. This ability replaces weapon training 2.

## Deadly Critical (Ex) {#deadly-critical}

At 13th level, when a weapon master confirms a critical hit with his chosen weapon, he can increase
the weapon's damage multiplier by +1 as an immediate action. He can use this ability once per day at
13th level, plus one additional time per day for every three levels above 13th. This ability
replaces weapon training 3.

## Critical Specialist (Ex) {#critical-specialist}

At 17th level, the save DCs of any effects caused by a critical hit with a weapon master's chosen
weapon increase by +4. This ability replaces weapon training 4.

## Unstoppable Strike (Ex) {#unstoppable-strike}

At 19th level, a weapon master can take a standard action to make one attack with his chosen weapon
as a touch attack that ignores [damage reduction](ref/rule/damage-reduction) (or
[hardness](ref/umr/hardness), if attacking an object). This ability replaces armor mastery.
