+++
id = "ref/arc-paladin/wilderness-warden"
kind = "archetype"
title = "Wilderness Warden"
source_ids = ["ultimate-wilderness"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "wilderness_warden", path = "json/archetypes_paladin.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/paladin" },
]

[fields]
kind = "archetype"
replaces = ["Divine grace", "Aura of courage", "3rd-, 9th-, and 15th-level mercies", "Aura of resolve", "Aura of justice"]
alters = ["Smite evil", "Spells"]
+++

**Sources:** Ultimate Wilderness pg 71\
Wilderness wardens are vigilant guardians of natural places of all kinds, from mountain peaks to
tangled thickets.

**Gained class skills:** climb, kg, kna, sur, swim

**Lost class skills:** diplo, heal, kno, spc

**Natural Defense (Su)**

**Ability:** Once per day, a wilderness warden can grant herself energy resistance 10 to cold,
electricity, or fire and a +2 insight bonus to her CMD for a number of minutes equal to her paladin
level.

**Gained:** At 2nd Level

**Replaces:** Divine grace

**Smite Evil (Su)**

**Alters:** Smite evil

**At 4th Level:** A wilderness warden gains this ability at 4th level, and it functions at her
paladin level - 3. She can expend a daily use of _smite evil_ to gain an additional daily use of
_natural defense._ She deals additional damage on her first successful attack when the target of her
_smite evil_ is an evil fey, humanoid (giant), magical beast, or monstrous humanoid, rather than an
evil dragon, outsider (evil), or undead.

**Aura of Comfort (Ex)**

**Gained:** At 3rd Level

**Passive:** A wilderness warden is comfortable in nearly any climate, as if she were affected by a
constant [endure elements](ref/spell/endure-elements) spell, and she and allies within 10 feet of
her gain a +4 bonus on Constitution checks and saving throws to resist fatigue; exhaustion; and the
effects of hunger, thirst, and hot or cold climates (including from magical effects).

**Replaces:** Aura of courage

**Favored Terrain (Ex)**

**Ability:** A wilderness warden selects a [favored terrain](ref/ability/favored-terrain), as per
the [ranger](ref/class/ranger) class feature.

**Gained:** At 3rd Level

**Repeat:** She selects an additional favored terrain, and the bonuses she gains in her previous
favored terrain(s) increase by 2., 9, 6

**Replaces:** 3rd-, 9th-, and 15th-level mercies

**Spells**

**Alters:** Spells

**Passive:** For each level of spell she can cast, a wilderness warden can prepare and cast one
spell per day from the druid spell list rather than the paladin spell list.

**Aura of Purity (Su)**

**Gained:** At 8th Level

**Passive:** A wilderness warden gains immunity to poison. Each ally within 10 feet gains a +2 bonus
on saving throws against disease and poison.

**Replaces:** Aura of resolve

**Natural Shield (Su)**

**Ability:** A wilderness warden can expend two daily uses of her _natural defense_ ability to grant
the benefits of that ability to all nonevil allies within 10 feet for 1 minute.

**Gained:** At 11th Level

**Replaces:** Aura of justice
