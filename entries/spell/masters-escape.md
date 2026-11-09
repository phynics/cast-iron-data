+++
id = "ref/spell/masters-escape"
kind = "spell"
title = "Master's Escape"
source_ids = ["monster-summoners-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "masters_escape", path = "json/spells14.json" },
]
[[sources]]
publication = "monster-summoners-handbook"
page = "22"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Teleportation"]
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Cleric", level = 4 },
  { class = "Druid", level = 4 },
  { class = "Hunter", level = 4 },
  { class = "Oracle", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Summoner", level = 3 },
  { class = "Warpriest", level = 4 },
  { class = "Witch", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "you and one summoned creature you control" },
]
duration = "1 round/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 3: Summoner\
4: Arcanist, Cleric, Druid, Hunter, Oracle, Sorcerer, Warpriest, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level (D)
Saving throw: none
Spell resistance: no
Target: you and one summoned creature you control
Subschool: Teleportation
:::

You create an extradimensional link between yourself and one summoned creature you control that
allows you to switch places. After casting master's escape, you can teleport to your summoned
creature's space as a swift action, causing your summoned creature to teleport to your former space.
If your summoned creature is reduced to 0 or fewer hit points before you can use this spell's
effect, you can teleport to a space that you can see within 30 feet as an immediate action. After
using either of these effects, the spell ends. A summoner can target his eidolon with this spell.
