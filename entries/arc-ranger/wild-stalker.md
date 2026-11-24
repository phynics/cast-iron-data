+++
id = "ref/arc-ranger/wild-stalker"
kind = "archetype"
title = "Wild Stalker"
aon = "ArchetypeDisplay.aspx?FixedName=Ranger%20Wild%20Stalker"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "wild_stalker", path = "json/archetypes_ranger.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/ranger" },
]
[[sources]]
publication = "ultimate-combat"
page = "68"

[fields]
kind = "archetype"
features = [
  { anchor = "strong-senses", level = 1 },
  { anchor = "uncanny-dodge", level = 2 },
  { anchor = "rage-of-the-wild", level = 4 },
  { anchor = "rage-powers", level = 5 },
  { anchor = "wild-talents", level = 6 },
]
trades = [
  { replaces = "1st favored enemy", feature = "favored-enemy", levels = [1], by = ["strong-senses"] },
  { replaces = "2nd-level combat style feat", feature = "combat-style-feat", levels = [2], by = ["uncanny-dodge"] },
  { replaces = "Hunter's bond", feature = "hunter-s-bond", by = ["rage-of-the-wild"] },
  { replaces = "2nd, 3rd, 4th, and 5th favored enemy", feature = "favored-enemy", levels = [5, 10, 15, 20], by = ["rage-powers"] },
  { replaces = "6th-, 10th-, 14th-, and 18th-level combat style feat", feature = "combat-style-feat", levels = [6, 10, 14, 18], by = ["wild-talents"] },
]
+++

Civilization grows stronger and more decadent with each passing year. It tears into unclaimed
wilderness and destroys the fragile ecology in its constant push for expansion and exploitation. The
wild stalker forsakes the bonds of community and lives in the trackless wilds far from others of his
kind, or perhaps grew up there, never knowing of civilization as anything more than his enemy. He
drives pioneers back to civilization and strives to keep the land unspoiled.

## Strong Senses (Ex) {#strong-senses}

At 1st level, a wild stalker's life among the wild has sharpened his senses. He gains
[low-light vision](ref/rule/low-light-vision) and a +1 bonus on Perception checks. If he already has
low-light vision, he gains a +2 bonus on Perception checks instead. This bonus increases by +1 for
every four levels after 1st (to a maximum of +6 at 20th level, or +7 if the character did not gain
low-light vision from this ability). This ability replaces the ranger's first favored enemy ability.

## Uncanny Dodge (Ex) {#uncanny-dodge}

At 2nd level, a wild stalker gains [uncanny dodge](ref/ability/uncanny-dodge) as the barbarian's
class feature. This ability replaces the ranger's 2nd-level combat style feat.

## Rage of the Wild (Ex) {#rage-of-the-wild}

At 4th level, a wild stalker gains the rage ability as the [barbarian](ref/class/barbarian) class
feature, but its barbarian level is considered to be his ranger level -3. This ability replaces
hunter's bond.

## Rage Powers {#rage-powers}

At 5th level, a wild stalker ranger gains a single rage power, as the barbarian class feature. He
gains another rage power each five levels after 5th (to a maximum of four rage powers at 20th
level). This ability replaces the ranger's second, third, fourth, and fifth favored enemy abilities.

## Wild Talents (Ex) {#wild-talents}

At 6th level, a wild stalker can either take a rage power, or gains a +2 insight bonus into any one
of the following skills: Acrobatics, Climb, Perception, Stealth, Survival, or Swim. The wild stalker
can gain one of these two benefits again every five levels after 6th (to a maximum of 4 times at
20th level). This ability replaces the ranger's 6th-, 10th-, 14th-, and 18th-level combat style feat
abilities.
