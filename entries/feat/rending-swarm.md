+++
id = "ref/feat/rending-swarm"
kind = "feat"
title = "Rending Swarm"
source_ids = ["blood-of-the-beast"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "rending_swarm", path = "json/feat13.json" },
]
[[sources]]
publication = "blood-of-the-beast"
page = "23"

[fields]
kind = "feat"
feat_types = ["Combat", "Teamwork"]
prerequisites = "Dex 15, Rat Stack, swarming racial trait."
prerequisite_feats = ["ref/feat/rat-stack"]
benefit = "You gain a +1 bonus on all melee damage rolls for each allied creature you share a square with that also has this feat."
+++

## Rending Swarm (Combat, Teamwork)

Together, you and your allies tear through enemies' defenses.\
**Prerequisites:** Dex 15, [Rat Stack](ref/feat/rat-stack), swarming racial trait.\
**Benefit:** You gain a +1 bonus on all melee damage rolls for each allied creature you share a
square with that also has this feat.

If two or more allies sharing a square have this feat and hit the same adjacent creature in a round,
they tear it in different directions, dealing additional damage at the end of the round. This rend
attack deals an amount of damage equal to 1d6 + the highest Strength modifier of all qualifying
allies in the same square who struck the target this round.
