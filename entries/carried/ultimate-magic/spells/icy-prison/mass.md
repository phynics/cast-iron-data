+++
id = "ref/carried/ultimate-magic/spells/icy-prison/mass"
kind = "spell"
title = "Icy Prison, Mass"
source_ids = ["ultimate-magic"]
section = ["Spells", "Icy Prison"]
tags = ["evocation", "cold"]
provenance = [
  { dataset = "psrd-data", record = "pfsrd://Ultimate Magic/Spells/Icy Prison/Mass", path = "ultimate_magic/spell/icy_prison_mass.json" },
]

[fields]
kind = "spell"
school = "evocation"
descriptors = ["cold"]
levels = [
  { class = "Arcanist", level = 9 },
  { class = "Sorcerer", level = 9 },
  { class = "Wizard", level = 9 },
]
casting_time = "1 standard action"
components = "V, S"
range = "medium (10 ft. + 10 ft./level)"
effects = [
  { label = "Target", value = "one creature/level, no two of which can be more than 30 ft. apart." },
]
duration = "1 minute/level; see text"
saving_throw = "Reflex partial"
spell_resistance = "yes"
+++

::: statblock
School: evocation \[cold\]
Level: 9: Arcanist, Sorcerer, Wizard
Casting Time: 1 standard action
Components: V, S
Range: medium (10 ft. + 10 ft./level)
Target: one creature/level, no two of which can be more than 30 ft. apart.
Duration: 1 minute/level; see text
Saving Throw: Reflex partial
Spell Resistance: yes
:::

_As icy prison, but it affects 1 creature/level._

This spell functions as _[icy prison](ref/spell/icy-prison)_, except as noted above.
