+++
id = "ref/arc-bard/dwarven-scholar"
kind = "archetype"
title = "Dwarven Scholar"
aon = "ArchetypeDisplay.aspx?FixedName=Bard%20Dwarven%20Scholar"
source_ids = ["blood-of-the-ancients"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "dwarven_scholar", path = "json/archetypes_bard.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/bard" },
]
[[sources]]
publication = "blood-of-the-ancients"
page = "30"

[fields]
kind = "archetype"
features = [
  { anchor = "studied-insight" },
  { anchor = "dwarven-training", level = 2 },
  { anchor = "bardic-performance" },
  { anchor = "war-chant", level = 1 },
]
trades = [
  { replaces = "Versatile performance", feature = "versatile-performance", by = ["dwarven-training"] },
  { replaces = "Inspire courage", feature = "bardic-performance", power = "inspire courage", by = ["war-chant"] },
  { replaces = "suggestion", feature = "bardic-performance", power = "suggestion", by = ["war-chant"] },
  { alters = "Weapon and armor proficiency", feature = "weapon-and-armor-proficiencies" },
]
+++

A dwarven scholar researches the lineage of the kings of the old dwarven empires and learns their
ancient tactics. She keeps these ancient traditions alive by sharing them with her allies.

## Weapon and Armor Proficiency {#weapon-and-armor-proficiency}

A dwarven scholar is proficient with one weapon of her choosing with the word "dwarven" in its name,
in addition to her normal weapon proficiencies. She is not proficient with shields.

This alters the bard's weapon and armor proficiency.

## Studied Insight (Ex) {#studied-insight}

A dwarven scholar uses her Wisdom modifier instead of her Charisma modifier to determine all class
features and effects relating to her bard class, including her bardic performance ability,
[bonus spells](ref/rule/determine-bonuses) per day, the maximum spell level she can cast, and the
save DCs of her spells.

## Dwarven Training (Ex) {#dwarven-training}

At 2nd level, a dwarven scholar masters one aspect of dwarven combat and gains a bonus combat feat.
She must meet the prerequisites for this feat, but she treats her bard level as her base attack
bonus (in addition to base attack bonuses gained from other classes and racial Hit Dice) for the
purpose of qualifying for this feat. At 6th level and every 4 levels thereafter, she gains another
bonus combat feat.

This replaces versatile performance.

## Bardic Performance {#bardic-performance}

A dwarven scholar gains the following type of bardic performance.

## War Chant (Su) {#war-chant}

At 1st level, a dwarven scholar can use her performance to inspire the martial prowess of the
ancient dwarves in her allies. The dwarven scholar selects a single combat feat she knows. Allies
affected by this performance gain the benefit of this feat for as long as the performance is
maintained. To be affected, an ally must be able to perceive the dwarven scholar's performance. If a
combat feat has a daily use limitation (such as [Stunning Fist](ref/feat/stunning-fist)), any uses
of that combat feat by the dwarven scholar's allies while using this ability counts toward the
dwarven scholar's feat's daily limit.

At 6th level, the dwarven scholar may grant the benefit of two combat feats at the same time. She
may use one of these feats to meet a prerequisite of the second feat. Maintaining two feats in this
way requires spending 2 rounds of bardic performance every round.

This replaces inspire courage and suggestion.
