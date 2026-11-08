+++
id = "ref/spell/beast-shape-2"
kind = "spell"
title = "Beast Shape II"
source_ids = ["core-rulebook", "ultimate-wilderness", "animal-archive"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "beast_shape_2", path = "json/spells12.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/beast-shape-1" },
]

[fields]
kind = "spell"
school = "transmutation"
subschools = ["Polymorph"]
levels = [
  { class = "Alchemist", level = 3 },
  { class = "Arcanist", level = 3 },
  { class = "Bloodrager", level = 3 },
  { class = "Investigator", level = 3 },
  { class = "Magus", level = 3 },
  { class = "Red Mantis Assassin", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Wizard", level = 3 },
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
Level: 3: Alchemist, Arcanist, Bloodrager, Investigator, Magus, Red Mantis Assassin, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M (a piece of the creature whose form you plan to assume)
Range: personal
Duration: 1 minute/level (D)
Saving throw: none
Spell resistance: no
Target: you
Subschool: Polymorph
:::

### Beast Shape II

**Sources:** PRPG Core Rulebook pg 247

This spell functions as [beast shape I](ref/spell/beast-shape-1), except that it also allows you to
assume the form of a Tiny or Large creature of the animal type. If the form you assume has any of
the following abilities, you gain the listed ability: climb 60 feet, fly 60 feet (good
maneuverability), swim 60 feet, [darkvision](ref/rule/darkvision) 60 feet,
[low-light vision](ref/rule/low-light-vision), scent, grab, pounce, and trip.

_Tiny animal:_ If the form you take is that of a Tiny animal, you gain a +4 size bonus to your
Dexterity, a -2 penalty to your Strength, and a +1 natural armor bonus.

_Large animal:_ If the form you take is that of a Large animal, you gain a +4 size bonus to your
Strength, a -2 penalty to your Dexterity, and a +4 natural armor bonus.
