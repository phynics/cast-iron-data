+++
id = "ref/arc-oracle/enlightened-philosopher"
kind = "archetype"
title = "Enlightened Philosopher"
aon = "ArchetypeDisplay.aspx?FixedName=Oracle%20Enlightened%20Philosopher"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "enlightened_philosopher", path = "json/archetypes_oracle.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/oracle" },
]
[[sources]]
publication = "ultimate-magic"
page = "58"

[fields]
kind = "archetype"
features = [
  { anchor = "recommended-mysteries" },
  { anchor = "revelations" },
  { anchor = "mental-acuity" },
  { anchor = "final-revelation" },
]
trades = [
  { replaces = "Additional class skills from her mystery", feature = "mystery", power = "class skills" },
  { replaces = "Mystery bonus spells at these levels", feature = "mystery", levels = [4, 6, 8, 10, 12, 14, 16, 18], power = "bonus spells" },
  { replaces = "Final revelation of the oracle's mystery", feature = "final-revelation", by = ["final-revelation"] },
]
+++

The enlightened philosopher seeks enlightenment through compassion, moderation, and humility. By
following her philosophy's teachings, the enlightened philosopher seeks to reach enlightenment and
become one with the universe.

## Alignment {#alignment}

Any lawful.

## Recommended Mysteries {#recommended-mysteries}

ancestor, fire, heavens, lore, metal, nature, stone, time, waves, wood.

## Class Skills {#class-skills}

An enlightened philosopher adds Linguistics and all Knowledge skills to her list of class skills.
These replace the additional class skills from her mystery.

## Bonus Spells {#bonus-spells}

_owl's wisdom_ (4th), _water walk_ (6th), _discern lies_ (8th), _true seeing_ (10th), _wind walk_
(12th), _ethereal jaunt_ (14th), _moment of prescience_ (16th), _astral projection_ (18th). These
bonus spells replace the oracle's mystery bonus spells at these levels.

## Revelations {#revelations}

An enlightened philosopher must take the following revelation at 7th level.

## Mental Acuity (Ex) {#mental-acuity}

As the [lore](ref/mystery/lore) mystery revelation (see page 50 of the _Advanced Player's Guide_).

## Final Revelation {#final-revelation}

Upon achieving 20th level, you achieve true enlightenment and become one with the universe. You
receive a bonus on all saving throws equal to your Charisma modifier. You become immune to
confusion, exhaustion, fatigue, nausea, and sickened effects. You can take 20 on all Knowledge skill
checks. Should you die, you are reborn 3 days later as a living example of the summoning of your
chosen philosophy (treat as the _[reincarnate](ref/spell/reincarnate)_ spell). This replaces the
final revelation of the oracle's mystery.
