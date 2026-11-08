+++
id = "ref/spell/invigorate-mass"
kind = "spell"
title = "Mass Invigorate"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "invigorate_mass", path = "json/spells14.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/invigorate" },
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

### Mass Invigorate

**Sources:** Advanced Player's Guide pg 230

This spell works as [invigorate](ref/spell/invigorate), except that it affects multiple creatures.
