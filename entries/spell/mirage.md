+++
id = "ref/spell/mirage"
kind = "spell"
title = "Mirage"
aon = "SpellDisplay.aspx?ItemName=Mirage"
source_ids = ["ultimate-wilderness"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "mirage", path = "json/spells14.json" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "232"

[fields]
kind = "spell"
school = "illusion"
subschools = ["Figment"]
levels = [
  { class = "Bard", level = 3 },
  { class = "Druid", level = 3 },
  { class = "Hunter", level = 3 },
  { class = "Mesmerist", level = 3 },
  { class = "Occultist", level = 3 },
  { class = "Psychic", level = 3 },
  { class = "Ranger", level = 3 },
  { class = "Skald", level = 3 },
]
casting_time = "10 minutes"
components = "V, S, M (a pinch of sand and a drop of water)"
range = "long (400 ft. + 40 ft./level)"
effects = [
  { label = "Area", value = "one 40-ft.-cube/level (S)" },
]
duration = "2 hours/level (D)"
saving_throw = "Will disbelief (see below)"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 3: Bard, Druid, Hunter, Mesmerist, Occultist, Psychic, Ranger, Skald
Casting time: 10 minutes
Components: V, S, M (a pinch of sand and a drop of water)
Range: long (400 ft. + 40 ft./level)
Duration: 2 hours/level (D)
Saving throw: Will disbelief (see below)
Spell resistance: yes
Area: one 40-ft.-cube/level (S)
Subschool: Figment
:::

You create an image of a pool of water, a group of standing stones, a cove, an island, or another
simple land formation over a stretch of flat land or water. The image is purely visual, and
structures, equipment, and creatures within the area are not hidden or changed in appearance.

Anyone interacting with the illusion can attempt to disbelieve it, and a creature trained in
Survival can make a special attempt to disbelieve the illusion. The creature must be within 120 feet
of the illusion's area and can attempt a Survival check instead of a Will saving throw. If the
result is equal to or greater than the spell's save DC, the creature realizes the mirage is an
illusion as if it disbelieved the spell.
