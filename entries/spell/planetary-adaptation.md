+++
id = "ref/spell/planetary-adaptation"
kind = "spell"
title = "Planetary Adaptation"
source_ids = ["people-of-the-stars", "distant-worlds"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "planetary_adaptation", path = "json/spells7.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/planar-adaptation" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Alchemist", level = 5 },
  { class = "Arcanist", level = 5 },
  { class = "Cleric", level = 4 },
  { class = "Investigator", level = 5 },
  { class = "Oracle", level = 4 },
  { class = "Sorcerer", level = 5 },
  { class = "Summoner", level = 5 },
  { class = "Unchained Summoner", level = 5 },
  { class = "Warpriest", level = 4 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 standard action"
components = "V"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 hour/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 4: Cleric, Oracle, Warpriest\
5: Alchemist, Arcanist, Investigator, Sorcerer, Summoner, Unchained Summoner, Wizard
Casting time: 1 standard action
Components: V
Range: personal
Duration: 1 hour/level
Saving throw: none
Spell resistance: no
Target: you
:::

**Sources:** People of the Stars pg 29, Distant Worlds pg 55

This spell functions as [planar adaptation](ref/spell/planar-adaptation), except that it works only
on worlds of the Material Plane. The cold void of space is considered a single world for the purpose
of this spell, allowing you to survive in vacuum.
