+++
id = "ref/spell/gravity-well"
kind = "spell"
title = "Gravity Well"
aon = "SpellDisplay.aspx?ItemName=Gravity%20Well"
source_ids = ["dragonslayers-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "gravity_well", path = "json/spells5.json" },
]
[[sources]]
publication = "dragonslayers-handbook"
page = "29"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Arcanist", level = 5 },
  { class = "Druid", level = 6 },
  { class = "Hunter", level = 6 },
  { class = "Sorcerer", level = 5 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 standard action"
components = "V, S, M (a small lead weight)"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "1 round/level (D)"
saving_throw = "Fortitude negates"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 5: Arcanist, Sorcerer, Wizard\
6: Druid, Hunter
Casting time: 1 standard action
Components: V, S, M (a small lead weight)
Range: medium (100 ft. + 10 ft./level)
Duration: 1 round/level (D)
Saving throw: Fortitude negates
Spell resistance: no
Target: one creature
:::

You bring into being a localized region of increased gravity that crushes a creature to the ground.
Affected targets weigh twice as much as normal, can move only at half speed, jump only half as far
as normal, and can lift and carry only half as much as normal. Any flying target has its
maneuverability worsened by two steps (from good to poor, for example; minimum clumsy) and plummets
to the ground unless it succeeds at a DC 25 Fly check to remain in the air.
[Freedom of movement](ref/spell/freedom-of-movement) negates the effects of this spell. A creature
targeted by gravity well behaves normally in the area of a reverse gravity spell.
