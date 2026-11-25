+++
id = "ref/arc-companion/bully"
kind = "archetype"
title = "Bully"
source_ids = ["ultimate-wilderness"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "bully", path = "json/archetypes_COMPANION.json" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "187"

[fields]
kind = "archetype"
features = [
  { anchor = "bullying-thrill", level = 9 },
]
trades = [
  { replaces = "Share Spells" },
  { replaces = "Multiattack", by = ["bullying-thrill"] },
]
+++

Bigger than others of its kind, a bully is used to winning fights and displays of dominance for its
choice of mates, territory, or other privileges.

## Bully Feats {#bully-feats}

In addition to the standard feats available to animal companions, a bully can select
[Greater Bull Rush](ref/feat/greater-bull-rush), [Greater Overrun](ref/feat/greater-overrun),
[Greater Reposition](ref/feat/greater-reposition), [Greater Trip](ref/feat/greater-trip),
[Improved Reposition](ref/feat/improved-reposition), and [Improved Trip](ref/feat/improved-trip). It
can use [Power Attack](ref/feat/power-attack) instead of
[Combat Expertise](ref/feat/combat-expertise) as a prerequisite to qualify for feats on this list.

This replaces share spells.

## Bullying Thrill (Ex) {#bullying-thrill}

At 9th level, whenever a bully succeeds at a bull rush, overrun, reposition, or trip combat maneuver
check, after fully resolving the combat maneuver, it gains a +2 morale bonus on attack and damage
rolls until the end of its next turn.

This replaces Multiattack.
