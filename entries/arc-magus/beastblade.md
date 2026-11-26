+++
id = "ref/arc-magus/beastblade"
kind = "archetype"
title = "Beastblade"
aon = "ArchetypeDisplay.aspx?FixedName=Magus%20Beastblade"
source_ids = ["familiar-folio"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "beastblade", path = "json/archetypes_magus.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/magus" },
]
[[sources]]
publication = "familiar-folio"
page = "8"

[fields]
kind = "archetype"
features = [
  { anchor = "familiar", level = 3 },
  { anchor = "tandem-touch", level = 4 },
  { anchor = "familiar-pool", level = 7 },
  { anchor = "familiar-spellstrike", level = 11 },
]
trades = [
  { replaces = "Magus arcana gained at 3rd level", feature = "magus-arcana", levels = [3], by = ["familiar"] },
  { replaces = "Spell recall", feature = "spell-recall", by = ["tandem-touch"] },
  { replaces = "Knowledge pool", feature = "knowledge-pool", by = ["familiar-pool"] },
  { replaces = "Improved spell recall", feature = "improved-spell-recall", by = ["familiar-spellstrike"] },
]
+++

Beastblade magi work in tandem with their familiars, using spell, steel, and claw to clear the
battlefield of foes.

## Familiar (Ex) {#familiar}

At 3rd level, the beastblade gains the [familiar](ref/arcana/familiar) magus arcana. This ability
replaces the magus arcana gained at 3rd level.

## Tandem Touch (Su) {#tandem-touch}

At 4th level, while the beastblade's familiar is holding the charge for a touch spell, the
beastblade can cast another spell without discharging the familiar's held charge. This ability
replaces spell recall.

## Familiar Pool (Su) {#familiar-pool}

At 7th level, when a beastblade prepares his magus spells, he can expend points from his arcane pool
(up to a maximum number of points equal to his Intelligence modifier) to empower his familiar. For
each point expended in this way, the familiar can cast one magus spell as a
[spell-like ability](ref/umr/spell-like-abilities) once that day. Each spell selected must be 3
spell levels lower than the highest spell level the beastblade can cast, and can't require a
material component that costs more than 1 gp. This ability replaces knowledge pool.

## Familiar Spellstrike (Su) {#familiar-spellstrike}

At 11th level, whenever a beastblade's familiar successfully delivers a touch spell against a
creature the magus threatens, the target provokes an attack of opportunity from the magus. This
ability replaces improved spell recall.
