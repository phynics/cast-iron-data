+++
id = "ref/arc-warpriest/fist-of-the-godclaw"
kind = "archetype"
title = "Fist of the Godclaw"
aon = "ArchetypeDisplay.aspx?FixedName=Warpriest%20Fist%20of%20the%20Godclaw"
source_ids = ["disciples-doctrine"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "fist_of_the_godclaw", path = "json/archetypes_warpriest.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/warpriest" },
]
[[sources]]
publication = "disciples-doctrine"
page = "12"

[fields]
kind = "archetype"
features = [
  { anchor = "deities" },
  { anchor = "blessings-of-the-godclaw", level = 1 },
  { anchor = "detect-chaos", level = 3 },
  { anchor = "alignment-channel", level = 6 },
  { anchor = "aspect-of-law", level = 20 },
]
trades = [
  { replaces = "Bonus feat gained at 3rd level", feature = "bonus-feats", levels = [3], by = ["detect-chaos"] },
  { replaces = "Bonus feats gained at 6th level and 12th level", feature = "bonus-feats", levels = [6, 12], by = ["alignment-channel"] },
  { replaces = "Aspect of war", feature = "aspect-of-war", by = ["aspect-of-law"] },
  { alters = "Blessings", feature = "blessings", by = ["blessings-of-the-godclaw"] },
  { alters = "Alignment restriction" },
]
+++

Devoted to the divine control of law above all else, these zealots seek to establish absolute order.
Disciplined and precise, they lead their allies against the chaotic hordes.

## Alignment {#alignment}

A fist of the Godclaw must be of a lawful alignment.

This alters the warpriest's alignment restriction.

## Deities {#deities}

A fist of the Godclaw must worship [Abadar](ref/faith/abadar), [Asmodeus](ref/faith/asmodeus),
[Iomedae](ref/faith/iomedae), [Irori](ref/faith/irori), or [Torag](ref/faith/torag). Alternatively,
the fist of the Godclaw must venerate the pantheon of these deities known as the Godclaw.

## Blessings of the Godclaw (Ex) {#blessings-of-the-godclaw}

A fist of the [Godclaw](ref/blessing/godclaw) must select the [Law](ref/blessing/law) blessing and
the Godclaw blessing (see below).

This alters blessings.

## Detect Chaos (Sp) {#detect-chaos}

At 3rd level, a fist of the Godclaw can cast _[detect chaos](ref/spell/detect-chaos)_ three times
per day as a [spell-like ability](ref/umr/spell-like-abilities), using his warpriest level as his
caster level. If the fist of the Godclaw already has, or later gains, the ability to cast
_[detect chaos](ref/spell/detect-chaos)_, then he can cast _[detect chaos](ref/spell/detect-chaos)_
at will as a spell-like ability.

This replaces the bonus feat gained at 3rd level.

## Alignment Channel (Su) {#alignment-channel}

At 6th level, a fist of the Godclaw gains [Alignment Channel](ref/feat/alignment-channel) as a bonus
feat. When he uses this feat and spends fervor to channel energy, he can harm only outsiders with
the chaotic subtype. Additionally, when using this feat, he expends only one use of his fervor to
channel energy and deals 1d6 points of damage for every 2 warpriest levels he has. At 12th level, a
fist of the Godclaw can expend an additional use of fervor to channel energy as a move action.

This replaces the bonus feats gained at 6th level and 12th level.

## Aspect of Law (Ex) {#aspect-of-law}

At 20th level, a fist of the Godclaw can channel an aspect of law, growing even more inflexible.
Once per day as a swift action, a warpriest can treat his level as his base attack bonus, gains DR
20/chaotic, and becomes immune to mind-affecting effects. In addition, he can take the average
result on any die roll instead of rolling normally. This ability lasts for 1 minute.

This replaces aspect of war.
