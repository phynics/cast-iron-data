+++
id = "ref/arc-fighter/pack-mule"
kind = "archetype"
title = "Pack Mule"
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
replaces = ["The bonus feat gained at 1st level", "Bravery", "Armor training 1 through 4", "Armor mastery"]
alters = ["The fighter's skill ranks per level"]
replaces_features = ["bravery", "armor-mastery"]
+++

Pack mules carry heavy loads with ease and small packages with discretion. Unlike most couriers or
porters, pack mules are also trained combatants able to defend their charges should the need arise.
Many are willing to transport illegal goods, serving as runners for smugglers or muscle for bandits.
Pack mules seeking legitimate work prove useful additions to merchant caravans and adventuring
parties.

**Skill Ranks per Level**

**Alters:** The fighter's skill ranks per level

**Info:** He gains 4 + Int modifier skill ranks every level.

**Unobtrusive**

**Info:** A pack mule gains [Bluff](ref/skill/bluff) (Cha), [Disguise](ref/skill/disguise) (Cha),
[Sleight of Hand](ref/skill/sleight-of-hand) (Dex), and [Stealth](ref/skill/stealth) (Dex) as class
skills.

**Replaces:** The bonus feat gained at 1st level

**Efficient Packer (Ex)**

**Gained:** At 2nd Level

**Passive:** A pack mule adds a bonus equal to [half](ref/misc/fractions-and-rounding) his fighter
level on Sleight of Hand checks to conceal objects on his body. He also adds a bonus equal to 1/2
his class level to his Strength score for the purpose of determining his
[carrying capacity](ref/rule/carrying-capacity).

**Replaces:** Bravery

**Weight Training (Ex)**

**Ability:** A pack mule can move at his normal speed while carrying a medium load.

**At 11th Level:** The check penalty is now reduced by 4, the max Dex bonus is increased by 4.

**At 7th Level:** The check penalty is now reduced by 2, the max Dex bonus is increased by 2, and
the pack mule can now move at his normal speed while carrying a heavy load.

**Gained:** At 3rd Level

**Passive:** A pack mule learns to be more maneuverable when carrying loads. Whenever he is carrying
a medium or heavy load, he reduces the check penalty by 1 (to a minimum of 0) and increases the
maximum Dexterity bonus allowed by 1.

**Replaces:** Armor training 1 through 4

**Healthy as a Mule (Ex)**

**Gained:** At 19th Level

**Passive:** Whenever the pack mule takes
[Constitution, Dexterity, or Strength damage](ref/rule/ability-damage-drain), he reduces the amount
of ability damage taken by 2, to a minimum of 0.

**Replaces:** Armor mastery
