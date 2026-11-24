+++
id = "ref/arc-rogue/swashbuckler"
kind = "archetype"
title = "Swashbuckler"
aon = "ArchetypeDisplay.aspx?FixedName=Rogue%20Swashbuckler"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "swashbuckler", path = "json/archetypes_rogue.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/rogue" },
]
[[sources]]
publication = "advanced-players-guide"
page = "135"

[fields]
kind = "archetype"
features = [
  { anchor = "martial-training", level = 1 },
  { anchor = "daring", level = 3 },
]
trades = [
  { replaces = "Trapfinding", feature = "trapfinding", by = ["martial-training"] },
  { replaces = "Trap sense", feature = "trap-sense", by = ["daring"] },
]
+++

> _**Note:** This is a rogue archetype, and has no relation to the
> [swashbuckler](ref/class/swashbuckler) hybrid class._

A paragon of mobile swordplay, the swashbuckler is a rogue who focuses almost exclusively on honing
her skill at arms and perfecting daring acrobatic moves and elaborate flourishes that border on
performance.

## Martial Training (Ex) {#martial-training}

At 1st level, the swashbuckler may select one martial weapon to add to her list of weapon
proficiencies. In addition, she may take the [combat trick](ref/talent/combat-trick) rogue talent up
to two times. This ability replaces trapfinding.

## Daring (Ex) {#daring}

At 3rd level, a swashbuckler gains a +1 morale bonus on Acrobatics checks and saving throws against
fear. This bonus increases by +1 for every 3 levels beyond 3rd. This ability replaces trap sense.

## Rogue Talents {#rogue-talents}

The following rogue talents complement the swashbuckler archetype: offensive defense, positioning
attack, powerful sneak, and weapon training.

## Advanced Talents {#advanced-talents}

The following advanced rogue talents complement the swashbuckler archetype: crippling strike,
entanglement of blades, and redirect attack.
