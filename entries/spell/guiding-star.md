+++
id = "ref/spell/guiding-star"
kind = "spell"
title = "Guiding Star"
aon = "SpellDisplay.aspx?ItemName=Guiding%20Star"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "guiding_star", path = "json/spells5.json" },
]
[[sources]]
publication = "advanced-players-guide"
page = "226"

[fields]
kind = "spell"
school = "divination"
levels = [
  { class = "Cleric", level = 3 },
  { class = "Hunter", level = 2 },
  { class = "Oracle", level = 3 },
  { class = "Psychic", level = 3 },
  { class = "Ranger", level = 2 },
  { class = "Shaman", level = 2 },
  { class = "Warpriest", level = 3 },
  { class = "Witch", level = 3 },
]
casting_time = "1 minute"
components = "V, S, M (a spool of thread or string)"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 day/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 2: Hunter, Ranger, Shaman\
3: Cleric, Oracle, Psychic, Warpriest, Witch
Casting time: 1 minute
Components: V, S, M (a spool of thread or string)
Range: personal
Duration: 1 day/level (D)
Saving throw: none
Spell resistance: no
Target: you
:::

You form a bond with your surroundings when you cast this spell. For the remaining duration of the
spell you can always, as a standard action, determine your approximate distance from that area as
well as the direction you must travel in order to reach it. You cannot determine the location of the
area if you are on a different plane. The area counts as "very familiar" for the purposes of
teleport or similar spells. You can only attune yourself to one location at a time. If you cast the
spell at another spot you lose the ability to locate your original area.
