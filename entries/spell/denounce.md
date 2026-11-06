+++
id = "ref/spell/denounce"
kind = "spell"
title = "Denounce"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "denounce", path = "json/spells3.json" },
]

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["language-dependant", "mind-affecting"]
levels = [
  { class = "Bard", level = 4 },
  { class = "Inquisitor", level = 4 },
  { class = "Mesmerist", level = 4 },
  { class = "Psychic", level = 5 },
  { class = "Skald", level = 4 },
]
casting_time = "1 standard action"
components = "V"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Area", value = "30-ft.-radius burst" },
]
duration = "1 hour/level"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 4: Bard, Inquisitor, Mesmerist, Skald\
5: Psychic
Casting time: 1 standard action
Components: V
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 hour/level
Saving throw: Will negates
Spell resistance: yes
Area: 30-ft.-radius burst
Subschool: Compulsion
Descriptors: language-dependant, mind-affecting
:::

**Sources:** Advanced Player's Guide pg 215

You speak out against a single creature within line of sight and turn possible allies against it by
drawing upon the power of your voice and conviction. Creatures in the area who can see the denounced
creature must make a Will saving throw or have their starting attitude toward the denounced creature
worsened by two levels. For example, creatures previously indifferent to the subject turn
unfriendly. Diplomacy checks made to reverse the effects of denounce are made at a -10 penalty.
