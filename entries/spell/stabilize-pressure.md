+++
id = "ref/spell/stabilize-pressure"
kind = "spell"
title = "Stabilize Pressure"
aon = "SpellDisplay.aspx?ItemName=Stabilize%20Pressure"
source_ids = ["aquatic-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "stabilize_pressure", path = "json/spells9.json" },
]
[[sources]]
publication = "aquatic-adventures"
page = "61"

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Alchemist", level = 2 },
  { class = "Bloodrager", level = 2 },
  { class = "Cleric", level = 2 },
  { class = "Druid", level = 2 },
  { class = "Hunter", level = 2 },
  { class = "Investigator", level = 2 },
  { class = "Oracle", level = 2 },
  { class = "Psychic", level = 2 },
  { class = "Ranger", level = 2 },
  { class = "Shaman", level = 2 },
  { class = "Summoner", level = 2 },
  { class = "Unchained Summoner", level = 2 },
  { class = "Warpriest", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, M (a piece of shell)"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "instantaneous"
saving_throw = "Fortitude negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 2: Alchemist, Bloodrager, Cleric, Druid, Hunter, Investigator, Oracle, Psychic, Ranger, Shaman, Summoner, Unchained Summoner, Warpriest
Casting time: 1 standard action
Components: V, S, M (a piece of shell)
Range: touch
Duration: instantaneous
Saving throw: Fortitude negates (harmless)
Spell resistance: yes (harmless)
Target: creature touched
:::

You instantly stabilize the target's pressure, causing it to adjust to its current pressure all at
once. This doesn't help it readjust to future pressure changes.
