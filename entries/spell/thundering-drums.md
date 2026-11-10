+++
id = "ref/spell/thundering-drums"
kind = "spell"
title = "Thundering Drums"
aon = "SpellDisplay.aspx?ItemName=Thundering%20Drums"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "thundering_drums", path = "json/spells10.json" },
]
[[sources]]
publication = "advanced-players-guide"
page = "249"

[fields]
kind = "spell"
school = "evocation"
descriptors = ["sonic"]
levels = [
  { class = "Bard", level = 3 },
  { class = "Skald", level = 3 },
]
casting_time = "1 standard action"
components = "V, S"
range = "15 ft."
effects = [
  { label = "Area", value = "cone-shaped burst" },
]
duration = "instantaneous"
saving_throw = "Fortitude partial"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 3: Bard, Skald
Casting time: 1 standard action
Components: V, S
Range: 15 ft.
Duration: instantaneous
Saving throw: Fortitude partial
Spell resistance: yes
Area: cone-shaped burst
Descriptors: sonic
:::

You strike the ground in front of you, filling the area in front of you with the thunder of pounding
drums. Any creature in the area takes 1d8 points of sonic damage per caster level (maximum 5d8) and
is knocked prone. A successful Fortitude save halves the damage and negates being knocked prone.
