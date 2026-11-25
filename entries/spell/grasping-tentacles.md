+++
id = "ref/spell/grasping-tentacles"
kind = "spell"
title = "Grasping Tentacles"
aon = "SpellDisplay.aspx?ItemName=Grasping%20Tentacles"
source_ids = ["dirty-tactics-toolbox"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "grasping_tentacles", path = "json/spells12.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/black-tentacles" },
]
[[sources]]
publication = "dirty-tactics-toolbox"
page = "30"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["creation"]
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Bloodrager", level = 3 },
  { class = "Magus", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Summoner", level = 3 },
  { class = "Witch", level = 3 },
  { class = "Wizard", level = 3 },
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
Level: 3: Arcanist, Bloodrager, Magus, Sorcerer, Summoner, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M (octopus or squid tentacle)
Range: medium (100 ft. + 10 ft./level)
Duration: 1 round/level (D)
Saving throw: none
Spell resistance: no
Area: 20-ft.-radius spread
Subschool: creation
:::

### Grasping Tentacles

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
