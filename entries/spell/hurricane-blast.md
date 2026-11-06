+++
id = "ref/spell/hurricane-blast"
kind = "spell"
title = "Hurricane Blast"
source_ids = ["pathfinder-24-the-final-wish"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "hurricane_blast", path = "json/spells5.json" },
]

[fields]
kind = "spell"
school = "evocation"
descriptors = ["air"]
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Druid", level = 3 },
  { class = "Hunter", level = 3 },
  { class = "Sorcerer", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S"
range = "personal"
effects = [
  { label = "Area", value = "5-ft.-radius burst/2 levels (maximum 25-ft.-radius burst) centered on you" },
]
duration = "1 round"
saving_throw = "Reflex negates"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 3: Druid, Hunter\
4: Arcanist, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S
Range: personal
Duration: 1 round
Saving throw: Reflex negates
Spell resistance: no
Area: 5-ft.-radius burst/2 levels (maximum 25-ft.-radius burst) centered on you
Descriptors: air
:::

**Sources:** Pathfinder \#24: The Final Wish pg 60

This spell creates a severe blast of air (approximately 50 mph) that originates from you, affecting
all creatures in the burst.

A Tiny or smaller creature on the ground is knocked down and rolled 1d4×10 feet, taking 1d4 points
of nonlethal damage per 10 feet. If flying, a Tiny or smaller creature is blown back 2d6×10 feet and
takes 2d6 points of nonlethal damage due to battering and buffeting.

Small creatures are knocked prone by the force of the wind, or if flying are blown back 1d6×10 feet.

Medium creatures are unable to move forward against the force of the wind, or if flying are blown
back 1d6×5 feet.

Large or larger creatures may move normally within a hurricane blast effect.

Hurricane blast can't move a creature beyond the limit of its range. Any creature, regardless of
size, takes a -4 penalty on ranged attacks and Listen checks in the area of a hurricane blast. The
force of the gust automatically extinguishes candles, torches, and similar unprotected flames. It
causes protected flames, such as those of lanterns, to dance wildly and has a 50% chance to
extinguish those lights.

In addition to the effects noted, a hurricane blast can do anything that a sudden blast of wind
would be expected to do. It can create a stinging spray of sand or dust, fan a large fire, overturn
delicate awnings or hangings, and blow gases or vapors to the edge of its range.
