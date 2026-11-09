+++
id = "ref/spell/tactical-insight"
kind = "spell"
title = "Tactical Insight"
source_ids = ["quests-and-campaigns"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "tactical_insight", path = "json/spells10.json" },
]
[[sources]]
publication = "quests-and-campaigns"
page = "29"

[fields]
kind = "spell"
school = "divination"
levels = [
  { class = "Bard", level = 6 },
  { class = "Inquisitor", level = 6 },
  { class = "Skald", level = 6 },
]
casting_time = "1 standard action"
components = "V, S"
range = "1 hex"
effects = [
  { label = "Targets", value = "one army" },
]
duration = "1 battle"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 6: Bard, Inquisitor, Skald
Casting time: 1 standard action
Components: V, S
Range: 1 hex
Duration: 1 battle
Saving throw: none
Spell resistance: no
Targets: one army
:::

Choose a single army tactic. You grant mastery of this tactic to the target army for the spell's
duration. This tactic may bring an army's total known tactics to a number greater than normally
allowed.
