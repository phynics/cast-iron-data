+++
id = "ref/rule/terrain-improvements"
kind = "rule"
title = "Terrain Improvements"
source_ids = ["ultimate-campaign"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "terrain_improvements", path = "json/rules_campaign_types04.json" },
]
[[sources]]
publication = "ultimate-campaign"
page = "210"

[fields]
kind = "none"
+++

Terrain improvements are changes to a hex that improve the land for your kingdom's use, such as
cultivating fields, digging mines, and clearing forests for lumber. The following list describes
common improvements. An improvement marked with an asterisk (\*) can share the same hex as other
improvements.

Some terrain improvements affect a settlement's Defense, which is used in the
[mass combat rules](ref/rule/mass-combat).

**Terrain:** This indicates what kind of hex you can build this terrain improvement in.

**Effect:** This line states the effect the terrain improvement has on that hex (or in some cases,
your entire kingdom).

If an improvement says you can upgrade it into another improvement, you can do so by paying the cost
difference between the two improvements. When the upgrade is complete, you lose the benefit of the
old improvement but gain the benefit of the new improvement.

**Cost:** This line gives the cost in BP to build the terrain improvement.

### Table 4-6: Terrain and Terrain Improvements

|Terrain|Exploration Time^[1](ref/rule/terrain-improvements#footnote-1)^|Preparation Time^[2](ref/rule/terrain-improvements#footnote-2)^|Preparation Cost^[3](ref/rule/terrain-improvements#footnote-3)^|Farm Cost^[4](ref/rule/terrain-improvements#footnote-4)^|Road Cost^[5](ref/rule/terrain-improvements#footnote-5)^ ^[6](ref/rule/terrain-improvements#footnote-6)^|
| --- | --- | --- | --- | --- | --- |
|Cavern^[7](ref/rule/terrain-improvements#footnote-7)^|3 days|3 months|8 BP|-|4 BP|
|Coastline^[8](ref/rule/terrain-improvements#footnote-8)^|Special|Special|Special|Special|Special|
|Desert|2 days|1 month|4 BP|8 BP|4 BP|
|Forest|2 days|2 months|4 BP|-|2 BP|
|Hills|1 day|1 month|2 BP|4 BP|3 BP|
|Jungle|2 days|4 months|12 BP|-|4 BP|
|Marsh|3 days|3 months|8 BP|-|4 BP|
|Mountains|3 days|4 months|12 BP|-|4 BP|
|Plains|1 day|Immediate|1 BP|2 BP|1 BP|
|Water|2 days|-|-|-|-|

###### ^1^ {#footnote-1}

Exploration time represents how many days a typical scouting party requires to explore a hex of this
type. These times assume a party speed of 30 feet. For parties with different speeds, see
[Table 3-3: Exploration Time (1 Hex)](ref/rule/movement-ucp). Treat Cavern as Mountain and Jungle as
Marsh for exploration time. Do not adjust the speed for Water hexes; it's assumed that the party is
already using a boat or other watercraft to explore.

###### ^2^ {#footnote-2}

Preparation time represents the months of labor (beginning with the current turn) required to
prepare the hex for settlement. Construction of buildings can begin in the current month for
settlements built on plains.

###### ^3^ {#footnote-3}

Preparation cost represents the BP cost to clear a hex of this type in preparation for founding a
settlement.

###### ^4^ {#footnote-4}

Farm cost represents the BP cost to cultivate a hex for farming. A Farm must be within or adjacent
to a hex containing a river, lake, swamp, or Canal, or adjacent to at least 2 hexes that already
contain Farms.

###### ^5^ {#footnote-5}

Road cost represents the BP cost to establish a Road that crosses a hex and connects to all adjacent
hexes. The cost to build a Road doubles if the hex contains rivers. A kingdom with a Size of 26 or
greater can build a Highway (or upgrade a Road to a Highway).

###### ^6^ {#footnote-6}

If the hex contains any rivers, double the listed cost to reflect the need to build bridges.

###### ^7^ {#footnote-7}

This is a large system of caves and underground passages and can be found in any terrain type except
Marsh. It functions as an additional hex that exists underground, below the surface hex.

###### ^8^ {#footnote-8}

Treat this as the adjacent land terrain type for all purposes.
