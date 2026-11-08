+++
id = "ref/spell/planetary-adaptation-mass"
kind = "spell"
title = "Mass Planetary Adaptation"
source_ids = ["people-of-the-stars", "distant-worlds"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "planetary_adaptation_mass", path = "json/spells7.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/planetary-adaptation" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Arcanist", level = 7 },
  { class = "Cleric", level = 6 },
  { class = "Oracle", level = 6 },
  { class = "Sorcerer", level = 7 },
  { class = "Summoner", level = 6 },
  { class = "Unchained Summoner", level = 6 },
  { class = "Warpriest", level = 6 },
  { class = "Wizard", level = 7 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature/level, no two of which can be more than 30 ft. apart" },
]
duration = "1 hour/level"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 6: Cleric, Oracle, Summoner, Unchained Summoner, Warpriest\
7: Arcanist, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Target: one creature/level, no two of which can be more than 30 ft. apart
Duration: 1 hour/level
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
:::

## Planetary Adaptation

**Sources:** People of the Stars pg 29, Distant Worlds pg 55

This spell functions as planar adaptation, except that it works only on worlds of the Material
Plane. The cold void of space is considered a single world for the purpose of this spell, allowing
you to survive in vacuum.

### Mass Planetary Adaptation

**Sources:** People of the Stars pg 29

This spell functions as [planetary adaptation](ref/spell/planetary-adaptation), except as noted
above.
