+++
id = "ref/arc-monk/sage-counselor"
kind = "archetype"
title = "Sage Counselor"
aon = "ArchetypeDisplay.aspx?FixedName=Monk%20Sage%20Counselor"
source_ids = ["ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "sage_counselor", path = "json/archetypes_monk2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/monk" },
]
[[sources]]
publication = "ultimate-intrigue"
page = "67"

[fields]
kind = "archetype"
features = [
  { anchor = "cunning-fist", level = 1 },
  { anchor = "feinting-flurry", level = 4 },
  { anchor = "deceptive-ki", level = 4 },
]
trades = [
  { replaces = "Bonus feats gained at 1st, 2nd, and 6th levels", feature = "bonus-feat", levels = [1, 2, 6], by = ["cunning-fist"] },
  { replaces = "bonus feat gained at 10th level", feature = "bonus-feat", levels = [10], by = ["feinting-flurry"] },
  { replaces = "The ability to spend ki to increase his speed by 20 feet for 1 round", by = ["deceptive-ki"] },
  { alters = "Flurry of blows", feature = "flurry-of-blows", by = ["feinting-flurry"] },
  { alters = "ki pool", feature = "ki-pool", by = ["feinting-flurry", "deceptive-ki"] },
  { alters = "Class skills" },
]
+++

Sage counselors are ascetics and mystics who leave the confines of the monastery walls to advise
secular people about spiritual truths and to seek knowledge of the outside world. They often find
work as mentors teaching religion and martial arts, and some of them even become counselors for
people in high places. Sage counselors often speak in metaphors, knowing that indirect persuasion is
more effective than speaking plainly, and they use indirect tactics in combat as well.

## Class Skills {#class-skills}

A sage counselor adds Bluff, Diplomacy, and Knowledge (nobility) to his list of class skills,
instead of Climb, Escape Artist, and Perception.

This alters the monk's class skills.

## Cunning Fist (Ex) {#cunning-fist}

A sage counselor gains [Combat Expertise](ref/feat/combat-expertise) as a bonus feat, even if he
doesn't meet the prerequisites, and he can ignore the Intelligence prerequisite on feats that have
Combat Expertise as a prerequisite. At 2nd level, he gains
[Improved Feint](ref/feat/improved-feint), and at 6th level, he gains
[Greater Feint](ref/feat/greater-feint), even if he doesn't meet the prerequisites.

This ability replaces the bonus feats gained at 1st, 2nd, and 6th levels.

## Feinting Flurry {#feinting-flurry}

At 4th level, a sage counselor can spend 1 ki point while performing a flurry of blows to
[feint](ref/skill/bluff) an opponent as a swift action, but he can't spend 1 ki point to make an
additional attack when making a flurry of blows. At 10th level, he can also choose to replace his
first attack during a flurry of blows with a feint check.

This ability alters flurry of blows and ki pool, and it replaces the bonus feat gained at 10th
level.

## Deceptive Ki (Su) {#deceptive-ki}

At 4th level, the sage counselor can spend 1 point from his ki pool as a swift action to give
himself a +4 insight bonus on his next Bluff check. The sage counselor does not gain the ability to
spend ki to increase his speed by 20 feet for 1 round.

This ability alters ki pool (and it replaces the ki power gained at 4th level for an unchained
monk).
