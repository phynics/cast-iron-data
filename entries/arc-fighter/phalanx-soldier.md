+++
id = "ref/arc-fighter/phalanx-soldier"
kind = "archetype"
title = "Phalanx Soldier"
aon = "ArchetypeDisplay.aspx?FixedName=Fighter%20Phalanx%20Soldier"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "phalanx_soldier", path = "json/archetypes_fighter2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/fighter" },
]
[[sources]]
publication = "advanced-players-guide"
page = "105"

[fields]
kind = "archetype"
features = [
  { anchor = "stand-firm", level = 2 },
  { anchor = "phalanx-fighting", level = 3 },
  { anchor = "ready-pike", level = 5 },
  { anchor = "deft-shield", level = 7 },
  { anchor = "shield-ally", level = 9 },
  { anchor = "irresistible-advance", level = 15 },
  { anchor = "shielded-fortress", level = 20 },
]
trades = [
  { replaces = "Bravery", feature = "bravery", by = ["stand-firm"] },
  { replaces = "Armor training 1", feature = "armor-training", levels = [3], by = ["phalanx-fighting"] },
  { replaces = "Weapon training 1", feature = "weapon-training", levels = [5], by = ["ready-pike"] },
  { replaces = "Armor training 2 and 3", feature = "armor-training", levels = [7, 11], by = ["deft-shield"] },
  { replaces = "Weapon training 2, 3, and 4", feature = "weapon-training", levels = [9, 13, 17], by = ["shield-ally"] },
  { replaces = "Armor training 4", feature = "armor-training", levels = [15], by = ["irresistible-advance"] },
  { replaces = "Weapon mastery", feature = "weapon-mastery", by = ["shielded-fortress"] },
]
+++

The phalanx soldier specializes in defensive tactics, using his shield to guard himself and his
allies and forming a shield wall like an unbreakable anvil against which his enemies break.

## Stand Firm (Ex) {#stand-firm}

At 2nd level, a phalanx soldier gains a +1 bonus to CMD against [bull rush](ref/rule/bull-rush),
drag, [overrun](ref/rule/overrun), and [trip](ref/rule/trip) attempts. This bonus also applies on
saves against [trample](ref/umr/trample) attacks. The bonus increases by +1 for every four levels
beyond 2nd. This ability replaces bravery.

## Phalanx Fighting (Ex) {#phalanx-fighting}

At 3rd level, when a phalanx soldier wields a shield, he can use any polearm or spear of his size as
a one-handed weapon. This ability replaces armor training 1.

## Ready Pike (Ex) {#ready-pike}

At 5th level, a phalanx soldier can, once per day, [ready](ref/rule/ready) a weapon with the
[brace](ref/misc/brace) property as an immediate action, gaining a +1 bonus on attack and damage
rolls. For every four levels beyond 5th, this bonus increases by +1, and he can use the ability one
additional time per day. He cannot use this ability when [flat-footed](ref/rule/flat-footed). This
ability replaces weapon training 1.

## Deft Shield (Ex) {#deft-shield}

At 7th level, the armor check penalty from a shield and the attack roll penalty are reduced by -1
for a phalanx soldier using a [tower shield](ref/eq-armor/tower-shield). At 11th level, these
penalties are reduced by -2. This ability replaces armor training 2 and 3.

## Shield Ally (Ex) {#shield-ally}

At 9th level, when a phalanx fighter is using a heavy or tower shield, he can, as a move action,
provide partial [cover](ref/rule/cover) (+2 cover bonus to AC, +1 bonus on Reflex saves) to himself
and all adjacent allies until the beginning of his next turn.

At 13th level, he can instead provide cover (+4 cover bonus to AC, +2 bonus on Reflex saves) and
[evasion](ref/ability/evasion) (as a [rogue](ref/class/rogue)) to one adjacent ally until the
beginning of his next turn. This cover does not allow Stealth checks.

At 17th level, he can provide cover to himself and all adjacent allies, or he can provide improved
cover (+8 cover bonus to AC, +4 bonus on Reflex saves,
[improved evasion](ref/ability/improved-evasion)) to a single adjacent ally. This ability replaces
weapon training 2, 3, and 4.

## Irresistible Advance (Ex) {#irresistible-advance}

At 15th level, a phalanx fighter gains a bonus on bull rush and overrun CMB checks. This bonus
depends on the type of shield used: +1 with a buckler, +2 with a light shield, +3 with a heavy
shield, or +4 with a tower shield. This ability replaces armor training 4.

## Shielded Fortress (Ex) {#shielded-fortress}

At 20th level, a phalanx fighter's shield cannot be [disarmed](ref/rule/disarm) or
[sundered](ref/rule/sunder). He gains evasion (as a rogue) when using a shield (improved evasion
when using a tower shield). As a move action, a phalanx fighter can provide evasion to all adjacent
allies until the beginning of his next turn. As an immediate action, he can provide improved evasion
to an adjacent ally against one attack. This ability replaces weapon mastery.
