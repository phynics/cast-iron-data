+++
id = "ref/arc-druid/blight-druid"
kind = "archetype"
title = "Blight Druid"
aon = "ArchetypeDisplay.aspx?FixedName=Druid%20Blight%20Druid"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "blight_druid", path = "json/archetypes_druid.json" },
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
  { anchor = "nature-bond" },
  { anchor = "vermin-empathy", level = 1 },
  { anchor = "miasma", level = 5 },
  { anchor = "blightblooded", level = 9 },
  { anchor = "plaguebearer", level = 13 },
]
trades = [
  { replaces = "Wild empathy", feature = "wild-empathy", by = ["vermin-empathy"] },
  { replaces = "Trackless step", feature = "trackless-step", by = ["miasma"] },
  { replaces = "resist nature's lure", feature = "resist-nature-s-lure", by = ["miasma"] },
  { replaces = "Venom immunity", feature = "venom-immunity", by = ["blightblooded"] },
  { replaces = "A thousand faces", feature = "a-thousand-faces", by = ["plaguebearer"] },
  { alters = "Nature bond", feature = "nature-bond", by = ["nature-bond"] },
]
+++

The devoted servants of nature corrupted, ruined, and destroyed, blight druids are the caretakers of
lands ravaged by natural disaster. While some are devoted to reforming and reclaiming lands
despoiled by the ravages of civilization, others seek out the more rapacious violence inherent in
nature and feed the creeping rot and decay that brings an end to all things.

## Nature Bond (Ex) {#nature-bond}

A blight druid may not bond with an animal companion, but may either call a
[familiar](ref/sidekick/familiar) as a [wizard](ref/class/wizard) of her druid level or select from
the Darkness, Death, and [Destruction](ref/domain/destruction) domains in addition to those normally
available.

## Vermin Empathy (Su) {#vermin-empathy}

A blight druid can improve the attitude of vermin as a normal druid can with animals. Vermin have a
starting attitude of unfriendly. The blight druid can also improve the attitude of animals and
mindless undead creatures that were formerly animals, but she takes a -4 penalty on the check unless
the animal or undead has a disease special attack. This ability replaces wild empathy.

## Miasma (Ex) {#miasma}

Starting at 5th level, if a blight druid is adjacent to a creature at the beginning of its turn, the
creature must succeed at a Fortitude save with a DC of 10 + 1/2 the druid's level + the druid's
Wisdom modifier or become [sickened](ref/misc/sickened) for 1 round. A creature of the animal, fey,
or plant type that fails its save is [nauseated](ref/misc/nauseated) for 1 round and sickened for 1
minute thereafter. If the creature makes its save, it is immune to this effect for 24 hours, as are
creatures immune to disease. This ability replaces trackless step and resist nature's lure.

## Blightblooded (Ex) {#blightblooded}

At 9th level, a blight druid gains immunity to all diseases, including natural and supernatural
diseases. She also becomes immune to effects that would cause her to become sickened or nauseated.
This ability replaces venom immunity.

## Plaguebearer (Su) {#plaguebearer}

Starting at 13th level, any creature that strikes a blight druid with a touch attack, unarmed
strike, or natural weapon must succeed at a Fortitude save with a DC of 10 + 1/2 the druid's level +
the druid's Wisdom modifier or contract a disease, as the _[contagion](ref/spell/contagion)_ spell.
If the creature makes its save, it is immune to this effect for 24 hours. This ability replaces a
thousand faces.
