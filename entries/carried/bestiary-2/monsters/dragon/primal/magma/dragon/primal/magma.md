+++
id = "ref/carried/bestiary-2/monsters/dragon/primal/magma/dragon/primal/magma"
kind = "creature"
title = "Dragon, Primal, Magma"
source_ids = ["bestiary-2"]
section = ["Monsters", "Dragon", "Primal", "Magma", "Dragon", "Primal"]
tags = ["tiny"]
provenance = [
  { dataset = "psrd-data", record = "pfsrd://Bestiary 2/Monsters/Dragon/Primal/Magma/Dragon/Primal/Magma", path = "bestiary_2/creature/dragon_primal_magma.json" },
]

[fields]
kind = "creature"
cr = "4"
size = "Tiny"
abilities = ["13", "16", "13", "12", "12", "11"]
+++

::: statblock
CR: 4
Size: Tiny
Race: cn dragon (extraplanar, fire)
Hit Dice: 5d12
Speed: 40 ft.
Ability Scores: Str 13, Dex 16, Con 13, Int 12, Wis 12, Cha 11
Environment: any mountains or underground (Plane of Fire)
Organization: solitary
Treasure: triple
Natural Armor: +4
Breath Weapon: cone, 2d6 fire
:::

## Special Abilities {#special-abilities}

### Magma Tomb {#magma-tomb}

::: statblock
Ability Type: Supernatural
:::

Once per day, a great wyrm magma dragon can spit lava onto a target within 120 feet, dealing damage
normally for its breath weapon. This magma cools instantly—it does not continue doing damage at this
point but does entrap the victim (see universal monster rules in appendix; DC equals the dragon's
breath weapon save DC, 3d6 minutes, [hardness](ref/umr/hardness) 8, hp 45).

### Magma Breath {#magma-breath}

::: statblock
Ability Type: Supernatural
:::

Three times per day, an ancient or older magma dragon can breathe a cone of lava instead of fire.
The damage is unchanged, but the magma clings to those it damages, dealing half damage each round
thereafter for 1d3 rounds. After this magma cools, it crumbles to dust.

### Spell-Like Abilities {#spell-like-abilities}

::: statblock
Ability Type: Spell-Like
:::

A magma dragon gains the following [spell-like abilities](ref/umr/spell-like-abilities), usable at
will (unless indicated otherwise) on reaching the listed age category. Very young—burning hands;
Juvenile—scorching ray; Adult—wall of fire; Old—fire shield (warm shield, constant); Ancient—delayed
blast fireball (3/day); Great wyrm—wall of lava.

### Superheated {#superheated}

::: statblock
Ability Type: Supernatural
:::

At young age and older, a magma dragon's bite attack deals additional fire damage equal to its age
category.

## Table: Magma Special Abilities {#table-magma-special-abilities}

::: table
caption = "Table: Magma Special Abilities"
head = [
  [
    { text = "Age Category", header = true },
    { text = "Special Abilities", header = true },
    { text = "Caster Level", header = true },
  ],
]
body = [
  [
    { text = "Wyrmling" },
    { text = "Immune to fire, vulnerable to cold" },
    { text = "—" },
  ],
  [
    { text = "Very young" },
    { text = "_[Burning hands](ref/spell/burning-hands)_" },
    { text = "—" },
  ],
  [
    { text = "Young" },
    { text = "Superheated" },
    { text = "1st" },
  ],
  [
    { text = "Juvenile" },
    { text = "_[Scorching ray](ref/spell/scorching-ray)_" },
    { text = "3rd" },
  ],
  [
    { text = "Young adult" },
    { text = "DR 5/magic, [spell resistance](ref/rule/spell-resistance)" },
    { text = "5th" },
  ],
  [
    { text = "Adult" },
    { text = "Frightful presence, _[wall of fire](ref/spell/wall-of-fire)_" },
    { text = "7th" },
  ],
  [
    { text = "Mature adult" },
    { text = "DR 10/magic" },
    { text = "9th" },
  ],
  [
    { text = "Old" },
    { text = "_[Fire shield](ref/spell/fire-shield)_" },
    { text = "11th" },
  ],
  [
    { text = "Very old" },
    { text = "DR 15/magic" },
    { text = "13th" },
  ],
  [
    { text = "Ancient" },
    { text = "Magma breath, _[delayed blast fireball](ref/spell/delayed-blast-fireball)_" },
    { text = "15th" },
  ],
  [
    { text = "Wyrm" },
    { text = "DR 20/magic" },
    { text = "17th" },
  ],
  [
    { text = "Great wyrm" },
    { text = "Magma tomb, _[wall of lava](ref/spell/wall-of-lava)_" },
    { text = "19th" },
  ],
]
:::
