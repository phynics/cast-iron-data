+++
id = "ref/arc-fighter/swarm-fighter"
kind = "archetype"
title = "Swarm Fighter"
aon = "ArchetypeDisplay.aspx?FixedName=Fighter%20Swarm%20Fighter"
source_ids = ["kobolds-of-golarion"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "swarm_fighter", path = "json/archetypes_fighter2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/fighter" },
]
[[sources]]
publication = "kobolds-of-golarion"
page = "23"

[fields]
kind = "archetype"
features = [
  { anchor = "athletic-prowess" },
  { anchor = "mobility", level = 1 },
  { anchor = "safety-in-numbers", level = 2 },
  { anchor = "bonus-teamwork-feats", level = 2 },
  { anchor = "share-space", level = 5 },
  { anchor = "strike-the-underbelly", level = 9 },
  { anchor = "always-underfoot", level = 13 },
  { anchor = "soft-underbelly", level = 20 },
]
trades = [
  { replaces = "The bonus feat a fighter gains at first level, and can't be replaced at a later level", feature = "bonus-feats", levels = [1], by = ["mobility"] },
  { replaces = "Bravery", feature = "bravery", by = ["safety-in-numbers"] },
  { replaces = "The bonus combat feats the fighter normally receives at those levels", feature = "bonus-feats", levels = [2, 6, 10, 14, 18], by = ["bonus-teamwork-feats"] },
  { replaces = "Weapon training 1", feature = "weapon-training", levels = [5], by = ["share-space"] },
  { replaces = "Weapon training 2", feature = "weapon-training", levels = [9], by = ["strike-the-underbelly"] },
  { replaces = "Weapon training 3 and 4", feature = "weapon-training", levels = [13, 17], by = ["always-underfoot"] },
  { replaces = "Weapon mastery", feature = "weapon-mastery", by = ["soft-underbelly"] },
  { alters = "Weapon and armor proficiencies", feature = "weapon-and-armor-proficiencies" },
]
+++

Kobolds know there's strength in numbers, and they rarely send fewer than two kobolds out on patrol.
This reliance on one another extends to combat tactics too—overwhelming numbers and tight quarters
are the [kobold](ref/race/kobold) fighter's friends. Scuttling between the legs of friend and foe
alike, the swarm fighter is an unshakable combatant.

## Weapon and Armor Proficiency {#weapon-and-armor-proficiency}

A swarm fighter is proficient with all simple and martial weapons. She is proficient with light and
medium armor, but not with shields.

## Athletic Prowess (Ex) {#athletic-prowess}

A swarm fighter adds [Acrobatics](ref/skill/acrobatics) and [Climb](ref/skill/climb) to her class
skills, and gains a bonus on checks with these skills equal to 1/2 her swarm fighter level.

## Mobility (Ex) {#mobility}

The swarm fighter gains [Mobility](ref/feat/mobility) as a bonus feat, even if she does not meet the
prerequisites.

This replaces the bonus feat a fighter gains at first level, and can't be replaced at a later level.

## Safety in Numbers (Ex) {#safety-in-numbers}

A swarm fighter benefits greatly from the proximity of her allies. She gains a morale bonus on saves
against fear effects equal to the number of allies within 20 feet of her. This bonus can't exceed
[half](ref/misc/fractions-and-rounding) her level.

This ability replaces bravery.

## Bonus Teamwork Feats (Ex) {#bonus-teamwork-feats}

At 2nd level and every 4 levels thereafter, the swarm fighter gains a bonus Teamwork Feat.

This ability replaces the bonus combat feats the fighter normally receives at those levels.

## Bonus Feats (Ex) {#bonus-feats}

At 4th level, and every 4 levels thereafter, the swarm fighter gains a bonus combat feat. These are
gained as with the fighter's normal bonus feats class feature (but less frequently).

## Share Space (Ex) {#share-space}

At 5th level, the swarm fighter can move into the space of another creature at least one size
category larger than she is. She may end her movement in, and make attacks from, that space. She
must succeed at the Acrobatics check for moving through an occupied square to move into a space
occupied by an enemy. While sharing the space of another creature, she gains a +2 shield bonus to AC
and a +1 circumstance bonus on Reflex saves.

This ability replaces weapon training 1.

## Strike the Underbelly (Ex) {#strike-the-underbelly}

At 9th level, creatures with which the swarm fighter shares a space are denied their Dexterity bonus
to Armor Class against the swarm fighter's attacks.

This ability replaces weapon training 2.

## Always Underfoot (Ex) {#always-underfoot}

At 13th level, the swarm fighter gains [Step Up](ref/feat/step-up) as a bonus feat. A creature
sharing a square with the swarm fighter is considered adjacent for the purposes of this feat. At
17th level, the swarm fighter gains [Following Step](ref/feat/following-step) as a bonus feat.

These abilities replace weapon training 3 and 4.

## Soft Underbelly (Ex) {#soft-underbelly}

At 20th level, any attacks made against creatures with which the swarm fighter shares a space
automatically confirm all critical threats.

This ability replaces weapon mastery.
