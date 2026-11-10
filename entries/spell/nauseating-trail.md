+++
id = "ref/spell/nauseating-trail"
kind = "spell"
title = "Nauseating Trail"
aon = "SpellDisplay.aspx?ItemName=Nauseating%20Trail"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "nauseating_trail", path = "json/spells7.json" },
]
[[sources]]
publication = "advanced-class-guide"
page = "189"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Creation"]
descriptors = ["poison"]
levels = [
  { class = "Alchemist", level = 3 },
  { class = "Arcanist", level = 3 },
  { class = "Druid", level = 3 },
  { class = "Investigator", level = 3 },
  { class = "Magus", level = 3 },
  { class = "Shaman", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Witch", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, M (a rotten egg or cabbage leaves)"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Target", value = "one willing creature" },
]
duration = "1 round/level"
saving_throw = "none and Fortitude negates (see text)"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 3: Alchemist, Arcanist, Druid, Investigator, Magus, Shaman, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M (a rotten egg or cabbage leaves)
Range: medium (100 ft. + 10 ft./level)
Duration: 1 round/level
Saving throw: none and Fortitude negates (see text)
Spell resistance: no
Target: one willing creature
Subschool: Creation
Descriptors: poison
:::

The target exudes stinking vapors that fill its space. The vapors do not obscure sight, but it
nauseates creatures as stinking cloud. The target is immune to these vapors. These vapors persist as
the creature moves, filling every square it passes through until it has filled a number of squares
equal to 4 × your caster level - if you move through more squares than that, the squares over that
amount at not filled with the vapors. Each creature that enters or ends its turn in the area filled
with these vapors must succeed at a Fortitude save or become nauseated as long as it remains in the
square and for 1d4+1 rounds after it leaves.
