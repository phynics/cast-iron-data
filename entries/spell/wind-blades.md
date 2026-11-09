+++
id = "ref/spell/wind-blades"
kind = "spell"
title = "Wind Blades"
source_ids = ["advanced-race-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "wind_blades", path = "json/spells16.json" },
]
[[sources]]
publication = "advanced-race-guide"
page = "160"

[fields]
kind = "spell"
school = "transmutation"
descriptors = ["air"]
levels = [
  { class = "Arcanist", level = 5 },
  { class = "Druid", level = 5 },
  { class = "Hunter", level = 5 },
  { class = "Magus", level = 5 },
  { class = "Sorcerer", level = 5 },
  { class = "Witch", level = 5 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "1 round/level"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 5: Arcanist, Druid, Hunter, Magus, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: 1 round/level
Saving throw: Will negates
Spell resistance: yes
Target: creature touched
Descriptors: air
:::

> _[Sylphs](ref/race/sylph) have access to the following spell._

You harden the air around the target into jagged invisible blades that deal damage based on how fast
the target moves. On its turn, the target takes 1d6 points of slashing damage if it moves at least 5
feet, plus 1d6 points of slashing damage for each additional 10 feet of movement. Movement that
doesn't pass through air (such as burrowing, swimming, or teleportation) doesn't cause this damage.

In areas of strong wind, the target takes damage on its turn, even if it doesn't move. The wind
deals 1d8 points of slashing damage for strong wind, plus 1d8 for every wind category above strong.
This extra damage does not occur from instantaneous wind effects (such as
[gust of wind](ref/spell/gust-of-wind)), only from wind effects that last at least 1 round.
