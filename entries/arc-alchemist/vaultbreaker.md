+++
id = "ref/arc-alchemist/vaultbreaker"
kind = "archetype"
title = "Vaultbreaker"
aon = "ArchetypeDisplay.aspx?FixedName=Alchemist%20Vaultbreaker"
source_ids = ["villain-codex"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "vaultbreaker", path = "json/archetypes_alchemist2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/alchemist" },
]
[[sources]]
publication = "villain-codex"
page = "236"

[fields]
kind = "archetype"
features = [
  { anchor = "breaking-and-entering", level = 1 },
  { anchor = "rogue-talents", level = 2 },
  { anchor = "safecracking", level = 1 },
  { anchor = "enhanced-safecracking", level = 3 },
]
trades = [
  { replaces = "The Brew Potion bonus feat", feature = "brew-potion", by = ["breaking-and-entering"] },
  { replaces = "The Throw Anything bonus feat", feature = "throw-anything", by = ["safecracking"] },
  { replaces = "Poison use", feature = "poison-use", by = ["enhanced-safecracking"] },
  { alters = "Discoveries", feature = "discovery", by = ["rogue-talents"] },
  { alters = "Bombs", feature = "bomb", by = ["safecracking", "enhanced-safecracking"] },
]
+++

The vaultbreaker combines stealth with his bomb-making talents to construct special focused charges
that can disable or destroy hinges, locks, and similar mechanisms.

## Breaking and Entering (Ex) {#breaking-and-entering}

A vaultbreaker gains [Stealth](ref/skill/stealth) as a class skill and can disarm magical traps as
if he were a [rogue](ref/class/rogue) with the [trapfinding](ref/ability/trapfinding) ability.

This ability replaces the Brew Potion bonus feat.

## Rogue Talents {#rogue-talents}

A vaultbreaker can choose any of the following rogue talents in place of a discovery:
[expert leaper](ref/talent/expert-leaper), [fast stealth](ref/talent/fast-stealth),
[ledge walker](ref/talent/ledge-walker), [nimble climber](ref/talent/nimble-climber), or
[wall scramble](ref/talent/wall-scramble).

This ability alters discoveries.

## Safecracking (Ex) {#safecracking}

At 1st level, a vaultbreaker's bombs can help him disable locks. He gains
[penetrating charge](ref/discovery/penetrating-charge) (see above) as a bonus discovery. Because
this ability replaces Throw Anything, the vaultbreaker's bombs do not add his Intelligence bonus to
damage rolls.

This ability alters bombs and replaces the Throw Anything bonus feat.

## Enhanced Safecracking (Ex) {#enhanced-safecracking}

At 3rd level, a vaultbreaker gains [incendiary charge](ref/discovery/incendiary-charge) (see above)
as a bonus discovery, and his incendiary charges ignore 10 points of an object's
[hardness](ref/umr/hardness) instead of 5.

This ability alters bombs and replaces the poison use class ability.
