+++
id = "ref/spell/stone-throwing"
kind = "spell"
title = "Stone Throwing"
aon = "SpellDisplay.aspx?ItemName=Stone%20Throwing"
source_ids = ["giant-hunters-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "stone_throwing", path = "json/spells9.json" },
]
[[sources]]
publication = "giant-hunters-handbook"
page = "27"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Bloodrager", level = 1 },
  { class = "Cleric", level = 2 },
  { class = "Druid", level = 2 },
  { class = "Hunter", level = 1 },
  { class = "Magus", level = 2 },
  { class = "Oracle", level = 2 },
  { class = "Ranger", level = 1 },
  { class = "Sorcerer", level = 2 },
  { class = "Warpriest", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, M (powdered stone)"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "1 minute/level"
saving_throw = "Fortitude negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 1: Bloodrager, Hunter, Ranger\
2: Arcanist, Cleric, Druid, Magus, Oracle, Sorcerer, Warpriest, Wizard
Casting time: 1 standard action
Components: V, S, M (powdered stone)
Range: touch
Duration: 1 minute/level
Saving throw: Fortitude negates (harmless)
Spell resistance: yes (harmless)
Target: creature touched
:::

The subject gains the rock throwing and rock catching abilities. It can use these abilities with any
solid, mostly inflexible object with a [hardness](ref/umr/hardness) of at least 5.

The subject can hurl rocks up to two categories smaller than its own size. The range increment for
this attack is 20 feet, and rocks can be hurled a maximum of 5 range increments. Damage is based on
the size of the subject-1d8 points of damage for a Large creature, 1d6 for a Medium creature, or 1d4
for a Small creature-plus 1-1/2 times the thrower's Strength bonus.

For every size category smaller than Large the subject is, it receives a cumulative -5 penalty on
Reflex saves to catch rocks (or similar projectiles) thrown at it.
