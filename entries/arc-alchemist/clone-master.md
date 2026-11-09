+++
id = "ref/arc-alchemist/clone-master"
kind = "archetype"
title = "Clone Master"
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
replaces = ["Bombs", "Poison resistance +6", "poison immunity"]
+++

Clone masters practice duplicating existing creatures in order to better understand how to create
new life. A clone master has the following class features.

**Bomb**

**Passive:** A clone master's bombs deal damage one die step lower than normal (regular bombs deal
d4s, [concussive bombs](ref/discovery/concussive-bomb) deal 1d3s, and so on).

**Replaces:** Bombs

**Lesser Simulacrum**

**Gained:** At 7th Level

**Passive:** A clone master adds [lesser simulacrum](ref/spell/simulacrum-lesser) to his formula
book as a 3rd-level extract.

**Rebirth**

**Ability:** A clone master can prepare a clone of himself that awakens if he is slain. Creating the
clone costs 5,000 gp, takes 1 week of work, and requires 3 additional weeks for the clone to grow to
maturity. If he dies, the clone awakens as if the alchemist had used the [clone](ref/spell/clone)
spell on himself. He can have one inert of himself at a time. Unused clones created by a clone
master do not rot.

**Gained:** At 8th Level

**Replaces:** Poison resistance +6, poison immunity

**Simulacrum**

**Gained:** At 13th Level

**Passive:** A clone master adds [simulacrum](ref/spell/simulacrum) to his formula book as a
5th-level extract.

**Clone**

**Gained:** At 16th Level

**Passive:** A clone master adds _[clone](ref/spell/clone)_ to his formula book as a 6th-level
extract.

**Discoveries:** The following discoveries complement the clone master archetype:
[alchemical simulacrum](ref/discovery/alchemical-simulacrum),
[doppelganger simulacrum](ref/discovery/doppelganger-simulacrum),
[preserve organs](ref/discovery/preserve-organs), and
[parasitic twin](ref/discovery/parasitic-twin).
