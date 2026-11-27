+++
id = "ref/arc-fighter/polearm-master"
kind = "archetype"
title = "Polearm Master"
aon = "ArchetypeDisplay.aspx?FixedName=Fighter%20Polearm%20Master"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "polearm_master", path = "json/archetypes_fighter2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/fighter" },
]
[[sources]]
publication = "advanced-players-guide"
page = "106"

[fields]
kind = "archetype"
features = [
  { anchor = "pole-fighting", level = 2 },
  { anchor = "steadfast-pike", level = 3 },
  { anchor = "polearm-training", level = 5 },
  { anchor = "flexible-flanker", level = 9 },
  { anchor = "sweeping-fend", level = 13 },
  { anchor = "step-aside", level = 17 },
  { anchor = "polearm-parry", level = 19 },
  { anchor = "weapon-mastery", level = 20 },
]
trades = [
  { replaces = "Bravery", feature = "bravery", by = ["pole-fighting"] },
  { replaces = "Armor training 1, 2, 3, and 4", feature = "armor-training", levels = [3, 7, 11, 15], by = ["steadfast-pike"] },
  { replaces = "Weapon training 1", feature = "weapon-training", levels = [5], by = ["polearm-training"] },
  { replaces = "Weapon training 2", feature = "weapon-training", levels = [9], by = ["flexible-flanker"] },
  { replaces = "Weapon training 3", feature = "weapon-training", levels = [13], by = ["sweeping-fend"] },
  { replaces = "Weapon training 4", feature = "weapon-training", levels = [17], by = ["step-aside"] },
  { replaces = "Armor mastery", feature = "armor-mastery", by = ["polearm-parry"] },
  { alters = "Weapon mastery", feature = "weapon-mastery", by = ["weapon-mastery"] },
]
+++

The polearm master is schooled in the ancient wisdom that enemies are best faced at the end of long
striking pole, lashing like a serpent before clumsy swords and axes can even be brought to bear.

## Pole Fighting (Ex) {#pole-fighting}

At 2nd level, as an immediate action, a polearm master can shorten the grip on his spear or polearm
with reach and use it against adjacent targets. This action results in a -4 penalty on attack rolls
with that weapon until he spends another immediate action to return to the normal grip. The penalty
is reduced by -1 for every four levels beyond 2nd. This ability replaces bravery.

## Steadfast Pike (Ex) {#steadfast-pike}

At 3rd level, a polearm master gains a +1 bonus on attack rolls with [readied](ref/rule/ready)
attacks and attacks of opportunity made with a spear or polearm. The bonus increases by +1 for every
four levels beyond 3rd. This ability replaces armor training 1, 2, 3, and 4.

## Polearm Training (Ex) {#polearm-training}

At 5th level, a polearm master gains a +1 bonus on attack and damage rolls with spears and polearms.
The bonus increases by +1 for every four levels beyond 5th. This ability replaces weapon training 1.

## Flexible Flanker (Ex) {#flexible-flanker}

At 9th level, a polearm master may choose any square adjacent to him and treat that square as his
location for determining who he is [flanking](ref/rule/flanking), even if that square is occupied by
a creature, object, or solid barrier. This ability replaces weapon training 2.

## Sweeping Fend (Ex) {#sweeping-fend}

At 13th level, a polearm master can use any spear or pole arm to make a
[bull rush](ref/rule/bull-rush) or [trip](ref/rule/trip) maneuver, though he takes a -4 penalty to
his CMB when making such attempts. Weapons with the [trip](ref/misc/trip) property do not incur this
penalty on trip maneuvers. This ability replaces weapon training 3.

## Step Aside (Ex) {#step-aside}

At 17th level, when a creature threatened by a polearm master takes
[a 5-foot step](ref/rule/take-5-foot-step) into a square adjacent to him, he can take a 5-foot step
as an immediate action. This 5-foot step must be subtracted from his movement on the next turn. He
also gains a +2 dodge bonus to his AC against that opponent until the end of his next turn. This
ability replaces weapon training 4.

## Polearm Parry (Ex) {#polearm-parry}

At 19th level, when an opponent threatened by a polearm master makes a melee attack against an ally,
he may take an immediate action to grant his ally a +2 shield bonus to AC and DR 5/— against that
attack. He may use this ability to protect himself, but only if the attacking creature is not
adjacent to him. This ability replaces armor mastery.

## Weapon Mastery (Ex) {#weapon-mastery}

A polearm master must choose a spear or polearm.
