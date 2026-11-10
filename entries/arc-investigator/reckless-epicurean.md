+++
id = "ref/arc-investigator/reckless-epicurean"
kind = "archetype"
title = "Reckless Epicurean"
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
replaces = ["Trapfinding", "Investigator talent gained at 5th level", "Investigator talent gained at 13th level"]
alters = ["Poison resistance", "poison immunity"]
replaces_features = ["trapfinding"]
alters_features = ["poison-resistance"]
+++

Reckless epicureans are investigators who, for whatever reason, tend to test unknown concoctions on
themselves. Whether an obsessive scientist, a healer determined to ensure the safety of her
tinctures, or a seeker of new and interesting potions, a reckless epicurean's body is saturated with
experimental chemicals and magic. She can prepare extracts without formulae by approximating the
taste, and she can guzzle cursed concoctions without batting an eyelash.

**A Familiar Taste (Ex)**

**Alters:** Poison resistance, poison immunity

**Gained:** At 2nd Level

**Passive:** A reckless epicurean adds half her level as a bonus on Perception and Spellcraft checks
to identify potions. The benefits she receives from _poison resistance_ and _poison immunity_ also
apply against harmful potions and other ingested substances with negative effects, such as drugs.

**Replaces:** Trapfinding

**Experimental Potable (Su)**

**Ability:** A reckless epicurean can prepare one _experimental potable_ using a formula that she
does not know from the alchemist formulae list into an extract slot of the appropriate level. These
_experimental potables_ often have side effects. When a creature consumes one of these potables, the
investigator must succeed at a Spellcraft check (DC = 15 + the formula's level). On a failure, she
must roll on the [Wild Magic Surge table](ref/rule/wild-magic) to determine the extra effects. If
the wild magic surge effect isn't possible due to the nature of the spell or effect, roll instead on
the Universal Surge Effects table. Results concerning the caster affect the drinker of the
_experimental potable_ instead.

**Gained:** At 5th Level

**Replaces:** Investigator talent gained at 5th level

At 8th level: She can now prepare 2 _experimental potables_ per day.

At 11th level: She can now create 3 _experimental potables_ per day.

At 14th level: She can now prepare 4 _experimental potables_ per day.

At 17th level: She can now create 5 _experimental potables_ per day.

At 20th level: She can now prepare 6 _experimental potables_ per day.

**Sympathetic Resistance (Su)**

**Gained:** At 13th Level

**Passive:** When a reckless epicurean drinks an extract or a potion, she gains an alchemical bonus
on saves against spells and [spell-like abilities](ref/umr/spell-like-abilities) of the same school
as that potion or extract for a number of rounds equal to her Intelligence modifier. This bonus is
equal to the level of the spell contained in the extract or potion.

**Replaces:** Investigator talent gained at 13th level

**Usage:** Intelligence modifier times/day
