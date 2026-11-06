+++
id = "ref/spell/blinding-ray"
kind = "spell"
title = "Blinding Ray"
source_ids = ["advanced-race-guide", "mythic-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "blinding_ray", path = "json/spells2.json" },
]

[fields]
kind = "spell"
school = "evocation"
descriptors = ["good", "light"]
levels = [
  { class = "Cleric", level = 2 },
  { class = "Inquisitor", level = 3 },
  { class = "Oracle", level = 2 },
  { class = "Paladin", level = 2 },
  { class = "Warpriest", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Effect", value = "one or more rays of light" },
]
duration = "instantaneous (see text)"
saving_throw = "Fortitude negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 2: Cleric, Oracle, Paladin, Warpriest\
3: Inquisitor
Casting time: 1 standard action
Components: V, S, DF
Range: close (25 ft. + 5 ft./2 levels)
Duration: instantaneous (see text)
Saving throw: Fortitude negates
Spell resistance: yes
Effect: one or more rays of light
Descriptors: good, light
:::

**Sources:** Advanced Race Guide pg 101

> _[Dhampirs](ref/race/dhampir) have access to the following spell._

You blast your enemies with blinding rays of sunlight. You may fire one ray, plus one additional ray
for every four levels beyond 3rd (to a maximum of three rays at 11th level). Each ray requires a
ranged touch attack to hit. If a ray hits, it explodes into powerful motes of light, and the target
must save or be blinded for 1 round. If the target has light blindness, light sensitivity, or is
otherwise vulnerable to bright light, it instead must save or be blinded for 1d4 rounds and take 1d4
points of damage per two caster levels (maximum 5d4). Any creature blinded by a ray sheds light as a
sunrod for the duration of its blindness. The rays may be fired at the same or different targets,
but all rays must be aimed at targets within 30 feet of each other and fired simultaneously.

### Mythic Blinding Ray

**Sources:** Mythic Adventures pg 86\
On a successful saving throw, the target is dazzled for 1 round. On a failed saving throw, the
target is instead blinded for 1d4 rounds.

A target with light blindness, light sensitivity, or any other vulnerability to light is instead
blinded for 1d4 rounds on a successful saving throw and permanently blinded on a failed saving
throw.
