+++
id = "ref/spell/polar-midnight"
kind = "spell"
title = "Polar Midnight"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "polar_midnight", path = "json/spells7.json" },
]
[[sources]]
publication = "ultimate-magic"
page = "232"

[fields]
kind = "spell"
school = "transmutation"
descriptors = ["cold", "darkness"]
levels = [
  { class = "Cleric", level = 9 },
  { class = "Druid", level = 9 },
  { class = "Oracle", level = 9 },
  { class = "Shaman", level = 9 },
  { class = "Witch", level = 9 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Effect", value = "30-ft. spread" },
]
duration = "1 round/level"
saving_throw = "Fortitude partial"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 9: Cleric, Druid, Oracle, Shaman, Witch
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level
Saving throw: Fortitude partial
Spell resistance: yes
Effect: 30-ft. spread
Descriptors: cold, darkness
:::

You plunge an area into the brutal chill of the arctic night. Illumination conditions are dropped by
two steps (though only to darkness, not supernatural darkness), and all creatures in the area take
5d6 points of cold damage and 1d6 points of Dexterity damage per round. A successful Fortitude save
each round negates the Dexterity damage but not the cold damage. Any creature that doesn't move on
its turn becomes encased in a sheath of ice equivalent to wall of ice, is helpless, and cannot
breathe. Corpses in the area for longer than 1 round are transmuted into solid ice; reviving the icy
corpse requires [miracle](ref/spell/miracle), [true resurrection](ref/spell/true-resurrection), or
[wish](ref/spell/wish). As a move action, you may move the area of effect up to 10 feet in any
direction.
