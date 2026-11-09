+++
id = "ref/spell/thaumaturgic-circle"
kind = "spell"
title = "Thaumaturgic Circle"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "thaumaturgic_circle", path = "json/spells10.json" },
]
[[sources]]
publication = "occult-adventures"
page = "189"

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Cleric", level = 4 },
  { class = "Inquisitor", level = 4 },
  { class = "Medium", level = 3 },
  { class = "Occultist", level = 3 },
  { class = "Oracle", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Summoner", level = 4 },
  { class = "Warpriest", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S, DF, M (a 3-ft.-diameter circle of powdered silver)"
range = "touch"
effects = [
  { label = "Area", value = "10-ft.-radius emanation from touched creature" },
]
duration = "10 minutes/level"
saving_throw = "Will negates (harmless)"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 3: Medium, Occultist\
4: Arcanist, Cleric, Inquisitor, Oracle, Sorcerer, Summoner, Warpriest, Wizard
Casting time: 1 standard action
Components: V, S, DF, M (a 3-ft.-diameter circle of powdered silver)
Range: touch
Duration: 10 minutes/level
Saving throw: Will negates (harmless)
Spell resistance: no
Area: 10-ft.-radius emanation from touched creature
:::

This spell functions as [magic circle against chaos](ref/spell/magic-circle-against-chaos), evil,
good, or law, but rather than stipulating an alignment descriptor, you can designate any one
non-alignment subtype of outsider, including air, earth, fire, and water, as well as outsider races
such as angels and devils.
