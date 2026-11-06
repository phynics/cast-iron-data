+++
id = "ref/spell/synesthesia"
kind = "spell"
title = "Synesthesia"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "synesthesia", path = "json/spells10.json" },
]

[fields]
kind = "spell"
school = "illusion"
subschools = ["Phantasm"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Mesmerist", level = 3 },
  { class = "Psychic", level = 3 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Targets", value = "one living creature" },
]
duration = "1 round/level"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 3: Mesmerist, Psychic
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level
Saving throw: Will negates
Spell resistance: yes
Targets: one living creature
Subschool: Phantasm
Descriptors: mind-affecting
:::

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
