+++
id = "ref/spell/spell-absorption-greater"
kind = "spell"
title = "Greater Spell Absorption"
source_ids = ["inner-sea-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "spell_absorption_greater", path = "json/spells9.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/spell-absorption" },
]
[[sources]]
publication = "inner-sea-magic"
page = "61"

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Arcanist", level = 8 },
  { class = "Sorcerer", level = 8 },
  { class = "Wizard", level = 8 },
]
casting_time = "1 round"
components = "V, S, M (a prism)"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 round/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 8: Arcanist, Sorcerer, Wizard
Casting time: 1 round
Components: V, S, M (a prism)
Range: personal
Target: you
Duration: 1 round/level
Saving throw: none
Spell resistance: no
:::

### Greater Spell Absorption

This spell functions as [spell absorption](ref/spell/spell-absorption), save that you can absorb
countered spells of 6th level or lower.
