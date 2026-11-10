+++
id = "ref/spell/siege-of-trees"
kind = "spell"
title = "Siege of Trees"
aon = "SpellDisplay.aspx?ItemName=Siege%20of%20Trees"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "siege_of_trees", path = "json/spells9.json" },
]
[[sources]]
publication = "ultimate-combat"
page = "244"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Druid", level = 7 },
]
casting_time = "10 minutes"
components = "V, S, DF"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Targets", value = "one Large plant per three caster levels" },
]
duration = "1 hour/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 7: Druid
Casting time: 10 minutes
Components: V, S, DF
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 hour/level (D)
Saving throw: none
Spell resistance: no
Targets: one Large plant per three caster levels
:::

You imbue inanimate plants with limited mobility and a semblance of life. Each plant targeted acts
as a [light catapult](ref/eq-siegeengine/catapult-light) until the end of the spell's duration,
though you must spend a standard action to aim each of these tree catapults before the first time
they fire, and anytime thereafter when you want the trees to fire at a new target. The catapult uses
your caster level as its targeting bonus. With a free action, you can command one or all of the
trees under your command to stop firing. You do not need to supply ammunition to these tree
catapults; they will automatically load themselves with rocks and boulders in the area, digging them
deep from the ground if need be. You can supply the trees ammunition if you desire. The tree will
not load flaming ammunition, and these catapult trees cannot be affected by energy siege shot if the
energy selected is fire.
