+++
id = "ref/spell/forced-mutation"
kind = "spell"
title = "Forced Mutation"
source_ids = ["people-of-the-wastes"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "forced_mutation", path = "json/spells13.json" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Cleric", level = 3 },
  { class = "Inquisitor", level = 3 },
  { class = "Magus", level = 3 },
  { class = "Occultist", level = 3 },
  { class = "Oracle", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Warpriest", level = 3 },
  { class = "Witch", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, M (a small piece of radioactive clay)"
range = "touch"
effects = [
  { label = "Target", value = "living creature touched" },
]
duration = "1 round/level"
saving_throw = "Fortitude negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 3: Arcanist, Cleric, Inquisitor, Magus, Occultist, Oracle, Sorcerer, Warpriest, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M (a small piece of radioactive clay)
Range: touch
Duration: 1 round/level
Saving throw: Fortitude negates
Spell resistance: yes
Target: living creature touched
:::

**Sources:** People of the Wastes pg 29

The body of the target creature twists and distorts, reshaping into a grotesque figure. Because of
the disfigurement, the creature takes a -4 penalty to Constitution and Charisma. The creature also
receives one of the following deformities (your choice) from the list in the mutant acquired
template: blind, deaf, fragile, fractured mind, lame, poor ability (applied to your choice of
Strength, Dexterity, Intelligence, or Wisdom), spasms, and useless arm. The deformity is subject to
all limitations described in the mutant template (for example, this spell cannot impose the lame
deformity on a creature with a base speed slower than 20 feet).
