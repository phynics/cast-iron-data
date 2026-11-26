+++
id = "ref/arc-rogue/okeno-liberator"
kind = "archetype"
title = "Okeno Liberator"
aon = "ArchetypeDisplay.aspx?FixedName=Rogue%20Okeno%20Liberator"
source_ids = ["inner-sea-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "okeno_liberator", path = "json/archetypes_rogue.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/rogue" },
]
[[sources]]
publication = "inner-sea-combat"
page = "41"

[fields]
kind = "archetype"
features = [
  { anchor = "bond-breaker", level = 1 },
  { anchor = "covert-commander", level = 3 },
  { anchor = "catch-off-guard", level = 4 },
]
trades = [
  { replaces = "Trapfinding", feature = "trapfinding", by = ["bond-breaker"] },
  { replaces = "Trap sense", feature = "trap-sense", by = ["covert-commander"] },
  { replaces = "Uncanny dodge", feature = "uncanny-dodge", by = ["catch-off-guard"] },
]
+++

The sight of yellow sails on the Inner Sea signals the approach of a ship from Okeno, home port of
the most ruthless and feared of all slaving operations. Most who see these sails flee in terror, but
some freedom fighters actually endeavor to be captured, knowing that being taken to Stonespine
Island in manacles is the easiest way to infiltrate the city, liberate other slaves, and lead them
to freedom.

## Bond Breaker (Ex) {#bond-breaker}

An Okeno liberator adds 1/2 her class level to Escape Artist checks, and never takes a penalty on
Disable Device checks when using improvised tools to open locks. This ability replaces trapfinding.

## Covert Commander (Ex) {#covert-commander}

An Okeno liberator grants all allies within 30 feet who are in her line of sight (but not herself) a
+1 competence bonus on Disguise and Stealth checks. This bonus increases by 1 for every 3 levels
beyond 3rd. This ability replaces trap sense.

## Catch Off-Guard (Ex) {#catch-off-guard}

At 4th level, the Okeno liberator is adept at improvising weapons. She gains
[Catch Off-Guard](ref/feat/catch-off-guard) as a bonus feat. This ability replaces uncanny dodge.

## Rogue Talents {#rogue-talents}

The following rogue talents complement the Okeno liberator archetype: deft palm, fast picks, fast
stealth, quick disguise, slow reactions, underhanded.

## Advanced Talents {#advanced-talents}

The following advanced rogue talents complement the Okeno liberator archetype: defensive roll, fast
tumble, knock-out blow, skill mastery, weapon snatcher.
