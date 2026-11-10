+++
id = "ref/arc-gunslinger/commando"
kind = "archetype"
title = "Commando"
source_ids = ["ultimate-wilderness"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "commando", path = "json/archetypes_gunslinger.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/gunslinger" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "91"

[fields]
kind = "archetype"
replaces = ["Utility shot deed", "Expert loading deed", "Lightning reload deed", "Slinger's luck deed", "Nimble", "The bonus feat gained at 4th level"]
alters = ["Gun training"]
replaces_features = ["nimble"]
alters_features = ["gun-training"]
+++

Commandos are those rough and ready gunslingers who excel at hit-and-run tactics and leveraging
their expertise in the wild against their enemies.

**Gained class skills:** kg, kna, stl

**Lost class skills:** ke, kl, soh

**Deeds**

**Ability:** A commando gains the following deeds; each of these deeds replaces an existing deed.

**Trap Shot (Ex)**

**Ability:** The commando can spend 1 point of grit and target a 5-foot square with her firearm. If
she succeeds at an attack against an AC of 10, she triggers a single trap within that 5-foot square,
even if she is unaware of the trap. If a creature is occupying the same square as the triggered
trap, the trap affects the creature as if it had triggered the trap.

**Gained:** At 3rd Level

**Replaces:** Utility shot deed

**Special:** If there are multiple traps within the same 5-foot square, the commando must declare
which trap she is triggering; otherwise it is determined randomly.

**Sniping Shot (Ex)**

**Gained:** At 11th Level

**Replaces:** Expert loading deed

**Swift:** The commando can spend 1 point of grit to negate the -20 penalty on Stealth checks when
sniping until the start of her next turn.

**Camouflage (Ex)**

**Ability:** As long as the commando has 1 point of grit, she gains the _camouflage_
[ranger](ref/class/ranger) class feature: She can use the Stealth skill to hide in any of her
favored terrains, even if the terrain doesn't grant [cover](ref/rule/cover) or
[concealment](ref/rule/concealment).

**Gained:** At 11th Level

**Replaces:** Lightning reload deed

**Hide in Plain Sight (Ex)**

**Ability:** As long as the commando has 1 point of grit, she gains the _hide in plain sight_ ranger
class feature: While in any of her favored terrains, she can use the Stealth skill even while being
observed.

**Gained:** At 15th Level

**Replaces:** Slinger's luck deed

**Favored Terrain (Ex)**

**Ability:** A commando gains the [favored terrain](ref/ability/favored-terrain) ranger class
feature.

**At 10th Level:** She can pick a third favored terrain.

**At 14th Level:** A commando can pick a fourth favored terrain.

**At 18th Level:** The commando can select a fifth favored terrain.

**At 6th Level:** The commando can select a second favored terrain.

**Gained:** At 2nd Level

**Replaces:** Nimble

**Track (Ex)**

**Gained:** At 4th Level

**Passive:** A commando adds half her level on Survival checks to follow tracks.

**Replaces:** The bonus feat gained at 4th level

**Trapsmith**

**Ability:** A commando can learn how to create one ranger trap in place of gaining the next level
of gun training. A commando can use a known trap a number of times per day equal to her Wisdom bonus
(minimum 1). The DC for a commando's trap is equal to 10 + half her commando level + her Wisdom
bonus, and it lasts 1 day per 2 levels she has.

**Alters:** Gun training

**Gained:** At 5th Level

**Special:** A commando can set only extraordinary ranger traps with this ability; as with
extraordinary ranger traps, the trap DC for these traps has a -2 penalty.
