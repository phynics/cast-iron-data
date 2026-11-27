+++
id = "ref/arc-rogue/planar-sneak"
kind = "archetype"
title = "Planar Sneak"
aon = "ArchetypeDisplay.aspx?FixedName=Rogue%20Planar%20Sneak"
source_ids = ["planes-of-power"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "planar_sneak", path = "json/archetypes_rogue.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/rogue" },
]
[[sources]]
publication = "planes-of-power"
page = "8"

[fields]
kind = "archetype"
features = [
  { anchor = "planar-sense", level = 3 },
  { anchor = "elemental-execution", level = 4 },
]
trades = [
  { replaces = "Trap sense", feature = "trap-sense", by = ["planar-sense"] },
  { replaces = "Uncanny dodge", feature = "uncanny-dodge", by = ["elemental-execution"] },
  { replaces = "improved uncanny dodge", feature = "improved-uncanny-dodge", by = ["elemental-execution"] },
]
+++

A planar sneak finds creative ways to defy conventional limitations when trying to overcome
extraplanar obstacles.

## Planar Sense (Ex) {#planar-sense}

At 3rd level, a planar sneak gains a +1 bonus on saving throws against all effects with the air,
chaos, earth, evil, fire, good, law, or water descriptors. This bonus increases by 1 for every 3
rogue levels thereafter (to a maximum of +6 at 18th level).

This ability replaces trap sense.

## Elemental Execution (Su) {#elemental-execution}

At 4th level, a planar sneak treats creatures with the elemental subtype as though they were
vulnerable to her sneak attack, but she deals only half as much sneak attack damage as she normally
would. She can confirm critical hits against such creatures, though 50% of the time, the critical
hit is automatically negated and damage is instead rolled normally. At 8th level, this ability also
applies to all outsiders otherwise immune to critical hits and sneak attack damage.

This ability replaces uncanny dodge and improved uncanny dodge.

## Rogue Talents {#rogue-talents}

The following rogue talents complement the planar sneak archetype: guileful polyglot, strong stroke,
terrain mastery.

## Advanced Rogue Talents {#advanced-rogue-talents}

The following advanced rogue talents complement this archetype: defensive roll, hide in plain sight,
and skill mastery.
