+++
id = "ref/arc-fighter/spear-fighter"
kind = "archetype"
title = "Spear Fighter"
aon = "ArchetypeDisplay.aspx?FixedName=Fighter%20Spear%20Fighter"
source_ids = ["martial-arts-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "spear_fighter", path = "json/archetypes_fighter2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/fighter" },
]
[[sources]]
publication = "martial-arts-handbook"
page = "11"

[fields]
kind = "archetype"
features = [
  { anchor = "balanced-stride", level = 2 },
  { anchor = "spear-parry", level = 3 },
  { anchor = "weapon-training", level = 5 },
  { anchor = "weapon-mastery", level = 20 },
]
trades = [
  { replaces = "Bravery", feature = "bravery", by = ["balanced-stride"] },
  { replaces = "Armor training 1, 2, 3, and 4", feature = "armor-training", levels = [3, 7, 11, 15], by = ["spear-parry"] },
  { replaces = "armor mastery", feature = "armor-mastery", by = ["spear-parry"] },
  { alters = "The fighter's armor proficiencies", feature = "weapon-and-armor-proficiencies", power = "armor" },
  { alters = "Weapon training", feature = "weapon-training", by = ["weapon-training"] },
  { alters = "Weapon mastery", feature = "weapon-mastery", by = ["weapon-mastery"] },
  { alters = "Class skills" },
]
+++

The spear is one of the oldest weapons known to most humanoid races, and no weapon has seen as much
use across the different continents of Golarion. One of the oldest spear-fighting styles originates
in Vudra, where many martial arts traditions consider the spear to be the ultimate weapon.

## Class Skills {#class-skills}

A spear fighter adds Acrobatics to his list of class skills and removes Ride as a class skill.

This alters the fighter's class skills.

## Armor Proficiency {#armor-proficiency}

A spear fighter is not proficient with heavy armor or tower shields. Instead, he gains
[Dodge](ref/feat/dodge) as a bonus feat, even if he doesn't fulfill the prerequisites, but he can't
use this feat while wearing heavy armor or using a shield.

This alters the fighter's armor proficiencies.

## Balanced Stride (Ex) {#balanced-stride}

At 2nd level, the spear fighter gains a +1 bonus on Acrobatics checks to avoid attacks of
opportunity. This bonus increases by 1 for every 4 levels he has beyond 2nd.

This replaces bravery.

## Spear Parry (Ex) {#spear-parry}

At 3rd level, a spear fighter learns to parry his opponents' attacks with his spear. This functions
as a swashbuckler's [opportune parry and riposte](ref/swashdeed/opportune-parry-and-riposte) deed
except as noted below. The spear fighter must use a weapon from the spears
[weapon group](ref/ability/weapon-groups) to perform the parry. He doesn't need panache to parry an
attack or to make an attack against a creature whose attack he has parried; instead, he takes a
cumulative -4 penalty on all attacks (including further parry attempts) until the end of his next
turn. At 7th, 11th, and 15th levels, the penalty decreases by 1. At 19th level, a spear fighter can
use spear parry without penalty.

This replaces armor training 1, 2, 3, and 4, and armor mastery.

## Weapon Training (Ex) {#weapon-training}

At 5th level, a spear fighter must choose the spears weapon group for the weapon training class
feature.

## Weapon Mastery (Ex) {#weapon-mastery}

At 20th level, a spear fighter must choose a weapon from the spears weapon group for his weapon
mastery class feature.
