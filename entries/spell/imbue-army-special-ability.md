+++
id = "ref/spell/imbue-army-special-ability"
kind = "spell"
title = "Imbue Army Special Ability"
source_ids = ["quests-and-campaigns"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "imbue_army_special_ability", path = "json/spells14.json" },
]

[fields]
kind = "spell"
school = "evocation"
levels = [
  { class = "Cleric", level = 9 },
  { class = "Oracle", level = 9 },
]
casting_time = "10 minutes"
components = "V, S, F (a silver mirror worth 100 gp)"
range = "1 hex"
effects = [
  { label = "Target", value = "one army" },
]
duration = "1 battle"
saving_throw = "none or Will negates (harmless)"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 9: Cleric, Oracle
Casting time: 10 minutes
Components: V, S, F (a silver mirror worth 100 gp)
Range: 1 hex
Duration: 1 battle
Saving throw: none or Will negates (harmless)
Spell resistance: yes
Target: one army
:::

**Sources:** Quests and Campaigns pg 29

You imbue the target with an [army special ability](ref/rule/special-abilities-ucp) possessed by the
army's commander. The army is treated as if it consists of units who all possess the chosen special
ability. This special ability is in addition to any special abilities the army inherently possessed
prior to the casting of the spell.
