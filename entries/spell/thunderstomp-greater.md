+++
id = "ref/spell/thunderstomp-greater"
kind = "spell"
title = "Greater Thunderstomp"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "thunderstomp_greater", path = "json/spells10.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/thunderstomp" },
]
[[sources]]
publication = "advanced-class-guide"
page = "196"

[fields]
kind = "spell"
school = "evocation"
descriptors = ["earth"]
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Bloodrager", level = 3 },
  { class = "Druid", level = 3 },
  { class = "Hunter", level = 3 },
  { class = "Magus", level = 3 },
  { class = "Ranger", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S"
range = "60 ft."
effects = [
  { label = "Area", value = "60-ft. line" },
]
duration = "instantaneous"
saving_throw = "none"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 3: Arcanist, Bloodrager, Druid, Hunter, Magus, Ranger, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S
Range: 60 ft.
Area: 60-ft. line
Duration: instantaneous
Saving throw: none
Spell resistance: yes
Descriptors: earth
:::

### Greater Thunderstomp

This spell functions as [thunderstomp](ref/spell/thunderstomp), except as noted, and it affects all
creatures in the area, regardless of size. When you attempt the combat maneuver check, apply its
result to each creature within the area.
