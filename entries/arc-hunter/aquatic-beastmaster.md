+++
id = "ref/arc-hunter/aquatic-beastmaster"
kind = "archetype"
title = "Aquatic Beastmaster"
aon = "ArchetypeDisplay.aspx?FixedName=Hunter%20Aquatic%20Beastmaster"
source_ids = ["blood-of-the-sea"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "aquatic_beastmaster", path = "json/archetypes_hunter.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/hunter" },
]
[[sources]]
publication = "blood-of-the-sea"
page = "22"

[fields]
kind = "archetype"
features = [
  { anchor = "animal-focus", level = 1 },
  { anchor = "wild-empathy", level = 1 },
  { anchor = "oceanic-defense", level = 4 },
]
trades = [
  { replaces = "Improved empathic link", feature = "improved-empathic-link", by = ["oceanic-defense"] },
  { alters = "Animal focus", feature = "animal-focus", by = ["animal-focus"] },
  { alters = "Wild Empathy", feature = "wild-empathy", by = ["wild-empathy"] },
]
+++

Hunters beneath the sea are just as committed as their surface-dwelling counterparts to working
alongside their animal companions to eradicate threats. Although many aquatic beastmasters simply
want to be left alone in the areas they have claimed as their own, others use their abilities to
fight against aboleth masterminds, sahuagin tribes, and other villains that haunt the oceans.

## Animal Focus (Su) {#animal-focus}

An aquatic beastmaster emulates animals found beneath the waves. This functions as
[animal focus](ref/ability/animal-foci), but it allows only the following choices.

### Crab {#crab}

The creature gains a +4 competence bonus on Swim checks and a +2 competence bonus on
[grapple](ref/rule/grapple) combat maneuver checks. These bonuses increase to +6 and +4,
respectively, at 8th level and to +8 and +6 at 15th level.

### Dolphin {#dolphin}

The creature gains a +4 competence bonus on Knowledge checks to identify the abilities and
weaknesses of creatures. This bonus increases to +6 at 8th level and to +8 at 15th level.

### Eel {#eel}

The creature gains a +2 enhancement bonus to Dexterity. This bonus increases to +4 at 8th level and
to +6 at 15th level.

### Manta Ray {#manta-ray}

The creature gains a +4 competence bonus on Stealth checks and a +2 bonus on saving throws against
poison. These bonuses increase to +6 and +4, respectively, at 8th level and to +8 and +6 at 15th
level.

### Octopus {#octopus}

The creature gains a +4 competence bonus on Swim checks and a +2 competence bonus on grapple combat
maneuver checks. These bonuses increase to +6 and +4, respectively, at 8th level and to +8 and +6 at
15th level.

### Orca {#orca}

The creature gains a +2 enhancement bonus to Strength. This bonus increases to +4 at 8th level and
to +6 at 15th level.

### Shark {#shark}

The creature gains a +4 competence bonus on Survival checks to track a creature to which the hunter
or her animal companion has dealt damage in the past 24 hours. This bonus increases to +6 at 8th
level and to +8 at 15th level.

### Snake {#snake}

The creature gains a +2 bonus on attack rolls when making attacks of opportunity and a +2 dodge
bonus to AC against attacks of opportunity. These bonuses increase to +4 at 8th level and to +6 at
15th level.

### Turtle {#turtle}

The creature gains a +2 enhancement bonus to its natural armor bonus. This bonus increases to +4 at
8th level and to +6 at 15th level. (A creature without natural armor has an effective natural armor
bonus of +0.)

This ability alters animal focus.

## Wild Empathy (Ex) {#wild-empathy}

An aquatic beastmaster's wild empathy functions only on creatures that have a swim speed or the
aquatic or water subtype. However, she can improve the attitude of any such creature with
Intelligence 2 or less regardless of type, including mindless creatures.

## Oceanic Defense (Ex) {#oceanic-defense}

At 4th level, an aquatic beastmaster gains a +4 bonus on saving throws against spells with the water
descriptor and the extraordinary or supernatural abilities of creatures with the aquatic or water
subtype whenever her animal companion is within 60 feet.

This ability replaces improved empathic link.
