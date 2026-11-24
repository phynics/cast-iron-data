+++
id = "ref/arc-rogue/burglar"
kind = "archetype"
title = "Burglar"
aon = "ArchetypeDisplay.aspx?FixedName=Rogue%20Burglar"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "burglar", path = "json/archetypes_rogue.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/rogue" },
]
[[sources]]
publication = "advanced-players-guide"
page = "132"

[fields]
kind = "archetype"
features = [
  { anchor = "careful-disarm", level = 4 },
  { anchor = "distraction", level = 8 },
]
trades = [
  { replaces = "Uncanny dodge", feature = "uncanny-dodge", by = ["careful-disarm", "distraction"] },
  { replaces = "Improved uncanny dodge", feature = "improved-uncanny-dodge", by = ["distraction"] },
]
+++

Adept at infiltration, trap removal, and lock picking, burglars prey on the homes of the wealthy and
forgotten tombs alike. Such riches are guarded with vicious traps and hazards, but the devious mind
of the burglar allows her to find such dangers and avoid them.

## Careful Disarm (Ex) {#careful-disarm}

At 4th level, whenever a burglar attempts to disarm a trap using Disable Device, she does not spring
the trap unless she fails by 10 or more. If she does set off a trap she was attempting to disarm,
she adds double her trap sense bonus to avoid the trap. This ability replaces uncanny dodge.

## Distraction (Ex) {#distraction}

At 8th level, whenever a burglar is detected while using Stealth, she can immediately attempt a
Bluff skill check opposed by the Sense Motive skill of the creature that spotted her. If this check
succeeds, the target assumes that the noise was something innocent and disregards the detection.
This only functions if the creature cannot see the rogue. This ability can only be used once during
a given Stealth attempt. If the same creature detects the rogue's presence again, the ability has no
effect. This ability replaces improved uncanny dodge.

## Rogue Talents {#rogue-talents}

The following rogue talents complement the burglar archetype: fast picks, fast stealth, nimble
climber, quick disable, and trap spotter.

## Advanced Talents {#advanced-talents}

The following advanced rogue talents complement the burglar archetype: knock-out blow, skill
mastery, and thoughtful reexamining.
