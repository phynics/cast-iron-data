+++
id = "ref/spell/detect-snares-and-pits"
kind = "spell"
title = "Detect Snares and Pits"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "detect_snares_and_pits", path = "json/spells3.json" },
]

[fields]
kind = "spell"
school = "divination"
levels = [
  { class = "Druid", level = 1 },
  { class = "Hunter", level = 1 },
  { class = "Occultist", level = 1 },
  { class = "Ranger", level = 1 },
]
casting_time = "1 standard action"
components = "V, S"
range = "60 ft."
effects = [
  { label = "Area", value = "cone-shaped emanation" },
]
duration = "concentration, up to 10 min./level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 1: Druid, Hunter, Occultist, Ranger
Casting time: 1 standard action
Components: V, S
Range: 60 ft.
Duration: concentration, up to 10 min./level (D)
Saving throw: none
Spell resistance: no
Area: cone-shaped emanation
:::

**Sources:** PRPG Core Rulebook pg 268

You can detect simple pits, deadfalls, and snares as well as mechanical traps constructed of natural
materials. The spell does not detect complex traps, including trapdoor traps.

Detect snares and pits does detect certain natural hazards: quicksand (a snare), a sinkhole (a pit),
or unsafe walls of natural rock (a deadfall). It does not reveal other potentially dangerous
conditions. The spell does not detect magic traps (except those that operate by pit, deadfall, or
snaring; see the spell [snare](ref/spell/snare)), nor mechanically complex ones, nor those that have
been rendered safe or inactive.

The amount of information revealed depends on how long you study a particular area.

_1st Round:_ Presence or absence of hazards.

_2nd Round:_ Number of hazards and the location of each. If a hazard is outside your line of sight,
then you discern its direction but not its exact location.

_Each Additional Round:_ The general type and trigger for one particular hazard closely examined by
you.

Each round, you can turn to examine a new area. The spell can penetrate barriers, but 1 foot of
stone, 1 inch of common metal, a thin sheet of lead, or 3 feet of wood or dirt blocks it.
