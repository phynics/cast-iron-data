+++
id = "ref/spell/open-book"
kind = "spell"
title = "Open Book"
source_ids = ["ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "open_book", path = "json/spells7.json" },
]
[[sources]]
publication = "ultimate-intrigue"
page = "220"

[fields]
kind = "spell"
school = "divination"
descriptors = ["curse"]
levels = [
  { class = "Antipaladin", level = 2 },
  { class = "Arcanist", level = 3 },
  { class = "Bard", level = 2 },
  { class = "Inquisitor", level = 2 },
  { class = "Mesmerist", level = 2 },
  { class = "Psychic", level = 2 },
  { class = "Skald", level = 2 },
  { class = "Sorcerer", level = 3 },
  { class = "Witch", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, M (a page torn from a book)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "permanent"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 2: Antipaladin, Bard, Inquisitor, Mesmerist, Psychic, Skald\
3: Arcanist, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M (a page torn from a book)
Range: close (25 ft. + 5 ft./2 levels)
Duration: permanent
Saving throw: Will negates
Spell resistance: yes
Target: one creature
Descriptors: curse
:::

You lay bare not only the mind of a target, but the target's history as well. The target takes a -2
penalty on saving throws against divinations, and Diplomacy checks to gather information about the
target gain a bonus equal to half your caster level (maximum +10).
