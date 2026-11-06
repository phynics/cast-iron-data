+++
id = "ref/spell/carve-passage"
kind = "spell"
title = "Carve Passage"
source_ids = ["inner-sea-races"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "carve_passage", path = "json/spells2.json" },
]

[fields]
kind = "spell"
school = "transmutation"
descriptors = ["earth"]
levels = [
  { class = "Arcanist", level = 5 },
  { class = "Druid", level = 5 },
  { class = "Hunter", level = 5 },
  { class = "Sorcerer", level = 5 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 standard action"
components = "V, S, F (a tiny diamond pick worth 500 gp)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Area", value = "dirt or loose rock in one 5-ft. cube/level" },
]
duration = "instantaneous"
saving_throw = "see text"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 5: Arcanist, Druid, Hunter, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, F (a tiny diamond pick worth 500 gp)
Range: close (25 ft. + 5 ft./2 levels)
Duration: instantaneous
Saving throw: see text
Spell resistance: no
Area: dirt or loose rock in one 5-ft. cube/level
Descriptors: earth
:::

**Sources:** Inner Sea Races pg 218

> _The following spell is available to the indicated race or ethnicity: [Kobold](ref/race/kobold)_

You can excavate and move an amount of snow, earth, dust, sand, and loose or packed rocks or ice
chunks (each no more than 5 feet in diameter) whose volume fills one 5-foot cube per level. If you
are buried, you can open a space around yourself and use any remaining cubes for tunneling. This
spell is otherwise similar to [expeditious excavation](ref/spell/expeditious-excavation). Carve
passage has no effect on earth creatures or solid rock or ice.
