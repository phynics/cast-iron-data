+++
id = "ref/spell/spell-immunity-communal"
kind = "spell"
title = "Communal Spell Immunity"
aon = "SpellDisplay.aspx?ItemName=Spell%20Immunity%2C%20Communal"
source_ids = ["core-rulebook", "ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "spell_immunity_communal", path = "json/spells9.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/spell-immunity" },
]
[[sources]]
publication = "ultimate-combat"
page = "244"

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Alchemist", level = 4 },
  { class = "Cleric", level = 4 },
  { class = "Inquisitor", level = 4 },
  { class = "Investigator", level = 4 },
  { class = "Occultist", level = 4 },
  { class = "Oracle", level = 4 },
  { class = "Psychic", level = 4 },
  { class = "Spiritualist", level = 4 },
  { class = "Warpriest", level = 4 },
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
Level: 4: Alchemist, Cleric, Inquisitor, Investigator, Occultist, Oracle, Psychic, Spiritualist, Warpriest
Casting time: 1 standard action
Components: V, S, DF
Range: touch
Duration: 10 minutes/level
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
Target: creature touched
:::

### Communal Spell Immunity

This spell functions like [spell immunity](ref/spell/spell-immunity), except you divide the duration
in 10-minute intervals among the creatures touched.
