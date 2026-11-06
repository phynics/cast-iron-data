+++
id = "ref/spell/create-greater-undead"
kind = "spell"
title = "Create Greater Undead"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "create_greater_undead", path = "json/spells3.json" },
]

[fields]
kind = "spell"
school = "necromancy"
descriptors = ["evil"]
levels = [
  { class = "Arcanist", level = 8 },
  { class = "Cleric", level = 8 },
  { class = "Oracle", level = 8 },
  { class = "Shaman", level = 8 },
  { class = "Sorcerer", level = 8 },
  { class = "Wizard", level = 8 },
]
casting_time = "1 hour"
components = "V, S, M (a clay pot filled with grave dirt and an onyx gem worth at least 50 gp per HD of the undead to be created)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one corpse" },
]
duration = "instantaneous"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 8: Arcanist, Cleric, Oracle, Shaman, Sorcerer, Wizard
Casting time: 1 hour
Components: V, S, M (a clay pot filled with grave dirt and an onyx gem worth at least 50 gp per HD of the undead to be created)
Range: close (25 ft. + 5 ft./2 levels)
Duration: instantaneous
Saving throw: none
Spell resistance: no
Target: one corpse
Descriptors: evil
:::

**Sources:** PRPG Core Rulebook pg 261

This spell functions like create undead, except that you can create more powerful and intelligent
sorts of undead: shadows, wraiths, spectres, and devourers. The type or types of undead created is
based on caster level, as shown below.

|Caster Level|Undead Created|
| --- | --- |
|15th or lower|Shadow|
|16th-17th|Wraith|
|18th-19th|Spectre|
|20th or higher|Devourer|
