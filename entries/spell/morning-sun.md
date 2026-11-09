+++
id = "ref/spell/morning-sun"
kind = "spell"
title = "Morning Sun"
source_ids = ["heroes-of-the-darklands"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "morning_sun", path = "json/spells7.json" },
]
[[sources]]
publication = "heroes-of-the-darklands"
page = "15"

[fields]
kind = "spell"
school = "evocation"
descriptors = ["light"]
levels = [
  { class = "Cleric", level = 7 },
  { class = "Druid", level = 7 },
  { class = "Inquisitor", level = 6 },
  { class = "Oracle", level = 7 },
  { class = "Shaman", level = 7 },
]
casting_time = "1 standard action"
components = "V, S, M (500 gp worth of gold dust)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Area", value = "60-ft. radius" },
]
duration = "1 minute/level (D)"
saving_throw = "Fortitude negates and Reflex half; see text"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 6: Inquisitor\
7: Cleric, Druid, Oracle, Shaman
Casting time: 1 standard action
Components: V, S, M (500 gp worth of gold dust)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 minute/level (D)
Saving throw: Fortitude negates and Reflex half; see text
Spell resistance: no
Area: 60-ft. radius
Descriptors: light
:::

This spell conjures a miniature sphere of sunlight, approximately the size of a human fist, at a
desired location within range. The sphere sheds bright light in a 60-foot-radius burst. Creatures
that take penalties in bright light do so while within the sphere's area of illumination. Creatures
that start their turns within the area of illumination and that are damaged or destroyed by sunlight
must succeed at a Fortitude save or become staggered until 1d4+1 rounds after they leave the
affected area. Non-creatures, such as hazardous fungi and mold that are destroyed by sunlight,
become inert for the duration of the spell. The sphere cannot be moved from the place it was cast.
The sphere deals 10d6 points of fire damage to anything it touches and anything that passes within 5
feet of it. A successful Reflex save reduces this damage by half.
