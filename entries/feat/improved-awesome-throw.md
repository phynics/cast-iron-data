+++
id = "ref/feat/improved-awesome-throw"
kind = "feat"
title = "Improved Awesome Throw"
aon = "FeatDisplay.aspx?ItemName=Improved%20Awesome%20Throw"
source_ids = ["pathfinder-91-battle-of-bloodmarch-hills"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "improved_awesome_throw", path = "json/feat08.json" },
]
relations = [
  { kind = "prerequisite", target = "ref/feat/throw-anything", label = "or" },
]
[[sources]]
publication = "pathfinder-91-battle-of-bloodmarch-hills"
page = "69"

[fields]
kind = "feat"
feat_types = ["Combat"]
prerequisites = "Str 25, Awesome Throw, Greater Bull Rush, Throw Anything or rock throwing, size Large or larger."
prerequisite_feats = ["ref/feat/awesome-throw", "ref/feat/greater-bull-rush", "ref/feat/throw-anything"]
benefit = "When you make an awesome throw combat maneuver, for every 5 by which your combat maneuver check exceeds the target's CMD, you send the target flying 5 additional feet. Furthermore, this movement provokes attacks of opportunity from your allies."
+++

## Improved Awesome Throw (Combat)

When you perform an awesome throw, you knock opponents back farther.\
**Prerequisites:** Str 25, [Awesome Throw](ref/feat/awesome-throw),
[Greater Bull Rush](ref/feat/greater-bull-rush), [Throw Anything](ref/feat/throw-anything) or
[rock throwing](ref/umr/rock-throwing), size Large or larger.\
**Benefit:** When you make an awesome throw combat maneuver, for every 5 by which your combat
maneuver check exceeds the target's CMD, you send the target flying 5 additional feet. Furthermore,
this movement provokes attacks of opportunity from your allies.
