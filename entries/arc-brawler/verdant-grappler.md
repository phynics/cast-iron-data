+++
id = "ref/arc-brawler/verdant-grappler"
kind = "archetype"
title = "Verdant Grappler"
aon = "ArchetypeDisplay.aspx?FixedName=Brawler%20Verdant%20Grappler"
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
features = [
  { anchor = "green-grasp", level = 2 },
  { anchor = "thorny-embrace", level = 5 },
  { anchor = "phytological-anatomy", level = 11 },
]
trades = [
  { replaces = "Bonus feat gained at 2nd level", feature = "bonus-combat-feats", levels = [2], by = ["green-grasp"] },
  { replaces = "Close weapon mastery", feature = "close-weapon-mastery", by = ["thorny-embrace"] },
  { replaces = "The combat feat gained at 11th level", feature = "bonus-combat-feats", levels = [11], by = ["phytological-anatomy"] },
  { alters = "Maneuver training", feature = "maneuver-training", by = ["green-grasp"] },
]
+++

By accepting spirits of nature into her soul, a verdant grappler can entangle her foes with tangled
undergrowth.

## Green Grasp (Su) {#green-grasp}

At 2nd level, a verdant grappler gains [Improved Grapple](ref/feat/improved-grapple) as a bonus
feat. At 3rd level, she must choose [grapple](ref/rule/grapple) as her first combat maneuver for
maneuver training. When she pins a creature, she can cause roots and vines to burst from the ground
(no matter the surrounding terrain), allowing the verdant grappler to attempt to tie up the creature
without needing to retrieve rope or use a hand to hold the rope; as usual, a tied-up creature is
[pinned](ref/rule/grapple-conditions) and not helpless. The verdant grappler must remain within 30
feet of the tied-up creature, or the vines automatically release it. She can tie up only one
creature at a time with green grasp.

This replaces the bonus feat gained at 2nd level and alters maneuver training.

## Thorny Embrace (Su) {#thorny-embrace}

At 5th level, when a verdant grappler uses green grasp to tie up a creature, she can have the roots
and vines grow vicious thorns that automatically damage the tied-up creature each round at the start
of the verdant grappler's turn. The thorns deal damage equal to the base unarmed strike damage of a
brawler 4 levels lower than the verdant grappler.

This replaces close weapon mastery.

## Phytological Anatomy (Su) {#phytological-anatomy}

At 11th level, the verdant grappler transforms partially into a plant. She gains a +2 bonus on
saving throws against mind-affecting, paralysis, poison, polymorph, sleep, and stunning effects.

This replaces the combat feat gained at 11th level.
