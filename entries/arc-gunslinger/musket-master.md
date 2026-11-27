+++
id = "ref/arc-gunslinger/musket-master"
kind = "archetype"
title = "Musket Master"
aon = "ArchetypeDisplay.aspx?FixedName=Gunslinger%20Musket%20Master"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "musket_master", path = "json/archetypes_gunslinger.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/gunslinger" },
]
[[sources]]
publication = "ultimate-combat"
page = "50"

[fields]
kind = "archetype"
features = [
  { anchor = "gunsmith", level = 1 },
  { anchor = "steady-aim", level = 1 },
  { anchor = "fast-musket", level = 3 },
  { anchor = "rapid-reloader", level = 1 },
  { anchor = "musket-training", level = 5 },
]
trades = [
  { replaces = "Gunslinger's dodge deed", feature = "deeds", power = "gunslinger's dodge", by = ["steady-aim"] },
  { replaces = "Utility shot deed", feature = "deeds", power = "utility shot", by = ["fast-musket"] },
  { replaces = "Gun training 1, 2, 3, and 4", feature = "gun-training", levels = [5, 9, 13, 17], by = ["musket-training"] },
  { alters = "Gunsmith", feature = "gunsmith", by = ["gunsmith"] },
]
+++

Pistols and other one-handed firearms are often easy to conceal and faster to load than other
firearms, and do sufficient damage for most situations. But some gunslingers want a little more
firepower and range. These are the musket masters; the best of these gunslingers can reload a musket
with dazzling speed, potentially putting even their pistol-wielding brethren to shame.

## Weapon Proficiency {#weapon-proficiency}

Instead of proficiency with all firearms, a musket master only gains proficiency with two-handed
firearms. She must take the [Exotic Weapon Proficiency](ref/feat/exotic-weapon-proficiency)
(firearms) feat to gain proficiency with one-handed firearms and firearm siege engines.

## Gunsmith {#gunsmith}

A musket master must take a [musket](ref/eq-weapon/musket) when she chooses a battered firearm at
1st level.

## Deeds {#deeds}

A musket master swaps a pair of deeds for the following.

## Steady Aim (Ex) {#steady-aim}

At 1st level, as long as a musket master has at least 1 grit point, she can take a move-equivalent
action to increase the accuracy of a two-handed firearm. When she does, she increases the range
increment of the firearm she is firing by 10 feet. This stacks with other abilities that increase
her range increment. This deed replaces the gunslinger's dodge deed.

## Fast Musket (Ex) {#fast-musket}

At 3rd level, as long as the musket master has 1 grit point, she can reload any two-handed firearm
as if it were a one-handed firearm. This deed replaces the utility shot deed.

## Rapid Reloader {#rapid-reloader}

At 1st level, a musket master gains [Rapid Reload](ref/feat/rapid-reload) (musket) as a bonus feat.
Use the updated version of this feat on page 115.

## Musket Training (Ex) {#musket-training}

Starting at 5th level, a musket master increases her skill with two-handed firearms. She gains a
bonus on damage rolls equal to her Dexterity modifier, and when she misfires with a two-handed
firearm, the misfire value increases by 2 instead of 4. Every four levels thereafter (9th, 13th, and
17th), the bonus on damage rolls increases by +1. This replaces gun training 1, 2, 3, and 4.
