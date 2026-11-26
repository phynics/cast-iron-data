+++
id = "ref/arc-alchemist/aquachymist"
kind = "archetype"
title = "Aquachymist"
aon = "ArchetypeDisplay.aspx?FixedName=Alchemist%20Aquachymist"
source_ids = ["aquatic-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "aquachymist", path = "json/archetypes_alchemist.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/alchemist" },
]
[[sources]]
publication = "aquatic-adventures"
page = "49"

[fields]
kind = "archetype"
features = [
  { anchor = "sureseal-alchemy", level = 1 },
  { anchor = "underwater-bombs", level = 1 },
  { anchor = "amphibious-mutagen", level = 2 },
]
trades = [
  { replaces = "The discovery at 2nd level", feature = "discovery", levels = [2], by = ["amphibious-mutagen"] },
  { alters = "Alchemy", feature = "alchemy", by = ["sureseal-alchemy"] },
  { alters = "Bombs", feature = "bomb", by = ["underwater-bombs"] },
  { alters = "Class skills" },
]
+++

The principles of alchemy work equally well underwater and on land, but mixing solutions and keeping
them pure is a tougher task beneath the waves. Aquachymists are those rare few alchemists of
land-dwelling and aquatic races alike who strive to unlock new and fantastic secrets of alchemy that
can be discovered only in the water's depths.

## Class Skills {#class-skills}

An aquachymist has Swim as a class skill instead of Fly.

This alters the alchemist's class skills.

## Sureseal Alchemy (Su) {#sureseal-alchemy}

An aquachymist's extracts and mutagens self-generate a flexible outer shell of sureseal, similar to
[sureseal bladders](ref/eq-misc/sureseal-bladder-mundane) (see page 57), allowing the aquachymist to
craft a waterproof supply without expending a plethora of sureseal bladders.

This ability alters alchemy.

## Underwater Bombs (Su) {#underwater-bombs}

An aquachymist's fire bombs deal steam damage, allowing them to deal damage underwater or on land.
Since thrown weapons don't work well underwater, when the aquachymist creates a bomb, he either
weights it or includes excess air as part of the action of creating the bomb, granting the bomb his
choice of swiftly rising or swiftly sinking [buoyancy](ref/rule/buoyancy) and allowing him to target
foes directly above or below him. If the attack misses, the bomb doesn't deal splash damage, but
instead continues to travel up or down until it loses potency at the end of the alchemist's turn;
the exception is when the aquachymist throws a swiftly sinking bomb close to the bottom, in which
case it might reach the bottom and explode there. Because of the strange aquadynamic features of the
aquachymist's underwater bombs, they have a range increment of only 5 feet above the water.

This ability alters bombs.

## Amphibious Mutagen (Su) {#amphibious-mutagen}

At 2nd level, an aquachymist's mutagen allows him to breathe both air and water for its duration, in
addition to its other effects.

This ability replaces the discovery at 2nd level.
