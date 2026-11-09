+++
id = "ref/spell/lead-anchor"
kind = "spell"
title = "Lead Anchor"
aon = "SpellDisplay.aspx?ItemName=Lead%20Anchor"
source_ids = ["aquatic-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "lead_anchor", path = "json/spells6.json" },
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
  { class = "Skald", level = 2 },
  { class = "Witch", level = 2 },
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
Level: 2: Alchemist, Bard, Druid, Hunter, Investigator, Medium, Occultist, Psychic, Ranger, Shaman, Skald, Witch
Casting time: 1 standard action
Components: V, S, DF, M (a bag of air)
Range: touch
Duration: 10 minutes/level
Saving throw: Will negates
Spell resistance: yes
Target: creature touched
:::

The target's buoyancy becomes and stays swiftly sinking, regardless of how dense the target and its
gear are. Among other effects, the target can walk on the bottom, but she also needs to succeed at a
DC 20 Swim check to swim towards the surface and to stay above the bottom (see
[Buoyancy](ref/rule/buoyancy)). This makes lead anchor a useful spell both for exploring the sea
floor and for drowning an air-breathing foe in the water.
