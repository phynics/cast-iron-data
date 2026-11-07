+++
id = "ref/carried/bestiary-4/monsters/shadow-creature"
kind = "creature"
title = "Shadow Creature"
source_ids = ["bestiary-4"]
section = ["Monsters"]
tags = ["outsider", "augmented aberration", "large"]
provenance = [
  { dataset = "psrd-data", record = "pfsrd://Bestiary 4/Monsters/Shadow Creature", path = "bestiary_4/creature/shadow_creature.json" },
]

[fields]
kind = "creature"
cr = "13"
creature_type = "outsider"
subtypes = ["augmented aberration"]
size = "Large"
alignment = "CE"
ac = "27, touch 10, flat-footed 26 (+1 Dex, +17 natural, –1 size)"
hp = "162 (12d8+108)"
fortitude = "+13"
reflex = "+5"
will = "+13"
melee = "bite +20 (4d8+18/19–20)"
ranged = "6 strands +10 touch (1d6 Str)"
special_attacks = "pull (strands, 5 ft.), strands"
abilities = ["34", "13", "29", "13", "16", "12"]
+++

::: statblock
CR: 13
XP: 25,600
Alignment: CE
Size: Large
Type: Outsider (augmented aberration)
Init: +5
Senses: [darkvision](ref/rule/darkvision) 60 ft., [low-light vision](ref/rule/low-light-vision); Perception +24
AC: 27, touch 10, flat-footed 26 (+1 Dex, +17 natural, –1 size)
hp: 162 (12d8+108)
Fort: +13
Ref: +5
Will: +13
Defensive Abilities: shadow blend
DR: 10/magic
Immune: electricity
Resist: cold 15
SR: 27
Weaknesses: vulnerable to fire
Speed: 10 ft.
Melee: bite +20 (4d8+18/19–20)
Ranged: 6 strands +10 touch (1d6 Str)
Space: 10 ft.
Reach: 10 ft.
Special Attacks: pull (strands, 5 ft.), strands
Ability Scores: Str 34, Dex 13, Con 29, Int 13, Wis 16, Cha 12
Base Atk: +9
CMB: +22
CMD: 33 (can't be tripped)
Feats: Improved Critical (bite), Improved Initiative, Iron Will, Skill Focus (Perception), Skill Focus (Stealth), Weapon Focus (strand)
Skills: Climb +27, Knowledge (dungeoneering) +13, Knowledge (religion) +13, Perception +24, Stealth +18 (+44 in icy or stony areas)
Racial Modifiers: +26 Stealth in icy or stony areas
Languages: Aklo, Common
Environment: any underground
Organization: solitary, pair, or cluster (3–6)
Treasure: standard
:::

_A tentacled horror that seems to shift in and out of the shadows, this bizarre beast is an
amalgamation of darkness and menace._

## Special Abilities {#special-abilities}

### Strands {#strands}

::: statblock
Ability Type: Extraordinary
:::

A shadow roper can extend up to six thin, sticky strands from its body at a time, launching them to
a maximum range of 50 feet. A shadow roper's attacks with its strands resolve as ranged touch
attacks. These strands are quite strong, but can be severed by any amount of slashing damage; each
strand has an AC of 20. A creature struck by a strand is numbed and weakened by the strange
material, and must succeed at a DC 25 Fortitude save or take 1d6 points of Strength damage. The save
DC is Constitution-based.

When a Material Plane creature is trapped on or chooses to remain on the Shadow Plane, it often
finds that its offspring take on some of the eerie qualities of its new home dimension. Those who
are born in that place become weird mockeries of their kin on the Material Plane.

Their colorings become jet-black (or at best a hazy gray), their features become more menacing, and
their eyes glow white, a dulled crimson, a dark green, or a strange violet. The variety of shadow
creatures is as vast as that on the Material Plane, creating dangers that are similar but have
additional defenses and abilities characteristic of creatures truly native to the Shadow Plane's
perpetual gloom.

Shadow creatures on the Material Plane will produce offspring, giving rise to shadow creature
enclaves in dark corners of the world. Stranger still, a burgeoning ecology of shadow creatures that
forms a colony on the Material Plane seems to create a small blighted realm of shadow where they
dwell. As such, areas grow more and more overcast. Shadows become unnaturally deeper, darker, and
more cloying until the land itself seems to assume the landscape and terrain of the Shadow Plane. As
part of this transformation process, one of the more intelligent shadow creatures in the area
becomes a shadow lord—a dread agent of shadow that controls powerful shadow abilities and works to
expand its alien domain.

## Creating a Shadow Creature {#creating-a-shadow-creature}

"Shadow creature" is an inherited template that can be added to any living creature, referred to
hereafter as the base creature. A shadow creature retains all the base creature's statistics and
abilities except as noted here.

### Challenge Rating {#challenge-rating}

Same as the base creature +1.

### Alignment {#alignment}

Any (usually nongood).

### Type {#type}

The base creature's type changes to outsider, and it gains the augmented subtype. Do not recalculate
BAB, saves, or skill ranks.

### Senses {#senses}

As the base creature plus [darkvision](ref/rule/darkvision) 60 feet and
[low-light vision](ref/rule/low-light-vision).

### Defensive Abilities {#defensive-abilities}

A shadow creature gains DR and resistance to cold and electricity based on its Hit Dice, as noted on
the following table.

|Hit Dice|Resist Cold and Electricity|DR|
| --- | --- | --- |
|1-4|5|—|
|5-10|10|5/magic|
|11+|15|10/magic|

::: statblock
Ability Type: Supernatural
:::

_Shadow Blend _In any illumination other than bright light, a shadow creature blends into the
shadows, giving it concealment (20% miss chance). A shadow creature can suspend or resume this
ability as a free action.

_Spell Resistance (Ex)_A shadow creature gains [spell resistance](ref/rule/spell-resistance) equal
to the base creature's CR + 6.

## Creating a Shadow Lord {#creating-a-shadow-lord}

"Shadow lord" is an acquired template that can be added to any shadow creature with 5 or more Hit
Dice (referred to hereafter as the base creature). Most shadow lords were originally humanoids. A
shadow lord retains all the base creature's statistics and abilities (including those granted by the
shadow creature template) except as noted here.

### Challenge Rating {#challenge-rating-2}

Same as the base creature +2.

### Alignment {#alignment-2}

Any evil.

### Senses {#senses-2}

A shadow lord gains the see in darkness ability.

### Armor Class {#armor-class}

Same as the base creature (see also the incorporeal step ability).

### Defensive Abilities {#defensive-abilities-2}

::: statblock
Ability Type: Supernatural
:::

A shadow lord gains the following defensive abilities.

_Energy Resistance and Damage Reduction _A shadow lord gains
[damage reduction](ref/rule/damage-reduction) and resistance to cold and electricity based on its
Hit Dice, as noted on the table below. This replaces the energy resistance and damage reduction
granted by the shadow creature template.

|Hit Dice|Resist Cold and Electricity|DR|
| --- | --- | --- |
|5-10|15|10/magic|
|11-15|20|15/magic|
|16+|30|20/magic|

::: statblock
Ability Type: Supernatural
:::

_Incorporeal Step _:_ _When a shadow lord moves, it gains the incorporeal subtype and quality,
including a deflection bonus to AC equal to its Charisma bonus. It loses the incorporeal subtype and
special ability when it stops moving.

### Attacks {#attacks}

A shadow lord gains a melee touch attack that deals 1d6 points of damage (Fortitude negates). The
save DC is equal to 10 + 1/2 the shadow lord's Hit Dice + the shadow lord's Charisma modifier. On a
critical hit, the shadow lord's touch attack also deals 1 point of Constitution damage (also negated
by the saving throw).

### Special Attacks {#special-attacks}

::: statblock
Ability Type: Supernatural
:::

A shadow lord gains the following special attacks. Their saving throw DCs for these attacks are
equal to 10 + 1/2 the shadow lord's Hit Dice + the shadow lord's Charisma modifier, unless otherwise
noted.

_Cloying Gloom Blast _Three times per day, the shadow lord can unleash a 30-foot cone of cloying
gloom. On a failed Fortitude saving throw, creatures in the cone are affected by a
_[slow](ref/spell/slow)_ spell (caster level equal to the shadow lord's Hit Dice) and are blinded
for the duration of the _[slow](ref/spell/slow)_ effect.

### Spell-Like Abilities {#spell-like-abilities}

A shadow lord gains the following [spell-like abilities](ref/umr/spell-like-abilities), with a
caster level equal to its Hit Dice: at will—_[ray of sickening](ref/spell/ray-of-sickening)_;
3/day—_[shadow conjuration](ref/spell/shadow-conjuration)_, _[shadow step](ref/spell/shadow-step)_;
1/day—_greater shadow __conjuration_ (if the shadow lord has 11 or more Hit Dice),
_[shadow walk](ref/spell/shadow-walk)_.

A creature created with _[shadow conjuration](ref/spell/shadow-conjuration)_ or
_[greater shadow conjuration](ref/spell/shadow-conjuration-greater)_ that would normally have a
celestial or fiendish template (such as a bear) instead gains the shadow creature template.

### Special Qualities {#special-qualities}

::: statblock
Ability Type: Supernatural
:::

A shadow lord gains the following special quality.

_Planar Thinning _Once per day as a full-round action, a shadow lord can thin the barriers between
the Material Plane and Shadow Plane, making it considerably easier for creatures to cross between
the two. This functions like the planar travel aspect of the _[gate](ref/spell/gate)_ spell (caster
level equal to the shadow lord's Hit Dice). This planar thinning is immediately dispelled if in an
area of normal or bright light.

### Ability Scores {#ability-scores}

Dex +4, Cha +4.

### Skills {#skills}

A shadow lord gains a +8 racial bonus on all Stealth checks.
