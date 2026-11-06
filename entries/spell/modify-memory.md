+++
id = "ref/spell/modify-memory"
kind = "spell"
title = "Modify Memory"
source_ids = ["core-rulebook", "mythic-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "modify_memory", path = "json/spells14.json" },
]

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Bard", level = 4 },
  { class = "Medium", level = 4 },
  { class = "Mesmerist", level = 4 },
  { class = "Psychic", level = 5 },
  { class = "Skald", level = 4 },
]
casting_time = "1 round; see text"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one living creature" },
]
duration = "permanent"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 4: Bard, Medium, Mesmerist, Skald\
5: Psychic
Casting time: 1 round; see text
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: permanent
Saving throw: Will negates
Spell resistance: yes
Target: one living creature
Subschool: Compulsion
Descriptors: mind-affecting
:::

**Sources:** PRPG Core Rulebook pg 315

You reach into the subject's mind and modify as many as 5 minutes of its memories in one of the
following ways.

- Eliminate all memory of an event the subject actually experienced. This spell cannot negate charm,
  geas/quest, suggestion, or similar spells.
- Allow the subject to recall with perfect clarity an event it actually experienced.
- Change the details of an event the subject actually experienced.
- Implant a memory of an event the subject never experienced.

Casting the spell takes 1 round. If the subject fails to save, you proceed with the spell by
spending as much as 5 minutes (a period of time equal to the amount of memory you want to modify)
visualizing the memory you wish to modify in the subject. If your concentration is disturbed before
the visualization is complete, or if the subject is ever beyond the spell's range during this time,
the spell is lost.

A modified memory does not necessarily affect the subject's actions, particularly if it contradicts
the creature's natural inclinations. An illogical modified memory is dismissed by the creature as a
bad dream, too much wine, or another similar excuse.

### Mythic Modify Memory

**Sources:** Mythic Adventures pg 102\
You can modify an additional 5 minutes of the subject's memory per tier. You may affect multiple
memories with one casting of the spell, as long as the total number of minutes doesn't exceed this
limit. Each affected memory counts as a minimum of 5 minutes. For example, you could implant a
memory of having a brief meeting with the mayor before lunch and another brief meeting just after
dinner, even though the two events would have been hours apart.

_Augmented (8th):_ If you expend four uses of mythic power, instead of altering the target's
memories, you alter all other creatures' memories of the target (only the target gets a saving throw
against the spell). All creatures on the same plane as the target forget his name, their
relationship to him, and everything he has done; he is essentially a stranger to them. Any important
acts by the target are attributed to someone else. Everyone's memories of history are rewritten to
incorporate this change. The target's memories are unaffected. You can exclude a number of other
creatures up to your tier from the effects of this spell (so they remember the truth), including
yourself if you wish. Written records are unchanged unless you expend an additional six uses of
mythic power when you cast the spell, and written records on other planes remain unchanged
regardless.
