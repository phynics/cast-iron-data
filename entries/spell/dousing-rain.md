+++
id = "ref/spell/dousing-rain"
kind = "spell"
title = "Dousing Rain"
aon = "SpellDisplay.aspx?ItemName=Dousing%20Rain"
source_ids = ["villain-codex"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "dousing_rain", path = "json/spells13.json" },
]
[[sources]]
publication = "villain-codex"
page = "176"

[fields]
kind = "spell"
school = "evocation"
descriptors = ["water"]
levels = [
  { class = "Bard", level = 2 },
  { class = "Druid", level = 2 },
  { class = "Hunter", level = 2 },
  { class = "Shaman", level = 2 },
  { class = "Skald", level = 2 },
  { class = "Witch", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, M/DF (a drop of water)"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Area", value = "cylinder (10-ft. radius, 40 ft. high)" },
]
duration = "1 round/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 2: Bard, Druid, Hunter, Shaman, Skald, Witch
Casting time: 1 standard action
Components: V, S, M/DF (a drop of water)
Range: medium (100 ft. + 10 ft./level)
Duration: 1 round/level (D)
Saving throw: none
Spell resistance: no
Area: cylinder (10-ft. radius, 40 ft. high)
Descriptors: water
:::

With a beckoning gesture, you call forth a downpour of rain. For the duration of the spell, the
following effects apply within the affected area. Nonmagical fires are automatically extinguished,
and all creatures and objects in the area gain fire resistance 5. The conjured water is conductive,
and whenever a doused creature takes electricity damage, it takes 1 additional point of electricity
damage. At 6th, 12th, and 18th levels, the fire resistance increases by 5 and the additional
electricity damage increases by 1 point.
