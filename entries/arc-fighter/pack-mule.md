+++
id = "ref/arc-fighter/pack-mule"
kind = "archetype"
title = "Pack Mule"
aon = "ArchetypeDisplay.aspx?FixedName=Fighter%20Pack%20Mule"
source_ids = ["black-markets"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "pack_mule", path = "json/archetypes_fighter2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/fighter" },
]
[[sources]]
publication = "black-markets"
page = "26"

[fields]
kind = "archetype"
features = [
  { anchor = "unobtrusive", level = 1 },
  { anchor = "efficient-packer", level = 2 },
  { anchor = "weight-training", level = 3 },
  { anchor = "healthy-as-a-mule", level = 19 },
]
trades = [
  { replaces = "The bonus feat gained at 1st level", feature = "bonus-feats", levels = [1], by = ["unobtrusive"] },
  { replaces = "Bravery", feature = "bravery", by = ["efficient-packer"] },
  { replaces = "Armor training 1 through 4", feature = "armor-training", levels = [3, 7, 11, 15], by = ["weight-training"] },
  { replaces = "Armor mastery", feature = "armor-mastery", by = ["healthy-as-a-mule"] },
  { alters = "The fighter's skill ranks per level" },
]
+++

Pack mules carry heavy loads with ease and small packages with discretion. Unlike most couriers or
porters, pack mules are also trained combatants able to defend their charges should the need arise.
Many are willing to transport illegal goods, serving as runners for smugglers or muscle for bandits.
Pack mules seeking legitimate work prove useful additions to merchant caravans and adventuring
parties.

## Skill Ranks per Level {#skill-ranks-per-level}

4 + Int modifier. This alters the fighter's skill ranks per level.

## Unobtrusive {#unobtrusive}

A pack mule gains [Bluff](ref/skill/bluff) (Cha), [Disguise](ref/skill/disguise) (Cha),
[Sleight of Hand](ref/skill/sleight-of-hand) (Dex), and [Stealth](ref/skill/stealth) (Dex) as class
skills. This ability replaces the bonus feat gained at 1st level.

## Efficient Packer (Ex) {#efficient-packer}

At 2nd level, a pack mule adds a bonus equal to 1/2 his fighter level on Sleight of Hand checks to
conceal objects on his body. He also adds a bonus equal to 1/2 his class level to his Strength score
for the purpose of determining his [carrying capacity](ref/rule/carrying-capacity). This ability
replaces bravery.

## Weight Training (Ex) {#weight-training}

At 3rd level, a pack mule learns to be more maneuverable when carrying loads. Whenever he is
carrying a medium or heavy load, he reduces the check penalty by 1 (to a minimum of 0) and increases
the maximum Dexterity bonus allowed by 1. At 7th, 11th, and 15th levels, these benefits increase by
1 (to a maximum of 4 at 15th level).

In addition, a pack mule can move at his normal speed while carrying a medium load. At 7th level, a
pack mule can move at his normal speed while carrying a heavy load.

This ability replaces armor training 1 through 4.

## Healthy as a Mule (Ex) {#healthy-as-a-mule}

At 19th level, whenever the pack mule takes
[Constitution, Dexterity, or Strength damage](ref/rule/ability-damage-drain), he reduces the amount
of ability damage taken by 2, to a minimum of 0. This ability replaces armor mastery.
