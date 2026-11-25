+++
id = "ref/spell/familiar-double"
kind = "spell"
title = "Familiar Double"
aon = "SpellDisplay.aspx?ItemName=Familiar%20Double"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "familiar_double", path = "json/spells15.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/project-image" },
]
[[sources]]
publication = "advanced-class-guide"
page = "181"

[fields]
kind = "spell"
school = "illusion"
subschools = ["shadow"]
levels = [
  { class = "Witch", level = 7 },
]
casting_time = "1 standard action"
components = "V, S, M (a small replica of you worth 5 gp)"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Effect", value = "one shadow duplicate" },
]
duration = "1 round/level (D)"
saving_throw = "Will disbelief (if interacted with)"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 7: Witch
Casting time: 1 standard action
Components: V, S, M (a small replica of you worth 5 gp)
Range: medium (100 ft. + 10 ft./level)
Duration: 1 round/level (D)
Saving throw: Will disbelief (if interacted with)
Spell resistance: no
Effect: one shadow duplicate
Subschool: shadow
:::

### Familiar Double

This spell functions as [project image](ref/spell/project-image), except the image appears in your
familiar's square and moves when your familiar moves.
