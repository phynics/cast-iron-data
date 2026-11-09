+++
id = "ref/spell/inveigle-monster"
kind = "spell"
title = "Inveigle Monster"
source_ids = ["inner-sea-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "inveigle_monster", path = "json/spells14.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/inveigle-person" },
]
[[sources]]
publication = "inner-sea-intrigue"
page = "60"

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Charm"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Bard", level = 3 },
  { class = "Mesmerist", level = 3 },
  { class = "Psychic", level = 3 },
  { class = "Skald", level = 3 },
  { class = "Sorcerer", level = 4 },
  { class = "Witch", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, M (a drop of alcohol)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one humanoid creature" },
]
duration = "1 hour/level"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 3: Bard, Mesmerist, Psychic, Skald\
4: Arcanist, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, M (a drop of alcohol)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 hour/level
Saving throw: Will negates
Spell resistance: yes
Target: one humanoid creature
Subschool: Charm
Descriptors: mind-affecting
:::

### Inveigle Monster

This spell functions as [inveigle person](ref/spell/inveigle-person) except as noted above.
