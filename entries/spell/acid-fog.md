+++
id = "ref/spell/acid-fog"
kind = "spell"
title = "Acid Fog"
aon = "SpellDisplay.aspx?ItemName=Acid%20Fog"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "acid_fog", path = "json/spells.json" },
]
[[sources]]
publication = "core-rulebook"
page = "239"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Creation"]
descriptors = ["acid"]
levels = [
  { class = "Arcanist", level = 6 },
  { class = "Magus", level = 6 },
  { class = "Sorcerer", level = 6 },
  { class = "Unchained Summoner", level = 6 },
  { class = "Wizard", level = 6 },
]
casting_time = "1 standard action"
components = "V, S, M (powdered peas and an animal hoof)"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Effect", value = "fog spreads in 20-ft. radius, 20 ft. high" },
]
duration = "1 round/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 6: Arcanist, Magus, Sorcerer, Unchained Summoner, Wizard
Casting time: 1 standard action
Components: V, S, M (powdered peas and an animal hoof)
Range: medium (100 ft. + 10 ft./level)
Duration: 1 round/level
Saving throw: none
Spell resistance: no
Effect: fog spreads in 20-ft. radius, 20 ft. high
Subschool: Creation
Descriptors: acid
:::

Acid fog creates a billowing mass of misty vapors like the solid fog spell. In addition to slowing
down creatures and obscuring sight, this spell's vapors are highly acidic. Each round on your turn,
starting when you cast the spell, the fog deals 2d6 points of acid damage to each creature and
object within it.
