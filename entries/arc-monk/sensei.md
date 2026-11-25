+++
id = "ref/arc-monk/sensei"
kind = "archetype"
title = "Sensei"
aon = "ArchetypeDisplay.aspx?FixedName=Monk%20Sensei"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "sensei", path = "json/archetypes_monk2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/monk" },
]
[[sources]]
publication = "ultimate-combat"
page = "60"

[fields]
kind = "archetype"
features = [
  { anchor = "advice", level = 1 },
  { anchor = "insightful-strike", level = 2 },
  { anchor = "mystic-wisdom", level = 6 },
]
trades = [
  { replaces = "Flurry of blows", feature = "flurry-of-blows", by = ["advice"] },
  { replaces = "fast movement", feature = "fast-movement", by = ["advice"] },
  { replaces = "improved evasion", feature = "improved-evasion", by = ["advice"] },
  { replaces = "Evasion", feature = "evasion", by = ["insightful-strike"] },
  { replaces = "bonus feat gained at 2nd level", feature = "bonus-feat", levels = [2], by = ["insightful-strike"] },
  { replaces = "Bonus feats at 6th, 10th, and 14th level", feature = "bonus-feat", levels = [6, 10, 14], by = ["mystic-wisdom"] },
]
+++

The sensei is a revered teacher who imparts lessons on the oneness of mind, body, and spirit, along
with occasional correction that is subtle and swift. Rather than using wisdom for his own benefit
alone, he uses it to better those around him.

## Skills {#skills}

A sensei gains Diplomacy, Linguistics, and all Knowledge skills as class skills.

## Advice (Ex) {#advice}

A sensei's advice is identical to bardic performance (using oratory), allowing him to
[inspire courage](ref/performance/inspire-courage) at 1st level,
[inspire competence](ref/performance/inspire-competence) at 3rd level, and
[inspire greatness](ref/performance/inspire-greatness) at 9th level, as a bard of the sensei's
level, usable a total number of rounds per day equal to his level + his Wisdom modifier (minimum 1).
This ability replaces flurry of blows, fast movement, and improved evasion.

## Insightful Strike (Ex) {#insightful-strike}

At 2nd level, a sensei may use his Wisdom bonus in lieu of his Strength or Dexterity on attack rolls
and combat maneuver checks with unarmed strikes or monk weapons. This ability replaces evasion and
the bonus feat gained at 2nd level.

## Mystic Wisdom (Su) {#mystic-wisdom}

At 6th level, a sensei may use his advice ability when spending points from his ki pool to activate
a class ability (using the normal actions required for each) in order to have that ability affect
one ally within 30 feet rather than the sensei himself. At 12th level, a sensei may affect all
allies within 30 feet rather than himself (spending points from his ki pool only once, not once for
each target).

At 10th level, a sensei may instead spend 1 point from his ki pool (as a swift action) while using
advice to provide a single ally within 30 feet with evasion, fast movement, high jump, purity of
body, or slow fall. At 14th level, a sensei may spend 2 points to grant one of the abilities listed
above to all allies within 30 feet, or diamond body, diamond soul, or improved evasion to a single
ally within 30 feet. These abilities function at the sensei's level and last 1 round. This ability
replaces the bonus feats at 6th, 10th, and 14th level.
