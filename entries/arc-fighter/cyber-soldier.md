+++
id = "ref/arc-fighter/cyber-soldier"
kind = "archetype"
title = "Cyber-Soldier"
aon = "ArchetypeDisplay.aspx?FixedName=Fighter%20Cyber-Soldier"
source_ids = ["technology-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "cyber_soldier", path = "json/archetypes_fighter.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/fighter" },
]
[[sources]]
publication = "technology-guide"
page = "12"

[fields]
kind = "archetype"
features = [
  { anchor = "cybernetic-combat", level = 5 },
  { anchor = "improved-implantation", level = 7 },
  { anchor = "resilience", level = 19 },
]
trades = [
  { replaces = "Weapon training 1", feature = "weapon-training", levels = [5], by = ["cybernetic-combat"] },
  { replaces = "Armor training 2 and 4", feature = "armor-training", levels = [7, 15], by = ["improved-implantation"] },
  { replaces = "Armor mastery", feature = "armor-mastery", by = ["resilience"] },
]
+++

Cyber-soldiers replace fallible flesh with precision-crafted machinery. Some seek to exceed the
limitations of humanoid flesh, while others become cyber-soldiers through drastic repairs
necessitated by horrific injuries. A cyber-soldier has the following class features.

## Cybernetic Combat (Ex) {#cybernetic-combat}

At 5th level, a cyber-soldier gains a +1 bonus on attack rolls with
[implanted weapons](ref/tech-cyber/implanted-weaponry),
[cybernetic arms](ref/tech-cyber/cybernetic-arm), and melee or thrown weapons wielded with a
cybernetic arm. Weapons wielded with two cybernetic arms receive double the bonus, except when such
weapons are thrown. This damage bonus increases by 1 for every 4 levels gained. This attack bonus
does not stack with the attack bonus for weapon training. A cyber-soldier gains a slam attack for
each cybernetic arm. These attacks deal 1d6 points of bludgeoning damage for a Medium cyber-soldier
and 1d4 points of bludgeoning damage for a Small cyber-soldier. This ability replaces weapon
training 1.

## Improved Implantation (Ex) {#improved-implantation}

At 7th level, a cyber-soldier can exceed the normal limitations on [cybertech](ref/rule/cybertech)
implantation. Her brain and body slots each accommodate one more piece of cybertech than normal. In
addition, her limit on implantation points increases by 1/2 his cyber-soldier level. She can
allocate these points between his Intelligence and Constitution scores as she chooses. At 15th
level, her body slot can accommodate two more pieces of cybertech than normal. This ability replaces
armor training 2 and 4.

## Resilience (Ex) {#resilience}

At 19th level, a cyber-soldier has a reservoir of 5
[temporary hit points](ref/rule/temporary-hit-points) for each piece of implanted cybertech in his
body. Lost temporary hit points are recovered at the rate of 10 points per hour. This ability
replaces armor mastery.
