+++
id = "ref/spell/curse-of-dragonflies"
kind = "spell"
title = "Curse of Dragonflies"
source_ids = ["blood-of-the-coven"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "curse_of_dragonflies", path = "json/spells3.json" },
]

[fields]
kind = "spell"
school = "conjuration"
descriptors = ["air", "curse"]
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Druid", level = 3 },
  { class = "Hunter", level = 3 },
  { class = "Magus", level = 3 },
  { class = "Shaman", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Summoner", level = 4 },
  { class = "Witch", level = 3 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S, M (a paper insect)"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "permanent (D)"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 3: Druid, Hunter, Magus, Witch\
4: Arcanist, Shaman, Sorcerer, Summoner, Wizard
Casting time: 1 standard action
Components: V, S, M (a paper insect)
Range: medium (100 ft. + 10 ft./level)
Duration: permanent (D)
Saving throw: Will negates
Spell resistance: yes
Target: one creature
Descriptors: air, curse
:::

**Sources:** Blood of the Coven pg 21

You invest a target with cursed elemental energy, making the open skies anathema to it. If the
affected creature ever tries to fly more than 5 feet above the ground, paper insects erupt from the
air around the creature to interfere with its movement. The affected creature's flight
maneuverability decreases by one step for every 3 caster levels you have. A creature whose
maneuverability would be brought below clumsy must land at the end of its turn each round or fall.

This spell does not affect incorporeal creatures or creatures that are otherwise intangible (such as
a wizard using gaseous form to fly).
