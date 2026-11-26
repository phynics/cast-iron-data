+++
id = "ref/arc-druid/draconic-druid"
kind = "archetype"
title = "Draconic Druid"
aon = "ArchetypeDisplay.aspx?FixedName=Druid%20Draconic%20Druid"
source_ids = ["legacy-of-dragons"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "draconic_druid", path = "json/archetypes_druid.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/druid" },
]
[[sources]]
publication = "legacy-of-dragons"
page = "24"

[fields]
kind = "archetype"
features = [
  { anchor = "drake-companion", level = 1 },
  { anchor = "dragon-sense", level = 1 },
  { anchor = "resist-dragon-s-might" },
  { anchor = "dragon-shape" },
]
trades = [
  { replaces = "Nature bond", feature = "nature-bond", by = ["drake-companion"] },
  { replaces = "wild empathy", feature = "wild-empathy", by = ["drake-companion"] },
  { replaces = "woodland stride", feature = "woodland-stride", by = ["drake-companion"] },
  { replaces = "venom immunity", feature = "venom-immunity", by = ["drake-companion"] },
  { replaces = "a thousand faces", feature = "a-thousand-faces", by = ["drake-companion"] },
  { replaces = "timeless body", feature = "timeless-body", by = ["drake-companion"] },
  { replaces = "Nature sense", feature = "nature-sense", by = ["dragon-sense"] },
  { replaces = "Resist nature's lure", feature = "resist-nature-s-lure", by = ["resist-dragon-s-might"] },
]
+++

Some druids believe that dragons are the ultimate expression of nature, combining elemental fury
with majestic beauty. These druids consort with dragons and eventually transform into draconic
forms.

## Drake Companion {#drake-companion}

A draconic druid gains a [drake companion](ref/sidekick/drake) instead of an animal companion.

This ability replaces nature bond, wild empathy, woodland stride, venom immunity, a thousand faces,
and timeless body.

## Dragon Sense {#dragon-sense}

A draconic druid studies dragons and their history. She gains a +2 bonus on Knowledge (arcana) and
Knowledge (history) checks.

This ability replaces nature sense.

## Resist Dragon's Might {#resist-dragon-s-might}

A draconic druid gains a +4 bonus on saving throws against the spells,
[spell-like abilities](ref/umr/spell-like-abilities), and supernatural abilities of dragons.

This ability replaces resist nature's lure.

## Dragon Shape {#dragon-shape}

A draconic druid can't use wild shape to change into any of the usual forms available to a druid.
Instead, at 4th level, she can use wild shape to change into a dragon-scaled version of herself with
long fangs, gaining a +1 natural armor bonus to her AC and a [bite attack](ref/umr/natural-attacks)
appropriate for her size (1d6 points of damage for a Medium druid) but otherwise retaining her usual
form. At 10th level, she can spend two uses of wild shape to transform into a Medium dragon as per
_[form of the dragon I](ref/spell/form-of-the-dragon-1)_, and at 12th level, she can spend two uses
to change into a Large dragon as per _[form of the dragon II](ref/spell/form-of-the-dragon-2)_. Each
time that a draconic druid uses wild shape counts as a separate casting of the spell for the purpose
of refreshing her uses of her breath weapon.
