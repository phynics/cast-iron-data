+++
id = "ref/spell/duplicate-familiar"
kind = "spell"
title = "Duplicate Familiar"
source_ids = ["familiar-folio"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "duplicate_familiar", path = "json/spells13.json" },
]
[[sources]]
publication = "familiar-folio"
page = "22"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Creation"]
levels = [
  { class = "Alchemist", level = 4 },
  { class = "Arcanist", level = 5 },
  { class = "Investigator", level = 4 },
  { class = "Sorcerer", level = 5 },
  { class = "Witch", level = 5 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 standard action"
components = "V, S, M (alchemically preserved mockingfey feathers), F (familiar)"
range = "touch"
effects = [
  { label = "Effect", value = "temporary duplicate of familiar touched" },
]
duration = "10 minutes/level"
saving_throw = "Fortitude negates"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 4: Alchemist, Investigator\
5: Arcanist, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M (alchemically preserved mockingfey feathers), F (familiar)
Range: touch
Duration: 10 minutes/level
Saving throw: Fortitude negates
Spell resistance: no
Effect: temporary duplicate of familiar touched
Subschool: Creation
:::

You create a duplicate of a familiar. The familiar's master can use the duplicate as if it were his
familiar in all respects, though he doesn't gain the bonus special ability from more than one
familiar at a time. When the spell's duration expires, the familiar duplicate shrivels into nothing,
even if petrified or otherwise transformed.
