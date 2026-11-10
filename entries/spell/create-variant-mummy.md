+++
id = "ref/spell/create-variant-mummy"
kind = "spell"
title = "Create Variant Mummy"
aon = "SpellDisplay.aspx?ItemName=Create%20Variant%20Mummy"
source_ids = ["pathfinder-81-shifting-sands"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "create_variant_mummy", path = "json/spells3.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/create-undead" },
]
[[sources]]
publication = "pathfinder-81-shifting-sands"
page = "73"

[fields]
kind = "spell"
school = "necromancy"
descriptors = ["evil"]
levels = [
  { class = "Arcanist", level = 7 },
  { class = "Cleric", level = 7 },
  { class = "Oracle", level = 7 },
  { class = "Sorcerer", level = 7 },
  { class = "Wizard", level = 7 },
]
casting_time = "1 hour"
components = "V, S, M (onyx gems worth 50 gp per HD of the undead to be created)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "1 corpse steeped in a peat bog for at least 24 hours" },
]
duration = "instantaneous"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 7: Arcanist, Cleric, Oracle, Sorcerer, Wizard
Casting time: 1 hour
Components: V, S, M (onyx gems worth 50 gp per HD of the undead to be created)
Range: close (25 ft. + 5 ft./2 levels)
Duration: instantaneous
Saving throw: none
Spell resistance: no
Target: 1 corpse steeped in a peat bog for at least 24 hours
Descriptors: evil
:::

This spell functions as [create undead](ref/spell/create-undead), except it creates one of the
following variant mummies: bog mummy, ice mummy, or Osirian tomb guardian.
