+++
id = "ref/rule/siege-engine-qualities"
kind = "rule"
title = "Siege Engine Qualities"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "siege_engine_qualities", path = "json/rules_rulesets02.json" },
]

[fields]
kind = "none"
+++

**Sources:** Ultimate Combat pg 159

The following are the various entries on the equipment tables for siege engines. While ranged siege
engines use most of these entries, close-assault siege engines only use some of them.

**Cost:** This value is the siege engine's cost in gold pieces (gp). The cost includes gear needed
to work the engine as well as gear for upkeep. Typical ammunition costs and weights are given in
siege weapon description.

**Damage:** This column gives the damage typically dealt by the engine. If the engine has a special
mode of attack or damage, this space is marked by the words "see description." If the siege engine
does not deal any damage, but rather is a tool for getting close to or over fortifications, this
entry features a dash (—). Some ranged siege engines can be loaded with special ammunition that
affects or overrides the weapon's typical damage or range.

As large and imprecise weapons, siege engines do not deal [sneak attack](ref/ability/sneak-attack)
damage or any other kind of precision damage.

**Critical:** The entry for this column notes how the engine is used with the rules for critical
hits. Unlike normal ranged weapons, siege engines can deal critical damage to objects as well as
creatures.

**Range:** Any attack at more than the distance listed in this entry is penalized for range. Beyond
this range, the attack or targeting check takes a cumulative -2 penalty for each full range
increment (or fraction thereof) of distance to the target. Some siege engines have a minimum range
for effectiveness. If that is the case, the range of this weapon is followed by a parenthetical with
the minimum range, followed by the abbreviation "min."

**Type:** Like weapons, siege engines that deal damage are classified according to the type of
damage they deal: B for bludgeoning, P for piercing, or S for slashing. Some engines deal damage of
multiple types. Some special siege engines (like the firedrake and the firewyrm) deal energy damage,
typically fire damage. In those cases, the type of energy damage is listed instead.

**Crew:** This column gives the number of creatures needed to properly use the siege engine,
assuming Medium creatures. Some siege engines can be used with a smaller crew, but there are usually
consequences such as slower aiming, firing, or movement.

**Aim:** This column gives the number of full-round actions (or move actions if the crew leader has
the [Master Siege Engineer](ref/feat/master-siege-engineer) feat) required to aim a siege engine. If
the siege engine is being controlled by less than its normal crew complement, the number of actions
it takes for the crew to aim the siege engine is doubled.

**Load:** This column gives the number of full-round actions (or move actions if the crew leader has
the Master Siege Engineer feat) required to load a siege engine.

**Speed:** This is how fast the siege engine can be moved with move actions made by its entire crew.

### Ranged Siege Engines

Ranged siege engines assault structures and people from a distance, by propelling ammunition in some
fashion. Siege engines hurl massive projectiles in one of two ways: direct fire or indirect fire.
Both take a number of actions to load or aim, and the basic rules are described below.

**Load Ammunition:** In order for a ranged siege engine to fire, it needs to be loaded with
ammunition. Loading ammunition takes a number of full-round actions depending on the siege engine
(this time can be reduced to move actions if the crew leader has the
[Master Siege Engineer](ref/feat/master-siege-engineer) feat).

**Aiming a Siege Engine:** Ranged siege engines must be aimed in order to attack a desired target
(in the case of direct-fire siege engines) or square (in the case of indirect-fire siege engines).
Aiming takes a number of full-round actions (or move actions if the crew leader has the Master Siege
Engineer feat), with the number depending on the specific siege engine. Aiming a siege engine with a
diminished crew doubles the amount of time it takes to aim the siege engine. Each time a new target
or square is chosen as the target of a siege engine's attack, that engine must be aimed anew.

**Direct-Fire Ranged Siege Engines:** Direct-fire weapons launch their projectiles on a relatively
flat trajectory, allowing them to more easily target creatures or pummel barriers directly in front
of them.

A direct-fire weapon uses a normal attack roll, with the normal penalty for nonproficient use. In
addition, a direct-fire weapon takes a -2 attack roll penalty per size category that the weapon is
larger than the creature aiming it. Creatures that have ranks in Knowledge (engineering) are not
adversely affected by their size when firing direct-fire ranged siege engines.

Sheer manpower can also reduce the penalties for size. Increasing the crew of these weapons by 1 or
more can reduce the attack roll penalty for creature size: as long as an extra crew member is no
smaller than three size categories smaller than the direct-fire weapon, it can reduce the penalty
due to the aiming creature's size by 2. For example, a Huge ballista fired by a Medium creature that
is part of a crew of two (the creature aiming the ballista and someone to help position it) takes
only a -2 penalty on attack rolls.

**Indirect-Fire Ranged Siege Engines:** Indirect-fire weapons launch projectiles in high arcs toward
their targets. They typically lob heavier missiles and payloads than direct-fire weapons, but they
are harder to aim accurately. Indirect weapons can bypass many forms of fortification, delivering
their payloads of solid shot, scatter shot, or even disease-ridden offal to targets beyond the walls
of castles. They can also be used to batter fortifications where they are most vulnerable, arcing
down on towers and walls, crushing them with the weight of stone or raining down smaller projectiles
on a wall's defenders.

Indirect-fire weapons use a targeting mechanic similar to that described for catapults in the Core
Rulebook, hereafter referred to as an indirect attack. The following is an update to those rules.

**Indirect Attack:** To fire an indirect-fire ranged siege engine, the crew leader makes a targeting
check against the DC of the siege engine. This check uses his base attack bonus, his Intelligence
modifier (if not trained in Knowledge \[engineering\]) or Knowledge (engineering) skill modifier (if
trained in that skill), any penalty for not being proficient in the siege engine, and the
appropriate modifiers from Table 3-12. If the check succeeds, the ammunition of the indirect attack
hits the square the siege engine was aimed at, dealing the indicated damage or effect to any object
or creature within the area of its attack. Creatures may get a saving throw to limit the effect of
the attack; this is typically based on the type of ammunition used.

If the attack misses the intended square, roll 1d8 to determine in what direction the shot veers. A
roll of 1 indicates the ammunition falls short (toward the siege engine), with rolls of 2 through 8
counting squares clockwise around the target square. Roll 1d4 for every range increment at which the
attack was made (1d4 if the target square is within the engine's first range increment, 2d4 if the
target square is within the second range increment, and so on). The total is the number of squares
by which the attack misses, with the direction in which the squares are counted determined by the d8
roll. The ammunition deals its damage and any other effects in the square it lands on.

|Condition|Modifier|
| --- | --- |
|No line of sight to target square|-6|
|Successive shots (crew can see where most recent miss landed)|Cumulative +2 per previous miss (maximum +10)|
|Successive shots (crew can't see where most recent miss landed, but observer is providing feedback)|Cumulative +1 per previous miss (maximum +5)|
|Successive shots after hit|+10|

### Close-Assault Siege Engines

While most siege engines attack at range, some are used up close to directly undermine defenses,
batter through them, or otherwise bypass them. Some close assault weapons are not even weapons at
all, but instead provide means for assault forces to protect themselves or circumvent fortifications
without destroying them.

### Ammunition

Ammunition can be used either in select types of indirect-fire siege engines, or with cannons. The
ammunition description specifies which types of siege engines use the special ammunition. The costs
and weights presented are for individual uses of special ammunition.
