+++
id = "ref/spell/lost-locale"
kind = "spell"
title = "Lost Locale"
aon = "SpellDisplay.aspx?ItemName=Lost%20Locale"
source_ids = ["inner-sea-races"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "lost_locale", path = "json/spells6.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/lost-passage" },
]
[[sources]]
publication = "inner-sea-races"
page = "220"

[fields]
kind = "spell"
school = "enchantment"
subschools = ["compulsion"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Arcanist", level = 9 },
  { class = "Psychic", level = 9 },
  { class = "Sorcerer", level = 9 },
  { class = "Wizard", level = 9 },
]
casting_time = "24 hours"
components = "V, S"
range = "1 mile/level"
effects = [
  { label = "Area", value = "one 1-mile cube/level" },
]
duration = "2 hours/level (D)"
saving_throw = "Will partial"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 9: Arcanist, Psychic, Sorcerer, Wizard
Casting time: 24 hours
Components: V, S
Range: 1 mile/level
Duration: 2 hours/level (D)
Saving throw: Will partial
Spell resistance: yes
Area: one 1-mile cube/level
Subschool: compulsion
Descriptors: mind-affecting
:::

### Lost Locale

This spell functions as [lost passage](ref/spell/lost-passage), except that it affects a larger
area. Lost locale can be made permanent with [permanency](ref/spell/permanency) at a cost of 90,000
gp.
