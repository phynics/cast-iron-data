+++
id = "ref/arc-rogue/bekyar-kidnapper"
kind = "archetype"
title = "Bekyar Kidnapper"
aon = "ArchetypeDisplay.aspx?FixedName=Rogue%20Bekyar%20Kidnapper"
source_ids = ["inner-sea-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "bekyar_kidnapper", path = "json/archetypes_rogue.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/rogue" },
]
[[sources]]
publication = "inner-sea-combat"
page = "36"

[fields]
kind = "archetype"
features = [
  { anchor = "clean-capture", level = 1 },
  { anchor = "abductor", level = 3 },
]
trades = [
  { replaces = "Trapfinding", feature = "trapfinding", by = ["clean-capture"] },
  { replaces = "Trap sense", feature = "trap-sense", by = ["abductor"] },
]
+++

One of the many ethnicities found in the Mwangi Expanse, the Bekyar people are slavers and demon
worshipers. A Bekyar kidnapper is not only adept at hiding herself in thick jungles and quickly
subduing her prey, but also at spreading rumors of hidden ruins, buried treasure, and other such
valuables that might lure an unwary foreigner into her traps.

## Clean Capture (Ex) {#clean-capture}

At 1st level, a Bekyar kidnapper reduces the penalty to her combat maneuver check to tie up a pinned
or otherwise restrained target by an amount equal to 1/2 her rogue level. In addition, she can take
the feats [Improved Grapple](ref/feat/improved-grapple) and
[Greater Grapple](ref/feat/greater-grapple) as rogue talents. She can ignore the
[Improved Unarmed Strike](ref/feat/improved-unarmed-strike) requirement when selecting these feats
as rogue talents, but must meet all other prerequisites. This ability replaces trapfinding.

## Abductor (Ex) {#abductor}

At 3rd level, a Bekyar kidnapper gains a +1 bonus on combat maneuver checks to grapple a foe. In
addition, the Bekyar kidnapper treats her combat maneuver bonus as 1 higher when a foe tries to
grapple her or when a grappled target attempts to break free of her grapple. These bonuses increase
by 1 for every 3 levels beyond 3rd. This ability replaces trap sense.

## Rogue Talents {#rogue-talents}

The following rogue talents complement the Bekyar kidnapper archetype: black market connections,
camouflage, combat trick, rope master, survivalist, and terrain mastery.

## Advanced Talents {#advanced-talents}

The following advanced rogue talents complement the Bekyar kidnapper archetype: crippling strike,
hide in plain sight, knock-out blow, rumormonger, and weapon snatcher.
