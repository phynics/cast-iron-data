+++
id = "ref/spell/alter-river"
kind = "spell"
title = "Alter River"
source_ids = ["people-of-the-river"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "alter_river", path = "json/spells.json" },
]
[[sources]]
publication = "people-of-the-river"
page = "26"

[fields]
kind = "spell"
school = "transmutation"
descriptors = ["water"]
levels = [
  { class = "Arcanist", level = 5 },
  { class = "Cleric", level = 4 },
  { class = "Druid", level = 4 },
  { class = "Hunter", level = 4 },
  { class = "Oracle", level = 4 },
  { class = "Sorcerer", level = 5 },
  { class = "Warpriest", level = 4 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 standard action"
components = "V, S, M (silt from a dry riverbed)"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Target", value = "area of river up to 5 ft. wide/2 levels and 10 ft. long/level" },
]
duration = "1 minute/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 4: Cleric, Druid, Hunter, Oracle, Warpriest\
5: Arcanist, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M (silt from a dry riverbed)
Range: medium (100 ft. + 10 ft./level)
Duration: 1 minute/level (D)
Saving throw: none
Spell resistance: no
Target: area of river up to 5 ft. wide/2 levels and 10 ft. long/level
Descriptors: water
:::

You alter the flow of water in a natural freshwater channel such as a river, stream, or waterfall.
The first version of this spell alters the speed of a river's flow. The second diverts the course of
the targeted river.

_Alter Current:_ The river's current increases or decreases in speed by up to 1 mile per hour per 2
caster levels you possess. A typical placid river travels at a rate of up to 2 mph (no effect on
local movement); a swift river travels 2-4 mph, moving creatures and objects 10 to 40 feet
downstream per round; and an area of river rapids travels 7-10 mph, moving creatures and objects 60
to 90 feet downstream per round. Altering the speed of the current alters the difficulty of swimming
in the water accordingly.

_Divert River:_ The river diverts its course in a direction of your choosing. The river flows in the
general direction indicated, but otherwise conforms to the shape of the local terrain. This spell
cannot cause a river to flow uphill, though the river surges over its natural banks and inundates
terrain lower than its average depth. Creatures in the path of the redirected river are in danger of
being swept away; if directed properly, this spell causes a flood. See
[Aquatic Terrain](ref/rule/aquatic-terrain) for more details.

Alter river can be made permanent with a [permanency](ref/spell/permanency) spell. Clever
application of spells such as [move earth](ref/spell/move-earth) can be combined with this spell to
likewise make the river's new course permanent.
