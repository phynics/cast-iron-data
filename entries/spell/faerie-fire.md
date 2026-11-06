+++
id = "ref/spell/faerie-fire"
kind = "spell"
title = "Faerie Fire"
source_ids = ["core-rulebook", "mythic-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "faerie_fire", path = "json/spells4.json" },
]

[fields]
kind = "spell"
school = "evocation"
descriptors = ["light"]
levels = [
  { class = "Druid", level = 1 },
  { class = "Hunter", level = 1 },
  { class = "Mesmerist", level = 1 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "long (400 ft. + 40 ft./level)"
effects = [
  { label = "Area", value = "creatures and objects within a 5-ft.-radius burst" },
]
duration = "1 minute/level (D)"
saving_throw = "none"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 1: Druid, Hunter, Mesmerist
Casting time: 1 standard action
Components: V, S, DF
Range: long (400 ft. + 40 ft./level)
Duration: 1 minute/level (D)
Saving throw: none
Spell resistance: yes
Area: creatures and objects within a 5-ft.-radius burst
Descriptors: light
:::

**Sources:** PRPG Core Rulebook pg 280

A pale glow surrounds and outlines the subjects. Outlined subjects shed light as candles. Creatures
outlined by faerie fire take a -20 penalty on all Stealth checks. Outlined creatures do not benefit
from the [concealment](ref/rule/concealment) normally provided by [darkness](ref/spell/darkness)
(though a 2nd-level or higher magical darkness effect functions normally), [blur](ref/spell/blur),
[displacement](ref/spell/displacement), [invisibility](ref/spell/invisibility), or similar effects.
The light is too dim to have any special effect on undead or dark-dwelling creatures vulnerable to
light. The faerie fire can be blue, green, or violet, according to your choice at the time of
casting. The faerie fire does not cause any harm to the objects or creatures thus outlined.

### Mythic Faerie Fire

**Sources:** Mythic Adventures pg 93\
Outlined creatures are dazzled. The spell outlines figment illusions in the burst, revealing them as
such. This effect applies only to figments with a caster level equal to or less than your tier.

_Augmented (2nd):_ If you expend two uses of mythic power, each creature in the burst must succeed
at a Fortitude save or be blinded for 1 round.
