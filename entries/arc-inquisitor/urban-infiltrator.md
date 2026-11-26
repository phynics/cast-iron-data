+++
id = "ref/arc-inquisitor/urban-infiltrator"
kind = "archetype"
title = "Urban Infiltrator"
aon = "ArchetypeDisplay.aspx?FixedName=Inquisitor%20Urban%20Infiltrator"
source_ids = ["magic-tactics-toolbox"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "urban_infiltrator", path = "json/archetypes_inquisitor.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/inquisitor" },
]
[[sources]]
publication = "magic-tactics-toolbox"
page = "18"

[fields]
kind = "archetype"
features = [
  { anchor = "gifted-detective", level = 1 },
  { anchor = "a-thousand-faces", level = 11 },
]
trades = [
  { replaces = "Monster lore", feature = "monster-lore", by = ["gifted-detective"] },
  { replaces = "Stalwart", feature = "stalwart", by = ["a-thousand-faces"] },
  { alters = "Class skills" },
]
+++

Masters of secretly gathering information to further their faith's ends, urban infiltrators excel at
operating within an unfriendly society or infiltrating an enemy cult. This archetype is popular
among Cult of the [Dawnflower](ref/faith/sarenrae) inquisitors operating in Taldor, but it is
available to any inquisitor who prefers subtle investigation to forthright zeal.

## Class Skills {#class-skills}

An urban infiltrator adds Disable Device, Knowledge (history), Knowledge (local), and Knowledge
(nobility) to her list of class skills in place of Knowledge (dungeoneering) and Knowledge (nature).

This alters the inquisitor's class skills.

## Gifted Detective (Ex) {#gifted-detective}

An urban infiltrator adds her Wisdom modifier as well as her Charisma modifier on Bluff and Disguise
skill checks and on Diplomacy checks to gather information. Attempting a Diplomacy check to gather
information never takes an urban infiltrator more than 1 hour.

This ability replaces monster lore.

## A Thousand Faces (Su) {#a-thousand-faces}

At 11th level, an urban inquisitor gains the ability to change her appearance at will, as if using
the _[alter self](ref/spell/alter-self)_ spell.

This ability replaces stalwart.
