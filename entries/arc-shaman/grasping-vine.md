+++
id = "ref/arc-shaman/grasping-vine"
kind = "archetype"
title = "Grasping Vine"
aon = "ArchetypeDisplay.aspx?FixedName=Shaman%20Grasping%20Vine"
source_ids = ["legacy-of-the-first-world"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "grasping_vine", path = "json/archetypes_shaman.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/shaman" },
]
[[sources]]
publication = "legacy-of-the-first-world"
page = "16"

[fields]
kind = "archetype"
features = [
  { anchor = "spirit" },
  { anchor = "plant-spirit" },
  { anchor = "verdant-magic" },
  { anchor = "greentongue", level = 2 },
  { anchor = "flower-s-form", level = 8 },
]
trades = [
  { replaces = "Spirit magic spells granted by the shaman's spirit", feature = "spirit-magic", by = ["verdant-magic"] },
  { replaces = "Shaman's hex gained at 2nd level", feature = "hex", levels = [2], by = ["greentongue"] },
  { replaces = "Shaman's hex gained at 8th level", feature = "hex", levels = [8], by = ["flower-s-form"] },
  { alters = "Spirit animal", feature = "spirit-animal", by = ["plant-spirit"] },
]
+++

Grasping vine shamans are typically adherents of one of several scattered sects dedicated to the
Green Mother. They revere plant life in all its forms, with a special fondness for poisonous or
carnivorous plants. Unlike most shamans, a grasping vine is guided by a plantlike creature rather
than a spirit animal.

## Spirit {#spirit}

Though a grasping vine is not limited to a particular choice of spirit, common selections are
[Life](ref/shamanspirit/life), [Nature](ref/shamanspirit/nature), or [Wood](ref/shamanspirit/wood).

## Plant Spirit (Ex) {#plant-spirit}

A shaman's spirit animal is made of leaves and thorny vines. This [plant](ref/type/plant) spirit has
the statistics and abilities as a shaman's spirit animal, but it is treated as a creature of the
plant type rather than a native outsider.

This ability alters the shaman's spirit animal.

## Verdant Magic {#verdant-magic}

A grasping vine adds the following spells to the list of spells she can cast using spirit magic:
_entangle_ (1st), _barkskin_ (2nd), _thorny entanglement_ (3rd), _command plants_ (4th), _wall of
thorns_ (5th), _fire seeds_ (6th), _animate plants_ (7th), _horrid wilting_ (8th), and _shambler_
(9th).

This ability replaces the spirit magic spells granted by the shaman's spirit.

## Greentongue (Sp) {#greentongue}

At 2nd level, as a standard action, a grasping vine can use
_[speak with plants](ref/spell/speak-with-plants)_ as a
[spell-like ability](ref/umr/spell-like-abilities). The grasping vine can use this ability a number
of times per day equal to half her shaman level. In addition, while under the effects of
_[speak with plants](ref/spell/speak-with-plants)_, the grasping vine can deliver a
_[suggestion](ref/spell/suggestion)_ (as per the spell) to a single plant creature within 30 feet,
ignoring the plant's immunity to mind-affecting effects. The grasping vine can use this ability once
per day at 2nd level, plus an additional time per day every 4 levels after 2nd level.

This ability replaces the shaman's hex gained at 2nd level.

## Flower's Form (Sp) {#flower-s-form}

At 8th level, as a standard action, a grasping vine can assume the form of a Small or Medium plant
creature, as per _[plant shape I](ref/spell/plant-shape-1)_. At 12th level, this ability functions
as _[plant shape II](ref/spell/plant-shape-2)_. At 16th level, this ability functions as
_[plant shape III](ref/spell/plant-shape-3)_. The grasping vine can use this ability for 1 minute
per shaman level per day. This duration does not need to be used consecutively, but it must be spent
in 1-minute increments.

This ability replaces the shaman's hex gained at 8th level.
