+++
id = "ref/spell/screaming-flames"
kind = "spell"
title = "Screaming Flames"
source_ids = ["horror-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "screaming_flames", path = "json/spells8.json" },
]

[fields]
kind = "spell"
school = "evocation"
descriptors = ["evil", "fire", "mind-affecting"]
levels = [
  { class = "Antipaladin", level = 3 },
  { class = "Cleric", level = 3 },
  { class = "Oracle", level = 3 },
  { class = "Warpriest", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, M/DF (a charred animal or humanoid skull fragment)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Effect", value = "a sheet of flames up to 15 ft. long and 10 ft. high that moves 15 ft. in a straight line" },
]
duration = "instantaneous"
saving_throw = "Reflex half and Will negates (see text)"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 3: Antipaladin, Cleric, Oracle, Warpriest
Casting time: 1 standard action
Components: V, S, M/DF (a charred animal or humanoid skull fragment)
Range: close (25 ft. + 5 ft./2 levels)
Duration: instantaneous
Saving throw: Reflex half and Will negates (see text)
Spell resistance: yes
Effect: a sheet of flames up to 15 ft. long and 10 ft. high that moves 15 ft. in a straight line
Descriptors: evil, fire, mind-affecting
:::

**Sources:** Horror Adventures pg 126

A sheer wall of flame appears and rushes away from you. Tendrils of fire reach out of it, shaped
into skulls screaming in agony. When the wall passes through a creature's space, that creature must
succeed at a Reflex save or take 1d8 points of fire damage for every 2 caster levels you have
(maximum 5d8). Any creature taking fire damage must also succeed at a Will save or take 1d3 points
of Wisdom damage. Deaf creatures receive a +4 circumstance bonus on their Will saves.

If your campaign uses [the sanity system](ref/rule/sanity), a creature takes 1d6 points of sanity
damage instead of Wisdom damage.
