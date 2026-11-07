+++
id = "ref/spell/homeward-bound"
kind = "spell"
title = "Homeward Bound"
source_ids = ["planar-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "homeward_bound", path = "json/spells13.json" },
]

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Cleric", level = 3 },
  { class = "Oracle", level = 3 },
  { class = "Sorcerer", level = 4 },
  { class = "Warpriest", level = 3 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 minute"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "one willing extraplanar creature" },
]
duration = "instantaneous"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 3: Cleric, Oracle, Warpriest\
4: Arcanist, Sorcerer, Wizard
Casting time: 1 minute
Components: V, S
Range: touch
Target: one willing extraplanar creature
Duration: instantaneous
Saving throw: Will negates (harmless)
Spell resistance: yes
:::

## Dismissal

**Sources:** PRPG Core Rulebook pg 271

This spell forces an extraplanar creature back to its proper plane if it fails a Will save. If the
spell is successful, the creature is instantly whisked away, but there is a 20% chance of actually
sending the subject to a plane other than its own.

### Homeward Bound

**Sources:** Planar Adventures pg 41

This spell functions as dismissal, except as noted above.
