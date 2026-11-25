+++
id = "ref/spell/inveigle-monster"
kind = "spell"
title = "Inveigle Monster"
aon = "SpellDisplay.aspx?ItemName=Inveigle%20Monster"
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
subschools = ["charm"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Arcanist", level = 7 },
  { class = "Bard", level = 5 },
  { class = "Mesmerist", level = 5 },
  { class = "Psychic", level = 6 },
  { class = "Skald", level = 5 },
  { class = "Sorcerer", level = 7 },
  { class = "Witch", level = 7 },
  { class = "Wizard", level = 7 },
]
casting_time = "1 standard action"
components = "V, M (a drop of alcohol)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one living creature" },
]
duration = "1 day/level"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 5: Bard, Mesmerist, Skald\
6: Psychic\
7: Arcanist, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, M (a drop of alcohol)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 day/level
Saving throw: Will negates
Spell resistance: yes
Target: one living creature
Subschool: charm
Descriptors: mind-affecting
:::

### Inveigle Monster

This spell functions as [inveigle person](ref/spell/inveigle-person) except as noted above.
