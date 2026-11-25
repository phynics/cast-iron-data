+++
id = "ref/arc-magus/nature-bonded-magus"
kind = "archetype"
title = "Nature-Bonded Magus"
aon = "ArchetypeDisplay.aspx?FixedName=Magus%20Nature-Bonded%20Magus"
source_ids = ["ultimate-wilderness"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "nature_bonded_magus", path = "json/archetypes_magus.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/magus" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "92"

[fields]
kind = "archetype"
features = [
  { anchor = "natural-magic" },
  { anchor = "plant-familiar", level = 1 },
  { anchor = "familiar-symbiosis", level = 4 },
  { anchor = "woodland-stride", level = 7 },
  { anchor = "improved-familiar-symbiosis", level = 11 },
]
trades = [
  { replaces = "Arcane pool", feature = "arcane-pool", by = ["plant-familiar"] },
  { replaces = "Spell recall", feature = "spell-recall", by = ["familiar-symbiosis"] },
  { replaces = "Knowledge pool", feature = "knowledge-pool", by = ["woodland-stride"] },
  { replaces = "Improved spell recall", feature = "improved-spell-recall", by = ["improved-familiar-symbiosis"] },
]
+++

A nature-bonded magus synergizes arcane magic and the divine magic traditions of druids into a
deadly synthesis.

## Natural Magic {#natural-magic}

A nature-bonded magus adds one 0-level and one 1st-level spell from the druid spell list to the
magus spell list and his spellbook. Each time a nature-bonded magus gains the ability to cast a new
level of spells, he can add one spell of that level from the druid spell list to both the magus
spell list and his spellbook.

## Plant Familiar {#plant-familiar}

A nature-bonded magus gains the [familiar](ref/arcana/familiar) magus arcana. A nature-bonded magus
must choose a plant familiar (see page 190) as his familiar.

This replaces arcane pool.

## Familiar Symbiosis (Su) {#familiar-symbiosis}

At 4th level, when a nature-bonded magus is adjacent to his familiar, he can merge with his familiar
as a standard action; both the nature-bonded magus and the familiar provoke attacks of opportunity
with this action. Doing so causes the plant familiar to bond with a part of the nature-bonded
magus's body as though it were growing on him. While merged, the nature-bonded magus's familiar can
take no actions (but can still attempt Perception checks and communicate with the nature-bonded
magus), and it can't be targeted or harmed by effects. As long as his familiar is merged, the
nature-bonded magus gains half his plant familiar's natural armor adjustment to AC.

The nature-bonded magus can separate from his plant familiar as a standard action that provokes
attacks of opportunity for both of them. Once they have separated, the familiar appears in an
adjacent square of the nature-bonded magus' choosing.

This replaces spell recall.

## Woodland Stride (Ex) {#woodland-stride}

At 7th level, a nature-bonded magus can move through any sort of undergrowth (such as natural
briars, overgrown areas, thorns, and similar terrain) at his normal speed and without taking damage
or suffering any other impairment. Briars, overgrown areas, and thorns that are enchanted or
magically manipulated to impede motion, however, still affect him.

This replaces knowledge pool.

## Improved Familiar Symbiosis (Su) {#improved-familiar-symbiosis}

At 11th level, when a nature-bonded magus is merged with his familiar, he gains a +4 enhancement
bonus to his Strength and Constitution.

This replaces improved spell recall.
