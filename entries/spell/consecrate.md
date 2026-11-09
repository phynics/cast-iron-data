+++
id = "ref/spell/consecrate"
kind = "spell"
title = "Consecrate"
aon = "SpellDisplay.aspx?ItemName=Consecrate"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "consecrate", path = "json/spells12.json" },
]
[[sources]]
publication = "core-rulebook"
page = "258"

[fields]
kind = "spell"
school = "evocation"
descriptors = ["good"]
levels = [
  { class = "Cleric", level = 2 },
  { class = "Inquisitor", level = 2 },
  { class = "Oracle", level = 2 },
  { class = "Warpriest", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, DF, M (a vial of holy water and 25 gp worth of silver dust)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Area", value = "20-ft. radius emanation" },
]
duration = "2 hours/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 2: Cleric, Inquisitor, Oracle, Warpriest
Casting time: 1 standard action
Components: V, S, DF, M (a vial of holy water and 25 gp worth of silver dust)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 2 hours/level
Saving throw: none
Spell resistance: no
Area: 20-ft. radius emanation
Descriptors: good
:::

This spell blesses an area with positive energy. The DC to resist positive channeled energy within
this area gains a +3 sacred bonus. Every undead creature entering a consecrated area suffers minor
disruption, suffering a -1 penalty on attack rolls, damage rolls, and saves. Undead cannot be
created within or summoned into a consecrated area. If the consecrated area contains an altar,
shrine, or other permanent fixture dedicated to your deity, pantheon, or aligned higher power, the
modifiers given above are doubled (+6 sacred bonus to positive channeled energy DCs, -2 penalties
for undead in the area).

You cannot consecrate an area with a similar fixture of a deity other than your own patron. Instead,
the consecrate spell curses the area, cutting off its connection with the associated deity or power.
This secondary function, if used, does not also grant the bonuses and penalties relating to undead,
as given above.

Consecrate counters and dispels [desecrate](ref/spell/desecrate).
