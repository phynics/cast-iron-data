+++
id = "ref/arc-unchained-summoner/construct-caller"
kind = "archetype"
title = "Construct Caller"
aon = "ArchetypeDisplay.aspx?FixedName=Summoner%20%28Unchained%29%20Construct%20Caller"
source_ids = ["construct-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "construct_caller", path = "json/archetypes_summoner_UC.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/unchained-summoner" },
]
[[sources]]
publication = "construct-handbook"
page = "10"

[fields]
kind = "archetype"
features = [
  { anchor = "construct-eidolon", level = 1 },
  { anchor = "planar-tinkering", level = 3 },
]
trades = [
  { replaces = "Summon monster I", feature = "summon-monster-i", by = ["planar-tinkering"] },
  { alters = "Eidolon", feature = "eidolon", by = ["construct-eidolon"] },
]
+++

Construct callers use their mechanical and planar understandings to work planar energies as a
tinkerer works parts. They use this understanding to hand-craft unique, constructed eidolons.

## Construct Eidolon (Ex) {#construct-eidolon}

A construct caller must select the [inevitable](ref/eidolon/inevitable) subtype for her eidolon. A
construct eidolon functions as an inevitable eidolon except as noted here. A construct eidolon can
be of any alignment. It has no Constitution score and gains bonus hit points appropriate for a
construct of its size. At 12th level, the construct eidolon gains DR 5/adamantine instead of DR
5/chaotic.

This alters eidolon.

## Planar Tinkering (Ex) {#planar-tinkering}

At 3rd level, a construct caller learns to better shape planar energy to improve her eidolon. The
number of points in her eidolon's evolution pool increases by 1. The number of points in the
eidolon's evolution pool increases by an additional 1 at 7th level and every 4 levels thereafter,
for a total of 5 additional points at 19th level.

This replaces _summon monster I_.
