+++
id = "ref/spell/atavism"
kind = "spell"
title = "Atavism"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "atavism", path = "json/spells.json" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Druid", level = 4 },
  { class = "Hunter", level = 4 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one animal" },
]
duration = "1 minute/level"
saving_throw = "Fortitude negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 4: Druid, Hunter
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 minute/level
Saving throw: Fortitude negates
Spell resistance: yes
Target: one animal
:::

**Sources:** Ultimate Magic pg 207

By bringing forth the primeval ancestry of the target animal, you awaken a savage engine of
destruction. The animal immediately gains the advanced creature simple template. It gains a +2 bonus
on all rolls, including damage rolls and special ability DCs, a +4 bonus to AC and CMD, and +2 hit
points per HD. The animal's primal instincts take hold for the duration of this spell - if the
animal knows tricks granted by the Handle Animal skill, it loses access to all of those tricks save
for "attack." This spell has no effect on animals that already have the advanced creature template.
