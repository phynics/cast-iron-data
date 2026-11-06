+++
id = "ref/carried/bestiary-2/monsters/dragon/primal/cloud/dragon/primal/cloud"
kind = "creature"
title = "Dragon, Primal, Cloud"
source_ids = ["bestiary-2"]
section = ["Monsters", "Dragon", "Primal", "Cloud", "Dragon", "Primal"]
tags = ["small"]
provenance = [
  { dataset = "psrd-data", record = "pfsrd://Bestiary 2/Monsters/Dragon/Primal/Cloud/Dragon/Primal/Cloud", path = "bestiary_2/creature/dragon_primal_cloud.json" },
]

[fields]
kind = "creature"
cr = "5"
size = "Small"
abilities = ["10", "13", "13", "10", "14", "13"]
+++

::: statblock
CR: 5
Size: Small
Race: cn dragon (air, extraplanar)
Hit Dice: 6d12
Speed: 40 ft., swim 40 ft.
Ability Scores: Str 10, Dex 13, Con 13, Int 10, Wis 14, Cha 13
Environment: any sky (Plane of Air)
Organization: solitary
Treasure: triple
Natural Armor: +5
Breath Weapon: cone, 2d8 electricity
:::

## Special Abilities {#special-abilities}

### Cloud Form {#cloud-form}

::: statblock
Ability Type: Supernatural
:::

An adult or older cloud dragon can change itself into a cloudy vapor as a swift action for a number
of rounds per day equal to its Hit Dice. This ability functions as gaseous form but the dragon's fly
speed is unchanged.

### Cloud Breath {#cloud-breath}

::: statblock
Ability Type: Supernatural
:::

A great wyrm cloud dragon's breath weapon creates a cloud that persists in its cone shape for 1d4
rounds. Treat this cloud as a fog cloud that deals electricity damage equal to half the dragon's
breath weapon damage to any creature that ends its turn still within the cloud (Reflex save halves
the damage—DC equals the dragon's breath weapon save DC).

### Mist Vision {#mist-vision}

::: statblock
Ability Type: Supernatural
:::

A cloud dragon can see through fog, clouds, and similar obscuring effects with perfect clarity.

### Spell-Like Abilities {#spell-like-abilities}

::: statblock
Ability Type: Spell-Like
:::

A cloud dragon gains the following [spell-like abilities](ref/umr/spell-like-abilities), usable at
will (unless indicated otherwise) on reaching the listed age category. Very young—obscuring mist;
Young—fog cloud; Adult—solid fog; Old—cloudkill (3/day); Ancient—wind walk; Great wyrm—storm of
vengeance (1/day).

### Thundering Bite {#thundering-bite}

::: statblock
Ability Type: Supernatural
:::

An ancient or older cloud dragon's bite makes a thundering crash whenever it attacks, dealing an
additional 2d6 points of sonic damage. A great wyrm's thundering bite deals an additional 4d6 sonic
damage.

## Table: Cloud Special Abilities {#table-cloud-special-abilities}

::: table
caption = "Table: Cloud Special Abilities"
head = [
  [
    { text = "Age Category", header = true },
    { text = "Special Abilities", header = true },
    { text = "Caster Level", header = true },
  ],
  [
    { text = "Wyrmling" },
    { text = "Immune to electricity, mist vision" },
    { text = "—" },
  ],
  [
    { text = "Very young" },
    { text = "_[Obscuring mist](ref/spell/obscuring-mist)_" },
    { text = "—" },
  ],
  [
    { text = "Young" },
    { text = "_[Fog cloud](ref/spell/fog-cloud)_" },
    { text = "—" },
  ],
  [
    { text = "Juvenile" },
    { text = "Frightful presence" },
    { text = "1st" },
  ],
  [
    { text = "Young adult" },
    { text = "DR 5/magic, [spell resistance](ref/rule/spell-resistance)" },
    { text = "3rd" },
  ],
  [
    { text = "Adult" },
    { text = "Cloud form, _[solid fog](ref/spell/solid-fog)_" },
    { text = "5th" },
  ],
  [
    { text = "Mature adult" },
    { text = "DR 10/magicv" },
    { text = "7th" },
  ],
  [
    { text = "Old" },
    { text = "_[Cloudkill](ref/spell/cloudkill)_" },
    { text = "9th" },
  ],
  [
    { text = "Very old" },
    { text = "DR 15/magic" },
    { text = "11th" },
  ],
  [
    { text = "Ancient" },
    { text = "Thundering bite, _[wind walk](ref/spell/wind-walk)_" },
    { text = "13th" },
  ],
  [
    { text = "Wyrm" },
    { text = "DR 20/magic" },
    { text = "15th" },
  ],
  [
    { text = "Great wyrm" },
    { text = "Cloud breath, _[storm of vengeance](ref/spell/storm-of-vengeance)_" },
    { text = "17th" },
  ],
]
:::
