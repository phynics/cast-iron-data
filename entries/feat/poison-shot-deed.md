+++
id = "ref/feat/poison-shot-deed"
kind = "feat"
title = "Poison Shot Deed"
aon = "FeatDisplay.aspx?ItemName=Poison%20Shot%20Deed"
source_ids = ["dirty-tactics-toolbox"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "poison_shot_deed", path = "json/feat12.json" },
]
relations = [
  { kind = "prerequisite", target = "ref/feat/amateur-gunslinger", label = "or" },
]
[[sources]]
publication = "dirty-tactics-toolbox"
page = "9"

[fields]
kind = "feat"
feat_types = ["Grit"]
prerequisites = "Amateur Gunslinger or grit class feature."
prerequisite_feats = ["ref/feat/amateur-gunslinger"]
benefit = "You can spend 1 grit point to load your firearm with 1 dose of inhaled or ingested poison as a move action. This action has no chance of exposing you to the poison (as if you had the poison use class feature). Shooting a firearm loaded with a poison in this manner is a standard action that provokes attacks of opportunity and sprays out the poison in a 15-foot cone. Any creatures caught in the blast take no damage but are exposed to this poison and must each immediately attempt a save against the poison as though the onset time had elapsed."
+++

## Poison Shot Deed (Grit)

You can specially prepare bullets to deliver poisons that are normally used more subtly.\
**Prerequisites:** [Amateur Gunslinger](ref/feat/amateur-gunslinger) or grit class feature.\
**Benefit:** You can spend 1 grit point to load your firearm with 1 dose of inhaled or ingested
poison as a move action. This action has no chance of exposing you to the poison (as if you had the
[poison use](ref/ability/poison-use) class feature). Shooting a firearm loaded with a poison in this
manner is a standard action that provokes attacks of opportunity and sprays out the poison in a
15-foot cone. Any creatures caught in the blast take no damage but are exposed to this poison and
must each immediately attempt a save against the poison as though the onset time had elapsed.
