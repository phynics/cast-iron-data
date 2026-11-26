+++
id = "ref/arc-cavalier/sister-in-arms"
kind = "archetype"
title = "Sister-in-Arms"
aon = "ArchetypeDisplay.aspx?FixedName=Cavalier%20Sister-in-Arms"
source_ids = ["adventurers-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "sister_in_arms", path = "json/archetypes_cavalier.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/cavalier" },
]
[[sources]]
publication = "adventurers-guide"
page = "83"

[fields]
kind = "archetype"
features = [
  { anchor = "halfhearted-challenge", level = 1 },
  { anchor = "maiden-s-order", level = 1 },
  { anchor = "devoted-defender", level = 3 },
  { anchor = "maiden-s-loyalty", level = 4 },
  { anchor = "dedicated-commander", level = 11 },
]
trades = [
  { replaces = "Mount", feature = "mount", by = ["maiden-s-order"] },
  { replaces = "Cavalier's charge", feature = "cavalier-s-charge", by = ["devoted-defender"] },
  { replaces = "Expert trainer", feature = "expert-trainer", by = ["maiden-s-loyalty"] },
  { replaces = "Mighty charge", feature = "mighty-charge", by = ["dedicated-commander"] },
  { replaces = "supreme charge", feature = "supreme-charge", by = ["dedicated-commander"] },
  { alters = "Challenge", feature = "challenge", by = ["halfhearted-challenge"] },
  { alters = "Order", feature = "order", by = ["maiden-s-order"] },
]
+++

Some of the most charismatic [Gray Maidens](ref/rule/aff-scarred-ladies) combine their devotion to
their sisters with the intense tactical training they received, learning to perfectly direct their
companions and inspiring them to survive and emerge victorious. Known as sisters-in-arms, these
scarred soldiers are highly respected by their fellow Maidens for their dedication.

In the aftermath of Ileosa's fall, groups of Maidens forged a tight-knit family from their fellow
survivors, knowing that nobody else truly understood the horrors they had endured—or had been forced
to commit. Even after being accepted back into Korvosan society or fleeing the reach of the city's
justice, the [Gray Maidens](ref/rule/aff-scarred-ladies)' sisterhood has endured.

Sisters-in-arms are almost never neutral on the subject of Queen Ileosa; some still hold true to the
cruel queen's ideals and lead bands of like-minded veterans, while others have forsaken Ileosa in
favor of total devotion to their fellow survivors. Of the latter, the majority support the Scarlet
Rose, whether as social and emotional support for their recovering sisters, as field commanders for
military endeavors, or as private adventurers with ties to the order. Loyalist sisters-in-arms, by
contrast, are almost always plotting to reclaim Korvosa.

## Halfhearted Challenge (Ex) {#halfhearted-challenge}

Sisters-in-arms vigilantly protect their allies, weakening their focus on their challenged foe. A
sister-in-arms adds only [half](ref/misc/fractions-and-rounding) her cavalier level (minimum 1) to
damage rolls against her challenge target.

This ability alters challenge.

## Maiden's Order (Ex) {#maiden-s-order}

All sisters-in-arms share a talent for aiding and inspiring their fellow Gray Maidens, strengthened
by training and the bond of sisterhood. Generally, those loyal to Queen Ileosa refer to their pledge
as the order of the fanged crown, while those who have forsaken the cruel queen call it the order of
the scarlet rose. In either case, the benefits are the same.

A sister-in-arms does not choose an order. Instead, she is considered to belong to both the
[order of the dragon](ref/order/order-of-the-dragon) and the
[order of the lion](ref/order/order-of-the-lion), and she gains all of the benefits of both orders
(including additional class skills and conditional skill bonuses, additional challenge benefits, and
order abilities) at the appropriate levels. At 1st level, a sister-in-arms chooses which order's
edicts she must follow; generally, those of the fanged crown choose the order of the lion's edicts,
while those of the scarlet rose choose the order of the dragon's edicts.

This ability alters order and replaces mount.

## Devoted Defender (Ex) {#devoted-defender}

Sisters-in-arms cling to their fellow Gray Maidens as closely as family and protect them with
intense devotion. At 3rd level, a sister-in-arms gains [Bodyguard](ref/feat/bodyguard) as a bonus
feat (she does not need to meet the feat's prerequisite).

This ability replaces cavalier's charge.

## Maiden's Loyalty (Ex) {#maiden-s-loyalty}

The loyalty of a sister-in-arms is absolute. At 4th level, a sister-in-arms gains a +2 bonus on Will
saves against any effect that would compel her to attack or betray her allies. This bonus increases
by 1 for every 4 levels beyond 4th.

This ability replaces expert trainer.

## Dedicated Commander (Ex) {#dedicated-commander}

A sister-in-arms can inspire and direct allies with great efficiency. At 11th level, the
sister-in-arms can use lion's call or strategy order as a move action, rather than as a standard
action. At 20th level, she can use act as one, lion's call, or strategy order as a swift or move
action.

This ability replaces mighty charge and supreme charge.
