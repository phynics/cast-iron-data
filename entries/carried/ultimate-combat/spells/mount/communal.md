+++
id = "ref/carried/ultimate-combat/spells/mount/communal"
kind = "spell"
title = "Mount, Communal"
source_ids = ["ultimate-combat"]
section = ["Spells", "Mount"]
tags = ["conjuration", "summoning"]
provenance = [
  { dataset = "psrd-data", record = "pfsrd://Ultimate Combat/Spells/Mount/Communal", path = "ultimate_combat/spell/mount_communal.json" },
]

[fields]
kind = "spell"
school = "conjuration"
subschools = ["summoning"]
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Magus", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Summoner", level = 2 },
  { class = "Witch", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 round"
components = "V, S, M (a bit of horse hair)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Effect", value = "up to six mounts" },
]
duration = "2 hours/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
School: conjuration (summoning)
Level: 2: Arcanist, Magus, Sorcerer, Summoner, Witch, Wizard
Casting Time: 1 round
Components: V, S, M (a bit of horse hair)
Range: close (25 ft. + 5 ft./2 levels)
Effect: up to six mounts
Duration: 2 hours/level (D)
Saving Throw: none
Spell Resistance: no
:::

_As mount, but you may divide the duration among creatures touched._

This spell functions like _[mount](ref/spell/mount)_, except you can summon up to six light horses
or ponies, and you divide the duration in 2-hour increments among the steeds summoned.
