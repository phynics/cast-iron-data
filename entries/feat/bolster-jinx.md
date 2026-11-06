+++
id = "ref/feat/bolster-jinx"
kind = "feat"
title = "Bolster Jinx"
source_ids = ["halflings-of-golarion"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "bolster_jinx", path = "json/feat02.json" },
]
relations = [
  { kind = "prerequisite", target = "ref/feat/great-fortitude", label = "or" },
  { kind = "prerequisite", target = "ref/feat/iron-will", label = "or" },
  { kind = "prerequisite", target = "ref/feat/lightning-reflexes", label = "or" },
]

[fields]
kind = "feat"
prerequisites = "Great Fortitude, Iron Will, or Lightning Reflexes; Halfling Jinx trait."
prerequisite_feats = ["ref/feat/great-fortitude", "ref/feat/iron-will", "ref/feat/lightning-reflexes"]
benefit = "A jinxed target's penalty on Fortitude, Reflex, or Will saves increases by 2 if you have the Great Fortitude, Lightning Reflexes, or Iron Will feat, respectively. If you have more than one of these feats, the additional penalties apply to all of the corresponding saves."
+++

**Sources:** Halflings of Golarion pg 26

Your ability to resist certain effects somehow makes it even harder for creatures you jinx to do the
same.\
**Prerequisites:** [Great Fortitude](ref/feat/great-fortitude), [Iron Will](ref/feat/iron-will), or
[Lightning Reflexes](ref/feat/lightning-reflexes); Halfling Jinx trait.\
**Benefit:** A jinxed target's penalty on Fortitude, Reflex, or Will saves increases by 2 if you
have the Great Fortitude, Lightning Reflexes, or Iron Will feat, respectively. If you have more than
one of these feats, the additional penalties apply to all of the corresponding saves.
