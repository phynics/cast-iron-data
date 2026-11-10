+++
id = "ref/spell/lost-locale"
kind = "spell"
title = "Lost Locale"
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
subschools = ["Compulsion"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Bard", level = 4 },
  { class = "Skald", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S"
range = "long (400 ft. + 40 ft./level)"
effects = [
  { label = "Area", value = "one 30-ft. cube/level (S)" },
]
duration = "2 hours/level (D)"
saving_throw = "Will partial"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 4: Arcanist, Bard, Skald, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S
Range: long (400 ft. + 40 ft./level)
Duration: 2 hours/level (D)
Saving throw: Will partial
Spell resistance: yes
Area: one 30-ft. cube/level (S)
Subschool: Compulsion
Descriptors: mind-affecting
:::

### Lost Locale

This spell functions as [lost passage](ref/spell/lost-passage), except that it affects a larger
area. Lost locale can be made permanent with [permanency](ref/spell/permanency) at a cost of 90,000
gp.
