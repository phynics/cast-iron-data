+++
id = "ref/spell/beast-shape-3"
kind = "spell"
title = "Beast Shape III"
aon = "SpellDisplay.aspx?ItemName=Beast%20Shape%20III"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "beast_shape_3", path = "json/spells12.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/beast-shape-2" },
]
[[sources]]
publication = "core-rulebook"
page = "247"

[fields]
kind = "spell"
school = "transmutation"
subschools = ["polymorph"]
levels = [
  { class = "Alchemist", level = 5 },
  { class = "Arcanist", level = 5 },
  { class = "Investigator", level = 5 },
  { class = "Magus", level = 5 },
  { class = "Red Mantis Assassin", level = 5 },
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
Level: 5: Alchemist, Arcanist, Investigator, Magus, Red Mantis Assassin, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M (a piece of the creature whose form you plan to assume)
Range: personal
Duration: 1 minute/level (D)
Saving throw: none
Spell resistance: no
Target: you
Subschool: polymorph
:::

### Beast Shape III

This spell functions as [beast shape II](ref/spell/beast-shape-2), except that it also allows you to
assume the form of a Diminutive or Huge creature of the animal type. This spell also allows you to
take on the form of a Small or Medium creature of the magical beast type. If the form you assume has
any of the following abilities, you gain the listed ability: burrow 30 feet, climb 90 feet, fly 90
feet (good maneuverability), swim 90 feet, [blindsense](ref/rule/blindsight-and-blindsense) 30 feet,
[darkvision](ref/rule/darkvision) 60 feet, [low-light vision](ref/rule/low-light-vision), scent,
constrict, ferocity, grab, jet, poison, pounce, rake, trample, trip, and web.

_Diminutive animal:_ If the form you take is that of a Diminutive animal, you gain a +6 size bonus
to your Dexterity, a -4 penalty to your Strength, and a +1 natural armor bonus.

_Huge animal:_ If the form you take is that of a Huge animal, you gain a +6 size bonus to your
Strength, a -4 penalty to your Dexterity, and a +6 natural armor bonus.

_Small magical beast:_ If the form you take is that of a Small magical beast, you gain a +4 size
bonus to your Dexterity, and a +2 natural armor bonus.

_Medium magical beast:_ If the form you take is that of a Medium magical beast, you gain a +4 size
bonus to your Strength, and a +4 natural armor bonus.
