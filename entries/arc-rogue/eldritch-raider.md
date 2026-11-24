+++
id = "ref/arc-rogue/eldritch-raider"
kind = "archetype"
title = "Eldritch Raider"
aon = "ArchetypeDisplay.aspx?FixedName=Rogue%20Eldritch%20Raider"
source_ids = ["advanced-race-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "eldritch_raider", path = "json/archetypes_rogue.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/rogue" },
]
[[sources]]
publication = "advanced-race-guide"
page = "189"

[fields]
kind = "archetype"
features = [
  { anchor = "class-skills" },
  { anchor = "skill-ranks-per-level" },
  { anchor = "detect-magic", level = 2 },
  { anchor = "eldritch-intuition", level = 3 },
  { anchor = "new-talents" },
  { anchor = "major-eldritch-magic" },
  { anchor = "minor-eldritch-magic" },
]
trades = [
  { replaces = "Rogue talent rogues gained at 2nd level", feature = "rogue-talents", levels = [2], by = ["detect-magic"] },
  { replaces = "Trap sense", feature = "trap-sense", by = ["eldritch-intuition"] },
]
+++

An eldritch raider is a rogue who seeks to unravel the mysteries of the destruction of the gillmen's
homeland. They explore old ruins that date back to the days of the old human empire and track down
relics and lore from its glory days. An eldritch raider has the following class features.

## Class Skills {#class-skills}

An eldritch raider adds Knowledge (arcana), Knowledge (history), and Spellcraft to her list of class
skills and removes Disguise, Perform, and Sleight of Hand from her list of class skills.

## Skill Ranks per Level {#skill-ranks-per-level}

6 + Int modifier.

## Detect Magic (Sp) {#detect-magic}

At 2nd level, an eldritch raider gains the ability to use _[detect magic](ref/spell/detect-magic)_
at will. The eldritch raider treats her rogue level as her caster level for this ability. This
ability counts as the [minor magic](ref/talent/minor-magic) rogue talent for purposes of qualifying
for other rogue talents. This ability replaces the rogue talent rogues gained at 2nd level.

## Eldritch Intuition (Ex) {#eldritch-intuition}

At 3rd level, an eldritch raider gains an intuitive sense that allows her to more easily activate
sorcerer and wizard spell completion and spell trigger items. She gains a +1 bonus on Use Magic
Device checks for this purpose. This bonus increases to +2 at 6th level, +3 at 9th level, +4 at 12th
level, +5 at 15th level, and +6 at 18th level. This ability replaces the trap sense class feature.

## New Talents {#new-talents}

An eldritch raider has access to the following new advanced talents when selecting rogue advanced
talents.

## Major Eldritch Magic (Sp) {#major-eldritch-magic}

The eldritch raider gains the ability to cast a 3rd-level spell from the sorcerer/wizard spell list
two times per day as a [spell-like ability](ref/umr/spell-like-abilities). The caster level for this
ability is equal to her rogue level. The save DC for this spell is 13 + her Intelligence modifier.
The eldritch raider must have an Intelligence of at least 13 to select this talent. The eldritch
raider must have the major magic, minor eldritch magic, and minor magic rogue talents before
choosing this talent.

## Minor Eldritch Magic (Sp) {#minor-eldritch-magic}

The eldritch raider gains the ability to cast a 2nd-level spell from the sorcerer/wizard spell list
two times per day as a [spell-like ability](ref/umr/spell-like-abilities). The caster level for this
ability is equal to her rogue level. The save DC for this spell is 12 + her Intelligence modifier.
The eldritch raider must have an Intelligence of at least 12 to select this talent. The eldritch
raider must have the [major magic](ref/talent/major-magic) and minor magic rogue talents before
choosing this talent.

## Rogue Talents {#rogue-talents}

The following rogue talents complement the eldritch raider archetype: major magic, minor magic,
[quick disable](ref/talent/quick-disable), [trap spotter](ref/talent/trap-spotter) (_Core
Rulebook_); [fast picks](ref/talent/fast-picks) (_Advanced Player's Guide_);
[black market connections](ref/talent/black-market-connections),
[esoteric scholar](ref/talent/esoteric-scholar), [ninja trick](ref/talent/ninja-trick) (slow
metabolism, [wall climber](ref/ninjatrick/wall-climber)) (_Ultimate Combat_).

## Advanced Talents {#advanced-talents}

The following advanced rogue talents complement the eldritch raider archetype: dispelling attack,
improved evasion, slippery mind (_Core Rulebook_); major eldritch magic, minor eldritch magic
(_Advanced Race Guide_); thoughtful reexamination (_Advanced Player's Guide_); familiar, hard to
fool (_Ultimate Combat_).
