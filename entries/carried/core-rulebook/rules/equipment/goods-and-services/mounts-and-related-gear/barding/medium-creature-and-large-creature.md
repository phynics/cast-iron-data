+++
id = "ref/carried/core-rulebook/rules/equipment/goods-and-services/mounts-and-related-gear/barding/medium-creature-and-large-creature"
kind = "item"
title = "Barding, Medium Creature and Large Creature"
source_ids = ["core-rulebook"]
section = ["Rules", "Equipment", "Goods And Services", "Mounts and Related Gear", "Barding"]
tags = ["mounts and related gear"]
provenance = [
  { dataset = "psrd-data", record = "pfsrd://Core Rulebook/Rules/Equipment/Goods And Services/Mounts and Related Gear/Barding/Medium Creature and Large Creature", path = "core_rulebook/item/barding_medium_creature_and_large_creature.json" },
]

[fields]
kind = "item"
category = "Mounts and Related Gear"
attributes = [
  { label = "Gear Type", value = "Mounts and Related Gear" },
  { label = "Large Creature: Price", value = "×42" },
  { label = "Large Creature: Weight", value = "×22" },
  { label = "Medium Creature: Price", value = "×22" },
  { label = "Medium Creature: Weight", value = "×12" },
]
+++

::: statblock
Gear Type: Mounts and Related Gear
Large Creature\: Price: ×42
Large Creature\: Weight: ×22
Medium Creature\: Price: ×22
Medium Creature\: Weight: ×12
:::

Barding is a type of armor that covers the head, neck, chest, body, and possibly legs of a horse or
other mount. Barding made of medium or heavy armor provides better protection than light barding,
but at the expense of speed. Barding can be made of any of the armor types found on Table: Armor and
Shields.

Armor for a horse (a Large nonhumanoid creature) costs four times as much as human armor (a Medium
humanoid creature) and also weighs twice as much (see Table: Armor for Unusual Creatures). If the
barding is for a pony or other Medium mount, the cost is only double, and the weight is the same as
for Medium armor worn by a humanoid. Medium or heavy barding slows a mount that wears it, as shown
on the table below.

Flying mounts can't fly in medium or heavy barding.

Removing and fitting barding takes five times as long as the figures given on Table: Donning Armor.
A barded animal cannot be used to carry any load other than a rider and normal saddlebags.

## Barding {#barding}

::: table
head = [
  [
    { text = "Barding", header = true, rowspan = 2 },
    { text = "Modifier", header = true, colspan = 3 },
  ],
  [
    { text = "(40 ft.)", header = true },
    { text = "(50 ft.)", header = true },
    { text = "(60 ft.)", header = true },
  ],
]
body = [
  [
    { text = "Medium" },
    { text = "30 ft." },
    { text = "35 ft." },
    { text = "40 ft." },
  ],
  [
    { text = "Heavy" },
    { text = "30 ft.\\*" },
    { text = "35 ft.\\*" },
    { text = "40 ft.\\*" },
  ],
]
foot = [
  [
    { text = "\\* A mount wearing heavy armor moves at only triple its normal speed when running instead of quadruple.", colspan = 4 },
  ],
]
:::
