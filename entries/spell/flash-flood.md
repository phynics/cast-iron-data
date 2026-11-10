+++
id = "ref/spell/flash-flood"
kind = "spell"
title = "Flash Flood"
source_ids = ["wilderness-origins"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "flash_flood", path = "json/spells4.json" },
]
[[sources]]
publication = "wilderness-origins"
page = "27"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Creation"]
descriptors = ["water"]
levels = [
  { class = "Arcanist", level = 6 },
  { class = "Druid", level = 6 },
  { class = "Hunter", level = 6 },
  { class = "Shaman", level = 6 },
  { class = "Sorcerer", level = 6 },
  { class = "Wizard", level = 6 },
]
casting_time = "1 standard action"
components = "V, S, M (water-smoothed pebble)"
range = "60 ft."
effects = [
  { label = "Area", value = "cone-shaped burst" },
]
duration = "instantaneous and 1 round per level; see text"
saving_throw = "Reflex partial, see text"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 6: Arcanist, Druid, Hunter, Shaman, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M (water-smoothed pebble)
Range: 60 ft.
Duration: instantaneous and 1 round per level; see text
Saving throw: Reflex partial, see text
Spell resistance: no
Area: cone-shaped burst
Subschool: Creation
Descriptors: water
:::

You call forth a fast-moving wave that batters all creatures in its path and leaves the target area
flooded. Each creature in the area must succeed at a Reflex save or take 1d6 points of bludgeoning
damage per 2 caster levels (maximum 10d6). The wave also attempts a bull rush combat maneuver
against all creatures of any size within its area of effect. Attempt a single combat maneuver check
and apply the result to each creature within the area. Your CMB for this bull rush is equal to your
caster level plus your Intelligence, Wisdom, or Charisma modifier, whichever is highest. This bull
rush attempt doesn't provoke attacks of opportunity.

The area covered by the cone remains inundated for 1 round per caster level. If cast on land, treat
the area as a deep bog. If cast on water, the water level within the affected area rises by 5 feet.
