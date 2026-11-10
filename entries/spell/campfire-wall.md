+++
id = "ref/spell/campfire-wall"
kind = "spell"
title = "Campfire Wall"
aon = "SpellDisplay.aspx?ItemName=Campfire%20Wall"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "campfire_wall", path = "json/spells2.json" },
]
[[sources]]
publication = "advanced-players-guide"
page = "210"

[fields]
kind = "spell"
school = "evocation"
descriptors = ["fire", "light"]
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Bard", level = 3 },
  { class = "Druid", level = 2 },
  { class = "Hunter", level = 2 },
  { class = "Occultist", level = 2 },
  { class = "Ranger", level = 2 },
  { class = "Skald", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, M/DF (ash made from burnt thorns)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Effect", value = "20-ft.-radius sphere centered on fire source" },
]
duration = "2 hours/level; see below (D)"
saving_throw = "none"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 2: Druid, Hunter, Occultist, Ranger\
3: Arcanist, Bard, Skald, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M/DF (ash made from burnt thorns)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 2 hours/level; see below (D)
Saving throw: none
Spell resistance: yes
Effect: 20-ft.-radius sphere centered on fire source
Descriptors: fire, light
:::

You can create a barrier around a fire of at least campfire size that shelters everyone inside so
long as the fire continues to burn. The barrier appears as a crackling sphere of light and fire that
is clearly visible, providing as much illumination as a torch. The barrier bocks line of sight,
granting creatures on either side of the barrier [total concealment](ref/rule/concealment) from
creatures on the other side. Any object or creature passing through the barrier from outside takes
1d6 points of fire damage and is also outlined with light equivalent to that of a torch, for 1d6
minutes. Creatures outlined in this way are plainly visible regardless of the light conditions and
do not benefit from any sort of concealment, magical or otherwise. The light is not bright enough to
have any special effect on undead or creatures vulnerable to light. Creatures inside the barrier can
leave without penalty, but if they try to return they suffer the same consequences as anyone else.
If the fire source at the barrier's center is extinguished or moved, the spell ends.
