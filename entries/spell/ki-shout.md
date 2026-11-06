+++
id = "ref/spell/ki-shout"
kind = "spell"
title = "Ki Shout"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "ki_shout", path = "json/spells6.json" },
]

[fields]
kind = "spell"
school = "evocation"
descriptors = ["sonic"]
levels = [
  { class = "Arcanist", level = 7 },
  { class = "Bard", level = 5 },
  { class = "Psychic", level = 7 },
  { class = "Skald", level = 5 },
  { class = "Sorcerer", level = 7 },
  { class = "Wizard", level = 7 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one living creature" },
]
duration = "instantaneous"
saving_throw = "Fortitude partial"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 5: Bard, Skald\
7: Arcanist, Psychic, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: instantaneous
Saving throw: Fortitude partial
Spell resistance: yes
Target: one living creature
Descriptors: sonic
:::

**Sources:** Ultimate Magic pg 226

With a guttural bark, you unleash a sudden blast of sonic energy that strikes your opponent. The
target takes 1d6 points of sonic damage per level (maximum 20d6) and is stunned for 1 round; a
successful Fortitude save reduces the damage by half and negates the stun.
