+++
id = "ref/feat/wave-strike"
kind = "feat"
title = "Wave Strike"
aon = "FeatDisplay.aspx?ItemName=Wave%20Strike"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "wave_strike", path = "json/feat17.json" },
]
relations = [
  { kind = "prerequisite", target = "ref/feat/quick-draw", label = "or" },
]
[[sources]]
publication = "ultimate-combat"
page = "123"

[fields]
kind = "feat"
feat_types = ["Combat"]
prerequisites = "Weapon expertise class feature or Quick Draw, Bluff 1 rank."
prerequisite_feats = ["ref/feat/quick-draw"]
benefit = "If on your first turn of combat you draw a melee weapon to attack an opponent within your reach, you can spend a swift action to make a Bluff check to feint against that opponent."
+++

## Wave Strike (Combat)

You present a serene facade until you unsheathe your weapon and strike in one fluid motion.\
**Prerequisites:** Weapon expertise class feature or [Quick Draw](ref/feat/quick-draw), Bluff 1
rank.\
**Benefit:** If on your first turn of combat you draw a melee weapon to attack an opponent within
your reach, you can spend a swift action to make a Bluff check to [feint](ref/rule/feint) against
that opponent.
