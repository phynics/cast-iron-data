+++
id = "ref/arc-druid/undine-adept"
kind = "archetype"
title = "Undine Adept"
aon = "ArchetypeDisplay.aspx?FixedName=Druid%20Undine%20Adept"
source_ids = ["advanced-race-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "undine_adept", path = "json/archetypes_druid2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/druid" },
]
[[sources]]
publication = "advanced-race-guide"
page = "176"

[fields]
kind = "archetype"
features = [
  { anchor = "domains" },
  { anchor = "amphibious", level = 2 },
  { anchor = "augment-summoning", level = 3 },
  { anchor = "resist-water-s-call", level = 4 },
  { anchor = "wild-shape", level = 6 },
  { anchor = "commune-with-water-spirits", level = 9 },
]
trades = [
  { replaces = "Woodland stride", feature = "woodland-stride", by = ["amphibious"] },
  { replaces = "Trackless step", feature = "trackless-step", by = ["augment-summoning"] },
  { replaces = "Resist nature's lure", feature = "resist-nature-s-lure", by = ["resist-water-s-call"] },
  { replaces = "Wild shape", feature = "wild-shape", by = ["wild-shape"] },
  { replaces = "Venom immunity", feature = "venom-immunity", by = ["commune-with-water-spirits"] },
]
+++

An undine adept dedicates herself to preserving the knowledge of the first undines and ensuring her
people's ancient connections to the natural world remain undisturbed. They serve as the keepers of
the roots of the undine people and as their protectors. An undine adept has the following class
features.

**Prerequisites:** Undine

## Domains {#domains}

An undine adept who chooses a domain must choose the Community or [Water](ref/domain/water) domain,
or any subdomain of those domains.

## Amphibious (Su) {#amphibious}

At 2nd level, the undine adept gains the [aquatic](ref/subtype/aquatic) subtype and the
[amphibious](ref/umr/amphibious) universal monster ability, allowing her to breathe water or air.
This ability replaces woodland stride.

## Augment Summoning (Su) {#augment-summoning}

At 3rd level, any creature with the water subtype the undine adept summons with either
_[summon monster](ref/spell/summon-monster)_ or
_[summon nature's ally](ref/spell/summon-natures-ally)_ gains the benefits of the
[Augment Summoning](ref/feat/augment-summoning) feat. This replaces trackless step.

## Resist Water's Call (Su) {#resist-water-s-call}

At 4th level, an undine adept gains a +4 bonus on saving throws against the spell-like and
supernatural abilities of outsiders with the aquatic or water subtype, fey with the aquatic or water
subtype, and spells and effects with the water descriptor. This ability replaces resist nature's
lure.

## Wild Shape (Su) {#wild-shape}

At 6th level, an undine adept gains the ability to use wild shape. When an undine takes the form of
a creature with the aquatic or water subtype, this ability functions at her class level + 1. For all
other forms, her effective druid level for the ability is equal to her actual undine adept level.
This ability otherwise functions as and replaces wild shape.

## Commune with Water Spirits {#commune-with-water-spirits}

At 9th level, an undine adept adds _[commune](ref/spell/commune)_ to her druid spell list. She may
use this spell whether she worships a deity or elemental forces. This ability replaces venom
immunity.
