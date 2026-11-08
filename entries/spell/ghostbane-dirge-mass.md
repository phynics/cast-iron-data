+++
id = "ref/spell/ghostbane-dirge-mass"
kind = "spell"
title = "Mass Ghostbane Dirge"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "ghostbane_dirge_mass", path = "json/spells13.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/ghostbane-dirge" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Bard", level = 4 },
  { class = "Cleric", level = 5 },
  { class = "Inquisitor", level = 5 },
  { class = "Occultist", level = 5 },
  { class = "Oracle", level = 5 },
  { class = "Paladin", level = 3 },
  { class = "Shaman", level = 5 },
  { class = "Skald", level = 4 },
  { class = "Warpriest", level = 5 },
]
casting_time = "1 standard action"
components = "V, S, M/DF (an old reed from a wind instrument)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one incorporeal creature/level, no two of which can be more than 30 ft. apart" },
]
duration = "1 round/level"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 3: Paladin\
4: Bard, Skald\
5: Cleric, Inquisitor, Occultist, Oracle, Shaman, Warpriest
Casting time: 1 standard action
Components: V, S, M/DF (an old reed from a wind instrument)
Range: close (25 ft. + 5 ft./2 levels)
Target: one incorporeal creature/level, no two of which can be more than 30 ft. apart
Duration: 1 round/level
Saving throw: Will negates
Spell resistance: yes
:::

### Mass Ghostbane Dirge

**Sources:** Advanced Player's Guide pg 225

This spell functions as [ghostbane dirge](ref/spell/ghostbane-dirge), except that it affects
multiple targets.
