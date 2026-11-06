+++
id = "ref/feat/wave-strike"
kind = "feat"
title = "Wave Strike"
source_ids = ["ultimate-combat", "pathfinder-unchained"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "wave_strike", path = "json/feat17.json" },
]
relations = [
  { kind = "prerequisite", target = "ref/feat/quick-draw", label = "or" },
]

[fields]
kind = "feat"
feat_types = ["Combat"]
prerequisites = "Weapon expertise class feature or Quick Draw, Bluff 1 rank."
prerequisite_feats = ["ref/feat/quick-draw"]
benefit = "If on your first turn of combat you draw a melee weapon to attack an opponent within your reach, you can spend a swift action to make a Bluff check to feint against that opponent."
+++

## Wave Strike (Combat)

**Sources:** Ultimate Combat pg 123

You present a serene facade until you unsheathe your weapon and strike in one fluid motion.\
**Prerequisites:** Weapon expertise class feature or [Quick Draw](ref/feat/quick-draw), Bluff 1
rank.\
**Benefit:** If on your first turn of combat you draw a melee weapon to attack an opponent within
your reach, you can spend a swift action to make a Bluff check to [feint](ref/rule/feint) against
that opponent.

### Stamina

**Sources:** Pathfinder Unchained pg 135\
You can spend 2 stamina points to use this feat on your second or subsequent turns in a combat. You
can use this combat trick only once per combat, though you can use it in addition to using the feat
on your first turn.
