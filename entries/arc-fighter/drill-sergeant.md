+++
id = "ref/arc-fighter/drill-sergeant"
kind = "archetype"
title = "Drill Sergeant"
aon = "ArchetypeDisplay.aspx?FixedName=Fighter%20Drill%20Sergeant"
source_ids = ["melee-tactics-toolbox"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "drill_sergeant", path = "json/archetypes_fighter.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/fighter" },
]
[[sources]]
publication = "melee-tactics-toolbox"
page = "11"

[fields]
kind = "archetype"
features = [
  { anchor = "tactician", level = 2 },
  { anchor = "weapon-training", level = 5 },
  { anchor = "greater-tactician", level = 9 },
  { anchor = "weapon-trainer", level = 13 },
  { anchor = "master-tactician", level = 17 },
]
trades = [
  { replaces = "Bravery", feature = "bravery", by = ["tactician"] },
  { replaces = "Weapon training 2", feature = "weapon-training", levels = [9], by = ["greater-tactician"] },
  { replaces = "Weapon training 3", feature = "weapon-training", levels = [13], by = ["weapon-trainer"] },
  { replaces = "Weapon training 4", feature = "weapon-training", levels = [17], by = ["master-tactician"] },
  { alters = "Weapon training 1", feature = "weapon-training", levels = [5], by = ["weapon-training"] },
]
+++

Drill sergeants excel at training other combatants in fighting techniques.

## Tactician (Ex) {#tactician}

At 2nd level, a drill sergeant gains the [cavalier's](ref/class/cavalier) tactician class feature,
treating his fighter level as his cavalier level for the purposes of this ability. This ability
replaces bravery.

## Weapon Training (Ex) {#weapon-training}

At 5th level, a drill sergeant gains weapon training with one
[group of weapons](ref/ability/weapon-groups). He doesn't gain weapon training with other groups at
later levels, though his weapon training bonus improves by 1 for every 4 levels after 5th level.
This ability modifies weapon training 1.

## Greater Tactician (Ex) {#greater-tactician}

At 9th level, the drill sergeant gains the cavalier's greater tactician class feature. This ability
replaces weapon training 2.

## Weapon Trainer (Ex) {#weapon-trainer}

At 13th level, when a drill sergeant wields a weapon he has weapon training in, all allies within 30
feet who can see and hear the drill sergeant gain [half](ref/misc/fractions-and-rounding) his weapon
training bonus when they wield any weapon from the same weapon group.

This bonus doesn't stack with any weapon training bonus an ally already possesses.

This ability replaces weapon training 3.

## Master Tactician (Ex) {#master-tactician}

At 17th level, the drill sergeant gains the cavalier's master tactician class feature.

This ability replaces weapon training 4.
