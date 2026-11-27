+++
id = "ref/arc-fighter/corsair"
kind = "archetype"
title = "Corsair"
aon = "ArchetypeDisplay.aspx?FixedName=Fighter%20Corsair"
source_ids = ["pirates-of-the-inner-sea"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "corsair", path = "json/archetypes_fighter.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/fighter" },
]
[[sources]]
publication = "pirates-of-the-inner-sea"
page = "22"

[fields]
kind = "archetype"
features = [
  { anchor = "pirate-weapons" },
  { anchor = "deck-fighting", level = 2 },
  { anchor = "armored-pirate", level = 3 },
  { anchor = "improved-deck-fighting", level = 6 },
]
trades = [
  { replaces = "the fighter's 2nd-level bonus feat", feature = "bonus-feats", levels = [2], by = ["deck-fighting"] },
  { replaces = "armor training", feature = "armor-training", by = ["armored-pirate"] },
  { replaces = "the fighter's 6th-level bonus feat", feature = "bonus-feats", levels = [6], by = ["improved-deck-fighting"] },
]
+++

A corsair is a pirate who focuses on shipboard combat, relying on his strength of arms over his
agility. He specializes in traditional pirate weapons, but often wears heavier armor than is
normally seen on a ship. A corsair moves and fights easily in his armor, however, even in the water.
Captains value corsairs because of the skill they exhibit in defending the ship and in boarding
actions.

## Pirate Weapons (Ex) {#pirate-weapons}

A corsair is well versed in the types of weapons favored by pirates. When selecting a
[group of weapons](ref/ability/weapon-groups) for his Weapon Training ability, he can select Pirate
Weapons as a group. The Pirate Weapons group consists of the crossbow,
[cutlass](ref/eq-weapon/cutlass), [dagger](ref/eq-weapon/dagger),
[hook hand](ref/eq-weapon/hook-hand), [rapier](ref/eq-weapon/rapier), and
[short sword](ref/eq-weapon/short-sword).

## Deck Fighting (Ex) {#deck-fighting}

A corsair is used to fighting on crowded decks, and isn't fazed by fighting multiple opponents at
once. At 2nd level, he gains [Cleave](ref/feat/cleave) as a bonus feat. He may use this feat even if
he does not meet the prerequisites. A corsair does not take the normal -2 penalty to his AC when
using the Cleave feat. This ability replaces the fighter's 2nd-level bonus feat.

## Armored Pirate (Ex) {#armored-pirate}

A corsair wears heavier armor than is common aboard a ship. At 3rd level, the corsair reduces the
armor check penalty of any light armor he wears to 0 for purposes of Acrobatics and Swim checks. At
7th level, this becomes true of medium armor as well. At 11th level, it includes heavy armor. This
ability replaces armor training.

## Improved Deck Fighting (Ex) {#improved-deck-fighting}

At 6th level, the corsair gains [Great Cleave](ref/feat/great-cleave) as a bonus feat. He may use
this feat even if he does not meet the prerequisites. A corsair does not take the normal -2 penalty
to his AC when using the Great Cleave feat. This ability replaces the fighter's 6th-level bonus
feat.
