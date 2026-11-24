+++
id = "ref/arc-fighter/two-weapon-warrior"
kind = "archetype"
title = "Two-Weapon Warrior"
aon = "ArchetypeDisplay.aspx?FixedName=Fighter%20Two-Weapon%20Warrior"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "two_weapon_warrior", path = "json/archetypes_fighter2.json" },
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
  { anchor = "defensive-flurry", level = 3 },
  { anchor = "twin-blades", level = 5 },
  { anchor = "doublestrike", level = 9 },
  { anchor = "improved-balance", level = 11 },
  { anchor = "equal-opportunity", level = 13 },
  { anchor = "perfect-balance", level = 15 },
  { anchor = "deft-doublestrike", level = 17 },
  { anchor = "deadly-defense", level = 19 },
]
trades = [
  { replaces = "Armor training 1 and 2", feature = "armor-training", levels = [3, 7], by = ["defensive-flurry"] },
  { replaces = "Weapon training 1", feature = "weapon-training", levels = [5], by = ["twin-blades"] },
  { replaces = "Weapon training 2", feature = "weapon-training", levels = [9], by = ["doublestrike"] },
  { replaces = "Armor training 3", feature = "armor-training", levels = [11], by = ["improved-balance"] },
  { replaces = "Weapon training 3", feature = "weapon-training", levels = [13], by = ["equal-opportunity"] },
  { replaces = "Armor training 4", feature = "armor-training", levels = [15], by = ["perfect-balance"] },
  { replaces = "Weapon training 4", feature = "weapon-training", levels = [17], by = ["deft-doublestrike"] },
  { replaces = "Armor mastery", feature = "armor-mastery", by = ["deadly-defense"] },
]
+++

Trained under great masters who preached the simple truth that two are better than one when it comes
to weapons, the two-weapon warrior is a terror when his hands are full. From paired daggers to
exotic double weapons, all combinations come equally alive in his skilled hands.

## Defensive Flurry (Ex) {#defensive-flurry}

At 3rd level, when a two-weapon warrior makes a [full attack](ref/rule/full-attack) with both
weapons, he gains a +1 dodge bonus to AC against melee attacks until the beginning of his next turn.
This bonus increases by +1 every four levels after 3rd. This ability replaces armor training 1
and 2.

## Twin Blades (Ex) {#twin-blades}

At 5th level, a two-weapon warrior gains a +1 bonus on attack and damage rolls when making a full
attack with two weapons or a double weapon. This bonus increases by +1 for every four levels after
5th. This ability replaces weapon training 1.

## Doublestrike (Ex) {#doublestrike}

At 9th level, a two-weapon warrior may, as a standard action, make one attack with both his primary
and secondary weapons. The penalties for [attacking with two weapons](ref/rule/two-weapon-fighting)
apply normally. This ability replaces weapon training 2.

## Improved Balance (Ex) {#improved-balance}

At 11th level, the attack penalties for fighting with two weapons are reduced by -1 for a two-weapon
warrior. Alternatively, he may use a one-handed weapon in his off-hand, treating it as if it were a
light weapon with the normal light weapon penalties. This ability replaces armor training 3.

## Equal Opportunity (Ex) {#equal-opportunity}

At 13th level, when a two-weapon warrior makes an attack of opportunity, he may attack once with
both his primary and secondary weapons. The penalties for attacking with two weapons apply normally.
This ability replaces weapon training 3.

## Perfect Balance (Ex) {#perfect-balance}

At 15th level, the penalties for fighting with two weapons are reduced by an additional -1 for a
two-weapon warrior. This benefit stacks with improved balance. If he is using a one-handed weapon in
his off hand, treating it as a light weapon, he uses the normal light weapon penalties. This ability
replaces armor training 4.

## Deft Doublestrike (Ex) {#deft-doublestrike}

At 17th level, when a two-weapon warrior hits an opponent with both weapons, he can make a
[disarm](ref/rule/disarm) or [sunder](ref/rule/sunder) attempt (or [trip](ref/rule/trip), if one or
both weapons can be used to trip) against that opponent as an immediate action that does not provoke
attacks of opportunity. This ability replaces weapon training 4.

## Deadly Defense (Ex) {#deadly-defense}

At 19th level, when a two-weapon warrior makes a full attack with both weapons, every creature that
hits him with a melee attack before the beginning of his next turn provokes an attack of opportunity
from the warrior. This ability replaces armor mastery.
