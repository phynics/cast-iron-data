+++
id = "ref/arc-hunter/feykiller"
kind = "archetype"
title = "Feykiller"
aon = "ArchetypeDisplay.aspx?FixedName=Hunter%20Feykiller"
source_ids = ["legacy-of-the-first-world"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "feykiller", path = "json/archetypes_hunter.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/hunter" },
]
[[sources]]
publication = "legacy-of-the-first-world"
page = "13"

[fields]
kind = "archetype"
features = [
  { anchor = "animal-focus", level = 1 },
  { anchor = "iron-talons", level = 1 },
  { anchor = "resist-nature-s-lure", level = 4 },
  { anchor = "grounded", level = 17 },
]
trades = [
  { replaces = "Wild empathy", feature = "wild-empathy", by = ["iron-talons"] },
  { replaces = "speak with master", feature = "speak-with-master", by = ["iron-talons"] },
  { replaces = "Improved empathic link", feature = "improved-empathic-link", by = ["resist-nature-s-lure"] },
  { replaces = "One with the wild", feature = "one-with-the-wild", by = ["grounded"] },
  { alters = "Animal focus", feature = "animal-focus", by = ["animal-focus"] },
]
+++

Some hunters in fey-plagued regions are dedicated to tracking down and eradicating these threats.
They use their connection to the natural world to ground their senses and fight corrupted First
World intrusions.

## Animal Focus (Su) {#animal-focus}

A feykiller emulates animals that grant her the ability to unmask fey trickery. She adds the
following choices to her [animal focus](ref/ability/animal-foci) ability instead of the bear, frog,
monkey, mouse, and snake choices.

### Crow {#crow}

The creature gains a +4 competence bonus on Knowledge checks to identify the abilities and
weaknesses of creatures. This bonus increases to +6 at 8th level and +8 at 15th level.

### Goat {#goat}

The creature gains a +2 competence bonus on saving throws against enchantment spells and
[spell-like abilities](ref/umr/spell-like-abilities). This bonus increases to +4 at 8th level and +6
at 15th level.

### Mongoose {#mongoose}

The creature gains a +2 competence bonus on grapple combat maneuver checks and on saving throws
against poison. These bonuses increase to +4 at 8th level and +6 at 15th level.

### Shark {#shark}

The creature gains a +4 competence bonus on Survival checks to track a creature that has taken
damage from the hunter or her animal companion in the past 24 hours. This bonus increases to +6 at
8th level and +8 at 15th level.

### Turtle {#turtle}

The creature gains a +2 enhancement bonus to its natural armor bonus. This bonus increases to +4 at
8th level and +6 at 15th level. (A creature without natural armor has an effective natural armor
bonus of +0.)

This ability alters animal focus.

## Iron Talons (Ex) {#iron-talons}

Through training and prayer, a feykiller imbues her animal companion with an enhanced ability to
fight fey. One of the animal companion's natural attacks, as selected by the feykiller, is treated
as cold iron for the purpose of overcoming [damage reduction](ref/rule/damage-reduction). At 7th
level, all of her animal companion's natural attacks are treated as cold iron.

This ability replaces wild empathy and speak with master.

## Resist Nature's Lure (Ex) {#resist-nature-s-lure}

At 4th level, a feykiller gains the [resist nature's lure](ref/ability/resist-natures-lure) druid
class feature whenever her animal companion is within 60 feet.

This ability replaces improved empathic link.

## Grounded (Su) {#grounded}

At 17th level, a feykiller gains a +4 insight bonus on saving throws against illusion and
enchantment effects, and she is immune to illusion and enchantment effects created by fey. This
ability functions only when her animal companion is within 60 feet.

This ability replaces one with the wild.
