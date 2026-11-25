+++
id = "ref/arc-brawler/feral-striker"
kind = "archetype"
title = "Feral Striker"
aon = "ArchetypeDisplay.aspx?FixedName=Brawler%20Feral%20Striker"
source_ids = ["ultimate-wilderness"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "feral_striker", path = "json/archetypes_brawler.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/brawler" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "42"

[fields]
kind = "archetype"
features = [
  { anchor = "feral-aspect", level = 1 },
]
trades = [
  { replaces = "Martial flexibility", feature = "martial-flexibility", by = ["feral-aspect"] },
]
+++

A feral striker taps into a reservoir of druidic power hidden inside herself, allowing her to take
animalistic characteristics.

## Feral Aspect (Su) {#feral-aspect}

This functions as the [shifter aspect](ref/ability/aspects) class feature of the shifter, except the
feral striker can choose only from the [bear](ref/aspect/bear), [bull](ref/aspect/bull),
[falcon](ref/aspect/falcon), [snake](ref/aspect/snake), [stag](ref/aspect/stag),
[tiger](ref/aspect/tiger), and [wolf](ref/aspect/wolf) aspects. She has access to only the minor
versions all these aspects.

At 6th level, the feral striker can take on two minor aspects simultaneously as a move action. Each
aspect counts toward her total number of minutes (so if a feral striker who normally has 9 total
minutes of aspects takes on two aspects simultaneously for 4 minutes, she still has 1 minute
remaining). She can end one or both aspects as a free action on her turn.

At 10th level, the feral shifter adds her Constitution modifier to the total number of minutes per
day in which she can use feral aspect.

At 12th level, the feral striker can take on three aspects simultaneously as a move action or one or
two aspects as a swift action.

At 20th level, the feral striker can take on as many aspects as she wishes at once as a swift
action, and they count as only one aspect for the purpose of calculating duration.

This replaces martial flexibility.
