+++
id = "ref/spell/mydriatic-spontaneity-mass"
kind = "spell"
title = "Mass Mydriatic Spontaneity"
source_ids = ["blood-of-shadows"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "mydriatic_spontaneity_mass", path = "json/spells7.json" },
]

[fields]
kind = "spell"
school = "evocation"
descriptors = ["darkness", "light"]
levels = [
  { class = "Arcanist", level = 7 },
  { class = "Bard", level = 5 },
  { class = "Mesmerist", level = 5 },
  { class = "Psychic", level = 6 },
  { class = "Skald", level = 5 },
  { class = "Sorcerer", level = 7 },
  { class = "Witch", level = 7 },
  { class = "Wizard", level = 7 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one or more living creatures, no two of which can be more than 30 ft. apart" },
]
duration = "1 round/level"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 5: Bard, Mesmerist, Skald\
6: Psychic\
7: Arcanist, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Target: one or more living creatures, no two of which can be more than 30 ft. apart
Duration: 1 round/level
Saving throw: Will negates
Spell resistance: yes
Descriptors: darkness, light
:::

## Mydriatic Spontaneity

**Sources:** Blood of Shadows pg 28

You overstimulate the target with alternating flashes of light and shadow within its eyes, causing
its pupils to rapidly dilate and contract. While under the effects of this spell, the target is
racked by splitting headaches and unable to see clearly, becoming nauseated for the spell's
duration. Each round, the target's pupils randomly become dilated or contracted for 1 round. During
any round that its eyes are dilated, the target is blinded if exposed to bright light or dazzled if
exposed to normal light. During any round its eyes are contracted, the target is blinded if exposed
to darkness or dazzled if exposed to dim light. In addition, any creature can attempt a Stealth
check to avoid detection from the target, even if the creature lacks cover or concealment.

### Mass Mydriatic Spontaneity

**Sources:** Blood of Shadows pg 29

This spell functions as mydriatic spontaneity, except it can affect multiple creatures.
