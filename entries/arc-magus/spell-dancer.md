+++
id = "ref/arc-magus/spell-dancer"
kind = "archetype"
title = "Spell Dancer"
aon = "ArchetypeDisplay.aspx?FixedName=Magus%20Spell%20Dancer"
source_ids = ["advanced-race-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "spell_dancer", path = "json/archetypes_magus.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/magus" },
]
[[sources]]
publication = "advanced-race-guide"
page = "24"

[fields]
kind = "archetype"
features = [
  { anchor = "spell-dance", level = 1 },
  { anchor = "arcane-movement", level = 5 },
  { anchor = "dance-of-avoidance", level = 7 },
  { anchor = "greater-dance-of-avoidance", level = 13 },
]
trades = [
  { replaces = "The magus's ability to expend points from his arcane pool as a swift action to grant any weapon he is holding magic bonuses for 1 minute", by = ["spell-dance"] },
  { replaces = "Bonus feat a magus receives at 5th level", feature = "bonus-feats", levels = [5], by = ["arcane-movement"] },
  { replaces = "Medium armor", feature = "medium-armor", by = ["dance-of-avoidance"] },
  { replaces = "Heavy armor", feature = "heavy-armor", by = ["greater-dance-of-avoidance"] },
]
+++

The strong emphasis on wizards within elven culture influences how even non-wizard elves see
themselves. Many elven magi do not consider themselves masters of a blend of martial and magical
talents, but rather a sub-category of wizards who study the effect of physical movement and
techniques upon spellcasting ability. They believe their ability to cast spells while fighting is an
outgrowth of the concept of the "spell dance,"

which itself is just another kind of wizardry.

A spell dancer has the following class features.

## Class Skills {#class-skills}

A spell dancer adds Acrobatics and Perform (dance) to his list of class skills and removes
Intimidate and Ride from his list of class skills.

## Spell Dance (Su) {#spell-dance}

At 1st level, a spell dancer gains the ability to expend 1 point from his arcane pool as a swift
action to gain a +10 enhancement bonus to his movement rate and a +2 dodge bonus to Armor Class
against attacks of opportunity provoked by moving through threatened spaces for 1 minute. For every
four levels beyond 1st, the spell dancer gains another +10 enhancement bonus to movement and +2 to
AC against attacks of opportunity provoked from movement.

At 5th level, once per spell dance as a swift action, the spell dancer may use one of the following
on himself as a swift action: _[blur](ref/spell/blur), [fly](ref/spell/fly),_ or
_[haste](ref/spell/haste)_. These abilities last for 1 round. At 9th level, the spell dancer may
instead take a swift action to use _[dimension door](ref/spell/dimension-door)_ as a
[spell-like ability](ref/umr/spell-like-abilities) once during a spelldance. At 13th level, the
spell dancer may instead choose to take a swift action to gain
_[freedom of movement](ref/spell/freedom-of-movement)_ for 1d4 rounds.

This ability replaces the magus's ability to expend points from his arcane pool as a swift action to
grant any weapon he is holding magic bonuses for 1 minute.

## Arcane Movement (Su) {#arcane-movement}

At 5th level, whenever a spell dancer casts a magus spell, he gains a competence bonus on
Acrobatics, Climb, Escape Artist, and Stealth checks equal to the spell's level until the beginning
of his next turn. This ability replaces the bonus feat a magus receives at 5th level.

## Dance of Avoidance (Su) {#dance-of-avoidance}

At 7th level, while wearing light armor or no armor, a spell dancer gains a +2 insight bonus to
Armor Class. This ability replaces the medium armor class feature.

## Greater Dance of Avoidance (Su) {#greater-dance-of-avoidance}

At 13th level, while wearing light armor or no armor, a spell dancer's insight bonus to Armor Class
increases to +4. This ability replaces the heavy armor class feature.

## Magus Arcana {#magus-arcana}

The following magus arcana complement the spell dancer archetype:
[arcane cloak](ref/arcana/arcane-cloak), [prescient defense](ref/arcana/prescient-defense)
(_Ultimate Combat_); [close range](ref/arcana/close-range), [concentrate](ref/arcana/concentrate),
[hasted assault](ref/arcana/hasted-assault), [spell shield](ref/arcana/spell-shield) (_Ultimate
Magic_).
