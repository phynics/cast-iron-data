+++
id = "ref/arc-skald/twilight-speaker"
kind = "archetype"
title = "Twilight Speaker"
aon = "ArchetypeDisplay.aspx?FixedName=Skald%20Twilight%20Speaker"
source_ids = ["heroes-from-the-fringe"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "twilight_speaker", path = "json/archetypes_skald.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/skald" },
]
[[sources]]
publication = "heroes-from-the-fringe"
page = "12"

[fields]
kind = "archetype"
features = [
  { anchor = "devout" },
  { anchor = "twilight-envoy", level = 1 },
  { anchor = "inspired-devotion" },
  { anchor = "song-of-understanding", level = 6 },
  { anchor = "song-of-secrecy", level = 10 },
  { anchor = "community-domain", level = 2 },
  { anchor = "findeladlara-s-blessing", level = 7 },
  { anchor = "findeladlara-s-hand", level = 20 },
]
trades = [
  { replaces = "Bardic knowledge", feature = "bardic-knowledge", by = ["twilight-envoy"] },
  { replaces = "Inspired rage", feature = "inspired-rage", by = ["song-of-secrecy"] },
  { replaces = "song of strength", feature = "song-of-strength", by = ["song-of-secrecy"] },
  { replaces = "dirge of doom", feature = "dirge-of-doom", by = ["song-of-secrecy"] },
  { replaces = "Versatile performance", feature = "versatile-performance", by = ["community-domain"] },
  { replaces = "well-versed", feature = "well-versed", by = ["community-domain"] },
  { replaces = "Lore master", feature = "lore-master", by = ["findeladlara-s-blessing"] },
  { replaces = "Master skald", feature = "master-skald", by = ["findeladlara-s-hand"] },
]
+++

From the extraordinarily reclusive Snowcaster elves come the twilight speakers, who consider it a
sacred duty to seek out and befriend non-elven communities. These elves travel among outsiders as
envoys, diplomats, traders, and even spies as events demand. Deeply devoted to the elven goddess
Findeladlara (_Pathfinder Campaign Setting: Inner Sea Gods_ 183), twilight speakers wander far and
wide, vigilant for threats to their homes and their people.

Twilight speaker is a skald archetype that is available only to elves.

## Devout {#devout}

A twilight speaker must worship the elven goddess [Findeladlara](ref/faith/findeladlara), and his
alignment must be within one step of chaotic good. A twilight speaker who does not meet these
requirements cannot use inspired devotion or Findeladlara's blessing.

## Twilight Envoy {#twilight-envoy}

A twilight speaker gains a bonus equal to half his skald level on Bluff, Diplomacy, and Sense Motive
checks.

This replaces bardic knowledge.

## Raging Song (Su) {#raging-song}

A twilight speaker gains the following raging songs.

## Inspired Devotion (Su) {#inspired-devotion}

The twilight speaker inspires fervor rather than fury. Affected allies gain a +1 competence bonus on
attack rolls and a +1 morale bonus on saving throws. At 6th, 12th, and 18th levels, these bonuses
increase by 1.

## Song of Understanding (Su) {#song-of-understanding}

At 6th level, a twilight speaker can use his raging song to create an aura that allows creatures to
speak and understand each others' languages. By expending 4 rounds of raging song, the twilight
speaker creates an aura that grants him and creatures in a 60-foot [spread](ref/misc/spread)
centered on him the effects of _[tongues](ref/spell/tongues)_. This aura uses the skald's level as
the caster level for all purposes, including duration. A twilight speaker can dismiss this aura as a
standard action.

## Song of Secrecy (Su) {#song-of-secrecy}

At 10th level, a twilight speaker can use his song to shroud allies from detection. Affected allies
gain a bonus equal to half the twilight speaker's skald level on Stealth checks, and they can
attempt such checks without [cover](ref/rule/cover) or [concealment](ref/rule/concealment). Song of
secrecy is audible only to those affected.

This replaces inspired rage, song of strength, and dirge of doom.

## Community Domain {#community-domain}

At 2nd level, a twilight speaker gains the Community domain and gains the powers and spells of the
domain. He treats his skald level as his cleric level, and he uses his Charisma modifier in place of
his Wisdom modifier for the purposes of the domain's abilities.

This replaces versatile performance and well-versed.

## Findeladlara's Blessing (Su) {#findeladlara-s-blessing}

At 7th level, once per day a twilight speaker can activate any spell trigger or spell completion
item as though the spell were on the skald spell list. He can use this ability an additional time
per day at 13th and 19th levels.

This ability replaces lore master.

## Findeladlara's Hand {#findeladlara-s-hand}

At 20th level, the twilight speaker can use Findeladlara's blessing at will.

This replaces master skald.
