+++
id = "ref/spell/burning-arc"
kind = "spell"
title = "Burning Arc"
source_ids = ["humans-of-golarion"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "burning_arc", path = "json/spells2.json" },
]
[[sources]]
publication = "humans-of-golarion"
page = "28"

[fields]
kind = "spell"
school = "evocation"
descriptors = ["fire"]
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one primary target plus one additional target/3 levels (each of which must be within 15 ft. of the primary target)" },
]
duration = "instantaneous"
saving_throw = "Reflex half"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 2: Arcanist, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: instantaneous
Saving throw: Reflex half
Spell resistance: yes
Target: one primary target plus one additional target/3 levels (each of which must be within 15 ft. of the primary target)
Descriptors: fire
:::

Keleshites brag that they stole this spell from genie-kind thousands of years ago while other
civilizations struggled without fire.

This spell causes an arc of flame to leap from your fingers, burning a number of enemies nearby. It
deals 1d6 points of fire damage per caster level (maximum 10d6). For every additional target the
discharge arcs to, reduce the number of damage dice by half (rounded down). Therefore, at 9th level,
your burning arc deals 9d6 points of fire damage to the primary target, then 4d6 points of fire
damage to a secondary target, then 2d6 points of fire damage to an additional target.

Each target can attempt a Reflex saving throw for half damage. The Reflex DC to halve the damage of
the secondary bolts is 2 lower than the DC to halve the damage of the primary bolt. You may choose
secondary targets as you like, but they must all be within 15 feet of the primary target, and no
target can be struck more than once. You can choose to affect fewer secondary targets than the
maximum.
