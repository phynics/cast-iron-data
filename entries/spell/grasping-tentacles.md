+++
id = "ref/spell/grasping-tentacles"
kind = "spell"
title = "Grasping Tentacles"
source_ids = ["core-rulebook", "dirty-tactics-toolbox"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "grasping_tentacles", path = "json/spells12.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/black-tentacles" },
]

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Creation"]
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Bloodrager", level = 4 },
  { class = "Magus", level = 4 },
  { class = "Psychic", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Spiritualist", level = 4 },
  { class = "Summoner", level = 3 },
  { class = "Unchained Summoner", level = 4 },
  { class = "Witch", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S, M (octopus or squid tentacle)"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Area", value = "20-ft.-radius spread" },
]
duration = "1 round/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 3: Summoner\
4: Arcanist, Bloodrager, Magus, Psychic, Sorcerer, Spiritualist, Unchained Summoner, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M (octopus or squid tentacle)
Range: medium (100 ft. + 10 ft./level)
Duration: 1 round/level (D)
Saving throw: none
Spell resistance: no
Area: 20-ft.-radius spread
Subschool: Creation
:::

### Grasping Tentacles

**Sources:** Dirty Tactics Toolbox pg 30

This spell functions as [black tentacles](ref/spell/black-tentacles), except the tentacles blindly
grasp at the targets' eyes and ears, and tug at their hair, clothes, and equipment. Instead of
grapple attempts, the tentacles attempt dirty trick combat maneuver checks (CMB = your caster
level + 4 \[the tentacles' Strength bonus\] + 1 \[the tentacles' size bonus\]). Roll on the
following table to determine the effect of a successful dirty trick combat maneuver check.

|d%|Effect|
| --- | --- |
|01-20|Blinded. The tentacles suction over the victim's eyes.|
|21-40|Deafened. The tentacles clap themselves around the victim's ears.|
|41-60|Entangled. The tentacles weave around the victim's limbs.|
|61-80|Shaken. The tentacles menace the victim from all sides. This is a fear effect.|
|81-100|Sickened. The tentacles give off sickening vapors. This is a poison effect.|
