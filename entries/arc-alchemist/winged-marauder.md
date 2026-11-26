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
features = [
  { anchor = "flying-beast-tamer", level = 1 },
]
trades = [
  { replaces = "Mutagen", feature = "mutagen", by = ["flying-beast-tamer"] },
  { replaces = "persistent mutagen", feature = "persistent-mutagen", by = ["flying-beast-tamer"] },
  { replaces = "Disable Device, Sleight of Hand, and Use Magic Device as class skills" },
]
+++

Goblin alchemists have created a mixture of pheromones that they use to manipulate and entice giant
vultures or dire bats to do their bidding. These goblins strap harnesses to the chests of these
flying animals and hang beneath them, dropping flaming alchemical solutions on the helpless folks
below.

## Class Skills {#class-skills}

A winged marauder gains Acrobatics, Handle Animal, and Ride as class skills. These replace Disable
Device, Sleight of Hand, and Use Magic Device as class skills.

## Flying Beast Tamer (Ex) {#flying-beast-tamer}

At 1st level, a winged marauder acquires a flying mount as an
[animal companion](ref/sidekick/animal-companion). This works as the druid animal companion class
feature, except the marauder must select a [dire bat](ref/companion/dire-bat) or
[giant vulture](ref/companion/vulture-giant). The marauder's effective druid level is equal to his
alchemist level. A marauder and his companion don't gain the share spells ability. This ability
replaces the mutagen and persistent mutagen class features.

## Discovery {#discovery}

A winged marauder can select the following additional discovery.

### Sipping Pet (Ex) {#sipping-pet}

As a standard action, the marauder can administer a dose of a liquid (such as an extract,
[infusion](ref/discovery/infusion), potion, or an alchemical liquid like
[antitoxin](ref/eq-misc/antitoxin)) to his animal companion, even if the companion is unconscious.
The alchemist must be adjacent to or riding the companion to use this ability. An alchemist must
have the infusion discovery to select this discovery.
