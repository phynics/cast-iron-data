+++
id = "ref/spell/pain-strike-mass"
kind = "spell"
title = "Mass Pain Strike"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "pain_strike_mass", path = "json/spells7.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/pain-strike" },
]

[fields]
kind = "spell"
school = "evocation"
descriptors = ["evil", "pain"]
levels = [
  { class = "Arcanist", level = 5 },
  { class = "Psychic", level = 4 },
  { class = "Sorcerer", level = 5 },
  { class = "Spiritualist", level = 5 },
  { class = "Witch", level = 5 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Targets", value = "one living creature/level, no two of which can be more than 30 ft. apart" },
]
duration = "1 round/level (D)"
saving_throw = "Fortitude negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 4: Psychic\
5: Arcanist, Sorcerer, Spiritualist, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Targets: one living creature/level, no two of which can be more than 30 ft. apart
Duration: 1 round/level (D)
Saving throw: Fortitude negates
Spell resistance: yes
Descriptors: evil, pain
:::

### Mass Pain Strike

**Sources:** Advanced Player's Guide pg 234

This spell works like [pain strike](ref/spell/pain-strike), except as noted above.
