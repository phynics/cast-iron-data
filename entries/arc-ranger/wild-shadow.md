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
replaces = ["Hunter's bond", "Woodland stride", "Quarry", "Camouflage", "Improved quarry"]
alters = ["Track", "wild empathy", "Favored terrain"]
+++

The isolation that some [half-elves](ref/race/half-elf) feel leads them to live a life of isolation
amid the wild places of the world. Such rangers stalk the wild like shadows, creating close bonds
with the wild itself instead of seeking the solace and aid of companions. While ill at ease within
cities and other urban areas, they are adept at using the terrain to tactical advantage; they dart
through brambles and rough terrain with uncommon grace and use the land itself to lock down enemies.
A wild shadow has the following class features.

**Prerequisites:** Half-elf

**Wild at Heart (Ex)**

**Alters:** Track, wild empathy

**Gained:** At 1st Level

**Passive:** A wild shadow adds only 1/2 his class level when making _wild empathy_ checks while in
urban areas, and adds only 1/4 his class level to follow or identify tracks in such areas. In
non-urban settings, he is considered two levels higher when determining the bonuses for such checks.

**Favored Terrain (Ex)**

**Alters:** Favored terrain

**Info:** When a wild shadow chooses a _favored terrain,_ he cannot choose urban as the terrain
type. Furthermore, when he chooses a new _favored terrain_ type, he cannot choose the urban terrain
type.

**Gained:** At 3rd Level

**Woodland Stride (Ex)**

**At 4th Level:** This ability functions as the 7th-level ranger class feature
[of the same name](ref/ability/woodland-stride), but the wild shadow gains it at 4th level instead.

**Replaces:** Hunter's bond

**Unfettered Step (Ex)**

**Ability:** A wild shadow's _woodland stride_ class feature functions in any
[difficult terrain](ref/rule/terrain-and-obstacles) within any of his _favored terrains,_ even in
areas that are enchanted or magically manipulated to impede motion.

**Gained:** At 7th Level

**Replaces:** Woodland stride

**Harrying Attack (Ex)**

**Flavor:** A wild shadow can use his knowledge of terrain to make shrewd attacks in combat. Such
attacks can make foes fumble or cause them to become entangled within areas of the wild shadow's
_favored terrain._

**Gained:** At 11th Level

**Replaces:** Quarry

**Special:** He can dismiss this effect at any time as a **free action**, but he cannot select a new
_harried prey_ for 24 hours. If the wild shadow sees proof that his _harried prey_ is dead, he can
select a new _harried prey_ after waiting 1 hour.

**Standard:** The wild shadow denotes one target within line of sight and within one of his _favored
terrains_ as his _harried prey._ Once the foe is so designated, every time the wild shadow hits this
_harried prey_ with a melee or ranged weapon attack (either manufactured or natural), that creature
is [entangled](ref/rule/entangled) for 1 round. A wild shadow can have no more than one _harried
prey_ at a time and that creature must correspond to one of his _favored enemy_ types.

**Wild Stalker (Ex)**

**Flavor:** A wild shadow learns to better use natural surroundings to obscure his position in
combat.

**Gained:** At 14th Level

**Passive:** Whenever a wild shadow is within one of his _favored terrains_ and a feature of that
terrain grants him [cover](ref/rule/cover), the bonuses to AC and Reflex saves for that cover
improve by 1. Additionally, while he is within one of his _favored terrains,_ if he gains
[concealment](ref/rule/concealment) or total concealment, the miss chance of either type of
concealment improves by 10%.

**Repeat:** The bonuses granted by cover increase by 1 and the miss chance increases by another
10%., 16, 3

**Replaces:** Camouflage

**Master of Terrain (Ex)**

**Choice:** A wild shadow can use his _harrying attack_ against creatures other than his _favored
enemy_ or he can spend a **standard action** to designate up to two of his _favored enemies_ as his
_harried prey_ instead.

**Gained:** At 19th Level

**Replaces:** Improved quarry
