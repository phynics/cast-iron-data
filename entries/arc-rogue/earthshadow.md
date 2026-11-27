+++
id = "ref/arc-rogue/earthshadow"
kind = "archetype"
title = "Earthshadow"
aon = "ArchetypeDisplay.aspx?FixedName=Rogue%20Earthshadow"
source_ids = ["elemental-masters-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "earthshadow", path = "json/archetypes_rogue.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/rogue" },
]
[[sources]]
publication = "elemental-masters-handbook"
page = "8"

[fields]
kind = "archetype"
features = [
  { anchor = "earthlink", level = 1 },
  { anchor = "earthcraft", level = 2 },
]
trades = [
  { replaces = "Trapfinding", feature = "trapfinding", by = ["earthlink"] },
  { replaces = "Evasion", feature = "evasion", by = ["earthcraft"] },
  { replaces = "rogue talents gained at 4th, 8th, 12th, and 16th levels", feature = "rogue-talents", levels = [4, 8, 12, 16], by = ["earthcraft"] },
]
+++

When the dwarves began their Quest for Sky millennia ago to reach the world's surface, they already
had a deep understanding of the earth's secrets. In the centuries since, the mystic lore the dwarves
call earthcraft has been passed down through the generations, and its practitioners are called
earthshadows. While many earthshadows are dwarves, their secrets have been shared with a worthy few
members of other races over the ages.

## Earthlink (Su) {#earthlink}

The earth grants an earthshadow swiftness and hones her senses. When an earthshadow is in direct
contact with an expanse of natural earth or unworked stone that is at least as large as she is, she
adds half her rogue level (minimum 1) to Acrobatics and Perception checks.

This replaces trapfinding.

## Earthcraft (Su) {#earthcraft}

At 2nd level, an earthshadow can draw upon the power of earth to perform mystical tricks. At the
start of each day, an earthshadow gains a pool of earthcraft points equal to half her rogue level
plus her Wisdom modifier, and she can spend earthcraft points to use certain
[spell-like abilities](ref/umr/spell-like-abilities). The caster level of these spell-like abilities
is equal to the earthshadow's rogue level. Earthcraft effects affect only the earthshadow, even if
the spell could normally affect others. She can spend 1 earthcraft point to cast
_[blend](ref/spell/blend)_, even if she is not an elf, but this ability works only in areas of
natural earth or unworked stone.

At 4th level, an earthshadow can spend 2 earthcraft points to cast
_[meld into stone](ref/spell/meld-into-stone)_.

At 8th level, an earthshadow can spend 3 earthcraft points to cast
_[dimension door](ref/spell/dimension-door)_. She must be able to see her destination (or she must
be able to otherwise sense its surface, such as with [tremorsense](ref/umr/tremorsense)), and her
current location must be connected to her destination by continuous natural earth or unworked stone.

At 12th level, an earthshadow can spend 5 earthcraft points to cast the spell
_[stone tell](ref/spell/stone-tell)_ but can communicate only with unworked stone.

At 16th level, an earthshadow can spend 6 earthcraft points to cast _[statue](ref/spell/statue)_.

This ability replaces evasion and the rogue talents gained at 4th, 8th, 12th, and 16th levels.

## Rogue Talents {#rogue-talents}

The following rogue talents complement the earthshadow archetype: extra earthcraft (see below),
favored terrain, fortified position (see below), major magic, minor magic, resiliency, and trap
spotter.

## Advanced Talents {#advanced-talents}

The following advanced rogue talents complement the earthshadow archetype: against the wall (see
below), dispelling attack, hide in plain sight, slippery mind, and stony skin (see below).
