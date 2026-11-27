+++
id = "ref/arc-bard/busker"
kind = "archetype"
title = "Busker"
aon = "ArchetypeDisplay.aspx?FixedName=Bard%20Busker"
source_ids = ["heroes-of-the-streets"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "busker", path = "json/archetypes_bard.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/bard" },
]
[[sources]]
publication = "heroes-of-the-streets"
page = "26"

[fields]
kind = "archetype"
features = [
  { anchor = "bardic-performance", level = 1 },
  { anchor = "busker-stunts" },
  { anchor = "quick-hands", level = 1 },
  { anchor = "patter" },
  { anchor = "living-statue", level = 3 },
  { anchor = "fascinate", level = 6 },
  { anchor = "suggestion", level = 8 },
  { anchor = "inventive-juggler", level = 9 },
  { anchor = "impossible-sleight-of-hand", level = 15 },
  { anchor = "flexible-performer" },
]
trades = [
  { replaces = "Bardic performance", feature = "bardic-performance", by = ["bardic-performance"] },
]
+++

A busker uses his dazzling physical stunts to get by on his own in the city streets. Buskers
commonly use their skills to entertain for a few coins, but also pick pockets, hide in plain sight
as statues, and manipulate the desperate in medicine shows. Many buskers are also
[jugglers](ref/arc-bard/juggler).

## Bardic Performance {#bardic-performance}

Buskers do not gain the bardic performance ability or any of its performance types, except as noted
below.

## Busker Stunts (Su) {#busker-stunts}

A busker knows how to magically enhance the effectiveness of his physical stunts. He can use this
ability for a number of rounds per day equal to 4 + his Charisma modifier. Maintaining a stunt is a
free action, but it ends immediately if the busker is killed, paralyzed, stunned, knocked
unconscious, or otherwise prevented from taking a free action to maintain it each round. This
ability is treated as bardic performance for the purposes of feats, abilities, and other effects
that affect bardic performance. Like a bardic performance, a busker stunt cannot be maintained at
the same time as other performance abilities.

## Quick Hands (Su) {#quick-hands}

At 1st level as a swift action, a busker can call on his stunts to gain a +1 competence bonus on
Acrobatics checks, a +1 dodge bonus to AC and on Reflex saves, and a +1 bonus on attack rolls as if
from _[haste](ref/spell/haste)_. This bonus increases to +2 at 5th level, +3 at 11th level, and +4
at 17th level. At 5th level, while maintaining this stunt the busker also gains an extra attack at
his highest base attack bonus as if from _[haste](ref/spell/haste)_.

## Patter (Su) {#patter}

A busker can engage in brisk conversation that seems innocuous, but actually encourages creatures to
reveal secrets to the busker. Each round while maintaining this stunt, the busker can force one
creature within 30 feet that is able to see and hear the busker and has an attitude of indifferent
or better towards him to attempt a Will save (DC = 10 + 1/2 the busker's bard level + the busker's
Charisma modifier). On a failed save, the target must answer one yes/no question the busker asks to
the best of its ability. Anyone observing this (including the creature asked, even if it succeeds at
its save) must succeed at a Sense Motive check (opposed by the busker's Bluff check) to realize the
question was asked or answered. A target that feels threatened or is in combat is immune to this
ability. This is a language-dependent, mind-affecting enchantment effect.

## Living Statue (Su) {#living-statue}

At 3rd level, a busker can use this stunt to hold perfectly still. While maintaining this stunt the
busker can attempt a Bluff check (opposed by all observers' Sense Motive checks) to appear
paralyzed, dead, or as a statue (this requires that the busker be disguised to look as though he
were made of stone or metal, which is aided with a
[statue disguise kit](ref/eq-misc/statue-disguise-kit); see page 13). Even magical means of
determining the true nature of the busker do not function for an observer that fails this check. If
the busker takes any physical actions, this stunt ends.

## Fascinate (Su) {#fascinate}

At 6th level, the busker can [fascinate](ref/misc/fascinated) creatures with his stunts, as per the
bardic performance ability.

## Suggestion (Sp) {#suggestion}

At 8th level, the busker can implant a _[suggestion](ref/spell/suggestion)_ in a creature with his
stunts, as per the bardic performance ability of the same name.

## Inventive Juggler (Ex) {#inventive-juggler}

At 9th level, a busker masters unconventionally dangerous juggling techniques. While maintaining
this stunt, the busker can use a thrown weapon (even an improvised one) to threaten spaces as though
he were using a [reach](ref/misc/reach) weapon. At 12th level and every 3 levels thereafter, the
busker threatens squares up to 10 feet farther away with thrown weapons.

## Impossible Sleight of Hand (Su) {#impossible-sleight-of-hand}

At 15th level, a busker can store items in or retrieve them from a personal extradimensional space
with a maximum capacity of 8,000 cubic feet and 8,000 pounds as a busker stunt. The item may be sent
from or called to his hand or any place it fits on his person. He can access the extradimensional
space only to store or retrieve a single object at a time; to retrieve or store an object larger
than Fine size, the busker must expend 1 additional round of busker stunts for each size category
larger than Fine. This stunt is instantaneous and must be activated again each time the busker
wishes to use it. The extradimensional space empties its contents within the busker's space if he
dies.

## Flexible Performer (Ex) {#flexible-performer}

A busker can attempt Acrobatics, Disguise, Sleight of Hand, and Stealth checks to earn money instead
of Perform checks. He can use his Bluff modifier in place of his Diplomacy modifier on Diplomacy
checks.
