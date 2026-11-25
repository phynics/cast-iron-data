+++
id = "ref/arc-skald/instigator"
kind = "archetype"
title = "Instigator"
aon = "ArchetypeDisplay.aspx?FixedName=Skald%20Instigator"
source_ids = ["ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "instigator", path = "json/archetypes_skald.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/skald" },
]
[[sources]]
publication = "ultimate-intrigue"
page = "49"

[fields]
kind = "archetype"
features = [
  { anchor = "raging-song" },
  { anchor = "song-of-rabble-rousing", level = 5 },
  { anchor = "song-of-riot", level = 10 },
  { anchor = "revolutionary-heart", level = 7 },
]
trades = [
  { replaces = "Spell kenning", feature = "spell-kenning", by = ["song-of-rabble-rousing"] },
  { replaces = "Dirge of doom", feature = "dirge-of-doom", by = ["song-of-riot"] },
  { replaces = "Lore master", feature = "lore-master", by = ["revolutionary-heart"] },
]
+++

The instigator influences the will of the people, turning them toward his own purposes. Regardless
of whether what the instigator says is true or not, he inflames emotions in others and suspends
their reason. Instigators are often revolutionaries, political or otherwise, but they might also be
warmongering firebrands or wicked souls who spread prejudice against others.

## Raging Song (Su) {#raging-song}

An instigator gains the following raging songs.

## Song of Rabble-Rousing (Sp) {#song-of-rabble-rousing}

At 5th level, the instigator can perform for 1 full round and spend 4 rounds of raging song. This
affects those who hear the song for up to 1 hour as per _[enthrall](ref/spell/enthrall)_. This
ability replaces spell kenning.

## Song of Riot (Sp, Su) {#song-of-riot}

At 10th level, the instigator can fill the hearts of his listeners with hatred and rouse them into a
frenzy. He can use this performance on all targets with fewer than 4 Hit Dice and a Wisdom score
lower than 16 who are currently enthralled, without disrupting the _[enthrall](ref/spell/enthrall)_
effect (even if a creature succeeds at its saving throw). This ability requires a standard action to
activate and costs 4 additional rounds of raging song.

Enthralled creatures must each attempt a new saving throw against an effect that functions as the
_[foster hatred](ref/spell/foster-hatred)_ spell, except that, unlike with the spell, the instigator
is free to choose subgroups, organizations, religions, or the like regardless of the targets' races.
Creatures that fail the saving throw or choose to forego it also gain the effects of the
instigator's raging song whenever they attack the target of their hatred, for as long as the
_[foster hatred](ref/spell/foster-hatred)_ effect lasts; however, they do not gain the effects of
the instigator's rage powers when they're under the effects of raging song in this way.

This ability replaces dirge of doom.

## Revolutionary Heart (Su) {#revolutionary-heart}

At 7th level, an instigator's tumultuous mastery of demagoguery and revolution makes it difficult
for others' compulsions to sway him. Once per day, when he fails a saving throw against a compulsion
effect, he can attempt another saving throw after 1 time increment (1 round if the effect is
measured in rounds, 1 minute if the effect is measured in minutes, 10 minutes if the spell is
measured in 10-minute increments, and so on). Every 6 skald levels thereafter, he gains an
additional daily use of this ability (to a maximum of 3 per day at 19th level).

This ability replaces lore master.
