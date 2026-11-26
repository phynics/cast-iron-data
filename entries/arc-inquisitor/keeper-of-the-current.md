+++
id = "ref/arc-inquisitor/keeper-of-the-current"
kind = "archetype"
title = "Keeper of the Current"
aon = "ArchetypeDisplay.aspx?FixedName=Inquisitor%20Keeper%20of%20the%20Current"
source_ids = ["blood-of-the-sea"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "keeper_of_the_current", path = "json/archetypes_inquisitor.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/inquisitor" },
]
[[sources]]
publication = "blood-of-the-sea"
page = "24"

[fields]
kind = "archetype"
features = [
  { anchor = "underwater-hunter", level = 2 },
  { anchor = "marine-magic", level = 5 },
  { anchor = "rudderless-attack", level = 5 },
]
trades = [
  { replaces = "Track", feature = "track", by = ["underwater-hunter"] },
  { replaces = "Discern lies", feature = "discern-lies", by = ["rudderless-attack"] },
  { alters = "Spellcasting", feature = "spells", by = ["marine-magic"] },
]
+++

Aquatic creatures worship many different deities and powers based on their alignment, their
community, and their culture, including [Gozreh](ref/faith/gozreh), [Hei Feng](ref/faith/hei-feng),
[Kelizandri](ref/faith/kelizandri), and the fearsome demon lord [Dagon](ref/faith/dagon). These
deities all have organized churches beneath the waves that engage zealous followers to hunt down
apostates and enemies. Regardless of their faith, these undersea zealots are known as keepers of the
current.

## Underwater Hunter (Ex) {#underwater-hunter}

Tracking creatures underwater is particularly challenging, but a keeper of the current can read
traces of eddies in the water to follow her prey. A keeper of the current adds her level as a bonus
on Survival checks to follow creatures underwater. She gains no bonus when finding or following
tracks out of the water. Rules for using the Survival skill underwater are on page 47 of _Pathfinder
Campaign Setting: Aquatic Adventures_.

This ability replaces track.

## Marine Magic {#marine-magic}

At 5th level and at every 3 levels thereafter, a keeper of the current can learn a spell with the
water descriptor from the cleric, druid, inquisitor, or wizard spell list in place of a spell she
already knows. In effect, she loses an old spell in exchange for a new one. The new spell's level
must be the same as that of the spell being exchanged, and it must be at least 1 level lower than
the highest-level inquisitor spell she can cast. The keeper of the current can swap out only a
single spell at any given level and must choose whether to swap the spell at the same time she gains
new spells known for the level.

This ability alters the inquisitor's spellcasting.

## Rudderless Attack (Ex) {#rudderless-attack}

At 5th level, an opponent that takes extra damage from the keeper of the current's
[bane](ref/spell/bane) or greater bane ability has its swim speed halved for 1d4 rounds. A
successful Fortitude saving throw (DC = 10 + half the inquisitor's level + her Wisdom modifier)
negates this effect. If the keeper of the current targets a creature already affected by this
ability, its swim speed is not further reduced but the duration of the effect is extended by 1d4
rounds.

This ability replaces discern lies.
