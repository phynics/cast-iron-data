+++
id = "ref/spell/bless-water"
kind = "spell"
title = "Bless Water"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "bless_water", path = "json/spells12.json" },
]
[[sources]]
publication = "core-rulebook"
page = "249"

[fields]
kind = "spell"
school = "transmutation"
descriptors = ["good"]
levels = [
  { class = "Cleric", level = 1 },
  { class = "Inquisitor", level = 1 },
  { class = "Oracle", level = 1 },
  { class = "Paladin", level = 1 },
  { class = "Warpriest", level = 1 },
]
casting_time = "1 minute"
components = "V, S, M (5 pounds of powdered silver worth 25 gp)"
range = "touch"
effects = [
  { label = "Target", value = "flask of water touched" },
]
duration = "instantaneous"
saving_throw = "Will negates (object)"
spell_resistance = "yes (object)"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 1: Cleric, Inquisitor, Oracle, Paladin, Warpriest
Casting time: 1 minute
Components: V, S, M (5 pounds of powdered silver worth 25 gp)
Range: touch
Duration: instantaneous
Saving throw: Will negates (object)
Spell resistance: yes (object)
Target: flask of water touched
Descriptors: good
:::

This transmutation imbues a flask (1 pint) of water with positive energy, turning it into holy
water.
