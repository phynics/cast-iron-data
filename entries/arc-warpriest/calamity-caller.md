+++
id = "ref/arc-warpriest/calamity-caller"
kind = "archetype"
title = "Calamity Caller"
source_ids = ["heroes-from-the-fringe"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "calamity_caller", path = "json/archetypes_warpriest.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/warpriest" },
]

[fields]
kind = "none"
+++

**Sources:** Heroes from the Fringe pg 12\
While all elves feel a deep connection to nature, some elven priests take this bond further, using
their link to call down the wrath of nature upon their enemies. Ekujae are most inclined to harness
this connection, but any elf can wield their bond to nature in this way.

**Prerequisites:** Elf

**Catastrophic Blessing**

**Ability:** A calamity caller must select a disaster blessing
([Earthquake](ref/blessing/earthquake), [Flood](ref/blessing/flood),
[Tornado](ref/blessing/tornado), or [Wildfire](ref/blessing/wildfire)) as one of his two blessings,
even if the calamity caller's deity does not grant the disaster blessing's associated domain.

**Alters:** Blessings

**Calamity (Su)**

**At 12th Level:** Enhanced effects now persist for 2 additional rounds.

**At 16th Level:** Enhanced effects now persist for 3 additional rounds.

**At 4th Level:** A calamity caller can create an enhanced calamity when he uses this ability. An
enhanced calamity deals twice the calamity's normal damage; in addition, a creature that fails its
save suffers an additional effect (see below). A creature must take damage from the calamity to
suffer these additional effects. The calamity caller can create an _enhanced calamity_ a number of
times per day equal to [half](ref/misc/fractions-and-rounding) of his warpriest level.

**At 8th Level:** Effects created by an _enhanced calamity_ that last for 1 or more rounds persist
for 1 additional round.

**Replaces:** Focus weapon, sacred weapon, bonus feats

**Special:** The calamities available to calamity callers, the type of damage they deal, the saving
throw to resist the damage, and the secondary effect they cause when enhanced, are listed below.

**Standard:** A calamity caller can cause a 5-foot square within 30 feet to suffer a calamity. A
calamity deals 1d6 damage to creatures within that square. The type of calamity determines what type
of damage the calamity deals (see below). An affected creature can attempt a saving throw to reduce
this damage by half (DC = 10 + half the calamity caller's warpriest level + the calamity caller's
Wisdom modifier); the type of save is determined by the calamity. The calamity caller can use this
ability at will.

At 3rd level: The amount of damage 2d6.

At 5th level: The amount of damage 3d6.

At 7th level: The amount of damage 4d6.

At 9th level: The amount of damage 5d6.

At 11th level: The amount of damage 6d6.

At 13th level: The amount of damage 7d6.

At 15th level: The amount of damage 8d6.

At 17th level: The amount of damage 9d6.

At 19th level: The amount of damage 10d6.

**Acid Rain**

**Ability:** A brief rain shower deals acid damage to the target square, with a Fortitude save for
half damage. A creature that fails its save against _enhanced_ acid rain continues to dissolve for 1
round, automatically taking half the original damage.

**Blizzard**

**Ability:** Hail deals cold damage to the target square, with a Fortitude save for half damage. A
creature that fails its save against an _enhanced_ blizzard is [blinded](ref/misc/blinded) for 1
round.

**Deadfall**

**Ability:** A tree branch, stone boulder, or other heavy object falls on the target square. A
deadfall deals bludgeoning damage, with a Reflex save for half damage. A creature that fails its
save against an _enhanced_ deadfall is knocked [prone](ref/rule/prone).

**At 12th Level:** The target is also [confused](ref/misc/confused) for 1 round.

**Flash Flood**

**Ability:** A brief surge of stormy water deals bludgeoning damage to the target square, with a
Reflex save for half damage. An _enhanced_ flash flood does not cause additional effects; instead,
an _enhanced_ flash flood targets creatures in a 5-foot radius.

**At 12th Level:** The area increases to a 10-foot radius.

**At 16th Level:** The area increases to a 15-foot radius.

**Lightning Strike**

**Ability:** A bolt of lightning deals electricity damage to the target square, with a Reflex save
for half damage. A creature that fails its save against an _enhanced_ lightning strike is
[staggered](ref/misc/staggered) for 1 round by electrical impulses.

**Thorny Vines**

**Ability:** Vines covered with thick thorns wrap around the target square. The thorny vines deal
piercing damage, with a Reflex save for half damage. A creature that fails its save against
_enhanced_ thorny vines is [entangled](ref/rule/entangled) for 1 round.

**Volcanic Rift**

**Ability:** A magmatic rift emits a plume of fire into the air, dealing fire damage to the target
square, with a Fortitude save for half damage. An _enhanced_ volcanic rift also emits poisonous and
corrosive gases; a creature that fails its save against the _enhanced_ volcanic rift is
[sickened](ref/misc/sickened) for 1 round.

**Aspect of Disaster (Su)**

**Gained:** At 20th Level

**Passive:** A creature affected by a calamity caller's _enhanced calamity_ does not receive a save
to reduce the damage or avoid the calamity's effects.

**Replaces:** Aspect of war
