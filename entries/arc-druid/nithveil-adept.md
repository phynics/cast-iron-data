+++
id = "ref/arc-druid/nithveil-adept"
kind = "archetype"
title = "Nithveil Adept"
aon = "ArchetypeDisplay.aspx?FixedName=Druid%20Nithveil%20Adept"
source_ids = ["inner-sea-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "nithveil_adept", path = "json/archetypes_druid2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/druid" },
]
[[sources]]
publication = "inner-sea-intrigue"
page = "44"

[fields]
kind = "archetype"
features = [
  { anchor = "nithveil-skills", level = 1 },
  { anchor = "nature-bond", level = 1 },
  { anchor = "animal-speech", level = 1 },
  { anchor = "resist-fey-influence", level = 4 },
  { anchor = "locate-nithveil", level = 9 },
]
trades = [
  { replaces = "Spontaneous casting", feature = "spontaneous-casting", by = ["animal-speech"] },
  { replaces = "Resist nature's lure", feature = "resist-nature-s-lure", by = ["resist-fey-influence"] },
  { alters = "Nature bond", feature = "nature-bond", by = ["nature-bond"] },
  { replaces = "Nature sense", feature = "nature-sense", by = ["nithveil-skills"] },
]
+++

Nithveil adepts learn the secret magic of the First World fey in the moving, reality-phasing city of
Nithveil, which appears on the new moon at seemingly random locations in the Grungir Forest in the
Lands of the Linnorm Kings. The most common deities worshiped by these druids are the Green Mother
and the Lantern King, Eldest patrons of intrigue and trickery.

## Nithveil Skills {#nithveil-skills}

A Nithveil adept adds Bluff, Diplomacy, Disguise, Sense Motive, Perform (any), and Stealth to her
list of class skills.

This ability replaces nature sense.

## Nature Bond (Su) {#nature-bond}

A Nithveil adept cannot select an animal companion, and can take only a domain. If she worships an
[Eldest](ref/rule/the-eldest), the Nithveil trickster can choose any of the domains or subdomains
granted by that Eldest in addition to those normally available to druids.

This ability alters nature bond.

## Animal Speech (Su) {#animal-speech}

A Nithveil adept can imbue normal animals with the ability to speak for a brief period. Once per day
as a standard action, the Nithveil adept can touch an animal to grant it the ability to speak any
language the druid knows for 1 minute per druid level. This does not increase the animal's
Intelligence or improve its attitude, and the animal behaves as though communicating with someone
under the effects of a _[speak with animals](ref/spell/speak-with-animals)_ spell, save that it can
speak with anyone who understands the language the Nithveil adept grants it. The Nithveil adept
gains one additional use of this ability at 4th level and every 4 levels thereafter.

This ability replaces spontaneous casting.

## Resist Fey Influence (Ex) {#resist-fey-influence}

At 4th level, a Nithveil adept gains a +4 bonus on saving throws against the spell-like and
supernatural abilities of fey. Once per day before attempting such a saving throw, the Nithveil
adept can choose to roll two dice and take the better result, applying the +4 bonus as normal.

This ability replaces resist nature's lure.

## Locate Nithveil (Sp) {#locate-nithveil}

At 9th level, a Nithveil adept can cast _[find the path](ref/spell/find-the-path)_ as a
[spell-like ability](ref/umr/spell-like-abilities), but only to locate Nithveil. The spell's
duration is extended until the druid reaches her destination or until Nithveil recedes from the
Material Plane at the end of the new moon. This ability can be used only once per month, during the
new moon.
