+++
id = "ref/spell/spell-absorption-greater"
kind = "spell"
title = "Greater Spell Absorption"
source_ids = ["inner-sea-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "spell_absorption_greater", path = "json/spells9.json" },
]

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Arcanist", level = 5 },
  { class = "Sorcerer", level = 5 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 round"
components = "V, S, M (a prism)"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 round/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 5: Arcanist, Sorcerer, Wizard
Casting time: 1 round
Components: V, S, M (a prism)
Range: personal
Duration: 1 round/level
Saving throw: none
Spell resistance: no
Target: you
:::

## Spell Absorption

**Sources:** Inner Sea Magic pg 61

If you successfully counterspell a 3rd-level or lower level spell (through either
[dispel magic](ref/spell/dispel-magic) or normal means) while spell absorption is in effect, you
absorb the countered spell and use it to regain spells you have already cast. If you're a wizard,
you regain the use of any single spell that you have cast since the last time you prepared spells.
If you're a sorcerer, you regain a single spell slot. The spell recovered or spell slot regained
must be of an equal level or lower than the spell you counterspelled.

### Greater Spell Absorption

**Sources:** Inner Sea Magic pg 61

This spell functions as spell absorption, save that you can absorb countered spells of 6th level or
lower.
