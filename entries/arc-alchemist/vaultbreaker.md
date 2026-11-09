+++
id = "ref/arc-alchemist/vaultbreaker"
kind = "archetype"
title = "Vaultbreaker"
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
replaces = ["Brew Potion", "Throw Anything", "Poison use"]
alters = ["Discoveries", "Bombs", "Bombs"]
+++

The vaultbreaker combines stealth with his bomb-making talents to construct special focused charges
that can disable or destroy hinges, locks, and similar mechanisms.

**Breaking and Entering (Ex)**

**Passive:** A vaultbreaker gains [Stealth](ref/skill/stealth) (DEX) as a class skill and can disarm
magical traps as if he were a [rogue](ref/class/rogue) with the
[trapfinding](ref/ability/trapfinding) ability.

**Replaces:** Brew Potion

**Rogue Talents**

**Alters:** Discoveries

**Passive:** A vaultbreaker can choose any of the following rogue talents in place of a discovery:
[expert leaper](ref/talent/expert-leaper), [fast stealth](ref/talent/fast-stealth),
[ledge walker](ref/talent/ledge-walker), [nimble climber](ref/talent/nimble-climber), or
[wall scramble](ref/talent/wall-scramble).

**Safecracking (Ex)**

**Ability:** He gains [penetrating charge](ref/discovery/penetrating-charge) as a bonus discovery.

**Alters:** Bombs

**Flavor:** A vaultbreaker's bombs can help him disable locks.

**Gained:** At 1st Level

**Replaces:** Throw Anything

**Special:** Because this ability replaces Throw Anything, the vaultbreaker's bombs do not add his
Intelligence bonus to damage rolls.

**Enhanced Safecracking (Ex)**

**Alters:** Bombs

**Gained:** At 3rd Level

**Passive:** A vaultbreaker gains [incendiary charge](ref/discovery/incendiary-charge) as a bonus
discovery, and his incendiary charges ignore 10 points of an object's [hardness](ref/umr/hardness)
instead of 5.

**Replaces:** Poison use
