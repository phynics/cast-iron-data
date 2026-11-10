+++
id = "ref/spell/naga-shape-2"
kind = "spell"
title = "Naga Shape II"
aon = "SpellDisplay.aspx?ItemName=Naga%20Shape%20II"
source_ids = ["blood-of-the-beast"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "naga_shape_2", path = "json/spells7.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/naga-shape-1" },
]
[[sources]]
publication = "blood-of-the-beast"
page = "19"

[fields]
kind = "spell"
school = "transmutation"
subschools = ["Polymorph"]
levels = [
  { class = "Alchemist", level = 4 },
  { class = "Arcanist", level = 4 },
  { class = "Bloodrager", level = 4 },
  { class = "Investigator", level = 4 },
  { class = "Magus", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S, M (a piece of the creature whose form you want to assume)"
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
Level: 4: Alchemist, Arcanist, Bloodrager, Investigator, Magus, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M (a piece of the creature whose form you want to assume)
Range: personal
Duration: 1 minute/level (D)
Saving throw: none
Spell resistance: no
Target: you
Subschool: Polymorph
:::

### Naga Shape II

This spell functions as [naga shape I](ref/spell/naga-shape-1). Additionally, if the form you assume
has any of the following abilities, you gain the listed ability: burrow 30 feet, climb 90 feet, fly
90 feet (good maneuverability), swim 90 feet, [blindsense](ref/rule/blindsight-and-blindsense) 30
feet, [darkvision](ref/rule/darkvision) 60 feet, [low-light vision](ref/rule/low-light-vision),
compression, constrict, detect thoughts, dreamsight, grab, hypnosis, poison, sneak attack +2d6, and
spit.
