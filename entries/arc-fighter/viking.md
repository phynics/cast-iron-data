+++
id = "ref/arc-fighter/viking"
kind = "archetype"
title = "Viking"
aon = "ArchetypeDisplay.aspx?FixedName=Fighter%20Viking"
source_ids = ["ultimate-wilderness", "people-of-the-north"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "viking", path = "json/archetypes_fighter2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/fighter" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "51"
[[sources]]
publication = "people-of-the-north"
page = "24"

[fields]
kind = "archetype"
features = [
  { anchor = "fearsome", level = 2 },
  { anchor = "shield-defense", level = 3 },
  { anchor = "berserker", level = 5 },
  { anchor = "rage-powers", level = 6 },
]
trades = [
  { replaces = "Bravery", feature = "bravery", by = ["fearsome"] },
  { replaces = "Armor training", feature = "armor-training", by = ["shield-defense"] },
  { replaces = "Weapon training", feature = "weapon-training", by = ["berserker"] },
  { alters = "Weapon and armor proficiencies", feature = "weapon-and-armor-proficiencies" },
  { alters = "The fighter's bonus feats", feature = "bonus-feats", by = ["rage-powers"] },
]
+++

Vikings seek to raid "softer societies" and return with their longships filled with plunder. A
viking strikes fear into the heart of her foes, and in battle she can fly into a terrible rage. Many
vikings wear the pelts of bears or wolves, drawing on the strength and ferocity of these beasts in
battle. Vikings do not wear heavy armor, but they are skilled at fighting with an axe or spear in
conjunction with a shield.

## Weapon and Armor Proficiency {#weapon-and-armor-proficiency}

A viking is not proficient with heavy armor or tower shields.

This alters the fighter's weapon and armor proficiencies.

## Fearsome (Ex) {#fearsome}

At 2nd level, a viking can attempt an Intimidate check to demoralize an opponent as a move action.
At 10th level, she can do so as a swift action. At 18th level, she can attempt to demoralize a foe
as a free action once per round.

This replaces bravery.

## Shield Defense (Ex) {#shield-defense}

At 3rd level, a viking learns the art of fighting with a shield. Whenever she is wearing medium,
light, or no armor and using a shield, the viking's shield bonus to AC increases by 1. At 7th, 11th,
and 15th levels, this bonus increases by 1.

This replaces armor training.

## Berserker (Ex) {#berserker}

At 5th level, a viking gains the rage ability as per the [barbarian](ref/class/barbarian) class
feature, and she uses her fighter level as her barbarian level for the purposes of determining her
rounds of rage, qualifying for rage powers, and determining the effects of rage powers.

This replaces weapon training.

## Rage Powers (Ex) {#rage-powers}

At 6th level, whenever a viking gains a fighter bonus feat, she can instead gain a single rage
power, as the barbarian class feature, in place of the bonus feat. Once selected, these rage powers
cannot be changed.

This alters the fighter's bonus feats.
