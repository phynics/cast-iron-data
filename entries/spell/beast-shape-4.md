+++
id = "ref/spell/beast-shape-4"
kind = "spell"
title = "Beast Shape IV"
source_ids = ["core-rulebook", "ultimate-wilderness", "animal-archive"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "beast_shape_4", path = "json/spells12.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/beast-shape-3" },
]
[[sources]]
publication = "core-rulebook"
page = "247"

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

### Beast Shape IV

This spell functions as [beast shape III](ref/spell/beast-shape-3) except that it also allows you to
assume the form of a Tiny or Large creature of the magical beast type. If the form you assume has
any of the following abilities, you gain the listed ability: burrow 60 feet, climb 90 feet, fly 120
feet (good maneuverability), swim 120 feet, [blindsense](ref/rule/blindsight-and-blindsense) 60
feet, [darkvision](ref/rule/darkvision) 90 feet, [low-light vision](ref/rule/low-light-vision),
scent, [tremorsense](ref/umr/tremorsense) 60 feet, breath weapon, constrict, ferocity, grab, jet,
poison, pounce, rake, rend, roar, spikes, trample, trip, and web. If the creature has immunity or
resistance to any elements, you gain resistance 20 to those elements. If the creature has
vulnerability to an element, you gain that vulnerability.

_Tiny magical beast:_ If the form you take is that of a Tiny magical beast, you gain a -2 penalty to
your Strength, a +8 size bonus to your Dexterity, and a +3 natural armor bonus.

_Large magical beast:_ If the form you take is that of a Large magical beast, you gain a +6 size
bonus to your Strength, a -2 penalty on your Dexterity, a +2 size bonus to your Constitution, and a
+6 natural armor bonus.
