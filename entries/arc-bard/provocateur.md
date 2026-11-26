+++
id = "ref/arc-bard/provocateur"
kind = "archetype"
title = "Provocateur"
aon = "ArchetypeDisplay.aspx?FixedName=Bard%20Provocateur"
source_ids = ["inner-sea-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "provocateur", path = "json/archetypes_bard2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/bard" },
]
[[sources]]
publication = "inner-sea-intrigue"
page = "45"

[fields]
kind = "archetype"
features = [
  { anchor = "provocateur", level = 1 },
  { anchor = "calumny", level = 2 },
  { anchor = "damning-performance", level = 4 },
]
trades = [
  { replaces = "Bardic knowledge", feature = "bardic-knowledge", by = ["provocateur"] },
  { replaces = "The versatile performance gained at 2nd level", feature = "versatile-performance", levels = [2], by = ["calumny"] },
  { replaces = "Suggestion", feature = "bardic-performance", power = "suggestion", by = ["damning-performance"] },
  { replaces = "mass suggestion", feature = "bardic-performance", power = "mass suggestion", by = ["damning-performance"] },
]
+++

Provocateurs are bards who use their art to make controversial political statements, undermine
enemies' reputations, and upset the status quo on a large scale. They can be found most often in
areas of political unrest such as the unruly Chelish city of Kintargo, throughout rebellion-fraught
Galt, and among the backstabbing upper classes of Absalom, Brevoy, and Taldor.

## Provocateur (Ex) {#provocateur}

A provocateur adds 1/2 his bard level on skill checks to reduce a target's
[influence](ref/rule/influence) and on skill checks to reduce a target's attitude toward another
creature or organization.

This replaces bardic knowledge.

## Calumny (Ex) {#calumny}

At 2nd level, a provocateur can use his Perform (comedy, oratory, or sing) modifier in place of his
Bluff and Diplomacy modifier on checks to [spread a rumor](ref/rule/influencing-a-rumor) and in
place of his Intimidate modifier on checks to demoralize foes. This ability replaces the versatile
performance gained at 2nd level.

## Damning Performance (Su) {#damning-performance}

At 4th level, a provocateur can cause all observers fascinated by her
[fascinate](ref/performance/fascinate) performance to become less friendly to a target creature or
group of her choice for 10 minutes per bard level. Affected observers' attitudes toward the target,
the target's influence (_Ultimate Intrigue_ 102) with affected observers, and affected observers'
trust level as [contacts](ref/rule/contacts) for the target are all reduced by one step. If she
reveals information during the performance that would reduce those creatures' attitudes anyway,
those attitudes worsen by an additional step for the duration. If the provocateur engages in a
[verbal duel](ref/rule/verbal-duels) against the target with an audience affected by damning
performance, she automatically gains two edges.

At 18th level, the duration increases to 1 day per bard level. This ability replaces _suggestion_
and _mass suggestion_.
