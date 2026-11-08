+++
id = "ref/spell/spindrift-spritz-mass"
kind = "spell"
title = "Mass Spindrift Spritz"
source_ids = ["elemental-masters-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "spindrift_spritz_mass", path = "json/spells9.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/spindrift-spritz" },
]

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Healing"]
descriptors = ["water"]
levels = [
  { class = "Cleric", level = 4 },
  { class = "Druid", level = 4 },
  { class = "Hunter", level = 3 },
  { class = "Inquisitor", level = 4 },
  { class = "Oracle", level = 4 },
  { class = "Paladin", level = 3 },
  { class = "Ranger", level = 3 },
  { class = "Shaman", level = 4 },
  { class = "Spiritualist", level = 4 },
  { class = "Warpriest", level = 4 },
]
casting_time = "1 immediate action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature/level, no two of which can be more than 20 ft. apart" },
]
duration = "instantaneous"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 3: Hunter, Paladin, Ranger\
4: Cleric, Druid, Inquisitor, Oracle, Shaman, Spiritualist, Warpriest
Casting time: 1 immediate action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Target: one creature/level, no two of which can be more than 20 ft. apart
Duration: instantaneous
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
Subschool: Healing
Descriptors: water
:::

## Spindrift Spritz

**Sources:** Elemental Master's Handbook pg 14

You can cast this spell only as a response to a target attempting a saving throw against an effect
that would cause the fatigued, shaken, sickened, or staggered conditions. The target can roll its
saving throw twice and take the higher result.

### Mass Spindrift Spritz

**Sources:** Elemental Master's Handbook pg 14

This spell functions as [spindrift spritz](ref/spell/spindrift-spritz), except as noted above.
