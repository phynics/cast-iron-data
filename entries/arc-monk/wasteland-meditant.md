+++
id = "ref/arc-monk/wasteland-meditant"
kind = "archetype"
title = "Wasteland Meditant"
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
replaces = ["Stunning fist", "Evasion", "Slow fall", "Improved evasion", "Quivering palm"]
+++

Some monks journey to remote and isolated corners of the world to find serenity and a heightened
sense of awareness.

**Dehydrating Strike (Su)**

**At 1st Level:** As a **free action** as a part of a melee attack, a wasteland meditant can draw
the moisture out of a living creature damaged by his unarmed strike. Unless the creature succeeds at
a Will save (DC = 10 + half the monk's level + his Wisdom modifier), the creature is
[fatigued](ref/misc/fatigued) for a number of rounds equal to half the wasteland meditant's level
(minimum 1).

**At 10th Level:** A creature that fails its save is [exhausted](ref/misc/exhausted) instead of
fatigued.

**At 5th Level:** The creature struck is also [staggered](ref/misc/staggered) for 1 round if it
fails its save.

**Replaces:** Stunning fist

**Special:** Creatures immune to critical hits or precision damage are immune to this ability. When
used against a plant creature or a creature with the water subtype, dehydrating strike inflicts the
above conditions (as applicable) on a failed save and also deals damage equal to 1d6 + an additional
number of d6s equal to [one-fourth](ref/misc/fractions-and-rounding) of his monk level (2d6 total at
4th level, 3d6 at 8th level, etc.) This damage is in addition to the wasteland meditant's normal
unarmed strike damage.

**Usage:** 3 + Wisdom modifier times/day, but only once per round

**Usage:** 3 + Wisdom modifier times/day, but only once per round

**Vigor (Ex)**

**Gained:** At 2nd Level

**Passive:** When a wasteland meditant succeeds at a Fortitude save against an effect with a partial
effect on a successful save, he instead suffers no effect.

**Replaces:** Evasion

**Desert Strider (Ex)**

**Ability:** A wasteland meditant ignores movement penalties for
[difficult terrain](ref/rule/terrain-and-obstacles) when in desert terrain. Additionally, he kicks
up dust around his body whenever he performs a double **move action** in desert terrain. This dust
grants the wasteland meditant [concealment](ref/rule/concealment). The miss chance granted by this
concealment is 10%.

**Gained:** At 4th Level

**Replaces:** Slow fall

**Special:** This concealment lasts until the start of the meditant's next turn and stacks with any
concealment provided by movement, such as from the [Wind Stance](ref/feat/wind-stance) feat.

At 6th level: The concealment 20%.

At 8th level: The concealment 30%.

At 10th level: The concealment 40%.

At 12th level: The concealment 50%.

At 14th level: The concealment 60%.

At 16th level: The concealment 70%.

At 18th level: The concealment 80%.

**Improved Vigor (Ex)**

**Gained:** At 9th Level

**Passive:** A wasteland meditant's _[vigor](ref/spell/vigor)_ ability improves. He still takes no
damage on a successful Fortitude saving throw against attacks, but henceforth he takes only half
damage on a failed save.

**Replaces:** Improved evasion

**Pillar of Salt (Su)**

**Ability:** He can use _pillar of salt_ once per day as part of an unarmed strike, and he must
announce his intent before making his attack roll. Creatures immune to critical hits or
transmutation effects cannot be affected.

**Flavor:** A wasteland meditant can transform a creature's body into a column of crumbling salt
with a touch.

**Info:** A creature successfully damaged by the wasteland meditant's unarmed strike must succeed at
a Fortitude saving throw (DC = 10 + half the monk's level + his Wisdom modifier) or begin to
calcify. Each round thereafter, the target of _pillar of salt_ takes 2 points of
[Strength and Dexterity drain](ref/rule/ability-damage-drain) and gains a +1 bonus to its natural
armor as a crust of salt begins to cover its body and restrict movement. These effects take place
every round at the start of the wasteland meditant's turn and continue for 1 round per level the
wasteland meditant has.

**Gained:** At 15th Level

**Replaces:** Quivering palm

**Special:** If the target is reduced to 0 Strength or Dexterity at any time during this duration,
the creature is instantly killed and its body is transformed into a pillar of salt. A creature
killed in this way can't be brought back to life except by [miracle](ref/spell/miracle),
[true resurrection](ref/spell/true-resurrection), or [wish](ref/spell/wish). Total immersion in
water suppresses the ongoing effects of _pillar of salt_ but resets the accumulated natural armor
bonus to zero. As long as the target lives, the ongoing effect of _pillar of salt_ can be ended via
a [heal](ref/spell/heal) spell.
