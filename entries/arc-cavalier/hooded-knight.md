+++
id = "ref/arc-cavalier/hooded-knight"
kind = "archetype"
title = "Hooded Knight"
aon = "ArchetypeDisplay.aspx?FixedName=Cavalier%20Hooded%20Knight"
source_ids = ["legacy-of-the-first-world"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "hooded_knight", path = "json/archetypes_cavalier.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/cavalier" },
]
[[sources]]
publication = "legacy-of-the-first-world"
page = "26"

[fields]
kind = "archetype"
features = [
  { anchor = "feytouched-mount", level = 1 },
  { anchor = "hero-of-the-roads", level = 1 },
  { anchor = "champion-of-the-roads", level = 9 },
  { anchor = "paragon-of-the-roads", level = 17 },
]
trades = [
  { replaces = "Tactician", feature = "tactician", by = ["hero-of-the-roads"] },
  { replaces = "Greater tactician", feature = "greater-tactician", by = ["champion-of-the-roads"] },
  { replaces = "Master tactician", feature = "master-tactician", by = ["paragon-of-the-roads"] },
  { alters = "The cavalier's mount", feature = "mount", by = ["feytouched-mount"] },
  { alters = "Class skills" },
]
+++

Some cavaliers wander the lonely roads of the world—any world, including the First World—protecting
travelers and acting as their honor guard. Like the [Eldest](ref/rule/the-eldest) they usually
venerate, they wear heavy hoods and rarely show their faces.

Hooded knights are usually members of the [order of the blossom](ref/order/order-of-the-blossom)
(see page 27), the [order of the shield](ref/order/order-of-the-shield), or the
[order of the sword](ref/order/order-of-the-sword).

## Class Skills {#class-skills}

A hooded knight gains Knowledge (geography) and Survival as class skills instead of Climb and Swim.

This alters the cavalier's class skills.

## Feytouched Mount {#feytouched-mount}

A hooded knight's mount has the [feytouched](ref/template/fey-touched-creature) simple template (see
page 10) when he is riding it, but it cannot use its
[change shape](ref/carried/bestiary/rules/universal-monster-rules/change-shape) ability while being
ridden.

This ability alters the cavalier's mount.

## Hero of the Roads (Ex) {#hero-of-the-roads}

When on a road, a hooded knight gains a +2 bonus on initiative checks and Knowledge (geography),
Perception, Stealth, and Survival checks. These bonuses increase by 2 at 9th and 17th level. The
speed of any mount a hooded knight rides is increased by 10 feet at 9th level and by an additional
10 feet at 17th level. By spending 1 minute coaxing his allies' mounts and expending one use of his
challenge ability, a hooded knight can grant the same speed increase to the mounts ridden by all
allies within 30 feet who can see and hear him. This speed increase to his allies' mounts lasts for
1 hour.

A hooded knight and his mount can [hustle](ref/rule/overland-movement) while traveling on a road
without taking damage for 2 hours each day, plus an additional 2 hours at 5th level and every 5
levels thereafter (to a maximum of 8 hours at 15th level).

This ability replaces tactician.

## Champion of the Roads (Sp) {#champion-of-the-roads}

At 9th level, a hooded knight gains _[dimension door](ref/spell/dimension-door)_ as a
[spell-like ability](ref/umr/spell-like-abilities) with a caster level equal to his cavalier level.
If the hooded knight is riding a mount, his mount does not count against the number of creatures he
brings along with this ability. If the destination is not a road, the hooded knight is shunted to
the nearest open space on a road, taking damage as described in the
_[dimension door](ref/spell/dimension-door)_ spell.

The cavalier can use this ability once per day, plus one additional time for every 4 levels beyond
9th, to a maximum of three times per day at 17th level.

This ability replaces greater tactician.

## Paragon of the Roads (Sp) {#paragon-of-the-roads}

At 17th level, when a hooded knight uses his champion of the roads ability, he can treat the ability
as _[greater teleport](ref/spell/teleport-greater)_ rather than
_[dimension door](ref/spell/dimension-door)_. The hooded knight's mount and the mounts ridden by any
creatures he brings along do not count against the number of teleported creatures.

This ability replaces master tactician.
