+++
id = "ref/spell/paranoia"
kind = "spell"
title = "Paranoia"
aon = "SpellDisplay.aspx?ItemName=Paranoia"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "paranoia", path = "json/spells7.json" },
]
[[sources]]
publication = "occult-adventures"
page = "179"

[fields]
kind = "spell"
school = "illusion"
subschools = ["Phantasm"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Bard", level = 2 },
  { class = "Medium", level = 1 },
  { class = "Mesmerist", level = 1 },
  { class = "Psychic", level = 2 },
  { class = "Skald", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Witch", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "1 round/level (D)"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 1: Medium, Mesmerist\
2: Arcanist, Bard, Psychic, Skald, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level (D)
Saving throw: Will negates
Spell resistance: yes
Target: one creature
Subschool: Phantasm
Descriptors: mind-affecting
:::

The target believes everyone it sees is an enemy. The target becomes hostile to all creatures,
treating all creatures as enemies and only itself as an ally. The target must attempt attacks of
opportunity whenever any creature provokes them. Finally, whenever the target is adjacent to two or
more creatures, its paranoia overwhelms it, and it takes a -2 penalty on attack rolls, weapon damage
rolls, ability checks, skill checks, and saving throws.
