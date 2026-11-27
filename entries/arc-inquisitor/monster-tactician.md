+++
id = "ref/arc-inquisitor/monster-tactician"
kind = "archetype"
title = "Monster Tactician"
aon = "ArchetypeDisplay.aspx?FixedName=Inquisitor%20Monster%20Tactician"
source_ids = ["monster-summoners-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "monster_tactician", path = "json/archetypes_inquisitor.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/inquisitor" },
]
[[sources]]
publication = "monster-summoners-handbook"
page = "7"

[fields]
kind = "archetype"
features = [
  { anchor = "summon-monster", level = 1 },
  { anchor = "summon-tactics", level = 5 },
]
trades = [
  { replaces = "Judgment", feature = "judgment", by = ["summon-monster"] },
  { replaces = "Discern lies", feature = "discern-lies", by = ["summon-tactics"] },
  { replaces = "second judgment", feature = "second-judgment", by = ["summon-tactics"] },
  { replaces = "third judgment", feature = "third-judgment", by = ["summon-tactics"] },
  { replaces = "slayer", feature = "slayer", by = ["summon-tactics"] },
  { replaces = "true judgment", feature = "true-judgment", by = ["summon-tactics"] },
]
+++

While most inquisitors have learned to take advantage of the movements of their opponents and allies
in combat, some instead summon creatures as a means of claiming strategic advantage, exploiting the
mystic connection between themselves and their summoned creatures to impart a bit of their own
tactical knowledge.

## Summon Monster (Sp) {#summon-monster}

Starting at 1st level, a monster tactician can cast _[summon monster I](ref/spell/summon-monster-1)_
as a [spell-like ability](ref/umr/spell-like-abilities) a number of times per day equal to 3 + her
Wisdom modifier. She can cast this spell as a standard action, and the creatures remain for 1 minute
per level (instead of 1 round per level). At 3rd level and every 2 inquisitor levels thereafter, the
power of this ability increases by 1 spell level, allowing her to summon more powerful creatures (to
a maximum of _[summon monster IX](ref/spell/summon-monster-9)_ at 17th level). A monster tactician
cannot have more than one _[summon monster](ref/spell/summon-monster)_ spell active in this way at a
time; if she uses another, any existing _[summon monster](ref/spell/summon-monster)_ immediately
ends. These _[summon monster](ref/spell/summon-monster)_ spells are considered to be part of the
monster tactician's spell list for the purposes of spell trigger and spell completion items. In
addition, she can expend uses of this ability to fulfill the construction requirements of any magic
items she creates, so long as she can use this ability to cast the required spells.

At 2nd level and each level thereafter, the monster tactician can add one monster from the expanded
_[summon monster](ref/spell/summon-monster)_ list (see pages 28–29) to her list of available
summoned creatures. She can add a new option to any _summon monster_ spell she can cast at the time
she chooses the monster; once made, these choices cannot be changed.

This ability replaces judgment.

## Summon Tactics (Su) {#summon-tactics}

At 5th level, every time a monster tactician casts a summoning spell, she can choose any one
teamwork feat she knows. All creatures summoned by the spell are treated as if they had the chosen
feat for all purposes, without needing to meet any prerequisites. At 8th level and again at 16th
level, the number of teamwork feats that she can choose when casting a summoning spell increases
by 1. She cannot choose the same feat twice. At 20th level, all creatures summoned by the spell are
treated as if they knew all of the monster tactician's teamwork feats. This ability replaces
_discern lies_, second judgment, third judgment, slayer, and true judgment.
