+++
id = "ref/spell/fungal-infestation"
kind = "spell"
title = "Fungal Infestation"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "fungal_infestation", path = "json/spells13.json" },
]

[fields]
kind = "spell"
school = "necromancy"
descriptors = ["disease"]
levels = [
  { class = "Druid", level = 3 },
  { class = "Hunter", level = 3 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "1d3 days"
saving_throw = "Fortitude negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 3: Druid, Hunter
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: 1d3 days
Saving throw: Fortitude negates
Spell resistance: yes
Target: creature touched
Descriptors: disease
:::

**Sources:** Ultimate Magic pg 221

You coat the target in necrotic fungus that makes its flesh soft and fragile. Toadstools, ringworm,
and other disgusting fungal growths sprout from its skin. The target takes 1d3 points of Charisma
damage. Any physical attack against the target automatically adds 1d6 points of bleed damage.
