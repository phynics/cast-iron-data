+++
id = "ref/arc-magus/hexcrafter"
kind = "archetype"
title = "Hexcrafter"
aon = "ArchetypeDisplay.aspx?FixedName=Magus%20Hexcrafter"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "hexcrafter", path = "json/archetypes_magus.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/magus" },
]
[[sources]]
publication = "ultimate-magic"
page = "48"

[fields]
kind = "archetype"
features = [
  { anchor = "hex-magus", level = 4 },
  { anchor = "hex-arcana" },
  { anchor = "accursed-strike" },
  { anchor = "spells" },
]
trades = [
  { replaces = "Spell recall", feature = "spell-recall", by = ["hex-magus"] },
]
+++

A hexcrafter magus has uncovered the secret of using his _arcane pool_ to recreate
[witch](ref/class/witch) hexes. These magi can hex friend and foe, curse those they strike, and
expand their spell selection to include many curses and harmful spells.

## Hex Magus (Su) {#hex-magus}

At 4th level, the hexcrafter magus gains access to a small number of witch's hexes. The hexcrafter
magus picks one hex from the witch's hex class feature. He gains the benefit of or uses that hex as
if he were a witch of a level equal to his magus level. This feature replaces spell recall.

## Hex Arcana {#hex-arcana}

A hexcrafter gains access to the following magus arcana, or may select any witch hex in place of a
magus arcana. At 12th level, the hexcrafter may select a hex or major hex in place of a magus
arcana. At 18th level, a hexcrafter can select a hex, major hex, or grand hex in place of a magus
arcana. He cannot select any hex or arcana more than once.

## Accursed Strike (Sp) {#accursed-strike}

A hexcrafter magus who can cast _[bestow curse](ref/spell/bestow-curse)_,
_[major curse](ref/spell/curse-major)_, or any spell with the [curse](ref/spelldef/curse) descriptor
can deliver these prepared spells using the spellstrike ability, even if the spells are not touch
attack spells.

## Spells {#spells}

A hexcrafter magus adds the following spells to his magus spell list: _bestow curse_, _major curse_,
and all other spells of 6th level or lower that have the curse descriptor.

## Magus Arcana {#magus-arcana}

The following magus arcana complement the hexcrafter archetype:
[arcane accuracy](ref/arcana/arcane-accuracy), [broad study](ref/arcana/broad-study),
[familiar](ref/arcana/familiar), and quicken magic.
