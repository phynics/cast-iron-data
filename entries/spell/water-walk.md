+++
id = "ref/spell/water-walk"
kind = "spell"
title = "Water Walk"
source_ids = ["core-rulebook", "ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "water_walk", path = "json/spells11.json" },
]

[fields]
kind = "spell"
school = "transmutation"
descriptors = ["water"]
levels = [
  { class = "Cleric", level = 3 },
  { class = "Hunter", level = 3 },
  { class = "Medium", level = 2 },
  { class = "Oracle", level = 3 },
  { class = "Psychic", level = 3 },
  { class = "Ranger", level = 3 },
  { class = "Shaman", level = 3 },
  { class = "Warpriest", level = 3 },
  { class = "Witch", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "touch"
effects = [
  { label = "Targets", value = "one touched creature/level" },
]
duration = "10 minutes/level (D)"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 2: Medium\
3: Cleric, Hunter, Oracle, Psychic, Ranger, Shaman, Warpriest, Witch
Casting time: 1 standard action
Components: V, S, DF
Range: touch
Duration: 10 minutes/level (D)
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
Targets: one touched creature/level
Descriptors: water
:::

**Sources:** PRPG Core Rulebook pg 368

The transmuted creatures can tread on any liquid as if it were firm ground. Mud, oil, snow,
quicksand, running water, ice, and even lava can be traversed easily, since the subjects' feet hover
an inch or two above the surface. Creatures crossing molten lava still take damage from the heat
because they are near it. The subjects can walk, run, charge, or otherwise move across the surface
as if it were normal ground.

If the spell is cast underwater (or while the subjects are partially or wholly submerged in whatever
liquid they are in), the subjects are borne toward the surface at 60 feet per round until they can
stand on it.

### Communal Water Walk

**Sources:** Ultimate Combat pg 249

This spell functions like water walk, except you divide the duration in 10-minute intervals among
the creatures touched.
