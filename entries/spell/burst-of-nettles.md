+++
id = "ref/spell/burst-of-nettles"
kind = "spell"
title = "Burst of Nettles"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "burst_of_nettles", path = "json/spells2.json" },
]

[fields]
kind = "spell"
school = "conjuration"
descriptors = ["acid"]
levels = [
  { class = "Druid", level = 3 },
  { class = "Hunter", level = 3 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Area", value = "10-ft.-radius burst" },
]
duration = "instantaneous"
saving_throw = "Reflex half"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 3: Druid, Hunter
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: instantaneous
Saving throw: Reflex half
Spell resistance: yes
Area: 10-ft.-radius burst
Descriptors: acid
:::

**Sources:** Ultimate Magic pg 210

You release a burst of barbed, acid-filled nettles. Creatures caught in the burst take 3d6 points of
damage plus 1d6 points of acid damage on the next round. Those that save take half damage from the
initial burst and no damage on the next round.
