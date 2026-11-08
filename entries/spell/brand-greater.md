+++
id = "ref/spell/brand-greater"
kind = "spell"
title = "Greater Brand"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "brand_greater", path = "json/spells2.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/brand" },
]

[fields]
kind = "spell"
school = "transmutation"
descriptors = ["curse"]
levels = [
  { class = "Inquisitor", level = 4 },
]
casting_time = "1 round"
components = "V, S, DF"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "permanent"
saving_throw = "Fortitude negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 4: Inquisitor
Casting time: 1 round
Components: V, S, DF
Range: touch
Target: creature touched
Duration: permanent
Saving throw: Fortitude negates
Spell resistance: yes
Descriptors: curse
:::

### Greater Brand

**Sources:** Advanced Player's Guide pg 207

This spell functions like [brand](ref/spell/brand), except that it inflicts 1d6 points of damage
when applied and cannot be removed, even temporarily. In addition, a greater brand blazes as bright
as a torch when brought within 30 feet of a visible symbol of your faith. While the symbol is
blazing, the recipient is sickened. Like the effects of bestow curse, a greater brand cannot be
dispelled, but it can be removed by any means that removes a
[mark of justice](ref/spell/mark-of-justice).
