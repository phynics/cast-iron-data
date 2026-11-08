+++
id = "ref/arc-skald/wyrm-singer"
kind = "archetype"
title = "Wyrm Singer"
source_ids = ["legacy-of-dragons"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "wyrm_singer", path = "json/archetypes_skald.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/skald" },
]

[fields]
kind = "archetype"
replaces = ["Inspired rage", "Song of the fallen", "Rage power gained at 12th level"]
+++

**Sources:** Legacy of Dragons pg 14\
Wyrm singers spin fragments of the story of the ongoing struggle between noble Apsu and wicked
Dahak.

**Wyrm Song (Su)**

**Info:** A wyrm singer gains the following _raging songs._

**Draconic Rage (Su)**

**Ability:** A wyrm singer can kindle an echo of ancient rage felt between warring dragon clans in
his allies. This ability acts as _inspired rage,_ except instead of _inspire rage's_ normal bonuses,
those affected gain a morale bonus on melee attack and damage rolls equal to 2 +
[one-eighth](ref/misc/fractions-and-rounding) of his skald level. Those affected also gain a morale
bonus on saving throws against paralysis and sleep effects equal to 2 + one-fourth of his skald
level. They still take a -1 penalty to their AC.

**Gained:** At 1st Level

**Replaces:** Inspired rage

**Wyrm Saga (Su)**

**Ability:** A wyrm singer embraces the essence of the draconic histories, allowing his allies to
manifest aspects of a dragon in their physical forms. The wyrm singer selects a single ally within
60 feet to take on a draconic aspect (as per [form of the dragon I](ref/spell/form-of-the-dragon-1))
of a type of the wyrm singer's choice. The ally cannot use the breath weapon attack provided by
_form of the dragon._ The wyrm singer must expend 1 round of _raging song_ each round to maintain
wyrm saga, and can affect only a single ally at a time.

**Gained:** At 14th Level

**Replaces:** Song of the fallen

**Breath Weapon (Su)**

**Gained:** At 12th Level

**Replaces:** Rage power gained at 12th level

**Swift:** Once per day, a wyrm singer can grant a breath weapon attack to himself or an ally
affected by his draconic rage _raging song._ Using the breath weapon is a **standard action**, and
it affects creatures in a 30-foot cone or a 60-foot line. The breath weapons deals 1d6 points of
damage per 2 skald levels the wyrm singer has, and is of an energy type of the wyrm singer's choice
(acid, cold, electricity, or fire). Creatures caught in the area can attempt a Reflex save (DC =
10 + 1/2 the wyrm singer's skald level + his Charisma modifier) to halve the damage.
