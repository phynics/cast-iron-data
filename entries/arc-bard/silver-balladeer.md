+++
id = "ref/arc-bard/silver-balladeer"
kind = "archetype"
title = "Silver Balladeer"
aon = "ArchetypeDisplay.aspx?FixedName=Bard%20Silver%20Balladeer"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "silver_balladeer", path = "json/archetypes_bard2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/bard" },
]
[[sources]]
publication = "occult-adventures"
page = "115"

[fields]
kind = "archetype"
features = [
  { anchor = "bardic-performance" },
  { anchor = "break-curse", level = 6 },
  { anchor = "holy-vibration", level = 9 },
  { anchor = "mass-break-curse", level = 18 },
  { anchor = "pure-heart", level = 2 },
  { anchor = "silver-mastery", level = 2 },
]
trades = [
  { replaces = "Suggestion", feature = "bardic-performance", power = "suggestion", by = ["break-curse"] },
  { replaces = "Inspire greatness", feature = "bardic-performance", power = "inspire greatness", by = ["holy-vibration"] },
  { replaces = "Mass suggestion", feature = "bardic-performance", power = "mass suggestion", by = ["mass-break-curse"] },
  { replaces = "Well-versed", feature = "well-versed", by = ["pure-heart"] },
  { replaces = "The 2nd-level versatile performance", feature = "versatile-performance", levels = [2], by = ["silver-mastery"] },
  { alters = "Alignment" },
]
+++

The bright purity of silver makes beautiful music, and its vibrations are also anathema to unnatural
creatures. Some bards use a mixture of silver-stringed instruments and esoteric knowledge to battle
the dark forces of the world.

## Alignment {#alignment}

A silver balladeer must have a good alignment. This ability alters alignment.

## Bardic Performance {#bardic-performance}

A silver balladeer gains the bardic performances listed below. These bardic performances all require
the use of a silver or silver-stringed instrument, which costs twice as much as a normal
[masterwork instrument](ref/eq-misc/musical-instrument-masterwork).

## Break Curse (Su) {#break-curse}

At 6th level, a silver balladeer can suppress a single curse affecting an ally within 30 feet that
is able to see and hear her. Each round the silver balladeer uses break curse, she attempts a
Perform check against the original DC of the curse. If successful, she suppresses the curse for 1
round. After she has suppressed the curse for 4 consecutive rounds, she can attempt a caster level
check to remove the curse as if she had cast _[remove curse](ref/spell/remove-curse)_. This ability
replaces suggestion.

## Holy Vibration (Su) {#holy-vibration}

At 9th level, a silver balladeer can spend a round of bardic performance to make a single door or a
window within 30 feet resonate with a holy vibration. Undead and creatures with the evil subtype are
unable to open a door or window affected in this way (as _[arcane lock](ref/spell/arcane-lock)_) for
10 minutes per bard level. If such a creature has the incorporeal subtype, it is unable to move
through the affected door or window, or through any walls, floors, or ceilings within 20 feet of it.
Incorporeal creatures can attempt Charisma checks to break through areas warded by holy vibration,
using the same break DC as for the object the creature is trying to move through. This ability
replaces inspire greatness.

## Mass Break Curse (Su) {#mass-break-curse}

At 18th level, a silver balladeer can suppress all curses among any number of allies within 30 feet
when using break curse. Every 4 consecutive rounds of using this performance, the silver balladeer
can attempt a caster level check to remove a single curse on a single ally affected by this
performance, as if she had cast _[remove curse](ref/spell/remove-curse)_. This ability replaces mass
suggestion.

## Pure Heart (Ex) {#pure-heart}

At 2nd level, a silver balladeer gains a +4 bonus on saving throws against curses, hexes, and charm
effects. This ability replaces well-versed.

## Silver Mastery (Su) {#silver-mastery}

At 2nd level, a silver balladeer treats silver weapons as if they were also
[cold iron](ref/eq-material/cold-iron) for the purpose of overcoming
[damage reduction](ref/rule/damage-reduction). Also,
[alchemical silver](ref/eq-material/alchemical-silver) weapons do not impose a penalty on damage
rolls when wielded by a silver balladeer, and a silver balladeer gains a +1 bonus on attack rolls
made with [mithral](ref/eq-material/mithral) weapons. This ability replaces the 2nd-level versatile
performance.
