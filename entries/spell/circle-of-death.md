+++
id = "ref/spell/circle-of-death"
kind = "spell"
title = "Circle of Death"
source_ids = ["core-rulebook", "mythic-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "circle_of_death", path = "json/spells2.json" },
]

[fields]
kind = "spell"
school = "necromancy"
descriptors = ["death"]
levels = [
  { class = "Arcanist", level = 6 },
  { class = "Inquisitor", level = 6 },
  { class = "Sorcerer", level = 6 },
  { class = "Spiritualist", level = 6 },
  { class = "Wizard", level = 6 },
]
casting_time = "1 standard action"
components = "V, S, M (a crushed black pearl worth 500 gp)"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Area", value = "several living creatures within a 40-ft.-radius burst" },
]
duration = "instantaneous"
saving_throw = "Fortitude negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 6: Arcanist, Inquisitor, Sorcerer, Spiritualist, Wizard
Casting time: 1 standard action
Components: V, S, M (a crushed black pearl worth 500 gp)
Range: medium (100 ft. + 10 ft./level)
Duration: instantaneous
Saving throw: Fortitude negates
Spell resistance: yes
Area: several living creatures within a 40-ft.-radius burst
Descriptors: death
:::

**Sources:** PRPG Core Rulebook pg 255

Circle of death snuffs out the life force of living creatures, killing them instantly. The spell
slays 1d4 HD worth of living creatures per caster level (maximum 20d4). Creatures with the fewest HD
are affected first; among creatures with equal HD, those who are closest to the burst's point of
origin are affected first. No creature of 9 or more HD can be affected, and HD that are not
sufficient to affect a creature are wasted.

### Mythic Circle of Death

**Sources:** Mythic Adventures pg 88\
The number of Hit Dice worth of creatures killed by the spell increases to 1d6 per caster level
(maximum 20d6). Add your tier to the maximum HD of creatures that can be affected by the spell. (For
example, at 3rd tier, a creature with 12 HD cannot be affected.)

_Augmented (6th):_ If you expend two uses of mythic power, creatures that succeed at their saves
against this spell take 1d6 points of damage per tier.
