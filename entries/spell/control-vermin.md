+++
id = "ref/spell/control-vermin"
kind = "spell"
title = "Control Vermin"
source_ids = ["monster-codex"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "control_vermin", path = "json/spells12.json" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Cleric", level = 3 },
  { class = "Druid", level = 2 },
  { class = "Hunter", level = 2 },
  { class = "Oracle", level = 3 },
  { class = "Ranger", level = 4 },
  { class = "Sorcerer", level = 3 },
  { class = "Warpriest", level = 3 },
  { class = "Witch", level = 2 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, M/DF (a beetle)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "up to 1 HD/level of vermin, no two of which can be more than 30 ft. apart" },
]
duration = "1 hour/level"
saving_throw = "Will negates"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 2: Druid, Hunter, Witch\
3: Arcanist, Cleric, Oracle, Sorcerer, Warpriest, Wizard\
4: Ranger
Casting time: 1 standard action
Components: V, S, M/DF (a beetle)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 hour/level
Saving throw: Will negates
Spell resistance: no
Target: up to 1 HD/level of vermin, no two of which can be more than 30 ft. apart
:::

**Sources:** Monster Codex pg 45

You and a number of allies less than or equal to your caster level designated upon casting can use
Handle Animal and Ride checks to influence or control the targeted vermin as if they were animals
and had animal-level intelligence.
