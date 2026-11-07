+++
id = "ref/carried/mythic-adventures/monsters/skeleton/mythic"
kind = "creature"
title = "Skeleton, Mythic"
source_ids = ["mythic-adventures"]
section = ["Monsters", "Skeleton"]
tags = ["undead", "mythic", "medium"]
provenance = [
  { dataset = "psrd-data", record = "pfsrd://Mythic Adventures/Monsters/Skeleton/Mythic", path = "mythic_adventures/creature/mythic/skeleton_mythic.json" },
]

[fields]
kind = "creature"
cr = "1"
creature_type = "undead"
subtypes = ["mythic"]
size = "Medium"
alignment = "NE"
ac = "15, touch 12, flat-footed 13 (+2 Dex, +3 natural)"
hp = "17 (2d8+8)"
fortitude = "+0"
reflex = "+2"
will = "+3"
melee = "2 scimitars +3 (1d6+2/18-20) or 2 claws +3 (1d4+2)"
special_attacks = "mythic power (1/day, surge +1d6), relentless, superior two-weapon fighting"
abilities = ["15", "14", "-", "-", "10", "10"]
+++

::: statblock
CR: 1
XP: 400
Alignment: NE
Size: Medium
Type: Undead (mythic)
Init: +7M
Senses: [darkvision](ref/rule/darkvision) 60 ft.; Perception +0
AC: 15, touch 12, flat-footed 13 (+2 Dex, +3 natural)
hp: 17 (2d8+8)
Fort: +0
Ref: +2
Will: +3
Defensive Abilities: [channel resistance](ref/rule/channel-resistance) +2
DR: 5/bludgeoning
Immune: cold, undead traits
Speed: 30 ft.
Melee: 2 scimitars +3 (1d6+2/18-20) or 2 claws +3 (1d4+2)
Special Attacks: mythic power (1/day, surge +1d6), relentless, superior two-weapon fighting
Ability Scores: Str 15, Dex 14, Con -, Int -, Wis 10, Cha 10
Base Atk: +1
CMB: +3
CMD: 15
Feats: Improved InitiativeB, M
Environment: any
Organization: any
Treasure: standard (2 scimitars, other treasure)
MR: 1
:::

_Its eyes glowing like bluish-white flames amid the shadows of its kingly helm, this skeleton wields
two fearsome scimitars._

A mythic skeleton is an animated corpse created with mythic magic such as _mythic animate dead_. It
has an unnatural cunning that belies its mindless nature and a natural instinct for killing.

## Creating a Mythic Skeleton {#creating-a-mythic-skeleton}

"Mythic skeleton" is an acquired template that can be added to any creature with the skeleton
template (referred to hereafter as the base skeleton).

### Mythic Subtype {#mythic-subtype}

A mythic skeleton gains the mythic subtype, with a rank equal to half the CR of the base skeleton.
Instead of gaining additional abilities according to its CR, it always gains
[channel resistance](ref/rule/channel-resistance) +2, relentless, and superior two-weapon fighting.
The mythic skeleton gains all other benefits of having the mythic subtype: ability score bonuses,
bonus hit points, mythic feats, mythic power, natural armor bonus, and
[spell resistance](ref/rule/spell-resistance) increase (if any).

### CR {#cr}

Adjust the base skeleton's CR according to its mythic rank (this template doesn't increase the base
skeleton's CR other than from the mythic rank).

### Hit Dice {#hit-dice}

A mythic skeleton's Hit Dice are determined as though it were a zombie instead of a skeleton.

### Relentless {#relentless}

::: statblock
Ability Type: Extraordinary
:::

Any melee attack made against a mythic skeleton provokes an attack of opportunity from the skeleton.

### Superior Two Weapon Fighting {#superior-two-weapon-fighting}

::: statblock
Ability Type: Extraordinary
:::

A mythic humanoid skeleton usually fights with a scimitar in each hand. It does not take a penalty
on attack or damage rolls for attacking with two weapons.

## Other Mythic Skeletons {#other-mythic-skeletons}

Other types of skeletons have the following additional or altered abilities.

### Mythic Bloody Skeleton {#mythic-bloody-skeleton}

Destroying a mythic bloody skeleton in the area of a non-mythic _[bless](ref/spell/bless)_ spell
doesn't prevent it from returning to unlife.

### Mythic Burning Skeleton {#mythic-burning-skeleton}

Add half the burning skeleton's mythic rank to its fiery aura damage and melee attack fire damage.
Add its mythic rank to the DC of its fiery death ability.

## Mythic Skeletal Champion {#mythic-skeletal-champion}

To create a mythic skeletal champion, increase its [channel resistance](ref/rule/channel-resistance)
by +2, and add the mythic subtype, additional Hit Dice as if the skeletal champion were a zombie of
its size, and mythic abilities according to the base skeletal champion's Hit Dice.
