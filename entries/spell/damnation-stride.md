+++
id = "ref/spell/damnation-stride"
kind = "spell"
title = "Damnation Stride"
source_ids = ["advanced-race-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "damnation_stride", path = "json/spells3.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/dimension-door" },
]
[[sources]]
publication = "advanced-race-guide"
page = "173"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Teleportation"]
descriptors = ["fire"]
levels = [
  { class = "Arcanist", level = 5 },
  { class = "Sorcerer", level = 5 },
  { class = "Summoner", level = 4 },
  { class = "Unchained Summoner", level = 4 },
  { class = "Witch", level = 5 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 standard action"
components = "V"
range = "long (400 ft. + 40 ft./level)"
effects = [
  { label = "Target", value = "you (teleportation) and creatures within a 10-foot-radius burst (burst of flame) (see text)" },
]
duration = "instantaneous"
saving_throw = "Reflex half, see text"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 4: Summoner, Unchained Summoner\
5: Arcanist, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V
Range: long (400 ft. + 40 ft./level)
Duration: instantaneous
Saving throw: Reflex half, see text
Spell resistance: no
Target: you (teleportation) and creatures within a 10-foot-radius burst (burst of flame) (see text)
Subschool: Teleportation
Descriptors: fire
:::

> _[Tieflings](ref/race/tiefling) have access to the following spell._

This spell functions like [dimension door](ref/spell/dimension-door), except you leave behind a
burst of fire. Choose one corner of your starting square. A 10-foot-radius burst of flame explodes
from that corner the moment you leave, dealing 4d6 points of fire damage.
