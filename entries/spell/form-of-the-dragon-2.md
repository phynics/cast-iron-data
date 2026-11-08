+++
id = "ref/spell/form-of-the-dragon-2"
kind = "spell"
title = "Form of the Dragon II"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "form_of_the_dragon_2", path = "json/spells13.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/form-of-the-dragon-1" },
]

[fields]
kind = "spell"
school = "transmutation"
subschools = ["Polymorph"]
levels = [
  { class = "Alchemist", level = 6 },
  { class = "Arcanist", level = 6 },
  { class = "Investigator", level = 6 },
  { class = "Magus", level = 6 },
  { class = "Sorcerer", level = 6 },
  { class = "Wizard", level = 6 },
]
casting_time = "1 standard action"
components = "V, S, M (a scale of the dragon type you plan to assume)"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 minute/level (D)"
saving_throw = "see below"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 6: Alchemist, Arcanist, Investigator, Magus, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M (a scale of the dragon type you plan to assume)
Range: personal
Duration: 1 minute/level (D)
Saving throw: see below
Spell resistance: no
Target: you
Subschool: Polymorph
:::

### Form of the Dragon II

**Sources:** PRPG Core Rulebook pg 286

This spell functions as [form of the dragon I](ref/spell/form-of-the-dragon-1) except that it also
allows you to assume the form of a Large chromatic or metallic dragon. You gain the following
abilities: a +6 size bonus to Strength, a +4 size bonus to Constitution, a +6 natural armor bonus,
fly 90 feet (poor), [darkvision](ref/rule/darkvision) 60 feet, a breath weapon, DR 5/magic, and
resistance to one element. You also gain one bite (2d6), two claws (1d8), two wing attacks (1d6),
and one tail slap attack (1d8). You can only use the breath weapon twice per casting of this spell,
and you must wait 1d4 rounds between uses. All breath weapons deal 8d8 points of damage and allow a
Reflex save for half damage. Line breath weapons increase to 80-foot lines and cones increase to
40-foot cones.
