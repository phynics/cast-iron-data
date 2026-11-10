+++
id = "ref/spell/polymorph-familiar"
kind = "spell"
title = "Polymorph Familiar"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "polymorph_familiar", path = "json/spells7.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/beast-shape-1" },
]
[[sources]]
publication = "advanced-class-guide"
page = "190"

[fields]
kind = "spell"
school = "transmutation"
subschools = ["Polymorph"]
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Red Mantis Assassin", level = 3 },
  { class = "Shaman", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Witch", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "your familiar" },
]
duration = "1 minute/level (D)"
saving_throw = "none"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 3: Arcanist, Red Mantis Assassin, Shaman, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 minute/level (D)
Saving throw: none
Spell resistance: yes
Target: your familiar
Subschool: Polymorph
:::

This spell functions as [beast shape I](ref/spell/beast-shape-1), except it grants your familiar the
form of any Small animal. Your familiar retains all of its special abilities and continues to grant
you the special ability associated with its normal shape (such as a bat familiar's bonus on Fly
checks).

At caster level 7th, this spell functions as beast shape II. At caster level 9th, it functions as
beast shape III. At caster level 11th, it functions as beast shape IV.
