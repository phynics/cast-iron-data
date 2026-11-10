+++
id = "ref/spell/curse-terrain-supreme"
kind = "spell"
title = "Supreme Curse Terrain"
aon = "SpellDisplay.aspx?ItemName=Curse%20Terrain%2C%20Supreme"
source_ids = ["horror-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "curse_terrain_supreme", path = "json/spells3.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/curse-terrain-lesser" },
]
[[sources]]
publication = "horror-adventures"
page = "115"

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

### Supreme Curse Terrain

By touching the ground, you curse the land with seven unnatural hazards. This functions as
[lesser curse terrain](ref/spell/curse-terrain-lesser), but with the effects of the grand perilous
demesne curse (see below).

#### Grand Perilous Demesne

**Type** regional curse; **Area** 18-mile-radius emanation; **Save** Will DC 22 to remove\
**Effect** As per major perilous demesne (see above), except up to seven hazards, each of CR 14 or
less, imperil creatures in the area. The hazards are arranged so that if any are encountered
together, the encounter's effective CR from hazards must be no more than 15 (for instance, two CR 13
hazards could be encountered together).

**Cure** [Remove curse](ref/spell/remove-curse) removes a grand perilous demesne only if followed by
a casting of [hallow](ref/spell/hallow) at the effect's center, and then casting
[disintegrate](ref/spell/disintegrate) on each of the hazards before the next nightfall or midnight.
