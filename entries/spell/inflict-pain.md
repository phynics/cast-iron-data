+++
id = "ref/spell/inflict-pain"
kind = "spell"
title = "Inflict Pain"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "inflict_pain", path = "json/spells14.json" },
]
[[sources]]
publication = "occult-adventures"
page = "174"

[fields]
kind = "spell"
school = "enchantment"
descriptors = ["mind-affecting", "pain"]
levels = [
  { class = "Antipaladin", level = 2 },
  { class = "Arcanist", level = 3 },
  { class = "Inquisitor", level = 2 },
  { class = "Medium", level = 2 },
  { class = "Mesmerist", level = 2 },
  { class = "Occultist", level = 2 },
  { class = "Psychic", level = 2 },
  { class = "Sorcerer", level = 3 },
  { class = "Spiritualist", level = 2 },
  { class = "Witch", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "1 round/level"
saving_throw = "Will partial, see text"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 2: Antipaladin, Inquisitor, Medium, Mesmerist, Occultist, Psychic, Spiritualist\
3: Arcanist, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level
Saving throw: Will partial, see text
Spell resistance: yes
Target: one creature
Descriptors: mind-affecting, pain
:::

You telepathically wrack the target's mind and body with agonizing pain that imposes a -4 penalty on
attack rolls, skill checks, and ability checks. A successful Will save reduces the duration to 1
round.
