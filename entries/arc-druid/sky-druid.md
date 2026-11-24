+++
id = "ref/arc-druid/sky-druid"
kind = "archetype"
title = "Sky Druid"
aon = "ArchetypeDisplay.aspx?FixedName=Druid%20Sky%20Druid"
source_ids = ["advanced-race-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "sky_druid", path = "json/archetypes_druid2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/druid" },
]
[[sources]]
publication = "advanced-race-guide"
page = "158"

[fields]
kind = "archetype"
features = [
  { anchor = "nature-bond", level = 1 },
  { anchor = "sky-s-embrace", level = 2 },
  { anchor = "resist-storm", level = 4 },
  { anchor = "skymaster", level = 5 },
  { anchor = "wild-shape", level = 6 },
  { anchor = "soaring-form", level = 9 },
  { anchor = "into-the-wild-blue", level = 13 },
]
trades = [
  { replaces = "Woodland stride", feature = "woodland-stride", by = ["sky-s-embrace"] },
  { replaces = "Resist nature's lure", feature = "resist-nature-s-lure", by = ["resist-storm"] },
  { replaces = "Trackless step", feature = "trackless-step", by = ["skymaster"] },
  { replaces = "Wild shape", feature = "wild-shape", by = ["wild-shape"] },
  { replaces = "Venom immunity", feature = "venom-immunity", by = ["soaring-form"] },
  { replaces = "A thousand faces", feature = "a-thousand-faces", by = ["into-the-wild-blue"] },
  { alters = "Nature bond", feature = "nature-bond", by = ["nature-bond"] },
]
+++

Some druids develop ties not to a particular landscape, but instead to the endless blue expanse of
the skies. Such are the sky druids, who are more at home soaring through air than standing on the
ground. A sky druid has the following class features.

**Prerequisites:** Sylph

## Weapon and Armor Proficiency {#weapon-and-armor-proficiency}

A sky druid loses medium armor proficiency.

## Nature Bond (Ex) {#nature-bond}

At 1st level, a sky druid who chooses an [animal](ref/domain/animal) companion must select one with
a fly speed. If choosing a domain, the sky druid must choose from the [Air](ref/domain/air),
Animals, Liberation, and [Weather](ref/domain/weather) domains, or subdomains appropriate to those
domains.

## Sky's Embrace (Su) {#sky-s-embrace}

At 2nd level, a sky druid no longer takes falling damage, as though she were constantly under the
effect of _[feather fall](ref/spell/feather-fall)_. Additionally, she may take ranks in the Fly
skill regardless of whether she has a natural fly speed, and may use her Fly skill in place of
Acrobatics when making jump checks. This ability replaces woodland stride.

## Resist Storm (Ex) {#resist-storm}

At 4th level, a sky druid gains a +4 bonus on saving throws against spells with the air or
electricity descriptors and against effects that control or modify the weather (such as
_[sleet storm](ref/spell/sleet-storm)_). This ability replaces resist nature's lure.

## Skymaster (Su) {#skymaster}

At 5th level, a sky druid can use the _[fly](ref/spell/fly)_ spell (self only) for a number of
minutes per day equal to her druid level. These minutes do not need to be consecutive. This ability
replaces trackless step.

## Wild Shape (Su) {#wild-shape}

At 6th level, a sky druid gains the ability to use wild shape. When a sky druid takes the form of a
creature with a fly speed, this ability functions at her class level + 1. For all other forms, her
effective druid level for the ability is equal to her actual sky druid level. This ability otherwise
functions as and replaces wild shape.

## Soaring Form (Ex) {#soaring-form}

At 9th level, a sky druid is no longer affected by [altitude sickness](ref/rule/mountain-travel) or
natural or magical wind. This ability replaces venom immunity.

## Into the Wild Blue (Su) {#into-the-wild-blue}

At 13th level, a sky druid gains a fly speed equal to twice her base land speed (good
maneuverability). This ability replaces a thousand faces.
