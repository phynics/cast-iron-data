+++
id = "ref/arc-druid/road-keeper"
kind = "archetype"
title = "Road Keeper"
aon = "ArchetypeDisplay.aspx?FixedName=Druid%20Road%20Keeper"
source_ids = ["ultimate-wilderness"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "road_keeper", path = "json/archetypes_druid2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/druid" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "48"

[fields]
kind = "archetype"
features = [
  { anchor = "one-with-the-road" },
  { anchor = "road-bond", level = 1 },
  { anchor = "take-the-high-road", level = 2 },
  { anchor = "trodden-path", level = 4 },
  { anchor = "road-less-traveled", level = 4 },
]
trades = [
  { replaces = "Spontaneous casting", feature = "spontaneous-casting", by = ["one-with-the-road"] },
  { replaces = "Wild empathy", feature = "wild-empathy", by = ["road-bond"] },
  { replaces = "Woodland stride", feature = "woodland-stride", by = ["take-the-high-road"] },
  { replaces = "Resist nature's lure", feature = "resist-nature-s-lure", by = ["trodden-path"] },
  { replaces = "Wild shape", feature = "wild-shape", by = ["road-less-traveled"] },
  { alters = "Nature bond", feature = "nature-bond", by = ["road-bond"] },
]
+++

Guardians of the lonely paths between cities, road keepers protect the wild from travelers, and
travelers from the wild.

## One with the Road (Su) {#one-with-the-road}

A road keeper casts the following spells as though her caster level were 1 higher:
1st—_longstrider_, 2nd—_scent trail_, 3rd—_nature's exile_, 4th—_freedom of movement_, 5th—_tree
stride_, 6th—_find the path_, 7th—_wind walk_, 8th—_word of recall_, 9th—_world wave_. At 9th level,
the bonus to her caster level for these spells increases to +2.

This replaces spontaneous casting.

## Road Bond (Ex) {#road-bond}

If the road keeper chooses a cleric domain as her nature bond, she must choose from the Community,
Liberation, [Protection](ref/domain/protection), [Travel](ref/domain/travel), or
[Weather](ref/domain/weather) domains. The road keeper can also choose any subdomain associated with
these domains.

This alters nature bond and replaces wild empathy.

## Take the High Road (Ex) {#take-the-high-road}

At 2nd level, a road keeper travels over roads and paths at an accelerated rate. She and her allies
can [hustle](ref/rule/overland-movement) for 2 hours without taking nonlethal damage, instead of 1,
provided they travel along a road or path. Additionally, as long as they travel on a road or path,
the road keeper and her allies count as traveling along a highway regardless of the quality of the
road or path on which they travel. Allies must remain within 30 feet of the road keeper to benefit
from this ability.

This replaces woodland stride.

## Trodden Path (Ex) {#trodden-path}

At 4th level, a road keeper gains a +4 bonus on Survival checks to follow or identify tracks. She
also gains this bonus on saving throws against severe weather effects.

This replaces resist nature's lure.

## Road Less Traveled (Su) {#road-less-traveled}

At 4th level, a road keeper can discourage creatures from entering or exiting the wild. Once per day
as a standard action, she can target a creature within 30 feet and curse it with clumsiness and
disorientation. The road keeper chooses whether to punish her target for entering the wild from a
road or building, or vice versa. If her target is entering the wild, it treats every square of
wilderness not on a road or in a building as [difficult terrain](ref/rule/terrain-and-obstacles). If
her target is exiting the wild, it treats every square on a road or inside a building as difficult
terrain. In either case, the ground feels uneven and the target suffers extreme vertigo during
movement. The victim of this curse can attempt a Will saving throw (DC = 10 +
[half](ref/misc/fractions-and-rounding) the road keeper's level + her Wisdom modifier) at the
beginning of its turn each round to end the effect. The effect lasts until the target successfully
saves or for a number of minutes equal to the road keeper's level. A creature's movement isn't
affected if it is burrowing, climbing, earth gliding, flying, or swimming. This is a mind-affecting
curse effect.

At 6th level and every 2 levels thereafter, the road keeper can target an additional creature per
day with this ability (to a maximum number of nine targets per day at 20th level). She can target
more than one creature with a single use of this ability or the same target more than once in the
same day (though its effects do not stack), but her total number of targets per day cannot exceed
this daily maximum. If she targets more than one creature at one time, each target must be within 30
feet of the road keeper.

This replaces wild shape.
