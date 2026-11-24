+++
id = "ref/arc-barbarian/invulnerable-rager"
kind = "archetype"
title = "Invulnerable Rager"
aon = "ArchetypeDisplay.aspx?FixedName=Barbarian%20Invulnerable%20Rager"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "invulnerable_rager", path = "json/archetypes_barbarian.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/barbarian" },
]
[[sources]]
publication = "advanced-players-guide"
page = "79"

[fields]
kind = "archetype"
features = [
  { anchor = "invulnerability", level = 2 },
  { anchor = "extreme-endurance", level = 3 },
]
trades = [
  { replaces = "Uncanny dodge", feature = "uncanny-dodge", by = ["invulnerability"] },
  { replaces = "improved uncanny dodge", feature = "improved-uncanny-dodge", by = ["invulnerability"] },
  { replaces = "damage reduction", feature = "damage-reduction", by = ["invulnerability"] },
  { replaces = "Trap sense", feature = "trap-sense", by = ["extreme-endurance"] },
]
+++

Some barbarians learn to take whatever comes their way, shrugging off mortal wounds with ease. These
barbarians invite their enemies to attack them, and use pain to fuel their rage. An invulnerable
rager has the following class features.

## Invulnerability (Ex) {#invulnerability}

At 2nd level, the invulnerable rager gains [DR](ref/rule/damage-reduction)/— equal to
[half](ref/misc/fractions-and-rounding) her barbarian level. This
[damage reduction](ref/rule/damage-reduction) is doubled against nonlethal damage. This ability
replaces uncanny dodge, improved uncanny dodge, and damage reduction.

## Extreme Endurance (Ex) {#extreme-endurance}

At 3rd level, the invulnerable rager is inured to either hot or cold climate effects (choose one) as
if using _[endure elements](ref/spell/endure-elements)_. In addition, the barbarian gains 1 point of
fire or cold [resistance](ref/umr/resistance) for every three levels beyond 3rd. This ability
replaces trap sense.

## Rage Powers {#rage-powers}

The following rage powers complement the invulnerable rager archetype:
[come and get me](ref/ragepower/come-and-get-me), [guarded life](ref/ragepower/guarded-life),
[increased damage reduction](ref/ragepower/increased-damage-reduction)\*,
[inspire ferocity](ref/ragepower/inspire-ferocity),
[reckless abandon](ref/ragepower/reckless-abandon), and
[renewed vigor](ref/ragepower/renewed-vigor)\*.
