+++
id = "ref/arc-fighter/free-hand-fighter"
kind = "archetype"
title = "Free Hand Fighter"
aon = "ArchetypeDisplay.aspx?FixedName=Fighter%20Free%20Hand%20Fighter"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "free_hand_fighter", path = "json/archetypes_fighter.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/fighter" },
]
[[sources]]
publication = "advanced-players-guide"
page = "105"

[fields]
kind = "archetype"
features = [
  { anchor = "deceptive-strike", level = 2 },
  { anchor = "elusive", level = 3 },
  { anchor = "singleton", level = 5 },
  { anchor = "timely-tip", level = 9 },
  { anchor = "interference", level = 13 },
  { anchor = "reversal", level = 19 },
]
trades = [
  { replaces = "Bravery", feature = "bravery", by = ["deceptive-strike"] },
  { replaces = "Armor training 1, 2, 3, and 4", feature = "armor-training", levels = [3, 7, 11, 15], by = ["elusive"] },
  { replaces = "Weapon training 1 and 4", feature = "weapon-training", levels = [5, 17], by = ["singleton"] },
  { replaces = "Weapon training 2", feature = "weapon-training", levels = [9], by = ["timely-tip"] },
  { replaces = "Weapon training 3", feature = "weapon-training", levels = [13], by = ["interference"] },
  { replaces = "Armor mastery", feature = "armor-mastery", by = ["reversal"] },
]
+++

The free hand fighter specializes in the delicate art of handling a single weapon in one hand while
using his free hand to balance, block, tip, and distract his opponents. While not a brawler, his
open hand is as much a weapon as a bow or blade. His fighting school benefits only apply when he is
using a one-handed weapon and carrying nothing in his other hand.

## Deceptive Strike (Ex) {#deceptive-strike}

At 2nd level, a free hand fighter gains a +1 bonus to CMB and CMD on [disarm](ref/rule/disarm)
checks and on Bluff checks to feint or create a diversion to hide. This bonus increases by +1 for
every four levels after 2nd. This ability replaces bravery.

## Elusive (Ex) {#elusive}

At 3rd level, a free hand fighter gains a +1 dodge bonus to AC. This bonus increases by +1 for every
four levels after 2nd. This bonus does not apply when wearing medium or heavy armor or carrying a
medium or heavier load. This ability replaces armor training 1, 2, 3, and 4.

## Singleton (Ex) {#singleton}

At 5th level, a free hand fighter gains a +1 bonus on attack and damage rolls when wielding a melee
weapon in one hand and leaving his other hand free. This bonus increases by +1 per six levels after
5th. This ability replaces weapon training 1 and 4.

## Timely Tip (Ex) {#timely-tip}

At 9th level, a free hand fighter can make a disarm combat maneuver against a target he threatens as
a move action to push aside the target's shield. If successful, the target loses its shield bonus to
AC against the free hand fighter's next attack. This ability replaces weapon training 2.

## Interference (Ex) {#interference}

At 13th level, a free hand fighter can make a disarm or [trip](ref/rule/trip) combat maneuver
against a target he threatens as a move action to push his opponent off balance. If successful, the
target becomes [flat-footed](ref/rule/flat-footed). This condition lasts until the target takes
damage from a melee or ranged attack or until the beginning of the free hand fighter's next turn,
whichever comes first. This ability replaces weapon training 3.

## Reversal (Ex) {#reversal}

At 19th level, a free hand fighter can make a disarm combat maneuver against a creature he threatens
as an immediate action when he is the target of a melee attack from another creature. If successful,
the attack changes to target the target of the free hand fighter's maneuver instead of the free hand
fighter himself. This ability replaces armor mastery.
