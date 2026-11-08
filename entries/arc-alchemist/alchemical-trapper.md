+++
id = "ref/arc-alchemist/alchemical-trapper"
kind = "archetype"
title = "Alchemical Trapper"
source_ids = ["monster-codex"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "alchemical_trapper", path = "json/archetypes_alchemist.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/alchemist" },
]

[fields]
kind = "archetype"
replaces = ["The discovery at 2nd level", "The discovery at 4th level"]
+++

**Sources:** Monster Codex pg 128\
Because kobolds rely on [traps](ref/rule/traps) to soften up enemies, kobold alchemists learn to
turn bombs into traps. When such alchemists are preparing defenses against larger creatures that
might enter their tunnels and attempt to exterminate them, their skills mean the difference between
life and death.

**Prerequisites:** Kobold

**Bomb Trap (Su)**

**Fullround:** Creating a bomb trap uses one of the alchemical trapper's bombs per day. A bomb trap
fills a single 5-foot square and cannot be placed in the same area as any other trap.

**Gained:** At 2nd Level

**Provokes attack of opportunity:** Yes

**Replaces:** The discovery at 2nd level

**Special:** The alchemical trapper needs the same materials required for making a bomb. The DCs for
Perception checks to notice the trap, Disable Device checks to disable it, and saving throws to
avoid it are equal to the DC for the alchemical trapper's bombs. All bomb traps have location
triggers and do not reset. The alchemical trapper can use any one discovery that applies to a bomb
(Primary Bomb Discovery) when making a bomb trap. The bomb trap lasts 10 minutes for each alchemist
level the trapper possesses. If the bomb trap is not disabled or exploded within that time frame,
the trap becomes inert.

**Trapfinding (Ex)**

**Ability:** An alchemical trapper can find and disable traps, as the
[trapfinding](ref/ability/trapfinding) class feature of the [rogue](ref/class/rogue).

**Gained:** At 4th Level

**Replaces:** The discovery at 4th level
