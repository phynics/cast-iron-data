+++
id = "ref/carried/core-rulebook/spells/heal/mass"
kind = "spell"
title = "Heal, Mass"
source_ids = ["core-rulebook"]
section = ["Spells", "Heal"]
tags = ["conjuration", "healing"]
provenance = [
  { dataset = "psrd-data", record = "pfsrd://Core Rulebook/Spells/Heal/Mass", path = "core_rulebook/spell/heal_mass.json" },
]

[fields]
kind = "spell"
school = "conjuration"
subschools = ["healing"]
levels = [
  { class = "Cleric", level = 9 },
  { class = "Oracle", level = 9 },
  { class = "Shaman", level = 9 },
  { class = "Warpriest", level = 9 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Targets", value = "one or more creatures, no two of which can be more than 30 ft. apart" },
]
duration = "instantaneous"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
School: conjuration (healing)
Level: 9: Cleric, Oracle, Shaman, Warpriest
Casting Time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Targets: one or more creatures, no two of which can be more than 30 ft. apart
Duration: instantaneous
Saving Throw: Will negates (harmless)
Spell Resistance: yes (harmless)
:::

_As heal, but affects 1 subject/level._

This spell functions like _[heal](ref/spell/heal)_, except as noted above. The maximum number of hit
points restored to each creature is 250.
