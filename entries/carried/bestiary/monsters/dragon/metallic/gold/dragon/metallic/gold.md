+++
id = "ref/carried/bestiary/monsters/dragon/metallic/gold/dragon/metallic/gold"
kind = "creature"
title = "Dragon, Metallic, Gold"
source_ids = ["bestiary"]
section = ["Monsters", "Dragon", "Metallic", "Gold", "Dragon", "Metallic"]
tags = ["small"]
provenance = [
  { dataset = "psrd-data", record = "pfsrd://Bestiary/Monsters/Dragon/Metallic/Gold/Dragon/Metallic/Gold", path = "bestiary/creature/dragon_metallic_gold.json" },
]

[fields]
kind = "creature"
cr = "7"
size = "Small"
abilities = ["17", "14", "15", "14", "15", "14"]
+++

::: statblock
CR: 7
Size: Small
Race: lg dragon (fire)
Hit Dice: 8d12
Speed: 60 ft., swim 60 ft.
Ability Scores: Str 17, Dex 14, Con 15, Int 14, Wis 15, Cha 14
Environment: warm plains
Organization: solitary
Treasure: triple
Natural Armor: +7
Breath Weapon: cone, 2d10 fire
:::

## Special Abilities {#special-abilities}

### Change Shape {#change-shape}

::: statblock
Ability Type: Supernatural
:::

A very young or older gold dragon can assume any animal or humanoid form three times per day as if
using polymorph.

### Detect Gems {#detect-gems}

::: statblock
Ability Type: Spell-Like
:::

A young or older gold dragon can detect gems three times per day. This functions as locate object,
but can only be used to locate gemstones.

### Divine Aid {#divine-aid}

::: statblock
Ability Type: Spell-Like
:::

Once a week, a great wyrm gold dragon can call upon celestial powers for aid. This functions as a
miracle.

### Fast Flight {#fast-flight}

::: statblock
Ability Type: Extraordinary
:::

A young or older gold dragon is treated as one size category larger when determining his fly speed.

### Fire Aura {#fire-aura}

::: statblock
Ability Type: Supernatural
:::

An old or older gold dragon is surrounded by an aura of fire. All creatures within 5 feet of the
dragon take 1d6 points of fire damage at the beginning of the dragon's turn. An ancient gold
dragon's aura extends to 10 feet. A great wyrm's damage increases to 2d6. The dragon can activate or
suppress this aura as a free action.

### Luck {#luck}

::: statblock
Ability Type: Spell-Like
:::

Once per day an adult or older gold dragon can touch a gem, usually one embedded in the dragon's
hide, and enspell it to bring good luck. As long as the dragon carries the gem, it and every good
creature within a given radius of it (10 ft. per age category) receives a +1 luck bonus on all
saving throws. If the dragon gives an enspelled gem to another creature, only that bearer gets the
bonus. The effect lasts 1d3 hours plus 3 hours per age category of the dragon. This ability is the
equivalent of a 2nd-level spell.

### Spell-Like Abilities {#spell-like-abilities}

::: statblock
Ability Type: Spell-Like
:::

A gold dragon gains the following [spell-like abilities](ref/umr/spell-like-abilities) upon reaching
the listed age category. Its caster level for these effects is equal to its Hit Dice, and any save
DCs are Charisma-based. A gold dragon can use these abilities at will. Very young—detect evil;
Juvenile—bless; Adult—daylight; Old—geas/quest; Ancient—sunburst; Great wyrm—foresight.

### Weakening Breath {#weakening-breath}

::: statblock
Ability Type: Supernatural
:::

Instead of a cone of fire, a gold dragon can breathe a cone of weakening gas. Creatures within the
cone must succeed on a Fortitude save or take 1 point of Strength damage per age category (Will save
half).

## Age Category {#age-category}

::: table
head = [
  [
    { text = "Age Category", header = true },
    { text = "Special Abilities", header = true },
    { text = "Caster Level\\*", header = true },
  ],
]
body = [
  [
    { text = "Wyrmling" },
    { text = "Fire subtype, weakening breath" },
    { text = "—" },
  ],
  [
    { text = "Very young" },
    { text = "Change shape, _[detect evil](ref/spell/detect-evil)_" },
    { text = "—" },
  ],
  [
    { text = "Young" },
    { text = "Fast flight, detect gems" },
    { text = "1st" },
  ],
  [
    { text = "Juvenile" },
    { text = "_[Bless](ref/spell/bless)_" },
    { text = "3rd" },
  ],
  [
    { text = "Young adult" },
    { text = "DR 5/magic, [spell resistance](ref/rule/spell-resistance)" },
    { text = "5th" },
  ],
  [
    { text = "Adult" },
    { text = "Frightful presence, luck, _[daylight](ref/spell/daylight)_" },
    { text = "7th" },
  ],
  [
    { text = "Mature adult" },
    { text = "DR 10/magic" },
    { text = "9th" },
  ],
  [
    { text = "Old" },
    { text = "Fire aura, _[geas/quest](ref/spell/geas-quest)_" },
    { text = "11th" },
  ],
  [
    { text = "Very old" },
    { text = "DR 15/magic" },
    { text = "13th" },
  ],
  [
    { text = "Ancient" },
    { text = "_[Sunburst](ref/spell/sunburst)_" },
    { text = "15th" },
  ],
  [
    { text = "Wyrm" },
    { text = "DR 20/magic" },
    { text = "17th" },
  ],
  [
    { text = "Great wyrm" },
    { text = "Divine aid, _[foresight](ref/spell/foresight)_" },
    { text = "19th" },
  ],
]
foot = [
  [
    { text = "\\* A gold dragon can cast cleric spells as arcane spells.", colspan = 3 },
  ],
]
:::
