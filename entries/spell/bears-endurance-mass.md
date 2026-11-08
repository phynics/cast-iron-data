+++
id = "ref/spell/bears-endurance-mass"
kind = "spell"
title = "Mass Bear's Endurance"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "bears_endurance_mass", path = "json/spells12.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/bears-endurance" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Arcanist", level = 6 },
  { class = "Cleric", level = 6 },
  { class = "Druid", level = 6 },
  { class = "Hunter", level = 6 },
  { class = "Magus", level = 6 },
  { class = "Oracle", level = 6 },
  { class = "Psychic", level = 6 },
  { class = "Shaman", level = 6 },
  { class = "Sorcerer", level = 6 },
  { class = "Summoner", level = 4 },
  { class = "Unchained Summoner", level = 6 },
  { class = "Warpriest", level = 6 },
  { class = "Wizard", level = 6 },
]
casting_time = "1 standard action"
components = "V, S, M/DF (a few hairs, or a pinch of dung, from a bear)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Targets", value = "one creature/level, no two of which can be more than 30 ft. apart" },
]
duration = "1 minute/level"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 4: Summoner\
6: Arcanist, Cleric, Druid, Hunter, Magus, Oracle, Psychic, Shaman, Sorcerer, Unchained Summoner, Warpriest, Wizard
Casting time: 1 standard action
Components: V, S, M/DF (a few hairs, or a pinch of dung, from a bear)
Range: close (25 ft. + 5 ft./2 levels)
Targets: one creature/level, no two of which can be more than 30 ft. apart
Duration: 1 minute/level
Saving throw: Will negates (harmless)
Spell resistance: yes
:::

## Bear's Endurance

**Sources:** PRPG Core Rulebook pg 246

The affected creature gains greater vitality and stamina. The spell grants the subject a +4
enhancement bonus to Constitution, which adds the usual benefits to hit points, Fortitude saves,
Constitution checks, and so forth. Hit points gained by a temporary increase in Constitution score
are not temporary hit points. They go away when the subject's Constitution drops back to normal.
They are not lost first as temporary hit points are.

### Mass Bear's Endurance

**Sources:** PRPG Core Rulebook pg 247

Mass [bear's endurance](ref/spell/bears-endurance) works like bear's endurance, except that it
affects multiple creatures.
