+++
id = "ref/spell/siege-scatter"
kind = "spell"
title = "Siege Scatter"
source_ids = ["inner-sea-races"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "siege_scatter", path = "json/spells9.json" },
]
[[sources]]
publication = "inner-sea-races"
page = "223"

[fields]
kind = "spell"
school = "evocation"
descriptors = ["earth"]
levels = [
  { class = "Druid", level = 5 },
  { class = "Hunter", level = 4 },
  { class = "Ranger", level = 4 },
  { class = "Shaman", level = 5 },
]
casting_time = "1 round"
components = "V, S"
range = "long (400 ft. + 40 ft./level)"
effects = [
  { label = "Area", value = "50-ft.-radius spread" },
]
duration = "instantaneous"
saving_throw = "Reflex partial (see text)"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 4: Hunter, Ranger\
5: Druid, Shaman
Casting time: 1 round
Components: V, S
Range: long (400 ft. + 40 ft./level)
Duration: instantaneous
Saving throw: Reflex partial (see text)
Spell resistance: yes
Area: 50-ft.-radius spread
Descriptors: earth
:::

> _The following spell is available to the indicated race or ethnicity: [Dwarf](ref/race/dwarf)_

A roiling blast of rough rock and dirt scatters along the ground in the area, dealing 1d6 points of
slashing damage per 2 caster levels (maximum 5d6) to all creatures on the ground in the area, even
on a successful saving throw. Creatures in the area that fail the Reflex save fall prone and are
knocked to the nearest edge of the area, taking 1d6 points of bludgeoning damage for every 10 feet
they travel this way. Creatures that did not move during the past round and those with the stability
racial trait gain a +4 bonus on the saving throw.
