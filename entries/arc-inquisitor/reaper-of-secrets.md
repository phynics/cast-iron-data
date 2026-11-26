+++
id = "ref/arc-inquisitor/reaper-of-secrets"
kind = "archetype"
title = "Reaper of Secrets"
aon = "ArchetypeDisplay.aspx?FixedName=Inquisitor%20Reaper%20of%20Secrets"
source_ids = ["dirty-tactics-toolbox"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "reaper_of_secrets", path = "json/archetypes_inquisitor.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/inquisitor" },
]
[[sources]]
publication = "dirty-tactics-toolbox"
page = "17"

[fields]
kind = "archetype"
features = [
  { anchor = "bound-by-secrecy" },
  { anchor = "deceitful-lore", level = 1 },
  { anchor = "soul-piercing-gaze", level = 1 },
  { anchor = "mind-game-tactics", level = 3 },
]
trades = [
  { replaces = "Monster lore", feature = "monster-lore", by = ["deceitful-lore"] },
  { replaces = "Stern gaze", feature = "stern-gaze", by = ["soul-piercing-gaze"] },
  { replaces = "Solo tactics", feature = "solo-tactics", by = ["mind-game-tactics"] },
]
+++

Masters of mind tricks and deception, these divine assassins track down and kill anyone who has
forbidden knowledge about their faiths.

## Bound by Secrecy (Ex) {#bound-by-secrecy}

A reaper of secrets must choose [Norgorber](ref/faith/norgorber) as her deity. If she ever changes
her deity, she loses this archetype and becomes a normal inquisitor.

## Deceitful Lore (Ex) {#deceitful-lore}

At 1st level, a reaper of secrets adds her Wisdom modifier on Bluff and Disguise skill checks in
addition to her Charisma modifier. This ability replaces monster lore.

## Soul-Piercing Gaze (Su) {#soul-piercing-gaze}

At 1st level, as a swift action, a reaper of secrets can focus on a single creature she can see. She
then gains an insight bonus on Perception and Sense Motive checks against that creature equal to 1/2
her level (minimum +1). The effect ends if she focuses on a new target. This ability replaces stern
gaze.

## Mind-Game Tactics (Su) {#mind-game-tactics}

At 3rd level, a reaper of secrets can read other creatures so well she can use their reactions to
gain a tactical advantage. She treats any creature targeted by her soul-piercing gaze as if it were
her ally and possessed the same teamwork feats as she does for the purposes of positioning and
threatening when she determines whether she receives a benefit from her teamwork feats. She cannot
use this ability to benefit from any teamwork feats that require particular actions from allies,
such as [Swap Places](ref/feat/swap-places).

For example, a reaper of secrets with the [Precise Strike](ref/feat/precise-strike) feat gains the
bonus from that feat if she and the target of her soul-piercing gaze occupy flanking positions
relative to the creature she attacks.

This ability replaces solo tactics.
