+++
id = "ref/arc-cleric/evangelist"
kind = "archetype"
title = "Evangelist"
aon = "ArchetypeDisplay.aspx?FixedName=Cleric%20Evangelist"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "evangelist", path = "json/archetypes_cleric.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/cleric" },
]
[[sources]]
publication = "ultimate-combat"
page = "40"

[fields]
kind = "archetype"
features = [
  { anchor = "single-minded" },
  { anchor = "public-speaker" },
  { anchor = "sermonic-performance", level = 1 },
  { anchor = "spontaneous-casting", level = 1 },
]
trades = [
  { replaces = "The 1st-, 9th-, and 15th-level channel energy abilities", feature = "channel-energy", levels = [1, 9, 15], by = ["sermonic-performance"] },
  { alters = "Spontaneous casting", feature = "spontaneous-casting", by = ["spontaneous-casting"] },
]
+++

The evangelist is the voice of her religion in the world. Where others nurture the faith among
believers, an evangelist proclaims the coming glory of her deific patron and issues the clarion call
to all around to heed the truth, or obey the call to war and crusade against the enemies of the
church.

## Single-Minded {#single-minded}

An evangelist focuses her skills and learning on proclamation rather than the fine details of the
church's deeper mysteries or martial training. Thus, she may select only one domain and does not
gain Medium Armor Proficiency or Shield Proficiency.

## Public Speaker {#public-speaker}

An evangelist gains [Perform](ref/skill/perform-any) as a class skill. In addition, she is trained
to project her voice with great skill and effect; the DC to hear her speak in difficult conditions
is reduced by an amount equal to her class level plus her Charisma modifier (minimum 0).

## Sermonic Performance {#sermonic-performance}

An evangelist gains the ability to deliver a select number of supernatural and spell-like
performances through the force and power of her divinely inspired preaching and exhortation. This
ability is similar in all respects to bardic performance as used by a bard of the same level
(including interactions with feats, spells, and prestige classes), using Perform (oratory) as the
evangelist's performance skill. However, an evangelist gains only the following types of bardic
performance: [countersong](ref/performance/countersong), [fascinate](ref/performance/fascinate), and
[inspire courage](ref/performance/inspire-courage) at 1st level;
[inspire greatness](ref/performance/inspire-greatness) at 9th level; and
[inspire heroics](ref/performance/inspire-heroics) at 15th level. Sermonic performance replaces the
1st-, 9th-, and 15th-level channel energy abilities. This caps the cleric's channel energy damage at
7d6 points.

## Spontaneous Casting {#spontaneous-casting}

An evangelist does not gain the ability to spontaneously cast _cure_ or _inflict_ spells by
sacrificing prepared spells. However, an evangelist can spontaneously cast the following spells by
sacrificing a prepared spell of the noted level or above:

|Spell level|Spontaneous spell|
| --- | --- |
|1st level|_command_|
|2nd level|_enthrall_|
|3rd level|_tongues_|
|4th level|_suggestion_|
|5th level|_greater command_|
|6th level|_geas/quest_|
|7th level|_mass suggestion_|
|8th level|_sympathy_|
|9th level|_demand_|
