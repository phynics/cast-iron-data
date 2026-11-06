+++
id = "ref/carried/bestiary-2/monsters/dragon/primal/brine/dragon/primal/brine"
kind = "creature"
title = "Dragon, Primal, Brine"
source_ids = ["bestiary-2"]
section = ["Monsters", "Dragon", "Primal", "Brine", "Dragon", "Primal"]
tags = ["tiny"]
provenance = [
  { dataset = "psrd-data", record = "pfsrd://Bestiary 2/Monsters/Dragon/Primal/Brine/Dragon/Primal/Brine", path = "bestiary_2/creature/dragon_primal_brine.json" },
]

[fields]
kind = "creature"
cr = "3"
size = "Tiny"
abilities = ["16", "15", "11", "13", "10", "11"]
+++

::: statblock
CR: 3
Size: Tiny
Race: ln dragon (extraplanar, water)
Hit Dice: 4d12
Speed: 60 ft., swim 60 ft.
Ability Scores: Str 16, Dex 15, Con 11, Int 13, Wis 10, Cha 11
Environment: any aquatic (Plane of Water)
Organization: solitary
Treasure: triple
Natural Armor: +3
Breath Weapon: line, 2d6 acid
:::

## Special Abilities {#special-abilities}

### Capsize {#capsize}

::: statblock
Ability Type: Extraordinary
:::

An old or older brine dragon can attempt to capsize a boat or ship by ramming it as a charge attack
and making a CMB check. The DC of this check is 25 or the result of the boat captain's Profession
(sailor) check, whichever is higher. For each size category larger the ship is than the brine
dragon's size, the dragon takes a cumulative –10 penalty on the check.

### Desiccating Bite {#desiccating-bite}

::: statblock
Ability Type: Supernatural
:::

An ancient brine dragon's bite causes weakness, dealing 1d2 points of Strength drain in addition to
its normal damage. A great wyrm's bite deals 1d4 points of Strength drain. A Fortitude save (DC
equals the dragon's breath weapon save DC) negates the Strength drain.

### Painful Strikes {#painful-strikes}

::: statblock
Ability Type: Supernatural
:::

A great wyrm brine dragon's natural attacks are so laden with salt and acidic crystals that every
time it strikes a creature with one of these attacks, the target must make a Fortitude save (DC
equals the dragon's breath weapon save DC) or be stunned for a round from the pain.

### Spell-like Abilities {#spell-like-abilities}

::: statblock
Ability Type: Spell-Like
:::

A brine dragon gains the following [spell-like abilities](ref/umr/spell-like-abilities), usable at
will (unless indicated otherwise) at the listed age. Very young—speak with animals (fish only);
Young—obscuring mist; Juvenile—water breathing; Adult—control water; Ancient—horrid wilting (3/day);
Great wyrm—tsunami (3/day).

### Table: Brine Special Abilities {#table-brine-special-abilities}

::: table
caption = "Table: Brine Special Abilities"
head = [
  [
    { text = "Age Category", header = true },
    { text = "Special Abilities", header = true },
    { text = "Caster Level", header = true },
  ],
  [
    { text = "Wyrmling" },
    { text = "Immunity to acid, water breathing" },
    { text = "—" },
  ],
  [
    { text = "Very young" },
    { text = "_[Speak with animals](ref/spell/speak-with-animals)_ (fish only)" },
    { text = "—" },
  ],
  [
    { text = "Young" },
    { text = "_[Obscuring mist](ref/spell/obscuring-mist)_" },
    { text = "1st" },
  ],
  [
    { text = "Juvenile" },
    { text = "_[Water breathing](ref/spell/water-breathing)_" },
    { text = "3rd" },
  ],
  [
    { text = "Young adult" },
    { text = "DR 5/magic, [spell resistance](ref/rule/spell-resistance)" },
    { text = "5th" },
  ],
  [
    { text = "Adult" },
    { text = "Frightful presence, _[control water](ref/spell/control-water)_" },
    { text = "7th" },
  ],
  [
    { text = "Mature adult" },
    { text = "DR 10/magic" },
    { text = "9th" },
  ],
  [
    { text = "Old" },
    { text = "Capsize" },
    { text = "11th" },
  ],
  [
    { text = "Very old" },
    { text = "DR 15/magic" },
    { text = "13th" },
  ],
  [
    { text = "Ancient" },
    { text = "Desiccating bite, _[horrid wilting](ref/spell/horrid-wilting)_" },
    { text = "15th" },
  ],
  [
    { text = "Wyrm" },
    { text = "DR 20/magic" },
    { text = "17th" },
  ],
  [
    { text = "Great wyrm" },
    { text = "Painful strikes, _[tsunami](ref/spell/tsunami)_" },
    { text = "19th" },
  ],
]
:::
