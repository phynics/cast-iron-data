+++
id = "ref/arc-barbarian/beastkin-berserker"
kind = "archetype"
title = "Beastkin Berserker"
aon = "ArchetypeDisplay.aspx?FixedName=Barbarian%20Beastkin%20Berserker"
source_ids = ["heroes-of-the-darklands"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "beastkin_berserker", path = "json/archetypes_barbarian.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/barbarian" },
]
[[sources]]
publication = "heroes-of-the-darklands"
page = "21"

[fields]
kind = "archetype"
features = [
  { anchor = "savage-rapport", level = 1 },
  { anchor = "feral-transformation", level = 4 },
]
trades = [
  { replaces = "Fast movement", feature = "fast-movement", by = ["savage-rapport"] },
  { replaces = "Rage powers gained at 4th, 8th, and 12th levels", feature = "rage-powers", levels = [4, 8, 12], by = ["feral-transformation"] },
]
+++

While some barbarians take on bestial aspects in their rages, the beastkin berserker descends so
deeply into primal fury that she actually transforms into an animal. Berserkers of the surface world
often associate with predators such as bears or wolves, and are sometimes mistaken for lycanthropes.
The barbarians in Deep Tolguth shapechange into rampaging dinosaurs or megafauna, crafting their
armor out of the hide and bones of their favored animals.

## Savage Rapport (Ex) {#savage-rapport}

At 1st level, a beastkin berserker gains a spiritual connection to a specific kind of creature with
the animal type (such as a [badger](ref/monster/badger) or a
[triceratops](ref/monster/dinosaur-triceratops)). She adds [half](ref/misc/fractions-and-rounding)
her level (minimum 1) on Handle Animal, Intimidate, and Sense Motive checks involving the chosen
type of animal.

At 5th level and every 5 levels thereafter (10th, 15th, and 20th levels), the beastkin berserker can
select an additional kind of animal to which these bonuses apply.

This ability replaces fast movement.

## Feral Transformation (Su) {#feral-transformation}

At 4th level, when entering a rage, a beastkin berserker can take the form of a Small or Medium
animal. This functions as _[beast shape I](ref/spell/beast-shape-1)_, except the duration is for as
long as the beastkin berserker rages and the animal must be one she has chosen with her savage
rapport.

At 8th level, the beastkin berserker can use feral transformation to take the form of a Large or
Tiny animal that she has chosen with her savage rapport. Feral transformation now acts as
_[beast shape II](ref/spell/beast-shape-2)_.

At 12th level, a beastkin berserker is able to use feral transformation to take the form of a Huge
or Diminutive animal that she has chosen with her savage rapport. Feral transformation now functions
as _[beast shape III](ref/spell/beast-shape-3)_.

This ability replaces the rage powers gained at 4th, 8th, and 12th levels.
