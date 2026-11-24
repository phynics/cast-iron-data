+++
id = "ref/arc-fighter/two-handed-fighter"
kind = "archetype"
title = "Two-Handed Fighter"
aon = "ArchetypeDisplay.aspx?FixedName=Fighter%20Two-Handed%20Fighter"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "two_handed_fighter", path = "json/archetypes_fighter2.json" },
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
  { anchor = "shattering-strike", level = 2 },
  { anchor = "overhand-chop", level = 3 },
  { anchor = "weapon-training" },
  { anchor = "backswing", level = 7 },
  { anchor = "piledriver", level = 11 },
  { anchor = "greater-power-attack", level = 15 },
  { anchor = "devastating-blow", level = 19 },
]
trades = [
  { replaces = "Bravery", feature = "bravery", by = ["shattering-strike"] },
  { replaces = "Armor training 1", feature = "armor-training", levels = [3], by = ["overhand-chop"] },
  { replaces = "Armor training 2", feature = "armor-training", levels = [7], by = ["backswing"] },
  { replaces = "Armor training 3", feature = "armor-training", levels = [11], by = ["piledriver"] },
  { replaces = "Armor training 4", feature = "armor-training", levels = [15], by = ["greater-power-attack"] },
  { replaces = "Armor mastery", feature = "armor-mastery", by = ["devastating-blow"] },
]
+++

Some fighters focus their efforts on finding the biggest, heaviest, most imposing weapon they can
find and training to manage and harness the weight of their massive weapons for maximum impact.
These fighting school benefits only apply when using two-handed weapons.

## Shattering Strike (Ex) {#shattering-strike}

At 2nd level, a two-handed fighter gains a +1 bonus to CMB and CMD on [sunder](ref/rule/sunder)
attempts and on damage rolls made against objects. These bonuses increase by +1 for every four
levels beyond 2nd. This ability replaces bravery.

## Overhand Chop (Ex) {#overhand-chop}

At 3rd level, when a two-handed fighter makes a single attack (with the attack action or a
[charge](ref/rule/charge)) with a two-handed weapon, he adds double his Strength bonus on damage
rolls. This ability replaces armor training 1.

## Weapon Training (Ex) {#weapon-training}

As the fighter class feature, but the bonuses only apply when wielding two-handed melee weapons.

## Backswing (Ex) {#backswing}

At 7th level, when a two-handed fighter makes a [full attack](ref/rule/full-attack) with a
two-handed weapon, he adds double his Strength bonus on damage rolls for all attacks after the
first. This ability replaces armor training 2.

## Piledriver (Ex) {#piledriver}

At 11th level, as a standard action, a two-handed fighter can make a single melee attack with a
two-handed weapon. If the attack hits, he may make a [bull rush](ref/rule/bull-rush) or
[trip](ref/rule/trip) combat maneuver against the target of his attack as a free action that does
not provoke an attack of opportunity. This ability replaces armor training 3.

## Greater Power Attack (Ex) {#greater-power-attack}

At 15th level, when using [Power Attack](ref/feat/power-attack) with a two-handed melee weapon, the
bonus damage from Power Attack is doubled (+100%) instead of increased by half (+50%). This ability
replaces armor training 4.

## Devastating Blow (Ex) {#devastating-blow}

At 19th level, as a standard action, a two-handed fighter may make a single melee attack with a
two-handed weapon at a -5 penalty. If the attack hits, it is treated as a critical threat. Special
weapon abilities that activate only on a critical hit do not activate if this critical hit is
confirmed. This ability replaces armor mastery.
