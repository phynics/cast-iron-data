+++
id = "ref/arc-ranger/wild-shadow"
kind = "archetype"
title = "Wild Shadow"
aon = "ArchetypeDisplay.aspx?FixedName=Ranger%20Wild%20Shadow"
source_ids = ["advanced-race-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "wild_shadow", path = "json/archetypes_ranger.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/ranger" },
]
[[sources]]
publication = "advanced-race-guide"
page = "45"

[fields]
kind = "archetype"
features = [
  { anchor = "wild-at-heart", level = 1 },
  { anchor = "favored-terrain", level = 3 },
  { anchor = "woodland-stride", level = 4 },
  { anchor = "unfettered-step", level = 7 },
  { anchor = "harrying-attack", level = 11 },
  { anchor = "wild-stalker", level = 14 },
  { anchor = "master-of-terrain", level = 19 },
]
trades = [
  { replaces = "Hunter's bond", feature = "hunter-s-bond", by = ["woodland-stride"] },
  { replaces = "Ranger's woodland stride class feature gained at 7th level", feature = "woodland-stride", by = ["unfettered-step"] },
  { replaces = "Quarry", feature = "quarry", by = ["harrying-attack"] },
  { replaces = "Camouflage", feature = "camouflage", by = ["wild-stalker"] },
  { replaces = "Improved quarry", feature = "improved-quarry", by = ["master-of-terrain"] },
  { alters = "Track", feature = "track", by = ["wild-at-heart"] },
  { alters = "wild empathy", feature = "wild-empathy", by = ["wild-at-heart"] },
  { alters = "Favored terrain", feature = "favored-terrain", by = ["favored-terrain"] },
]
+++

The isolation that some [half-elves](ref/race/half-elf) feel leads them to live a life of isolation
amid the wild places of the world. Such rangers stalk the wild like shadows, creating close bonds
with the wild itself instead of seeking the solace and aid of companions. While ill at ease within
cities and other urban areas, they are adept at using the terrain to tactical advantage; they dart
through brambles and rough terrain with uncommon grace and use the land itself to lock down enemies.
A wild shadow has the following class features.

## Wild at Heart (Ex) {#wild-at-heart}

At 1st level, a wild shadow adds only 1/2 his class level when making wild empathy checks while in
urban areas, and adds only 1/4 his class level to follow or identify tracks in such areas. In
non-urban settings, he is considered two levels higher when determining the bonuses for such checks.
This ability alters the track and wild empathy class features.

## Favored Terrain (Ex) {#favored-terrain}

At 3rd level, when a wild shadow chooses a favored terrain, he cannot choose urban as the terrain
type. Furthermore, at 8th level and every five levels thereafter, when he chooses a new favorite
terrain type, he cannot choose the urban terrain type. This ability alters the favored terrain class
feature.

## Woodland Stride (Ex) {#woodland-stride}

This ability functions as the 7th-level ranger class feature
[of the same name](ref/ability/woodland-stride), but the wild shadow gains it at 4th level instead.
This ability replaces the hunter's bond class feature.

## Unfettered Step (Ex) {#unfettered-step}

At 7th level, a wild shadow's woodland stride class feature functions in any
[difficult terrain](ref/rule/terrain-and-obstacles) within any of his favored terrains, even in
areas that are enchanted or magically manipulated to impede motion. This ability replaces the
ranger's woodland stride class feature gained at 7th level.

## Harrying Attack (Ex) {#harrying-attack}

At 11th level, a wild shadow can use his knowledge of terrain to make shrewd attacks in combat. Such
attacks can make foes fumble or cause them to become [entangled](ref/rule/entangled) within areas of
the wild shadow's favored terrain. As a standard action, the wild shadow denotes one target within
line of sight and within one of his favored terrains as his harried prey. Once the foe is so
designated, every time the wild shadow hits this harried prey with a melee or ranged weapon attack
(either manufactured or natural), that creature is entangled for 1 round. A wild shadow can have no
more than one harried prey at a time and that creature must correspond to one of his favored enemy
types. He can dismiss this effect at any time as a free action, be he cannot select a new harried
prey for 24 hours. If the wild shadow sees proof that his harried prey is dead, he can select a new
harried prey after waiting 1 hour. This ability replaces the quarry class feature.

## Wild Stalker (Ex) {#wild-stalker}

At 14th level, a wild shadow learns to better use natural surroundings to obscure his position in
combat. Whenever a wild shadow is within one of his favored terrains and a feature of that terrain
grants him [cover](ref/rule/cover), the bonuses to AC and Reflex saves for that cover improve by 1.
Additionally, while he is within one of his favored terrains, if he gains
[concealment](ref/rule/concealment) or total concealment, the miss chance of either type of
concealment improves by 10%. Furthermore, at 16th level and 19th level, the bonuses granted by cover
increase by 1 and the miss chance increases by another 10% (maximum +3 and +30% respectively at 20th
level). This ability replaces the camouflage class feature.

## Master of Terrain (Ex) {#master-of-terrain}

At 19th level, a wild shadow can use his harrying attack against creatures other than his favored
enemy or he can spend a standard action to designate up to two of his favored enemies as his harried
prey instead. This ability replaces the improved quarry class feature.
