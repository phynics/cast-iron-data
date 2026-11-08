+++
id = "ref/spell/animal-shapes"
kind = "spell"
title = "Animal Shapes"
source_ids = ["core-rulebook", "ultimate-wilderness", "animal-archive"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "animal_shapes", path = "json/spells12.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/beast-shape-3" },
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

### Animal Shapes

**Sources:** PRPG Core Rulebook pg 241

As [beast shape III](ref/spell/beast-shape-3), except you change the form of up to one willing
creature per caster level into an animal of your choice; the spell has no effect on unwilling
creatures. All creatures must take the same kind of animal form. Recipients remain in the animal
form until the spell expires or until you dismiss it for all recipients. In addition, an individual
subject may choose to resume its normal form as a full-round action; doing so ends the spell for
that subject alone.
