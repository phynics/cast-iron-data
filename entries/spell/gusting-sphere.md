+++
id = "ref/spell/gusting-sphere"
kind = "spell"
title = "Gusting Sphere"
aon = "SpellDisplay.aspx?ItemName=Gusting%20Sphere"
source_ids = ["advanced-race-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "gusting_sphere", path = "json/spells5.json" },
]
[[sources]]
publication = "advanced-race-guide"
page = "160"

[fields]
kind = "spell"
school = "evocation"
descriptors = ["air"]
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Bloodrager", level = 2 },
  { class = "Druid", level = 2 },
  { class = "Hunter", level = 2 },
  { class = "Magus", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Effect", value = "5-ft.-diameter sphere of air" },
]
duration = "1 round/level"
saving_throw = "Fortitude negates (object) or Reflex negates, see text"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 2: Arcanist, Bloodrager, Druid, Hunter, Magus, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S
Range: medium (100 ft. + 10 ft./level)
Duration: 1 round/level
Saving throw: Fortitude negates (object) or Reflex negates, see text
Spell resistance: yes
Effect: 5-ft.-diameter sphere of air
Descriptors: air
:::

> _[Sylphs](ref/race/sylph) have access to the following spell._

A swirling ball of wind rolls in whichever direction you point, hurling those it strikes with great
force. The sphere is treated in all ways as an area of severe wind, applying a -4 penalty on ranged
weapon attacks that pass through it. The sphere moves 30 feet per round. As part of this movement,
it can ascend or jump up to 30 feet to strike a target. If it enters a space containing a Medium or
smaller creature, it stops moving for that round and generates a sharp thrust of wind to bull rush
the creature. The sphere's CMB for bull rush combat maneuvers uses your caster level in place of its
base attack bonus, with a +2 bonus for its Strength score (14). Whether or not the bull rush is
successful, the creature takes 1d6 points of nonlethal bludgeoning damage from the attack. If the
bull rush fails, the creature is still subject to the severe winds from the sphere as long as they
remain in the same square as it. A gusting sphere rolls over objects or barriers that are less than
4 feet tall.

The sphere moves as long as you actively direct it (a move action for you); otherwise, it merely
stays at rest. A gusting sphere immediately dissipates if it exceeds the spell's range.
