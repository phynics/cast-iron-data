+++
id = "ref/spell/crime-of-opportunity"
kind = "spell"
title = "Crime of Opportunity"
aon = "SpellDisplay.aspx?ItemName=Crime%20of%20Opportunity"
source_ids = ["ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "crime_of_opportunity", path = "json/spells3.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/crime-wave" },
]
[[sources]]
publication = "ultimate-intrigue"
page = "208"

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Antipaladin", level = 4 },
  { class = "Arcanist", level = 7 },
  { class = "Bard", level = 5 },
  { class = "Mesmerist", level = 5 },
  { class = "Psychic", level = 7 },
  { class = "Sorcerer", level = 7 },
  { class = "Wizard", level = 7 },
]
casting_time = "1 standard action"
components = "V, S, M (a tarnished coin)"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Target", value = "one creature/level, no two of which can be more than 30 ft. apart" },
]
duration = "1 round/level (D)"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 4: Antipaladin\
5: Bard, Mesmerist\
7: Arcanist, Psychic, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M (a tarnished coin)
Range: medium (100 ft. + 10 ft./level)
Duration: 1 round/level (D)
Saving throw: Will negates
Spell resistance: yes
Target: one creature/level, no two of which can be more than 30 ft. apart
Subschool: Compulsion
Descriptors: mind-affecting
:::

### Crime of Opportunity

You awaken a sudden criminal impulse in the target, compelling it to commit a criminal act as if
affected by the [crime wave](ref/spell/crime-wave) spell.
