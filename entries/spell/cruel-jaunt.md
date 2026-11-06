+++
id = "ref/spell/cruel-jaunt"
kind = "spell"
title = "Cruel Jaunt"
source_ids = ["horror-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "cruel_jaunt", path = "json/spells3.json" },
]

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Teleportation"]
descriptors = ["evil", "fear", "mind-affecting"]
levels = [
  { class = "Antipaladin", level = 4 },
  { class = "Arcanist", level = 6 },
  { class = "Cleric", level = 6 },
  { class = "Inquisitor", level = 6 },
  { class = "Magus", level = 6 },
  { class = "Oracle", level = 6 },
  { class = "Psychic", level = 6 },
  { class = "Shaman", level = 6 },
  { class = "Sorcerer", level = 6 },
  { class = "Warpriest", level = 6 },
  { class = "Witch", level = 6 },
  { class = "Wizard", level = 6 },
]
casting_time = "1 standard action"
components = "V, S, M/DF (a dilated human eyeball)"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 round/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 4: Antipaladin\
6: Arcanist, Cleric, Inquisitor, Magus, Oracle, Psychic, Shaman, Sorcerer, Warpriest, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M/DF (a dilated human eyeball)
Range: medium (100 ft. + 10 ft./level)
Duration: 1 round/level (D)
Saving throw: none
Spell resistance: no
Target: you
Subschool: Teleportation
Descriptors: evil, fear, mind-affecting
:::

**Sources:** Horror Adventures pg 114

You gain the ability to detect fear, as per [sense fear](ref/spell/sense-fear), but you sense
creatures within medium range.

Once per round as a standard action, you can teleport to a creature suffering from a fear effect
within the spell's range if you are aware of the creature and its rough location. You can carry
objects with you so long as you don't transport more than your maximum load. You arrive in a random
open space within 20 feet of the creature and immediately begin sensing the location of creatures
with a fear condition from your new location.

Once you teleport to a new location with this spell, you can take no additional actions for the
round, as if casting dimension door. You can't teleport if there are no creatures suffering from a
fear effect in range.
