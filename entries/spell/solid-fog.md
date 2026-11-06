+++
id = "ref/spell/solid-fog"
kind = "spell"
title = "Solid Fog"
source_ids = ["core-rulebook", "mythic-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "solid_fog", path = "json/spells9.json" },
]

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Creation"]
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Magus", level = 4 },
  { class = "Mesmerist", level = 4 },
  { class = "Shaman", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Spiritualist", level = 4 },
  { class = "Unchained Summoner", level = 4 },
  { class = "Witch", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S, M (powdered peas and an animal hoof)"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Effect", value = "fog spreads in 20-ft. radius" },
]
duration = "1 minute/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 4: Arcanist, Magus, Mesmerist, Shaman, Sorcerer, Spiritualist, Unchained Summoner, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M (powdered peas and an animal hoof)
Range: medium (100 ft. + 10 ft./level)
Duration: 1 minute/level
Saving throw: none
Spell resistance: no
Effect: fog spreads in 20-ft. radius
Subschool: Creation
:::

**Sources:** PRPG Core Rulebook pg 345

This spell functions like fog cloud, but in addition to obscuring sight, the solid fog is so thick
that it impedes movement. Creatures moving through a solid fog move at half their normal speed and
take a -2 penalty on all melee attack and melee damage rolls. The vapors prevent effective ranged
weapon attacks (except for magic rays and the like). A creature or object that falls into solid fog
is slowed so that each 10 feet of vapor that it passes through reduces the falling damage by 1d6. A
creature cannot take a 5-foot-step while in solid fog. Solid fog, and effects that work like solid
fog, do not stack with each other in terms of slowed movement and attack penalties.

Unlike normal fog, only a severe wind (31+ mph) disperses these vapors, and it does so in 1 round.

Solid fog can be made permanent with a [permanency](ref/spell/permanency) spell. A permanent solid
fog dispersed by wind reforms in 10 minutes.

### Mythic Solid Fog

**Sources:** Mythic Adventures pg 109\
The penalty on melee attack and damage rolls increases to -4. The cloud's radius and height both
increase to 50 feet.

_Augmented:_ The augmented version of mythic solid fog has the same additional benefits as the
augmented version of mythic fog cloud.
