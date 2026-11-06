+++
id = "ref/spell/anywhere-but-here"
kind = "spell"
title = "Anywhere but Here"
source_ids = ["planar-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "anywhere_but_here", path = "json/spells.json" },
]

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Teleportation"]
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Magus", level = 4 },
  { class = "Psychic", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Summoner", level = 4 },
  { class = "Unchained Summoner", level = 4 },
  { class = "Witch", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V"
range = "touch"
effects = [
  { label = "Target", value = "you and up to four willing creatures, none of whom can be on their home plane" },
]
duration = "instantaneous"
saving_throw = "Will negates (harmless)"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 4: Arcanist, Magus, Psychic, Sorcerer, Summoner, Unchained Summoner, Witch, Wizard
Casting time: 1 standard action
Components: V
Range: touch
Duration: instantaneous
Saving throw: Will negates (harmless)
Spell resistance: no
Target: you and up to four willing creatures, none of whom can be on their home plane
Subschool: Teleportation
:::

**Sources:** Planar Adventures pg 38

This spell functions similarly to plane shift, but instead of transporting the targets to a
destination near an intended location on a specific plane, anywhere but here transports affected
creatures to a random plane. A creature can be affected by anywhere but here only if it is currently
not on its home plane (although targets can, by chance, end up traveling to their home plane as a
result of this spell). Subjects always appear in a location that is not inherently harmful, but the
exact destination is otherwise random. The specific plane is determined by the table below; the
location on the destination plane where the transported creatures arrive is completely subject to
the GM's whim.

|d%|Planar Destination|
| --- | --- |
|01-07|Abyss|
|08-14|Abaddon|
|15-20|Hell|
|21-24|Shadow Plane|
|25-28|First World|
|29-35|Maelstrom|
|36-42|Boneyard|
|43-49|Axis|
|50-56|Ethereal Plane|
|57-63|Elysium|
|64-70|Nirvana|
|71-77|Heaven|
|78-84|Astral Plane|
|85-90|Random demiplane|
|91-95|Material Plane (random world)|
|96-100|GM's choice|

A creature that is transported by anywhere but here cannot be affected by a subsequent casting of
anywhere but here for 24 hours afterward (but can be affected normally by other forms of planar
travel).
