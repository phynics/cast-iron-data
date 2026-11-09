+++
id = "ref/spell/daylight"
kind = "spell"
title = "Daylight"
source_ids = ["core-rulebook", "adventurers-guide", "inner-sea-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "daylight", path = "json/spells3.json" },
]
[[sources]]
publication = "core-rulebook"
page = "264"

[fields]
kind = "spell"
school = "evocation"
descriptors = ["light"]
levels = [
  { class = "Adept", level = 3 },
  { class = "Arcanist", level = 3 },
  { class = "Bard", level = 3 },
  { class = "Cleric", level = 3 },
  { class = "Druid", level = 3 },
  { class = "Hunter", level = 3 },
  { class = "Inquisitor", level = 3 },
  { class = "Magus", level = 3 },
  { class = "Occultist", level = 3 },
  { class = "Oracle", level = 3 },
  { class = "Paladin", level = 3 },
  { class = "Shaman", level = 3 },
  { class = "Skald", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Warpriest", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "object touched" },
]
duration = "10 minutes/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 3: Adept, Arcanist, Bard, Cleric, Druid, Hunter, Inquisitor, Magus, Occultist, Oracle, Paladin, Shaman, Skald, Sorcerer, Warpriest, Wizard
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: 10 minutes/level (D)
Saving throw: none
Spell resistance: no
Target: object touched
Descriptors: light
:::

You touch an object when you cast this spell, causing the object to shed bright light in a 60-foot
radius. This illumination increases the light level for an additional 60 feet by one step (darkness
becomes dim light, dim light becomes normal light, and normal light becomes bright light). Creatures
that take penalties in bright light take them while within the 60-foot radius of this magical light.
Despite its name, this spell is not the equivalent of daylight for the purposes of creatures that
are damaged or destroyed by such light.

If daylight is cast on a small object that is then placed inside or under a light-proof covering,
the spell's effects are blocked until the covering is removed.

Daylight brought into an area of magical darkness (or vice versa) is temporarily negated, so that
the otherwise prevailing light conditions exist in the overlapping areas of effect.

Daylight counters or dispels any darkness spell of equal or lower level, such as
[darkness](ref/spell/darkness).
