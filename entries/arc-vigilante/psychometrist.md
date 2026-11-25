+++
id = "ref/arc-vigilante/psychometrist"
kind = "archetype"
title = "Psychometrist"
aon = "ArchetypeDisplay.aspx?FixedName=Vigilante%20Psychometrist"
source_ids = ["ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "psychometrist", path = "json/archetypes_vigilante.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/vigilante" },
]
[[sources]]
publication = "ultimate-intrigue"
page = "59"

[fields]
kind = "archetype"
features = [
  { anchor = "occult-awareness", level = 1 },
  { anchor = "implements-and-focus-powers", level = 2 },
  { anchor = "mental-focus", level = 2 },
  { anchor = "object-reading", level = 2 },
  { anchor = "psychometric-strike", level = 20 },
]
trades = [
  { replaces = "Social talent gained at 1st level", feature = "social-talent", levels = [1], by = ["occult-awareness"] },
  { replaces = "Vigilante talents gained at 2nd, 6th, 12th, and 18th levels", feature = "vigilante-talent", levels = [2, 6, 12, 18], by = ["implements-and-focus-powers"] },
  { replaces = "Unshakable", feature = "unshakable", by = ["object-reading"] },
  { alters = "Vengeance strike", feature = "vengeance-strike", by = ["psychometric-strike"] },
]
+++

Wise vigilantes know that there is power in certain seemingly unremarkable items. Psychometrists
aren't spellcasters; instead, they collect strange items or create their own uncanny gadgets that
seem to only work for them. Psychometrists often hide their clandestine activities behind the guise
of an eccentric peddler, curator, tinker, or artificer.

## Class Skills {#class-skills}

A psychometrist adds Knowledge (arcana) and Knowledge (history) to his list of class skills, instead
of Knowledge (dungeoneering) and Knowledge (engineering).

This alters the vigilante's class skills.

## Occult Awareness {#occult-awareness}

At 1st level, a psychometrist gains [Psychic Sensitivity](ref/feat/psychic-sensitivity) as a bonus
feat.

This ability replaces the social talent gained at 1st level.

## Implements and Focus Powers (Su) {#implements-and-focus-powers}

At 2nd level, a psychometrist learns to use the powers of one
[implement school](ref/ability/implements) from the [occultist](ref/class/occultist) class; the
conjuration implement school is not available to a psychometrist. This implement school does not
allow the psychometrist to cast any spells of that school of magic, though, and he can't use
spell-trigger or spell-completion magic items from any schools without succeeding at the appropriate
Use Magic Device check. A psychometrist can't select an implement school more than once.

The psychometrist treats his vigilante level as his occultist level for purposes of determining how
his implements' focus powers work, and for determining at what level he may choose certain focus
powers. Unlike an occultist, each of a psychometrist's focus powers has its own associated implement
or gadget. For example, a psychometrist might own a scabbard implement to use the legacy weapon
focus power and an implement that is a pair of boots to use the sudden speed focus power. The
psychometrist must assign mental focus separately to each implement each day, and he doesn't gain
resonant powers from his implements. Otherwise, this ability acts like the occultist's implements
class feature. At 6th, 12th, and 18th levels, the psychometrist learns to use one additional
implement school.

Each time a psychometrist learns an implement school, he learns the base focus power from that
school, plus one focus power from each implement school he has previously learned (but not from the
new school he just learned). The psychometrist can use focus powers only by expending mental focus
(see below). Unless otherwise noted, the DC for any saving throw against a focus power equals 10 +
1/2 the psychometrist's vigilante level + the psychometrist's Intelligence modifier. The
psychometrist can select a school he already knows, and in this case, he gains a total of two new
focus powers from that school (instead of learning the base focus power from the new school).

This replaces the vigilante talents gained at 2nd, 6th, 12th, and 18th levels.

## Mental Focus (Su) {#mental-focus}

At 2nd level, like an occultist, a psychometrist has mental focus he can invest into his implements
each day to allow him to utilize abilities tied to them. A psychometrist has a number of points of
mental focus equal to [half](ref/misc/fractions-and-rounding) his vigilante level plus his
Intelligence modifier.

## Object Reading (Su) {#object-reading}

At 2nd level, a psychometrist can read information from items he examines, and gains the occultist's
[object reading](ref/spell/object-reading) ability .

This ability replaces unshakable.

## Psychometric Strike (Su) {#psychometric-strike}

At 20th level, a psychometrist gains twice the usual benefits of vengeance strike (up to the same
maximum) against an opponent who possesses an object that once belonged to the psychometrist.

This ability alters vengeance strike.
