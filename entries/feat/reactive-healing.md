+++
id = "ref/feat/reactive-healing"
kind = "feat"
title = "Reactive Healing"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "reactive_healing", path = "json/feat13.json" },
]
relations = [
  { kind = "prerequisite", target = "ref/feat/quick-channel", label = "or" },
  { kind = "prerequisite", target = "ref/feat/quicken-spell", label = "or" },
]
[[sources]]
publication = "advanced-class-guide"
page = "155"

[fields]
kind = "feat"
prerequisites = "Quick Channel or Quicken Spell; channel energy or lay on hands class feature."
prerequisite_feats = ["ref/feat/quick-channel", "ref/feat/quicken-spell"]
benefit = "When the damage from an attack or an effect would reduce you to 0 or fewer hit points, you can expend one use of channel energy (of a form that would heal you) or lay on hands as an immediate action to heal yourself. The healing affects only you, even if it would normally affect others."
+++

You can channel healing energy in response to an attack that would knock you unconscious.\
**Prerequisites:** [Quick Channel](ref/feat/quick-channel) or
[Quicken Spell](ref/feat/quicken-spell); [channel energy](ref/ability/channel-energy) or
[lay on hands](ref/ability/lay-on-hands) class feature.\
**Benefit:** When the damage from an attack or an effect would reduce you to 0 or fewer hit points,
you can expend one use of channel energy (of a form that would heal you) or lay on hands as an
immediate action to heal yourself. The healing affects only you, even if it would normally affect
others.
