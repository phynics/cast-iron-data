+++
id = "ref/spell/mark-of-obvious-ethics"
kind = "spell"
title = "Mark of Obvious Ethics"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "mark_of_obvious_ethics", path = "json/spells6.json" },
]

[fields]
kind = "spell"
school = "divination"
descriptors = ["curse"]
levels = [
  { class = "Cleric", level = 3 },
  { class = "Oracle", level = 3 },
  { class = "Warpriest", level = 3 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "1 day/level"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 3: Cleric, Oracle, Warpriest
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: 1 day/level
Saving throw: Will negates
Spell resistance: yes
Target: creature touched
Descriptors: curse
:::

**Sources:** Advanced Class Guide pg 187

You mark one creature with a glowing sigil. The target's alignment must be opposite yours on at
least one alignment axis - if you are neutral with no other alignment components, the target must
have an alignment with no neutral component. Any creature that sees the target can attempt a DC 15
Knowledge (religion) check to discern the target's alignment, even if the mark is covered. You are
aware of the direction and distance to the target as long as it remains within 100 miles of you and
on the same plane.
