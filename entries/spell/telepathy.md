+++
id = "ref/spell/telepathy"
kind = "spell"
title = "Telepathy"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "telepathy", path = "json/spells10.json" },
]

[fields]
kind = "spell"
school = "divination"
descriptors = ["mind-affecting"]
levels = [
  { class = "Arcanist", level = 6 },
  { class = "Medium", level = 4 },
  { class = "Mesmerist", level = 4 },
  { class = "Psychic", level = 5 },
  { class = "Sorcerer", level = 6 },
  { class = "Spiritualist", level = 6 },
  { class = "Wizard", level = 6 },
]
casting_time = "1 standard action"
components = "V"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 minute/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 4: Medium, Mesmerist\
5: Psychic\
6: Arcanist, Sorcerer, Spiritualist, Wizard
Casting time: 1 standard action
Components: V
Range: personal
Duration: 1 minute/level
Saving throw: none
Spell resistance: no
Target: you
Descriptors: mind-affecting
:::

**Sources:** Occult Adventures pg 189

You can mentally communicate with any other creature within 100 feet that has a language. It is
possible to address multiple creatures at once telepathically, although maintaining a telepathic
conversation with more than one creature at a time is just as difficult as speaking and listening to
multiple people simultaneously.
