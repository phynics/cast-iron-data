+++
id = "ref/arc-fighter/savage-warrior"
kind = "archetype"
title = "Savage Warrior"
aon = "ArchetypeDisplay.aspx?FixedName=Fighter%20Savage%20Warrior"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "savage_warrior", path = "json/archetypes_fighter2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/fighter" },
]
[[sources]]
publication = "advanced-players-guide"
page = "107"

[fields]
kind = "archetype"
features = [
  { anchor = "spark-of-life", level = 2 },
  { anchor = "natural-savagery", level = 5 },
  { anchor = "savage-charge", level = 9 },
  { anchor = "careful-claw", level = 13 },
  { anchor = "greater-savage-charge", level = 17 },
  { anchor = "natural-weapon-mastery", level = 20 },
]
trades = [
  { replaces = "Bravery", feature = "bravery", by = ["spark-of-life"] },
  { replaces = "Weapon training 1", feature = "weapon-training", levels = [5], by = ["natural-savagery"] },
  { replaces = "Weapon training 2", feature = "weapon-training", levels = [9], by = ["savage-charge"] },
  { replaces = "Weapon training 3", feature = "weapon-training", levels = [13], by = ["careful-claw"] },
  { replaces = "Weapon training 4", feature = "weapon-training", levels = [17], by = ["greater-savage-charge"] },
  { replaces = "Weapon mastery", feature = "weapon-mastery", by = ["natural-weapon-mastery"] },
]
+++

Warriors' might is not measured only by their skill with steel, but also by their ability to inflict
death with fang and claw, horn and hoof, and every exotic appendage the natural and unnatural world
has to offer.

## Spark of Life (Ex) {#spark-of-life}

At 2nd level, a savage warrior gains a +1 bonus on saving throws made against energy drain and death
effects. This bonus increases by +1 for every four levels beyond 2nd. This ability replaces bravery.

## Natural Savagery (Ex) {#natural-savagery}

At 5th level, a savage warrior gains a +1 bonus on attack and damage rolls with natural weapons.
This bonus also applies to CMB and CMD for [grappling](ref/rule/grapple). This bonus increases by +1
for every four levels beyond 5th. This ability replaces weapon training 1.

## Savage Charge (Ex) {#savage-charge}

At 9th level, when a savage warrior attacks with a natural weapon at the end of a
[charge](ref/rule/charge), he gains a bonus on his natural weapon attack rolls equal to
[half](ref/misc/fractions-and-rounding) his fighter level, while suffering a penalty to his AC equal
to half his fighter level. These replace the normal attack roll bonus and AC penalty for charging.
This bonus also applies to his CMB for a [bull rush](ref/rule/bull-rush) or
[overrun](ref/rule/overrun) combat maneuvers made when charging. This ability replaces weapon
training 2.

## Careful Claw (Ex) {#careful-claw}

At 13th level, when using a natural weapon to attack a creature using
_[fire shield](ref/spell/fire-shield)_ or a similar effect that damages creatures attacking it (such
as a [barbed devil's](ref/monster/devil-barbed-devil-hamatula) barbed defense), a savage warrior
reduces the damage from such effects by an amount equal to 1/2 his fighter level. This ability
replaces weapon training 3.

## Greater Savage Charge (Ex) {#greater-savage-charge}

At 17th level, when using savage charge, the AC penalty is reduced to 1/4 his fighter level instead
of 1/2 his fighter level. In addition, a savage warrior can charge through friendly creatures and
[difficult terrain](ref/rule/terrain-and-obstacles). This ability replaces weapon training 4.

## Natural Weapon Mastery (Ex) {#natural-weapon-mastery}

At 20th level, a savage warrior must choose one natural weapon. This ability replaces weapon
mastery.
