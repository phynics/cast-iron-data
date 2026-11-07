+++
id = "ref/spell/atavism-mass"
kind = "spell"
title = "Mass Atavism"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "atavism_mass", path = "json/spells.json" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Druid", level = 8 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one animal/level, no two of which can be more than 30 ft. apart" },
]
duration = "1 minute/level"
saving_throw = "Fortitude negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 8: Druid
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Target: one animal/level, no two of which can be more than 30 ft. apart
Duration: 1 minute/level
Saving throw: Fortitude negates
Spell resistance: yes
:::

## Atavism

**Sources:** Ultimate Magic pg 207

By bringing forth the primeval ancestry of the target animal, you awaken a savage engine of
destruction. The animal immediately gains the advanced creature simple template. It gains a +2 bonus
on all rolls, including damage rolls and special ability DCs, a +4 bonus to AC and CMD, and +2 hit
points per HD. The animal's primal instincts take hold for the duration of this spell - if the
animal knows tricks granted by the Handle Animal skill, it loses access to all of those tricks save
for "attack." This spell has no effect on animals that already have the advanced creature template.

### Mass Atavism

**Sources:** Ultimate Magic pg 207

This spell functions as atavism, except that it affects multiple creatures.
