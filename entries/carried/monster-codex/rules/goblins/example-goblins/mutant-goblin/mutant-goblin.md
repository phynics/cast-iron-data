+++
id = "ref/carried/monster-codex/rules/goblins/example-goblins/mutant-goblin/mutant-goblin"
kind = "creature"
title = "Mutant Goblin"
aon = "MonsterDisplay.aspx?ItemName=Mutant%20Goblin"
source_ids = ["monster-codex"]
section = ["Rules", "Goblins", "Example Goblins", "Mutant Goblin"]
tags = ["humanoid", "goblinoid", "small"]
provenance = [
  { dataset = "psrd-data", record = "pfsrd://Monster Codex/Rules/Goblins/Example Goblins/Mutant Goblin/Mutant Goblin", path = "monster_codex/creature/mutant_goblin.json" },
]

[fields]
kind = "creature"
cr = "3"
creature_type = "humanoid"
subtypes = ["goblinoid"]
size = "Small"
alignment = "NE"
ac = "16, touch 12, flat-footed 13 (+3 Dex, +4 natural, -2 rage, +1 size)"
hp = "37 (3d12+12); fast healing 1"
fortitude = "+7"
reflex = "+4"
will = "+4; +2 vs. magic"
melee = "2 claws +9 (1d3+5)"
ranged = "composite shortbow +7 (1d4+5/×3)"
special_attacks = "breath weapon (20-ft. line, 3d4 acid damage, Reflex DC 14 half, usable every 1d4 rounds), rage (10 rounds/day), rage powers (superstition +2)"
special_qualities = "fast movement, mutations (breath weapon, claws, fast healing, wings)"
abilities = ["21", "17", "18", "8", "12", "6"]
+++

::: statblock
CR: 3
XP: 800
Alignment: NE
Size: Small
Type: Humanoid (goblinoid)
Class Levels: barbarian 3
Init: +7
Senses: [darkvision](ref/rule/darkvision) 60 ft.; Perception +7
AC: 16, touch 12, flat-footed 13 (+3 Dex, +4 natural, -2 rage, +1 size)
hp: 37 (3d12+12); [fast healing](ref/umr/fast-healing) 1
Fort: +7
Ref: +4
Will: +4; +2 vs. magic
Defensive Abilities: trap sense +1, uncanny dodge
Speed: 40 ft., fly 30 ft. (clumsy)
Melee: 2 claws +9 (1d3+5)
Ranged: composite shortbow +7 (1d4+5/×3)
Special Attacks: breath weapon (20-ft. line, 3d4 acid damage, Reflex DC 14 half, usable every 1d4 rounds), rage (10 rounds/day), rage powers (superstition +2)
Ability Scores: Str 21, Dex 17, Con 18, Int 8, Wis 12, Cha 6
Base Atk: +3
CMB: +7
CMD: 18
Feats: Improved Initiative, Power Attack
Skills: Fly -4, Intimidate +4, Perception +7, Ride +6, Stealth +13, Swim +10
Racial Modifiers: +4 Ride, +4 Stealth
Languages: Goblin
SQ: fast movement, mutations (breath weapon, claws, [fast healing](ref/umr/fast-healing), wings)
Combat Gear: potion of bull's strength, potion of cure serious wounds, potion of displacement, potion of protection from arrows, acid (2), alchemist's fire (2), smokestick, tanglefoot bag
Other Gear: composite shortbow with 20 arrows, 94 gp
:::

## Creating a Mutant Goblin {#creating-a-mutant-goblin}

"Mutant goblin" is an acquired template that can be added to a goblin (referred to hereafter as the
base creature). A mutant goblin uses the base creature's statistics and special abilities except as
noted here.

### CR {#cr}

Same as the base creature + 1.

### Armor Class {#armor-class}

Natural armor bonus increases by 4.

### Mutations {#mutations}

A mutant goblin gains four of the following mutations, determined randomly when it gains the
template. For every 5 Hit Dice it has (5, 10, and so on), it gains another random mutation. (Other
possible mutations include tusks, a spiked tail, and gills.)

#### Breath Weapon {#breath-weapon}

::: statblock
Ability Type: Supernatural
:::

: The goblin can spew a line of foul acidic blood from its mouth (20-foot line, Reflex DC = 10 + 1/2
Hit Die + its Constitution modifier for half damage, 1d4 points of acid damage per HD, usable every
1d4 rounds). If it has 5 or more HD, the range increases to 30 feet and the damage increases to 1d6
points of acid damage per HD.

#### Claws {#claws}

::: statblock
Ability Type: Extraordinary
:::

: The goblin's hands become claws. It gains a natural claw attack for each hand that deals damage
appropriate to its size, and gains the grab ability with its claws.

#### Extra Arm {#extra-arm}

::: statblock
Ability Type: Extraordinary
:::

: The goblin gains an extra arm with a functional hand, as the vestigial arm discovery. If it gains
this mutation again, it gains another arm.

#### Fast Healing {#fast-healing}

::: statblock
Ability Type: Extraordinary
:::

: The goblin gains [fast healing](ref/umr/fast-healing) 1. If it has 5 Hit Dice or more, this
increases to fast healing 2. If the creature has 10 HD or more, this increases to fast healing 5.

#### Venomous Bite {#venomous-bite}

::: statblock
Ability Type: Extraordinary
:::

: The mutant goblin grows large fangs, gaining a poisonous bite as a natural attack that deals
damage appropriate to its size. The poison functions like wyvern poison, except its DC is 10 + 1/2
HD + its Constitution modifier.

#### Wings {#wings}

::: statblock
Ability Type: Extraordinary
:::

: The goblin gains dragonfly wings, granting it a fly speed of 30 feet with clumsy maneuverability.

### Abilities {#abilities}

Str +4, Int –2.
