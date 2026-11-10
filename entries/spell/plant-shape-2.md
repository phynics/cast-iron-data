+++
id = "ref/spell/plant-shape-2"
kind = "spell"
title = "Plant Shape II"
aon = "SpellDisplay.aspx?ItemName=Plant%20Shape%20II"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "plant_shape_2", path = "json/spells7.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/plant-shape-1" },
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

### Plant Shape II

This spell functions as [plant shape I](ref/spell/plant-shape-1) except that it also allows you to
assume the form of a Large creature of the plant type. If the creature has immunity or resistance to
any elements, you gain resistance 20 to those elements. If the creature has vulnerability to an
element, you gain that vulnerability.

_Large plant:_ If the form you take is that of a Large plant, you gain a +4 size bonus to your
Strength, a +2 size bonus to your Constitution, and a +4 natural armor bonus.
