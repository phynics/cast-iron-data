+++
id = "ref/arc-vigilante/gunmaster"
kind = "archetype"
title = "Gunmaster"
source_ids = ["ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "gunmaster", path = "json/archetypes_vigilante.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/vigilante" },
]

[fields]
kind = "archetype"
replaces = ["Vigilante specialization", "Unshakable"]
alters = ["Weapon and armor proficiencies", "Vigilante talents"]
+++

**Sources:** Ultimate Intrigue pg 57\
Firearms can be potent tools for striking fear into the hearts of enemies, and canny vigilantes use
this to their advantage. Gunmasters brandish firearms like extensions of their will, taking down
their foes with deadly accuracy and skill.

**Weapon and Armor Proficiencies**

**Alters:** Weapon and armor proficiencies

**Info:** A gunmaster is proficient with all firearms but not with martial weapons or medium armor.

**Gunmaster**

**Ability:** A gunmaster gains the [gunslinger's](ref/class/gunslinger) gunsmith ability.
Additionally, the [Gunsmithing](ref/feat/gunsmithing) bonus feat allows the gunmaster to repair and
restore his initial battered firearm as if he were a gunslinger.

**At 5th Level:** The gunmaster gains a +1 bonus on attack and damage rolls with all firearms.

**Replaces:** Vigilante specialization

At 9th level: This bonus +2.

At 13th level: This bonus +3.

At 17th level: This bonus +4.

**Gunsmith**

**Ability:** You gain [Gunsmithing](ref/feat/gunsmithing) as a bonus feat, and one of the following
firearms of your choice: [blunderbuss](ref/eq-weapon/blunderbuss), [musket](ref/eq-weapon/musket),
or [pistol](ref/eq-weapon/pistol). Your starting weapon is battered, and only you know how to use it
properly. All other creatures treat your gun as if it had the [broken](ref/misc/broken) condition.
If the weapon already has the broken condition, it does not work at all for anyone else trying to
use it.

**Flavor:** Text from the gunslinger class ability.

**Special:** This starting weapon can only be sold for scrap (it's worth 4d10 gp when sold).

**Gunmaster Talents**

**Alters:** Vigilante talents

**Info:** A gunmaster can select from any of the following vigilante talents, in addition to general
vigilante talents.

**Deadeye (Ex)**

**Ability:** The gunmaster can resolve an attack against touch AC instead of normal AC when firing
one increment beyond his firearm's first range increment. The gunmaster still takes the -2 penalty
on attack rolls for shooting a target outside the firearm's first range increment.

**Special:** A gunmaster can spend multiple daily uses to resolve an attack at a further range
increment (for instance, he can spend three uses to resolve an attack three increments beyond his
first range increment).

**Usage:** 1 time/day + 1 per 4 vigilante levels beyond 2nd

**Death's Shot (Ex)**

**Immediate:** Three times per day, when the gunmaster scores a critical hit, he can attempt to kill
his enemy instantly. When the gunmaster uses this talent, the target must succeed at a Fortitude
saving throw with a DC equal to 10 + 1/2 the gunmaster's vigilante level + his Dexterity modifier.
On a failed saving throw, the target dies instantly.

**Prereq:** 20th-level vigilante

**Gunmaster Initiative (Ex)**

**Ability:** The gunmaster gains a +2 bonus on initiative checks. Furthermore, if he has the
[Quick Draw](ref/feat/quick-draw) feat, his hands are free and unrestrained, and the firearm is not
hidden, he can draw a single firearm as part of the initiative check.

**Prereq:** 4th-level vigilante

**Lightning Reload (Ex)**

**Prereq:** 12th-level vigilante

**Provokes attack of opportunity:** No

**Swift:** A gunmaster can reload a single barrel of a one-handed or two-handed firearm once per
round. If he has the [Rapid Reload](ref/feat/rapid-reload) feat or is using an alchemical cartridge
(or both), he can reload a single barrel of the weapon as a **free action** each round instead.

**Usage:** 1 time/day per 2 vigilante levels

**Quick Clear (Ex)**

**At 12th Level:** Once per day, when the gunmaster rolls a misfire with a gun that has the broken
condition, she can prevent the gun from exploding, though it retains the broken condition.

**Standard:** Once per day, the gunmaster can remove the broken condition from a single firearm he
is currently wielding, as long as that condition was gained by a firearm misfire.

**Nimble (Ex)**

**Gained:** At 4th Level

**Passive:** A gunmaster gains a +1 dodge bonus to AC while wearing light or no armor. Anything that
causes the gunmaster to lose her Dexterity bonus to AC also causes the gunmaster to lose this dodge
bonus.

**Replaces:** Unshakable

At 10th level: This bonus +2.

At 14th level: This bonus +3.

At 18th level: This bonus +4.
