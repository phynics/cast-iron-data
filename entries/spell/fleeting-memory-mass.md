+++
id = "ref/spell/fleeting-memory-mass"
kind = "spell"
title = "Mass Fleeting Memory"
source_ids = ["black-markets"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "fleeting_memory_mass", path = "json/spells4.json" },
]

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Arcanist", level = 8 },
  { class = "Bard", level = 6 },
  { class = "Skald", level = 6 },
  { class = "Sorcerer", level = 8 },
  { class = "Wizard", level = 8 },
]
casting_time = "1 standard action"
components = "V"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature/level, no two of which can be more than 30 ft. apart" },
]
duration = "1 round/level (D)"
saving_throw = "Will partial"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 6: Bard, Skald\
8: Arcanist, Sorcerer, Wizard
Casting time: 1 standard action
Components: V
Range: close (25 ft. + 5 ft./2 levels)
Target: one creature/level, no two of which can be more than 30 ft. apart
Duration: 1 round/level (D)
Saving throw: Will partial
Spell resistance: yes
Subschool: Compulsion
Descriptors: mind-affecting
:::

## Fleeting Memory

**Sources:** Black Markets pg 24

You create a gap in the target's memory, preventing the target from remembering anything that
happens from the moment you cast this spell until the moment its complete duration ends. Fleeting
memory doesn't wipe out its target's memories until the end of its duration, so the target can
remember the preceding rounds until the spell's duration ends. If the spell ends prematurely, either
because you dismiss it or because it is dispelled, it disperses without affecting its target's
memory.

Whether or not the target's save is successful, the target forgets that you cast a spell.

### Mass Fleeting Memory

**Sources:** Black Markets pg 25

This spell functions as fleeting memory, except that it affects multiple creatures.
