+++
id = "ref/rule/walls-uc"
kind = "rule"
title = "Walls"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "walls_uc", path = "json/rules_rulesets02.json" },
]

[fields]
kind = "none"
+++

**Sources:** Ultimate Combat pg 167

The walls that guard castles and cities are sturdy fortifications, usually constructed in a series
of 5-foot squares. A square of wall has an AC of 5, and [hardness](ref/umr/hardness) and hit points
equal to its type.

Squares of walls can be magically treated. Doing so doubles the [hardness](ref/umr/hardness) and hit
points. Magically treating wall squares costs 500 gp per wall square. A spellcaster with the
[Craft Magic Arms and Armor](ref/feat/craft-magic-arms-and-armor) feat can magically treat walls.

When a wall gains the broken condition, its [hardness](ref/umr/hardness) is halved, but the wall is
not breached. Only destroying a section of wall allows it to become breached. When a square of wall
is breached, any sections directly above it fall onto the missing section of walls. Doing this
reduces the falling wall section to half its current hit point total -1, which applies the broken
condition to that square of wall.

### Table 3-19: Walls

|Material|Hardness|Hit Points per 5-Foot Square|
| --- | --- | --- |
|Wood|5|30|
|Stone|8|45|
|Iron or steel|10|90|
|Adamantine|20|120|
