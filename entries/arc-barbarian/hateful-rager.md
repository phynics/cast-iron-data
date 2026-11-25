+++
id = "ref/arc-barbarian/hateful-rager"
kind = "archetype"
title = "Hateful Rager"
aon = "ArchetypeDisplay.aspx?FixedName=Barbarian%20Hateful%20Rager"
source_ids = ["advanced-race-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "hateful_rager", path = "json/archetypes_barbarian.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/barbarian" },
]
[[sources]]
publication = "advanced-race-guide"
page = "54"

[fields]
kind = "archetype"
features = [
  { anchor = "reduced-rage", level = 2 },
  { anchor = "favored-enemy", level = 2 },
  { anchor = "feed-the-rage", level = 5 },
  { anchor = "amplified-by-hate", level = 9 },
]
trades = [
  { replaces = "Barbarian's rage power gained at 2nd level", feature = "rage-powers", levels = [2, 8, 14, 20], by = ["favored-enemy"] },
  { replaces = "Improved uncanny dodge", feature = "improved-uncanny-dodge", by = ["feed-the-rage"] },
  { replaces = "Trap sense +3", feature = "trap-sense", levels = [9], by = ["amplified-by-hate"] },
]
+++

From a young age, many half-orcs are treated cruelly, bullied, ridiculed, and made outcasts. While
some hide their shame, others foster a deep, burning hatred that they channel into a raw fury and
unleash against their enemies. These half-orcs are called hateful ragers. A hateful rager has the
following class features.

## Reduced Rage (Ex) {#reduced-rage}

At 2nd level and every level thereafter, a hateful rager only gains 1 additional round of rage per
day instead of the normal 2 additional rounds of rage per day.

## Favored Enemy (Ex) {#favored-enemy}

At 2nd level, a hateful rager selects a [favored enemy](ref/ability/favored-enemy). This ability
works identically to the [ranger](ref/class/ranger) ability of the same name. At 8th, 14th, and 20th
level, the hateful rager selects another favored enemy and increases her bonus against one favored
enemy type, as described in the ranger class.

While raging, the hateful rager makes every effort to fight a favored enemy rather than other
opponents. If aware of the presence of a favored enemy, the hateful rager must make a DC 20 Will
save each round to attack another creature; failure means the barbarian must attack the favored
enemy or move closer to that enemy. She may freely attack creatures preventing her from reaching
that favored enemy (regardless of whether they are actively trying to prevent her attacks or merely
in the way). She can avoid harmful obstacles normally in her attempts to reach the target and is not
forced to take the shortest route.

This ability replaces the barbarian's rage power gained at 2nd level. At 8th, 14th, and 20th levels,
in place of a rage power she gains another favored enemy and increases her bonus against one favored
enemy type.

## Feed the Rage (Ex) {#feed-the-rage}

At 5th level, a hateful rager gains 1 additional round of rage for each favored enemy she knocks
unconscious or kills in combat. These current rounds of rage can only be used to add to the duration
of her rage, and disappear when the rage ends. This ability replaces improved uncanny dodge.

## Amplified by Hate (Ex) {#amplified-by-hate}

At 9th level, a hateful rager adds [half](ref/misc/fractions-and-rounding) her favored enemy bonus
to the DC of any rage power she uses against a favored enemy. This ability replaces trap sense +3.

## Rage Powers {#rage-powers}

The following rage powers complement the hateful rager archetype:
[intimidating glare](ref/ragepower/intimidating-glare), [roused anger](ref/ragepower/roused-anger),
[terrifying howl](ref/ragepower/terrifying-howl) (_Core Rulebook_);
[come and get me](ref/ragepower/come-and-get-me),
[inspire ferocity](ref/ragepower/inspire-ferocity),
[overbearing advance](ref/ragepower/overbearing-advance),
[reckless abandon](ref/ragepower/reckless-abandon) (_Advanced Player's Guide_).
