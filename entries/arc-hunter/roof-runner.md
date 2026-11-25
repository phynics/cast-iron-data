+++
id = "ref/arc-hunter/roof-runner"
kind = "archetype"
title = "Roof Runner"
aon = "ArchetypeDisplay.aspx?FixedName=Hunter%20Roof%20Runner"
source_ids = ["ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "roof_runner", path = "json/archetypes_hunter.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/hunter" },
]
[[sources]]
publication = "ultimate-intrigue"
page = "65"

[fields]
kind = "archetype"
features = [
  { anchor = "skilled" },
  { anchor = "natural-leaper", level = 2 },
  { anchor = "shingle-stride", level = 5 },
  { anchor = "alley-ghost", level = 8 },
  { anchor = "master-climber", level = 20 },
]
trades = [
  { replaces = "Track", feature = "track", by = ["natural-leaper"] },
  { replaces = "Woodland stride", feature = "woodland-stride", by = ["shingle-stride"] },
  { replaces = "Swift tracker", feature = "swift-tracker", by = ["alley-ghost"] },
  { alters = "Master hunter", feature = "master-hunter", by = ["master-climber"] },
  { alters = "Class skills", by = ["skilled"] },
  { replaces = "The hunter's proficiency with medium armor and shields", by = ["skilled"] },
]
+++

Roof runners are skilled ambushers, skirmishers, and spies who eschew heavier types of armor in
order to remain light on their feet. They lurk in the shadows of the rooftops to find people or
houses to rob, though some use their specialized skills for nobler purposes.

## Skilled (Ex) {#skilled}

A roof runner adds Acrobatics, Escape Artist, and Sleight of Hand to her list of class skills.

This alters the hunter's class skills and replaces the hunter's proficiency with medium armor and
shields.

## Natural Leaper (Ex) {#natural-leaper}

At 2nd level, a roof runner adds [half](ref/misc/fractions-and-rounding) her hunter level on
Acrobatics checks to jump.

This ability replaces track.

## Shingle Stride (Ex) {#shingle-stride}

At 5th level, a roof runner and her animal companion can move at full speed without penalty when
using Acrobatics to cross narrow or uneven surfaces, and climb at half speed (instead of one-quarter
speed) without taking the -5 penalty.

This ability replaces woodland stride.

## Alley Ghost (Ex) {#alley-ghost}

At 8th level, a roof runner gains the benefits of the [fast stealth](ref/talent/fast-stealth) rogue
talent.

This ability replaces swift tracker.

## Master Climber (Ex) {#master-climber}

At 20th level, a roof runner gains a climb speed equal to her base land speed, instead of being able
to move at full speed while tracking.

This ability alters master hunter.
