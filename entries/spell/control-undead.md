+++
id = "ref/spell/control-undead"
kind = "spell"
title = "Control Undead"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "control_undead", path = "json/spells12.json" },
]

[fields]
kind = "spell"
school = "necromancy"
levels = [
  { class = "Arcanist", level = 7 },
  { class = "Sorcerer", level = 7 },
  { class = "Wizard", level = 7 },
]
casting_time = "1 standard action"
components = "V, S, M (a piece of bone and a piece of raw meat)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Targets", value = "up to 2 HD/level of undead creatures, no two of which can be more than 30 ft. apart" },
]
duration = "1 minute/level"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 7: Arcanist, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M (a piece of bone and a piece of raw meat)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 minute/level
Saving throw: Will negates
Spell resistance: yes
Targets: up to 2 HD/level of undead creatures, no two of which can be more than 30 ft. apart
:::

**Sources:** PRPG Core Rulebook pg 260

This spell enables you to control undead creatures for a short period of time. You command them by
voice and they understand you, no matter what language you speak. Even if vocal communication is
impossible, the controlled undead do not attack you. At the end of the spell, the subjects revert to
their normal behavior.

Intelligent undead creatures remember that you controlled them, and they may seek revenge after the
spell's effects end.
