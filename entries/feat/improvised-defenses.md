+++
id = "ref/feat/improvised-defenses"
kind = "feat"
title = "Improvised Defenses"
source_ids = ["martial-arts-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "improvised_defenses", path = "json/feat09.json" },
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
benefit = "You gain a +1 shield bonus to AC when you are wielding an improvised weapon and have your other hand free."
+++

## Improvised Defenses (Combat)

**Sources:** Martial Arts Handbook pg 9

You can deftly defend yourself with makeshift weapons.\
**Prerequisites:** [Catch Off-Guard](ref/feat/catch-off-guard) or
[Throw Anything](ref/feat/throw-anything), base attack bonus +1.\
**Benefit:** You gain a +1 shield bonus to AC when you are wielding an
[improvised weapon](ref/misc/improvised-weapons) and have your other hand free.
