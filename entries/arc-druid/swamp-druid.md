+++
id = "ref/arc-druid/swamp-druid"
kind = "archetype"
title = "Swamp Druid"
aon = "ArchetypeDisplay.aspx?FixedName=Druid%20Swamp%20Druid"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "swamp_druid", path = "json/archetypes_druid2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/druid" },
]
[[sources]]
publication = "advanced-players-guide"
page = "100"

[fields]
kind = "archetype"
features = [
  { anchor = "marshwight", level = 2 },
  { anchor = "swamp-strider", level = 3 },
  { anchor = "pond-scum", level = 4 },
  { anchor = "wild-shape", level = 6 },
  { anchor = "slippery", level = 13 },
]
trades = [
  { replaces = "Woodland stride", feature = "woodland-stride", by = ["marshwight"] },
  { replaces = "Trackless step", feature = "trackless-step", by = ["swamp-strider"] },
  { replaces = "Resist nature's lure", feature = "resist-nature-s-lure", by = ["pond-scum"] },
  { replaces = "A thousand faces", feature = "a-thousand-faces", by = ["slippery"] },
  { alters = "Wild shape", feature = "wild-shape", by = ["wild-shape"] },
]
+++

Some druids eschew pleasant glades and groves and instead seek out dank marshes, misty bogs and
heaths, and trackless swamps as the place they call home and watch over with care, finding beauty
and life in abundance in places few others would willingly enter.

## Marshwight (Ex) {#marshwight}

At 2nd level, a swamp druid gains a bonus on Initiative checks and Knowledge (geography),
Perception, Stealth, Swim, and Survival checks equal to 1/2 her druid level in swamp terrain, and
she cannot be tracked in such an environment. This ability replaces woodland stride.

## Swamp Strider (Ex) {#swamp-strider}

At 3rd level, a swamp druid suffers no penalty to speed or on Acrobatics or Stealth checks in bogs
and undergrowth. This ability replaces trackless step.

## Pond Scum (Ex) {#pond-scum}

At 4th level, a swamp druid gains a +4 bonus on saves against disease and the exceptional,
supernatural, and [spell-like abilities](ref/umr/spell-like-abilities) of monstrous humanoids. A
swamp druid also gains DR/— equal to [half](ref/misc/fractions-and-rounding) her druid level against
attacks by swarms. If this damage resistance prevents damage, the druid is unaffected by distraction
or other special attacks of the swarm. This ability replaces resist nature's lure.

## Wild Shape (Su) {#wild-shape}

A swamp druid gains this ability at 6th level, except that her effective druid level for the ability
is equal to her druid level - 2.

## Slippery (Ex) {#slippery}

At 13th level, a swamp druid gains continuous
_[freedom of movement](ref/spell/freedom-of-movement)_. This ability replaces a thousand faces.
