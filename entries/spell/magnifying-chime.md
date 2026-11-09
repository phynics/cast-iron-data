+++
id = "ref/spell/magnifying-chime"
kind = "spell"
title = "Magnifying Chime"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "magnifying_chime", path = "json/spells6.json" },
]
[[sources]]
publication = "advanced-class-guide"
page = "186"

[fields]
kind = "spell"
school = "transmutation"
descriptors = ["sonic"]
levels = [
  { class = "Bard", level = 6 },
  { class = "Skald", level = 6 },
]
casting_time = "10 minutes"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "one unattended object or object in your possession" },
  { label = "Effect", value = "disruptive vibrations" },
]
duration = "1 round/level"
saving_throw = "Fortitude half (see text)"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 6: Bard, Skald
Casting time: 10 minutes
Components: V, S
Range: touch
Duration: 1 round/level
Saving throw: Fortitude half (see text)
Spell resistance: yes
Target: one unattended object or object in your possession
Effect: disruptive vibrations
Descriptors: sonic
:::

You cause the touched object to vibrate and release sonic energy once per round as a loud, dangerous
chime. The sound grows in strength as time passes. On your turn in the round after you cast the
spell, the chime deals 1d6 points of sonic damage to all creatures and objects within 5 feet of the
target. Each round after that, the damage increases by 1d6 and reaches 5 feet farther in all
directions. A successful Fortitude save halves the damage for that round only.
