+++
id = "ref/spell/curse-terrain-lesser"
kind = "spell"
title = "Lesser Curse Terrain"
source_ids = ["horror-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "curse_terrain_lesser", path = "json/spells3.json" },
]
[[sources]]
publication = "horror-adventures"
page = "114"

[fields]
kind = "spell"
school = "necromancy"
descriptors = ["curse", "evil"]
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Cleric", level = 2 },
  { class = "Druid", level = 2 },
  { class = "Hunter", level = 2 },
  { class = "Oracle", level = 2 },
  { class = "Shaman", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Warpriest", level = 2 },
  { class = "Witch", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "10 minutes"
components = "V, S, M (the heart of a creature that dwelled in the area and powdered onxy worth 350 gp)"
range = "touch"
effects = [
  { label = "Area", value = "300-ft. radius emanating from the touched point" },
]
duration = "1 day (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 2: Arcanist, Cleric, Druid, Hunter, Oracle, Shaman, Sorcerer, Warpriest, Witch, Wizard
Casting time: 10 minutes
Components: V, S, M (the heart of a creature that dwelled in the area and powdered onxy worth 350 gp)
Range: touch
Area: 300-ft. radius emanating from the touched point
Duration: 1 day (D)
Saving throw: none
Spell resistance: no
Descriptors: curse, evil
:::

By touching the ground, you curse the land with three unnatural hazards, as the minor perilous
demesne curse (see below). Though this makes the hazards appear frequently, their manifestations are
still unpredictable-you can't control when the hazards begin or end, nor where they appear within
the cursed terrain.

Curse terrain spells can be made permanent with a [permanency](ref/spell/permanency) spell. The
minimum caster level and gp cost are shown on the table. The spell is still dismissible if made
permanent.

|Spell|Minimum Caster Level|GP Cost|
| --- | --- | --- |
|Lesser Curse Terrain|9th|2,500 gp|
|Curse Terrain|11th|7,500 gp|
|Greater Curse Terrain|15th|17,500 gp|
|Supreme Curse Terrain|19th|27,500 gp|

#### Minor Perillous Demesne

**Type** regional curse; **Area** 300-foot-radius emanation; **Save** Will DC 13 to remove\
**Effect** Up to three hazards (see the [Environments section](ref/rule/horror-environments)), each
of CR 3 or less, imperil creatures in the area, though never with more than one hazard at a time. If
a creature places this curse, it can choose the hazards. The hazards must be appropriate to the type
of terrain (atthe GM's discretion). Any of the hazards that are rendered safe reset themselves and
become dangerous again at each midnight.
