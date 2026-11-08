+++
id = "ref/spell/curse-terrain"
kind = "spell"
title = "Curse Terrain"
source_ids = ["horror-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "curse_terrain", path = "json/spells3.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/curse-terrain-lesser" },
]

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
duration = "1 day"
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
Duration: 1 day
Saving throw: none
Spell resistance: no
Area: 300-ft. radius emanating from the touched point
Descriptors: curse, evil
:::

### Curse Terrain

**Sources:** Horror Adventures pg 114

By touching the ground, you curse the land with four unnatural hazards. This functions as
[lesser curse terrain](ref/spell/curse-terrain-lesser), but with the effects of the major perilous
demesne curse (see below).

#### Major Perilous Demesne

**Type** regional curse; **Area** 1-mile-radius emanation; **Save** Will DC 16 to remove\
**Effect** As per minor perilous demesne (see above), except this can involve up to four hazards,
each of CR 6 or less, imperil creatures in the area. If any hazards are encountered together, the
encounter's effective CR from hazards must be no more than 7 (for instance, two CR 5 hazards could
be encountered together).
