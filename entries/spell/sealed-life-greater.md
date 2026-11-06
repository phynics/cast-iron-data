+++
id = "ref/spell/sealed-life-greater"
kind = "spell"
title = "Greater Sealed Life"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "sealed_life_greater", path = "json/spells15.json" },
]

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Spiritualist", level = 6 },
]
casting_time = "1 standard action"
components = "S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "1 minute/level"
saving_throw = "none"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 6: Spiritualist
Casting time: 1 standard action
Components: S
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 minute/level
Saving throw: none
Spell resistance: yes
Target: one creature
:::

**Sources:** Occult Adventures pg 185

This spell functions as [sealed life](ref/spell/sealed-life), except it additionally provides the
benefits of death ward and renders its targets immune to effects that extract or transfer its soul,
such as possession and trap the soul. This spell prevents a soul from returning to its body if it
has already departed, until the spell's duration expires.
