+++
id = "ref/arc-alchemist/metamorph"
kind = "archetype"
title = "Metamorph"
aon = "ArchetypeDisplay.aspx?FixedName=Alchemist%20Metamorph"
source_ids = ["ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "metamorph", path = "json/archetypes_alchemist2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/alchemist" },
]
[[sources]]
publication = "ultimate-intrigue"
page = "19"

[fields]
kind = "archetype"
features = [
  { anchor = "shapechanger", level = 1 },
  { anchor = "mutagen", level = 1 },
  { anchor = "adaptive-physiology", level = 3 },
]
trades = [
  { replaces = "Alchemy", feature = "alchemy", by = ["shapechanger"] },
  { replaces = "bombs", feature = "bomb", by = ["shapechanger"] },
  { replaces = "extracts", feature = "extracts", by = ["shapechanger"] },
  { replaces = "mutagen", feature = "mutagen", by = ["mutagen"] },
  { replaces = "Throw Anything", feature = "throw-anything", by = ["shapechanger"] },
  { replaces = "Swift alchemy", feature = "swift-alchemy", by = ["adaptive-physiology"] },
  { replaces = "swift poisoning", feature = "swift-poisoning", by = ["adaptive-physiology"] },
  { replaces = "instant alchemy", feature = "instant-alchemy", by = ["adaptive-physiology"] },
  { alters = "Class skills" },
]
+++

Metamorphs eschew traditional alchemy, focusing on internal chemistry and the transfiguration of
living forms.

## Class Skills {#class-skills}

A metamorph adds Disguise to her list of class skills.

This alters the alchemist's class skills.

## Shapechanger (Su) {#shapechanger}

At 1st level, a metamorph gains the ability to transform herself into another form. This ability
functions like _[alter self](ref/spell/alter-self)_, except as noted here. The effect lasts for 1
hour per metamorph's alchemist level, or until she changes back. Changing form (to another form or
back) is a standard action that doesn't provoke attacks of opportunity. The metamorph is
[fatigued](ref/misc/fatigued) for 1 round each time she changes shape.

A metamorph can use this ability once per day at 1st level, and an additional time per day at 4th
level, and every 2 alchemist levels thereafter, for a total of nine times at 18th level. At 20th
level, a metamorph can use shapechanger as a free action once per round, either before or after all
her other actions, with no daily limit.

This ability can also function as _[monstrous physique I](ref/spell/monstrous-physique-1)_ at 5th
level, as _[monstrous physique II](ref/spell/monstrous-physique-2)_ at 9th level, as
_[monstrous physique III](ref/spell/monstrous-physique-3)_ at 11th level, as
_[monstrous physique IV](ref/spell/monstrous-physique-4)_ or
_[giant form I](ref/spell/giant-form-1)_ at 13th level, and as
_[giant form II](ref/spell/giant-form-2)_ at 15th level.

This ability replaces alchemy (which also includes bombs, extracts, and mutagen) and Throw Anything.

## Mutagen (Ex) {#mutagen}

At 1st level, a metamorph gains mutagen as a normal alchemist. She can take mutagen and cognatogen
discoveries despite not possessing the alchemy class feature that normally grants mutagen.

## Adaptive Physiology (Ex) {#adaptive-physiology}

At 3rd level, a metamorph gains a 25% chance to negate critical hits and precision damage, similar
to the [preserve organs](ref/discovery/preserve-organs) discovery. This chance increases to 50% at
6th level, and to 75% at 18th level.

This ability replaces swift alchemy, swift poisoning, and instant alchemy.
