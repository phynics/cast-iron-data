+++
id = "ref/spell/animus-mine-greater"
kind = "spell"
title = "Greater Animus Mine"
source_ids = ["heroes-of-the-darklands"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "animus_mine_greater", path = "json/spells.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/animus-mine" },
]

[fields]
kind = "spell"
school = "abjuration"
descriptors = ["mind-affecting"]
levels = [
  { class = "Mesmerist", level = 4 },
  { class = "Psychic", level = 5 },
]
casting_time = "1 standard action"
components = "V, S"
range = "personal"
effects = [
  { label = "Effect", value = "see text" },
]
duration = "1 hour/level or until discharged"
saving_throw = "Will negates (harmless)"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 4: Mesmerist\
5: Psychic
Casting time: 1 standard action
Components: V, S
Range: personal
Effect: see text
Duration: 1 hour/level or until discharged
Saving throw: Will negates (harmless)
Spell resistance: no
Descriptors: mind-affecting
:::

### Greater Animus Mine

**Sources:** Heroes of the Darklands pg 20

This functions as per [animus mine](ref/spell/animus-mine), except the triggering creature is
stunned for 1d4 rounds instead of staggered. If the target succeeds at a Will saving throw, it takes
only half damage and negates the stunned effect. If the target fails this Will saving throw, you
automatically succeed at any saving throw against the mind-affecting effect that triggered the mine.
