+++
id = "ref/arc-rogue/numerian-scavenger"
kind = "archetype"
title = "Numerian Scavenger"
aon = "ArchetypeDisplay.aspx?FixedName=Rogue%20Numerian%20Scavenger"
source_ids = ["technology-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "numerian_scavenger", path = "json/archetypes_rogue.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/rogue" },
]
[[sources]]
publication = "technology-guide"
page = "13"

[fields]
kind = "archetype"
features = [
  { anchor = "technic-training", level = 1 },
  { anchor = "lucky-glitch", level = 4 },
  { anchor = "robot-slayer", level = 8 },
]
trades = [
  { replaces = "Trapfinding", feature = "trapfinding", by = ["technic-training"] },
  { replaces = "Uncanny dodge", feature = "uncanny-dodge", by = ["lucky-glitch"] },
  { replaces = "Improved uncanny dodge", feature = "improved-uncanny-dodge", by = ["robot-slayer"] },
]
+++

A Numerian scavenger lives for the discovery of new technological wonders scraped from the depths of
the strange ruins, metal caverns, and outlandish junkyards of Numeria. She is well-versed in all the
ways that technology can be used to protect sites, as well as the ways in which it can malfunction.

## Technic Training (Ex) {#technic-training}

A Numerian scavenger adds 1/2 her rogue level to Perception skill checks to locate mechanical or
high-tech traps and to Disable Device skill checks against these traps (minimum +1). She gains
[Technologist](ref/feat/technologist) as a bonus feat. She cannot use Disable Device to disarm
magical traps. This ability replaces trapfinding.

## Lucky Glitch (Ex) {#lucky-glitch}

Starting at 4th level, whenever a Numerian scavenger triggers a
[glitch](ref/rule/timeworn-technology) when using a timeworn technological item, she rolls twice and
can choose which of the two glitch effects actually occurs. A Numerian scavenger always adds her
level to rolls to determine what kind of glitch occurs, and treats rolls of over 100 as 100. This
ability replaces uncanny dodge.

## Robot Slayer (Ex) {#robot-slayer}

At 8th level, a Numerian scavenger knows just where to strike robots to incapacitate and disable
them. When she deals sneak attack damage to a robot, she ignores all [hardness](ref/umr/hardness)
that robot possesses. This ability replaces improved uncanny dodge.
