+++
id = "ref/arc-hunter/flood-flourisher"
kind = "archetype"
title = "Flood Flourisher"
aon = "ArchetypeDisplay.aspx?FixedName=Hunter%20Flood%20Flourisher"
source_ids = ["people-of-the-wastes"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "flood_flourisher", path = "json/archetypes_hunter.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/hunter" },
]
[[sources]]
publication = "people-of-the-wastes"
page = "20"

[fields]
kind = "archetype"
features = [
  { anchor = "twin-hunters" },
  { anchor = "skilled-ambusher", level = 3 },
  { anchor = "watery-stride", level = 5 },
  { anchor = "water-striker", level = 6 },
  { anchor = "submerged-stealth", level = 8 },
  { anchor = "aquatic-action", level = 9 },
  { anchor = "sudden-strike", level = 12 },
  { anchor = "fast-submerged-stealth", level = 15 },
  { anchor = "fast-swimmer", level = 18 },
]
trades = [
  { replaces = "Hunter tactics", feature = "hunter-tactics", by = ["twin-hunters"] },
  { replaces = "The teamwork feat gained at 3rd level", feature = "teamwork-feat", levels = [3], by = ["skilled-ambusher"] },
  { replaces = "Woodland stride", feature = "woodland-stride", by = ["watery-stride"] },
  { replaces = "The teamwork feat gained at 6th level", feature = "teamwork-feat", levels = [6], by = ["water-striker"] },
  { replaces = "Swift tracker", feature = "swift-tracker", by = ["submerged-stealth"] },
  { replaces = "The teamwork feat gained at 9th level", feature = "teamwork-feat", levels = [9], by = ["aquatic-action"] },
  { replaces = "The teamwork feat gained at 12th level", feature = "teamwork-feat", levels = [12], by = ["sudden-strike"] },
  { replaces = "The teamwork feat gained at 15th level", feature = "teamwork-feat", levels = [15], by = ["fast-submerged-stealth"] },
  { replaces = "The teamwork feat gained at 18th level", feature = "teamwork-feat", levels = [18], by = ["fast-swimmer"] },
]
+++

Well adapted to their drenched surroundings, flood flourishers coordinate deadly ambushes with their
loyal animal companions by capitalizing on their mastery of the soggy terrain.

## Twin Hunters (Ex) {#twin-hunters}

Each time a flood flourisher gains a benefit from this archetype, she also grants the benefit to her
animal companion.

This replaces hunter tactics.

## Skilled Ambusher (Ex) {#skilled-ambusher}

At 3rd level, a flood flourisher gains either [Athletic](ref/feat/athletic) or
[Stealthy](ref/feat/stealthy) as a bonus feat.

This replaces the teamwork feat gained at 3rd level.

## Watery Stride (Ex) {#watery-stride}

At 5th level, a flood flourisher and her animal companion gain a swim speed equal to their base land
speed (maximum 30 feet). A flood flourisher or animal companion that already has a swim speed
instead gains a +10 bonus on Acrobatics checks to avoid provoking attacks of opportunity from
swimming out of a threatened square.

This replaces woodland stride.

## Water Striker (Ex) {#water-striker}

At 6th level, a flood flourisher gains the benefits of either
[Shot on the Run](ref/feat/shot-on-the-run) or [Spring Attack](ref/feat/spring-attack), even if she
does not meet either of the feats' prerequisites. She gains the benefits of this feat only while
using her swim speed.

This replaces the teamwork feat gained at 6th level.

## Submerged Stealth (Ex) {#submerged-stealth}

At 8th level, a flood flourisher learns how to ambush targets from beneath the muck, becoming a
silent threat. While in a deep bog, the flood flourisher can use cover from the water to attempt
Stealth checks with no penalties from the natural environment. While in a deep bog, as long as she
moves no more than 5 feet in a round, she has [tremorsense](ref/umr/tremorsense) out to a range of
30 feet against anything that moves within the same body of water. While underwater in a deep bog,
she can [hold her breath](ref/misc/hold-your-breath) for a number of minutes equal to 6 times her
Constitution score before she risks drowning.

This replaces swift tracker.

## Aquatic Action (Ex) {#aquatic-action}

At 9th level, a flood flourisher gains the benefits of the
[aquatic action](ref/vigtalent/aquatic-action) vigilante talent (see below).

This replaces the teamwork feat gained at 9th level.

## Sudden Strike (Ex) {#sudden-strike}

At 12th level, a flood flourisher can better take advantage of the element of surprise. She can take
a full round's worth of actions during the surprise round, rather than a single standard action or
move action.

This replaces the teamwork feat gained at 12th level.

## Fast Submerged Stealth (Ex) {#fast-submerged-stealth}

At 15th level, a flood flourisher can move up to her full swim speed with no penalty while using
Stealth in a deep bog, and she can maintain her [tremorsense](ref/umr/tremorsense) from her
submerged stealth while doing so.

This replaces the teamwork feat gained at 15th level.

## Fast Swimmer (Ex) {#fast-swimmer}

At 18th level, a flood flourisher increases her swim speed by 20 feet.

This replaces the teamwork feat gained at 18th level.
