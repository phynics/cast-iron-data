+++
id = "ref/spell/roaming-pit"
kind = "spell"
title = "Roaming Pit"
source_ids = ["magic-tactics-toolbox"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "roaming_pit", path = "json/spells8.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/create-pit" },
]

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Creation"]
levels = [
  { class = "Arcanist", level = 5 },
  { class = "Cleric", level = 6 },
  { class = "Druid", level = 6 },
  { class = "Hunter", level = 6 },
  { class = "Occultist", level = 6 },
  { class = "Psychic", level = 6 },
  { class = "Sorcerer", level = 5 },
  { class = "Summoner", level = 5 },
  { class = "Unchained Summoner", level = 5 },
  { class = "Warpriest", level = 6 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 standard action"
components = "V, S, M (powered diamond dust worth 10 gp)"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Effect", value = "mobile 10-ft.-by-10-ft. hold, 10 ft. deep/2 levels" },
]
duration = "1 round/level"
saving_throw = "Reflex negates"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 5: Arcanist, Sorcerer, Summoner, Unchained Summoner, Wizard\
6: Cleric, Druid, Hunter, Occultist, Psychic, Warpriest
Casting time: 1 standard action
Components: V, S, M (powered diamond dust worth 10 gp)
Range: medium (100 ft. + 10 ft./level)
Duration: 1 round/level
Saving throw: Reflex negates
Spell resistance: no
Effect: mobile 10-ft.-by-10-ft. hold, 10 ft. deep/2 levels
Subschool: Creation
:::

**Sources:** Magic Tactics Toolbox pg 13

This spell functions as [create pit](ref/spell/create-pit), except the pit is capable of movement.
As a move action, you can direct the pit to move up to 20 feet, though it must always remain on a
horizontal surface large enough to accommodate its area. If the pit's movement causes it to share a
space with a creature on the same horizontal surface, that creature must succeed at a Reflex saving
throw or fall into the pit. Any creature that avoids falling into the pit when it reaches its new
destination moves to the nearest safe space. Creatures that fall into the pit move with it if it is
relocated.
