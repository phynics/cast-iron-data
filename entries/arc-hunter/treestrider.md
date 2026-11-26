+++
id = "ref/arc-hunter/treestrider"
kind = "archetype"
title = "Treestrider"
aon = "ArchetypeDisplay.aspx?FixedName=Hunter%20Treestrider"
source_ids = ["ultimate-wilderness"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "treestrider", path = "json/archetypes_hunter.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/hunter" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "55"

[fields]
kind = "archetype"
features = [
  { anchor = "animal-companion", level = 1 },
  { anchor = "brachiation", level = 1 },
  { anchor = "improved-unarmed-strike", level = 2 },
  { anchor = "tree-stride", level = 10 },
]
trades = [
  { replaces = "Animal focus", feature = "animal-focus", by = ["brachiation"] },
  { replaces = "second animal focus", feature = "second-animal-focus", by = ["brachiation"] },
  { replaces = "Precise companion", feature = "precise-companion", by = ["improved-unarmed-strike"] },
  { replaces = "Raise animal companion", feature = "raise-animal-companion", by = ["tree-stride"] },
  { alters = "Animal companion", feature = "animal-companion", by = ["animal-companion"] },
]
+++

Some hunters are masters of the wild. Whether raised by apes or having some other link with simian
creatures, these hunters glide through the wilderness with ease.

## Animal Companion {#animal-companion}

As a free action, a treestrider must select an [ape](ref/companion/ape) as her animal companion.

This alters animal companion.

## Brachiation (Ex) {#brachiation}

A treestrider can gain a climb speed equal to half her base speed as a free action for 1 minute per
hunter level per day. This duration must be spent in 1-minute increments. In addition, she can use
her climb speed to move through the canopies of forests or jungles, provided the limbs of the trees
are strong enough to support her weight. The treestrider's companion gains a +10-foot enhancement
bonus to its climb speed. At 8th level, the treestrider's climb speed increases to equal her base
speed, the duration of her brachiation increases to 10 minutes per hunter level per day (usable in
10-minute increments), and the enhancement bonus to her companion's climb speed increases to +20
feet. At 15th level, she can use brachiation with no limit on the duration.

This replaces animal focus and second animal focus.

## Improved Unarmed Strike (Ex) {#improved-unarmed-strike}

At 2nd level, a treestrider gains [Improved Unarmed Strike](ref/feat/improved-unarmed-strike) as a
bonus feat.

This replaces precise companion.

## Tree Stride (Sp) {#tree-stride}

At 10th level, a treestrider can use a full-round action to move between two trees, as per the spell
_[tree stride](ref/spell/tree-stride)_. Unlike the spell, this ability has a duration of
instantaneous and the treestrider can make only a single transfer. She can bring her animal
companion with her, but if she does, her companion can't take any actions that round. Tree stride
can be used a number of times per day equal to 3 + the hunter's Wisdom modifier.

This replaces raise animal companion.
