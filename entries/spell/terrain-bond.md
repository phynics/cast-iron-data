+++
id = "ref/spell/terrain-bond"
kind = "spell"
title = "Terrain Bond"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "terrain_bond", path = "json/spells10.json" },
]
[[sources]]
publication = "ultimate-combat"
page = "247"

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Hunter", level = 4 },
  { class = "Ranger", level = 4 },
]
casting_time = "1 standard action"
components = "V, S, M (a pinch of earth taken from your most favored terrain)"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 hour/2 levels (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 4: Hunter, Ranger
Casting time: 1 standard action
Components: V, S, M (a pinch of earth taken from your most favored terrain)
Range: personal
Duration: 1 hour/2 levels (D)
Saving throw: none
Spell resistance: no
Target: you
Subschool: Compulsion
Descriptors: mind-affecting
:::

You call upon the spirits of nature to help you adapt to your environment. You treat the terrain you
are in as your most [favored terrain](ref/ability/favored-terrain) until this spell ends.

If you do not have the favored terrain class feature, you gain no benefit from this spell.
