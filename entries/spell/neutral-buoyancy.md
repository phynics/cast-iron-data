+++
id = "ref/spell/neutral-buoyancy"
kind = "spell"
title = "Neutral Buoyancy"
source_ids = ["aquatic-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "neutral_buoyancy", path = "json/spells7.json" },
]
[[sources]]
publication = "aquatic-adventures"
page = "60"

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
Level: 2: Alchemist, Bard, Druid, Hunter, Investigator, Medium, Occultist, Psychic, Ranger, Shaman
Casting time: 1 standard action
Components: V, S, DF, M (a bag of air)
Range: touch
Duration: 10 minutes/level
Saving throw: Will negates
Spell resistance: yes
Target: creature touched
:::

The target's buoyancy becomes and stays neutral, regardless of how dense the target and its gear
are. Among other effects, the target neither sinks nor rises when it doesn't attempt a Swim check,
making it easier to stay put while performing demanding actions or when helpless or disabled, and
the target can swim up and down with equal ease.
