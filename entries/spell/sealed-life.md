+++
id = "ref/spell/sealed-life"
kind = "spell"
title = "Sealed Life"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "sealed_life", path = "json/spells15.json" },
]
[[sources]]
publication = "occult-adventures"
page = "185"

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Medium", level = 2 },
  { class = "Spiritualist", level = 3 },
]
casting_time = "1 standard action"
components = "S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "1 round/level"
saving_throw = "none"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 2: Medium\
3: Spiritualist
Casting time: 1 standard action
Components: S
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level
Saving throw: none
Spell resistance: yes
Target: one creature
:::

You seal the life force within the target, preventing it from sharing its vitality with others.
Affected creatures can't transfer damage to or from another, such as through
[shield other](ref/spell/shield-other), a spiritualist's life bond, or a summoner's life link.
Effects such as vampiric touch that steal vitality from others deal damage normally, but provide no
benefits.
