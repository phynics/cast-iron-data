+++
id = "ref/spell/invigorate-mass"
kind = "spell"
title = "Mass Invigorate"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "invigorate_mass", path = "json/spells14.json" },
]

[fields]
kind = "spell"
school = "illusion"
subschools = ["Figment"]
levels = [
  { class = "Bard", level = 3 },
  { class = "Mesmerist", level = 3 },
  { class = "Psychic", level = 4 },
  { class = "Skald", level = 3 },
]
casting_time = "1 standard action"
components = "V"
range = "touch"
effects = [
  { label = "Targets", value = "creatures touched, up to one/level" },
]
duration = "10 minutes/level (D)"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 3: Bard, Mesmerist, Skald\
4: Psychic
Casting time: 1 standard action
Components: V
Range: touch
Targets: creatures touched, up to one/level
Duration: 10 minutes/level (D)
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
Subschool: Figment
:::

## Invigorate

**Sources:** Advanced Player's Guide pg 230

This spell banishes feelings of weariness. For the duration, the subject takes no penalties from the
fatigued or exhausted conditions. The effect of invigorate is merely an illusion, however, not a
substitute for actual rest or respite. When the spell ends, the subject takes 1d6 points of
nonlethal damage, along with the return of the original condition(s). A creature can be under the
effects of only one invigorate spell at a time; if it is cast a second time on that creature, the
first effect immediately ends.

### Mass Invigorate

**Sources:** Advanced Player's Guide pg 230

This spell works as invigorate, except that it affects multiple creatures.
