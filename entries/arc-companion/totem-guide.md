+++
id = "ref/arc-companion/totem-guide"
kind = "archetype"
title = "Totem Guide"
source_ids = ["ultimate-wilderness", "animal-archive"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "totem_guide", path = "json/archetypes_COMPANION.json" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "189"
[[sources]]
publication = "animal-archive"
page = "21"

[fields]
kind = "archetype"
features = [
  { anchor = "spiritual-guidance", level = 3 },
  { anchor = "beast-speech", level = 6 },
  { anchor = "eldritch-claws", level = 9 },
  { anchor = "ghost-guardian", level = 15 },
]
trades = [
  { replaces = "Evasion", by = ["spiritual-guidance"] },
  { replaces = "Devotion", by = ["beast-speech"] },
  { replaces = "Multiattack", by = ["eldritch-claws"] },
  { replaces = "Improved Evasion", by = ["ghost-guardian"] },
]
+++

Totem guides embody the wisdom and spirituality of the natural world, providing guidance as well as
aid in combat. Once a totem guide is chosen, a character can replace the companion if it is slain
but must choose the same kind of totem guide.

## Spiritual Guidance (Sp) {#spiritual-guidance}

At 3rd level, a totem guide can use _[guidance](ref/spell/guidance)_ as a
[spell-like ability](ref/umr/spell-like-abilities) at will as a full-round action, targeting itself
or its master. In addition, a totem guide's master can spontaneously cast the following spells while
adjacent to the totem guide by sacrificing a spell slot of equal or higher level:
_[detect animals or plants](ref/spell/detect-animals-or-plants)_ (1st), _[augury](ref/spell/augury)_
(2nd), _[helping hand](ref/spell/helping-hand)_ (3rd), _[divination](ref/spell/divination)_ (4th),
_[commune with nature](ref/spell/commune-with-nature)_ (5th), and
_[find the path](ref/spell/find-the-path)_ (6th). The totem guide serves as a divine focus for these
spells, but costly material components must still be provided.

This replaces evasion.

## Beast Speech (Ex) {#beast-speech}

At 6th level, a totem guide can speak with its master as though the two share a common language, and
it can speak with other animals of its species (or, at the GM's discretion, other creatures with
similar types).

This replaces devotion.

## Eldritch Claws {#eldritch-claws}

At 9th level, a totem guide gains [Eldritch Claws](ref/feat/eldritch-claws) as a bonus feat.

This replaces Multiattack.

## Ghost Guardian (Ex) {#ghost-guardian}

At 15th level, a totem guide's natural weapons deal full damage to incorporeal creatures, and its
natural armor bonus applies against incorporeal touch attacks. A totem guide can never be
transformed into or animated as an undead creature.

This replaces improved evasion.
