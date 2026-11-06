+++
id = "ref/spell/virulent-miasma"
kind = "spell"
title = "Virulent Miasma"
source_ids = ["villain-codex"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "virulent_miasma", path = "json/spells11.json" },
]

[fields]
kind = "spell"
school = "necromancy"
levels = [
  { class = "Antipaladin", level = 2 },
  { class = "Arcanist", level = 3 },
  { class = "Bloodrager", level = 3 },
  { class = "Druid", level = 3 },
  { class = "Hunter", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, M (a dried scab from a diseased creature)"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Effect", value = "cloud spreads in 20-ft. radius, 20 ft. high" },
]
duration = "1 round/level"
saving_throw = "Fortitude negates (see text)"
spell_resistance = "see text"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 2: Antipaladin\
3: Arcanist, Bloodrager, Druid, Hunter, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M (a dried scab from a diseased creature)
Range: medium (100 ft. + 10 ft./level)
Duration: 1 round/level
Saving throw: Fortitude negates (see text)
Spell resistance: see text
Effect: cloud spreads in 20-ft. radius, 20 ft. high
:::

**Sources:** Villain Codex pg 69

Virulent miasma creates fog like fog cloud, except that the vapors carry the taint of disease.
Living creatures take a -4 penalty on saving throws against disease effects as long as they remain
within the cloud and for 1d4+1 rounds after leaving. This effect of the spell allows a Fortitude
save to negate it, and it is subject to [spell resistance](ref/rule/spell-resistance). A creature
that succeeds at its saving throw against the fog (or ignores the fog due to spell resistance) is
not affected and need not make further saves even if it remains in the fog.
