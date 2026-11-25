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
subschools = ["compulsion"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Antipaladin", level = 1 },
  { class = "Mesmerist", level = 1 },
]
casting_time = "1 standard action"
components = "V, S, M (a slit purse)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "1 round"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 1: Antipaladin, Mesmerist
Casting time: 1 standard action
Components: V, S, M (a slit purse)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round
Saving throw: Will negates
Spell resistance: yes
Target: one creature
Subschool: compulsion
Descriptors: mind-affecting
:::

### Crime of Opportunity

You awaken a sudden criminal impulse in the target, compelling it to commit a criminal act as if
affected by the [crime wave](ref/spell/crime-wave) spell.
