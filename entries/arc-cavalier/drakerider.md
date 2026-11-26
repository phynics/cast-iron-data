+++
id = "ref/arc-cavalier/drakerider"
kind = "archetype"
title = "Drakerider"
aon = "ArchetypeDisplay.aspx?FixedName=Cavalier%20Drakerider"
source_ids = ["legacy-of-dragons"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "drakerider", path = "json/archetypes_cavalier.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/cavalier" },
]
[[sources]]
publication = "legacy-of-dragons"
page = "24"

[fields]
kind = "archetype"
features = [
  { anchor = "drake-mount", level = 1 },
  { anchor = "approved-order" },
]
trades = [
  { replaces = "Mount", feature = "mount", by = ["drake-mount"] },
  { replaces = "tactician", feature = "tactician", by = ["drake-mount"] },
  { replaces = "expert trainer", feature = "expert-trainer", by = ["drake-mount"] },
  { replaces = "banner", feature = "banner", by = ["drake-mount"] },
  { replaces = "greater tactician", feature = "greater-tactician", by = ["drake-mount"] },
  { replaces = "greater banner", feature = "greater-banner", by = ["drake-mount"] },
  { replaces = "master tactician", feature = "master-tactician", by = ["drake-mount"] },
  { alters = "Cavalier's charge", feature = "cavalier-s-charge", by = ["drake-mount"] },
]
+++

While many cavaliers dream of riding a dragon into battle, drakeriders come to learn that the
reality involves far more effort than they had expected. Unlike other cavaliers, drakeriders must
train their mounts from hatchlings, fighting and toiling alongside their drakes for years through
countless struggles before the proud dragons are willing to accept them as riders. Some residents of
Triaxus, envious of the close connection between dragonriders and dragons, attempt to emulate this
relationship by raising drake hatchlings. These efforts aren't always successful, sometimes leaving
the would-be drakeriders dead or maimed.

## Drake Mount {#drake-mount}

A drakerider gains a [drake companion](ref/sidekick/drake) instead of a mount. She gains cavalier's
charge at 9th level instead of 3rd.

This ability replaces mount, tactician, expert trainer, banner, greater tactician, greater banner,
and master tactician and alters cavalier's charge.

## Approved Order {#approved-order}

A drakerider can join only an order approved by its mount. Suitable orders include
[order of the beast](ref/order/order-of-the-beast-isc),
[order of the cockatrice](ref/order/order-of-the-cockatrice), and
[order of the dragon](ref/order/order-of-the-dragon), as well as other fitting orders at the GM's
discretion.
