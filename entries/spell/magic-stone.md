+++
id = "ref/spell/magic-stone"
kind = "spell"
title = "Magic Stone"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "magic_stone", path = "json/spells6.json" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Cleric", level = 1 },
  { class = "Druid", level = 1 },
  { class = "Hunter", level = 1 },
  { class = "Oracle", level = 1 },
  { class = "Shaman", level = 1 },
  { class = "Warpriest", level = 1 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "touch"
effects = [
  { label = "Targets", value = "up to three pebbles touched" },
]
duration = "30 minutes or until discharged"
saving_throw = "Will negates (harmless) (object)"
spell_resistance = "yes (harmless) (object)"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 1: Cleric, Druid, Hunter, Oracle, Shaman, Warpriest
Casting time: 1 standard action
Components: V, S, DF
Range: touch
Duration: 30 minutes or until discharged
Saving throw: Will negates (harmless) (object)
Spell resistance: yes (harmless) (object)
Targets: up to three pebbles touched
:::

**Sources:** PRPG Core Rulebook pg 310

You transmute as many as three pebbles, which can be no larger than sling bullets, so that they
strike with great force when thrown or slung. If hurled, they have a range increment of 20 feet. If
slung, treat them as sling bullets (range increment 50 feet). The spell gives them a +1 enhancement
bonus on attack and damage rolls. The user of the stones makes a normal ranged attack. Each stone
that hits deals 1d6+1 points of damage (including the spell's enhancement bonus), or 2d6+2 points
against undead.
