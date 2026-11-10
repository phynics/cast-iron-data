+++
id = "ref/spell/modify-memory"
kind = "spell"
title = "Modify Memory"
aon = "SpellDisplay.aspx?ItemName=Modify%20Memory"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "modify_memory", path = "json/spells14.json" },
]
[[sources]]
publication = "core-rulebook"
page = "315"

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
