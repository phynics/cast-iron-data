+++
id = "ref/spell/deeper-darkness"
kind = "spell"
title = "Deeper Darkness"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "deeper_darkness", path = "json/spells3.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/darkness" },
]

[fields]
kind = "spell"
school = "evocation"
descriptors = ["darkness"]
levels = [
  { class = "Adept", level = 3 },
  { class = "Antipaladin", level = 3 },
  { class = "Cleric", level = 3 },
  { class = "Inquisitor", level = 3 },
  { class = "Occultist", level = 3 },
  { class = "Oracle", level = 3 },
  { class = "Shaman", level = 3 },
  { class = "Warpriest", level = 3 },
]
casting_time = "1 standard action"
components = "V, M/DF (bat fur and a piece of coal)"
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
Level: 3: Adept, Antipaladin, Cleric, Inquisitor, Occultist, Oracle, Shaman, Warpriest
Casting time: 1 standard action
Components: V, M/DF (bat fur and a piece of coal)
Range: touch
Duration: 10 minutes/level (D)
Saving throw: none
Spell resistance: no
Target: object touched
Descriptors: darkness
:::

**Sources:** PRPG Core Rulebook pg 265

This spell functions as [darkness](ref/spell/darkness), except that objects radiate darkness in a
60-foot radius and the light level is lowered by two steps. Bright light becomes dim light and
normal light becomes darkness. Areas of dim light and darkness become supernaturally dark. This
functions like darkness, but even creatures with [darkvision](ref/rule/darkvision) cannot see within
the spell's confines.

This spell does not stack with itself. Deeper darkness can be used to counter or dispel any light
spell of equal or lower spell level.
