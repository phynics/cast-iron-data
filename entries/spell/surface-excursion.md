+++
id = "ref/spell/surface-excursion"
kind = "spell"
title = "Surface Excursion"
source_ids = ["heroes-of-the-darklands"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "surface_excursion", path = "json/spells10.json" },
]
[[sources]]
publication = "heroes-of-the-darklands"
page = "21"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Teleportation"]
levels = [
  { class = "Arcanist", level = 5 },
  { class = "Magus", level = 5 },
  { class = "Occultist", level = 4 },
  { class = "Psychic", level = 5 },
  { class = "Shaman", level = 5 },
  { class = "Sorcerer", level = 5 },
  { class = "Spiritualist", level = 4 },
  { class = "Summoner", level = 4 },
  { class = "Unchained Summoner", level = 4 },
  { class = "Witch", level = 5 },
  { class = "Wizard", level = 5 },
]
casting_time = "3 rounds"
components = "V, S, M (a handful of soil that has been in the sun for at least 6 hours)"
range = "touch"
effects = [
  { label = "Targets", value = "you plus up to one willing creature per 3 levels" },
]
duration = "1 hour/level (D)"
saving_throw = "Will negates (harmless)"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 4: Occultist, Spiritualist, Summoner, Unchained Summoner\
5: Arcanist, Magus, Psychic, Shaman, Sorcerer, Witch, Wizard
Casting time: 3 rounds
Components: V, S, M (a handful of soil that has been in the sun for at least 6 hours)
Range: touch
Duration: 1 hour/level (D)
Saving throw: Will negates (harmless)
Spell resistance: no
Targets: you plus up to one willing creature per 3 levels
Subschool: Teleportation
:::

You instantly transport yourself and touched allies onto the nearest sky-facing surface directly
above you. The destination surface may be solid ground or the surface of a body of water (or other
liquid), depending on your position. If reaching the surface would require crossing planar
boundaries or no sky-facing surface exists directly above your position, the spell fails and has no
effect.

When the spell is cast, a magical beacon appears at both your departure and arrival points,
suspended 3 feet in the air. These beacons are invisible to everyone but you and those allies
touched when the spell was cast. You and every creature originally targeted by the spell can touch
the beacon at your arrival point to teleport back to your original departure point. Each creature
that chooses to return in this manner is transported to a free space adjacent to the beacon at your
original departure point. If the area around the departure beacon is occupied by a solid body (for
instance, rubble from a cave-in), then you and each creature traveling with you take 1d6 points of
damage and are shunted to a random open space on a solid surface within 100 feet of the beacon. If
there is no free space within 100 feet, the spell effect ends with no return transportation.
