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
replaces = ["Spell recall"]
replaces_features = ["spell-recall"]
+++

A hexcrafter magus has uncovered the secret of using his _arcane pool_ to recreate
[witch](ref/class/witch) hexes. These magi can hex friend and foe, curse those they strike, and
expand their spell selection to include many curses and harmful spells.

**Hex Magus (Su)**

**Ability:** The hexcrafter magus gains access to a small number of witch hexes. The hexcrafter
magus picks one hex from the witch's _hex_ class feature. He gains the benefit of or uses that hex
as if he were a witch of a level equal to his magus level.

**Gained:** At 4th Level

**Replaces:** Spell recall

**Hex Arcana**

**Ability:** A hexcrafter gains access to the following magus arcana, or may select any witch hex in
place of a magus arcana.

**At 12th Level:** The hexcrafter may select a hex or major hex in place of a magus arcana.

**At 18th Level:** A hexcrafter can select a hex, major hex, or grand hex in place of a magus
arcana.

**Special:** He cannot select any hex or arcana more than once.

**Accursed Strike (Sp)**

**Ability:** A hexcrafter magus who can cast [bestow curse](ref/spell/bestow-curse),
[major curse](ref/spell/curse-major), or any spell with the [curse](ref/spelldef/curse) descriptor
can deliver these prepared spells using the _spellstrike_ ability, even if the spells are not touch
attack spells.

**Spells**

**Info:** A hexcrafter magus adds the following spells to his magus spell list: _bestow curse, major
curse,_ and all other spells of 6th level or lower that have the curse descriptor.

**Magus Arcana:** The following magus arcana complement the hexcrafter archetype:
[arcane accuracy](ref/arcana/arcane-accuracy), [broad study](ref/arcana/broad-study),
[familiar](ref/arcana/familiar), and [quickened magic](ref/arcana/quickened-magic).
