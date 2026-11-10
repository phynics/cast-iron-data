+++
id = "ref/spell/plant-shape-1"
kind = "spell"
title = "Plant Shape I"
aon = "SpellDisplay.aspx?ItemName=Plant%20Shape%20I"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "plant_shape_1", path = "json/spells7.json" },
]
[[sources]]
publication = "core-rulebook"
page = "322"

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

When you cast this spell you can assume the form of any Small or Medium creature of the plant type.
If the form you assume has any of the following abilities, you gain the listed ability:
[darkvision](ref/rule/darkvision) 60 feet, [low-light vision](ref/rule/low-light-vision), constrict,
grab, and poison. If the form you assume does not possess the ability to move, your speed is reduced
to 5 feet and you lose all other forms of movement. If the creature has vulnerability to an element,
you gain that vulnerability.

_Small plant:_ If the form you take is that of a Small plant, you gain a +2 size bonus to your
Constitution and a +2 natural armor bonus.

_Medium plant:_ If the form you take is that of a Medium plant, you gain a +2 size bonus to your
Strength, a +2 enhancement bonus to your Constitution, and a +2 natural armor bonus.
