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

## Lesser Curse Terrain

**Sources:** Horror Adventures pg 114

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

### Greater Curse Terrain

**Sources:** Horror Adventures pg 114

By touching the ground, you curse the land with six unnatural hazards. This functions as lesser
curse terrain, but with the effects of the greater perilous demesne curse (see below).

#### Greater Perilous Demesne

**Type** regional curse; **Area** 6-mile-radius emanation; **Save** Will DC 19 to remove\
**Effect** As per major perilous demesne (see above), except up to six hazards, each of CR 10 or
less, imperil creatures in the area. The hazards are arranged so that if any are encountered
together, the encounter's effective CR from hazards must be no more than 11 (for instance, two CR 9
hazards could be encountered together).

**Cure** [Remove curse](ref/spell/remove-curse) removes a greater perilous demesne only if followed
by a casting of [hallow](ref/spell/hallow) at the effect's center.

### Supreme Curse Terrain

**Sources:** Horror Adventures pg 115

By touching the ground, you curse the land with seven unnatural hazards. This functions as lesser
curse terrain, but with the effects of the grand perilous demesne curse (see below).

#### Grand Perilous Demesne

**Type** regional curse; **Area** 18-mile-radius emanation; **Save** Will DC 22 to remove\
**Effect** As per major perilous demesne (see above), except up to seven hazards, each of CR 14 or
less, imperil creatures in the area. The hazards are arranged so that if any are encountered
together, the encounter's effective CR from hazards must be no more than 15 (for instance, two CR 13
hazards could be encountered together).

**Cure** [Remove curse](ref/spell/remove-curse) removes a grand perilous demesne only if followed by
a casting of [hallow](ref/spell/hallow) at the effect's center, and then casting
[disintegrate](ref/spell/disintegrate) on each of the hazards before the next nightfall or midnight.
