+++
id = "ref/rule/siege-engines"
kind = "rule"
title = "Siege Engines"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "siege_engines", path = "json/rules_gm08.json" },
]

[fields]
kind = "none"
+++

**Sources:** PRPG Core Rulebook pg 434

Siege engines are large weapons, temporary structures, or pieces of equipment traditionally used in
besieging castles or fortresses.

_Also see [here](ref/rule/siege-engines-uc) for updated rules on siege engines._

Siege engines are treated as difficult devices if someone tries to disable them using Disable
Device. This takes 2d4 rounds and requires a DC 20 Disable Device check. Siege engines are typically
made out of wood and have an AC of 3 (-5 Dex, -2 size), a [Hardness](ref/umr/hardness) of 5, and 80
hit points. Siege engines made up of a different material might have different values. Some siege
engines are armored as well. Treat the siege engine as a Huge creature to determine the cost of such
armor. Siege engines can be crafted as masterwork and enchanted as magic weapons, adding bonuses on
attack rolls to the checks made to hit with the siege engine. A masterwork siege engine costs 300 gp
more than the listed price. Enchanting a siege engine costs twice the normal amount. For example, a
+1 flaming heavy catapult, armored with full plate, would have an AC of 11 and would cost 23,100 gp
(800 gp base + 6,000 gp for the armor + 300 gp masterwork + 16,000 gp for the enhancements).

**Catapult, Heavy:** A [heavy catapult](ref/eq-siegeengine/catapult-heavy) is a massive engine
capable of throwing rocks or heavy objects with great force. Because the catapult throws its payload
in a high arc, it can hit squares out of its line of sight. To fire a heavy catapult, the crew chief
makes a special check against DC 15 using only his base attack bonus, Intelligence modifier, range
increment penalty, and the appropriate modifiers from the lower section of Table 13-8. If the check
succeeds, the catapult stone hits the square the catapult was aimed at, dealing the indicated damage
to any object or character in the square. Characters who succeed on a DC 15 Reflex save take half
damage. Once a catapult stone hits a square, subsequent shots hit the same square unless the
catapult is reaimed or the wind changes direction or speed.

If a catapult stone misses, roll 1d8 to determine where it lands. This determines the misdirection
of the throw, with 1 being back toward the catapult and 2 through 8 counting clockwise around the
target square. Finally, count 1d4 squares away from the target square for every range increment of
the attack.

Loading a catapult requires a series of full-round actions. It takes a DC 15 Strength check to winch
the throwing arm down; most catapults have wheels to allow up to two crew members to use the aid
another action, assisting the main winch operator. A DC 15 Profession (siege engineer) check latches
the arm into place, and then another DC 15 Profession (siege engineer) check loads the catapult
ammunition. It takes four full-round actions to reaim a heavy catapult (multiple crew members can
perform these full-round actions in the same round, so it would take a crew of four only 1 round to
reaim the catapult).

A heavy catapult takes up a space 15 feet across.

### Catapult Attack Modifiers

|Condition|Modifier|
| --- | --- |
|No line of sight to target square|-6|
|Successive shots (crew can see where most recent misses landed)|Cumulative +2 per previous miss (maximum +10)|
|Successive shots (crew can't see where most recent misses landed, but observer is providing feedback)|Cumulative +1 per previous miss (maximum +5)|

**Catapult, Light:** This is a smaller, [lighter](ref/eq-siegeengine/catapult-light) version of the
heavy catapult. It functions as the heavy catapult, except that it takes a DC 10 Strength check to
winch the arm into place, and only two full-round actions are required to reaim the catapult.

A light catapult takes up a space 10 feet across.

**Ballista:** A [ballista](ref/eq-siegeengine/ballista-heavy) is essentially a Huge heavy crossbow
fixed in place. Its size makes it hard for most creatures to aim it. Thus, a Medium creature takes a
-4 penalty on attack rolls when using a ballista, and a Small creature takes a -6 penalty. It takes
a creature smaller than Large two full-round actions to reload the ballista after firing.

A ballista takes up a space 5 feet across.

**Ram:** This [heavy pole](ref/eq-siegeengine/ram-large) is sometimes suspended from a movable
scaffold that allows the crew to swing it back and forth against objects. As a full-round action,
the character closest to the front of the ram makes an attack roll against the AC of the
construction, applying the -4 penalty for lack of proficiency. It's not possible to be proficient
with this device. In addition to the damage given on Table 13-8, up to nine other characters holding
the ram can add their Strength modifiers to the ram's damage, if they devote an attack action to
doing so. It takes at least one Huge or larger creature, two Large creatures, four Medium creatures,
or eight Small creatures to swing a ram.

A ram is typically 30 feet long. In a battle, the creatures wielding the ram stand in two adjacent
columns of equal length, with the ram between them.

**Siege Tower:** This device is a massive wooden tower on wheels or rollers that can be rolled up
against a wall to allow attackers to scale the tower and thus get to the top of the wall with cover.
The wooden walls are usually 1 foot thick.

A typical [siege tower](ref/eq-siegeengine/siege-tower-large) takes up a space 15 feet across. The
creatures inside push it at a base land speed of 10 feet (and a siege tower can't run). The eight
creatures pushing on the ground floor have total cover, and those on higher floors get improved
cover and can fire through arrow slits.

### Table 13-8: Siege Engines

|Item|Cost|Damage|Critical|Range Increment|Typical Crew|
| --- | --- | --- | --- | --- | --- |
|[Catapult, heavy](ref/eq-siegeengine/catapult-heavy)|800 gp|6d6|-|200 ft. (100 ft. minimum)|4|
|[Catapult, light](ref/eq-siegeengine/catapult-light)|550 gp|4d6|-|150 ft. (100 ft. minimum)|2|
|[Ballista](ref/eq-siegeengine/ballista-heavy)|500 gp|3d8|19-20|120 ft.|1|
|[Ram](ref/eq-siegeengine/ram-large)|1,000 gp|3d6\*|-|-|10|
|[Siege tower](ref/eq-siegeengine/siege-tower-large)|2,000 gp|-|-|-|20|

\* See description for special rules.\
All siege weapons are listed here.
