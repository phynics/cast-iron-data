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
replaces = ["Trapfinding", "Uncanny dodge", "Improved uncanny dodge"]
+++

The escapologist excels at escaping any confinement, whether physical, magical, or mental. Few
restraints can hold an escapologist for long.

**Elusive**

**Ability:** An escapologist can use Disable Device to disarm magical traps.

**Passive:** An escapologist adds 1/2 her rogue level (minimum +1) as a bonus on all Disable Device
and Escape Artist checks.

**Replaces:** Trapfinding

**Special:** This counts as _trapfinding_ for the purpose of prerequisites and abilities that
require trapfinding.

**Unfettered Mind (Su)**

**Fullround:** An escapologist can attempt an Escape Artist check to remove a mind-affecting effect
currently affecting her. The DC of this check is equal to the effect's original save DC + 20. She
cannot remove effects that do not allow a saving throw. She can attempt to escape even if paralyzed
or restrained, as long as she can take purely mental actions.

**Gained:** At 3rd Level

**Replaces:** Uncanny dodge

**Special:** She can attempt this check against a particular effect once per round if the effect is
measured in rounds, once per minute if the effect is measured in minutes, once per 10 minutes if the
effect is measured in 10-minute intervals, and so on.

**Impossible Escape (Su)**

**Immediate:** An escapologist can attempt an Escape Artist check at a -10 penalty and apply the
result in place of either a failed Reflex save or her AC against an attack that would have hit her.
If she succeeds, her contortions let her avoid the attack or effect entirely.

**Gained:** At 8th Level

**Replaces:** Improved uncanny dodge

**Special:** Using this ability leaves the escapologist [staggered](ref/misc/staggered) until the
end of her next turn. If the escapologist can't become staggered, she can't use impossible escape.
