+++
id = "ref/spell/riversight"
kind = "spell"
title = "Riversight"
aon = "SpellDisplay.aspx?ItemName=Riversight"
source_ids = ["people-of-the-river"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "riversight", path = "json/spells8.json" },
]
[[sources]]
publication = "people-of-the-river"
page = "27"

[fields]
kind = "spell"
school = "divination"
subschools = ["Scrying"]
levels = [
  { class = "Cleric", level = 3 },
  { class = "Druid", level = 2 },
  { class = "Hunter", level = 2 },
  { class = "Inquisitor", level = 3 },
  { class = "Oracle", level = 3 },
  { class = "Ranger", level = 2 },
  { class = "Warpriest", level = 3 },
  { class = "Witch", level = 3 },
]
casting_time = "1 minute"
components = "V, S, F/DF (a smooth river stone)"
range = "see text"
effects = [
  { label = "Target", value = "nonmagical freshwater waterway" },
  { label = "Effect", value = "magical sensor" },
]
duration = "1 minute/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 2: Druid, Hunter, Ranger\
3: Cleric, Inquisitor, Oracle, Warpriest, Witch
Casting time: 1 minute
Components: V, S, F/DF (a smooth river stone)
Range: see text
Duration: 1 minute/level (D)
Saving throw: none
Spell resistance: no
Target: nonmagical freshwater waterway
Effect: magical sensor
Subschool: Scrying
:::

You can view events transpiring along a natural watercourse you touch. You can see anything on or
within the river as if you were present at that location, or you can observe anything happening
within 15 feet of the river's banks as if peering from the water's surface. Moving your point of
view to a different location along the river is a standard action, though your perception can follow
something moving along the river as a free action.

The range of this spell is affected by whether you are attempting to gaze up or downriver - if
viewing a location downriver, you can view any spot within 2 miles per caster level; if viewing
upriver, you can view any spot within 1/2 mile per caster level. The magical sensor created by this
spell can travel only as far along the river as your range and the river permits; obstructions such
as dams and reservoirs halt the sensor, as does an estuary flowing into the sea or other body of
saltwater.
