+++
id = "ref/rule/weapon-special-features"
kind = "rule"
title = "Weapon Special Features"
source_ids = ["core-rulebook", "ultimate-combat", "ultimate-equipment"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "weapon_special_features", path = "json/rules_basics02.json" },
]
[[sources]]
publication = "core-rulebook"
page = "144"
[[sources]]
publication = "ultimate-combat"
page = "130, 149"
[[sources]]
publication = "ultimate-equipment"
page = "22"

[fields]
kind = "none"
+++

Some weapons have special features in addition to those noted in their descriptions.

**Blocking:** When you use this weapon to fight defensively, you gain a +1 shield bonus to AC.

**Brace:** If you use a readied action to set a brace weapon against a charge, you deal double
damage on a successful hit against a charging character.

**Broken:** Items that have taken damage in excess of half their total hit points gain the
[broken](ref/misc/broken) condition, meaning they are less effective at their designated task.
Attacks made with a broken weapon suffer a -2 penalty on attack and damage rolls. Such weapons only
score a critical hit on a natural 20 and only deal ×2 damage on a confirmed critical hit. Both
firearms and _fragile_ weapons (see below) include effects that grant a weapon the broken condition
without the weapon explicitly taking damage.

If a weapon gains the broken condition from an effect, that weapon is considered to have taken
damage equal to half its hit points +1. This damage is repaired either by something that addresses
the effect that granted the weapon the broken condition (like quick clear in the case of firearm
misfires or the [Field Repair](ref/feat/field-repair) feat in the case of weapons with the fragile
quality) or by the normal method for recovering item hit points (detailed in the broken condition
description). When an effect that grants the broken condition is removed, the weapon regains the hit
points it lost when the broken condition was applied.

Damage done by an attack against a weapon cannot be repaired by an effect that removes the broken
condition.

**Deadly:** When you use this weapon to deliver a [coup de grace](ref/misc/helpless), it gains a +4
bonus to damage when calculating the DC of the Fortitude saving throw to see whether the target of
the coup de grace dies from the attack. The bonus is not added to the actual damage of the coup de
grace attack.

**Disarm:** When you use a disarm weapon, you get a +2 bonus on Combat Maneuver Checks to
[disarm](ref/rule/disarm) an enemy.

**Distracting:** You gain a +2 bonus on Bluff skill checks to [feint](ref/rule/feint) in combat
while wielding this weapon.

**Double:** You can use a double weapon to fight as if
[fighting with two weapons](ref/rule/two-weapon-fighting), but if you do, you incur all the normal
attack penalties associated with fighting with two weapons, just as if you were using a one-handed
weapon and a light weapon. You can choose to wield one end of a double weapon two-handed, but it
cannot be used as a double weapon when wielded in this way - only one end of the weapon can be used
in any given round.

**Fragile:** Weapons and armor with the fragile quality cannot take the beating that sturdier
weapons can. A fragile weapon gains the _broken_ condition (see above) if the wielder rolls a
natural 1 on an attack roll with the weapon. If a fragile weapon is already broken, the roll of a
natural 1 destroys it instead. Masterwork and magical fragile weapons and armor lack these flaws
unless otherwise noted in the item description or the special material description. If a weapon
gains the broken condition in this way, that weapon is considered to have taken damage equal to half
its hit points +1. This damage is repaired either by something that addresses the effect that
granted the weapon the broken condition (like quick clear in the case of firearm misfires or the
Field Repair feat) or by the repair methods described in the broken condition. When an effect that
grants the broken condition is removed, the weapon regains the hit points it lost when the broken
condition was applied. Damage done by an attack against a weapon (such as from a
[sunder](ref/rule/sunder) combat maneuver) cannot be repaired by an effect that removes the broken
condition.

**Grapple:** On a successful critical hit with a weapon of this type, you can
[grapple](ref/rule/grapple) the target of the attack. The wielder can then attempt a combat maneuver
check to grapple his opponent as a free action. This grapple attempt does not provoke an attack of
opportunity from the creature you are attempting to grapple if that creature is not threatening you.
While you grapple the target with a grappling weapon, you can only move or damage the creature on
your turn. You are still considered [grappled](ref/rule/grapple-conditions), though you do not have
to be adjacent to the creature to continue the grapple. If you move far enough away to be out of the
weapon's reach, you end the grapple with that action.

**Monk:** A monk weapon can be used by a [monk](ref/class/monk) to perform a flurry of blows.

**Nonlethal:** These weapons deal nonlethal damage.

**Performance:** When wielding this weapon, if an attack or combat maneuver made with this weapon
prompts a [combat performance check](ref/rule/performance-combat), you gain a +2 bonus on that
check.

**Reach:** A reach weapon is a melee weapon that allows its wielder to strike at targets that aren't
adjacent to him. Most reach weapons double the wielder's natural reach, meaning that a typical Small
or Medium wielder of such a weapon can attack a creature 10 feet away, but not a creature in an
adjacent square. A typical Large character wielding a reach weapon of the appropriate size can
attack a creature 15 or 20 feet away, but not adjacent creatures or creatures up to 10 feet away.

**Sunder:** When you use a sunder weapon, you get a +2 bonus on Combat Maneuver Checks to sunder
attempts.

**Trip:** You can use any weapon to make [trip](ref/rule/trip) attacks, but if you are tripped
during your own trip attempt, you can drop a trip weapon to avoid being tripped. If the weapon has
any other bonuses that apply during a trip attempt, those bonuses also apply during
[drag](ref/rule/drag) and [reposition](ref/rule/reposition) combat maneuvers.
