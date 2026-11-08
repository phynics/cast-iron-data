+++
id = "ref/spell/create-mindscape-greater"
kind = "spell"
title = "Greater Create Mindscape"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "create_mindscape_greater", path = "json/spells3.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/create-mindscape" },
]

[fields]
kind = "spell"
school = "illusion"
subschools = ["Phantasm"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Arcanist", level = 7 },
  { class = "Mesmerist", level = 6 },
  { class = "Psychic", level = 6 },
  { class = "Sorcerer", level = 7 },
  { class = "Wizard", level = 7 },
]
casting_time = "1 round"
components = "V, S"
range = "long (400 ft. + 40 ft./level)"
effects = [
  { label = "Target", value = "one creature/level" },
]
duration = "1 day/level"
saving_throw = "Will disbelief, see text"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 6: Mesmerist, Psychic\
7: Arcanist, Sorcerer, Wizard
Casting time: 1 round
Components: V, S
Range: long (400 ft. + 40 ft./level)
Target: one creature/level
Duration: 1 day/level
Saving throw: Will disbelief, see text
Spell resistance: yes
Subschool: Phantasm
Descriptors: mind-affecting
:::

### Greater Create Mindscape

**Sources:** Occult Adventures pg 163

This spell functions like [create mindscape](ref/spell/create-mindscape), except it can affect more
creatures, the mindscape lasts longer, and you can choose the mindscape's magic trait. You can also
direct a number of believable creatures at a time equal to your caster level.

Greater create mindscape can be made permanent with a [permanency](ref/spell/permanency) spell by a
caster of 15th level or higher at a cost of 17,500 gp. You and other creatures aware of a permanent
mindscape can come and go using the mindscape door spell.
