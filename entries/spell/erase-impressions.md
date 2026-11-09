+++
id = "ref/spell/erase-impressions"
kind = "spell"
title = "Erase Impressions"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "erase_impressions", path = "json/spells4.json" },
]
[[sources]]
publication = "occult-adventures"
page = "170"

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Medium", level = 3 },
  { class = "Mesmerist", level = 4 },
  { class = "Occultist", level = 3 },
  { class = "Psychic", level = 5 },
  { class = "Spiritualist", level = 4 },
]
casting_time = "1 round"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "object touched" },
]
duration = "instantaneous"
saving_throw = "Will negates (object)"
spell_resistance = "yes (object)"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 3: Medium, Occultist\
4: Mesmerist, Spiritualist\
5: Psychic
Casting time: 1 round
Components: V, S
Range: touch
Duration: instantaneous
Saving throw: Will negates (object)
Spell resistance: yes (object)
Target: object touched
:::

You banish psychic impressions from the object touched, rendering it devoid of recent history. You
choose how much time to erase, up to a maximum of 1 day per caster level. You must erase impressions
from the present time back; you cannot choose to leave recent events untouched. Impressions erased
in this manner cannot be recovered via object reading, legend lore, or similar measures.

Casting erase impressions on a corpse removes recent psychic impressions from when the creature was
alive as well, making those memories unavailable to [speak with dead](ref/spell/speak-with-dead).
For example, a 5th-level caster casting the spell on a 2-day-old corpse could erase the past 2 days
of psychic impressions from the corpse and 3 additional days of information from just before the
creature died.
