+++
id = "ref/arc-fighter/cavern-sniper"
kind = "archetype"
title = "Cavern Sniper"
aon = "ArchetypeDisplay.aspx?FixedName=Fighter%20Cavern%20Sniper"
source_ids = ["advanced-race-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "cavern_sniper", path = "json/archetypes_fighter.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/fighter" },
]
[[sources]]
publication = "advanced-race-guide"
page = "104"

[fields]
kind = "archetype"
features = [
  { anchor = "class-skills" },
  { anchor = "imbued-shot", level = 1 },
  { anchor = "silent-shooter", level = 2 },
  { anchor = "quick-and-deadly", level = 4 },
  { anchor = "sniper-training", level = 5 },
  { anchor = "greater-imbued-shot", level = 9 },
  { anchor = "weapon-mastery", level = 20 },
]
trades = [
  { replaces = "The 1st-level fighter bonus feat", feature = "bonus-feats", levels = [1], by = ["imbued-shot"] },
  { replaces = "Bravery", feature = "bravery", by = ["silent-shooter"] },
  { replaces = "The 4th-level fighter bonus feat", feature = "bonus-feats", levels = [4], by = ["quick-and-deadly"] },
  { replaces = "Weapon training 1, 3, and 4", feature = "weapon-training", levels = [5, 13, 17], by = ["sniper-training"] },
  { replaces = "Weapon training 2", feature = "weapon-training", levels = [9], by = ["greater-imbued-shot"] },
  { alters = "Weapon mastery", feature = "weapon-mastery", by = ["weapon-mastery"] },
]
+++

Perfectly at home in the darkness, the cavern sniper capitalizes on stealth and ranged attacks
imbued with his [spell-like abilities](ref/umr/spell-like-abilities) to harass his opponents. The
cavern sniper focuses on surprise, his innate magical abilities, and poison to take down unwary
foes. The cavern sniper has the following class features.

## Class Skills {#class-skills}

The cavern sniper adds Stealth to his list of class skills and removes Intimidate from his list of
class skills.

## Imbued Shot (Su) {#imbued-shot}

At 1st level, the cavern sniper gains the ability to imbue his arrows or bolts with the effect of
one of his drow _[faerie fire](ref/spell/faerie-fire)_, _[darkness](ref/spell/darkness)_, or
_[deeper darkness](ref/spell/deeper-darkness)_ [spell-like abilities](ref/umr/spell-like-abilities)
(provided he has access to the ability) as a swift action. When such an arrow or bolt is fired, the
spell's area is centered where the arrow or bolt lands. If the target of the attack has a space
larger than 5 feet, the cavern sniper can choose which square of the creature's space is the center
of the [spell-like ability](ref/umr/spell-like-abilities)'s effect, as long as that square is within
line of sight of the cavern sniper. The cavern sniper can instead choose to target a single square
within line of sight with an imbued arrow or bolt, and uses that square as the center of the
spell-like ability's area of effect on a hit (AC 5). The arrow must be fired during the round it was
imbued, or the spell-like ability is wasted. If the arrow or bolt misses, the use of the spell-like
ability is wasted. This ability replaces the 1st-level fighter bonus feat.

## Silent Shooter (Ex) {#silent-shooter}

At 2nd level, a cavern sniper gains a +2 bonus on Stealth checks made when loading a bow or
crossbow, poisoning ammunition, and making sniping attempts. This bonus increases by +2 for every
four levels beyond 2nd. This ability replaces bravery.

## Quick and Deadly (Ex) {#quick-and-deadly}

At 4th level, the cavern sniper can move at full speed while using Stealth at no penalty and can
apply poison to a single arrow or crossbow bolt as a swift action. This ability replaces the
4th-level fighter bonus feat.

## Sniper Training (Ex) {#sniper-training}

At 5th level, the cavern sniper chooses the bow or crossbow
[weapon group](ref/ability/weapon-groups) and gains a +2 bonus on attack rolls and damage rolls.
This bonus increases by +1 for every four levels beyond 5th. This ability replaces weapon training
1, 3, and 4.

## Greater Imbued Shot (Su) {#greater-imbued-shot}

At 9th level, the cavern sniper gains two extra uses of both his
_[faerie fire](ref/spell/faerie-fire)_ and _[darkness](ref/spell/darkness)_
[spell-like abilities](ref/umr/spell-like-abilities), but can only use these extra uses to imbue
arrows and bolts with the imbued shot class feature. This ability replaces weapon training 2.

## Weapon Mastery (Ex) {#weapon-mastery}

At 20th level, when the cavern sniper gains weapon mastery, he must choose a weapon in either the
bow or crossbow weapon group.
