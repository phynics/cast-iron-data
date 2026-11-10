+++
id = "ref/spell/groundswell"
kind = "spell"
title = "Groundswell"
aon = "SpellDisplay.aspx?ItemName=Groundswell"
source_ids = ["advanced-race-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "groundswell", path = "json/spells5.json" },
]
[[sources]]
publication = "advanced-race-guide"
page = "19"

[fields]
kind = "spell"
school = "transmutation"
descriptors = ["earth"]
levels = [
  { class = "Cleric", level = 2 },
  { class = "Druid", level = 2 },
  { class = "Hunter", level = 2 },
  { class = "Magus", level = 2 },
  { class = "Oracle", level = 2 },
  { class = "Ranger", level = 2 },
  { class = "Warpriest", level = 2 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "1 minute/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 2: Cleric, Druid, Hunter, Magus, Oracle, Ranger, Warpriest
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: 1 minute/level
Saving throw: none
Spell resistance: no
Target: creature touched
Descriptors: earth
:::

> _[Dwarven](ref/race/dwarf) spellcasters are renowned for shaping the ground beneath them, molding
> metal, and using magic to aid their craft. This spell one of several samples of such magics._

This spell allows the target to cause the ground to rise up beneath him. As a swift action, the
target can cause the ground to rise 5 feet, while all adjacent squares are treated as steep slopes.
The groundswell precludes flanking from creatures standing at lower elevations than the target. If
the target moves after creating a groundswell, the ground returns to its normal elevation at the end
of his turn; otherwise, it remains in place until the target moves or uses a swift action to return
the ground to normal. A groundswell cannot increase elevation of the ground beyond 5 feet.
