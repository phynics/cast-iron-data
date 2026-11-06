+++
id = "ref/rule/weapon-descriptions"
kind = "rule"
title = "Weapon Descriptions"
source_ids = ["core-rulebook", "ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "weapon_descriptions", path = "json/rules_basics02.json" },
]

[fields]
kind = "none"
+++

**Sources:** PRPG Core Rulebook pg 144, Ultimate Combat pg 137

**Cost:** This value is the weapon's cost in gold pieces (gp) or silver pieces (sp). The cost
includes miscellaneous gear that goes with the weapon, such as a scabbard or quiver. This cost is
the same for a Small or Medium version of the weapon. A Large version costs twice the listed price.

**Dmg:** These columns give the damage dealt by the weapon on a successful hit. The column labeled
**Dmg (S)** is for Small weapons. The column labeled **Dmg (M)** is for Medium weapons. If two
damage ranges are given, then the weapon is a double weapon. Use the second damage figure given for
the double weapon's extra attack. Table 6-5 gives weapon damage values for Tiny and Large weapons.

### Table 6-5: Tiny and Large Weapon Damage

|Tiny Weapon Damage|Small Weapon Damage|Medium Weapon Damage|Large Weapon Damage|
| --- | --- | --- | --- |
|-|1|1d2|1d3|
|1|1d2|1d3|1d4|
|1d2|1d3|1d4|1d6|
|1d3|1d4|1d6|1d8|
|1d4|1d6|1d8|2d6|
|1d4|1d6|2d4|2d6|
|1d6|1d8|1d10|2d8|
|1d8|1d10|1d12|3d6|
|1d8|1d10|2d6|3d6|
|1d10|2d6|2d8|3d8|
|2d6|2d8|2d10|4d8|

**Critical:** The entry in this column notes how the weapon is used with the rules for critical
hits. When your character scores a critical hit, roll the damage two, three, or four times, as
indicated by its critical multiplier (using all applicable modifiers on each roll), and add all the
results together.

Extra damage over and above a weapon's normal damage is not multiplied when you score a critical
hit.

> **×2:** The weapon deals double damage on a critical hit.
>
> **×3:** The weapon deals triple damage on a critical hit.
>
> **×3/×4:** One head of this double weapon deals triple damage on a critical hit. The other head
> deals quadruple damage on a critical hit.
>
> **×4:** The weapon deals quadruple damage on a critical hit.
>
> **19-20/×2:** The weapon scores a threat on a natural roll of 19 or 20 (instead of just 20) and
> deals double damage on a critical hit.
>
> **18-20/×2:** The weapon scores a threat on a natural roll of 18, 19, or 20 (instead of just 20)
> and deals double damage on a critical hit.

**Range:** Any attack at more than this distance is penalized for range. Beyond this range, the
attack takes a cumulative -2 penalty for each full range increment (or fraction thereof) of distance
to the target. For example, a dagger (with a range of 10 feet) thrown at a target that is 25 feet
away would incur a -4 penalty. A thrown weapon has a maximum range of five range increments. A
projectile weapon can shoot to 10 range increments.

**Weight:** This column gives the weight of a Medium version of the weapon. Halve this number for
Small weapons and double it for Large weapons. Some weapons have a special weight. See the weapon's
description for details.

**Type:** Weapons are classified according to the type of damage they deal: B for bludgeoning, P for
piercing, or S for slashing. Some monsters may be resistant or immune to attacks from certain types
of weapons.

Some weapons deal damage of multiple types. If a weapon causes two types of damage, the type it
deals is not half one type and half another; all damage caused is of both types. Therefore, a
creature would have to be immune to both types of damage to ignore any of the damage caused by such
a weapon.

In other cases, a weapon can deal either of two types of damage. In a situation where the damage
type is significant, the wielder can choose which type of damage to deal with such a weapon.

**Scatter:** A weapon with the scatter weapon quality can shoot two different types of ammunition.
It can fire normal bullets that target one creature, or it can make a scattering shot, attacking all
creatures within a cone. Cannons with the scatter weapon quality only fire grapeshot, unless their
descriptions state otherwise. When a scatter weapon attacks all creatures within a cone, it makes a
separate attack roll against each creature within the cone. Each attack roll takes a -2 penalty, and
its attack damage cannot be modified by precision damage or damage-increasing feats such as
[Vital Strike](ref/feat/vital-strike). Effects that grant [concealment](ref/rule/concealment), such
as fog or smoke, or the [blur](ref/spell/blur), [invisibility](ref/spell/invisibility), or
[mirror image](ref/spell/mirror-image) spells, do not foil a scatter attack. If any of the attack
rolls threaten a critical, confirm the critical for that attack roll alone. A firearm that makes a
scatter shot misfires only if all of the attack rolls made misfire. If a scatter weapon explodes on
a misfire, it deals triple its damage to all creatures within the misfire radius.
