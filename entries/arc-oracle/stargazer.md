+++
id = "ref/arc-oracle/stargazer"
kind = "archetype"
title = "Stargazer"
aon = "ArchetypeDisplay.aspx?FixedName=Oracle%20Stargazer"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "stargazer", path = "json/archetypes_oracle.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/oracle" },
]
[[sources]]
publication = "ultimate-magic"
page = "59"

[fields]
kind = "archetype"
features = [
  { anchor = "guiding-star" },
  { anchor = "star-chart" },
]
trades = [
  { replaces = "Additional class skills from her mystery", feature = "mystery", power = "class skills" },
  { replaces = "Mystery bonus spells at these levels", feature = "mystery", levels = [2, 4, 6, 8, 18], power = "bonus spells" },
]
+++

Some oracles seek meaning in the pattern of the stars across the night sky, the trails of comets,
and the eternal orbits of the planets.

## Recommended Mysteries {#recommended-mysteries}

dark tapestry, heavens, lore, nature, time.

## Class Skills {#class-skills}

A stargazer adds Knowledge (nature), Perception, and Survival to her list of class skills. These
replace the additional class skills from her mystery.

## Bonus Spells {#bonus-spells}

_faerie fire_ (2nd), _glitterdust_ (4th), _guiding star_ (6th), _wandering star motes_ (8th),
_meteor swarm_ (18th). These bonus spells replace the oracle's mystery bonus spells at these levels.

## Revelations {#revelations}

A stargazer must take the following revelations at the listed levels.

## Guiding Star (Su) {#guiding-star}

As the [heavens](ref/mystery/heavens) mystery revelation (see page 48 of the _Advanced Player's
Guide_). You must take this revelation at 1st level.

## Star Chart (Ex) {#star-chart}

As the heavens mystery revelation (see page 48 of the _Advanced Player's Guide_). You must take this
revelation at 7th level.
