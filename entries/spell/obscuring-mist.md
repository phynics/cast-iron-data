+++
id = "ref/spell/obscuring-mist"
kind = "spell"
title = "Obscuring Mist"
source_ids = ["core-rulebook", "mythic-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "obscuring_mist", path = "json/spells7.json" },
]

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Creation"]
levels = [
  { class = "Adept", level = 1 },
  { class = "Arcanist", level = 1 },
  { class = "Cleric", level = 1 },
  { class = "Druid", level = 1 },
  { class = "Hunter", level = 1 },
  { class = "Magus", level = 1 },
  { class = "Mesmerist", level = 1 },
  { class = "Oracle", level = 1 },
  { class = "Shaman", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Spiritualist", level = 1 },
  { class = "Unchained Summoner", level = 1 },
  { class = "Warpriest", level = 1 },
  { class = "Witch", level = 1 },
  { class = "Wizard", level = 1 },
]
casting_time = "1 standard action"
components = "V, S"
range = "20 ft."
effects = [
  { label = "Effect", value = "cloud spreads in 20-ft. radius from you, 20 ft. high" },
]
duration = "1 minute/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 1: Adept, Arcanist, Cleric, Druid, Hunter, Magus, Mesmerist, Oracle, Shaman, Sorcerer, Spiritualist, Unchained Summoner, Warpriest, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: 20 ft.
Duration: 1 minute/level (D)
Saving throw: none
Spell resistance: no
Effect: cloud spreads in 20-ft. radius from you, 20 ft. high
Subschool: Creation
:::

**Sources:** PRPG Core Rulebook pg 317

A misty vapor arises around you. It is stationary. The vapor obscures all sight, including
[darkvision](ref/rule/darkvision), beyond 5 feet. A creature 5 feet away has concealment (attacks
have a 20% miss chance). Creatures farther away have total concealment (50% miss chance, and the
attacker cannot use sight to locate the target).

A moderate wind (11+ mph), such as from a [gust of wind](ref/spell/gust-of-wind) spell, disperses
the fog in 4 rounds. A strong wind (21+ mph) disperses the fog in 1 round. A fireball, flame strike,
or similar spell burns away the fog in the explosive or fiery spell's area. A wall of fire burns
away the fog in the area into which it deals damage.

This spell does not function underwater.

### Mythic Obscuring Mist

**Sources:** Mythic Adventures pg 102\
The range increases to 50 feet, and the cloud's radius and height both increase to 50 feet.

_Augmented (3rd):_ If you expend two uses of mythic power, the range increases to 500 feet. The
cloud's radius increases to 500 feet, and its height increases to 100 feet. Winds can't dissipate
the mist unless the area of the wind affects the entire area of this spell. Areas of mist burned
away by fire spells become obscured again 1d4 rounds after the fire effect ends.

If you're at least 6th tier and expend three uses of mythic power, the range increases to 1 mile,
the cloud radius increases to 1 mile, and its height increases to 500 feet. The cloud is as
resistant to wind and fire effects as the 3rd-tier version.
