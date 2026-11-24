+++
id = "ref/arc-rogue/poisoner"
kind = "archetype"
title = "Poisoner"
aon = "ArchetypeDisplay.aspx?FixedName=Rogue%20Poisoner"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "poisoner", path = "json/archetypes_rogue.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/rogue" },
]
[[sources]]
publication = "advanced-players-guide"
page = "134"

[fields]
kind = "archetype"
features = [
  { anchor = "poison-use", level = 1 },
  { anchor = "master-poisoner", level = 3 },
]
trades = [
  { replaces = "Trapfinding", feature = "trapfinding", by = ["poison-use"] },
  { replaces = "Trap sense", feature = "trap-sense", by = ["master-poisoner"] },
]
+++

Some consider poisoning an evil act. The poisoner knows poison is just a tool toward an end, and is
no different than any other weapon. Some poisoners see themselves as great equalizers, as they are
able to craft weapons that the weakest of creatures can wield to devastating effect, but most have
no lofty delusions about their work.

## Poison Use (Ex) {#poison-use}

At 1st level, a poisoner is trained in the use of poison and cannot accidentally poison herself when
applying poison to a blade. This ability replaces trapfinding.

## Master Poisoner (Ex) {#master-poisoner}

At 3rd level, a poisoner can use Craft (alchemy) to change the type of a [poison](ref/rule/poison).
This requires 1 hour of work with an [alchemist's lab](ref/eq-misc/alchemists-lab) and a Craft
(alchemy) skill check with a DC equal to the poison's DC. If successful, the poison's type changes
to contact, ingested, inhaled, or injury. If the check fails, the poison is ruined. The poisoner
also receives a bonus on Craft (alchemy) skill checks when working with poison equal to 1/2 her
rogue level. This ability replaces trap sense.

## Rogue Talents {#rogue-talents}

The following rogue talents complement the poisoner archetype: distracting attack, lasting poison,
surprise attack, swift poison, and weapon training.

## Advanced Talents {#advanced-talents}

The following advanced rogue talents complement the poisoner archetype: deadly cocktail, hunter's
surprise, and opportunist.
