+++
id = "ref/spell/giant-form-1"
kind = "spell"
title = "Giant Form I"
aon = "SpellDisplay.aspx?ItemName=Giant%20Form%20I"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "giant_form_1", path = "json/spells13.json" },
]
[[sources]]
publication = "core-rulebook"
page = "289"

[fields]
kind = "spell"
school = "transmutation"
subschools = ["Polymorph"]
levels = [
  { class = "Alchemist", level = 6 },
  { class = "Arcanist", level = 7 },
  { class = "Investigator", level = 6 },
  { class = "Sorcerer", level = 7 },
  { class = "Wizard", level = 7 },
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
Level: 6: Alchemist, Investigator\
7: Arcanist, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M (a piece of the creature whose form you plan to assume)
Range: personal
Duration: 1 minute/level (D)
Saving throw: none
Spell resistance: no
Target: you
Subschool: Polymorph
:::

When you cast this spell you can assume the form of any Large humanoid creature of the giant
subtype. Once you assume your new form, you gain the following abilities: a +6 size bonus to
Strength, a -2 penalty to Dexterity, a +4 size bonus to Constitution, a +4 natural armor bonus, and
[low-light vision](ref/rule/low-light-vision). If the form you assume has any of the following
abilities, you gain the listed ability: [darkvision](ref/rule/darkvision) 60 feet, rend (2d6
damage), regeneration 5, rock catching, and rock throwing (range 60 feet, 2d6 damage). If the
creature has immunity or resistance to any elements, you gain resistance 20 to those elements. If
the creature has vulnerability to an element, you gain that vulnerability.
