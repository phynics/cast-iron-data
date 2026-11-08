+++
id = "ref/arc-fighter/phalanx-soldier"
kind = "archetype"
title = "Phalanx Soldier"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "phalanx_soldier", path = "json/archetypes_fighter2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/fighter" },
]

[fields]
kind = "archetype"
replaces = ["Bravery", "Armor training 1", "Weapon training 1", "Armor training 2 and 3", "Weapon training 2, 3, and 4", "Armor training 4", "Weapon mastery"]
+++

**Sources:** Advanced Player's Guide pg 105\
The phalanx soldier specializes in defensive tactics, using his shield to guard himself and his
allies and forming a shield wall like an unbreakable anvil against which his enemies break.

**Stand Firm (Ex)**

**Gained:** At 2nd Level

**Passive:** A phalanx soldier gains a +1 bonus to CMD against [bull rush](ref/rule/bull-rush),
[overrun](ref/rule/overrun), and [trip](ref/rule/trip) attempts. This bonus also applies on saves
against [trample](ref/umr/trample) attacks.

**Replaces:** Bravery

At 6th level: The bonus +2.

At 10th level: The bonus +3.

At 14th level: The bonus +4.

At 18th level: The bonus +5.

**Phalanx Fighting (Ex)**

**Ability:** When a phalanx soldier wields a shield, he can use any polearm or spear of his size as
a one-handed weapon.

**Gained:** At 3rd Level

**Replaces:** Armor training 1

**Ready Pike (Ex)**

**Immediate:** A phalanx soldier can [ready](ref/rule/ready) a weapon with the
[brace](ref/misc/brace) property, gaining a +1 bonus on attack and damage rolls.

**Gained:** At 5th Level

**Replaces:** Weapon training 1

**Special:** He cannot use this ability when [flat-footed](ref/rule/flat-footed).

**Usage:** 1 time/day + 1 per 4 fighter levels beyond 5th

At 9th level: This bonus +2.

At 13th level: This bonus +3.

At 17th level: This bonus +4.

**Deft Shield (Ex)**

**At 11th Level:** These penalties are reduced by 2.

**Gained:** At 7th Level

**Passive:** The armor check penalty from a shield and the attack roll penalty are reduced by 1 for
a phalanx soldier using a [tower shield](ref/eq-armor/tower-shield).

**Replaces:** Armor training 2 and 3

**Shield Ally (Ex)**

**At 13th Level:** He can instead provide cover (+4 cover bonus to AC, +2 bonus on Reflex saves) and
[evasion](ref/ability/evasion) (as a [rogue](ref/class/rogue)) to one adjacent ally until the
beginning of his next turn. This cover does not allow Stealth checks.

**At 17th Level:** He can provide cover to himself and all adjacent allies, or he can provide
improved cover (+8 cover bonus to AC, +4 bonus on Reflex saves,
[improved evasion](ref/ability/improved-evasion)) to a single adjacent ally.

**Gained:** At 9th Level

**Move:** When a phalanx fighter is using a heavy or tower shield, he can provide partial
[cover](ref/rule/cover) (+2 cover bonus to AC, +1 bonus on Reflex saves) to himself and all adjacent
allies until the beginning of his next turn.

**Replaces:** Weapon training 2, 3, and 4

**Irresistible Advance (Ex)**

**Gained:** At 15th Level

**Passive:** A phalanx fighter gains a bonus on bull rush and overrun CMB checks. This bonus depends
on the type of shield used: +1 with a buckler, +2 with a light shield, +3 with a heavy shield, or +4
with a tower shield.

**Replaces:** Armor training 4

**Shielded Fortress (Ex)**

**Immediate:** He can provide _improved evasion_ to an adjacent ally against one attack.

**Gained:** At 20th Level

**Move:** A phalanx fighter can provide _evasion_ to all adjacent allies until the beginning of his
next turn.

**Passive:** A phalanx fighter's shield cannot be [disarmed](ref/rule/disarm) or
[sundered](ref/rule/sunder). He gains _evasion_ (as a rogue) when using a shield (_improved evasion_
when using a tower shield).

**Replaces:** Weapon mastery
