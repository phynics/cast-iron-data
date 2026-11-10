+++
id = "ref/spell/dream-reality"
kind = "spell"
title = "Dream Reality"
source_ids = ["inner-sea-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "dream_reality", path = "json/spells13.json" },
]
[[sources]]
publication = "inner-sea-intrigue"
page = "60"

[fields]
kind = "spell"
school = "illusion"
subschools = ["Compulsion"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Alchemist", level = 5 },
  { class = "Arcanist", level = 6 },
  { class = "Bard", level = 5 },
  { class = "Cleric", level = 6 },
  { class = "Investigator", level = 5 },
  { class = "Mesmerist", level = 5 },
  { class = "Occultist", level = 5 },
  { class = "Oracle", level = 6 },
  { class = "Psychic", level = 6 },
  { class = "Skald", level = 5 },
  { class = "Sorcerer", level = 6 },
  { class = "Warpriest", level = 6 },
  { class = "Wizard", level = 6 },
]
casting_time = "1 standard action"
components = "V"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "1 minute/level (D)"
saving_throw = "Will disbelief"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 5: Alchemist, Bard, Investigator, Mesmerist, Occultist, Skald\
6: Arcanist, Cleric, Oracle, Psychic, Sorcerer, Warpriest, Wizard
Casting time: 1 standard action
Components: V
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 minute/level (D)
Saving throw: Will disbelief
Spell resistance: yes
Target: one creature
Subschool: Compulsion
Descriptors: mind-affecting
:::

You cause the target to perceive the world as if in a dream. When the spell ends, the target forgets
all identifying details of events that transpired while the spell lasted. The memories were not
taken from it; rather, its mind never recorded the memories as real in the first place. If
[modify memory](ref/spell/modify-memory) is cast upon it before the spell ends, the target remembers
these events. A target under the effect of [lullaby](ref/spell/lullaby) before this spell is cast
applies its penalty to the saving throw against this spell.
