+++
id = "ref/spell/darkness"
kind = "spell"
title = "Darkness"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "darkness", path = "json/spells3.json" },
]

[fields]
kind = "spell"
school = "evocation"
descriptors = ["darkness"]
levels = [
  { class = "Adept", level = 2 },
  { class = "Antipaladin", level = 2 },
  { class = "Arcanist", level = 2 },
  { class = "Bard", level = 2 },
  { class = "Cleric", level = 2 },
  { class = "Inquisitor", level = 2 },
  { class = "Magus", level = 2 },
  { class = "Occultist", level = 2 },
  { class = "Oracle", level = 2 },
  { class = "Shaman", level = 2 },
  { class = "Skald", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Warpriest", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, M/DF (bat fur and a piece of coal)"
range = "touch"
effects = [
  { label = "Target", value = "object touched" },
]
duration = "1 minute/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 2: Adept, Antipaladin, Arcanist, Bard, Cleric, Inquisitor, Magus, Occultist, Oracle, Shaman, Skald, Sorcerer, Warpriest, Wizard
Casting time: 1 standard action
Components: V, M/DF (bat fur and a piece of coal)
Range: touch
Duration: 1 minute/level (D)
Saving throw: none
Spell resistance: no
Target: object touched
Descriptors: darkness
:::

**Sources:** PRPG Core Rulebook pg 263

This spell causes an object to radiate darkness out to a 20-foot radius. This darkness causes the
illumination level in the area to drop one step, from bright light to normal light, from normal
light to dim light, or from dim light to darkness. This spell has no effect in an area that is
already dark. Creatures with light vulnerability or sensitivity take no penalties in normal light.
All creatures gain concealment (20% miss chance) in dim light. All creatures gain total concealment
(50% miss chance) in darkness. Creatures with [darkvision](ref/rule/darkvision) can see in an area
of dim light or darkness without penalty. Nonmagical sources of light, such as torches and lanterns,
do not increase the light level in an area of darkness. Magical light sources only increase the
light level in an area if they are of a higher spell level than darkness.

If darkness is cast on a small object that is then placed inside or under a lightproof covering, the
spell's effect is blocked until the covering is removed.

This spell does not stack with itself. Darkness can be used to counter or dispel any light spell of
equal or lower spell level.
