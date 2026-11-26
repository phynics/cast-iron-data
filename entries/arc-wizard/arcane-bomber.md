+++
id = "ref/arc-wizard/arcane-bomber"
kind = "archetype"
title = "Arcane Bomber"
aon = "ArchetypeDisplay.aspx?FixedName=Wizard%20Arcane%20Bomber"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "arcane_bomber", path = "json/archetypes_wizard.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/wizard" },
]
[[sources]]
publication = "ultimate-combat"
page = "75"

[fields]
kind = "archetype"
features = [
  { anchor = "bomb", level = 1 },
  { anchor = "spellblast-bombs", level = 1 },
  { anchor = "school-of-the-bomb", level = 1 },
]
trades = [
  { replaces = "Arcane bond", feature = "arcane-bond", by = ["bomb"] },
  { replaces = "Cantrips", feature = "cantrips", by = ["spellblast-bombs"] },
  { replaces = "Arcane school", feature = "arcane-school", by = ["school-of-the-bomb"] },
]
+++

To many wizards, the experimentation of the alchemist seems quaint, if not dangerous or frightening.
A few wizards take up the secrets of the bomb, however, fusing alchemy with their already
considerable magical power.

## Bomb (Su) {#bomb}

At 1st level, the arcane bomber gains an ability nearly identical to the
[alchemist's](ref/class/alchemist) bomb ability (_Advanced Player's Guide_ 28). Unlike the
alchemist, at 1st level, the arcane bomber chooses one type of energy from the following list: acid,
cold, fire, and electricity. He can throw bombs of that type, but cannot modify them with
discoveries. This ability stacks with the alchemist bomb ability to determine the level of bomb
damage, but an arcane bomber that becomes an alchemist does not gain that class's bomb ability, nor
does an alchemist that becomes an arcane bomber gain this bomb ability. This ability replaces arcane
bond.

## Spellblast Bombs (Su) {#spellblast-bombs}

At 1st level, as a swift action, an arcane bomber can sacrifice one of his spells to empower the
next bomb he throws during his turn. When he does, he gains a bonus to hit with the next bomb he
throws before the end of his turn equal to the level of the spell he sacrificed, and a bonus to
damage equal to twice the level of the spell. This ability replaces cantrips, but the arcana bomber
gains the _[detect magic](ref/spell/detect-magic)_ and _[read magic](ref/spell/read-magic)_ cantrips
and places them in his spellbook. He can cast either of these as 1st-level spells.

## School of the Bomb {#school-of-the-bomb}

The creation and use of bombs is often so engrossing or intellectually taxing that an arcane bomber
forsakes four schools of magic. These opposition schools are chosen at 1st level and cannot be
changed later. An arcane bomber who prepares spells from his opposition school must use two spell
slots of that level to prepare the spell. In addition, the arcane bomber takes a -4 penalty on any
skill checks made when crafting a magic item that has a spell from one of his opposition schools.
This ability replaces arcane school.
