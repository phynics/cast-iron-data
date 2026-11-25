+++
id = "ref/arc-rogue/deadly-courtesan"
kind = "archetype"
title = "Deadly Courtesan"
aon = "ArchetypeDisplay.aspx?FixedName=Rogue%20Deadly%20Courtesan"
source_ids = ["advanced-race-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "deadly_courtesan", path = "json/archetypes_rogue.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/rogue" },
]
[[sources]]
publication = "advanced-race-guide"
page = "208"

[fields]
kind = "archetype"
features = [
  { anchor = "bardic-performance", level = 2 },
  { anchor = "inspire-competence", level = 3 },
  { anchor = "performance-strike", level = 8 },
]
trades = [
  { replaces = "Rogue trick gained at 2nd level", feature = "rogue-talents", levels = [2], by = ["bardic-performance"] },
  { replaces = "All levels of trap sense", feature = "trap-sense", by = ["inspire-competence"] },
  { replaces = "Improved uncanny dodge", feature = "improved-uncanny-dodge", by = ["performance-strike"] },
]
+++

Skilled at manipulation and diversion, the deadly courtesan builds up those around her and
periodically takes them down. She can be a spy, entertainer, assassin, bodyguard, or just an
intimate to someone who needs it most. A deadly courtesan has the following class features.

## Class Skills {#class-skills}

At 1st level, a deadly courtesan adds Knowledge (history) and Knowledge (nobility) to her list of
class skills and removes Knowledge (dungeoneering) from her list of class skills.

## Bardic Performance (Su) {#bardic-performance}

At 2nd level, a deadly courtesan gains the bardic performance ability and the
[fascinate](ref/performance/fascinate) bardic performance. Her fascinate DC is 10 + 1/2 her rogue
level + her Charisma modifier. She can use this bardic performance for a number of rounds per day
equal to 1 + her Charisma modifier. At each level after 2nd, she can use bardic performance for 1
additional round per day. If the courtesan also has bard levels, she may use these rounds for either
class's fascinate bardic performance, and her bard and rogue levels stack for determining her
fascinate DC. This ability replaces the rogue trick gained at 2nd level.

## Inspire Competence (Su) {#inspire-competence}

At 3rd level, a deadly courtesan can use her bardic performance to
[inspire competence](ref/performance/inspire-competence). The bonus begins at +2 and increases by +1
for every six levels the courtesan has attained beyond 3rd (+3 at 9th and +4 at 15th). This ability
replaces all levels of trap sense.

## Performance Strike (Sp) {#performance-strike}

At 8th level, as a swift action, a deadly courtesan may expend rounds of bardic performance to gain
a morale bonus on one attack roll. The amount of the bonus is equal to the number of bardic
performance rounds expended (maximum bonus equal to 1/2 her deadly courtesan level). This ability
replaces improved uncanny dodge.

## Rogue Talents {#rogue-talents}

The following rogue talents complement the deadly courtesan archetype: finesse rogue, stand up
(_Core Rulebook_); charmer, coax information, fast fingers, honeyed words (_Advanced Player's
Guide_); convincing lie, deft palm (_Ultimate Combat_).

## Advanced Talents {#advanced-talents}

The following advanced rogue talents complement the deadly courtesan archetype: slippery mind (_Core
Rulebook_); master of disguise (_Advanced Player's Guide_); rumormonger, unwitting ally (_Ultimate
Combat_).
