+++
id = "ref/spell/eroding-ray"
kind = "spell"
title = "Eroding Ray"
source_ids = ["plane-hoppers-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "eroding_ray", path = "json/spells4.json" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Cleric", level = 2 },
  { class = "Druid", level = 2 },
  { class = "Hunter", level = 2 },
  { class = "Oracle", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Warpriest", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Effect", value = "ray" },
]
duration = "instantaneous"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 2: Arcanist, Cleric, Druid, Hunter, Oracle, Sorcerer, Warpriest, Wizard
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: instantaneous
Saving throw: none
Spell resistance: no
Effect: ray
:::

**Sources:** Plane-Hopper's Handbook pg 30

You channel a fraction of the tumultuous ecosystem of the Hao Jin Tapestry and redirect it through
your hands as a beam of deteriorating energy. You can fire one ray, plus one additional ray for
every 4 levels beyond 3rd (to a maximum of three rays at 11th level). Each ray requires a ranged
touch attack to hit and can target only a construct or an object. If a ray hits, the target begins
to crumble, taking 2d6 points of damage. This damage ignores [hardness](ref/umr/hardness) and
[damage reduction](ref/rule/damage-reduction).
