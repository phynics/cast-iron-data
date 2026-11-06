+++
id = "ref/spell/buoyancy"
kind = "spell"
title = "Buoyancy"
source_ids = ["advanced-class-guide", "pirates-of-the-inner-sea"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "buoyancy", path = "json/spells2.json" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Bard", level = 2 },
  { class = "Psychic", level = 2 },
  { class = "Red Mantis Assassin", level = 2 },
  { class = "Shaman", level = 2 },
  { class = "Skald", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Witch", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 immediate action"
components = "V"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Targets", value = "one Medium or smaller object or creature/level, no two of which can be more than 20 ft. apart" },
]
duration = "up to 1 round/level (see text)"
saving_throw = "Will negates (harmless) or Will negates (object)"
spell_resistance = "yes (object)"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 2: Arcanist, Bard, Psychic, Red Mantis Assassin, Shaman, Skald, Sorcerer, Witch, Wizard
Casting time: 1 immediate action
Components: V
Range: close (25 ft. + 5 ft./2 levels)
Duration: up to 1 round/level (see text)
Saving throw: Will negates (harmless) or Will negates (object)
Spell resistance: yes (object)
Targets: one Medium or smaller object or creature/level, no two of which can be more than 20 ft. apart
:::

**Sources:** Advanced Class Guide pg 177, Pirates of the Inner Sea pg 28

The affected targets become incredibly buoyant, floating naturally on any water at least 1 foot
deep. An affected creature that deliberately tries to submerge must succeed at a DC 20 Swim check
every round to stay underwater. If a target spends at least 1 round on dry land, the spell ends for
that creature only.
