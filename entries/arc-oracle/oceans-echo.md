+++
id = "ref/arc-oracle/oceans-echo"
kind = "archetype"
title = "Ocean's Echo"
aon = "ArchetypeDisplay.aspx?FixedName=Oracle%20Ocean%27s%20Echo"
source_ids = ["blood-of-the-sea"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "oceans_echo", path = "json/archetypes_oracle.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/oracle" },
]
[[sources]]
publication = "blood-of-the-sea"
page = "12"

[fields]
kind = "archetype"
features = [
  { anchor = "inspiring-song", level = 1 },
]
trades = [
  { replaces = "Additional class skills from her mystery", feature = "mystery", power = "class skills" },
  { replaces = "Mystery bonus spells at these levels", feature = "mystery", levels = [4, 8, 10, 12, 14], power = "bonus spells" },
  { replaces = "Revelations gained at 1st, 3rd, and 15th level", feature = "revelation", levels = [1, 3, 15], by = ["inspiring-song"] },
]
+++

Although many [merfolk](ref/race/merfolk) claim deep connections to both art and the natural world,
a rare few merfolk can manipulate the forces of nature and weave them into song. An ocean's echo is
a merfolk gifted with the powers of an oracle and a singing voice that evokes the legendary tales of
merfolk virtuosos.

## Class Skills {#class-skills}

An ocean's echo adds Bluff, Intimidate, Knowledge (nature), and Perform to her list of class skills.
These replace the additional class skills from her mystery.

## Bonus Spells {#bonus-spells}

_Sound burst_ (4th), _shout_ (8th), _song of discord_ (10th), _greater shout_ (12th), and _pied
piping_ (14th). These bonus spells replace the oracle's mystery bonus spells at these levels.

## Inspiring Song (Ex) {#inspiring-song}

The voice of an ocean's echo provides inspiration to allies. This ability is identical to bardic
performance (using Perform \[sing\] only), allowing her to
[inspire courage](ref/performance/inspire-courage) at 1st level,
[inspire competence](ref/performance/inspire-competence) at 3rd level, and
[inspire heroics](ref/performance/inspire-heroics) at 15th level, as a bard of the ocean's echo's
level. It is usable a total number of rounds per day equal to her level + her Charisma modifier
(minimum 1).

This ability replaces the revelations gained at 1st, 3rd, and 15th level.

## Recommended Mysteries {#recommended-mysteries}

[Ancestor](ref/mystery/ancestor), [heavens](ref/mystery/heavens), [life](ref/mystery/life),
[lore](ref/mystery/lore), [nature](ref/mystery/nature), [time](ref/mystery/time),
[waves](ref/mystery/waves), [wind](ref/mystery/wind).
