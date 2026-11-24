+++
id = "ref/arc-barbarian/armored-hulk"
kind = "archetype"
title = "Armored Hulk"
aon = "ArchetypeDisplay.aspx?FixedName=Barbarian%20Armored%20Hulk"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "armored_hulk", path = "json/archetypes_barbarian.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/barbarian" },
]
[[sources]]
publication = "ultimate-combat"
page = "28"

[fields]
kind = "archetype"
features = [
  { anchor = "indomitable-stance", level = 1 },
  { anchor = "armored-swiftness", level = 2 },
  { anchor = "resilience-of-steel", level = 3 },
  { anchor = "improved-armored-swiftness", level = 5 },
]
trades = [
  { replaces = "Fast movement", feature = "fast-movement", by = ["indomitable-stance"] },
  { replaces = "Uncanny dodge", feature = "uncanny-dodge", by = ["armored-swiftness"] },
  { replaces = "Trap sense", feature = "trap-sense", by = ["resilience-of-steel"] },
  { replaces = "Improved uncanny dodge", feature = "improved-uncanny-dodge", by = ["improved-armored-swiftness"] },
]
+++

Some barbarians disdain the hides and leather used as armor by most of their kin. Instead they
master the heaviest of armors, even those created by more civilized people, to gain greater
protection and stability in battle.

## Weapon and Armor Proficiency {#weapon-and-armor-proficiency}

An armored hulk gains proficiency in heavy armor.

## Indomitable Stance (Ex) {#indomitable-stance}

An armored hulk gains a +1 bonus on combat maneuver checks and to CMD for overrun combat maneuvers,
and on Reflex saves against [trample](ref/umr/trample) attacks. She also gains a +1 bonus to her AC
against charge attacks and on attack and damage rolls against charging creatures. This ability
replaces fast movement.

## Armored Swiftness (Ex) {#armored-swiftness}

At 2nd level, an armored hulk moves faster in medium and heavy armor. When wearing medium or heavy
armor, an armored hulk can move 5 feet faster than normal, to a maximum of her speed. This ability
replaces uncanny dodge.

## Resilience of Steel (Ex) {#resilience-of-steel}

At 3rd level, an armored hulk is able to use her armor to help avoid deadly hits. While wearing
heavy armor, she gains a +1 bonus to AC that applies only on critical hit confirmation rolls. This
bonus increases by +1 every 3 levels beyond 3rd (maximum +6 at 18th level). This ability replaces
trap sense.

## Improved Armored Swiftness (Ex) {#improved-armored-swiftness}

At 5th level, an armored hulk's land speed is faster than the norm for her race by +10 feet. This
benefit applies when she is wearing any armor, including heavy armor, but not while carrying a heavy
load. Apply this bonus before modifying the armored hulk's speed because of any load carried or
armor worn. This bonus stacks with any other bonuses to the barbarian's land speed. This ability
replaces improved uncanny dodge.

## Rage Powers {#rage-powers}

The following rage powers complement the armored hulk archetype:
[boasting taunt](ref/ragepower/boasting-taunt)\*,
[greater guarded life](ref/ragepower/greater-guarded-life),
[guarded life](ref/ragepower/guarded-life)\*, [guarded stance](ref/ragepower/guarded-stance),
[increased damage reduction](ref/ragepower/increased-damage-reduction),
[no escape](ref/ragepower/no-escape), [overbearing advance](ref/ragepower/overbearing-advance)\*,
[overbearing onslaught](ref/ragepower/overbearing-onslaught)\*,
[reflexive dodge](ref/ragepower/reflexive-dodge), [rolling dodge](ref/ragepower/rolling-dodge), and
[unexpected strike](ref/ragepower/unexpected-strike).
