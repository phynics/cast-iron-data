+++
id = "ref/spell/endothermic-touch"
kind = "spell"
title = "Endothermic Touch"
aon = "SpellDisplay.aspx?ItemName=Endothermic%20Touch"
source_ids = ["monster-codex"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "endothermic_touch", path = "json/spells4.json" },
]
[[sources]]
publication = "monster-codex"
page = "141"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Arcanist", level = 1 },
  { class = "Druid", level = 1 },
  { class = "Hunter", level = 1 },
  { class = "Shaman", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Witch", level = 1 },
  { class = "Wizard", level = 1 },
]
casting_time = "1 standard action"
components = "V, S, M/DF (a small bit of snakeskin)"
range = "touch"
effects = [
  { label = "Target", value = "one living creature that has the dragon type or the reptilian subtype" },
]
duration = "1 round/level"
saving_throw = "Fortitude negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 1: Arcanist, Druid, Hunter, Shaman, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M/DF (a small bit of snakeskin)
Range: touch
Duration: 1 round/level
Saving throw: Fortitude negates
Spell resistance: yes
Target: one living creature that has the dragon type or the reptilian subtype
:::

This spell slows the metabolism and other bodily functions of a creature for a short amount of time.
The target is staggered and moves at half its normal speed (round down to the next 5-foot
increment), but it can hold its breath for twice as long as normal.
