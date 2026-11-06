+++
id = "ref/carried/mythic-adventures/monsters/cockatrice/mythic"
kind = "creature"
title = "Cockatrice, Mythic"
source_ids = ["mythic-adventures"]
section = ["Monsters", "Cockatrice"]
tags = ["magical beast", "mythic", "small"]
provenance = [
  { dataset = "psrd-data", record = "pfsrd://Mythic Adventures/Monsters/Cockatrice/Mythic", path = "mythic_adventures/creature/mythic/cockatrice_mythic.json" },
]

[fields]
kind = "creature"
cr = "4"
creature_type = "Magical Beast"
subtypes = ["mythic"]
size = "Small"
alignment = "N"
ac = "17, touch 16, flat-footed 12 (+3 Dex, +2 dodge, +1 natural, +1 size)"
hp = "43 (6d10+10)"
fortitude = "+5"
reflex = "+8"
will = "+3"
melee = "bite +10 (1d4-2 plus petrification)"
special_attacks = "mythic power (1/day, surge +1d6)"
abilities = ["6", "17", "11", "2", "13", "8"]
+++

::: statblock
CR: 4
XP: 1,200
Alignment: N
Size: Small
Type: Magical Beast (mythic)
Init: +3
Senses: [darkvision](ref/rule/darkvision) 60 ft., [low-light vision](ref/rule/low-light-vision); Perception +11
Aura: petrification (30 feet)
AC: 17, touch 16, flat-footed 12 (+3 Dex, +2 dodge, +1 natural, +1 size)
hp: 43 (6d10+10)
Fort: +5
Ref: +8
Will: +3
Defensive Abilities: stone plumage
DR: 5/epic
Speed: 20 ft., fly 60 ft. (poor)
Melee: bite +10 (1d4-2 plus petrification)
Special Attacks: mythic power (1/day, surge +1d6)
Ability Scores: Str 6, Dex 17, Con 11, Int 2, Wis 13, Cha 8
Base Atk: +6
CMB: +3
CMD: 17
Feats: DodgeM, Skill Focus (Perception), Weapon Finesse
Skills: Fly +6, Perception +11
Environment: temperate plains
Organization: solitary, pair, flight (3-5), or flock (6-12)
Treasure: none
MR: 1
:::

_This beast is an unsettling combination of chicken and lizard, and its claws, beak, and wattles
seem made of stone._

## Special Abilities {#special-abilities}

### Petrification {#petrification}

::: statblock
Ability Type: Supernatural
:::

A mythic cockatrice's bite causes flesh to calcify and harden—multiple bites can cause a living
creature to fossilize into stone. Each time a creature is damaged by a mythic cockatrice's bite
attack, it must succeed at a DC 13 Fortitude save or take 1d6 points of Dexterity damage as its
flesh and bones stiffen and harden. If a creature's Dexterity score is reduced to 0 by a
cockatrice's bite, that creature immediately turns completely to stone, as if petrified by a flesh
to stone spell. Every day, a creature petrified by a cockatrice in this manner can attempt a new DC
12 Fortitude save; if it succeeds, the victim recovers from the petrification with a Dexterity score
of 1 (and thereafter can be restored to full Dexterity by natural healing or magic as normal). If a
petrified creature fails three of these Fortitude saves in a row, the petrified state becomes
permanent. A creature restored to flesh via magic has any Dexterity damage caused by cockatrice
bites removed, but not any existing Dexterity damage from other sources. A cockatrice is immune to
the petrification ability of itself and of other cockatrices, but other petrification attacks affect
them normally. The save DC is Constitution-based.

### Petrification Aura {#petrification-aura}

::: statblock
Ability Type: Supernatural
:::

A creature within 30 feet of a mythic cockatrice on its turn must successfully save or be subjected
by petrification as if it had been bitten.

### Stone Plumage {#stone-plumage}

::: statblock
Ability Type: Supernatural
:::

Any weapon that strikes a mythic cockatrice takes 1d6 points of damage that bypasses the weapon's
[hardness](ref/umr/hardness). Any creature attacking the cockatrice with natural weapons or unarmed
strikes takes 1d6 points of damage.

A mythic cockatrice is infused with stone, perhaps because of some aspect of its aging process, or
its body has absorbed minerals from countless stony foes, or its incessant grooming has slowly
petrified its own flesh. Even more aggressive and territorial than non-mythic kin, a mythic
cockatrice recklessly attacks anything that intrudes on its territory.
