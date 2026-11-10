+++
id = "ref/spell/object-reading"
kind = "spell"
title = "Object Reading"
aon = "SpellDisplay.aspx?ItemName=Object%20Reading"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "object_reading", path = "json/spells7.json" },
]
[[sources]]
publication = "occult-adventures"
page = "179"

[fields]
kind = "spell"
school = "divination"
levels = [
  { class = "Medium", level = 1 },
  { class = "Mesmerist", level = 2 },
  { class = "Occultist", level = 1 },
  { class = "Psychic", level = 2 },
  { class = "Spiritualist", level = 2 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "one touched object" },
]
duration = "concentration, up to 1 round per level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 1: Medium, Occultist\
2: Mesmerist, Psychic, Spiritualist
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: concentration, up to 1 round per level (D)
Saving throw: none
Spell resistance: no
Target: one touched object
:::

You read the psychic impressions left upon an object by emotionally or psychically charged events in
the item's history, or the information imprinted by the [charge object](ref/spell/charge-object) or
[implant false reading](ref/spell/implant-false-reading) spells. This spell returns the same
information as the [psychometry](ref/skill/appraise) occult skill unlock, but gives 1 piece of
information when cast and requires 1 round of concentration per additional piece of information
instead of 1 minute. You must still attempt an Appraise check to see how much information you gain.
You gain a +10 competence bonus on the check.
