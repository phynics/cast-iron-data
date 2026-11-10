+++
id = "ref/spell/explode-head"
kind = "spell"
title = "Explode Head"
aon = "SpellDisplay.aspx?ItemName=Explode%20Head"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "explode_head", path = "json/spells4.json" },
]
[[sources]]
publication = "occult-adventures"
page = "171"

[fields]
kind = "spell"
school = "evocation"
levels = [
  { class = "Arcanist", level = 6 },
  { class = "Magus", level = 6 },
  { class = "Psychic", level = 5 },
  { class = "Sorcerer", level = 6 },
  { class = "Wizard", level = 6 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one living corporeal creature" },
]
duration = "instantaneous"
saving_throw = "special, see text"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 5: Psychic\
6: Arcanist, Magus, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: instantaneous
Saving throw: special, see text
Spell resistance: yes
Target: one living corporeal creature
:::

You cause incredible pressure to build in the target's head; this spell works only on a creature
that has a head and would die from the loss of a head. The spell kills any such target that has 20
hit points or fewer, exploding its head and spreading debris in a 10-foot radius. Each creature in
the area must succeed at a Reflex saving throw or take 2d6 points of slashing damage from the flying
debris.

A target with more than 20 hit points takes 1d6 points of damage per caster level (maximum 20d6),
but can attempt a Fortitude save to take only half damage. If this damage would cause the target to
become disabled or dying, the target dies and its head explodes as described above.
