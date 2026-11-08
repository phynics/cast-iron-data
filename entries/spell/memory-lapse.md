+++
id = "ref/spell/memory-lapse"
kind = "spell"
title = "Memory Lapse"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "memory_lapse", path = "json/spells14.json" },
]

[fields]
kind = "spell"
school = "enchantment"
descriptors = ["mind-affecting"]
levels = [
  { class = "Arcanist", level = 1 },
  { class = "Bard", level = 1 },
  { class = "Mesmerist", level = 1 },
  { class = "Occultist", level = 1 },
  { class = "Skald", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Wizard", level = 1 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one living creature" },
]
duration = "instantaneous"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 1: Arcanist, Bard, Mesmerist, Occultist, Skald, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: instantaneous
Saving throw: Will negates
Spell resistance: yes
Target: one living creature
Descriptors: mind-affecting
:::

**Sources:** Advanced Player's Guide pg 232

You cause the target to forget what happened from the casting of the spell back to the beginning of
its last turn. This may allow a retry on a Diplomacy, Intimidate, or opposed skill check, though
only with respect to the target, not other creatures that may be present.
