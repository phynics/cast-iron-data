+++
id = "ref/arc-rogue/escapologist"
kind = "archetype"
title = "Escapologist"
aon = "ArchetypeDisplay.aspx?FixedName=Rogue%20Escapologist"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "escapologist", path = "json/archetypes_rogue.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/rogue" },
]
[[sources]]
publication = "occult-adventures"
page = "123"

[fields]
kind = "archetype"
features = [
  { anchor = "elusive", level = 1 },
  { anchor = "unfettered-mind", level = 3 },
  { anchor = "impossible-escape", level = 8 },
]
trades = [
  { replaces = "Trapfinding", feature = "trapfinding", by = ["elusive"] },
  { replaces = "Uncanny dodge", feature = "uncanny-dodge", by = ["unfettered-mind"] },
  { replaces = "Improved uncanny dodge", feature = "improved-uncanny-dodge", by = ["impossible-escape"] },
]
+++

The escapologist excels at escaping any confinement, whether physical, magical, or mental. Few
restraints can hold an escapologist for long.

## Elusive {#elusive}

An escapologist adds 1/2 her rogue level (minimum +1) as a bonus on all Disable Device and Escape
Artist checks. An escapologist can use Disable Device to disarm magical traps. This ability replaces
trapfinding, but counts as trapfinding for the purposes of prerequisites and abilities that require
trapfinding.

## Unfettered Mind (Su) {#unfettered-mind}

At 3rd level, an escapologist can attempt an Escape Artist check as a full-round action to remove a
mind-affecting effect currently affecting her. The DC of this check is equal to the effect's
original save DC + 20. She cannot remove effects that do not allow a saving throw. She can attempt
to escape even if paralyzed or restrained, as long as she can take purely mental actions. She can
attempt this check against a particular effect once per round if the effect is measured in rounds,
once per minute if the effect is measured in minutes, once per 10 minutes if the effect is measured
in 10-minute intervals, and so on. This ability replaces uncanny dodge.

## Impossible Escape (Su) {#impossible-escape}

At 8th level, as an immediate action, an escapologist can attempt an Escape Artist check at a -10
penalty and apply the result in place of either a failed Reflex save or her AC against an attack
that would have hit her. If she succeeds, her contortions let her avoid the attack or effect
entirely. Using this ability leaves the escapologist [staggered](ref/misc/staggered) until the end
of her next turn. If the escapologist can't become staggered, she can't use impossible escape. This
ability replaces improved uncanny dodge.
