+++
id = "ref/spell/salvage"
kind = "spell"
title = "Salvage"
aon = "SpellDisplay.aspx?ItemName=Salvage"
source_ids = ["pirates-of-the-inner-sea"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "salvage", path = "json/spells8.json" },
]
[[sources]]
publication = "pirates-of-the-inner-sea"
page = "28"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Arcanist", level = 9 },
  { class = "Cleric", level = 9 },
  { class = "Oracle", level = 9 },
  { class = "Sorcerer", level = 9 },
  { class = "Wizard", level = 9 },
]
casting_time = "1 standard action"
components = "V, S, M"
range = "long (400 ft. + 40 ft./level)"
effects = [
  { label = "Targets", value = "one shipwreck" },
]
duration = "see text"
saving_throw = "Fortitude negates (object)"
spell_resistance = "yes (object)"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 9: Arcanist, Cleric, Oracle, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M
Range: long (400 ft. + 40 ft./level)
Duration: see text
Saving throw: Fortitude negates (object)
Spell resistance: yes (object)
Targets: one shipwreck
:::

An invisible force pulls together the remains of a shipwreck. Bits of hull, tattered sails, broken
masts, and smashed figureheads knit themselves back together. Rotten wood turns solid once more, and
sails re-weave themselves as the rigging snakes across the masts.

It takes a variable amount of time for the ship to rebuild itself, depending on its size.

|Size|Duration|
| --- | --- |
|Raft|1 minute|
|Rowboat|1 minute|
|Keelboat|10 minutes|
|Longship|1 hour|
|Sailing ship|2 hours|
|Warship|3 hours|
|Galleon|4 hours|

At the end of the duration, an air bubble forms around the repaired ship. If submerged, the ship
shoots to the surface, erupting with a great splash before settling on the water.

Though the spell requires time to repair the ship, its effects are instantaneous. A salvaged ship
cannot be dispelled to return it to a shipwreck. However, before the spell's duration ends and while
the ship is still being repaired, salvage can be dispelled to interrupt the repair process. The ship
remains in the condition it was in when the spell was interrupted until a new salvage spell is cast
(but continues to age normally and suffers the effects of its environments). A new salvage spell's
duration is modified by any repairs already begun.
