+++
id = "ref/arc-skald/wyrm-singer"
kind = "archetype"
title = "Wyrm Singer"
aon = "ArchetypeDisplay.aspx?FixedName=Skald%20Wyrm%20Singer"
source_ids = ["legacy-of-dragons"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "wyrm_singer", path = "json/archetypes_skald.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/skald" },
]
[[sources]]
publication = "legacy-of-dragons"
page = "14"

[fields]
kind = "archetype"
features = [
  { anchor = "wyrm-song" },
  { anchor = "draconic-rage", level = 1 },
  { anchor = "wyrm-saga", level = 14 },
  { anchor = "breath-weapon", level = 12 },
]
trades = [
  { replaces = "Inspired rage", feature = "inspired-rage", by = ["draconic-rage"] },
  { replaces = "Song of the fallen", feature = "song-of-the-fallen", by = ["wyrm-saga"] },
  { replaces = "Rage power gained at 12th level", feature = "rage-powers", levels = [12], by = ["breath-weapon"] },
]
+++

Wyrm singers spin fragments of the story of the ongoing struggle between noble Apsu and wicked
Dahak.

## Wyrm Song (Su) {#wyrm-song}

A wyrm singer gains the following raging songs.

## Draconic Rage (Su) {#draconic-rage}

At 1st level, a wyrm singer can kindle an echo of ancient rage felt between warring dragon clans in
his allies. This ability acts as inspired rage, except those affected gain a +2 morale bonus on
melee attack and damage rolls and a +2 morale bonus on saving throws against paralysis and sleep
effects (but they still take a -1 penalty to their AC), rather than inspired rage's normal bonuses.
At 4th level and every 4 skald levels thereafter, the song's bonuses on saves against paralysis and
sleep effects increase by 1. At 8th and 16th levels, the song's bonus on melee attack and damage
rolls increases by 1.

This ability replaces inspired rage.

## Wyrm Saga (Su) {#wyrm-saga}

At 14th level, a wyrm singer embraces the essence of the draconic histories, allowing his allies to
manifest aspects of a dragon in their physical forms. The wyrm singer selects a single ally within
60 feet to take on a draconic aspect (as per
_[form of the dragon I](ref/spell/form-of-the-dragon-1)_) of a type of the wyrm singer's choice. The
ally cannot use the breath weapon attack provided by _form of the dragon_. The wyrm singer must
expend 1 round of raging song each round to maintain wyrm saga, and can affect only a single ally at
a time.

This ability replaces song of the fallen.

## Breath Weapon (Su) {#breath-weapon}

At 12th level, once per day as a swift action, a wyrm singer can grant a breath weapon attack to
himself or an ally affected by his draconic rage raging song. Using the breath weapon is a standard
action, and it affects creatures in a 30-foot cone or a 60-foot line. The breath weapons deals 1d6
points of damage per 2 skald levels the wyrm singer has, and is of an energy type of the wyrm
singer's choice (acid, cold, electricity, or fire). Creatures caught in the area can attempt a
Reflex save (DC = 10 + 1/2 the wyrm singer's skald level + his Charisma modifier) to halve the
damage. This ability replaces the rage power gained at 12th level.
