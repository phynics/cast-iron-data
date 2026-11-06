+++
id = "ref/feat/grab-and-go"
kind = "feat"
title = "Grab and Go"
source_ids = ["martial-arts-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "grab_and_go", path = "json/feat07.json" },
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
benefit = "As a free action, you can pick up an unattended item as part of a movement. Picking up the item does not provoke an attack of opportunity. If you have Throw Anything, you can pick up a number of closely gathered items that could be held in one hand (such as dishes from a stack of plates) equal to your Dexterity modifier (minimum 1). You must have a hand free to use this feat."
+++

## Grab and Go (Combat)

**Sources:** Martial Arts Handbook pg 8

You can snatch up an item to use as a weapon in the blink of an eye.\
**Prerequisites:** [Catch Off-Guard](ref/feat/catch-off-guard) or
[Throw Anything](ref/feat/throw-anything), base attack bonus +1.\
**Benefit:** As a free action, you can pick up an unattended item as part of a movement. Picking up
the item does not provoke an attack of opportunity. If you have Throw Anything, you can pick up a
number of closely gathered items that could be held in one hand (such as dishes from a stack of
plates) equal to your Dexterity modifier (minimum 1). You must have a hand free to use this feat.
