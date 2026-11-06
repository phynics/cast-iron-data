+++
id = "ref/spell/wave-shield"
kind = "spell"
title = "Wave Shield"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "wave_shield", path = "json/spells11.json" },
]

[fields]
kind = "spell"
school = "abjuration"
descriptors = ["water"]
levels = [
  { class = "Arcanist", level = 1 },
  { class = "Bloodrager", level = 1 },
  { class = "Druid", level = 1 },
  { class = "Hunter", level = 1 },
  { class = "Magus", level = 1 },
  { class = "Shaman", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Witch", level = 1 },
  { class = "Wizard", level = 1 },
]
casting_time = "1 immediate action"
components = "V"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 round or until discharged"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 1: Arcanist, Bloodrager, Druid, Hunter, Magus, Shaman, Sorcerer, Witch, Wizard
Casting time: 1 immediate action
Components: V
Range: personal
Duration: 1 round or until discharged
Saving throw: none
Spell resistance: no
Target: you
Descriptors: water
:::

**Sources:** Advanced Class Guide pg 199

You create a rushing torrent of water in the rough outline of a shield. The water protects you from
one physical or fire attack, granting you DR/- and fire resistance equal to half your caster level
(minimum 1) on that attack. Once the spell has reduced the damage of one attack against you, it is
discharged.
