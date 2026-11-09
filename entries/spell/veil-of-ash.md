+++
id = "ref/spell/veil-of-ash"
kind = "spell"
title = "Veil of Ash"
aon = "SpellDisplay.aspx?ItemName=Veil%20of%20Ash"
source_ids = ["pathfinder-24-the-final-wish"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "veil_of_ash", path = "json/spells11.json" },
]
[[sources]]
publication = "pathfinder-24-the-final-wish"
page = "61"

[fields]
kind = "spell"
school = "evocation"
descriptors = ["fire"]
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, M (a pinch of ash)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "1 round/level"
saving_throw = "Fortitude negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 2: Arcanist, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M (a pinch of ash)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level
Saving throw: Fortitude negates
Spell resistance: yes
Target: one creature
Descriptors: fire
:::

This spell causes a small cloud of searing, choking ash to appear around the face of the target. The
creature must succeed at a Fortitude saving throw or take 1d6 points of fire damage and be blinded.
The victim must make a new save against damage and blindness for each round the spell persists. The
target must have a discernable anatomy and no more than one head in order to be blinded. Undead,
constructs, and creatures without eyes or who don't rely on sight to sense their surroundings can be
damaged by this spell, but not blinded.

A moderate wind (11+ mph) disperses the ash cloud in 2 rounds; a strong wind (21+ mph) disperses the
cloud in 1 round.

This spell does not function underwater.
