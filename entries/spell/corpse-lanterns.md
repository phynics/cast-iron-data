+++
id = "ref/spell/corpse-lanterns"
kind = "spell"
title = "Corpse Lanterns"
source_ids = ["pathfinder-society-field-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "corpse_lanterns", path = "json/spells12.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/dancing-lights" },
]

[fields]
kind = "spell"
school = "necromancy"
descriptors = ["light"]
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Witch", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Effect", value = "up to 4 lights, all within a 10-ft.-radius area" },
]
duration = "1 minute/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 2: Arcanist, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: medium (100 ft. + 10 ft./level)
Duration: 1 minute/level (D)
Saving throw: none
Spell resistance: no
Effect: up to 4 lights, all within a 10-ft.-radius area
Descriptors: light
:::

**Sources:** Pathfinder Society Field Guide pg 57

This spell functions as [dancing lights](ref/spell/dancing-lights), except it summons up to four
spheres of light, each of which glows a sickly pale green. These corpse lanterns shed dim light in a
20-foot radius, and do not increase the light level in areas of normal light or bright light. In dim
or normal light, the radiance of corpse lanterns provides a strange contrast, giving all creatures
in the area a -5 penalty on Stealth checks. In addition, the hue interferes with illusion (pattern)
spells, giving all creatures in the illuminated area a +2 bonus on any saving throws against such
spells. Unlike dancing lights, you may have more than one corpse lanterns spell active at a time,
but you may only move one set in any given round. Moving the corpse lanterns does not require
concentration. Corpse lanterns can be made permanent on an area with a
[permanency](ref/spell/permanency) spell by a caster of at least 11th level for the cost of 7,500
gp.
