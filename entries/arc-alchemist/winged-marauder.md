+++
id = "ref/arc-alchemist/winged-marauder"
kind = "archetype"
title = "Winged Marauder"
aon = "ArchetypeDisplay.aspx?FixedName=Alchemist%20Winged%20Marauder"
source_ids = ["monster-codex"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "winged_marauder", path = "json/archetypes_alchemist2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/alchemist" },
]
[[sources]]
publication = "monster-codex"
page = "104"

[fields]
kind = "archetype"
replaces = ["Mutagen", "persistent mutagen"]
+++

Goblin alchemists have created a mixture of pheromones that they use to manipulate and entice giant
vultures or dire bats to do their bidding. These goblins strap harnesses to the chests of these
flying animals and hang beneath them, dropping flaming alchemical solutions on the helpless folks
below.

**Prerequisites:** Goblin

**Gained class skills:** acro, ha, ride

**Lost class skills:** dd, soh, umd

**Flying Beast Tamer (Ex)**

**Ability:** A winged marauder acquires a flying mount as an
[animal companion](ref/sidekick/animal-companion). This works as the druid animal companion class
feature, except the marauder must select a [dire bat](ref/companion/dire-bat) or
[giant vulture](ref/companion/vulture-giant). The marauder's effective druid level is equal to his
alchemist level.

**Gained:** At 1st Level

**Replaces:** Mutagen, persistent mutagen

**Special:** A marauder and his companion don't gain the _share spells_ ability.

**Discovery**

**Passive:** A winged marauder can select the following additional discovery.

**Sipping Pet (Ex)**

**Prereq:** The [infusion](ref/discovery/infusion) discovery.

**Standard:** The marauder can administer a dose of a liquid (such as an extract, infusion, potion,
or an alchemical liquid like [antitoxin](ref/eq-misc/antitoxin)) to his animal companion, even if
the companion is unconscious. The alchemist must be adjacent to or riding the companion to use this
ability.
