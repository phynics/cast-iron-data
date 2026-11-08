+++
id = "ref/spell/hex-ward"
kind = "spell"
title = "Hex Ward"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "hex_ward", path = "json/spells5.json" },
]

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Inquisitor", level = 1 },
  { class = "Occultist", level = 1 },
  { class = "Shaman", level = 1 },
  { class = "Witch", level = 1 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "1 hour/level"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 1: Inquisitor, Occultist, Shaman, Witch
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: 1 hour/level
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
Target: creature touched
:::

**Sources:** Ultimate Magic pg 223

You give the target a +4 resistance bonus on saving throws against witch hexes.
