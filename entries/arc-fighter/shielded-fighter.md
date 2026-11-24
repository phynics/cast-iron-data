+++
id = "ref/arc-fighter/shielded-fighter"
kind = "archetype"
title = "Shielded Fighter"
aon = "ArchetypeDisplay.aspx?FixedName=Fighter%20Shielded%20Fighter"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "shielded_fighter", path = "json/archetypes_fighter2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/fighter" },
]
[[sources]]
publication = "advanced-players-guide"
page = "108"

[fields]
kind = "archetype"
features = [
  { anchor = "active-defense", level = 3 },
  { anchor = "shield-fighter", level = 5 },
  { anchor = "shield-buffet", level = 9 },
  { anchor = "shield-guard", level = 17 },
  { anchor = "shield-mastery", level = 19 },
  { anchor = "shield-ward", level = 20 },
]
trades = [
  { replaces = "Armor training 1, 2, 3, and 4", feature = "armor-training", levels = [3, 7, 11, 15], by = ["active-defense"] },
  { replaces = "Weapon training 1", feature = "weapon-training", levels = [5], by = ["shield-fighter"] },
  { replaces = "Weapon training 2 and 3", feature = "weapon-training", levels = [9, 13], by = ["shield-buffet"] },
  { replaces = "Weapon training 4", feature = "weapon-training", levels = [17], by = ["shield-guard"] },
  { replaces = "Armor mastery", feature = "armor-mastery", by = ["shield-mastery"] },
  { replaces = "Weapon mastery", feature = "weapon-mastery", by = ["shield-ward"] },
]
+++

A shielded fighter focuses on both offense and defense, blending weapon and shield in perfect
balance to impede his enemies while delivering deadly blows, and even turning the shield itself into
a formidable weapon. These fighting school benefits apply when wielding a weapon and a shield
simultaneously.

## Active Defense (Ex) {#active-defense}

At 3rd level, a shielded fighter gains a +1 dodge bonus to AC when wielding a shield and
[fighting defensively](ref/misc/fighting-defensively), using
[Combat Expertise](ref/feat/combat-expertise), or using [total defense](ref/misc/total-defense).
This bonus increases by +1 for every four levels beyond 3rd. As a swift action, he may share this
bonus with one adjacent ally, or [half](ref/misc/fractions-and-rounding) of the bonus (minimum +0)
with all adjacent allies, until the beginning of his next turn. This ability replaces armor training
1, 2, 3, and 4.

## Shield Fighter (Ex) {#shield-fighter}

At 5th level, a shielded fighter gains a +1 bonus on attack and damage rolls when making a
[shield bash](ref/misc/shield-bash). These bonuses increase by +1 every four levels beyond 5th. With
a [full attack](ref/rule/full-attack) action, a shielded fighter may alternate between using his
weapon or his shield for each attack. This action does not grant additional attacks or incur
penalties as two-weapon fighting does. This ability replaces weapon training 1.

## Shield Buffet (Ex) {#shield-buffet}

At 9th level, as a move action, a shielded fighter may make a combat maneuver check to use his
shield to impede an adjacent enemy. If successful, the target suffers a -2 penalty on its attack
rolls against the shielded fighter and a -2 penalty to AC on attacks made by the shielded fighter
until the beginning of his next turn.

At 13th level, a shielded fighter may use this ability as a swift action. This ability replaces
weapon training 2 and 3.

## Shield Guard (Ex) {#shield-guard}

At 17th level, as a swift action, a shielded fighter may designate one square adjacent to him. He
may designate two squares if using a heavy shield or three squares if using a tower shield, but
these squares must be contiguous. Enemies in these squares cannot [flank](ref/rule/flanking) the
shielded fighter and do not count for flanking with other creatures. This effect lasts until he
moves from his position or uses another swift action to change the affected squares. This ability
replaces weapon training 4.

## Shield Mastery (Ex) {#shield-mastery}

At 19th level, a shielded fighter gains DR 5/— when wielding a shield. This ability replaces armor
mastery.

## Shield Ward (Ex) {#shield-ward}

At 20th level, a shielded fighter gains [evasion](ref/ability/evasion) (as a
[rogue](ref/class/rogue)) while wielding a shield, and adds his shield bonus to his AC (not
including enhancement bonuses) on Reflex saves and to his touch AC. In addition, his shield cannot
be [disarmed](ref/rule/disarm) or [sundered](ref/rule/sunder). This ability replaces weapon mastery.
