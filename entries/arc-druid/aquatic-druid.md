+++
id = "ref/arc-druid/aquatic-druid"
kind = "archetype"
title = "Aquatic Druid"
aon = "ArchetypeDisplay.aspx?FixedName=Druid%20Aquatic%20Druid"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "aquatic_druid", path = "json/archetypes_druid.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/druid" },
]
[[sources]]
publication = "advanced-players-guide"
page = "98"

[fields]
kind = "archetype"
features = [
  { anchor = "wild-empathy" },
  { anchor = "aquatic-adaptation", level = 2 },
  { anchor = "natural-swimmer", level = 3 },
  { anchor = "resist-ocean-s-fury", level = 4 },
  { anchor = "wild-shape" },
  { anchor = "seaborn", level = 9 },
  { anchor = "deep-diver", level = 13 },
]
trades = [
  { replaces = "Woodland stride", feature = "woodland-stride", by = ["aquatic-adaptation"] },
  { replaces = "Trackless step", feature = "trackless-step", by = ["natural-swimmer"] },
  { replaces = "Resist nature's lure", feature = "resist-nature-s-lure", by = ["resist-ocean-s-fury"] },
  { replaces = "Venom immunity", feature = "venom-immunity", by = ["seaborn"] },
  { replaces = "A thousand faces", feature = "a-thousand-faces", by = ["deep-diver"] },
  { alters = "Wild empathy", feature = "wild-empathy", by = ["wild-empathy"] },
  { alters = "Wild shape", feature = "wild-shape", by = ["wild-shape"] },
]
+++

Shepherds of the lakes and seas, aquatic druids guard ecosystems ranging from shallows streams to
deep ocean trenches, ministering to their residents and communing with the tides.

## Wild Empathy (Ex) {#wild-empathy}

An aquatic druid's wild empathy functions only on creatures that have a swim speed or the aquatic or
water subtype; however, she can improve the attitude of any such creature with Intelligence 2 or
less regardless of type, including mindless creatures.

## Aquatic Adaptation (Ex) {#aquatic-adaptation}

At 2nd level, an aquatic druid gains an insight bonus on Initiative checks and Knowledge
(geography), Perception, Stealth, Survival, and Swim checks equal to 1/2 her druid level in aquatic
terrain, and she cannot be tracked such environments. This ability replaces woodland stride.

## Natural Swimmer (Ex) {#natural-swimmer}

At 3rd level, an aquatic druid gains a swim speed equal to half her land speed. This ability
replaces trackless step.

## Resist Ocean's Fury (Ex) {#resist-ocean-s-fury}

At 4th level, an aquatic druid gains a +4 bonus on saving throws against spells of the water type or
the exceptional or supernatural abilities of creatures with the aquatic or water subtype. This
ability replaces resist nature's lure.

## Wild Shape (Su) {#wild-shape}

An aquatic druid gains this ability at 6th level, except that her effective druid level for the
ability is equal to her druid level - 2.

## Seaborn (Ex) {#seaborn}

At 9th level, an [aquatic](ref/subtype/aquatic) druid gains the aquatic subtype, the
[amphibious](ref/umr/amphibious) trait, and a swim speed equal to her land speed. She also can
endure cold climate effects as if using _[endure elements](ref/spell/endure-elements)_. This ability
replaces venom immunity.

## Deep Diver (Ex) {#deep-diver}

At 13th level, an aquatic druid gains DR/slashing or piercing equal to 1/2 her level. This
[damage reduction](ref/rule/damage-reduction) also applies against spells and
[spell-like abilities](ref/umr/spell-like-abilities) that inflict damage by grappling or crushing
(e.g., _[black tentacles](ref/spell/black-tentacles)_, _[crushing hand](ref/spell/crushing-hand)_).
She never takes [pressure damage](ref/rule/water-dangers) from deep water. This ability replaces a
thousand faces.
