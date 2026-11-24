+++
id = "ref/arc-monk/treetop-monk"
kind = "archetype"
title = "Treetop Monk"
aon = "ArchetypeDisplay.aspx?FixedName=Monk%20Treetop%20Monk"
source_ids = ["advanced-race-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "treetop_monk", path = "json/archetypes_monk2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/monk" },
]
[[sources]]
publication = "advanced-race-guide"
page = "206"

[fields]
kind = "archetype"
features = [
  { anchor = "branch-runner", level = 3 },
  { anchor = "wood-affinity", level = 5 },
  { anchor = "freedom-of-movement", level = 12 },
]
trades = [
  { replaces = "Still mind", feature = "still-mind", by = ["branch-runner"] },
  { replaces = "Purity of body", feature = "purity-of-body", by = ["wood-affinity"] },
  { replaces = "Abundant step", feature = "abundant-step", by = ["freedom-of-movement"] },
]
+++

While many vanaras follow traditional monastic training and traditions, others learn to blend exotic
combat and the mysterious forces of ki with the natural world, allowing them to move through trees
and overgrowth to deliver devastating attacks. A treetop monk has the following class features.

**Prerequisites:** Vanara

## Branch Runner (Ex) {#branch-runner}

At 3rd level, a treetop monk adds half the base speed bonus from his fast movement ability to his
racial climb speed. This ability replaces still mind.

## Wood Affinity (Su) {#wood-affinity}

At 5th level, a treetop monk may expend 1 point from his ki pool as a free action to treat a wooden
object as if it were not broken for 1 minute (this includes a weapon with a wooden haft such as an
axe or spear). At 8th level, as a free action, a treetop monk can expend 1 point from his ki pool to
use the [Lunge](ref/feat/lunge) feat with any wooden or wood-hafted melee weapon. This ability
replaces purity of body.

## Freedom of Movement (Su) {#freedom-of-movement}

At 12th level, a treetop may expend 1 point from his ki pool as a swift action to gain the effects
of _[freedom of movement](ref/spell/freedom-of-movement)_ for 1 round. This ability replaces
abundant step.
