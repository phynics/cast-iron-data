+++
id = "ref/spell/blessing-of-luck-and-resolve-mass"
kind = "spell"
title = "Mass Blessing of Luck and Resolve"
source_ids = ["advanced-race-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "blessing_of_luck_and_resolve_mass", path = "json/spells2.json" },
]

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Cleric", level = 6 },
  { class = "Inquisitor", level = 6 },
  { class = "Oracle", level = 6 },
  { class = "Paladin", level = 4 },
  { class = "Warpriest", level = 6 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Targets", value = "one creature/level, no two of which can be more than 30 ft. apart" },
]
duration = "1 minute/level (d), special see below"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 4: Paladin\
6: Cleric, Inquisitor, Oracle, Warpriest
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Targets: one creature/level, no two of which can be more than 30 ft. apart
Duration: 1 minute/level (d), special see below
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
Subschool: Compulsion
Descriptors: mind-affecting
:::

## Blessing of Luck and Resolve

**Sources:** Advanced Race Guide pg 68

> _[Halflings](ref/race/halfling) have access to the following spells._

A favored blessing of halfling clerics, this spell grants its target a +2 morale bonus on saving
throws against fear effects. If the target has the fearless racial trait, it is immune to fear
instead. If the target fails a saving throw against fear, it can end the spell as an immediate
action to reroll the save with a +4 morale bonus, and must take the new result, even if it is worse.

### Mass Blessing of Luck and Resolve

**Sources:** Advanced Race Guide pg 68

This spell functions like blessing of luck and resolve, except that it affects multiple creatures.
