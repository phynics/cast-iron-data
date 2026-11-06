+++
id = "ref/carried/bestiary-2/monsters/dragon/primal/umbral/umbral-dragon"
kind = "creature"
title = "Umbral Dragon"
source_ids = ["bestiary-2"]
section = ["Monsters", "Dragon", "Primal", "Umbral"]
tags = ["small"]
provenance = [
  { dataset = "psrd-data", record = "pfsrd://Bestiary 2/Monsters/Dragon/Primal/Umbral/Umbral Dragon", path = "bestiary_2/creature/umbral_dragon.json" },
]

[fields]
kind = "creature"
cr = "6"
size = "Small"
abilities = ["13", "14", "13", "14", "15", "14"]
+++

::: statblock
CR: 6
Size: Small
Race: ce dragon (extraplanar)
Hit Dice: 7d12
Speed: 40 ft.
Ability Scores: Str 13, Dex 14, Con 13, Int 14, Wis 15, Cha 14
Environment: any
Organization: solitary
Treasure: triple
Natural Armor: +6
Breath Weapon: cone, 2d8 negative energy
:::

## Special Abilities {#special-abilities}

### Breath Weapon {#breath-weapon}

::: statblock
Ability Type: Supernatural
:::

Although it deals negative energy damage, an umbral dragon's breath weapon does not heal undead
creatures.

### Create Shadows {#create-shadows}

::: statblock
Ability Type: Supernatural
:::

Any creature slain by an ancient or older umbral dragon rises as a shadow (if 8 HD or less) or
greater shadow (if above 8 HD) under the umbral dragon's control 1d4 rounds later.

### Energy Drain {#energy-drain}

::: statblock
Ability Type: Supernatural
:::

A great wyrm umbral dragon deals 1 negative level with each successful bite or claw attack (1 level,
DC 32).

### Ghost Bane {#ghost-bane}

::: statblock
Ability Type: Supernatural
:::

A young or older umbral dragon's physical attacks deal damage to incorporeal creatures normally.

### Umbral Scion {#umbral-scion}

::: statblock
Ability Type: Extraordinary
:::

Umbral dragons have negative energy affinity and are immune to energy drain and death effects.

### Shadow Breath {#shadow-breath}

::: statblock
Ability Type: Supernatural
:::

Three times per day, an adult or older umbral dragon can breathe a cone of shadows. Creatures who
fail a Fortitude save are blinded for 1d4 rounds and take 1 point of Str drain per age category
possessed by the dragon. A successful save negates the blindness and reduces Str drain to 1d4
points.

### Spell-Like Abilities {#spell-like-abilities}

::: statblock
Ability Type: Spell-Like
:::

An umbral dragon gains the following [spell-like abilities](ref/umr/spell-like-abilities), usable at
will (unless indicated otherwise) on reaching the listed age category. Young—darkness;
Juvenile—vampiric touch; Adult—shadow walk; Old—project image; Ancient—finger of death (3/day),
Great wyrm—shades. An umbral dragon can cast cleric spells as arcane spells.

## Table: Umbral Special Abilities {#table-umbral-special-abilities}

::: table
caption = "Table: Umbral Special Abilities"
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
    { text = "Umbral scion, immune to cold" },
    { text = "—" },
  ],
  [
    { text = "Very young" },
    { text = "_[Darkness](ref/spell/darkness)_" },
    { text = "—" },
  ],
  [
    { text = "Young" },
    { text = "Ghost bane" },
    { text = "1st" },
  ],
  [
    { text = "Juvenile" },
    { text = "Frightful presence, _[vampiric touch](ref/spell/vampiric-touch)_" },
    { text = "3rd" },
  ],
  [
    { text = "Young adult" },
    { text = "DR 5/magic, [spell resistance](ref/rule/spell-resistance)" },
    { text = "5th" },
  ],
  [
    { text = "Adult" },
    { text = "Shadow breath, _[shadow walk](ref/spell/shadow-walk)_" },
    { text = "7th" },
  ],
  [
    { text = "Mature adult" },
    { text = "DR 10/magic" },
    { text = "9th" },
  ],
  [
    { text = "Old" },
    { text = "_[Project image](ref/spell/project-image)_" },
    { text = "11th" },
  ],
  [
    { text = "Very old" },
    { text = "DR 15/magic" },
    { text = "13th" },
  ],
  [
    { text = "Ancient" },
    { text = "Create shadows, _[finger of death](ref/spell/finger-of-death)_" },
    { text = "15th" },
  ],
  [
    { text = "Wyrm" },
    { text = "DR 20/magic" },
    { text = "17th" },
  ],
  [
    { text = "Great wyrm" },
    { text = "Energy drain, _[shades](ref/spell/shades)_" },
    { text = "19th" },
  ],
]
:::
