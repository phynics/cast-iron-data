+++
id = "ref/rule/consulting-a-guide"
kind = "rule"
title = "Consulting a Guide"
source_ids = ["dungeoneers-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "consulting_a_guide", path = "json/rules_rulesets01.json" },
]

[fields]
kind = "none"
+++

**Sources:** Dungeoneer's Handbook pg 14

A PC may consult a dungeon guide whenever he enters a new room or area of the dungeon to learn more
about his current location, similar to how one gains information by making a Knowledge check.
Consulting a dungeon guide takes 10 minutes, and a dungeon guide may only be consulted once in a
given area. A dungeon guide only makes sense in context, and thus cannot be consulted outside of the
relevant dungeon except for the briefest and most general information about the dungeon in question.

When a PC consults a dungeon guide, the GM makes an accuracy check for the guide by secretly rolling
a d20 and adding the guide's **accuracy modifier** to the roll. The GM then compares the result of
the accuracy check to the DC of the information being sought (see the Accuracy Check DCs table). A
GM may modify these DCs at her discretion. If the result is equal to or greater than the accuracy
check DC, the GM should give the PC a clue or some knowledge about an aspect of the area in
question. For example, the book might mention some historical detail of the room's original purpose,
how to disarm an obstructive mechanism, where an exit leads, or if the area is a good place to rest.

If the dungeon guide's accuracy check fails by 4 or less, the book doesn't have any relevant
information on the area in question. If the dungeon guide fails the check by 5 or more, the GM
should provide the PC with seemingly true information that is actually inaccurate or dangerous in
some way. For example, the guide might reveal that there is a trap in the room, but give the wrong
location for it.

If a PC possesses ranks in the dungeon guide's **associated skill**, he may attempt a skill check
with the associated skill each time he consults the guide. If his check surpasses the guide's
associated skill DC, the guide receives a +2 bonus on its next accuracy check and the PC cannot
receive inaccurate information from the guide should it fail this accuracy check by 5 or more (in
this case the PC simply receives no pertinent information from consulting the text that time).

### Accuracy Check DCs

|Task|DC|
| --- | --- |
|Determine a mechanism's function|20|
|Determine whether an area is a safe place to rest|20|
|Fill in the next area of the map|25|
|Get a hint on how to solve a puzzle|25|
|Get a vague idea of nearby rooms|20|
|Identify a commonly encountered dungeon denizen|10 + creature's CR|
|Identify a room's original purpose|10|
|Locate a hidden trap|10 + trap's CR|
|Locate a nearby source of food or water|15|
