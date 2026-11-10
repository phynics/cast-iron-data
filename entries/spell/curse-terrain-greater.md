+++
id = "ref/spell/curse-terrain-greater"
kind = "spell"
title = "Greater Curse Terrain"
aon = "SpellDisplay.aspx?ItemName=Curse%20Terrain%2C%20Greater"
source_ids = ["horror-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "curse_terrain_greater", path = "json/spells3.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/curse-terrain-lesser" },
]
[[sources]]
publication = "horror-adventures"
page = "114"

[fields]
kind = "spell"
school = "necromancy"
descriptors = ["curse", "evil"]
levels = [
  { class = "Arcanist", level = 6 },
  { class = "Cleric", level = 6 },
  { class = "Druid", level = 6 },
  { class = "Hunter", level = 6 },
  { class = "Oracle", level = 6 },
  { class = "Shaman", level = 6 },
  { class = "Sorcerer", level = 6 },
  { class = "Warpriest", level = 6 },
  { class = "Witch", level = 6 },
  { class = "Wizard", level = 6 },
]
casting_time = "10 minutes"
components = "V, S, M (the heart of the creature that dwelled in the area and powdered onyx worth 1,500 gp)"
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
Level: 6: Arcanist, Cleric, Druid, Hunter, Oracle, Shaman, Sorcerer, Warpriest, Witch, Wizard
Casting time: 10 minutes
Components: V, S, M (the heart of the creature that dwelled in the area and powdered onyx worth 1,500 gp)
Range: touch
Area: 300-ft. radius emanating from the touched point
Duration: 1 day (D)
Saving throw: none
Spell resistance: no
Descriptors: curse, evil
:::

### Greater Curse Terrain

By touching the ground, you curse the land with six unnatural hazards. This functions as
[lesser curse terrain](ref/spell/curse-terrain-lesser), but with the effects of the greater perilous
demesne curse (see below).

#### Greater Perilous Demesne

**Type** regional curse; **Area** 6-mile-radius emanation; **Save** Will DC 19 to remove\
**Effect** As per major perilous demesne (see above), except up to six hazards, each of CR 10 or
less, imperil creatures in the area. The hazards are arranged so that if any are encountered
together, the encounter's effective CR from hazards must be no more than 11 (for instance, two CR 9
hazards could be encountered together).

**Cure** [Remove curse](ref/spell/remove-curse) removes a greater perilous demesne only if followed
by a casting of [hallow](ref/spell/hallow) at the effect's center.
