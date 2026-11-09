+++
id = "ref/feat/scapegoat"
kind = "feat"
title = "Scapegoat"
source_ids = ["blood-of-the-coven"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "scapegoat", path = "json/feat13.json" },
]
relations = [
  { kind = "prerequisite", target = "ref/feat/great-fortitude", label = "or" },
  { kind = "prerequisite", target = "ref/feat/iron-will", label = "or" },
]
[[sources]]
publication = "blood-of-the-coven"
page = "20"

[fields]
kind = "feat"
prerequisites = "Great Fortitude or Iron Will."
prerequisite_feats = ["ref/feat/great-fortitude", "ref/feat/iron-will"]
benefit = "You gain a +2 bonus on saving throws against curses. Once per day as a standard action, you can touch a creature suffering from a curse effect in an attempt to remove that curse from its target. You must attempt a character level check against the DC of the curse effect you wish to absorb. If you succeed, the curse is removed from the target but immediately affects you instead as if you were the original target and had failed your initial saving throw against the curse; you are subject to the curse's effects, removal conditions, and remaining duration."
+++

Your calloused soul attracts curses, even those afflicting others, and you have grown resistant to
their effects.\
**Prerequisites:** [Great Fortitude](ref/feat/great-fortitude) or [Iron Will](ref/feat/iron-will).\
**Benefit:** You gain a +2 bonus on saving throws against curses. Once per day as a standard action,
you can touch a creature suffering from a curse effect in an attempt to remove that curse from its
target. You must attempt a character level check against the DC of the curse effect you wish to
absorb. If you succeed, the curse is removed from the target but immediately affects you instead as
if you were the original target and had failed your initial saving throw against the curse; you are
subject to the curse's effects, removal conditions, and remaining duration.
