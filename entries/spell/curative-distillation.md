+++
id = "ref/spell/curative-distillation"
kind = "spell"
title = "Curative Distillation"
aon = "SpellDisplay.aspx?ItemName=Curative%20Distillation"
source_ids = ["healers-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "curative_distillation", path = "json/spells3.json" },
]
[[sources]]
publication = "healers-handbook"
page = "8"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Healing"]
levels = [
  { class = "Alchemist", level = 2 },
  { class = "Cleric", level = 3 },
  { class = "Investigator", level = 2 },
  { class = "Oracle", level = 3 },
  { class = "Warpriest", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, M (healing herb, alchemical remady, or potion of a healing spell worth at least 50 gp)"
range = "touch"
effects = [
  { label = "Target", value = "one living creature touched" },
]
duration = "instantaneous"
saving_throw = "Will half (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 2: Alchemist, Investigator\
3: Cleric, Oracle, Warpriest
Casting time: 1 standard action
Components: V, S, M (healing herb, alchemical remady, or potion of a healing spell worth at least 50 gp)
Range: touch
Duration: instantaneous
Saving throw: Will half (harmless)
Spell resistance: yes (harmless)
Target: one living creature touched
Subschool: Healing
:::

You concentrate the healing potential of the material component so that it's exceptionally potent
and restorative. This spell restores a number of hit points equal to 1d8 + 1 point per caster level
(maximum +10) to the target, and also grants the target the benefits of the material component. Roll
the hit points restored separately when determining how many total hit points this spell and the
material component restore.
