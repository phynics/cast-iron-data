+++
id = "ref/spell/mindlink"
kind = "spell"
title = "Mindlink"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "mindlink", path = "json/spells14.json" },
]

[fields]
kind = "spell"
school = "divination"
descriptors = ["mind-affecting"]
levels = [
  { class = "Arcanist", level = 1 },
  { class = "Medium", level = 1 },
  { class = "Mesmerist", level = 1 },
  { class = "Occultist", level = 1 },
  { class = "Psychic", level = 1 },
  { class = "Shaman", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Spiritualist", level = 1 },
  { class = "Wizard", level = 1 },
]
casting_time = "1 standard action"
components = "V"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "instantaneous"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 1: Arcanist, Medium, Mesmerist, Occultist, Psychic, Shaman, Sorcerer, Spiritualist, Wizard
Casting time: 1 standard action
Components: V
Range: touch
Duration: instantaneous
Saving throw: Will negates (harmless)
Spell resistance: yes
Target: creature touched
Descriptors: mind-affecting
:::

**Sources:** Occult Adventures pg 177

You link your mind to that of a touched creature to swiftly communicate a large amount of complex
information in an instant. You decide what the target learns, limited to any amount of information
that otherwise could be communicated in 10 minutes. This information comes in a series of visual
images and emotional sensations, and isn't language-dependent.
