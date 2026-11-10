+++
id = "ref/spell/spell-immunity-greater"
kind = "spell"
title = "Greater Spell Immunity"
aon = "SpellDisplay.aspx?ItemName=Spell%20Immunity%2C%20Greater"
source_ids = ["core-rulebook", "ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "spell_immunity_greater", path = "json/spells9.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/spell-immunity" },
]
[[sources]]
publication = "core-rulebook"
page = "347"

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Cleric", level = 8 },
  { class = "Oracle", level = 8 },
  { class = "Psychic", level = 8 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "10 minutes/level"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 8: Cleric, Oracle, Psychic
Casting time: 1 standard action
Components: V, S, DF
Range: touch
Target: creature touched
Duration: 10 minutes/level
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
:::

### Greater Spell Immunity

This spell functions like [spell immunity](ref/spell/spell-immunity), except the immunity applies to
spells of 8th level or lower. A creature can have only one spell immunity or greater spell immunity
spell in effect on it at a time.
