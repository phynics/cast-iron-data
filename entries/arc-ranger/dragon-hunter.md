+++
id = "ref/arc-ranger/dragon-hunter"
kind = "archetype"
title = "Dragon Hunter"
aon = "ArchetypeDisplay.aspx?FixedName=Ranger%20Dragon%20Hunter"
source_ids = ["dragonslayers-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "dragon_hunter", path = "json/archetypes_ranger.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/ranger" },
]
[[sources]]
publication = "dragonslayers-handbook"
page = "22"

[fields]
kind = "archetype"
features = [
  { anchor = "predatory-deduction", level = 1 },
  { anchor = "wyrm-hatred", level = 1 },
  { anchor = "dragoncrafting", level = 5 },
  { anchor = "undaunted", level = 10 },
  { anchor = "expert-dragoncrafter", level = 15 },
  { anchor = "elemental-resilience", level = 20 },
]
trades = [
  { replaces = "Track", feature = "track", by = ["predatory-deduction"] },
  { replaces = "The additional favored enemy and any bonuses to existing favored enemies gained at 5th level", feature = "favored-enemy", levels = [5], by = ["dragoncrafting"] },
  { replaces = "The additional favored enemy and any bonuses to existing favored enemies gained at 10th level", feature = "favored-enemy", levels = [10], by = ["undaunted"] },
  { replaces = "The additional favored enemy and any bonuses to existing favored enemies gained at 15th level", feature = "favored-enemy", levels = [15], by = ["expert-dragoncrafter"] },
  { replaces = "The additional favored enemy and any bonuses to existing favored enemies gained at 20th level", feature = "favored-enemy", levels = [20], by = ["elemental-resilience"] },
]
+++

The quintessential dragonslayers, dragon hunters are experts at forging through the wilds in search
of great wyrms. Dragon hunters have the following class features.

## Class Skills {#class-skills}

A dragon hunter adds Knowledge (arcana) to his list of class skills, in addition to the normal
ranger class skills.

## Predatory Deduction (Ex) {#predatory-deduction}

Beginning at 1st level, when a dragon hunter successfully uses Survival to spot the trail of a
creature of the dragon type, the hunter may attempt an immediate DC 15 Knowledge (arcana) check. On
a success, the dragon hunter is able to deduce the species, age category, size, and color of the
dragon. If the trail is less than 48 hours old, the dragon hunter gains a +2 circumstance bonus on
the Knowledge check. This ability replaces Track.

## Wyrm Hatred (Ex) {#wyrm-hatred}

Beginning at 1st level, a dragon hunter must select dragons as his favored enemy, granting him a +2
bonus on Bluff, Knowledge, Perception, Sense Motive, and Survival checks against creatures of the
dragon type. He also gains +2 bonuses on weapon attack and damage rolls against them. These bonuses
increase by +2 at 5th level and every five levels thereafter (10th, 15th, and 20th level).

## Dragoncrafting (Ex) {#dragoncrafting}

Dragon hunters are experts not only at tracking and killing dragons, but also at using dragon bodies
to craft unique equipment. A dragon hunter gains [Dragoncrafting](ref/feat/dragoncrafting) as a
bonus feat at 5th level, even if she does not meet the prerequisites. See page 18 of this book for
more information. This ability replaces the additional favored enemy and any bonuses to existing
favored enemies gained at 5th level.

## Undaunted (Ex) {#undaunted}

Beginning at 10th level, a dragon hunter gains a +4 bonus on Will saves made to resist
mind-affecting fear effects, Reflex saves made to avoid damage from breath weapons, Reflex saves
made to avoid crush attacks, and Reflex saves made to avoid damage from tail sweep attacks. This
ability replaces the additional favored enemy and any bonuses to existing favored enemies gained at
10th level.

## Expert Dragoncrafter (Ex) {#expert-dragoncrafter}

At 15th level, a dragon hunter may take 10 on Heal and Craft skill checks to harvest dragoncraft
materials and to create dragoncraft items. Additionally, the amount of time required to create a
dragoncraft item is reduced by half. This ability replaces the additional favored enemy and any
bonuses to existing favored enemies gained at 15th level.

## Elemental Resilience (Su) {#elemental-resilience}

At 20th level, a dragon hunter gains energy [resistance](ref/umr/resistance) 30 against a single
energy type for 1 hour. The energy types he may choose are acid, cold, electricity, and fire. He may
use this ability once per day. This ability replaces the additional favored enemy and any bonuses to
existing favored enemies gained at 20th level.
