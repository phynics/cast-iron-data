+++
id = "ref/spell/shield-speech-greater"
kind = "spell"
title = "Greater Shield Speech"
source_ids = ["taldor-echoes-of-glory"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "shield_speech_greater", path = "json/spells9.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/shield-speech" },
]
[[sources]]
publication = "taldor-echoes-of-glory"
page = "25"

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Cleric", level = 4 },
  { class = "Druid", level = 4 },
  { class = "Hunter", level = 4 },
  { class = "Oracle", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Warpriest", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S"
range = "30 ft."
effects = [
  { label = "Area", value = "30-ft. emanation centered on you" },
]
duration = "10 minutes/level"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 4: Arcanist, Cleric, Druid, Hunter, Oracle, Sorcerer, Warpriest, Wizard
Casting time: 1 standard action
Components: V, S
Range: 30 ft.
Area: 30-ft. emanation centered on you
Duration: 10 minutes/level
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
:::

### Greater Shield Speech

This spell functions as [shield speech](ref/spell/shield-speech), except all creatures within the
dome may communicate with each other as if linked by shield speech. If they speak with anyone
outside the area, those outside the area hear them normally.
