+++
id = "ref/spell/suspend-drowning"
kind = "spell"
title = "Suspend Drowning"
source_ids = ["blood-of-the-sea"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "suspend_drowning", path = "json/spells10.json" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Bard", level = 1 },
  { class = "Cleric", level = 1 },
  { class = "Druid", level = 1 },
  { class = "Hunter", level = 1 },
  { class = "Oracle", level = 1 },
  { class = "Ranger", level = 1 },
  { class = "Skald", level = 1 },
  { class = "Warpriest", level = 1 },
]
casting_time = "1 immediate action"
components = "V"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Targets", value = "one Medium creatures or smaller drowning creature/level, no two of which can be more than 20 ft. apart" },
]
duration = "1 round/level"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 1: Bard, Cleric, Druid, Hunter, Oracle, Ranger, Skald, Warpriest
Casting time: 1 immediate action
Components: V
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
Targets: one Medium creatures or smaller drowning creature/level, no two of which can be more than 20 ft. apart
:::

**Sources:** Blood of the Sea pg 21

The affected creatures immediately - though temporarily - stop drowning and cannot suffocate or
drown while this spell is in effect. A target that had been reduced to below 1 hit point from
drowning immediately returns to 1 hit point. The magic of this spell allows the targets to breathe,
drink, and talk normally for the duration of the spell, but targets cannot inhale to increase the
amount of air remaining in their lungs. When the spell effect ends, the target resumes drowning
unless it is in an environment that allows it to breathe normally (such as an air-breathing creature
returning to the surface) or has obtained a method of breathing normally (such as by consuming a
potion of water breathing).
