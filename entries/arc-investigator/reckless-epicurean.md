+++
id = "ref/arc-investigator/reckless-epicurean"
kind = "archetype"
title = "Reckless Epicurean"
aon = "ArchetypeDisplay.aspx?FixedName=Investigator%20Reckless%20Epicurean"
source_ids = ["potions-and-poisons"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "reckless_epicurean", path = "json/archetypes_investigator.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/investigator" },
]
[[sources]]
publication = "potions-and-poisons"
page = "14"

[fields]
kind = "archetype"
features = [
  { anchor = "a-familiar-taste", level = 2 },
  { anchor = "experimental-potable", level = 5 },
  { anchor = "sympathetic-resistance", level = 13 },
]
trades = [
  { replaces = "Trapfinding", feature = "trapfinding", by = ["a-familiar-taste"] },
  { replaces = "Investigator talent gained at 5th level", feature = "investigator-talent", levels = [5], by = ["experimental-potable"] },
  { replaces = "Investigator talent gained at 13th level", feature = "investigator-talent", levels = [13], by = ["sympathetic-resistance"] },
  { alters = "Poison resistance", feature = "poison-resistance", levels = [2, 5, 8], by = ["a-familiar-taste"] },
  { alters = "poison immunity", feature = "poison-resistance", levels = [11], by = ["a-familiar-taste"] },
]
+++

Reckless epicureans are investigators who, for whatever reason, tend to test unknown concoctions on
themselves. Whether an obsessive scientist, a healer determined to ensure the safety of her
tinctures, or a seeker of new and interesting potions, a reckless epicurean's body is saturated with
experimental chemicals and magic. She can prepare extracts without formulae by approximating the
taste, and she can guzzle cursed concoctions without batting an eyelash.

## A Familiar Taste (Ex) {#a-familiar-taste}

At 2nd level, a reckless epicurean adds half her level as a bonus on Perception and Spellcraft
checks to identify potions. The benefits she receives from poison resistance and poison immunity
also apply against harmful potions and other ingested substances with negative effects, such as
drugs.

This replaces trapfinding.

## Experimental Potable (Su) {#experimental-potable}

At 5th level, once per day, a reckless epicurean can prepare one experimental potable using a
formula that she does not know from the alchemist formulae list into an extract slot of the
appropriate level. These experimental potables often have side effects. When a creature consumes one
of these potables, the investigator must succeed at a Spellcraft check (DC = 15 + the formula's
level). On a failure, she must roll on the [Wild Magic Surge table](ref/rule/wild-magic) to
determine the extra effects. If the wild magic surge effect isn't possible due to the nature of the
spell or effect, roll instead on the Universal Surge Effects table (_Pathfinder Unchained_ 148).
Results concerning the caster affect the drinker of the experimental potable instead.

At 8th level, and every 3 levels thereafter, the reckless epicurean can prepare one additional
experimental potable per day.

This replaces the investigator talent gained at 5th level.

## Sympathetic Resistance (Su) {#sympathetic-resistance}

At 13th level, when a reckless epicurean drinks an extract or a potion, she gains an alchemical
bonus on saves against spells and [spell-like abilities](ref/umr/spell-like-abilities) of the same
school as that potion or extract for a number of rounds equal to her Intelligence modifier. This
bonus is equal to the level of the spell contained in the extract or potion. The investigator can
use this ability a number of times per day equal to her Intelligence modifier (minimum 1).

This replaces the investigator talent gained at 13th level.
