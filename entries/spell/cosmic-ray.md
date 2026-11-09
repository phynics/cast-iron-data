+++
id = "ref/spell/cosmic-ray"
kind = "spell"
title = "Cosmic Ray"
source_ids = ["people-of-the-stars"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "cosmic_ray", path = "json/spells12.json" },
]
[[sources]]
publication = "people-of-the-stars"
page = "28"

[fields]
kind = "spell"
school = "evocation"
levels = [
  { class = "Arcanist", level = 6 },
  { class = "Magus", level = 5 },
  { class = "Sorcerer", level = 6 },
  { class = "Wizard", level = 6 },
]
casting_time = "1 standard action"
components = "V, S, M (a piece of meteorite)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Effect", value = "ray" },
]
duration = "instantaneous and 1 round/level (see text)"
saving_throw = "Fortitude partial"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 5: Magus\
6: Arcanist, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M (a piece of meteorite)
Range: close (25 ft. + 5 ft./2 levels)
Duration: instantaneous and 1 round/level (see text)
Saving throw: Fortitude partial
Spell resistance: yes
Effect: ray
:::

You fling a ray of deadly cosmic energy at the target creature. If you succeed at a ranged touch
attack with the ray, the target takes 1d6 points of damage per caster level (maximum 20d6) and must
make a Fortitude save. On a failed save, the target becomes sickened for 1 round per caster level
and emits toxic cosmic energy for as long as it is sickened; any creature that comes within 5 feet
of the affected target must succeed at a Fortitude save (DC = spell's DC) or become sickened for 1
round per 2 caster levels.
