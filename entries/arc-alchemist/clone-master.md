+++
id = "ref/arc-alchemist/clone-master"
kind = "archetype"
title = "Clone Master"
aon = "ArchetypeDisplay.aspx?FixedName=Alchemist%20Clone%20Master"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "clone_master", path = "json/archetypes_alchemist.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/alchemist" },
]
[[sources]]
publication = "ultimate-magic"
page = "18"

[fields]
kind = "archetype"
features = [
  { anchor = "bomb", level = 1 },
  { anchor = "lesser-simulacrum", level = 7 },
  { anchor = "rebirth", level = 8 },
  { anchor = "simulacrum", level = 13 },
  { anchor = "clone", level = 16 },
]
trades = [
  { replaces = "Bombs", feature = "bomb", by = ["bomb"] },
  { replaces = "Poison resistance +6", feature = "poison-resistance", levels = [8], by = ["rebirth"] },
  { replaces = "poison immunity", feature = "poison-resistance", levels = [10], by = ["rebirth"] },
]
+++

Clone masters practice duplicating existing creatures in order to better understand how to create
new life. A clone master has the following class features.

## Bomb {#bomb}

A clone master's bombs deal damage one die step lower than normal (regular bombs deal d4s,
[concussive bombs](ref/discovery/concussive-bomb) deal 1d3s, and so on). This otherwise functions as
and replaces the standard alchemist bomb class feature.

## Lesser Simulacrum {#lesser-simulacrum}

At 7th level, a clone master adds _[lesser simulacrum](ref/spell/simulacrum-lesser)_ to his formula
book as a 3rd-level extract.

## Rebirth {#rebirth}

At 8th level, a [clone](ref/spell/clone) master can prepare a clone of himself that awakens if he is
slain. Creating the clone costs 5,000 gp, takes 1 week of work, and requires 3 additional weeks for
the clone to grow to maturity. If he dies, the clone awakens as if the alchemist had used the
_clone_ spell on himself. He can have one inert of himself at a time. Unused clones created by a
clone master do not rot. This ability replaces poison resistance +6 and poison immunity.

## Simulacrum {#simulacrum}

At 13th level, a clone master adds _[simulacrum](ref/spell/simulacrum)_ to his formula book as a
5th-level extract.

## Clone {#clone}

At 16th level, a [clone](ref/spell/clone) master adds _clone_ to his formula book as a 6th-level
extract.

## Discoveries {#discoveries}

The following discoveries complement the clone master archetype:
[alchemical simulacrum](ref/discovery/alchemical-simulacrum),
[doppelganger simulacrum](ref/discovery/doppelganger-simulacrum),
[preserve organs](ref/discovery/preserve-organs), and
[parasitic twin](ref/discovery/parasitic-twin).
