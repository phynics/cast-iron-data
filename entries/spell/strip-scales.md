+++
id = "ref/spell/strip-scales"
kind = "spell"
title = "Strip Scales"
aon = "SpellDisplay.aspx?ItemName=Strip%20Scales"
source_ids = ["kobolds-of-golarion"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "strip_scales", path = "json/spells15.json" },
]
[[sources]]
publication = "kobolds-of-golarion"
page = "27"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Arcanist", level = 5 },
  { class = "Druid", level = 4 },
  { class = "Hunter", level = 4 },
  { class = "Sorcerer", level = 5 },
  { class = "Witch", level = 5 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 standard action"
components = "V, S, M/DF (a single reptile scale)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one living creature" },
]
duration = "1 minute/level"
saving_throw = "Fortitude"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 4: Druid, Hunter\
5: Arcanist, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M/DF (a single reptile scale)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 minute/level
Saving throw: Fortitude
Spell resistance: yes
Target: one living creature
:::

You reduce the target's racial natural armor bonus by 1 point per 3 caster levels.
