+++
id = "ref/feat/makeshift-maneuvers"
kind = "feat"
title = "Makeshift Maneuvers"
source_ids = ["martial-arts-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "makeshift_maneuvers", path = "json/feat10.json" },
]
relations = [
  { kind = "prerequisite", target = "ref/feat/catch-off-guard", label = "or" },
  { kind = "prerequisite", target = "ref/feat/throw-anything", label = "or" },
]

[fields]
kind = "feat"
feat_types = ["Combat"]
prerequisites = "Catch Off-Guard or Throw Anything, base attack bonus +1."
prerequisite_feats = ["ref/feat/catch-off-guard", "ref/feat/throw-anything"]
benefit = "When you wield an improvised weapon, it gains the disarm and trip weapon properties."
+++

## Makeshift Maneuvers (Combat)

**Sources:** Martial Arts Handbook pg 9

Your skill with improvised weapons allows you to use them to hamper your opponents.\
**Prerequisites:** [Catch Off-Guard](ref/feat/catch-off-guard) or
[Throw Anything](ref/feat/throw-anything), base attack bonus +1.\
**Benefit:** When you wield an [improvised weapon](ref/misc/improvised-weapons), it gains the
[disarm](ref/rule/disarm) and [trip](ref/rule/trip) weapon properties.
