+++
id = "ref/spell/soothing-mud"
kind = "spell"
title = "Soothing Mud"
source_ids = ["ultimate-wilderness"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "soothing_mud", path = "json/spells9.json" },
]

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Healing"]
descriptors = ["earth", "water"]
levels = [
  { class = "Druid", level = 3 },
  { class = "Hunter", level = 3 },
  { class = "Ranger", level = 3 },
  { class = "Shaman", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Area", value = "dust, earth, sand, or water in one 5-ft. square/level" },
]
duration = "1 round/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 3: Druid, Hunter, Ranger, Shaman
Casting time: 1 standard action
Components: V, S, DF
Range: medium (100 ft. + 10 ft./level)
Duration: 1 round/level (D)
Saving throw: none
Spell resistance: no
Area: dust, earth, sand, or water in one 5-ft. square/level
Subschool: Healing
Descriptors: earth, water
:::

**Sources:** Ultimate Wilderness pg 236

You create an area of healing mud. Water, earth, sand, and dust thicken into a wet mud. The mud
functions as difficult terrain and does not sink if created in water unless weighed down by more
than 100 pounds per caster level you have. Each round a creature begins its turn in or on the mud,
the mud restores 1 hit point to it; this healing is unaffected by effects that increase a creature's
healing. A creature that rests partially or completely submerged in this mud for 1 full minute is
also healed of 1d4 points of ability damage to an ability score of its choice. A creature can be
healed of ability damage this way only once per day.
