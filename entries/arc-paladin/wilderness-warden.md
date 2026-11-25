+++
id = "ref/arc-paladin/wilderness-warden"
kind = "archetype"
title = "Wilderness Warden"
aon = "ArchetypeDisplay.aspx?FixedName=Paladin%20Wilderness%20Warden"
source_ids = ["ultimate-wilderness"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "wilderness_warden", path = "json/archetypes_paladin.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/paladin" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "71"

[fields]
kind = "archetype"
features = [
  { anchor = "natural-defense", level = 2 },
  { anchor = "smite-evil", level = 4 },
  { anchor = "aura-of-comfort", level = 3 },
  { anchor = "favored-terrain", level = 3 },
  { anchor = "spells" },
  { anchor = "aura-of-purity", level = 8 },
  { anchor = "natural-shield", level = 11 },
]
trades = [
  { replaces = "Divine grace", feature = "divine-grace", by = ["natural-defense"] },
  { replaces = "Aura of courage", feature = "aura-of-courage", by = ["aura-of-comfort"] },
  { replaces = "Mercies gained at 3rd level, 9th level, and 15th level", feature = "mercy", levels = [3, 9, 15], by = ["favored-terrain"] },
  { replaces = "Aura of resolve", feature = "aura-of-resolve", by = ["aura-of-purity"] },
  { replaces = "Aura of justice", feature = "aura-of-justice", by = ["natural-shield"] },
  { alters = "Smite evil", feature = "smite-evil", by = ["smite-evil"] },
  { alters = "Spells", feature = "spells", by = ["spells"] },
]
+++

Wilderness wardens are vigilant guardians of natural places of all kinds, from mountain peaks to
tangled thickets.

## Class Skills {#class-skills}

A wilderness warden gains Climb, Knowledge (geography), Knowledge (nature), Survival, and Swim as
class skills. She does not gain Diplomacy, Heal, Knowledge (nobility), or Spellcraft as class
skills.

This alters the paladin's class skills.

## Natural Defense (Su) {#natural-defense}

At 2nd level, once per day, a wilderness warden can grant herself energy resistance 10 to cold,
electricity, or fire and a +2 insight bonus to her CMD for a number of minutes equal to her paladin
level. The energy resistance increases by 5 and the CMD bonus increases by 1 at 5th level and every
5 levels thereafter.

This replaces divine grace.

## Smite Evil (Su) {#smite-evil}

A wilderness warden gains this ability at 4th level, and it functions at her paladin level - 3. She
can expend a daily use of smite evil to gain an additional daily use of natural defense. She deals
additional damage on her first successful attack when the target of her smite evil is an evil fey,
humanoid (giant), magical beast, or monstrous humanoid, rather than an evil dragon, outsider (evil),
or undead.

This alters smite evil.

## Aura of Comfort (Ex) {#aura-of-comfort}

At 3rd level, a wilderness warden is comfortable in nearly any climate, as if she were affected by a
constant _[endure elements](ref/spell/endure-elements)_ spell, and she and allies within 10 feet of
her gain a +4 bonus on Constitution checks and saving throws to resist fatigue; exhaustion; and the
effects of hunger, thirst, and hot or cold climates (including from magical effects).

This replaces aura of courage.

## Favored Terrain (Ex) {#favored-terrain}

At 3rd level, a wilderness warden selects a [favored terrain](ref/ability/favored-terrain), as per
the [ranger](ref/class/ranger) class feature. Every 6 levels after 3rd, she selects an additional
favored terrain; each time she does so, the bonuses she gains in her previous favored terrain or
terrains increase by 2.

This replaces the mercies gained at 3rd level , 9th level, and 15th level.

## Spells {#spells}

For each level of spell she can cast, a wilderness warden can prepare and cast one spell per day
from the druid spell list rather than the paladin spell list.

This alters the paladin's spells.

## Aura of Purity (Su) {#aura-of-purity}

At 8th level, a wilderness warden gains immunity to poison. Each ally within 10 feet gains a +2
bonus on saving throws against disease and poison.

This replaces aura of resolve.

## Natural Shield (Su) {#natural-shield}

At 11th level, a wilderness warden can expend two daily uses of her natural defense ability to grant
the benefits of that ability to all nonevil allies within 10 feet for 1 minute.

This replaces aura of justice.
