+++
id = "ref/template/waxwork"
kind = "rule"
title = "Waxwork"
source_ids = ["horror-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "waxwork", path = "json/monster_template4.json" },
]

[fields]
kind = "none"
+++

**Waxwork**

**Challenge rating:** Varies

**Inherited:** present

**Source:** Horror Adventures/246

The practice of making sculptures from wax dates back to the earliest humanoid civilizations. Only
the medium of wax can so closely duplicate the transparency of skin. Often, creators use powerful
magic to house an animating spirit within the wax model. A created waxwork creature obeys the
commands of its creator. Rarely, a wax sculpture animates of it own accord - the result of nearby
magic suffusing the wax or a lost spirit in search of a corporeal form. Such waxwork creatures are
uncontrolled.

A waxwork creature is the same size as the creature it duplicates, but weighs only half as much.

"Waxwork" is an inherited template that can be added to any Tiny or larger corporeal creature (other
than a construct or ooze), referred to hereafter as the base creature.

**CR:** Depends on Hit Dice, as follows.

|Waxwork HD|CR|
| --- | --- |
|1|2|
|2-3|3|
|4-5|4|
|6-7|5|
|8-10|6|
|11-13|7|
|14-16|8|
|17-19|9|
|20|10|

If the creature is larger or smaller than Medium, adjust the CR according to the table below.

|Waxwork Size|CR|Natural Armor Bonus|Bonus Hit points|
| --- | --- | --- | --- |
|Tiny or smaller|-2|+0|-|
|Small|-1|+1|+10|
|Medium|+0|+2|+20|
|Large|+1|+3|+30|
|Huge|+2|+4|+40|
|Gargantuan|+3|+7|+60|
|Colossal|+4|+11|+80|

**Alignment:** Always neutral.

**Type:** The creature's type changes to [construct](ref/type/construct). It doesn't retain any
subtypes, nor does it gain the augmented subtype. It uses all the base creature's statistics and
special abilities except as noted here.

**AC:** The waxwork creature's natural armor bonus is based on its size.

**Hit Dice:** Remove HD gained from class levels and change racial HD to d10s. Creatures without
racial HD are treated as if they have 1 racial HD. As constructs, waxwork creatures gain additional
hit points as noted in the following table.

**Saves:** The creature's base save bonuses are Fortitude +1/3 HD, Reflex +1/3 HD, and Will +1/3 HD.

**Defensive Abilities:** A waxwork creature loses the base creature's defensive abilities. It gains
waxen regeneration 5 (fire) and [immunity](ref/umr/immunity) to cold. If it has 11 or more HD, the
waxen regeneration increases to 10 (fire). It also gains all of the standard immunities and traits
possessed by constructs.

> **Waxen Regeneration (Su):** This ability functions like [regeneration](ref/umr/regeneration),
> except the waxwork creature has it without a Constitution score. A waxwork creature reduced to 0
> hit points is [staggered](ref/misc/staggered) instead of destroyed while its waxen regeneration is
> active; it ignores all damage dealt to it that would reduce its hit points below 0. Fire damage
> causes the waxwork creature's regeneration to stop functioning on the round following the attack.

**Weaknesses:** A waxwork creature is [vulnerable](ref/umr/vulnerabilities) to fire.

**Speed:** A waxwork creature retains movement types, except as follows: It loses burrow and magical
flight speeds. Winged waxwork creatures can fly, but maneuverability drops to clumsy. A waxwork
creature floats and must succeed at a DC 20 [Swim](ref/skill/swim) check each round to stay
underwater.

**Attacks:** A waxwork creature retains all the natural weapons and weapon proficiencies of the base
creature. It also gains a [slam attack](ref/umr/natural-attacks) that deals damage based on the
waxwork creature's size, but as if it were one size category larger than its actual size.

**Special Attacks:** A waxwork creature retains none of the base creature's special attacks.

**Abilities:** A waxwork creature has no Constitution or Intelligence score, and its Wisdom and
Charisma scores change to 10.

**BAB:** A waxwork creature's base attack bonus is equal to its Hit Dice.

**Skills:** A waxwork creature loses all of the base creature's skills and gains none of its own.

**Feats:** A waxwork creature loses all of the base creature's feats and gains
[Improved Initiative](ref/feat/improved-initiative) as a bonus feat.

**Special Qualities:** A waxwork creature loses most special qualities of the base creature. It
retains any extraordinary special qualities that improve its melee or ranged attacks. A waxwork
creature gains the [freeze](ref/umr/freeze) universal monster ability to appear as a wax sculpture.

### Variant Waxworks

The following variants alter the waxwork creature template.

#### Sentient Waxwork

Rarely, waxworks shaped like intelligent creatures develop minds of their own and can gain levels in
character classes.

**CR:** Same as a normal waxwork creature's CR.

**Abilities:** A sentient waxwork creature has an Intelligence score of 3d6.

**Skills:** A sentient waxwork creature gains skill points based on its Hit Dice and Intelligence.
[Disguise](ref/skill/disguise) and [Stealth](ref/skill/stealth) are class skills for it, but it has
no other class skills. If it was crafted to resemble a specific individual, it also gains a +10
racial bonus on Disguise checks to impersonate that individual.

**Feats:** A sentient waxwork gains retroactive [feats](ref/rule/step-6-skills-and-feats) based on
its Hit Dice.

**Languages:** A sentient waxwork creature speaks Common (or the language of the sculptor or
animating spirit).

#### Waxwork Candle

One or more small flames burn on wicks emerging from the waxwork creature's body, often its head or
hands. Though real, these flames don't consume the waxwork creature's body.

**CR:** Normal waxwork creature's CR + 1.

**Melee Attacks:** The waxwork creature's slam attack, or one natural attack it has, gains the
[burn](ref/umr/burn) universal monster ability. The additional fire damage is equal to the waxwork
creature's slam damage die. The waxwork creature gains a +2 racial bonus to the save DC.

**Special Qualities:** A waxwork candle creature gains illumination.

> **Illumination (Su):** A waxwork candle creature's flames create normal light within the
> creature's reach and increases the light level by one step within twice that distance (minimum 5
> feet). A waxwork candle creature is immune to its own fire, but not other flames (including those
> ignited by its own fire). The waxwork candle creature's flames can be extinguished as normal
> flames. It loses the burn ability when the wicks are unlit, but can magically reignite the flames
> as a move action.

**Construction:** Add [produce flame](ref/spell/produce-flame) as a spell requirement. Add 1,000 gp
to the price (and 500 gp to the cost).

### Construction

_Waxwork Creature;_ **CL** varies (equal to the waxwork creature's HD); **Price** 1,000 gp per HD
plus cost of wax

**Requirements** [Craft Construct](ref/feat/craft-construct),
[animate objects](ref/spell/animate-objects), [make whole](ref/spell/make-whole); **Skill**
[Craft](ref/skill/craft-any) (sculpture); **Cost** 500 gp per HD plus cost of wax
