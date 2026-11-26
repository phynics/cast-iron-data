+++
id = "ref/arc-ranger/poison-darter"
kind = "archetype"
title = "Poison Darter"
aon = "ArchetypeDisplay.aspx?FixedName=Ranger%20Poison%20Darter"
source_ids = ["blood-of-the-beast"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "poison_darter", path = "json/archetypes_ranger.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/ranger" },
]
[[sources]]
publication = "blood-of-the-beast"
page = "9"

[fields]
kind = "archetype"
features = [
  { anchor = "debilitating-venom" },
  { anchor = "poison-use", level = 1 },
  { anchor = "poison-style", level = 2 },
  { anchor = "precise-dart", level = 4 },
]
trades = [
  { replaces = "Favored enemy", feature = "favored-enemy", by = ["debilitating-venom"] },
  { replaces = "master hunter", feature = "master-hunter", by = ["debilitating-venom"] },
  { replaces = "Wild empathy", feature = "wild-empathy", by = ["poison-use"] },
  { replaces = "Hunter's bond", feature = "hunter-s-bond", by = ["precise-dart"] },
  { alters = "Combat style feat", feature = "combat-style-feat", by = ["poison-style"] },
]
+++

In dense jungles, foliage and tight spaces hinder all but the most deceptively humble weapons:
[blowguns](ref/eq-weapon/blowgun) and poison.

## Debilitating Venom (Ex) {#debilitating-venom}

A poison darter can concoct potent toxins that he can apply to his weapons. He can use this ability
a number of times per day equal to 1/2 his ranger level + his Wisdom modifier; if he has the toxic
skin alternate racial trait (_Pathfinder RPG Advanced Race Guide_ 190), he can expend a daily use of
that poison to employ his debilitating venom ability an additional time. The debilitating venom
functions only for the poison darter and becomes inert if not used within 1 hour. Creating a
debilitating venom is a standard action, and it can be applied to a weapon as a move action.

_Debilitating Venom_—injury; _save_ Fortitude DC = 10 + 1/2 the poison darter's level + his Wisdom
modifier; _frequency_ 1/round for 4 rounds; _effect_ 1d3 Dexterity damage; _cure_ 1 save.

At 5th level, the frequency increases to 6 rounds, and the toxin [sickens](ref/misc/sickened) a
creature for 1 round every time it fails its saving throw to resist the poison. At 10th level, the
poison's Dexterity damage increases to 1d4, and two successful saving throws are needed to cure the
poison. At 15th level, the poison dart can choose to deal Strength, Dexterity, or Constitution
damage with the debilitating venom, selected when he creates the toxin. At 20th level, the poison's
damage die increases to 1d6.

This ability replaces favored enemy and master hunter.

## Poison Use (Ex) {#poison-use}

A poison darter is trained in the use of poison and cannot accidentally poison himself when applying
poison to a weapon.

This ability replaces wild empathy.

## Poison Style (Ex) {#poison-style}

At 2nd level, in place of a combat style feat, a poison darter can select any rogue talent that
modifies sneak attacks or any alchemist discovery that modifies poisons he creates and applies,
using his Wisdom modifier in place of his Intelligence modifier and his ranger level in place of his
alchemist or rogue level for the purpose of meeting prerequisites. He can use the
[sticky poison](ref/discovery/sticky-poison) discovery to apply a single dose of poison to two
blowgun darts without reducing its potency.

This ability modifies combat style feat.

## Precise Dart (Ex) {#precise-dart}

At 4th level, a poison darter gains a [sneak attack](ref/ability/sneak-attack) identical to the
rogue class feature, but only when attacking with a blowgun. This deals 1d6 extra points of damage,
and the damage increases by 1d6 at 6th level and every 2 ranger levels thereafter.

This ability replaces hunter's bond.
