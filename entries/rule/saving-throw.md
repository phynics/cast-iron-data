+++
id = "ref/rule/saving-throw"
kind = "rule"
title = "Saving Throw"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "saving_throw", path = "json/rules_basics04.json" },
]

[fields]
kind = "none"
+++

**Sources:** PRPG Core Rulebook pg 216

Usually a harmful spell allows a target to make a saving throw to avoid some or all of the effect.
The saving throw entry in a spell description defines which type of saving throw the spell allows
and describes how saving throws against the spell work.

**Negates:** The spell has no effect on a subject that makes a successful saving throw.

**Partial:** The spell has an effect on its subject. A successful saving throw means that some
lesser effect occurs.

**Half:** The spell deals damage, and a successful saving throw halves the damage taken (round
down).

**None:** No saving throw is allowed.

**Disbelief:** A successful save lets the subject ignore the spell's effect.

**(object):** The spell can be cast on objects, which receive saving throws only if they are magical
or if they are attended (held, worn, grasped, or the like) by a creature resisting the spell, in
which case the object uses the creature's saving throw bonus unless its own bonus is greater. This
notation does not mean that a spell can be cast only on objects. Some spells of this sort can be
cast on creatures or objects. A magic item's saving throw bonuses are each equal to 2 + 1/2 the
item's caster level.

**(harmless):** The spell is usually beneficial, not harmful, but a targeted creature can attempt a
saving throw if it desires.

**Saving Throw Difficulty Class:** A saving throw against your spell has a DC of 10 + the level of
the spell + your bonus for the relevant ability (Intelligence for a wizard, Charisma for a bard,
paladin, or sorcerer, or Wisdom for a cleric, druid, or ranger). A spell's level can vary depending
on your class. Always use the spell level applicable to your class.

**Succeeding on a Saving Throw:** A creature that successfully saves against a spell that has no
obvious physical effects feels a hostile force or a tingle, but cannot deduce the exact nature of
the attack. Likewise, if a creature's saving throw succeeds against a targeted spell, you sense that
the spell has failed. You do not sense when creatures succeed on saves against effect and area
spells.

**Automatic Failures and Successes:** A natural 1 (the d20 comes up 1) on a saving throw is always a
failure, and the spell may cause damage to exposed items (see Items Surviving after a Saving Throw,
below). A natural 20 (the d20 comes up 20) is always a success.

**Voluntarily Giving up a Saving Throw:** A creature can voluntarily forego a saving throw and
willingly accept a spell's result. Even a character with a special resistance to magic can suppress
this quality.

**Items Surviving after a Saving Throw:** Unless the descriptive text for the spell specifies
otherwise, all items carried or worn by a creature are assumed to survive a magical attack. If a
creature rolls a natural 1 on its saving throw against the effect, however, an exposed item is
harmed (if the attack can harm objects). Refer to Table 9-2: Items Affected by Magical Attacks.
Determine which four objects carried or worn by the creature are most likely to be affected and roll
randomly among them. The randomly determined item must make a saving throw against the attack form
and take whatever damage the attack dealt. If the selected item is not carried or worn and is not
magical, it does not get a saving throw. It simply is dealt the appropriate damage.

### Table 9-2: Items Affected by Magical Attacks

|Order\*|Item|
| --- | --- |
|1st|Shield|
|2nd|Armor|
|3rd|Magic helmet, hat, or headband|
|4th|Item in hand (including weapon, wand, or the like)|
|5th|Magic cloak|
|6th|Stowed or sheathed weapon|
|7th|Magic bracers|
|8th|Magic clothing|
|9th|Magic jewelry (including rings)|
|10th|Anything else|
