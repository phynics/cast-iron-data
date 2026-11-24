+++
id = "ref/arc-rogue/roof-runner"
kind = "archetype"
title = "Roof Runner"
aon = "ArchetypeDisplay.aspx?FixedName=Rogue%20Roof%20Runner"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "roof_runner", path = "json/archetypes_rogue.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/rogue" },
]
[[sources]]
publication = "ultimate-combat"
page = "74"

[fields]
kind = "archetype"
features = [
  { anchor = "roof-running", level = 1 },
  { anchor = "tumbling-descent", level = 2 },
]
trades = [
  { replaces = "Trapfinding", feature = "trapfinding", by = ["roof-running"] },
  { replaces = "Trap sense", feature = "trap-sense", by = ["tumbling-descent"] },
]
+++

A specialized urban acrobat, the roof runner makes her home high atop the spires and gables of great
cities. She is skilled at traveling these uneven surfaces at full speed, performing daring leaps and
deftly balancing upon narrow and precarious ledges.

## Roof Running (Ex) {#roof-running}

At 1st level, a roof runner becomes entirely adept at moving across the tops of buildings, spires,
and similar locations. Provided she is wearing light armor or no armor, the roof runner can move at
full speed while traveling across the tops of buildings or similar structures, and takes no
penalties on any Dexterity-based Skill checks or Reflex saves that might be incurred from moving
about on a roof. This ability replaces trapfinding.

## Tumbling Descent (Ex) {#tumbling-descent}

At 2nd level, a roof runner can use her acrobatics skill to attempt a rapid descent from a rooftop
or another surface, ricocheting against another surface and then diving through an opening (such as
a balcony or window) directly below. So long as she has at least two surfaces no farther than 10
feet apart to bounce against, she can ricochet her body back from one to the next, descending great
distances with a single check. The DC is 10 + 5 for every additional 10-foot increment descended
beyond the initial 10 feet dropped. If she fails, she falls the full distance. This ability replaces
trap sense.

## Rogue Talents {#rogue-talents}

The following rogue talents complement the roof runner archetype: expert leaper, ledge walker,
nimble climber, stand up, and terrain mastery.

## Advanced Talents {#advanced-talents}

The following advanced rogue talent complements the roof runner archetype: fast tumble.
