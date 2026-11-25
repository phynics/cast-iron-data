+++
id = "ref/spell/delay-poison-communal"
kind = "spell"
title = "Communal Delay Poison"
aon = "SpellDisplay.aspx?ItemName=Delay%20Poison%2C%20Communal"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "delay_poison_communal", path = "json/spells3.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/delay-poison" },
]
[[sources]]
publication = "ultimate-combat"
page = "227"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["healing"]
levels = [
  { class = "Alchemist", level = 3 },
  { class = "Bard", level = 3 },
  { class = "Cleric", level = 3 },
  { class = "Druid", level = 3 },
  { class = "Hunter", level = 3 },
  { class = "Inquisitor", level = 3 },
  { class = "Investigator", level = 3 },
  { class = "Oracle", level = 3 },
  { class = "Paladin", level = 3 },
  { class = "Ranger", level = 3 },
  { class = "Skald", level = 3 },
  { class = "Warpriest", level = 3 },
  { class = "Witch", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "touch"
effects = [
  { label = "Targets", value = "creatures touched" },
]
duration = "1 hour/level"
saving_throw = "Fortitude negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 3: Alchemist, Bard, Cleric, Druid, Hunter, Inquisitor, Investigator, Oracle, Paladin, Ranger, Skald, Warpriest, Witch
Casting time: 1 standard action
Components: V, S, DF
Range: touch
Duration: 1 hour/level
Saving throw: Fortitude negates (harmless)
Spell resistance: yes (harmless)
Targets: creatures touched
Subschool: healing
:::

### Communal Delay Poison

This spell functions like [delay poison](ref/spell/delay-poison), except you divide the duration in
1-hour intervals among the creatures touched.
