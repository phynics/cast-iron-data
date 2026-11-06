+++
id = "ref/spell/detect-aberration"
kind = "spell"
title = "Detect Aberration"
source_ids = ["core-rulebook", "advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "detect_aberration", path = "json/spells3.json" },
]

[fields]
kind = "spell"
school = "divination"
levels = [
  { class = "Druid", level = 1 },
  { class = "Hunter", level = 1 },
  { class = "Psychic", level = 1 },
  { class = "Ranger", level = 1 },
  { class = "Shaman", level = 1 },
]
casting_time = "1 standard action"
components = "V, S"
range = "long (400 ft. + 40 ft./level)"
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
Level: 1: Druid, Hunter, Psychic, Ranger, Shaman
Casting time: 1 standard action
Components: V, S
Range: long (400 ft. + 40 ft./level)
Duration: concentration, up to 10 min./level (D)
Saving throw: none
Spell resistance: no
Area: cone-shaped emanation
:::

## Detect Animals or Plants

**Sources:** PRPG Core Rulebook pg 266

You can detect a particular kind of animal or plant in a cone emanating out from you in whatever
direction you face. You must think of a kind of animal or plant when using the spell, but you can
change the animal or plant kind each round. The amount of information revealed depends on how long
you search a particular area or focus on a specific kind of animal or plant.

_1st Round:_ Presence or absence of that kind of animal or plant in the area.

_2nd Round:_ Number of individuals of the specified kind in the area and the condition of the
healthiest specimen.

_3rd Round:_ The condition (see below) and location of each individual present. If an animal or a
plant is outside your line of sight, then you discern its direction but not its exact location.

_Conditions:_ For purposes of this spell, the categories of condition are as follows:

_Normal:_ Has at least 90% of full normal hit points, free of disease.

_Fair:_ 30% to 90% of full normal hit points remaining.

_Poor:_ Less than 30% of full normal hit points remaining, afflicted with a disease, or suffering
from a debilitating injury.

_Weak:_ 0 or fewer hit points remaining, afflicted with a disease that has reduced an ability score
to 5 or less, or crippled.

If a creature falls into more than one category, the spell indicates the weaker of the two.

Each round you can turn to detect a kind of animal or plant in a new area. The spell can penetrate
barriers, but 1 foot of stone, 1 inch of common metal, a thin sheet of lead, or 3 feet of wood or
dirt blocks it.

### Detect Aberration

**Sources:** Advanced Player's Guide pg 215

This spell functions like _[detect animals or plants](ref/spell/detect-animals-or-plants),_ except
it detects creatures of the aberration type.
