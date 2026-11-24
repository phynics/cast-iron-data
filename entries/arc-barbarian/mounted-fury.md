+++
id = "ref/arc-barbarian/mounted-fury"
kind = "archetype"
title = "Mounted Fury"
aon = "ArchetypeDisplay.aspx?FixedName=Barbarian%20Mounted%20Fury"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "mounted_fury", path = "json/archetypes_barbarian.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/barbarian" },
]
[[sources]]
publication = "advanced-players-guide"
page = "79"

[fields]
kind = "archetype"
features = [
  { anchor = "fast-rider" },
  { anchor = "bestial-mount", level = 5 },
]
trades = [
  { replaces = "Fast movement", feature = "fast-movement", by = ["fast-rider"] },
  { replaces = "Uncanny dodge", feature = "uncanny-dodge", by = ["bestial-mount"] },
  { replaces = "improved uncanny dodge", feature = "improved-uncanny-dodge", by = ["bestial-mount"] },
]
+++

Many barbarian tribes are masters of the horse, teaching their members how to ride from a young age.
As a result, barbarians from such tribes are even more terrifying when mounted, using their steeds'
speed and strength to great advantage. A mounted fury has the following class features.

## Fast Rider (Ex) {#fast-rider}

The speed of any mount the barbarian rides is increased by 10 feet. This ability replaces fast
movement.

## Bestial Mount (Ex) {#bestial-mount}

At 5th level, the mounted fury gains the service of a feral mount. This ability functions as a
druid's [animal companion](ref/sidekick/animal-companion), using the barbarian's level -4 as her
effective druid level. This companion must be one that she is capable of riding and is suitable as a
mount. A Medium barbarian can select a [camel](ref/companion/camel) or a
[horse](ref/companion/horse). A Small barbarian can select a [pony](ref/companion/pony) or a
[wolf](ref/companion/wolf), but can also select a [boar](ref/companion/boar) or a
[dog](ref/companion/dog) if she is at least 8th level. Whenever a barbarian is raging while mounted
on her bestial mount, the mount gains a +2 morale bonus to its Strength. This ability replaces
uncanny dodge and improved uncanny dodge.

## Rage Powers {#rage-powers}

The following rage powers complement the mounted fury archetype:
[ferocious mount](ref/ragepower/ferocious-mount),
[ferocious trample](ref/ragepower/ferocious-trample),
[greater ferocious mount](ref/ragepower/greater-ferocious-mount),
[greater ferocious trample](ref/ragepower/greater-ferocious-trample), and
[spirit steed](ref/ragepower/spirit-steed).
