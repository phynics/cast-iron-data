+++
id = "ref/spell/object-possession-greater"
kind = "spell"
title = "Greater Object Possession"
aon = "SpellDisplay.aspx?ItemName=Object%20Possession%2C%20Greater"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "object_possession_greater", path = "json/spells7.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/object-possession" },
]
[[sources]]
publication = "occult-adventures"
page = "179"

[fields]
kind = "spell"
school = "necromancy"
levels = [
  { class = "Arcanist", level = 7 },
  { class = "Occultist", level = 5 },
  { class = "Psychic", level = 6 },
  { class = "Sorcerer", level = 7 },
  { class = "Spiritualist", level = 6 },
  { class = "Witch", level = 7 },
  { class = "Wizard", level = 7 },
]
casting_time = "1 standard action"
components = "V, S"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Target", value = "unattended Gargantuan or smaller object (minimum Tiny) or construct" },
]
duration = "10 minutes/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 5: Occultist\
6: Psychic, Spiritualist\
7: Arcanist, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: medium (100 ft. + 10 ft./level)
Target: unattended Gargantuan or smaller object (minimum Tiny) or construct
Duration: 10 minutes/level (D)
Saving throw: none
Spell resistance: no
:::

### Greater Object Possession

This spell functions as [object possession](ref/spell/object-possession), except as noted above. The
possessed animated object has a number of Construction Points appropriate for its size (up to 5 CP
for Gargantuan objects). Your silver cord extends to medium range (100 ft. + 10 ft./level).

You can attempt to possess a construct instead of an unattended object as your first possession with
this spell. If you do, this spell acts as control construct, except as noted above.
