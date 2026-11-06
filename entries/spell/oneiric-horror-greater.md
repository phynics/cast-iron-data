+++
id = "ref/spell/oneiric-horror-greater"
kind = "spell"
title = "Greater Oneiric Horror"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "oneiric_horror_greater", path = "json/spells7.json" },
]

[fields]
kind = "spell"
school = "illusion"
subschools = ["Phantasm"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Bard", level = 2 },
  { class = "Medium", level = 1 },
  { class = "Mesmerist", level = 2 },
  { class = "Psychic", level = 2 },
  { class = "Skald", level = 2 },
  { class = "Sorcerer", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Target", value = "one living creature" },
]
duration = "1 round/level (D)"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 1: Medium\
2: Bard, Mesmerist, Psychic, Skald\
3: Arcanist, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S
Range: medium (100 ft. + 10 ft./level)
Duration: 1 round/level (D)
Saving throw: Will negates
Spell resistance: yes
Target: one living creature
Subschool: Phantasm
Descriptors: mind-affecting
:::

## Oneiric Horror

**Sources:** Occult Adventures pg 179

You cause the subject to believe it is being attacked by a creature out of its nightmares. Each
round, the subject makes a full-attack action against the creature. A flying creature can still
attempt a Fly check to hover. Each round on its turn after making a full attack against the
imaginary creature, the subject can attempt a new saving throw to end the effect. The subject is
fatigued for 1 minute after the spell ends.

### Greater Oneiric Horror

**Sources:** Occult Adventures pg 179

This spell functions as oneiric horror except each round the subject fails its Will save, it takes 1
point of Strength damage, and after the spell ends, the subject must succeed at a Fortitude save or
be fatigued for a number of minutes equal to the number of rounds spent under the spell's effect.
