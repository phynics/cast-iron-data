+++
id = "ref/carried/mythic-adventures/monsters/elemental/fire/mythic"
kind = "creature"
title = "Elemental, Fire, Mythic"
source_ids = ["mythic-adventures"]
section = ["Monsters", "Elemental", "Fire"]
tags = ["outsider", "elemental", "extraplanar", "fire", "mythic", "huge"]
provenance = [
  { dataset = "psrd-data", record = "pfsrd://Mythic Adventures/Monsters/Elemental/Fire/Mythic", path = "mythic_adventures/creature/mythic/elemental_fire_mythic.json" },
]

[fields]
kind = "creature"
cr = "14"
creature_type = "outsider"
subtypes = ["elemental", "extraplanar", "fire", "mythic"]
size = "Huge"
alignment = "N"
ac = "32, touch 19, flat-footed 21 (+9 Dex, +2 dodge, +13 natural, -2 size)"
hp = "202 (16d10+114)"
fortitude = "+14"
reflex = "+19"
will = "+8"
melee = "2 slams +23 (2d8+8 plus burn)"
special_attacks = "blinding blaze, burn (2d10, DC 22), inferno, mythic power (5/day, surge +1d8)"
abilities = ["26", "29", "18", "12", "13", "11"]
+++

::: statblock
CR: 14
XP: 38,400
Alignment: N
Size: Huge
Type: Outsider (elemental, extraplanar, fire, mythic)
Init: +13
Senses: [darkvision](ref/rule/darkvision) 60 ft.; Perception +20
Aura: frightful presence (60 ft., DC 18), shroud of flame (15 ft., 2d6 fire, DC 22), smoke cloud (10 ft., DC 22)
AC: 32, touch 19, flat-footed 21 (+9 Dex, +2 dodge, +13 natural, -2 size)
hp: 202 (16d10+114)
Fort: +14
Ref: +19
Will: +8
DR: 10/-
Immune: elemental traits, fire
Weaknesses: vulnerable to cold
Speed: 60 ft.
Melee: 2 slams +23 (2d8+8 plus burn)
Space: 15 ft.
Reach: 15 ft.
Special Attacks: blinding blaze, burn (2d10, DC 22), inferno, mythic power (5/day, surge +1d8)
Spell-like abilities: (CL 16th; concentration +16)\
At will-_[produce flame](ref/spell/produce-flame)_\
5/day-_[flame arrow](ref/spell/flame-arrow)_, _[wall of fire](ref/spell/wall-of-fire)_
Ability Scores: Str 26, Dex 29, Con 18, Int 12, Wis 13, Cha 11
Base Atk: +16
CMB: +26
CMD: 47
Feats: Blind-Fight, Combat ReflexesM, DodgeM, Improved InitiativeB, Iron WillM, Lightning Stance, Mobility, Spring Attack, Weapon FinesseB, Wind Stance
Skills: Acrobatics +28 (+40 when jumping), Climb +27, Escape Artist +28, Intimidate +19, Knowledge (planes) +20, Perception +20, Sense Motive +20
Languages: Ignan
Environment: any (Plane of Fire)
Organization: solitary, pair, or gang (3-8)
Treasure: none
MR: 5
:::

_This blazing conflagration is vaguely humanoid in shape, its horned visage almost too bright to
look upon._

## Special Abilities {#special-abilities}

### Blinding Blaze {#blinding-blaze}

::: statblock
Ability Type: Supernatural
:::

A mythic fire elemental can expend one use of mythic power as a swift action to burn brightly,
granting it a blinding gaze attack. This gaze causes permanent blindness and has a range of 60 feet.
A creature that succeeds at a DC 22 Fortitude save is instead dazzled for 1 round. Fire elementals
are immune to this blindness. The save DC is Constitution-based.

### Inferno {#inferno}

::: statblock
Ability Type: Extraordinary
:::

A mythic fire elemental can expend one use of mythic power as an immediate action to lose its
vulnerability to cold for 1 round. During this time, any fire damage it deals ignores fire
resistance and fire immunity.

### Shroud of Flame {#shroud-of-flame}

::: statblock
Ability Type: Extraordinary
:::

Any creature within a mythic fire elemental's reach must succeed at a DC 22 Reflex save at the start
of its turn or take 2d6 points of fire damage. The elemental can suppress or reactivate this ability
at will as a free action. The save DC is Constitution-based.

### Smoke Cloud {#smoke-cloud}

::: statblock
Ability Type: Extraordinary
:::

As a swift action, a mythic fire elemental can create a choking cloud of smoke. This cloud is
equivalent to that of pyrotechnics and lasts 1 minute. Fire elementals are immune to the effects of
this ability.

A mythic elder fire elemental is a living fragment of the original fires at the heart of its home
plane. Having learned the patience of a slow burn, it lacks both the recklessness of younger fire
elementals and the urge to inspire fear in the hearts of flammable mortals. It enjoys using smoke to
scatter opponents so it can chase them down and set them alight.
