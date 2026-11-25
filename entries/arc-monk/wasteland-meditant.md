+++
id = "ref/arc-monk/wasteland-meditant"
kind = "archetype"
title = "Wasteland Meditant"
aon = "ArchetypeDisplay.aspx?FixedName=Monk%20Wasteland%20Meditant"
source_ids = ["ultimate-wilderness"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "wasteland_meditant", path = "json/archetypes_monk2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/monk" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "64"

[fields]
kind = "archetype"
features = [
  { anchor = "dehydrating-strike", level = 1 },
  { anchor = "vigor", level = 2 },
  { anchor = "desert-strider", level = 4 },
  { anchor = "improved-vigor", level = 9 },
  { anchor = "pillar-of-salt", level = 15 },
]
trades = [
  { replaces = "Stunning fist", feature = "stunning-fist", by = ["dehydrating-strike"] },
  { replaces = "Evasion", feature = "evasion", by = ["vigor"] },
  { replaces = "Slow fall", feature = "slow-fall", by = ["desert-strider"] },
  { replaces = "Improved evasion", feature = "improved-evasion", by = ["improved-vigor"] },
  { replaces = "Quivering palm", feature = "quivering-palm", by = ["pillar-of-salt"] },
]
+++

Some monks journey to remote and isolated corners of the world to find serenity and a heightened
sense of awareness.

## Dehydrating Strike (Su) {#dehydrating-strike}

As a free action as part of a melee attack, a wasteland meditant can draw the moisture out of a
living creature damaged by his unarmed strike. Unless the creature succeeds at a Will save (DC =
10 + half the monk's level + his Wisdom modifier), the creature is [fatigued](ref/misc/fatigued) for
a number of rounds equal to half the wasteland meditant's level (minimum 1). At 5th level, the
creature struck is also [staggered](ref/misc/staggered) for 1 round if it fails its save. At 10th
level, a creature that fails its save is [exhausted](ref/misc/exhausted) instead of fatigued.

When used against a plant creature or a creature with the water subtype, dehydrating strike inflicts
the above conditions (as applicable) on a failed save and also deals 1d6 points of damage, plus 1d6
additional points of damage at 4th level and every 4 levels thereafter. This damage is in addition
to the wasteland meditant's normal unarmed strike damage. A wasteland meditant can use this ability
a number of times per day equal to 3 + his Wisdom modifier but only once per round.

Creatures immune to critical hits or precision damage are immune to this ability.

This replaces stunning fist.

## Vigor (Ex) {#vigor}

At 2nd level, when a wasteland meditant succeeds at a Fortitude save against an effect with a
partial effect on a successful save, he instead suffers no effect.

This replaces evasion.

## Desert Strider (Ex) {#desert-strider}

At 4th level, a wasteland meditant ignores movement penalties for
[difficult terrain](ref/rule/terrain-and-obstacles) when in desert terrain. Additionally, he kicks
up dust around his body whenever he performs a double move action in desert terrain. This dust
grants the wasteland meditant [concealment](ref/rule/concealment). The miss chance granted by this
concealment starts at 10% at 4th level and increases by 10% at 6th level and every 2 levels
thereafter, to a maximum of 80% at 18th level. This concealment lasts until the start of the
meditant's next turn and stacks with any concealment provided by movement, such as from the
[Wind Stance](ref/feat/wind-stance) feat.

This replaces slow fall.

## Improved Vigor (Ex) {#improved-vigor}

At 9th level, a wasteland meditant's [vigor](ref/spell/vigor) ability improves. He still takes no
damage on a successful Fortitude saving throw against attacks, but henceforth he takes only half
damage on a failed save.

This replaces improved evasion.

## Pillar of Salt (Su) {#pillar-of-salt}

At 15th level, a wasteland meditant can transform a creature's body into a column of crumbling salt
with a touch. He can use pillar of salt once per day as part of an unarmed strike, and he must
announce his intent before making his attack roll. Creatures immune to critical hits or
transmutation effects cannot be affected. A creature successfully damaged by the wasteland
meditant's unarmed strike must succeed at a Fortitude saving throw (DC = 10 + half the monk's
level + his Wisdom modifier) or begin to calcify. Each round thereafter, the target of pillar of
salt takes 2 points of [Strength and Dexterity drain](ref/rule/ability-damage-drain) and gains a +1
bonus to its natural armor as a crust of salt begins to cover its body and restrict movement. These
effects take place every round at the start of the wasteland meditant's turn and continue for 1
round per level the wasteland meditant has. If the target is reduced to 0 Strength or Dexterity at
any time during this duration, the creature is instantly killed and its body is transformed into a
pillar of salt. A creature killed in this way can't be brought back to life except by
_[miracle](ref/spell/miracle)_, _[true resurrection](ref/spell/true-resurrection)_, or
_[wish](ref/spell/wish)_. Total immersion in water suppresses the ongoing effects of pillar of salt
but resets the accumulated natural armor bonus to zero. As long as the target lives, the ongoing
effect of pillar of salt can be ended via a _[heal](ref/spell/heal)_ spell.

This replaces quivering palm.
