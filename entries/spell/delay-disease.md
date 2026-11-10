+++
id = "ref/spell/delay-disease"
kind = "spell"
title = "Delay Disease"
source_ids = ["advanced-race-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "delay_disease", path = "json/spells3.json" },
]
[[sources]]
publication = "advanced-race-guide"
page = "155"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Healing"]
levels = [
  { class = "Alchemist", level = 2 },
  { class = "Cleric", level = 2 },
  { class = "Druid", level = 2 },
  { class = "Hunter", level = 2 },
  { class = "Inquisitor", level = 2 },
  { class = "Investigator", level = 2 },
  { class = "Mesmerist", level = 2 },
  { class = "Oracle", level = 2 },
  { class = "Paladin", level = 2 },
  { class = "Ranger", level = 2 },
  { class = "Warpriest", level = 2 },
  { class = "Witch", level = 1 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "1 day"
saving_throw = "Fortitude negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 1: Witch\
2: Alchemist, Cleric, Druid, Hunter, Inquisitor, Investigator, Mesmerist, Oracle, Paladin, Ranger, Warpriest
Casting time: 1 standard action
Components: V, S, DF
Range: touch
Duration: 1 day
Saving throw: Fortitude negates (harmless)
Spell resistance: yes (harmless)
Target: creature touched
Subschool: Healing
:::

> _[Ratfolk](ref/race/ratfolk) have access to the following spell._

The target becomes temporarily immune to disease. Any disease to which it is exposed during the
spell's duration does not affect the target until the spell's duration has expired. If the target is
currently infected with a disease, you must make a caster level check against the disease's DC to
suspend it for the duration of the spell; otherwise, that disease affects the target normally. Delay
disease does not cure any damage a disease may have already done.
