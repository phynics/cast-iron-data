+++
id = "ref/arc-alchemist/psychonaut"
kind = "archetype"
title = "Psychonaut"
aon = "ArchetypeDisplay.aspx?FixedName=Alchemist%20Psychonaut"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "psychonaut", path = "json/archetypes_alchemist2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/alchemist" },
]
[[sources]]
publication = "ultimate-magic"
page = "19"

[fields]
kind = "archetype"
features = [
  { anchor = "bomb" },
  { anchor = "precognition", level = 5 },
  { anchor = "psychic-senses", level = 8 },
  { anchor = "remote-consciousness", level = 10 },
  { anchor = "greater-precognition", level = 15 },
  { anchor = "master-precognition", level = 17 },
]
trades = [
  { replaces = "Bombs", feature = "bomb", by = ["bomb"] },
  { replaces = "Poison resistance +4", feature = "poison-resistance", levels = [5], by = ["precognition"] },
  { replaces = "Poison resistance +6", feature = "poison-resistance", levels = [8], by = ["psychic-senses"] },
  { replaces = "Poison immunity", feature = "poison-resistance", levels = [10], by = ["remote-consciousness"] },
  { replaces = "Increase to bomb damage at this level", by = ["greater-precognition", "master-precognition"] },
]
+++

A psychonaut uses his knowledge to explore altered states of consciousness and even other planes of
existence. A psychonaut has the following class features.

## Bomb {#bomb}

A psychonaut's bombs deal damage [one die step](ref/misc/damage-die-adjustments) lower than normal
(regular bombs deal d4s, [concussive bombs](ref/discovery/concussive-bomb) deal 1d3s, and so on).
This ability otherwise functions as and replaces the standard alchemist bomb class feature.

## Precognition {#precognition}

At 5th level, a psychonaut adds _[augury](ref/spell/augury)_ to his formula book as a 2nd-level
extract (this extract does not require a divine focus component). This replaces poison resistance
+4.

## Psychic Senses {#psychic-senses}

At 8th level, a psychonaut adds
_[clairaudience/clairvoyance](ref/spell/clairaudience-clairvoyance)_,
_[detect scrying](ref/spell/detect-scrying)_, _[scrying](ref/spell/scrying)_, and
_[speak with dead](ref/spell/speak-with-dead)_ to his formula book as 3rd-level extracts (a
_[scrying](ref/spell/scrying)_ extract does not require a focus or divine focus component). When a
psychonaut uses a _[speak with dead](ref/spell/speak-with-dead)_ extract, he gains the power to hear
the lingering spirit within a corpse rather than enabling the corpse to audibly speak, but the
extract otherwise works as the spell. This ability replaces poison resistance +6.

## Remote Consciousness {#remote-consciousness}

At 10th level, a psychonaut adds _[dream](ref/spell/dream)_,
_[lesser astral projection](ref/spell/astral-projection-lesser)_,
_[nightmare](ref/spell/nightmare)_, _[plane shift](ref/spell/plane-shift)_,
_[sending](ref/spell/sending)_, and _[telepathic bond](ref/spell/telepathic-bond)_ to his formula
book as 4th-level extracts (a _[plane shift](ref/spell/plane-shift)_ extract does not require a
focus component). This ability replaces poison immunity.

## Greater Precognition {#greater-precognition}

At 15th level, a psychonaut adds _[moment of prescience](ref/spell/moment-of-prescience)_ to his
formula book as a 5th-level extract. This ability replaces the increase to bomb damage at this
level.

## Master Precognition {#master-precognition}

At 17th level, a psychonaut adds _[foresight](ref/spell/foresight)_ to his formula book as a
6th-level extract. This ability replaces the increase to bomb damage at this level.

## Discoveries {#discoveries}

The following discoveries complement the psychonaut archetype:
[confusion bomb](ref/discovery/confusion-bomb), [eternal potion](ref/discovery/eternal-potion),
[extend potion](ref/discovery/extend-potion), [lingering spirit](ref/discovery/lingering-spirit),
and [madness bomb](ref/discovery/madness-bomb).
