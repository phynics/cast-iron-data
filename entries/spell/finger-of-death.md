+++
id = "ref/spell/finger-of-death"
kind = "spell"
title = "Finger of Death"
source_ids = ["core-rulebook", "mythic-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "finger_of_death", path = "json/spells4.json" },
]

[fields]
kind = "spell"
school = "necromancy"
descriptors = ["death"]
levels = [
  { class = "Arcanist", level = 7 },
  { class = "Druid", level = 8 },
  { class = "Psychic", level = 7 },
  { class = "Sorcerer", level = 7 },
  { class = "Wizard", level = 7 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "instantaneous"
saving_throw = "Fortitude partial"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 7: Arcanist, Psychic, Sorcerer, Wizard\
8: Druid
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: instantaneous
Saving throw: Fortitude partial
Spell resistance: yes
Target: one creature
Descriptors: death
:::

**Sources:** PRPG Core Rulebook pg 282

This spell instantly delivers 10 points of damage per caster level. If the target's Fortitude saving
throw succeeds, it instead takes 3d6 points of damage + 1 point per caster level. The subject might
die from damage even if it succeeds on its saving throw.

### Mythic Finger of Death

**Sources:** Mythic Adventures pg 94\
The damage dealt increases to 15 points of damage per caster level plus 1d8 points of Constitution
damage. A creature that succeeds at its saving throw takes 3d8 points of damage + 1 point per caster
level, takes 1d4 points of Constitution damage, and is staggered for 1 round.
