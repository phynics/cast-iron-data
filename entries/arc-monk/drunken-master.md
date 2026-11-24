+++
id = "ref/arc-monk/drunken-master"
kind = "archetype"
title = "Drunken Master"
aon = "ArchetypeDisplay.aspx?FixedName=Monk%20Drunken%20Master"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "drunken_master", path = "json/archetypes_monk.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/monk" },
]
[[sources]]
publication = "advanced-players-guide"
page = "110"

[fields]
kind = "archetype"
features = [
  { anchor = "drunken-ki", level = 3 },
  { anchor = "drunken-strength", level = 5 },
  { anchor = "drunken-courage", level = 11 },
  { anchor = "drunken-resilience", level = 13 },
  { anchor = "firewater-breath", level = 19 },
]
trades = [
  { replaces = "Still mind", feature = "still-mind", by = ["drunken-ki"] },
  { replaces = "Purity of body", feature = "purity-of-body", by = ["drunken-strength"] },
  { replaces = "Diamond body", feature = "diamond-body", by = ["drunken-courage"] },
  { replaces = "Diamond soul", feature = "diamond-soul", by = ["drunken-resilience"] },
  { replaces = "Empty body", feature = "empty-body", by = ["firewater-breath"] },
]
+++

Most monks lead lives of moderation and quiet contemplation. But the drunken master finds perfection
through excess. Powered by strong wine, he uses his intoxication to reach a state where his ki is
more potent, if somewhat fleeting. A drunken master has the following class features.

## Drunken Ki (Su) {#drunken-ki}

At 3rd level, a drunken master can drink a tankard of ale or strong alcohol and gain one temporary
_ki_ point. The act of drinking is a standard action that does not provoke attacks of opportunity.
The monk can have a maximum number of drunken _ki_ points equal to 1 plus one additional point for
every two levels thereafter (5th, 7th, and so on). The monk can gain this temporary _ki_ even before
he gains a _ki_ pool at 4th level. These drunken _ki_ points last for 1 hour or until spent,
whichever is shorter. As long as he has at least 1 drunken _ki_ point, the monk can spend 1 _ki_
point as a swift action to move 5 feet without provoking attacks of opportunity. This ability
replaces still mind.

## Drunken Strength (Su) {#drunken-strength}

At 5th level, a drunken master can spend 1 point of _ki_ as a swift action to inflict 1d6 extra
points of damage on a single successful melee attack. The monk can choose to apply the damage after
the attack roll is made. At 10th level, the monk may spend 2 drunken _ki_ points to increase the
extra damage to 2d6. At 15th level, the monk may spend 3 drunken _ki_ points to increase the extra
damage to 3d6. At 20th level, the monk may spend 4 drunken _ki_ points to increase the extra damage
to 4d6. The monk must have at least 1 drunken _ki_ point to use this ability. This ability replaces
purity of body.

## Drunken Courage (Su) {#drunken-courage}

At 11th level, a drunken master is immune to fear as long as he has at least 1 point of drunken
_ki_. This ability replaces diamond body.

## Drunken Resilience (Ex) {#drunken-resilience}

At 13th level, a drunken master gains [DR](ref/rule/damage-reduction) 1/— as long as he has at least
1 point of drunken _ki_. At 16th level, the DR increases to 2/—. At 19th level, it increases to 3/—.
This ability replaces diamond soul.

## Firewater Breath (Su) {#firewater-breath}

At 19th level, a drunken master can take a drink and expel a gout of alcohol-fueled fire in a
30-foot cone. Creatures within the cone take 20d6 points of fire damage. A successful Reflex saving
throw (DC 10 + 1/2 the monk's level + the monk's Wis modifier) halves the damage. Using this ability
is a standard action that consumes 4 _ki_ points from the monk's _ki_ pool. The monk must have at
least 1 drunken _ki_ point to use this ability. This ability replaces empty body.
