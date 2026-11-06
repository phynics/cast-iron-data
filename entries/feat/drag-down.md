+++
id = "ref/feat/drag-down"
kind = "feat"
title = "Drag Down"
source_ids = ["ultimate-combat", "pathfinder-unchained"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "drag_down", path = "json/feat05.json" },
]

[fields]
kind = "feat"
feat_types = ["Combat"]
prerequisites = "Int 13, Combat Expertise, Improved Trip."
prerequisite_feats = ["ref/feat/combat-expertise", "ref/feat/improved-trip"]
benefit = "Whenever an opponent successfully trips you, you can attempt to trip that opponent as an immediate action."
+++

## Drag Down (Combat)

**Sources:** Ultimate Combat pg 98

When you are knocked prone, you are skilled at bringing your opponent down with you.\
**Prerequisites:** Int 13, [Combat Expertise](ref/feat/combat-expertise),
[Improved Trip](ref/feat/improved-trip).\
**Benefit:** Whenever an opponent successfully trips you, you can attempt to [trip](ref/rule/trip)
that opponent as an immediate action.

### Stamina

**Sources:** Pathfinder Unchained pg 118\
You can select this feat even if you don't meet the ability score prerequisite (Intelligence 13).
You gain the benefit of this feat only as long as you have at least 1 stamina point in your stamina
pool. If your retributive trip combat maneuver from Drag Down succeeds by 10 or more, you can spend
5 stamina points to stand up from prone without provoking an attack of opportunity as part of the
same immediate action as the trip attempt.
