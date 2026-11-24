+++
id = "ref/arc-fighter/mobile-fighter"
kind = "archetype"
title = "Mobile Fighter"
aon = "ArchetypeDisplay.aspx?FixedName=Fighter%20Mobile%20Fighter"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "mobile_fighter", path = "json/archetypes_fighter.json" },
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
  { anchor = "agility", level = 2 },
  { anchor = "leaping-attack", level = 5 },
  { anchor = "rapid-attack", level = 11 },
  { anchor = "fleet-footed", level = 15 },
  { anchor = "whirlwind-blitz", level = 20 },
]
trades = [
  { replaces = "Bravery", feature = "bravery", by = ["agility"] },
  { replaces = "Weapon training 1, 2, 3, and 4", feature = "weapon-training", levels = [5, 9, 13, 17], by = ["leaping-attack"] },
  { replaces = "Armor training 3", feature = "armor-training", levels = [11], by = ["rapid-attack"] },
  { replaces = "Armor training 4", feature = "armor-training", levels = [15], by = ["fleet-footed"] },
  { replaces = "Weapon mastery", feature = "weapon-mastery", by = ["whirlwind-blitz"] },
]
+++

Where some fighters focus on strength and raw power, the mobile fighter relies on swiftness and
mobility, gliding across the battlefield like a steel whirlwind and leaving destruction in his wake.

## Agility (Ex) {#agility}

At 2nd level, a mobile fighter gains a +1 bonus on saving throws made against effects that cause him
to become [paralyzed](ref/rule/paralyzed), [slowed](ref/spell/slow), or
[entangled](ref/rule/entangled). This bonus increases by +1 for every four levels beyond 2nd. This
ability replaces bravery.

## Leaping Attack (Ex) {#leaping-attack}

At 5th level, when a mobile fighter moves at least 5 feet prior to attacking, he gains a +1 bonus on
attack and damage rolls. This bonus increases by +1 for every four levels beyond 5th. This ability
replaces weapon training 1, 2, 3, and 4.

## Rapid Attack (Ex) {#rapid-attack}

At 11th level, a mobile fighter can combine a [full attack](ref/rule/full-attack) action with a
single move. He must forgo the attack at his highest bonus but may take the remaining attacks at any
point during his movement. This movement provokes attacks of opportunity as normal. This ability
replaces armor training 3.

## Fleet Footed (Ex) {#fleet-footed}

At 15th level, the mobile fighter's speed increases by 10 feet. He can
[take 10](ref/rule/taking-10-and-taking-20) on Acrobatics checks even while distracted or
threatened, and can take 20 on an Acrobatics check once per day for every five fighter levels he
possesses. This ability replaces armor training 4.

## Whirlwind Blitz (Ex) {#whirlwind-blitz}

At 20th level, a mobile fighter can make a full-attack action as a standard action. He may also use
the [Whirlwind Attack](ref/feat/whirlwind-attack) feat as a standard action. This ability replaces
weapon mastery.
