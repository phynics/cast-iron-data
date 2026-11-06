+++
id = "ref/carried/bestiary-2/monsters/dragon/primal/crystal/dragon/primal/crystal"
kind = "creature"
title = "Dragon, Primal, Crystal"
source_ids = ["bestiary-2"]
section = ["Monsters", "Dragon", "Primal", "Crystal", "Dragon", "Primal"]
tags = ["tiny"]
provenance = [
  { dataset = "psrd-data", record = "pfsrd://Bestiary 2/Monsters/Dragon/Primal/Crystal/Dragon/Primal/Crystal", path = "bestiary_2/creature/dragon_primal_crystal.json" },
]

[fields]
kind = "creature"
cr = "2"
size = "Tiny"
abilities = ["9", "16", "13", "10", "11", "16"]
+++

::: statblock
CR: 2
Size: Tiny
Race: cg dragon (earth, extraplanar)
Hit Dice: 3d12
Speed: 60 ft., burrow 30 ft., climb 30 ft.
Ability Scores: Str 9, Dex 16, Con 13, Int 10, Wis 11, Cha 16
Environment: any underground (Plane of Earth)
Organization: solitary
Treasure: triple
Natural Armor: +2
Breath Weapon: cone, 2d4 sonic
:::

## Special Abilities {#special-abilities}

### Razor Sharp {#razor-sharp}

::: statblock
Ability Type: Spell-Like
:::

All of a crystal dragon's natural attacks deal slashing damage.

### Ray Reflection {#ray-reflection}

::: statblock
Ability Type: Extraordinary
:::

An ancient crystal dragon's scales reflect ray spells back upon the ray's source if the ray fails to
overcome the dragon's [spell resistance](ref/rule/spell-resistance).

### Scintillating Aura {#scintillating-aura}

::: statblock
Ability Type: Supernatural
:::

A great wyrm crystal dragon radiates an aura of scintillating color from its jeweled scales to a
radius of 60 feet. All within this area must make a Will save each round to avoid being stunned (if
the victim has 15 or fewer Hit Dice) or confused (if the victim has more than 15 Hit Dice) for 1
round. The save DC is equal to the dragon's breath weapon save DC. This is a mind-affecting effect.
The dragon can activate or suppress this aura as a free action.

### Spell-Like Abilities {#spell-like-abilities}

::: statblock
Ability Type: Spell-Like
:::

A crystal dragon gains the following [spell-like abilities](ref/umr/spell-like-abilities), usable at
will (unless indicated otherwise) upon reaching the listed age category. Very young—color spray;
Juvenile—glitterdust; Adult—rainbow pattern; Old—stone to flesh (3/day); Ancient—prismatic spray
(3/day); Great wyrm—imprisonment (1/day).

### Tremorsense {#tremorsense}

::: statblock
Ability Type: Extraordinary
:::

Crystal dragons do not gain [tremorsense](ref/umr/tremorsense) until juvenile age (30 ft.),
improving at adult (60 ft.) and old (120 ft.).

## Table: Crystal Special Abilities {#table-crystal-special-abilities}

::: table
caption = "Table: Crystal Special Abilities"
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
    { text = "Immunity to sonic, razor sharp" },
    { text = "—" },
  ],
  [
    { text = "Very young" },
    { text = "_[Color spray](ref/spell/color-spray)_" },
    { text = "—" },
  ],
  [
    { text = "Young" },
    { text = "[Tremorsense](ref/umr/tremorsense)" },
    { text = "—" },
  ],
  [
    { text = "Juvenile" },
    { text = "_[Glitterdust](ref/spell/glitterdust)_" },
    { text = "—" },
  ],
  [
    { text = "Young adult" },
    { text = "DR 5/magic, [spell resistance](ref/rule/spell-resistance)" },
    { text = "—" },
  ],
  [
    { text = "Adult" },
    { text = "Frightful presence, _[rainbow pattern](ref/spell/rainbow-pattern)_" },
    { text = "1st" },
  ],
  [
    { text = "Mature adult" },
    { text = "DR 10/magic" },
    { text = "3rd" },
  ],
  [
    { text = "Old" },
    { text = "_[Stone to flesh](ref/spell/stone-to-flesh)_" },
    { text = "5th" },
  ],
  [
    { text = "Very old" },
    { text = "DR 15/magic" },
    { text = "7th" },
  ],
  [
    { text = "Ancient" },
    { text = "Ray reflection, _[prismatic spray](ref/spell/prismatic-spray)_" },
    { text = "9th" },
  ],
  [
    { text = "Wyrm" },
    { text = "DR 20/magic" },
    { text = "11th" },
  ],
  [
    { text = "Great wyrm" },
    { text = "_Imprisonment, s_cintillating aura" },
    { text = "13th" },
  ],
]
:::
