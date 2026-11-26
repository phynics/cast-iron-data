+++
id = "ref/arc-ninja/hunting-serpent"
kind = "archetype"
title = "Hunting Serpent"
aon = "ArchetypeDisplay.aspx?FixedName=Ninja%20Hunting%20Serpent"
source_ids = ["villain-codex"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "hunting_serpent", path = "json/archetypes_ninja.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/ninja" },
]
[[sources]]
publication = "villain-codex"
page = "104"

[fields]
kind = "archetype"
features = [
  { anchor = "relentless-pursuit", level = 3 },
  { anchor = "death-mark", level = 4 },
  { anchor = "certain-demise", level = 10 },
]
trades = [
  { replaces = "No trace", feature = "no-trace", by = ["relentless-pursuit"] },
  { replaces = "Uncanny dodge", feature = "uncanny-dodge", by = ["death-mark"] },
  { replaces = "improved uncanny dodge", feature = "improved-uncanny-dodge", by = ["death-mark"] },
  { replaces = "ninja tricks gained at 12th and 16th levels", feature = "ninja-tricks", levels = [12, 16], by = ["death-mark"] },
  { replaces = "Ninja trick gained at 10th level", feature = "ninja-tricks", levels = [10], by = ["certain-demise"] },
  { alters = "Class skills" },
]
+++

The order dispatches specially trained killers to hunt relentlessly and fight from the shadows.

## Class Skills {#class-skills}

A hunting serpent gains Survival as a class skill but loses Knowledge (nobility).

This ability alters the ninja's class skills.

## Relentless Pursuit (Ex) {#relentless-pursuit}

At 3rd level, a hunting serpent gains a +1 bonus on Diplomacy checks to gather information and on
Survival checks to identify or follow tracks. The bonus increases by 1 for every 3 ninja levels
beyond 3rd.

This ability replaces no trace.

## Death Mark (Ex) {#death-mark}

At 4th level, as a swift action once per day, a hunting serpent can mark an opponent damaged by her
sneak attack for death. A hunting serpent gains a +1 competence bonus on attack and damage rolls
against an opponent affected by death mark as well as on Survival checks to track the marked
creature. The bonuses from death mark and its number of uses per day increase by 1 at 8th, 12th, and
16th levels. The effects of death mark last for 24 hours, until the marked creature is slain, or
until the hunting serpent chooses to mark another creature, whichever comes first.

This ability replaces uncanny dodge, improved uncanny dodge, and the ninja tricks gained at 12th and
16th levels.

## Certain Demise (Ex) {#certain-demise}

At 10th level, the hunting serpent's sneak attack damage applies on the first attack she makes each
round against the target of her death mark ability, even if it normally wouldn't. Other effects that
trigger on a sneak attack do not apply with this ability.

This ability replaces the ninja trick gained at 10th level.
