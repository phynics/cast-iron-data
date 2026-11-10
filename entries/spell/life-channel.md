+++
id = "ref/spell/life-channel"
kind = "spell"
title = "Life Channel"
aon = "SpellDisplay.aspx?ItemName=Life%20Channel"
source_ids = ["advanced-race-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "life_channel", path = "json/spells6.json" },
]
[[sources]]
publication = "advanced-race-guide"
page = "101"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Cleric", level = 2 },
  { class = "Oracle", level = 2 },
  { class = "Warpriest", level = 2 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "one touched creature with negative energy affinity" },
]
duration = "1 minute/level"
saving_throw = "Fortitude negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 2: Cleric, Oracle, Warpriest
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: 1 minute/level
Saving throw: Fortitude negates (harmless)
Spell resistance: yes (harmless)
Target: one touched creature with negative energy affinity
:::

> _[Dhampirs](ref/race/dhampir) have access to the following spell._

When cast on a creature with negative energy affinity, the target is able to convert channeled
positive energy into temporary hit points. When subject to an effect that heals hit points only to
living creatures (such as cure light wounds or channel positive energy), the target gains a number
of temporary hit points equal to half the number of hit points that the positive energy would
normally heal. These temporary hit points go away at the end of this spell's duration.
