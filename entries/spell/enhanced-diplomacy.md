+++
id = "ref/spell/enhanced-diplomacy"
kind = "spell"
title = "Enhanced Diplomacy"
source_ids = ["taldor-echoes-of-glory"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "enhanced_diplomacy", path = "json/spells4.json" },
]
[[sources]]
publication = "taldor-echoes-of-glory"
page = "24"

[fields]
kind = "spell"
school = "divination"
levels = [
  { class = "Cleric", level = 0 },
  { class = "Druid", level = 0 },
  { class = "Hunter", level = 0 },
  { class = "Oracle", level = 0 },
  { class = "Warpriest", level = 0 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "1 minute or until discharged"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 0: Cleric, Druid, Hunter, Oracle, Warpriest
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: 1 minute or until discharged
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
Target: creature touched
:::

You imbue the subject with divine diplomacy skills. The creature gets a +2 competence bonus on a
single Diplomacy or Intimidate check. It must choose to use the bonus before making the roll to
which it applies.
