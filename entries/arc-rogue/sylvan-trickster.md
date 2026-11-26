+++
id = "ref/arc-rogue/sylvan-trickster"
kind = "archetype"
title = "Sylvan Trickster"
aon = "ArchetypeDisplay.aspx?FixedName=Rogue%20Sylvan%20Trickster"
source_ids = ["ultimate-wilderness"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "sylvan_trickster", path = "json/archetypes_rogue.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/rogue" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "77"

[fields]
kind = "archetype"
features = [
  { anchor = "wild-empathy", level = 1 },
  { anchor = "fey-tricks", level = 2 },
  { anchor = "resist-nature-s-lure", level = 4 },
  { anchor = "fey-resistance", level = 8 },
]
trades = [
  { replaces = "Trapfinding", feature = "trapfinding", by = ["wild-empathy"] },
  { replaces = "Uncanny dodge", feature = "uncanny-dodge", by = ["resist-nature-s-lure"] },
  { replaces = "Improved uncanny dodge", feature = "improved-uncanny-dodge", by = ["fey-resistance"] },
  { alters = "Rogue talents", feature = "rogue-talents", by = ["fey-tricks"] },
  { alters = "Class skills" },
]
+++

Sylvan tricksters are rogues who model themselves after the mischievous fey of legend. Though not
spellcasters, sylvan tricksters learn minor magical abilities reminiscent of those favored by fey
creatures. The journey for many sylvan tricksters began in childhood, learning at an elder's knee
the stories of the fey and the secrets of how to resist their tricks. Sylvan tricksters often live
in areas where the boundary with the First World is thin, and a few have even been there—voluntarily
or not.

## Class Skills {#class-skills}

A sylvan trickster adds Knowledge (nature) to her list of class skills and learns Sylvan as a bonus
language. She does not gain Knowledge (dungeoneering) as a class skill.

This alters the rogue's class skills.

## Wild Empathy (Ex) {#wild-empathy}

A sylvan trickster can improve an animal's attitude. This ability functions as the
[druid](ref/class/druid) ability of the [same name](ref/ability/wild-empathy), using the sylvan
trickster's rogue level as her effective druid level.

This replaces trapfinding.

## Fey Tricks {#fey-tricks}

A sylvan trickster can select a witch hex in place of a rogue talent. At 10th level, the sylvan
trickster can select a hex or major hex in place of a rogue talent. At 18th level, a sylvan
trickster can select a hex, major hex, or grand hex in place of a rogue talent. She cannot select
any hex more than once.

This alters rogue talents.

## Resist Nature's Lure (Ex) {#resist-nature-s-lure}

At 4th level, a sylvan trickster gains [resist nature's lure](ref/ability/resist-natures-lure) as
the druid ability of the same name.

This replaces uncanny dodge.

## Fey Resistance (Ex) {#fey-resistance}

At 8th level, a sylvan trickster gains DR 2/cold iron. At 11th level and every 3 levels thereafter,
this [damage reduction](ref/rule/damage-reduction) increases by 2 (to a maximum of DR 10/cold iron
at 20th level).

This replaces improved uncanny dodge.

## Rogue Talents {#rogue-talents}

The following rogue talents complement the sylvan trickster archetype: camouflage, charmer, honeyed
words, major magic, minor magic, survivalist, terrain mastery.

## Advanced Talents {#advanced-talents}

The following advanced rogue talents complement the sylvan trickster archetype: familiar, hide in
plain sight.
