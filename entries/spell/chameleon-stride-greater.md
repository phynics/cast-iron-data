+++
id = "ref/spell/chameleon-stride-greater"
kind = "spell"
title = "Greater Chameleon Stride"
source_ids = ["advanced-players-guide", "advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "chameleon_stride_greater", path = "json/spells2.json" },
]

[fields]
kind = "spell"
school = "illusion"
subschools = ["Glamer"]
descriptors = ["glamer"]
levels = [
  { class = "Hunter", level = 2 },
  { class = "Ranger", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 minute/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 2: Hunter, Ranger
Casting time: 1 standard action
Components: V, S, DF
Range: personal
Duration: 1 minute/level
Saving throw: none
Spell resistance: no
Target: you
Subschool: Glamer
Descriptors: glamer
:::

## Chameleon Stride

**Sources:** Advanced Player's Guide pg 210

You fade into the background, and while you are not truly invisible, you are hard to pinpoint due to
your translucent state. While under the effects of this spell, you gain a +4 bonus on Stealth checks
and have concealment from creatures more than 5 feet away (attacks have a 20% miss chance).

### Greater Chameleon Stride

**Sources:** Advanced Class Guide pg 177

This spell functions as chameleon stride, except it confers its bonuses upon all allies within 10
feet of you at the time the spell is cast. Those affected by this spell are able to see each other
and themselves as if they were unaffected by the spell. If an affected creature moves out of the
area, it loses the benefit of the spell. Creatures that move into the area after the spell is cast
do not gain its benefit.
