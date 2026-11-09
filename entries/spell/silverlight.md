+++
id = "ref/spell/silverlight"
kind = "spell"
title = "Silverlight"
source_ids = ["guide-to-the-river-kingdoms"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "silverlight", path = "json/spells9.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/daylight" },
]
[[sources]]
publication = "guide-to-the-river-kingdoms"
page = "25"

[fields]
kind = "spell"
school = "evocation"
descriptors = ["light"]
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Bard", level = 3 },
  { class = "Cleric", level = 3 },
  { class = "Druid", level = 3 },
  { class = "Hunter", level = 3 },
  { class = "Oracle", level = 3 },
  { class = "Paladin", level = 3 },
  { class = "Skald", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Warpriest", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, M (1 sp)"
range = "touch"
effects = [
  { label = "Target", value = "object touched" },
]
duration = "1 minute/level"
saving_throw = "Fortitude partial (see text)"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 3: Arcanist, Bard, Cleric, Druid, Hunter, Oracle, Paladin, Skald, Sorcerer, Warpriest, Wizard
Casting time: 1 standard action
Components: V, S, M (1 sp)
Range: touch
Duration: 1 minute/level
Saving throw: Fortitude partial (see text)
Spell resistance: no
Target: object touched
Descriptors: light
:::

As [daylight](ref/spell/daylight), except the object touched sheds bright silvery light in a 20-foot
radius. In addition to providing illumination, the area of bright light is painful to creatures that
are susceptible to alchemical silver. A creature with DR/silver that begins its turn within the
light of this spell is automatically dazzled and becomes sickened unless it succeeds on a Fortitude
save. These effects disappear 1 round after the target leaves the silverlight. A creature that
leaves the area and then returns must make a new saving throw. This spell provides dim light up to
40 feet away, but only creatures within 20 feet are subject to the above effects.
