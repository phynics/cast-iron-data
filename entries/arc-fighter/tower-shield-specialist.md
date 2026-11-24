+++
id = "ref/arc-fighter/tower-shield-specialist"
kind = "archetype"
title = "Tower Shield Specialist"
aon = "ArchetypeDisplay.aspx?FixedName=Fighter%20Tower%20Shield%20Specialist"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "tower_shield_specialist", path = "json/archetypes_fighter2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/fighter" },
]
[[sources]]
publication = "ultimate-combat"
page = "48"

[fields]
kind = "archetype"
features = [
  { anchor = "burst-barrier", level = 2 },
  { anchor = "tower-shield-training", level = 3 },
  { anchor = "tower-shield-specialist", level = 5 },
  { anchor = "tower-shield-defense", level = 9 },
  { anchor = "immediate-repositioning", level = 13 },
  { anchor = "tower-shield-evasion", level = 16 },
]
trades = [
  { replaces = "Bravery", feature = "bravery", by = ["burst-barrier"] },
  { replaces = "Weapon training 1", feature = "weapon-training", levels = [5], by = ["tower-shield-specialist"] },
  { replaces = "Weapon training 2", feature = "weapon-training", levels = [9], by = ["tower-shield-defense"] },
  { replaces = "Weapon training 3", feature = "weapon-training", levels = [13], by = ["immediate-repositioning"] },
  { replaces = "Weapon training 4", feature = "weapon-training", levels = [17], by = ["tower-shield-evasion"] },
  { replaces = "weapon mastery", feature = "weapon-mastery", by = ["tower-shield-evasion"] },
]
+++

Many fighters believe the [tower shield](ref/eq-armor/tower-shield) is a tool suitable only for
troops on the battlefield, claiming it is too large and bulky to use in skirmishes or within dungeon
corridors. Tower shield specialists defy those notions, using their massive shields with startling
skill and incredible effect. They use these seemingly clumsy shields to perform deft maneuvers that
confound their enemies.

## Burst Barrier (Ex) {#burst-barrier}

At 2nd level, a tower shield specialist can use his shield to screen himself from burst spells and
effects, gaining a +1 bonus on Reflex saves against them while employing a tower shield. This bonus
increases by +1 for every four levels after 2nd (to a maximum of +5 at 18th level). This ability
replaces bravery.

## Tower Shield Training (Ex) {#tower-shield-training}

At 3rd level, a tower shield specialist gains armor training as normal, but while he employs a tower
shield, the armor penalty is reduced by 3 and the maximum Dexterity bonus allowed by his armor
increases by 2. The benefit increases every four levels thereafter as per standard armor training;
if the tower shield specialist is not employing a tower shield, the benefits to armor training
revert to the normal bonuses.

## Tower Shield Specialist (Ex) {#tower-shield-specialist}

At 5th level, when a tower shield specialist employs a tower shield in combat, he does not take the
-2 penalty on attack rolls because of the shield's encumbrance. This ability replaces weapon
training 1.

## Tower Shield Defense (Ex) {#tower-shield-defense}

At 9th level, while using a tower shield, a tower shield specialist gains his shield bonus against
touch attacks. This ability replaces weapon training 2.

## Immediate Repositioning (Ex) {#immediate-repositioning}

At 13th level, as an immediate action, a tower shield specialist can reposition his tower shield to
another facing, but he cannot use this ability to interrupt an attack. This ability replaces weapon
training 3.

## Tower Shield Evasion (Ex) {#tower-shield-evasion}

At 16th level, while using a tower shield, the tower shield specialist gains
[evasion](ref/ability/evasion), as the [rogue](ref/class/rogue) class ability. At 20th level, the
shield specialist gains [improved evasion](ref/talent/improved-evasion), as the rogue advanced
talent, while using a tower shield. This ability replaces both weapon training 4 and weapon mastery.
