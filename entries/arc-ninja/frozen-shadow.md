+++
id = "ref/arc-ninja/frozen-shadow"
kind = "archetype"
title = "Frozen Shadow"
aon = "ArchetypeDisplay.aspx?FixedName=Ninja%20Frozen%20Shadow"
source_ids = ["inner-sea-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "frozen_shadow", path = "json/archetypes_ninja.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/ninja" },
]
[[sources]]
publication = "inner-sea-intrigue"
page = "38"

[fields]
kind = "archetype"
features = [
  { anchor = "hardy-killer", level = 2 },
  { anchor = "track-victim", level = 4 },
  { anchor = "swift-tracker", level = 8 },
]
trades = [
  { replaces = "Ability to treat Acrobatics jump checks as if he had a running start", by = ["hardy-killer"] },
  { replaces = "ability to reduce Acrobatics jump checks by half", by = ["hardy-killer"] },
  { replaces = "Uncanny dodge", feature = "uncanny-dodge", by = ["track-victim"] },
  { replaces = "Improved uncanny dodge", feature = "improved-uncanny-dodge", by = ["swift-tracker"] },
  { alters = "Ki pool", feature = "ki-pool", by = ["hardy-killer"] },
  { alters = "Class skills" },
]
+++

Frozen shadows belong to a rare ninja clan operating in Avistan, having migrated to the Lands of the
Linnorm Kings decades ago. Most members are Tian, Ulfen, and Varki humans, and they work as thieves,
power brokers, and spies loosely guided by secretive masters with unknown agendas.

## Class Skills {#class-skills}

A frozen shadow adds Survival to his list of class skills, instead of Diplomacy.

This ability alters the ninja's class skills.

## Hardy Killer (Ex) {#hardy-killer}

At 2nd level, a frozen shadow has become incredibly inured to his surrounding climate. At the
beginning of any day, the frozen shadow can spend 1 point from his ki pool to benefit from the
effects of an _[endure elements](ref/spell/endure-elements)_ spell. The frozen shadow does not treat
any Acrobatics skill check to jump as if he had a running start, and at 10th level he cannot reduce
the DC of Acrobatics skill checks made to jump by half.

This ability alters ki pool.

## Track Victim (Ex) {#track-victim}

Starting at 4th level, a frozen shadow adds half his ninja level on Survival checks to follow tracks
and on Perception checks to see through disguises. Additionally, if the frozen shadow sees a
creature that has changed its appearance using the Disguise skill, he can always attempt a
Perception check to see through the disguise, even if the disguised creature did nothing to draw
attention to itself. The frozen shadow also gains a +2 bonus to Will saving throws when attempting
to disbelieve an illusion affecting a creature or creatures.

This ability replaces uncanny dodge.

## Swift Tracker (Ex) {#swift-tracker}

At 8th level, a frozen shadow can move at his normal speed while using Survival to follow tracks
without taking the normal -5 penalty. He takes only a -10 penalty (instead of the normal -20) when
moving up to twice his normal speed while tracking. Additionally, his bonus on Will saving throws to
disbelieve illusions affecting a creature or creatures increases to +4.

This replaces improved uncanny dodge.

## Ninja Tricks {#ninja-tricks}

The following ninja tricks complement the frozen shadow archetype:
[bleeding attack](ref/ninjatrick/bleeding-attack), [darkvision](ref/ninjatrick/darkvision),
[deadly range](ref/ninjatrick/deadly-range), [fast stealth](ref/ninjatrick/fast-stealth),
[hidden weapons](ref/ninjatrick/hidden-weapons), [sudden disguise](ref/ninjatrick/sudden-disguise),
[vanishing trick](ref/ninjatrick/vanishing-trick), and [wall climber](ref/ninjatrick/wall-climber).

## Advanced Ninja Tricks {#advanced-ninja-tricks}

The following advanced ninja tricks complement the frozen shadow archetype:
[assassinate](ref/ninjatrick/assassinate), [ghost step](ref/ninjatrick/ghost-step),
[invisible blade](ref/ninjatrick/invisible-blade),
[master disguise](ref/ninjatrick/master-disguise), and
[see the unseen](ref/ninjatrick/see-the-unseen).
