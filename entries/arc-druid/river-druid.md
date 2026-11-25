+++
id = "ref/arc-druid/river-druid"
kind = "archetype"
title = "River Druid"
aon = "ArchetypeDisplay.aspx?FixedName=Druid%20River%20Druid"
source_ids = ["ultimate-wilderness", "people-of-the-river"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "river_druid", path = "json/archetypes_druid2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/druid" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "48"
[[sources]]
publication = "people-of-the-river"
page = "14"

[fields]
kind = "archetype"
features = [
  { anchor = "ferrier", level = 1 },
  { anchor = "read-the-currents", level = 2 },
  { anchor = "countercurrent", level = 3 },
  { anchor = "deep-breath", level = 4 },
  { anchor = "wild-shape", level = 6 },
  { anchor = "tongue-of-the-sun-and-moon", level = 15 },
]
trades = [
  { replaces = "Nature sense", feature = "nature-sense", by = ["ferrier"] },
  { replaces = "Woodland stride", feature = "woodland-stride", by = ["read-the-currents"] },
  { replaces = "Trackless step", feature = "trackless-step", by = ["countercurrent"] },
  { replaces = "Resist nature's lure", feature = "resist-nature-s-lure", by = ["deep-breath"] },
  { replaces = "Timeless body", feature = "timeless-body", by = ["tongue-of-the-sun-and-moon"] },
  { alters = "Class skills", by = ["ferrier"] },
  { alters = "Wild shape", feature = "wild-shape", by = ["wild-shape"] },
]
+++

These druids are the guardians of rivers and the creatures that depend on them. Just as rivers pour
from mountains to seas, river druids adapt to many environments and cultures. They can be found
wherever water flows, even among underground rivers or sewer systems.

## Ferrier (Ex) {#ferrier}

A river druid adds [Diplomacy](ref/skill/diplomacy) to her list of class skills and gains a +2 bonus
on Diplomacy and Knowledge (nature) skill checks.

This alters the druid's class skills and replaces nature sense.

## Read the Currents (Ex) {#read-the-currents}

At 2nd level, a river druid gains a bonus equal to [half](ref/misc/fractions-and-rounding) her druid
level on initiative checks and Acrobatics, Knowledge (geography), Perception, Stealth, Survival, and
Swim checks when she is in, on, or adjacent to flowing water.

This replaces woodland stride.

## Countercurrent (Ex) {#countercurrent}

At 3rd level, a river druid takes no penalty to speed or on Acrobatics or Stealth checks in shallow
water up to 2 feet deep (1 foot deep for Small characters) such as shallow bogs, shorelines,
streams, and partially flooded areas. A river druid (and any vehicle she pilots) isn't moved by
flowing water unless she allows it. Water that has been magically manipulated to impede or boost
motion still affects her.

This replaces trackless step.

## Deep Breath (Ex) {#deep-breath}

At 4th level, a river druid can [hold her breath](ref/misc/hold-your-breath) for a number of minutes
equal to her Constitution score (after this, she must begin attempting Constitution checks to avoid
suffocation as normal).

This replaces resist nature's lure.

## Wild Shape (Su) {#wild-shape}

A river druid gains this ability at 6th level, except her effective druid level for the ability is
equal to her druid level - 2.

This alters wild shape.

## Tongue of the Sun and Moon (Ex) {#tongue-of-the-sun-and-moon}

At 15th level, a river druid can speak with any living creature.

This replaces timeless body.
