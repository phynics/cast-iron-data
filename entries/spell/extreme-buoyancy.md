+++
id = "ref/spell/extreme-buoyancy"
kind = "spell"
title = "Extreme Buoyancy"
source_ids = ["aquatic-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "extreme_buoyancy", path = "json/spells4.json" },
]
[[sources]]
publication = "aquatic-adventures"
page = "59"

[fields]
kind = "spell"
school = "evocation"
levels = [
  { class = "Alchemist", level = 2 },
  { class = "Bard", level = 2 },
  { class = "Druid", level = 2 },
  { class = "Hunter", level = 2 },
  { class = "Investigator", level = 2 },
  { class = "Medium", level = 2 },
  { class = "Occultist", level = 2 },
  { class = "Psychic", level = 2 },
  { class = "Ranger", level = 2 },
  { class = "Shaman", level = 2 },
  { class = "Skald", level = 2 },
  { class = "Warpriest", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, DF, M (a bag of air)"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "10 minutes/level"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 2: Alchemist, Bard, Druid, Hunter, Investigator, Medium, Occultist, Psychic, Ranger, Shaman, Skald, Warpriest
Casting time: 1 standard action
Components: V, S, DF, M (a bag of air)
Range: touch
Duration: 10 minutes/level
Saving throw: Will negates
Spell resistance: yes
Target: creature touched
:::

The target's buoyancy becomes and stays swiftly rising, regardless of how dense the target and its
gear are. Among other effects, the target needs to succeed at a DC 20 Swim check to submerge itself
and to stay submerged (see [Buoyancy](ref/rule/buoyancy)).
