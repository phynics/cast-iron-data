+++
id = "ref/arc-bard/dervish-dancer"
kind = "archetype"
title = "Dervish Dancer"
aon = "ArchetypeDisplay.aspx?FixedName=Bard%20Dervish%20Dancer"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "dervish_dancer", path = "json/archetypes_bard.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/bard" },
]
[[sources]]
publication = "ultimate-combat"
page = "32"

[fields]
kind = "archetype"
features = [
  { anchor = "battle-dance", level = 1 },
  { anchor = "rain-of-blows", level = 6 },
  { anchor = "razor-s-kiss", level = 8 },
  { anchor = "leaf-on-the-wind", level = 14 },
  { anchor = "fleet" },
  { anchor = "versatile-dance", level = 2 },
  { anchor = "dance-of-fury", level = 12 },
  { anchor = "battle-fury", level = 20 },
]
trades = [
  { replaces = "Proficiency with the rapier and whip", feature = "weapon-and-armor-proficiencies", power = "weapons" },
  { replaces = "Suggestion", feature = "bardic-performance", power = "suggestion", by = ["rain-of-blows"] },
  { replaces = "mass suggestion", feature = "bardic-performance", power = "mass suggestion", by = ["rain-of-blows"] },
  { replaces = "Dirge of doom", feature = "bardic-performance", power = "dirge of doom", by = ["razor-s-kiss"] },
  { replaces = "Frightening performance", feature = "bardic-performance", power = "frightening tune", by = ["leaf-on-the-wind"] },
  { replaces = "Bardic knowledge", feature = "bardic-knowledge", by = ["fleet"] },
  { replaces = "lore master", feature = "lore-master", by = ["fleet"] },
  { replaces = "Versatile performance", feature = "versatile-performance", by = ["versatile-dance"] },
  { replaces = "Soothing performance", feature = "bardic-performance", power = "soothing performance", by = ["dance-of-fury"] },
  { replaces = "Deadly performance", feature = "bardic-performance", power = "deadly performance", by = ["battle-fury"] },
  { replaces = "Bardic performance", feature = "bardic-performance", by = ["battle-dance"] },
]
+++

Not all bards inspire others with their performances. Dervish dancers enter a near-mystical trance
that allows them to push their bodies beyond normal limits.

## Weapon and Armor Proficiency {#weapon-and-armor-proficiency}

Dervish dancers gain weapon proficiency with the [scimitar](ref/eq-weapon/scimitar) and
[kukri](ref/eq-weapon/kukri). This ability replaces their proficiency with the rapier and whip.

## Battle Dance {#battle-dance}

A dervish dancer is trained in the use of the Perform skill, especially dance, to create magical
effects on himself. This works like bardic performance, except the dervish dancer only affects
himself, and does not need to be able to see or hear his own performance. Battle dancing is treated
as bardic performance for the purposes of feats, abilities, effects, and the like that affect bardic
performance, except that battle dancing does not benefit from the
[Lingering Performance](ref/feat/lingering-performance) feat or any other ability that allows a
bardic performance to grant bonuses after it has ended. Battle dancing benefits apply only when the
bard is wearing light or no armor. Like bardic performance, it cannot be maintained at the same time
as other performance abilities.

Starting a battle dance is a move action, but it can be maintained each round as a free action.
Changing a battle dance from one effect to another requires the dervish dancer to stop the previous
performance and start the new one as a move action. Like a bard, a dervish dancer's performance ends
immediately if he is killed, paralyzed, stunned, knocked unconscious, or otherwise prevented from
taking a free action each round. A dervish dancer cannot perform more than one battle dance at a
time. At 10th level, a dervish dancer can start a battle dance as a swift action instead of a move
action.

Dervish dancers gain the inspire courage, inspire greatness, and inspire heroics bardic performance
types as battle dances, but these only provide benefit to the dervish dancer himself. This ability
replaces bardic performance.

## Rain of Blows (Su) {#rain-of-blows}

At 6th level, a dervish dancer can speed up his attacks. When making a
[full attack](ref/rule/full-attack) action, he may make one extra attack with any weapon he is
holding, as though under the effects of a _[haste](ref/spell/haste)_ spell. He also gains a +1 bonus
on attack rolls and a +1 dodge bonus to AC and on Reflex saves. At 9th level, and every three bard
levels thereafter, these bonuses increase by +1, to a maximum of +5 at 18th level. These bonuses do
not stack with the _[haste](ref/spell/haste)_ spell. This ability replaces suggestion and mass
suggestion.

## Razor's Kiss (Su) {#razor-s-kiss}

At 8th level, a dervish dancer can use his battle dance to improve his weapons' critical range. All
attacks he makes with manufactured weapons are treated as though he had the
[Improved Critical](ref/feat/improved-critical) feat. Natural weapons and spells are not affected.
This ability replaces dirge of doom.

## Leaf on the Wind (Su) {#leaf-on-the-wind}

At 14th level, a dervish dancer can use his battle dance to evade attacks with unearthly grace and
to shake off the effects of his wounds. Unlike other battle dances, leaf on the wind requires a
standard action each round to start or maintain the performance. Each round it is maintained,
including the first, the dervish dancer

gains a +6 dodge bonus to Armor Class and on

Reflex saves. If wounded, he heals 1 hit point

of damage per bard level. This ability

replaces frightening performance.

## Fleet (Su) {#fleet}

While performing a

battle dance, a dervish dancer

gains a +10 enhancement bonus

to his land speed. This bonus

increases by 5 feet for every

four bard levels gained after 1st

level, to a maximum of +30 feet

at 19th level. This ability replaces

bardic knowledge and lore master.

## Versatile Dance (Ex) {#versatile-dance}

At 2nd level, a dervish dancer

gains a bonus equal to [half](ref/misc/fractions-and-rounding) his level on Perform

(dance) checks. He can use his bonus for his Perform

(dance) skill in place of his bonus for Acrobatics. This

ability replaces versatile performance.

## Dance of Fury (Su) {#dance-of-fury}

At 12th level, a dervish dancer

can attack more than once as he moves while

performing a battle dance. He can combine a full-

attack action with a single move, taking the attacks

at any point during his movement, but must move

at least 5 feet between each attack. This movement

provokes attacks of opportunity as normal. This

ability replaces soothing performance.

## Battle Fury (Su) {#battle-fury}

At 20th level, the

dervish dancer can unleash a whirlwind

of blows while performing a battle dance.

As a full-round action, he can take a single

move action and unleash a single attack

at his highest bonus against each target

within his reach during any point of

his move, up to a maximum number of

attacks equal to the dervish dancer's

character level. This movement

provokes attacks of opportunity

as normal, and replaces

deadly performance.
