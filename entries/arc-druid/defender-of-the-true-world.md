+++
id = "ref/arc-druid/defender-of-the-true-world"
kind = "archetype"
title = "Defender of the True World"
aon = "ArchetypeDisplay.aspx?FixedName=Druid%20Defender%20of%20the%20True%20World"
source_ids = ["monster-hunters-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "defender_of_the_true_world", path = "json/archetypes_druid.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/druid" },
]
[[sources]]
publication = "monster-hunters-handbook"
page = "10"

[fields]
kind = "archetype"
features = [
  { anchor = "bonus-languages" },
  { anchor = "enemy-of-the-first-world", level = 1 },
  { anchor = "fey-empathy", level = 1 },
  { anchor = "fey-stalker", level = 3 },
  { anchor = "feybane", level = 4 },
  { anchor = "beguiling-immunity", level = 9 },
  { anchor = "first-world-deceiver", level = 13 },
]
trades = [
  { replaces = "Wild empathy", feature = "wild-empathy", by = ["fey-empathy"] },
  { replaces = "Trackless step", feature = "trackless-step", by = ["fey-stalker"] },
  { replaces = "Venom immunity", feature = "venom-immunity", by = ["beguiling-immunity"] },
  { replaces = "A thousand faces", feature = "a-thousand-faces", by = ["first-world-deceiver"] },
  { alters = "Spontaneous casting", feature = "spontaneous-casting", by = ["enemy-of-the-first-world"] },
  { alters = "Resist nature's lure", feature = "resist-nature-s-lure", by = ["feybane"] },
  { alters = "Class skills" },
]
+++

Some druids specialize in protecting Golarion from the threat of First World inhabitants. They are
devoted to tracking down, diverting, and slaying fey threats.

## Class Skills {#class-skills}

A defender of the true world gains Diplomacy as a class skill.

This alters the druid's class skills.

## Bonus Languages {#bonus-languages}

A defender of the true world can select Aklo, Sylvan, or Undercommon as bonus languages, in addition
to the normal list of bonus languages available.

## Enemy of the First World {#enemy-of-the-first-world}

A defender of the true world cannot use _[summon nature's ally](ref/spell/summon-natures-ally)_ to
summon fey creatures.

This modifies spontaneous casting.

## Fey Empathy (Ex) {#fey-empathy}

A defender of the true world gains a +2 competence bonus on Bluff, Diplomacy, and Intimidate checks
when interacting with fey creatures. This bonus increases by 1 for every 4 druid levels she has
(maximum +7 at 20th level).

This replaces wild empathy.

## Fey Stalker (Ex) {#fey-stalker}

At 3rd level, the defender of the true world's animal companion and any creatures she summons with
_[summon nature's ally](ref/spell/summon-natures-ally)_ gain a +1 morale bonus on attack and damage
rolls against fey creatures. This bonus increases to +2 at 8th level, +3 at 13th level, and +4 at
18th level.

This ability replaces trackless step.

## Feybane (Ex) {#feybane}

At 4th level, a defender of the true world doesn't gain a bonus on saving throws against spells and
effects that utilize or target plants. She instead treats her natural attacks as cold iron for the
purpose of overcoming [damage reduction](ref/rule/damage-reduction), and she gains a +2 bonus on
caster level checks to overcome the [spell resistance](ref/rule/spell-resistance) of fey creatures.

This ability alters resist nature's lure.

## Beguiling Immunity (Ex) {#beguiling-immunity}

At 9th level, a defender of the true world becomes immune to the mind-affecting effects of fey.

This ability replaces venom immunity.

## First World Deceiver (Su) {#first-world-deceiver}

At 13th level, a defender of the true world gains the ability to change her appearance as per
_[alter self](ref/spell/alter-self)_, except she can take the form of a humanoid or fey creature.
Her base land speed from this ability cannot exceed 60 feet.

This ability replaces a thousand faces.
