+++
id = "ref/arc-alchemist/first-world-innovator"
kind = "archetype"
title = "First World Innovator"
source_ids = ["legacy-of-the-first-world"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "first_world_innovator", path = "json/archetypes_alchemist.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/alchemist" },
]
[[sources]]
publication = "legacy-of-the-first-world"
page = "6"

[fields]
kind = "archetype"
replaces = ["Brew Potion", "poison use", "swift poisoning", "poison immunity", "Poison resistance"]
alters = ["Bombs"]
replaces_features = ["brew-potion", "poison-use", "swift-poisoning", "poison-resistance"]
+++

The First World's energies slowly leak into the Material Plane, haphazardly infusing mundane
reagents with unpredictable power. Those who can harness these unusual substances - called primal
reagents - walk a fine line between genius and catastrophe.

**Primal Reagents (Su)**

**Action:** Ability

**At 10th Level:** Whenever the First World innovator or would use a dose of primal reagents to
alter the damage type of a bomb, the bomb deals acid, cold, electricity, fire, force, or sonic
damage (determine the type randomly) instead of its normal damage. Additionally, whenever the First
World innovator would use a dose to gain an additional effect for a mutagen, he may roll 1d6 for the
effect, adding to the list of options above: 5) the mutagen grants immunity to poison and paralysis;
or 6) one numeric benefit of the mutagen (such as the natural armor bonus) selected by the First
World innovator increases by 1d3.

**At 6th Level:** The alchemist can expend multiple doses of primal reagents to apply multiple
effects. When throwing a bomb, he can expend 2 doses to change both the bomb's damage type and
damage dealt. When imbibing an elixir or potion, he can expend an additional number of doses equal
to the extract's or potion's spell level to increase its caster level by 2 instead of 1. When
imbibing a mutagen, he can expend 2 doses to roll twice for additional effects, applying both
results.

**Replaces:** Brew Potion, poison use, swift poisoning, poison immunity

By spending 10 minutes patrolling his surroundings after recovering his daily extract slots, a First
World innovator can gather a number of doses of primal reagents equal to
[half](ref/misc/fractions-and-rounding) his alchemist level + his Intelligence modifier. Primal
reagents retain their potency until the next time the First World innovator regains his extract
slots. As part of the same action used to consume an extract, imbibe a potion, throw a bomb, or
drink his mutagen, the First World innovator can expend 1 dose of primal reagents for additional
effects as described below.

**Bomb:** Expending 1 dose can change either the bomb's damage type or its damage dealt. When
changing the damage type, the bomb deals acid (1), cold (2), electricity (3), or fire (4) damage
(roll 1d4 to determine the type randomly) instead of its normal damage. When changing the bomb's
damage dealt, the bomb's die size [increases by one step](ref/misc/damage-die-adjustments) (for
example, increasing 1d6 to 1d8), but it deals 1 less point of damage per die rolled.

**Extract or Potion:** Expending 1 dose increases the caster level of the extract or potion by 1.

**Mutagen:** Expending 1 dose grants the First World innovator an additional effect for the duration
of the mutagen, determined at random (by rolling 1d4):

1. Halve all benefits provided by the mutagen.
1. Imbibing the mutagen immediately either heals 1d4 points of
  [ability damage](ref/rule/ability-damage-drain) to one ability score (if applicable) or restores a
  number of hit points equal to 2d8 plus the First World innovator's alchemist level.
1. The mutagen grants the First World innovator his choice of the benefits of the
  [lingering spirit](ref/discovery/lingering-spirit),
  [preserve organs](ref/discovery/preserve-organs), or
  [spontaneous healing](ref/discovery/spontaneous-healing) alchemist discoveries. He cannot select a
  discovery if he does not meet its prerequisites.
1. The mutagen grants the First World innovator his choice of the benefits of the
  [feral mutagen](ref/discovery/feral-mutagen), [tentacle](ref/discovery/tentacle),
  [vestigial arm](ref/discovery/vestigial-arm), or [wings](ref/discovery/wings) alchemist
  discoveries. He cannot select a discovery if he does not meet its prerequisites.

**Limited Bombs (Su)**

**Alters:** Bombs

**Passive:** A First World innovator can use a number of bombs per day equal to half his class
level + his Intelligence modifier (minimum 1) per day.

**Refined Reagents (Su)**

**Ability:** Whenever the First World innovator expends a dose of primal reagents to roll a die to
apply a randomized outcome to his bombs or mutagen, he can expend 1 additional dose to ignore the
result and roll again; he must take the second result.

**Gained:** At 2nd Level

**Replaces:** Poison resistance
