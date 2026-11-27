+++
id = "ref/arc-fighter/qadira-dawnflower-dervish"
kind = "archetype"
title = "Qadira: Dawnflower Dervish"
source_ids = ["inner-sea-primer"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "qadira_dawnflower_dervish", path = "json/archetypes_fighter2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/fighter" },
]
[[sources]]
publication = "inner-sea-primer"
page = "25"

[fields]
kind = "archetype"
features = [
  { anchor = "burst-of-speed", level = 3 },
  { anchor = "desert-stride", level = 7 },
  { anchor = "rapid-attack", level = 11 },
  { anchor = "lightning-strike", level = 15 },
]
trades = [
  { replaces = "Armor training 1", feature = "armor-training", levels = [3], by = ["burst-of-speed"] },
  { replaces = "Armor training 2", feature = "armor-training", levels = [7], by = ["desert-stride"] },
  { replaces = "Armor training 3", feature = "armor-training", levels = [11], by = ["rapid-attack"] },
  { replaces = "Armor training 4", feature = "armor-training", levels = [15], by = ["lightning-strike"] },
]
+++

In Qadira, home of the whirlwind, the [scorpion](ref/monster/scorpion-giant-scorpion), and the
[djinni](ref/monster/genie-djinni), no enemy is as feared as the dervishes of
[Sarenrae](ref/faith/sarenrae). While dervishes can be clerics, paladins, or rangers, zealous
fighters join their ranks as well. These spinning warriors prefer light or no armor and wield
[scimitars](ref/eq-weapon/scimitar) with devastating consequences, moving swiftly over the
treacherous desert sands to attack with lightning-fast strikes. They maneuver quickly among their
enemies, relying on their speed and their skill to see them through the battle.

## Suggested Feats {#suggested-feats}

[Agile Maneuvers](ref/feat/agile-maneuvers), [Combat Expertise](ref/feat/combat-expertise),
[Dazzling Display](ref/feat/dazzling-display), [Dervish Dance](ref/feat/dervish-dance) (see _World
Guide: The Inner Sea_), [Dodge](ref/feat/dodge), [Mobility](ref/feat/mobility),
[Spring Attack](ref/feat/spring-attack), [Step Up](ref/feat/step-up),
[Weapon Finesse](ref/feat/weapon-finesse), [Weapon Focus](ref/feat/weapon-focus) (scimitar),
[Weapon Specialization](ref/feat/weapon-specialization) (scimitar),
[Whirlwind Attack](ref/feat/whirlwind-attack).

## Burst of Speed (Ex) {#burst-of-speed}

At 3rd level, a Dawnflower dervish takes only a -1 penalty to her AC after
[charging](ref/rule/charge). At 7th level, the Dawnflower dervish can charge with no penalty. This
ability replaces armor training 1.

## Desert Stride (Ex) {#desert-stride}

At 7th level, a Dawnflower dervish can move through 10 feet of
[difficult terrain](ref/rule/terrain-and-obstacles) each round as if it were normal terrain. This
benefit stacks with the benefits provided by the [Acrobatic Steps](ref/feat/acrobatic-steps) and
[Nimble Moves](ref/feat/nimble-moves) feats. This ability replaces armor training 2.

## Rapid Attack (Ex) {#rapid-attack}

At 11th level, a Dawnflower dervish can combine a [full attack](ref/rule/full-attack) with a single
move. She must forgo the attack at her highest bonus but may take the remaining attacks at any point
during her movement. This movement provokes attacks of opportunity as normal. This ability replaces
armor training 3.

## Lightning Strike (Ex) {#lightning-strike}

At 15th level, as part of a full attack, a Dawnflower dervish can make one additional attack. This
attack is at the dervish's highest base attack bonus, but each attack in the round (including the
extra one) takes a -2 penalty. This ability replaces armor training 4.
