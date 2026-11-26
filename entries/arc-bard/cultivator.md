+++
id = "ref/arc-bard/cultivator"
kind = "archetype"
title = "Cultivator"
aon = "ArchetypeDisplay.aspx?FixedName=Bard%20Cultivator"
source_ids = ["ultimate-wilderness"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "cultivator", path = "json/archetypes_bard.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/bard" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "40"

[fields]
kind = "archetype"
features = [
  { anchor = "plant-magic" },
  { anchor = "verdant-voice", level = 1 },
  { anchor = "song-of-growth", level = 1 },
  { anchor = "resist-nature-s-lure", level = 2 },
  { anchor = "nature-lore", level = 5 },
]
trades = [
  { replaces = "Bardic knowledge", feature = "bardic-knowledge", by = ["verdant-voice"] },
  { replaces = "Countersong", feature = "bardic-performance", power = "countersong", by = ["song-of-growth"] },
  { replaces = "Well-versed", feature = "well-versed", by = ["resist-nature-s-lure"] },
  { alters = "The bard's spells", feature = "spells", by = ["plant-magic"] },
  { alters = "Lore master", feature = "lore-master", by = ["nature-lore"] },
]
+++

Cultivators use music to promote plant growth and influence the behavior of plants both naturally
and supernaturally. Most cultivators work in conjunction with local communities to maintain crops
and oversee harvests, while others serve as wardens of unspoiled natural wonders.

## Class Skills {#class-skills}

A cultivator gains Survival as a class skill.

This alters the bard's class skills.

## Plant Magic {#plant-magic}

A cultivator bard adds the following spells to his bard spell list at the corresponding spell
levels: _[entangle](ref/spell/entangle)_ (1st), _[greensight](ref/spell/greensight)_ (2nd),
_[plant growth](ref/spell/plant-growth)_ (3rd), _[antiplant shell](ref/spell/antiplant-shell)_
(4th), _[tree stride](ref/spell/tree-stride)_ (5th), _[green caress](ref/spell/green-caress)_ (6th).

This alters the bard's spells.

## Verdant Voice {#verdant-voice}

By combining traditional [Green Faith](ref/faith/green-faith) chants and fey songs into his bardic
performance, a cultivator gains the ability to affect a creature of the plant type with
mind-affecting bardic performances. However, doing so requires the cultivator to expend 1 additional
round of bardic performance each round he maintains a performance augmented by verdant voice.

This replaces bardic knowledge.

## Song of Growth (Su) {#song-of-growth}

A cultivator can spontaneously promote massive plant growth with his bardic performance. While he
maintains his song of growth, the cultivator can spend a standard action to select one side of a
square within 30 feet of himself and instantly create an opaque barrier of plant matter to block
that face, providing total [cover](ref/rule/cover). He can create one barrier as part of starting
his bardic performance if he starts the performance as a standard action. The side the cultivator
selects must be supported by the ground, and the growth itself cannot support more than 5 pounds of
weight. The conjured barrier has [hardness](ref/umr/hardness) 0, AC 5, and 2 hit points per bard
level. A cultivator can maintain a number of plant growths equal to his Charisma modifier +
[half](ref/misc/fractions-and-rounding) his bard level. These barriers immediately crumble to dust
when the cultivator ends his performance.

This performance replaces countersong.

## Resist Nature's Lure (Ex) {#resist-nature-s-lure}

At 2nd level, a cultivator gains [resist nature's lure](ref/ability/resist-natures-lure), as the
druid class feature of the same name, but with only a +2 bonus instead of +4. This increases to a +4
bonus at 4th level.

This replaces well-versed.

## Nature Lore (Ex) {#nature-lore}

At 5th level, the cultivator gains the lore master bard ability, except he can use it only on
Knowledge (nature) checks and Survival checks to track creatures in natural environments.

This alters lore master.
