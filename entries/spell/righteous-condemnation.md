+++
id = "ref/spell/righteous-condemnation"
kind = "spell"
title = "Righteous Condemnation"
source_ids = ["plane-hoppers-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "righteous_condemnation", path = "json/spells8.json" },
]

[fields]
kind = "spell"
school = "abjuration"
descriptors = ["good", "lawful"]
levels = [
  { class = "Cleric", level = 3 },
  { class = "Inquisitor", level = 3 },
  { class = "Oracle", level = 3 },
  { class = "Paladin", level = 2 },
  { class = "Warpriest", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 round/level (D)"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 2: Paladin\
3: Cleric, Inquisitor, Oracle, Warpriest
Casting time: 1 standard action
Components: V, S, DF
Range: personal
Duration: 1 round/level (D)
Saving throw: Will negates
Spell resistance: yes
Target: you
Descriptors: good, lawful
:::

**Sources:** Plane-Hopper's Handbook pg 13

Any creature of chaotic, neutral, or evil alignment who targets you with a spell must succeed at a
Will save or take a -4 penalty on Intelligence-, Wisdom-, and Charisma-based checks for the spell's
duration. Creatures with only neutral alignment components receive a +4 bonus on their Will saves
against this spell. The penalties for alignment components stack (therefore, a chaotic evil
spellcaster would take a -8 penalty).
