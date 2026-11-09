+++
id = "ref/spell/molten-orb"
kind = "spell"
title = "Molten Orb"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "molten_orb", path = "json/spells14.json" },
]
[[sources]]
publication = "advanced-class-guide"
page = "188"

[fields]
kind = "spell"
school = "evocation"
descriptors = ["earth", "fire"]
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Bloodrager", level = 2 },
  { class = "Magus", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Witch", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Effect", value = "ranged attack" },
]
duration = "instantaneous"
saving_throw = "none"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 2: Arcanist, Bloodrager, Magus, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: instantaneous
Saving throw: none
Spell resistance: yes
Effect: ranged attack
Descriptors: earth, fire
:::

You create a fist-sized, red-hot ball of molten metal that you immediately hurl as a splash weapon.
A direct hit deals 2d6 points of fire damage. Every creature within 5 feet of where the ball hits
takes 1d6 points of fire damage from the splash (Reflex half). Each of these creatures takes an
additional 1d6 points of fire damage on its turn for the next 1d3 rounds, unless it is cooled off
(with water, snow, or any effect that deals 5 or more points of cold damage).
