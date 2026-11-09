+++
id = "ref/spell/spell-resistance"
kind = "spell"
title = "Spell Resistance"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "spell_resistance", path = "json/spells9.json" },
]
[[sources]]
publication = "core-rulebook"
page = "347"

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Alchemist", level = 5 },
  { class = "Cleric", level = 5 },
  { class = "Inquisitor", level = 5 },
  { class = "Investigator", level = 5 },
  { class = "Occultist", level = 5 },
  { class = "Oracle", level = 5 },
  { class = "Psychic", level = 5 },
  { class = "Spiritualist", level = 5 },
  { class = "Warpriest", level = 5 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "1 minute/level"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 5: Alchemist, Cleric, Inquisitor, Investigator, Occultist, Oracle, Psychic, Spiritualist, Warpriest
Casting time: 1 standard action
Components: V, S, DF
Range: touch
Duration: 1 minute/level
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
Target: creature touched
:::

The target gains spell resistance equal to 12 + your caster level.
