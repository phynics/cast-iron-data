+++
id = "ref/arc-barbarian/titan-mauler"
kind = "archetype"
title = "Titan Mauler"
aon = "ArchetypeDisplay.aspx?FixedName=Barbarian%20Titan%20Mauler"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "titan_mauler", path = "json/archetypes_barbarian.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/barbarian" },
]
[[sources]]
publication = "ultimate-combat"
page = "30"

[fields]
kind = "archetype"
features = [
  { anchor = "big-game-hunter", level = 1 },
  { anchor = "jotungrip", level = 2 },
  { anchor = "massive-weapons", level = 3 },
  { anchor = "evade-reach", level = 5 },
  { anchor = "titanic-rage", level = 14 },
]
trades = [
  { replaces = "Fast movement", feature = "fast-movement", by = ["big-game-hunter"] },
  { replaces = "Uncanny dodge", feature = "uncanny-dodge", by = ["jotungrip"] },
  { replaces = "Trap sense", feature = "trap-sense", by = ["massive-weapons"] },
  { replaces = "Improved uncanny dodge", feature = "improved-uncanny-dodge", by = ["evade-reach"] },
  { replaces = "Indomitable will", feature = "indomitable-will", by = ["titanic-rage"] },
]
+++

In lands overrun by giants, dragons, and other hulking beasts, entire fellowships of barbarians hone
tactics and traditions with one purpose—to bring low these massive foes. While her enemies' size
makes the creatures strong, the titan mauler is even stronger, taking up weapons from her fallen
foes that no lesser warrior can lift, and using them when she beseeches the spirits to grant her
increased size and greater ferocity against her titanic foes.

## Big Game Hunter (Ex) {#big-game-hunter}

A titan mauler gains a +1 bonus on attack rolls and a +1 dodge bonus to AC in melee with creatures
larger than themselves. This ability replaces fast movement.

## Jotungrip (Ex) {#jotungrip}

At 2nd level, a titan mauler may choose to wield a two-handed melee weapon in one hand with a -2
penalty on attack rolls while doing so. The weapon must be appropriately sized for her, and it is
treated as one-handed when determining the effect of [Power Attack](ref/feat/power-attack), Strength
bonus to damage, and the like. This ability replaces uncanny dodge.

## Massive Weapons (Ex) {#massive-weapons}

At 3rd level, a titan mauler becomes skilled in the use of massive weapons looted from her titanic
foes. She can use two-handed weapons meant for creatures one size category larger, but the penalty
for doing so is increased by 4. However, the attack roll penalty for using weapons too large for her
size is reduced by 1, and this reduction increases by 1 for every three levels beyond 3rd (to a
minimum of 0). This ability replaces trap sense.

## Evade Reach (Ex) {#evade-reach}

At 5th level, as a swift action, a titan mauler may choose one creature within her line of sight.
Until the end of her turn, that target's reach is treated as if it were 5 feet shorter with respect
to reaching the titan mauler, and this reduction increases by 5 feet for every five levels beyond
5th. This ability replaces improved uncanny dodge.

## Titanic Rage (Su) {#titanic-rage}

At 14th level, a titan mauler may choose to gain the benefits of
_[enlarge person](ref/spell/enlarge-person)_ when she enters a rage. While using titanic rage, she
must spend 2 rounds of rage per round, and she becomes [exhausted](ref/misc/exhausted) rather than
fatigued when the rage ends. This ability replaces indomitable will.

## Rage Powers {#rage-powers}

The following rage powers complement the titan mauler archetype:
[body bludgeon](ref/ragepower/body-bludgeon),
[greater ground breaker](ref/ragepower/greater-ground-breaker),
[ground breaker](ref/ragepower/ground-breaker), [knockback](ref/ragepower/knockback),
[mighty swing](ref/ragepower/mighty-swing), [powerful blow](ref/ragepower/powerful-blow),
[smasher](ref/ragepower/smasher), and [strength surge](ref/ragepower/strength-surge).
