+++
id = "ref/arc-bard/sorrowsoul"
kind = "archetype"
title = "Sorrowsoul"
aon = "ArchetypeDisplay.aspx?FixedName=Bard%20Sorrowsoul"
source_ids = ["ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "sorrowsoul", path = "json/archetypes_bard2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/bard" },
]
[[sources]]
publication = "ultimate-intrigue"
page = "22"

[fields]
kind = "archetype"
features = [
  { anchor = "lyric-sorrow" },
  { anchor = "darkness-denied", level = 2 },
  { anchor = "spurn-harm" },
]
trades = [
  { replaces = "Soothing performance", feature = "bardic-performance", power = "soothing performance", by = ["lyric-sorrow"] },
  { replaces = "versatile performance", feature = "versatile-performance", by = ["lyric-sorrow"] },
  { replaces = "Well-versed", feature = "well-versed", by = ["darkness-denied"] },
  { replaces = "Lore master", feature = "lore-master", by = ["spurn-harm"] },
  { alters = "Bardic performance", feature = "bardic-performance", by = ["lyric-sorrow"] },
]
+++

It isn't uncommon for a bard to, on occasion, sing mournful tunes or craft elegies that depict the
deepest sadness or the most profound suffering. But while most bards who do so create such
performances for fame or wealth, the sorrowsoul has known tragedy and loss on a level so intimate,
he has bound it to his soul.

## Lyric Sorrow (Su) {#lyric-sorrow}

A sorrowsoul draws upon grief, rage, and tragedy to fuel his bardic performances. When a sorrowsoul
begins a bardic performance, he can choose to alter its effects with lyric sorrow. If he does so, he
uses twice the number of rounds of his bardic performance ability as normal, and even if the
sorrowsoul has the Lingering Performancefeat, the performance's effects do not last for any
additional rounds.

At 1st level, a sorrowsoul can use his lyric sorrow in conjunction with inspire courage. When he
chooses to do so, he increases his bonuses on saving throws and on weapon attack and damage rolls
from +1 to +2, but his other allies receive no benefit. His bonuses when using lyric sorrow with
inspire courage increase by 2 at 5th level and every 6 bard levels thereafter, to a maximum of +8 at
17th level.

At 12th level, a sorrowsoul can use his lyric sorrow ability in conjunction with inspire greatness
to grant himself 3 bonus Hit Dice, a +3 competence bonus on attack rolls, and a +2 competence bonus
on Fortitude saves; if he does so, inspire greatness only affects him, not any other allies.

At 15th level, a sorrowsoul can use his lyric sorrow ability in conjunction with the inspire heroics
bardic performance. When using the lyric sorrow version of this performance, a sorrowsoul gains fast
healing 5 and benefits from a 50% miss chance, as if under the effects of _displacement_, in
addition to the standard bonuses conferred by this bardic performance, but if he does so, inspire
heroics only affects him, not any other allies.

This ability alters bardic performance and replaces soothing performance and versatile performance.

## Darkness Denied (Ex) {#darkness-denied}

At 2nd level, a sorrowsoul gains a +4 bonus on saving throws against negative energy and death
effects.

This ability replaces well-versed.

## Spurn Harm (Su) {#spurn-harm}

A sorrowsoul can funnel his bardic powers to persevere in the face of seemingly certain death. At
5th level, a sorrowsoul can spend 3 rounds of his daily bardic performance as an immediate action to
gain a +2 insight bonus on all saving throws for 1 round. At 11th level, a sorrowsoul also gains
[spell resistance](ref/rule/spell-resistance) equal to 11 + his bard level when using this ability.
At 17th level, a sorrowsoul also gains DR 10/—when using this ability.

This ability replaces lore master.
