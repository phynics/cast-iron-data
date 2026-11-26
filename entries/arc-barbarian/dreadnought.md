+++
id = "ref/arc-barbarian/dreadnought"
kind = "archetype"
title = "Dreadnought"
aon = "ArchetypeDisplay.aspx?FixedName=Barbarian%20Dreadnought"
source_ids = ["horror-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "dreadnought", path = "json/archetypes_barbarian.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/barbarian" },
]
[[sources]]
publication = "horror-adventures"
page = "47"

[fields]
kind = "archetype"
features = [
  { anchor = "dead-calm" },
  { anchor = "steady-gait", level = 1 },
  { anchor = "fearless-killer", level = 14 },
  { anchor = "instant-dispassion", level = 17 },
]
trades = [
  { replaces = "Fast movement", feature = "fast-movement", by = ["steady-gait"] },
  { replaces = "Indomitable will", feature = "indomitable-will", by = ["fearless-killer"] },
  { replaces = "Tireless rage", feature = "tireless-rage", by = ["instant-dispassion"] },
  { alters = "Rage", feature = "rage", by = ["dead-calm"] },
]
+++

Unstoppable and fearless, the dreadnought turns the terror of her enemies into violent physical
power.

## Dead Calm (Ex) {#dead-calm}

A dreadnought can enter a dispassionate killing spree as a free action, granting her additional
combat prowess. The dreadnought gains only [half](ref/misc/fractions-and-rounding) the usual bonuses
from her rage but takes no penalty to her AC, can use all her normal skills and effects that require
concentration, and is not fatigued when her rage ends. The dreadnought cannot enter a rage for 1
minute after she ends her rage, and she cannot charge or run while under the effects of her rage.

This ability alters rage.

## Steady Gait (Ex) {#steady-gait}

A dreadnought advances steadily, shrugging off attempts to slow her advance. The dreadnought gains a
+1 bonus on saving throws and to her CMD against effects that would slow or immobilize her. This
bonus increases to +2 when she gains greater rage and +3 when she gains mighty rage.

This ability replaces fast movement.

## Fearless Killer (Su) {#fearless-killer}

Starting at 14th level, a dreadnought becomes implacable in her pursuit of slaughter. While in rage,
she is immune to fear effects.

This ability replaces indomitable will.

## Instant Dispassion (Ex) {#instant-dispassion}

At 17th level, a dreadnought can quickly turn her compassion on and off. She can enter a rage as
soon as she wants after ending a previous rage.

This ability replaces tireless rage.
