+++
id = "ref/arc-investigator/cartographer"
kind = "archetype"
title = "Cartographer"
source_ids = ["ultimate-wilderness"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "cartographer", path = "json/archetypes_investigator.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/investigator" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "56"

[fields]
kind = "archetype"
replaces = ["Poison lore", "poison resistance", "Keen recollection", "Swift alchemy"]
+++

Cartographers are eager trailblazers who explore uncharted terrain, study landmarks, and find new
paths through the wilderness. They record this information meticulously so that those who follow in
their footsteps can travel swiftly and safely within the studied area. Rather than studying poisons
like many investigators do, cartographers use their alchemical expertise to create better inks that
allow them to draw maps with incredible level of detail.

**Studied Terrain (Ex)**

**Action:** Ability

**Gained:** At 2nd Level

**Replaces:** Poison lore, poison resistance

A cartographer can expend one use of _inspiration_ to sketch a map and take notes of his
surroundings. Drawing the map takes 10 minutes. While he is within the studied area, the
cartographer can use _inspiration_ on Acrobatics, Climb, Fly, Ride, Stealth, Survival, and Swim
checks without expending a use of _inspiration,_ provided he is trained in the skill. If he already
has the ability to use _inspiration_ on any of these skills without expending a use of
_inspiration,_ he gains an additional +1 bonus on checks with that skill while in the studied area.

A cartographer can draw three types of maps (described below). He cannot combine different map types
in the same map, and areas within range that would belong in the other categories are excluded.

Much like alchemy, cartography requires materials, but the cost of those materials is negligible.
However, knowing an area so well as to gain these benefits requires more than just paper and ink - a
great deal of memorization and a bit of inspiration are also required. For this reason, a
cartographer can maintain these benefits in only one area at a time. The benefits remain in effect
until the cartographer studies a new area or refreshes his _inspiration pool._

**Dungeon Map**

**Ability:** While indoors, underground, or in any other type of environment where visibility is
limited by walls, the radius is 100 feet per level, and only areas that the cartographer has
explored within the past 24 hours count as _studied terrain._ Areas explored after drawing the map
do not retroactively become part of the \*studied terrain.

**Overland Map**

**Ability:** In natural terrain, the radius of the mapped area is equal to 1 mile per investigator
level. If he is unable to see the whole area, he extrapolates and uses his knowledge of geography to
fill in the blanks.

**Town Map**

**Ability:** While in an urban area or ruins, the radius is 1,000 feet per level or the entirety of
the urban or ruined area, whichever is smaller.

**Geographic Lore (Ex)**

**Ability:** A cartographer gains a deeper understanding of wilderness terrain. Whenever he is on
the Material Plane, he can determine where true north is as a **full-round action**. Furthermore, he
can create and sell maps to earn a number of gold pieces per week of dedicated work equal to half
his Knowledge (geography) check result per week.

**Gained:** At 3rd Level

**Replaces:** Keen recollection

**Swift Travels (Ex)**

**Gained:** At 4th Level

**Passive:** While in _studied terrain,_ a cartographer intuitively knows the easiest, shortest, and
fastest way through the wilderness. For the purpose of determining
[overland speed](ref/rule/overland-movement), the cartographer treats any trackless terrain as
though he were on a trail, and he treats any terrain with a road or trail as though it were a
highway. He can extend the benefit to up to one creature per investigator level traveling with him.

**Replaces:** Swift alchemy
