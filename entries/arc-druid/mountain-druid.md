+++
id = "ref/arc-druid/mountain-druid"
kind = "archetype"
title = "Mountain Druid"
aon = "ArchetypeDisplay.aspx?FixedName=Druid%20Mountain%20Druid"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "mountain_druid", path = "json/archetypes_druid.json" },
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
  { anchor = "mountaineer", level = 2 },
  { anchor = "sure-footed", level = 3 },
  { anchor = "spire-walker", level = 4 },
  { anchor = "wild-shape", level = 6 },
  { anchor = "mountain-stance", level = 9 },
  { anchor = "mountain-stone", level = 13 },
]
trades = [
  { replaces = "Woodland stride", feature = "woodland-stride", by = ["mountaineer"] },
  { replaces = "Trackless step", feature = "trackless-step", by = ["sure-footed"] },
  { replaces = "Resist nature's lure", feature = "resist-nature-s-lure", by = ["spire-walker"] },
  { replaces = "Venom immunity", feature = "venom-immunity", by = ["mountain-stance"] },
  { replaces = "A thousand faces", feature = "a-thousand-faces", by = ["mountain-stone"] },
  { alters = "Wild shape", feature = "wild-shape", by = ["wild-shape"] },
]
+++

As more and more of the soft, easy lands become cultivated and civilized, many druids look for
refuge and solitude among the eternal peaks of the highest mountains.

## Mountaineer (Ex) {#mountaineer}

At 2nd level, a mountain druid gains a bonus on Initiative checks and Climb, Knowledge (geography),
Perception, Stealth, and Survival checks equal to [half](ref/misc/fractions-and-rounding) her druid
level in mountainous terrain, and she cannot be tracked in such an environment. This ability
replaces woodland stride.

## Sure-Footed (Ex) {#sure-footed}

At 3rd level, a mountain druid suffers no penalty to speed or on Acrobatics or Stealth checks when
walking across steep slopes, rubble, or scree. This ability replaces trackless step.

## Spire Walker (Ex) {#spire-walker}

At 4th level, a mountain druid does not lose her Dexterity bonus when climbing. A mountain druid is
immune to [altitude sickness](ref/rule/mountain-travel) and ignores the effects of a cold climate as
if under the effects of _[endure elements](ref/spell/endure-elements)_. This ability replaces resist
nature's lure.

## Wild Shape (Su) {#wild-shape}

A mountain druid gains this ability at 6th level, except that her effective druid level for the
ability is equal to her druid level - 2. A mountain druid cannot use wild shape to adopt a plant
form. However, at 12th level she can assume the form of a Large giant as if using
_[giant form I](ref/spell/giant-form-1)_. At 16th level, she may assume the form of a Huge giant as
if using _[giant form II](ref/spell/giant-form-2)_.

## Mountain Stance (Ex) {#mountain-stance}

At 9th level, a mountain druid gains immunity to petrification and receives a +4 bonus on saving
throws or to CMD to resist any attempt to push, pull, bull rush, or drag her, or to resist any other
effect that would physically move her from her position (e.g., _[repel wood](ref/spell/repel-wood),
[reverse gravity](ref/spell/reverse-gravity),_ or being blown away by high winds). This does not
protect her against being tripped, grappled, or overrun. This ability replaces venom immunity.

## Mountain Stone (Ex) {#mountain-stone}

At 13th level, a mountain druid can transform her body into a weathered stone outcrop and back at
will. This effect functions as _[statue](ref/spell/statue)_. This ability replaces a thousand faces.
