+++
id = "ref/arc-fighter/airborne-ambusher"
kind = "archetype"
title = "Airborne Ambusher"
aon = "ArchetypeDisplay.aspx?FixedName=Fighter%20Airborne%20Ambusher"
source_ids = ["advanced-race-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "airborne_ambusher", path = "json/archetypes_fighter.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/fighter" },
]
[[sources]]
publication = "advanced-race-guide"
page = "201"

[fields]
kind = "archetype"
features = [
  { anchor = "class-skills" },
  { anchor = "combat-flyer", level = 2 },
  { anchor = "aerobatics", level = 5 },
  { anchor = "flying-dodger", level = 9 },
  { anchor = "plummeting-charge", level = 13 },
]
trades = [
  { replaces = "Bravery", feature = "bravery", by = ["combat-flyer"] },
  { replaces = "Weapon training 1", feature = "weapon-training", levels = [5], by = ["aerobatics"] },
  { replaces = "Weapon training 2", feature = "weapon-training", levels = [9], by = ["flying-dodger"] },
  { replaces = "Weapon training 3 and 4", feature = "weapon-training", levels = [13, 17], by = ["plummeting-charge"] },
]
+++

Driven by suspicion and hatred, [strix](ref/race/strix) doggedly guard their territories, making
deadly use of their flight. Using swift strikes from above, strix plummet onto their foes with
lethal force.

## Weapon and Armor Proficiency {#weapon-and-armor-proficiency}

An airborne ambusher is not proficient with heavy armor or tower shields.

## Class Skills {#class-skills}

An airborne ambusher adds Fly to his list of class skills and removes Climb from his list of class
skills.

## Combat Flyer (Ex) {#combat-flyer}

At 2nd level, an airborne ambusher may use his fighter bonus feats to select
[Flyby Attack](ref/feat/flyby-attack) and [Hover](ref/feat/hover). This replaces bravery.

## Aerobatics (Ex) {#aerobatics}

At 5th level, an airborne ambusher may make a Fly check instead of an Acrobatics check to move
through a threatened area or an enemy's space. This replaces weapon training 1.

## Flying Dodger (Ex) {#flying-dodger}

At 9th level, when an airborne ambusher flies at least half its fly speed on its turn, it gains a +1
dodge bonus to AC for 1 round. This bonus increases to +2 at 11th level and +4 at 17th level. This
ability replaces weapon training 2.

## Plummeting Charge (Ex) {#plummeting-charge}

At 13th level, if an airborne ambusher flies at least half its fly speed as part of a
[charge](ref/rule/charge), it gains a +2 racial bonus on the attack roll (in addition to the normal
charge bonus) and a +4 bonus on its critical confirmation roll. These bonuses improve to +4 and +6
at 17th level. This replaces weapon training 3 and 4.
