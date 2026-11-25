+++
id = "ref/arc-alchemist/bogborn-alchemist"
kind = "archetype"
title = "Bogborn Alchemist"
aon = "ArchetypeDisplay.aspx?FixedName=Alchemist%20Bogborn%20Alchemist"
source_ids = ["advanced-race-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "bogborn_alchemist", path = "json/archetypes_alchemist.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/alchemist" },
]
[[sources]]
publication = "advanced-race-guide"
page = "191"

[fields]
kind = "archetype"
features = [
  { anchor = "amphibious-mutagen", level = 1 },
  { anchor = "discovery-options" },
]
trades = [
  { replaces = "Throw anything", feature = "throw-anything", by = ["amphibious-mutagen"] },
]
+++

Some grippli alchemists are particularly attuned to the swamps and the dangerous creatures that
inhabit them; these serve as their laboratories and research subjects, respectively. These bogborn
alchemists have the following class features.

## Class Skills {#class-skills}

A bogborn alchemist adds Swim to his list of class skills.

## Amphibious Mutagen (Ex) {#amphibious-mutagen}

At 1st level, when a bogborn alchemist uses a mutagen, he may choose to have his mutagen form
enhanced for aquatic movement. This gives him the [amphibious](ref/umr/amphibious) special quality,
his feet elongate, and the webbing between his fingers and toes expands, granting a swim speed of 15
feet. This replaces throw anything.

## Discovery Options {#discovery-options}

A bogborn alchemist can select the toxic skin [grippli](ref/race/grippli) racial trait in place of
an alchemical discovery.

## Discoveries {#discoveries}

The following discoveries complement the bogborn alchemist archetype:
[chameleon](ref/discovery/chameleon) (_Advanced Race Guide_);
[concentrate poison](ref/discovery/concentrate-poison), [sticky poison](ref/discovery/sticky-poison)
(_Advanced Player's Guide_); [nauseating flesh](ref/discovery/nauseating-flesh),
[poison conversion](ref/discovery/poison-conversion) (_Ultimate Combat_);
[bottled ooze](ref/discovery/bottled-ooze), [tanglefoot bomb](ref/discovery/tanglefoot-bomb),
[tentacle](ref/discovery/tentacle) (_Ultimate Magic_).
