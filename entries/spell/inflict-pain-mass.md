+++
id = "ref/spell/inflict-pain-mass"
kind = "spell"
title = "Mass Inflict Pain"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "inflict_pain_mass", path = "json/spells14.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/inflict-pain" },
]
[[sources]]
publication = "occult-adventures"
page = "174"

[fields]
kind = "spell"
school = "enchantment"
descriptors = ["mind-affecting", "pain"]
levels = [
  { class = "Antipaladin", level = 4 },
  { class = "Arcanist", level = 7 },
  { class = "Inquisitor", level = 5 },
  { class = "Medium", level = 4 },
  { class = "Mesmerist", level = 5 },
  { class = "Occultist", level = 5 },
  { class = "Psychic", level = 6 },
  { class = "Sorcerer", level = 7 },
  { class = "Spiritualist", level = 5 },
  { class = "Witch", level = 7 },
  { class = "Wizard", level = 7 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature/level, no two of which can be more than 30 ft. apart." },
]
duration = "1 round/level"
saving_throw = "Will partial, see text"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 4: Antipaladin, Medium\
5: Inquisitor, Mesmerist, Occultist, Spiritualist\
6: Psychic\
7: Arcanist, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level
Saving throw: Will partial, see text
Spell resistance: yes
Target: one creature/level, no two of which can be more than 30 ft. apart.
Descriptors: mind-affecting, pain
:::

This spell functions like [inflict pain](ref/spell/inflict-pain) except as noted above.
