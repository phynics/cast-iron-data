+++
id = "ref/arc-ranger/trapper"
kind = "archetype"
title = "Trapper"
aon = "ArchetypeDisplay.aspx?FixedName=Ranger%20Trapper"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "trapper", path = "json/archetypes_ranger.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/ranger" },
]
[[sources]]
publication = "ultimate-magic"
page = "65"

[fields]
kind = "archetype"
replaces = ["Spellcasting ability"]
+++

A trapper is a ranger who focuses exclusively on traps, rather than learning conventional magic. A
trapper has the following class features.

**Gained class skills:** dd

**Trapfinding**

**Ability:** A trapper can use Disable Device to disarm magic traps.

**Passive:** A trapper adds 1/2 her ranger level on Perception skill checks made to locate traps and
on Disable Device skill checks (minimum +1).

**Trap**

**At 5th Level:** A trapper learns how to create a [snare trap](ref/rangertrap/snare-trap) and one
other ranger trap of her choice.

**Repeat:** She learns another trap., 7, 2

**Replaces:** Spellcasting ability

**Special:** The trapper can use these traps a total number of times per day equal to 1/2 her ranger
level + her Wisdom modifier. Once a trap is learned, it can't be unlearned and replaced with a
different type of trap. The trapper cannot select an individual trap more than once.

**Launch Trap**

**Ability:** A trapper can affix a magical ranger trap to an arrow, crossbow bolt, or thrown weapon,
allowing her to set the trap remotely or use it as a direct attack. Attaching the trap to the
projectile is part of the **full-round action** of creating a new trap. The trapped projectile is
fired or thrown in the normal manner. If fired at a square, the trap is treated as if the ranger had
set the trap in that square, except the DC is 5 lower than normal. If fired at a creature, the
target takes damage from the ranged weapon and is treated as if it had triggered the trap (saving
throw applies, if any). The attack has a maximum range of 60 feet, and range increments apply to the
attack roll.

**Gained:** At 10th Level

**Special:** The duration of the trapped projectile starts from when it is created, not from when it
is used.
