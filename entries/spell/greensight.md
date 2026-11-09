+++
id = "ref/spell/greensight"
kind = "spell"
title = "Greensight"
source_ids = ["ultimate-wilderness", "rival-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "greensight", path = "json/spells5.json" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "231"
[[sources]]
publication = "rival-guide"
page = "23"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Druid", level = 2 },
  { class = "Hunter", level = 2 },
  { class = "Shaman", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, M (a leaf)"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "10 minutes/level"
saving_throw = "Will negates (harmless)"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 2: Arcanist, Druid, Hunter, Shaman, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M (a leaf)
Range: touch
Duration: 10 minutes/level
Saving throw: Will negates (harmless)
Spell resistance: no
Target: creature touched
:::

The target of this spell gains the ability to see up to 60 feet through thick plant matter as though
it were transparent. Greenery, leaves, and vines - even lichen, moss, and slime - offer no
concealment to the recipient's sight, though her vision still can be blocked by solid wood, such as
trees or wooden structures. Undergrowth does not grant concealment to a creature against a target of
the effects of greensight.
