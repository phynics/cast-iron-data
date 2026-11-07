+++
id = "ref/spell/synesthesia-mass"
kind = "spell"
title = "Mass Synesthesia"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "synesthesia_mass", path = "json/spells10.json" },
]

[fields]
kind = "spell"
school = "illusion"
subschools = ["Phantasm"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Mesmerist", level = 5 },
  { class = "Psychic", level = 7 },
]
casting_time = "1 standard action"
components = "V, S"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Targets", value = "one or more living creatures, no two of which can be more than 30 ft. apart" },
]
duration = "1 round/level"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 5: Mesmerist\
7: Psychic
Casting time: 1 standard action
Components: V, S
Range: medium (100 ft. + 10 ft./level)
Targets: one or more living creatures, no two of which can be more than 30 ft. apart
Duration: 1 round/level
Saving throw: Will negates
Spell resistance: yes
Subschool: Phantasm
Descriptors: mind-affecting
:::

## Synesthesia

**Sources:** Occult Adventures pg 187

You overstimulate the senses of the affected creature, causing its senses to interfere with another.
While a creature is under the effects of this spell, sensory input is processed by the wrong senses,
such that noise triggers bursts of colors, smells create sounds, and so on. The affected creature
moves at half speed, has a 20% miss chance on attacks, and takes a -4 penalty to AC and on skill
checks and Reflex saves. Successful spellcasting while affected requires a
[concentration](ref/rule/concentration) check with a DC equal to this spell's save DC plus the level
of spell being cast.

In addition, the affected creature is considered distracted for the purpose of attempting Perception
checks. Effects that negate or reduce concealment do not affect the miss chance from synesthesia.

### Mass Synesthesia

**Sources:** Occult Adventures pg 188

This spell functions like synesthesia, except as noted above.
