+++
id = "ref/arc-brawler/verdant-grappler"
kind = "archetype"
title = "Verdant Grappler"
source_ids = ["ultimate-wilderness"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "verdant_grappler", path = "json/archetypes_brawler.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/brawler" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "43"

[fields]
kind = "archetype"
replaces = ["Bonus feat gained at 2nd level", "Close weapon mastery", "The combat feat gained at 11th level"]
alters = ["Maneuver training"]
replaces_features = ["close-weapon-mastery"]
alters_features = ["maneuver-training"]
+++

By accepting spirits of nature into her soul, a verdant grappler can entangle her foes with tangled
undergrowth.

**Green Grasp (Su)**

**Alters:** Maneuver training

**At 2nd Level:** A verdant grappler gains [Improved Grapple](ref/feat/improved-grapple) as a bonus
feat.

**At 3rd Level:** She must choose [grapple](ref/rule/grapple) as her first combat maneuver for
maneuver training. When she pins a creature, she can cause roots and vines to burst from the ground
(no matter the surrounding terrain), allowing the verdant grappler to attempt to tie up the creature
without needing to retrieve rope or use a hand to hold the rope; as usual, a tied-up creature is
[pinned](ref/rule/grapple-conditions) and not helpless.

**Replaces:** Bonus feat gained at 2nd level

**Special:** The verdant grappler must remain within 30 feet of the tied-up creature, or the vines
automatically release it. She can tie up only one creature at a time with _green grasp._

**Thorny Embrace (Su)**

**At 5th Level:** When a verdant grappler uses _green grasp_ to tie up a creature, she can have the
roots and vines grow vicious thorns that automatically damage the tied-up creature each round at the
start of the verdant grappler's turn. The thorns deal damage equal to the base unarmed strike damage
of a brawler 4 levels lower than the verdant grappler.

**Replaces:** Close weapon mastery

**Phytological Anatomy (Su)**

**Gained:** At 11th Level

**Passive:** The verdant grappler transforms partially into a plant. She gains a +2 bonus on saving
throws against mind-affecting, paralysis, poison, polymorph, sleep, and stunning effects.

**Replaces:** The combat feat gained at 11th level
