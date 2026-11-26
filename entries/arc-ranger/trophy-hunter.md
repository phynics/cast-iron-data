+++
id = "ref/arc-ranger/trophy-hunter"
kind = "archetype"
title = "Trophy Hunter"
aon = "ArchetypeDisplay.aspx?FixedName=Ranger%20Trophy%20Hunter"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "trophy_hunter", path = "json/archetypes_ranger.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/ranger" },
]
[[sources]]
publication = "ultimate-combat"
page = "67"

[fields]
kind = "archetype"
features = [
  { anchor = "improved-tracking", level = 1 },
  { anchor = "firearm-style", level = 2 },
  { anchor = "hunter-s-aim", level = 4 },
]
trades = [
  { replaces = "Wild empathy", feature = "wild-empathy", by = ["improved-tracking"] },
  { replaces = "All combat style feats", feature = "combat-style-feat", by = ["firearm-style"] },
  { replaces = "Hunter's bond", feature = "hunter-s-bond", by = ["hunter-s-aim"] },
]
+++

Some rangers have taken up the mysteries of black powder in order to become big game hunters.
Finding firearms useful for taking down large and dangerous prey, they enter the fight with the
crack of black powder fire, often ranging far and wide in their safaris and searches for
ever-more-dangerous denizens of the wild to track, study, appreciate—and kill. While this might
strike some as going against the ranger's usual respect for nature and the creatures of the wild,
trophy hunters understand that they are just more pieces in nature's grand puzzle, and that the laws
of the jungle—the right to kill and feed on those weaker than you, and the need to establish
dominance through cunning and bloodshed—are both their rights and their duty as the current top of
the food chain.

## Improved Tracking (Ex) {#improved-tracking}

At 1st level, a trophy hunter gains a +2 bonus on Survival skill checks when following or
identifying tracks. When he tracks, he can also attempt a Knowledge (nature) check at DC 15. On a
success, the trophy hunter can discern the type and condition of any animals or magical beasts he
tracks. By studying their tracks, the trophy hunter is able to identify a rough approximation of
their health, maneuverability, and their general behavior as compared to the norm. This ability
replaces wild empathy.

## Firearm Style {#firearm-style}

At 2nd level, a trophy hunter gains the [Amateur Gunslinger](ref/feat/amateur-gunslinger) feat and
[Exotic Weapon Proficiency](ref/feat/exotic-weapon-proficiency) (firearms), and can use any
1st-level gunslinger deed (page 10). At every four levels thereafter, the trophy hunter can take a
grit feat or select a gunslinger deed of his level or lower, ranger's choice. This ability replaces
all combat style feats.

## Hunter's Aim (Ex) {#hunter-s-aim}

At 4th level, a trophy hunter gains a specific understanding of the weaknesses and vulnerabilities
of his favored enemies, and his careful study of these enemies reveals the best way to hurt them.
When the trophy hunter makes a firearm attack against a favored enemy, he can target touch AC in the
first two range increments of his firearm. This ability stacks with other effects that increase the
range increments to target touch AC, adding one range increment to the effect. This ability replaces
hunter's bond.
