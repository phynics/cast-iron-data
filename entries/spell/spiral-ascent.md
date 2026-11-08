+++
id = "ref/spell/spiral-ascent"
kind = "spell"
title = "Spiral Ascent"
source_ids = ["inner-sea-temples"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "spiral_ascent", path = "json/spells9.json" },
]

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Teleportation"]
levels = [
  { class = "Cleric", level = 3 },
  { class = "Inquisitor", level = 3 },
  { class = "Oracle", level = 3 },
  { class = "Warpriest", level = 3 },
]
casting_time = "1 standard action"
components = "V, S"
range = "long (400 ft. + 40 ft./level)"
effects = [
  { label = "Target", value = "you and touched objects" },
]
duration = "instantaneous"
saving_throw = "Will negates (object)"
spell_resistance = "yes (object)"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 3: Cleric, Inquisitor, Oracle, Warpriest
Casting time: 1 standard action
Components: V, S
Range: long (400 ft. + 40 ft./level)
Duration: instantaneous
Saving throw: Will negates (object)
Spell resistance: yes (object)
Target: you and touched objects
Subschool: Teleportation
:::

**Sources:** Inner Sea Temples pg 43

You transform yourself into a helical beam of divine energy that instantly transports you upward to
a spot within range. The destination must be a square in the spell's range that's within 10 feet of
a point directly above you. The destination must be within your line of sight or familiar to you.
After using this spell, you can't take any other actions until your next turn. You can bring along
objects as long as their weight doesn't exceed your maximum load.

If you arrive in a place that is already occupied by a solid body, you are teleported to a random
open space on a suitable surface within the range and other limitations of the spell. If no such
space is available, the spell simply fails. This spell does not function on a plane lacking gravity.
On a plane with subjective directional gravity, you can use this spell to teleport in any direction.
