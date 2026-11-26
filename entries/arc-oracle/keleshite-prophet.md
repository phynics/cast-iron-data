+++
id = "ref/arc-oracle/keleshite-prophet"
kind = "archetype"
title = "Keleshite Prophet"
aon = "ArchetypeDisplay.aspx?FixedName=Oracle%20Keleshite%20Prophet"
source_ids = ["inner-sea-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "keleshite_prophet", path = "json/archetypes_oracle.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/oracle" },
]
[[sources]]
publication = "inner-sea-intrigue"
page = "42"

[fields]
kind = "archetype"
features = [
  { anchor = "divining-dance" },
]
trades = [
  { replaces = "Additional skills gained from the oracle's mystery", feature = "mystery", power = "class skills" },
  { replaces = "Bonus spells at those levels gained from the oracle's mystery", feature = "mystery", levels = [6, 10, 12, 16, 18], power = "bonus spells" },
]
+++

Keleshite prophets help guide and serve the vast Padishah Empire of Kelesh and its interests across
Golarion.

## Recommended Mysteries {#recommended-mysteries}

Any.

## Class Skills {#class-skills}

A Keleshite prophet adds Perception, Perform (dance), and all Knowledge skills to her list of class
skills.

These replace the additional skills gained from the oracle's mystery.

## Bonus Spells {#bonus-spells}

A Keleshite prophet gains the following bonus spells: _clairaudience/clairvoyance_ (6th), _prying
eyes_ (10th), _true seeing_ (12th), _prediction of failure_ (16th), _foresight_ (18th).

These replace the bonus spells at those levels gained from the oracle's mystery.

## Revelations {#revelations}

A Keleshite prophet must take the following revelation at 1st level.

## Divining Dance (Su) {#divining-dance}

Once per day, you can perform a sacred meditative dance that gives you great clarity of mind and
prepares you for what lies ahead. This dance must last for at least 1 minute, uninterrupted, and you
can take no other actions during the dance.

When you dance, attempt a Perform (dance) check; the results of the check determine the benefits you
gain for the next 24 hours, as listed below. You can always choose the benefit from a lower result,
if you wish (for example, if your Perform \[dance\] result is 15, you can choose to gain a +1 bonus
on your divinations' saving throws instead of choosing to use _[augury](ref/spell/augury)_ once as a
[spell-like ability](ref/umr/spell-like-abilities)). Perform (Dance) Result Benefit 0–9 Increase the
saving throw DC of any [divination](ref/spell/divination) spells you cast by 1. 10–19 Once in the
next 24 hours, as an immediate action, you can use _[augury](ref/spell/augury)_ as a
[spell-like ability](ref/umr/spell-like-abilities), using your oracle level as your caster level.
20–29 Once in the next 24 hours, you can use _divination_ as a
[spell-like ability](ref/umr/spell-like-abilities), using your oracle level as your caster level. If
you are at least 8th level, you can cast it in 1 minute instead of 10 minutes. 30–39 Once in the
next 24 hours, you can use _[commune](ref/spell/commune)_ as a
[spell-like ability](ref/umr/spell-like-abilities), using your oracle level as your caster level. If
you are at least 10th level, its casting time is in 1 minute instead of 10 minutes. 40+ Once in the
next 24 hours, you can use _[contact other plane](ref/spell/contact-other-plane)_ as a
[spell-like ability](ref/umr/spell-like-abilities), using your oracle level as your caster level.
