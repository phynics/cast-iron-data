+++
id = "ref/arc-companion/bodyguard"
kind = "archetype"
title = "Bodyguard"
source_ids = ["ultimate-wilderness", "animal-archive"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "bodyguard", path = "json/archetypes_COMPANION.json" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "187"
[[sources]]
publication = "animal-archive"
page = "20"

[fields]
kind = "archetype"
features = [
  { anchor = "shared-vigilance" },
  { anchor = "tenacious-guardian", level = 3 },
  { anchor = "uncanny-dodge", level = 9 },
  { anchor = "greater-tenacity", level = 15 },
]
trades = [
  { replaces = "Share Spells", by = ["shared-vigilance"] },
  { replaces = "Evasion", by = ["tenacious-guardian"] },
  { replaces = "Multiattack", by = ["uncanny-dodge"] },
  { replaces = "Improved Evasion", by = ["greater-tenacity"] },
]
+++

Some companions live lives of faithful devotion and steady vigilance, standing watch through long
hours and always ready to leap into action to protect their masters.

## Animal Feats {#animal-feats}

In addition to the standard feats available to animal companions, a bodyguard can select Bodyguard,
[Combat Patrol](ref/feat/combat-patrol), [Heroic Defiance](ref/feat/heroic-defiance),
[Heroic Recovery](ref/feat/heroic-recovery), and [In Harm's Way](ref/feat/in-harms-way).

## Shared Vigilance (Ex) {#shared-vigilance}

Both a bodyguard and its master gain [Alertness](ref/feat/alertness) as a bonus feat whenever they
are adjacent.

This replaces share spells.

## Tenacious Guardian (Ex) {#tenacious-guardian}

At 3rd level, a bodyguard can always act in a surprise round (though it remains
[flat-footed](ref/rule/flat-footed) until it acts). As long as its master is adjacent, a bodyguard
remains conscious (though it becomes [staggered](ref/misc/staggered)) when its hit points fall
below 0. While below 0 hit points, the bodyguard loses 1 hit point per round but gains a +2 morale
bonus on attack rolls, saving throws, and skill checks, dying only if its hit points reach a
negative total equal to its Constitution score plus its master's class level.

This replaces evasion.

## Uncanny Dodge (Ex) {#uncanny-dodge}

At 9th level, a bodyguard gains [uncanny dodge](ref/ability/uncanny-dodge) as per the
[rogue](ref/class/rogue) class feature of the same name.

This replaces Multiattack.

## Greater Tenacity (Ex) {#greater-tenacity}

At 15th level, a bodyguard with fewer than 0 hit points gains a +4 morale bonus on attack rolls,
saving throws, and skill checks; immunity to fear effects; and temporary hit points equal to its
master's class level (maximum 20). It dies only if its hit points reach a negative total equal to
twice its Constitution score plus its master's class level.

This replaces improved evasion.
