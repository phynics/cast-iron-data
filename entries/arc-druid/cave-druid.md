+++
id = "ref/arc-druid/cave-druid"
kind = "archetype"
title = "Cave Druid"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "cave_druid", path = "json/archetypes_druid.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/druid" },
]
[[sources]]
publication = "advanced-players-guide"
page = "99"

[fields]
kind = "archetype"
replaces = ["Nature sense", "Woodland stride", "Trackless step", "Resist nature's lure"]
alters = ["Nature bond", "Wild empathy", "Wild shape"]
replaces_features = ["nature-sense", "woodland-stride", "trackless-step", "resist-nature-s-lure"]
alters_features = ["nature-bond", "wild-empathy", "wild-shape"]
+++

Far from the green fields of the world above lies a lightless expanse beneath the surface. This
darkling fairyland is not without beauty and natural wonders of its own, and a few druids seek to
preserve this hidden realm and purge it of the fell horrors that creep up from below.

**Cavesense (Ex)**

**Passive:** A cave druid adds [Knowledge (dungeoneering)](ref/skill/knowledge-dungeoneering) (INT)
rather than Knowledge (geography) as a class skill and gains a +2 bonus on Knowledge (dungeoneering)
and Survival skill checks.

**Replaces:** Nature sense

**Nature Bond**

**Alters:** Nature bond

**Choice:** A cave druid may select the Darkness domain in addition to the choices normally allowed,
but may not select the Air or Weather domains.

**Wild Empathy (Ex)**

**Ability:** A cave druid can influence oozes, rather than magical beasts, with a -4 penalty on her
_wild empathy_ check.

**Alters:** Wild empathy

**Tunnelrunner (Ex)**

**Gained:** At 2nd Level

**Passive:** A cave druid can move through areas of rubble or narrow passages that require
[squeezing](ref/misc/squeezing) at her normal movement rate and without penalty.

**Replaces:** Woodland stride

**Lightfoot (Ex)**

**Gained:** At 3rd Level

**Passive:** A cave druid cannot be detected with [tremorsense](ref/umr/tremorsense).

**Replaces:** Trackless step

**Resist Subterranean Corruption (Ex)**

**Gained:** At 4th Level

**Passive:** A cave druid gains a +2 bonus on saves against exceptional, supernatural, and
[spell-like abilities](ref/umr/spell-like-abilities) of oozes and aberrations.

**Replaces:** Resist nature's lure

**Wild Shape (Su)**

**Ability:** A cave druid gains _wild shape,_ except that her effective druid level for this ability
is equal to her druid level - 2. She cannot use _wild shape_ to adopt a plant form.

**Alters:** Wild shape

**At 10th Level:** The cave druid can assume the form of a Small or Medium ooze as if using
[beast shape III](ref/spell/beast-shape-3).

**At 12th Level:** The druid can assume the form of a Tiny or Large ooze as if using
[beast shape IV](ref/spell/beast-shape-4) (treating the ooze as if it were a magical beast without a
natural armor bonus).

**Gained:** At 6th Level

**Special:** When in ooze form, the cave druid has no discernible anatomy and is immune to poison,
sneak attacks, and critical hits.
