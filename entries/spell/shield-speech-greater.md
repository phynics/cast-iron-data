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

## Shield Speech

**Sources:** Taldor, Echoes of Glory pg 25

You can securely communicate with one creature within range. So long as your target remains within
10 feet of you, you and it can speak freely to each other without fear of being overheard.
Communications that involve shield speech cannot be spied on, such as with a divination spell, and
observers of the conversation can tell you are communicating but cannot read lips or hear the
conversation unless they are the target of the spell. If you or the target speak to any other
creatures, they can hear you normally (only communication between you and the target is protected).
The spell does not shield writing, sign language, or any form of communication other than speaking.

### Greater Shield Speech

**Sources:** Taldor, Echoes of Glory pg 25

This spell functions as [shield speech](ref/spell/shield-speech), except all creatures within the
dome may communicate with each other as if linked by shield speech. If they speak with anyone
outside the area, those outside the area hear them normally.
