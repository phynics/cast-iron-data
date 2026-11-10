+++
id = "ref/arc-bloodrager/blood-conduit"
kind = "archetype"
title = "Blood Conduit"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "blood_conduit", path = "json/archetypes_bloodrager.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/bloodrager" },
]
[[sources]]
publication = "advanced-class-guide"
page = "82"

[fields]
kind = "archetype"
replaces = ["Fast movement", "Uncanny dodge", "improved uncanny dodge", "Indomitable will"]
alters = ["Bloodline feats"]
replaces_features = ["fast-movement", "uncanny-dodge", "improved-uncanny-dodge", "indomitable-will"]
+++

Blood conduits learn to channel their arcane might directly through their flesh, without the need
for mystical words or gestures.

**Contact Specialist (Ex)**

**Alters:** Bloodline feats

**At 1st Level:** A blood conduit selects a bonus feat from the following:
[Improved Bull Rush](ref/feat/improved-bull-rush), [Improved Grapple](ref/feat/improved-grapple),
[Improved Reposition](ref/feat/improved-reposition), [Improved Trip](ref/feat/improved-trip), and
[Improved Unarmed Strike](ref/feat/improved-unarmed-strike). He does not need to meet the
prerequisites to take this feat. He also adds those feats to his list of bloodline feats.

**Replaces:** Fast movement

**Spell Conduit (Su)**

**Gained:** At 5th Level

**Replaces:** Uncanny dodge, improved uncanny dodge

**Special:** The blood conduit must be wearing light or no armor.

**Swift:** When he succeeds at a [combat maneuver](ref/rule/combat-maneuvers) check to bull rush,
grapple, pin, reposition, or trip an opponent, or makes an unarmed strike against an enemy, he can
cast a touch spell on the creature that he affected with the combat maneuver, requiring no further
touch attack roll. If this spell would usually require a successful touch attack, his successful
combat maneuver check counts as this attack.

**Reflexive Conduit (Ex)**

**Immediate:** While wearing light or no armor, when the blood conduit is subject to a combat
maneuver check made to bull rush, grapple, pin, reposition, or trip him, he can target his attacker
with a bloodrager spell that has a range of touch. If the spell would normally require a touch
attack, a blood conduit can attempt a combat maneuver check for this attack instead.

**Gained:** At 14th Level

**Replaces:** Indomitable will
