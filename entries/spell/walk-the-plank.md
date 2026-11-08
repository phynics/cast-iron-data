+++
id = "ref/spell/walk-the-plank"
kind = "spell"
title = "Walk the Plank"
source_ids = ["advanced-players-guide", "villain-codex"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "walk_the_plank", path = "json/spells3.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/create-pit" },
]

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Creation"]
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Summoner", level = 2 },
  { class = "Unchained Summoner", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, F (miniature shovel costing 10 gp)"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Effect", value = "10-ft.-by-10-ft. hole, 10 ft. deep/2 levels" },
]
duration = "1 round + 1 round/level"
saving_throw = "Reflex negates"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 2: Arcanist, Sorcerer, Summoner, Unchained Summoner, Wizard
Casting time: 1 standard action
Components: V, S, F (miniature shovel costing 10 gp)
Range: medium (100 ft. + 10 ft./level)
Duration: 1 round + 1 round/level
Saving throw: Reflex negates
Spell resistance: no
Effect: 10-ft.-by-10-ft. hole, 10 ft. deep/2 levels
Subschool: Creation
:::

### Walk the Plank

**Sources:** Villain Codex pg 188

This spell functions as per [create pit](ref/spell/create-pit), except as noted here. All but the
top 10 feet of the hole is filled with saltwater, reducing the fall damage for anyone falling into
the pit to 1d3 points of nonlethal damage and allowing Huge or larger creatures at the water's
surface to simply pull themselves out of the pit as part of a normal move action, without a Climb
check. Additionally, the pit contains a single advanced shark for every 4 caster levels you have
(maximum four advanced sharks). If desired, when you cast the spell, you can substitute two of the
summoned sharks for one great white shark. These sharks immediately attack any creature that falls
into the pit, even you. If multiple creatures fall in the pit, the sharks attack randomly. When the
spell ends, creatures inside the hole rise up with the bottom of the pit, as normal for create pit,
but the conjured water and sharks vanish.
