+++
id = "ref/arc-bloodrager/steelblood"
kind = "archetype"
title = "Steelblood"
aon = "ArchetypeDisplay.aspx?FixedName=Bloodrager%20Steelblood"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "steelblood", path = "json/archetypes_bloodrager.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/bloodrager" },
]
[[sources]]
publication = "advanced-class-guide"
page = "85"

[fields]
kind = "archetype"
features = [
  { anchor = "indomitable-stance", level = 1 },
  { anchor = "armored-swiftness", level = 2 },
  { anchor = "armor-training", level = 5 },
  { anchor = "blood-deflection", level = 7 },
]
trades = [
  { replaces = "The bloodrager's armor proficiency", feature = "weapon-and-armor-proficiencies", power = "armor" },
  { replaces = "Fast movement", feature = "fast-movement", by = ["indomitable-stance"] },
  { replaces = "Uncanny dodge", feature = "uncanny-dodge", by = ["armored-swiftness"] },
  { replaces = "Improved uncanny dodge", feature = "improved-uncanny-dodge", by = ["armor-training"] },
  { replaces = "Damage reduction", feature = "damage-reduction", by = ["blood-deflection"] },
]
+++

Most bloodragers prefer light armor, but some learn the secret of using heavy armors. These
steelbloods plod around the battlefield inspiring fear and delivering carnage from within a steel
shell.

## Weapon and Armor Proficiency {#weapon-and-armor-proficiency}

A steelblood gains proficiency in heavy armor. A steelblood can cast bloodrager spells while wearing
heavy armor without incurring an arcane spell failure chance. This replaces the bloodrager's armor
proficiency.

## Indomitable Stance (Ex) {#indomitable-stance}

At 1st level, a steelblood gains a +1 bonus on combat maneuver checks, to CMD against
[overrun](ref/rule/overrun) combat maneuvers, and on Reflex saving throws against
[trample](ref/umr/trample) attacks. He also gains a +1 bonus to his AC against
[charge](ref/rule/charge) attacks and on attack and damage rolls against charging creatures. This
ability replaces fast movement.

## Armored Swiftness (Ex) {#armored-swiftness}

At 2nd level, a steelblood moves faster in medium and heavy armor. When wearing medium or heavy
armor, a steelblood can move 5 feet faster than normal in that armor, to a maximum of his
unencumbered speed. This ability replaces uncanny dodge.

## Armor Training (Ex) {#armor-training}

At 5th level, a steelblood learns to be more maneuverable while wearing armor. Whenever he is
wearing armor, he reduces the armor check penalty by 1 (to a maximum of 0) and increases the maximum
Dexterity bonus allowed by his armor by 1. Every 4 levels thereafter (9th, 13th, and 17th), these
bonuses increase by 1, to a maximum 4-point reduction of the armor check penalty and a +4 increase
of the maximum Dexterity bonus. This ability stacks with the fighter class feature of the same name.
This ability replaces improved uncanny dodge.

## Blood Deflection (Su) {#blood-deflection}

At 7th level, as an immediate action a steelblood can sacrifice a bloodrager spell slot to gain a
deflection bonus to AC equal to the level of the spell sacrificed. The deflection bonus lasts until
the start of his next turn. This ability can be applied after an attack roll is made against the
steelblood, allowing the steelblood to convert a hit into a miss if the deflection bonus is high
enough. This ability replaces [damage reduction](ref/rule/damage-reduction).
