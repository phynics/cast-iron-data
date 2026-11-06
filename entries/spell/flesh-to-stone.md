+++
id = "ref/spell/flesh-to-stone"
kind = "spell"
title = "Flesh to Stone"
source_ids = ["core-rulebook", "mythic-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "flesh_to_stone", path = "json/spells4.json" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Arcanist", level = 6 },
  { class = "Magus", level = 6 },
  { class = "Shaman", level = 6 },
  { class = "Sorcerer", level = 6 },
  { class = "Witch", level = 6 },
  { class = "Wizard", level = 6 },
]
casting_time = "1 standard action"
components = "V, S, M (lime, water, and earth)"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "instantaneous"
saving_throw = "Fortitude negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 6: Arcanist, Magus, Shaman, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M (lime, water, and earth)
Range: medium (100 ft. + 10 ft./level)
Duration: instantaneous
Saving throw: Fortitude negates
Spell resistance: yes
Target: one creature
:::

**Sources:** PRPG Core Rulebook pg 284

The subject, along with all its carried gear, turns into a mindless, inert statue. If the statue
resulting from this spell is broken or damaged, the subject (if ever returned to its original state)
has similar damage or deformities. The creature is not dead, but it does not seem to be alive either
when viewed with spells such as deathwatch.

Only creatures made of flesh are affected by this spell.

### Mythic Flesh to Stone

**Sources:** Mythic Adventures pg 94\
A creature that succeeds at its saving throw is partially petrified, becoming slowed (as the
[slow](ref/spell/slow) spell) for a number of rounds equal to your tier. The creature can end this
effect early by spending a full-round action breaking away its own petrified flesh, dealing 5d10
points of damage to itself. Any effect that removes or reverses petrification negates this partial
petrification and the slow effect. The spell can affect objects and undead, as long as the target is
primarily made of flesh or bone, such as a corpse or zombie. The spell doesn't affect the target's
gear. If cast on a creature with equipment, the creature transforms into stone but its gear doesn't.

_Augmented (9th):_ If you expend two uses of mythic power, any Large or smaller creature fully
petrified by the spell immediately animates and follows your commands, as if you had cast animate
objects.
