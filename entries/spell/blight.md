+++
id = "ref/spell/blight"
kind = "spell"
title = "Blight"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "blight", path = "json/spells2.json" },
]
[[sources]]
publication = "core-rulebook"
page = "250"

[fields]
kind = "spell"
school = "necromancy"
levels = [
  { class = "Arcanist", level = 5 },
  { class = "Druid", level = 4 },
  { class = "Hunter", level = 4 },
  { class = "Shaman", level = 5 },
  { class = "Sorcerer", level = 5 },
  { class = "Witch", level = 5 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "touch"
effects = [
  { label = "Target", value = "plant touched" },
]
duration = "instantaneous"
saving_throw = "Fortitude half; see text"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 4: Druid, Hunter\
5: Arcanist, Shaman, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S, DF
Range: touch
Duration: instantaneous
Saving throw: Fortitude half; see text
Spell resistance: yes
Target: plant touched
:::

This spell withers a single plant of any size. An affected plant creature takes 1d6 points of damage
per level (maximum 15d6) and may attempt a Fortitude saving throw for half damage. A plant that
isn't a creature doesn't receive a save and immediately withers and dies.

This spell has no effect on the soil or surrounding plant life.
