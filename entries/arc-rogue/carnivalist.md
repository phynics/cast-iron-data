+++
id = "ref/arc-rogue/carnivalist"
kind = "archetype"
title = "Carnivalist"
aon = "ArchetypeDisplay.aspx?FixedName=Rogue%20Carnivalist"
source_ids = ["animal-archive"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "carnivalist", path = "json/archetypes_rogue.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/rogue" },
]
[[sources]]
publication = "animal-archive"
page = "6"

[fields]
kind = "archetype"
features = [
  { anchor = "familiar", level = 1 },
  { anchor = "pet-performance", level = 2 },
  { anchor = "trained-legerdemain", level = 6 },
  { anchor = "sneak-attack", level = 2 },
  { anchor = "animal-trainer", level = 3 },
]
trades = [
  { replaces = "Rogue talents gained at 2nd, 4th, and 6th level", feature = "rogue-talents", levels = [2, 4, 6], by = ["trained-legerdemain"] },
  { replaces = "Trap sense", feature = "trap-sense", by = ["animal-trainer"] },
  { alters = "Sneak attack", feature = "sneak-attack", by = ["sneak-attack"] },
]
+++

Carnivalists train their miniature minions to perform acts of larceny and often hide their true
talents behind theatrical sideshows.

## Class Skills {#class-skills}

A carnivalist gains Handle Animal as a class skill.

## Familiar {#familiar}

At 1st level, a carnivalist gains a [familiar](ref/sidekick/familiar) as a wizard of equal level.
Levels in a class that grants a familiar stack with carnivalist levels for determining the
familiar's abilities.

## Pet Performance (Ex) {#pet-performance}

A carnivalist gains use of several bardic performances, making Handle Animal checks in place of any
Perform checks. At 2nd level, she gains the [distraction](ref/performance/distraction) bardic
performance. At 4th level, she gains the [fascinate](ref/performance/fascinate) bardic performance.
At 6th level, she also gains use of the following performance.

## Trained Legerdemain (Ex) {#trained-legerdemain}

At 6th level, a carnivalist can command a familiar or pet within 30 feet to make a Disable Device or
Sleight of Hand check as if trained in the skill, using its own skill ranks (if any), Dexterity
modifier, and equipment, with a competence bonus equal to 1/2 her rogue level. The check requires
the normal amount of time to complete and the DC increases by 5. The carnivalist must maintain this
pet performance each round her familiar or pet attempts a Disable Device or Sleight of Hand check.

The pet performance ability otherwise functions identically to bardic performance. Levels in a class
with the [distraction](ref/carried/bestiary/rules/universal-monster-rules/distraction) or fascinate
bardic performances stack with carnivalist levels for the purpose of determining bonuses granted by
these performances. This ability replaces the rogue talents gained at 2nd, 4th, and 6th level.

## Sneak Attack (Ex) {#sneak-attack}

A carnivalist gains this ability starting at 2nd level. The sneak attack damage dealt is 1d6 points
at 2nd level, and increases by 1d6 points every 4 carnivalist levels thereafter. A carnivalist's
familiar can also deal sneak attack damage as appropriate to foes as long as it is within 30 feet of
her (though only Small and larger creatures may flank enemies, as usual).

## Animal Trainer (Ex) {#animal-trainer}

Starting at 3rd level, a carnivalist receives a bonus equal to 1/2 her rogue level whenever she uses
Handle Animal on a Tiny or Small animal. In addition, she can increase the DC by 5 to reduce the
time needed to teach an animal a new trick or train an animal for a general purpose to 1 day for
every week normally required. She can also train more than one animal at once, although each animal
after the first adds 2 to the DC. This ability replaces trap sense.
