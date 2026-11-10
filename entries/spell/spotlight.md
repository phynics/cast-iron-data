+++
id = "ref/spell/spotlight"
kind = "spell"
title = "Spotlight"
source_ids = ["blood-of-shadows"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "spotlight", path = "json/spells9.json" },
]
[[sources]]
publication = "blood-of-shadows"
page = "29"

[fields]
kind = "spell"
school = "evocation"
descriptors = ["darkness", "light"]
levels = [
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
  { class = "Witch", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S"
range = "long (400 ft. + 40 ft./level)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "1 minute/level (D)"
saving_throw = "Reflex partial"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 3: Arcanist, Bard, Cleric, Druid, Hunter, Inquisitor, Magus, Occultist, Oracle, Paladin, Shaman, Skald, Sorcerer, Warpriest, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: long (400 ft. + 40 ft./level)
Duration: 1 minute/level (D)
Saving throw: Reflex partial
Spell resistance: yes
Target: one creature
Descriptors: darkness, light
:::

You create a mobile area of bright light centered on one target while simultaneously suppressing
other light sources surrounding it. The light level in the target's space increases to bright light,
causing the target to take any penalties that it would normally take in bright light. In addition,
all mundane light sources (and magic light sources of 3rd spell level or lower) within 20 feet of
the target's space are suppressed, shedding no light as long as they remain within this spell's
affected area and reverting the area normally affected by those light sources to their unmodified
illumination levels.

The effects of spotlight are centered on the target and move as the target does. As a result, the
target takes a -20 penalty on all Stealth checks for the spell's duration and cannot benefit from
concealment normally provided by darkness, as though illuminated with faerie fire.

If the target succeeds at its Reflex save, the spotlight is created in the target's square but does
not move with the target, and it hinders the Stealth checks only of creatures within that square.
