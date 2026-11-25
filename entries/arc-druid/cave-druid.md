+++
id = "ref/arc-druid/cave-druid"
kind = "archetype"
title = "Cave Druid"
aon = "ArchetypeDisplay.aspx?FixedName=Druid%20Cave%20Druid"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "cave_druid", path = "json/archetypes_druid.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/druid" },
]
[[sources]]
publication = "advanced-players-guide"
page = "99"

[fields]
kind = "archetype"
features = [
  { anchor = "cavesense", level = 1 },
  { anchor = "nature-bond" },
  { anchor = "wild-empathy" },
  { anchor = "tunnelrunner", level = 2 },
  { anchor = "lightfoot", level = 3 },
  { anchor = "resist-subterranean-corruption", level = 4 },
  { anchor = "wild-shape", level = 6 },
]
trades = [
  { replaces = "Nature sense", feature = "nature-sense", by = ["cavesense"] },
  { replaces = "Woodland stride", feature = "woodland-stride", by = ["tunnelrunner"] },
  { replaces = "Trackless step", feature = "trackless-step", by = ["lightfoot"] },
  { replaces = "Resist nature's lure", feature = "resist-nature-s-lure", by = ["resist-subterranean-corruption"] },
  { alters = "Nature bond", feature = "nature-bond", by = ["nature-bond"] },
  { alters = "Wild empathy", feature = "wild-empathy", by = ["wild-empathy"] },
  { alters = "Wild shape", feature = "wild-shape", by = ["wild-shape"] },
]
+++

Far from the green fields of the world above lies a lightless expanse beneath the surface. This
darkling fairyland is not without beauty and natural wonders of its own, and a few druids seek to
preserve this hidden realm and purge it of the fell horrors that creep up from below.

## Cavesense (Ex) {#cavesense}

A cave druid adds [Knowledge (dungeoneering)](ref/skill/knowledge-dungeoneering) rather than
Knowledge (geography) as a class skill and gains a +2 bonus on Knowledge (dungeoneering) and
Survival skill checks. This ability replaces the nature sense ability.

## Nature Bond {#nature-bond}

A cave druid may select the Darkness domain in addition to the choices normally allowed, but may not
select the Air or Weather domains.

## Wild Empathy (Ex) {#wild-empathy}

A cave druid can influence oozes, rather than magical beasts, with a -4 penalty on her wild empathy
check.

## Tunnelrunner (Ex) {#tunnelrunner}

At 2nd level, a cave druid can move through areas of rubble or narrow passages that require
[squeezing](ref/misc/squeezing) at her normal movement rate and without penalty. This ability
replaces woodland stride.

## Lightfoot (Ex) {#lightfoot}

At 3rd level, a cave druid cannot be detected with [tremorsense](ref/umr/tremorsense). This ability
replaces trackless step.

## Resist Subterranean Corruption (Ex) {#resist-subterranean-corruption}

At 4th level, a cave druid gains a +2 bonus on saves against exceptional, supernatural, and
[spell-like abilities](ref/umr/spell-like-abilities) of oozes and aberrations. This ability replaces
resist nature's lure.

## Wild Shape (Su) {#wild-shape}

A cave druid gains this ability at 6th level, except that her effective druid level for this ability
is equal to her druid level - 2. She cannot use wild shape to adopt a plant form. At 10th level, the
cave druid can assume the form of a Small or Medium ooze as if using
_[beast shape III](ref/spell/beast-shape-3)_, and at 12th level that of a Tiny or Large ooze as if
using _[beast shape IV](ref/spell/beast-shape-4)_ (treating the ooze as if it were a magical beast
without a natural armor bonus). When in ooze form, the cave druid has no discernible anatomy and is
immune to poison, sneak attacks, and critical hits.
