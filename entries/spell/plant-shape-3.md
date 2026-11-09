+++
id = "ref/spell/plant-shape-3"
kind = "spell"
title = "Plant Shape III"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "plant_shape_3", path = "json/spells7.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/plant-shape-2" },
]
[[sources]]
publication = "core-rulebook"
page = "323"

[fields]
kind = "spell"
school = "transmutation"
subschools = ["Polymorph"]
levels = [
  { class = "Alchemist", level = 5 },
  { class = "Arcanist", level = 5 },
  { class = "Investigator", level = 5 },
  { class = "Sorcerer", level = 5 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 standard action"
components = "V, S, M (a piece of the creature whose form you plan to assume)"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 minute/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 5: Alchemist, Arcanist, Investigator, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M (a piece of the creature whose form you plan to assume)
Range: personal
Duration: 1 minute/level (D)
Saving throw: none
Spell resistance: no
Target: you
Subschool: Polymorph
:::

### Plant Shape III

This spell functions as [plant shape II](ref/spell/plant-shape-2) except that it also allows you to
assume the form of a Huge creature of the plant type. If the form you assume has any of the
following abilities, you gain the listed ability: DR, regeneration 5, and trample.

_Huge plant:_ If the form you take is that of a Huge plant, you gain a +8 size bonus to your
Strength, a -2 penalty to your Dexterity, a +4 size bonus to your Constitution, and a +6 natural
armor bonus.
