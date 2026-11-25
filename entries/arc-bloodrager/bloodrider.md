+++
id = "ref/arc-bloodrager/bloodrider"
kind = "archetype"
title = "Bloodrider"
aon = "ArchetypeDisplay.aspx?FixedName=Bloodrager%20Bloodrider"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "bloodrider", path = "json/archetypes_bloodrager.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/bloodrager" },
]
[[sources]]
publication = "advanced-class-guide"
page = "82"

[fields]
kind = "archetype"
features = [
  { anchor = "fast-rider", level = 1 },
  { anchor = "feral-mount", level = 5 },
  { anchor = "blood-bond", level = 9 },
]
trades = [
  { replaces = "Fast movement", feature = "fast-movement", by = ["fast-rider"] },
  { replaces = "Uncanny dodge", feature = "uncanny-dodge", by = ["feral-mount"] },
  { replaces = "improved uncanny dodge", feature = "improved-uncanny-dodge", by = ["feral-mount"] },
  { replaces = "The bloodline feat gained at 9th level", feature = "bloodline", levels = [9], power = "bloodline feat", by = ["blood-bond"] },
]
+++

In the world's wild lands, a mount is an advantage in both everyday life and the dealing of death.
In many barbarian tribes, the true stature of a warrior is determined by his skill and ferocity on
horseback. Other tribes measure it in skill atop whatever terrible mounts their people employ. A
number of bloodragers are not only skilled in the art of mounted combat, but have learned to channel
their arcane energies directly into their mount.

## Fast Rider (Ex) {#fast-rider}

The bloodrider is adept at pushing his mount to its limit. The speed of any mount the bloodrager
rides increases by 10 feet. This ability replaces fast movement.

## Feral Mount (Ex) {#feral-mount}

At 5th level, the bloodrider gains the service of a feral mount. This ability functions as the
druid's [animal companion](ref/sidekick/animal-companion), using the bloodrager's level - 4 as his
effective druid level. This companion must be one he is capable of riding and suitable as a mount. A
Medium bloodrider can select a [camel](ref/companion/camel) or a [horse](ref/companion/horse). A
Small bloodrider can select a [pony](ref/companion/pony) or [wolf](ref/companion/wolf), but can also
select a [boar](ref/companion/boar) or [riding dog](ref/companion/dog) if he is at least 8th level.
Whenever a bloodrider is bloodraging, this feral mount gains a +2 morale bonus to its Strength. This
ability replaces uncanny dodge and improved uncanny dodge.

## Blood Bond (Su) {#blood-bond}

At 9th level, the bloodrider and his feral mount gain a closer bond that allows the bloodrider to
augment his mount based on his bloodline. While the bloodrider is bloodraging and on his feral
mount, he grants the mount all the immunities and resistances he gains from bloodline powers.
Furthermore, whenever the bloodrager is affected by a spell or
[spell-like ability](ref/umr/spell-like-abilities) with the range of personal while on the feral
mount, the feral mount also gains the benefit of that spell. This ability replaces the bloodline
feat gained at 9th level.
