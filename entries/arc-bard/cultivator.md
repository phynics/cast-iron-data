+++
id = "ref/arc-bard/cultivator"
kind = "archetype"
title = "Cultivator"
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
replaces = ["Bardic knowledge", "Countersong", "Well-versed"]
alters = ["The bard's spells", "Lore master"]
+++

Cultivators use music to promote plant growth and influence the behavior of plants both naturally
and supernaturally. Most cultivators work in conjunction with local communities to maintain crops
and oversee harvests, while others serve as wardens of unspoiled natural wonders.

**Gained class skills:** sur

**Plant Magic**

**Alters:** The bard's spells

**Info:** A cultivator bard adds the following spells to his bard spell list at the corresponding
spell levels: [entangle](ref/spell/entangle) (1st), [greensight](ref/spell/greensight) (2nd),
[plant growth](ref/spell/plant-growth) (3rd), [antiplant shell](ref/spell/antiplant-shell) (4th),
[tree stride](ref/spell/tree-stride) (5th), [green caress](ref/spell/green-caress) (6th).

**Verdant Voice**

**Ability:** By combining traditional [Green Faith](ref/faith/green-faith) chants and fey songs into
his bardic performance, a cultivator gains the ability to affect a creature of the plant type with
mind-affecting bardic performances. However, doing so requires the cultivator to expend 1 additional
round of bardic performance each round he maintains a performance augmented by _verdant voice._

**Replaces:** Bardic knowledge

**Song of Growth (Su)**

**Flavor:** A cultivator can spontaneously promote massive plant growth with his bardic performance.

**Replaces:** Countersong

**Special:** A cultivator can maintain a number of plant growths equal to his Charisma modifier +
[half](ref/misc/fractions-and-rounding) his bard level. These barriers immediately crumble to dust
when the cultivator ends his performance.

**Standard:** While he maintains his _song of growth,_ the cultivator can select one side of a
square within 30 feet of himself and instantly create an opaque barrier of plant matter to block
that face, providing total [cover](ref/rule/cover). He can create one barrier as part of starting
his bardic performance if he starts the performance as a standard action. The side the cultivator
selects must be supported by the ground, and the growth itself cannot support more than 5 pounds of
weight. The conjured barrier has [hardness](ref/umr/hardness) 0, AC 5, and 2 hit points per bard
level.

**Resist Nature's Lure (Ex)**

**At 4th Level:** This increases to a +4 bonus.

**Gained:** At 2nd Level

**Passive:** A cultivator gains [resist nature's lure](ref/ability/resist-natures-lure), as the
druid class feature of the same name, but with only a +2 bonus instead of +4.

**Replaces:** Well-versed

**Nature Lore (Ex)**

**Ability:** The cultivator gains the _lore master_ bard ability, except he can use it only on
Knowledge (nature) checks and Survival checks to track creatures in natural environments.

**Alters:** Lore master

**Gained:** At 5th Level
