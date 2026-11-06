+++
id = "ref/spell/caustic-eruption"
kind = "spell"
title = "Caustic Eruption"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "caustic_eruption", path = "json/spells2.json" },
]

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Creation"]
descriptors = ["acid"]
levels = [
  { class = "Arcanist", level = 7 },
  { class = "Sorcerer", level = 7 },
  { class = "Wizard", level = 7 },
]
casting_time = "1 standard action"
components = "V, S"
range = "30 ft."
effects = [
  { label = "Area", value = "30-ft.-radius burst" },
]
duration = "instantaneous and 2 rounds; see text"
saving_throw = "Reflex half (see text)"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 7: Arcanist, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S
Range: 30 ft.
Duration: instantaneous and 2 rounds; see text
Saving throw: Reflex half (see text)
Spell resistance: no
Area: 30-ft.-radius burst
Subschool: Creation
Descriptors: acid
:::

**Sources:** Ultimate Magic pg 210

Acid erupts from your space in all directions, causing 1d6 points of damage per caster level
(maximum 20d6) to creatures and unattended objects in the area. On your turn in each of the next 2
rounds, creatures and objects that failed their saves against the initial burst take an additional
1d6 points of acid damage per 2 caster levels (maximum 10d6) unless the acid is neutralized,
dispelled, or washed away.
