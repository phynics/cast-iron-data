+++
id = "ref/spell/spell-immunity-greater-communal"
kind = "spell"
title = "Greater Communal Spell Immunity"
aon = "SpellDisplay.aspx?ItemName=Spell%20Immunity%2C%20Greater%20Communal"
source_ids = ["core-rulebook", "ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "spell_immunity_greater_communal", path = "json/spells9.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/spell-immunity-greater" },
]
[[sources]]
publication = "ultimate-combat"
page = "245"

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Cleric", level = 9 },
  { class = "Oracle", level = 9 },
  { class = "Psychic", level = 9 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "touch"
effects = [
  { label = "Target", value = "creatures touched" },
]
duration = "10 minutes/level"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 9: Cleric, Oracle, Psychic
Casting time: 1 standard action
Components: V, S, DF
Range: touch
Target: creatures touched
Duration: 10 minutes/level
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
:::

### Greater Communal Spell Immunity

This spell functions like [greater spell immunity](ref/spell/spell-immunity-greater), except you
divide the duration among the creatures in 10-minute intervals among the creatures touched.
