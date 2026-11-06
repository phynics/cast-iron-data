+++
id = "ref/spell/storm-step"
kind = "spell"
title = "Storm Step"
source_ids = ["blood-of-the-elements"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "storm_step", path = "json/spells9.json" },
]

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Teleportation"]
descriptors = ["electricity"]
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Magus", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Witch", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "you" },
]
duration = "instantaneous"
saving_throw = "Reflex half"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 3: Arcanist, Magus, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: instantaneous
Saving throw: Reflex half
Spell resistance: yes
Target: you
Subschool: Teleportation
Descriptors: electricity
:::

**Sources:** Blood of the Elements pg 13

You are able to harness the power of the storm to transport yourself a short distance, by taking the
form of a furious, sizzling bolt of elemental electricity. You must either have line of sight to
your destination or you must specify a direction and distance within range. Creatures and objects in
the path of your passage take 1d8 points of electricity damage per 2 caster levels (maximum 5d8). A
successful Reflex save halves the damage.

If your path intersects with a solid object, you damage the barrier accordingly. If the damage is
enough to break through the barrier, you continue beyond the barrier as long as the spell's range
permits; otherwise, your movement stops in the square adjacent to the barrier and the effect ends.
