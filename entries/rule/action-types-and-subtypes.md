+++
id = "ref/rule/action-types-and-subtypes"
kind = "rule"
title = "Action Types and Subtypes"
source_ids = ["pathfinder-unchained"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "action_types_and_subtypes", path = "json/rules_opt_combat01.json" },
]
[[sources]]
publication = "pathfinder-unchained"
page = "102"

[fields]
kind = "none"
+++

This section describes the various actions in the game, their costs within this system, and new
rules on how each one works.

There are a number of different simple actions, free actions, and advanced actions you can take
during your turn. Taking a simple action requires 1 act. Free actions don't cost any acts; you just
say you want to take them, though some must be taken alongside other simple or advanced actions. In
addition, the GM may limit the number of free actions you're allowed during your turn.

Advanced actions are more complicated; you must commit 2 or more acts to perform them. Some advanced
actions require more acts than you can possibly commit during a single turn. In this case, you must
continue committing acts toward that advanced action over multiple turns until the advanced action
is complete. To take most advanced actions, you must commit all of their requisite acts
consecutively. If you stop committing acts toward such an advanced action, it never comes to
completion, and it must be started all over again in order to have a chance of success. Other
advanced actions can be completed after committing the total requisite number of acts, which can be
split up over time. In both cases, any roll attempted to determine whether an advanced action is
successful is attempted after the appropriate number of acts are committed to that advanced action
by the creature committing the final act. If an advanced action doesn't say whether it requires
consecutive or non-consecutive acts, all its acts must be consecutive.

Some actions and reactions have one or more of the following subtypes. The subtypes are thematic,
sometimes affect other actions taken later in the turn, and are used to determine whether (and at
what point) an action provokes attacks of opportunity.

**Attack Actions:** Actions with the attack subtype involve making at least one attack roll against
an opponent or object. They typically provoke attacks of opportunity only if the attack is a ranged
attack or you don't have the appropriate feat to take that attack action without provoking attacks
of opportunity, such as [Improved Unarmed Strike](ref/feat/improved-unarmed-strike) for unarmed
strikes or [Improved Trip](ref/feat/improved-trip) for trip attempts. In the latter case, the action
provokes an attack of opportunity only from the creature you target. When an attack action provokes
an attack of opportunity, the attack of opportunity is made before the provoking attack roll is
made.

The first time during your turn that you take an action with this subtype, you roll the attack as
normal. Each subsequent attack action taken during your turn imposes a cumulative -5 penalty on the
attack roll or combat maneuver check (so the second attack action has a -5 penalty on the attack
roll, the third has a -10 penalty, and so on).

**Complex Actions:** These actions involve intense concentration, strenuous physical manipulation of
objects, or some other source of complexity. A complex action always provokes attacks of
opportunity, which are made before the complex action is taken. Complex actions that occur over
multiple turns (whether consecutively or not) provoke attacks of opportunity on each turn that acts
are committed toward their completion.

**Move Actions:** These actions involve moving through the encounter area in some way. Actions with
the move subtype provoke attacks of opportunity when you attempt to either leave a square in an
enemy's threatened area or stand up from a prone position in a space that has at least 1 square in a
foe's threatened area. Not all actions that allow you to move have the move subtype. For example, a
step is a very slow and careful movement that doesn't have this subtype, and thus doesn't provoke
attacks of opportunity when you take that action to leave a square in a threatened area.

Actions without a Subtype: Actions without a subtype don't provoke attacks of opportunity.

## Two-Weapon Fighting and Flurry of Blows

When you fight with a second weapon in your off hand or with a double weapon, you can make two
attacks with the first attack simple action you take during your turn: one with your primary hand
and another with your off hand. You take penalties on these attack rolls as listed on
[Table 8-7: Two-Weapon Fighting Penalties](ref/rule/two-weapon-fighting). Any other attack simple
actions you take during your turn allow only one attack roll, using either the weapon in your
primary hand or the one in your off hand.

If you have the [Improved Two-Weapon Fighting](ref/feat/improved-two-weapon-fighting) feat, you can
make two attack rolls on both the first and second attack simple actions taken during your turn;
both of the attacks made on the second attack action are made at a -5 penalty. Further attack simple
actions taken during the same turn allow only one attack roll, using either the weapon in your
primary hand or the one in your off hand.

If you have the [Greater Two-Weapon Fighting](ref/feat/greater-two-weapon-fighting) feat, you can
make two attacks on each of your attack simple actions on your turn, though you take all the normal
penalties for two-weapon fighting, as well as the cumulative -5 penalty per attack simple action
(all attacks made as part of the same attack action have the same penalty).

The [flurry of blows class feature](ref/class/monk) works in a similar way. At 1st level, you can
make an additional attack with a -2 penalty on your first attack simple action during a turn. At 8th
level, you can make an additional attack on both your first and second attack simple actions during
your turn. At 15th level, you can make an additional attack on each of your attack simple actions
during your turn. You must, of course, take all the penalties associated with those attacks.
