+++
id = "ref/spell/hydrophobia"
kind = "spell"
title = "Hydrophobia"
source_ids = ["magical-marketplace"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "hydrophobia", path = "json/spells5.json" },
]
[[sources]]
publication = "magical-marketplace"
page = "8"

[fields]
kind = "spell"
school = "necromancy"
descriptors = ["emotion", "fear", "mind-affecting"]
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Bard", level = 2 },
  { class = "Cleric", level = 3 },
  { class = "Druid", level = 3 },
  { class = "Hunter", level = 3 },
  { class = "Oracle", level = 3 },
  { class = "Skald", level = 2 },
  { class = "Sorcerer", level = 3 },
  { class = "Warpriest", level = 3 },
  { class = "Witch", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Area", value = "30-ft.-radius burst" },
]
duration = "1 round/level"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 2: Bard, Skald\
3: Arcanist, Cleric, Druid, Hunter, Oracle, Sorcerer, Warpriest, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level
Saving throw: Will negates
Spell resistance: yes
Area: 30-ft.-radius burst
Descriptors: emotion, fear, mind-affecting
:::

Targets in the area must succeed at a Will save or become deathly afraid of drowning. If the target
is swimming or otherwise submerged in water, it must spend all of its efforts attempting to escape
from the water. As long as an affected target remains in water, it takes 1d6 points of nonlethal
damage each round as it thrashes about and swallows water. Even out of water, targets cannot imbibe
potions or willingly interact with any fluids for the duration of this spell.
