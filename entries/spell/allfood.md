+++
id = "ref/spell/allfood"
kind = "spell"
title = "Allfood"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "allfood", path = "json/spells.json" },
]
[[sources]]
publication = "advanced-players-guide"
page = "201"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Hunter", level = 2 },
  { class = "Ranger", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, M (a pinch of salt and pepper)"
range = "touch"
effects = [
  { label = "Target", value = "object touched, weighing up to 5 lbs./level" },
]
duration = "instantaneous"
saving_throw = "Will negates (object)"
spell_resistance = "yes (object)"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 2: Hunter, Ranger
Casting time: 1 standard action
Components: V, S, M (a pinch of salt and pepper)
Range: touch
Duration: instantaneous
Saving throw: Will negates (object)
Spell resistance: yes (object)
Target: object touched, weighing up to 5 lbs./level
:::

You can transform one object, weighing up to 5 lbs. per caster level, into an edible substance that
any living creature can chew, swallow, and safely digest. This allfood always has a bland taste and
slightly gooey consistency when chewed regardless of its original nature. One pound of allfood
provides enough sustenance to support a Medium creature for an entire day.

Objects of similar nature in close proximity, such as a pile of rocks, count as a single object for
the purpose of this spell. You cannot use this spell to transform objects with magical or other
exceptional qualities. An object's [hardness](ref/umr/hardness) is considered to be 0 for the
purposes of eating it, but it retains its normal hardness for all other situations, and becomes no
more vulnerable to sunder attacks, break attempts, or any other action typically directed against
objects. Objects such as hot coals or a burning torch continue to produce energy even after you
transform them into allfood and if a creature attempts to eat such an object, it takes damage
accordingly.
