+++
id = "ref/arc-cleric/scroll-scholar"
kind = "archetype"
title = "Scroll Scholar"
aon = "ArchetypeDisplay.aspx?FixedName=Cleric%20Scroll%20Scholar"
source_ids = ["pathfinder-society-field-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "scroll_scholar", path = "json/archetypes_cleric.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/cleric" },
]
[[sources]]
publication = "pathfinder-society-field-guide"
page = "26"

[fields]
kind = "archetype"
features = [
  { anchor = "diligent-student", level = 1 },
  { anchor = "secrets-revealed", level = 5 },
  { anchor = "flash-of-insight", level = 10 },
]
trades = [
  { replaces = "One of the 1st-level granted powers from her domains - the character gets to choose which of her two 1st-level granted powers it replaces", feature = "domains", levels = [1], power = "domain power", by = ["diligent-student"] },
  { replaces = "Channel energy damage boost at 5th level", feature = "channel-energy", levels = [5], by = ["secrets-revealed"] },
  { replaces = "The normal addition of a new 4th-level spell slot to the character's spells per day—from this point on, the cleric or wizard has one fewer 4th-level spell slot than other clerics or wizards", by = ["flash-of-insight"] },
]
+++

A scroll scholar values knowledge and learning as much as her other abilities, trading a portion of
her potential in her chosen class for greater breadth of skill at deciphering old texts, piecing
together strange fragments of esoteric lore, and deciphering the hidden qualities of strange and
unusual magical items. The scroll scholar archetype can be taken by either clerics or wizards—they
give up [different class abilities](ref/arc-wizard/scroll-scholar) for the new abilities granted by
this archetype. A wizard must either be a universalist wizard or a diviner wizard in order to take
this archetype—other types of school specializations are not suited to this archetype's focus. A
scroll scholar has the following class features.

## Diligent Student (Ex) {#diligent-student}

At 1st level, a scroll scholar chooses one [Knowledge](ref/skill/knowledge-all) skill. This becomes
a class skill if it is not already one. The scroll scholar adds
[half](ref/misc/fractions-and-rounding) her class level to all Knowledge checks of this type
(minimum 1). At 5th level and every five levels thereafter, a scroll scholar chooses 1 additional
Knowledge skill to receive this bonus. For clerics, this ability replaces one of the 1st-level
granted powers from her domains—the character gets to choose which of her two 1st-level granted
powers it replaces. For wizards, this ability replaces diviner's fortune (if a diviner) or hand of
the apprentice (if a universalist).

## Secrets Revealed (Sp) {#secrets-revealed}

At 5th level, a scroll scholar gains the ability to cast
_[comprehend languages](ref/spell/comprehend-languages)_ and _[identify](ref/spell/identify)_ as
[spell-like abilities](ref/umr/spell-like-abilities). Her caster level is equal to her character
level in whatever class she took the scroll scholar archetype for. She can cast these spells once
per day each at 5th level, twice per day each at 7th level, and three times per day each at 9th
level. At 11th level, one of these [spell-like abilities](ref/umr/spell-like-abilities) (scholar's
choice) becomes a constant [spell-like ability](ref/umr/spell-like-abilities), and at 13th level,
the second one becomes a constant spell-like ability. If the scholar is a cleric, this ability
replaces the increase to her channel energy damage normally gained at 5th level—her channel energy
damage increases to 3d6 at 7th level instead, and for the rest of her career as a cleric lags 1d6
behind normal. If the scholar is a wizard, this ability replaces her bonus feat for 5th level.

## Flash of Insight (Su) {#flash-of-insight}

At 10th level, once per day, a scroll scholar can gain a +5 bonus on a single attack roll, caster
level check, or saving throw as an immediate action. This decision must be made before the results
of the roll are known, but can be made after the die is rolled. This ability can be used twice per
day at 15th level, and 3 times per day at 20th level. This ability replaces the normal addition of a
new 4th-level spell slot to the character's spells per day—from this point on, the cleric or wizard
has one fewer 4th-level spell slot than other clerics or wizards.
