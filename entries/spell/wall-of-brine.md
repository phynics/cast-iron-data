+++
id = "ref/spell/wall-of-brine"
kind = "spell"
title = "Wall of Brine"
source_ids = ["inner-sea-races"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "wall_of_brine", path = "json/spells11.json" },
]

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Creation"]
descriptors = ["water"]
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Druid", level = 4 },
  { class = "Hunter", level = 3 },
  { class = "Magus", level = 4 },
  { class = "Ranger", level = 3 },
  { class = "Shaman", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S, M/DF (a bit of coral)"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Effect", value = "wall up to 10 ft./level long and 5 ft./level high (S)" },
]
duration = "concentration+ 1 round/level"
saving_throw = "none, see text"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 3: Hunter, Ranger\
4: Arcanist, Druid, Magus, Shaman, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M/DF (a bit of coral)
Range: medium (100 ft. + 10 ft./level)
Duration: concentration+ 1 round/level
Saving throw: none, see text
Spell resistance: yes
Effect: wall up to 10 ft./level long and 5 ft./level high (S)
Subschool: Creation
Descriptors: water
:::

**Sources:** Inner Sea Races pg 223

> _The following spell is available to the indicated race or ethnicity: [Merfolk](ref/race/merfolk)_

You conjure a 5-foot-thick wall of seawater with a powerful current flowing toward one side of the
wall, selected by you; a creature attempting to swim against this current must spend 4 squares of
movement to enter a square of the wall. A creature that begins its turn in the wall is ejected in
the direction of the current just before it acts. The wall provides cover against attacks from out
of the water, as usual for a body of water. The water and the currents deflect physical ranged
attacks into or through the wall, unless a weapon used is exceptionally massive (such as a siege
engine). A creature submerged in the wall takes the usual penalties for underwater combat. The wall
blocks gases and liquids and prevents water from mixing at its edges.
