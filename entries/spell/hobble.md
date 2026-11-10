+++
id = "ref/spell/hobble"
kind = "spell"
title = "Hobble"
aon = "SpellDisplay.aspx?ItemName=Hobble"
source_ids = ["villain-codex"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "hobble", path = "json/spells5.json" },
]
[[sources]]
publication = "villain-codex"
page = "200"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Arcanist", level = 1 },
  { class = "Bloodrager", level = 1 },
  { class = "Bard", level = 1 },
  { class = "Hunter", level = 1 },
  { class = "Inquisitor", level = 1 },
  { class = "Magus", level = 1 },
  { class = "Mesmerist", level = 1 },
  { class = "Ranger", level = 1 },
  { class = "Skald", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Wizard", level = 1 },
]
casting_time = "1 standard action"
components = "V, S, M (a drop of glue)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Targets", value = "one creature/level, no two of which can be more than 20 feet apart" },
]
duration = "1 round/level"
saving_throw = "Fortitude negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 1: Arcanist, Bloodrager, Bard, Hunter, Inquisitor, Magus, Mesmerist, Ranger, Skald, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M (a drop of glue)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level
Saving throw: Fortitude negates
Spell resistance: yes
Targets: one creature/level, no two of which can be more than 20 feet apart
:::

This spell disrupts the method a target uses for movement. Creatures under the effects of this spell
move at half their base speed (rounded down to the nearest 5-foot increment) but can still take
5-foot steps as normal. Incorporeal creatures and creatures flying with perfect maneuverability are
immune to the effects of this spell. Each round, a target receives another save to end the effect.
