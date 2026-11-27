+++
id = "ref/arc-barbarian/savage-technologist"
kind = "archetype"
title = "Savage Technologist"
aon = "ArchetypeDisplay.aspx?FixedName=Barbarian%20Savage%20Technologist"
source_ids = ["technology-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "savage_technologist", path = "json/archetypes_barbarian.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/barbarian" },
]
[[sources]]
publication = "technology-guide"
page = "13"

[fields]
kind = "archetype"
features = [
  { anchor = "rage", level = 1 },
  { anchor = "sword-and-gun", level = 2 },
  { anchor = "primal-magnetism", level = 3 },
  { anchor = "crack-shot", level = 5 },
]
trades = [
  { replaces = "Uncanny Dodge", feature = "uncanny-dodge", by = ["sword-and-gun"] },
  { replaces = "Improved Uncanny Dodge", feature = "improved-uncanny-dodge", by = ["crack-shot"] },
  { alters = "Rage", feature = "rage", by = ["rage"] },
]
+++

Savage technologists exhort Kellids to rise up against the depredations of the Technic League. But
rather than rejecting technology, they wield the League's own weapons against it. A savage
technologist has the following class features.

## Class Skills {#class-skills}

Acrobatics (Dex), Climb (Str), Craft (Int), Diplomacy (Cha), Intimidate (Cha), Knowledge (local)
(Int), Perception (Wis), Sense Motive (Wis), Perception (Wis), Ride (Dex), Survival (Wis), and Swim
(Str).

## Weapon and Armor Proficiency {#weapon-and-armor-proficiency}

A savage technologist is proficient with all simple and martial weapons, all firearms, light armor,
and shields (except tower shields).

## Rage (Ex) {#rage}

A savage technologist can enter rage as a barbarian, except she gains a morale bonus to Strength and
Dexterity instead of Strength and Constitution, and she does not take a penalty to Armor Class. She
retains the bonus on Will saving throws. When a barbarian ability would increase the savage
technologist's Strength while raging, it increases her Dexterity instead. This ability alters rage.

## Sword and Gun (Ex) {#sword-and-gun}

At 2nd level, when a raging savage technologist wields a one-handed firearm in one hand and a light
or one-handed melee weapon in the other, she can make ranged attacks with the firearm without
provoking attacks of opportunity. She also gains the benefits of the
[Two Weapon Fighting](ref/feat/two-weapon-fighting) feat, but only if all attacks are made with
those weapons. This ability replaces Uncanny Dodge.

## Primal Magnetism (Ex) {#primal-magnetism}

At 3rd level, a savage technologist adds her Strength modifier on Diplomacy checks when interacting
with tribal cultures. She can expend 2 rounds of rage (even if not raging) to add a bonus equal to
1/2 his barbarian level on a Diplomacy check.

## Crack Shot (Ex) {#crack-shot}

At 5th level, a savage technologist adds her Dexterity modifier to her damage rolls when making
ranged attacks with a firearm while raging. This ability replaces Improved Uncanny Dodge.
