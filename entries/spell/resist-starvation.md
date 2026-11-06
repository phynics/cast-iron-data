+++
id = "ref/spell/resist-starvation"
kind = "spell"
title = "Resist Starvation"
source_ids = ["villain-codex"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "resist_starvation", path = "json/spells8.json" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Antipaladin", level = 1 },
  { class = "Cleric", level = 1 },
  { class = "Oracle", level = 1 },
  { class = "Shaman", level = 1 },
  { class = "Warpriest", level = 1 },
]
casting_time = "1 standard action"
components = "V, S, M (crumb of food)"
range = "touch"
effects = [
  { label = "Target", value = "one living creature touched" },
]
duration = "1 day/level"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 1: Antipaladin, Cleric, Oracle, Shaman, Warpriest
Casting time: 1 standard action
Components: V, S, M (crumb of food)
Range: touch
Duration: 1 day/level
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
Target: one living creature touched
:::

**Sources:** Villain Codex pg 21

If the target doesn't eat on the day this spell is cast on it, the DC to avoid taking nonlethal
damage from starvation on the following day doesn't increase by 1. This spell fails if the target
hasn't already attempted at least one Constitution check to avoid starvation.
