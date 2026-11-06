+++
id = "ref/spell/mirage-arcana"
kind = "spell"
title = "Mirage Arcana"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "mirage_arcana", path = "json/spells14.json" },
]

[fields]
kind = "spell"
school = "illusion"
subschools = ["Glamer"]
descriptors = ["glamer"]
levels = [
  { class = "Arcanist", level = 5 },
  { class = "Bard", level = 5 },
  { class = "Mesmerist", level = 5 },
  { class = "Psychic", level = 5 },
  { class = "Skald", level = 5 },
  { class = "Sorcerer", level = 5 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 standard action"
components = "V, S"
range = "long (400 ft. + 40 ft./level)"
effects = [
  { label = "Area", value = "one 20-ft. cube/level (S)" },
]
duration = "concentration+1 hour/level (D)"
saving_throw = "Will disbelief (if interacted with)"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 5: Arcanist, Bard, Mesmerist, Psychic, Skald, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S
Range: long (400 ft. + 40 ft./level)
Duration: concentration+1 hour/level (D)
Saving throw: Will disbelief (if interacted with)
Spell resistance: no
Area: one 20-ft. cube/level (S)
Subschool: Glamer
Descriptors: glamer
:::

**Sources:** PRPG Core Rulebook pg 314

This spell functions like hallucinatory terrain, except that it enables you to make any area appear
to be something other than it is. The illusion includes audible, visual, tactile, and olfactory
elements. Unlike hallucinatory terrain, the spell can alter the appearance of structures (or add
them where none are present). Still, it can't disguise, conceal, or add creatures (though creatures
within the area might hide themselves within the illusion just as they can hide themselves within a
real location).
