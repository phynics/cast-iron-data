+++
id = "ref/spell/rend-body-2"
kind = "spell"
title = "Rend Body II"
source_ids = ["psychic-anthology"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "rend_body_2", path = "json/spells8.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/rend-body-1" },
]

[fields]
kind = "spell"
school = "evocation"
levels = [
  { class = "Psychic", level = 5 },
]
casting_time = "1 full-round action"
components = "S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "instantaneous"
saving_throw = "Fortitude partial (see text)"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 5: Psychic
Casting time: 1 full-round action
Components: S
Range: close (25 ft. + 5 ft./2 levels)
Duration: instantaneous
Saving throw: Fortitude partial (see text)
Spell resistance: yes
Target: one creature
:::

## Rend Body I

**Sources:** Psychic Anthology pg 10

You lacerate the body of the target creature with telekinetic force, rending it limb from limb. The
target creature takes 1d6 points of damage per caster level you have (maximum 10d6 points of
damage). If this spell deals an amount of damage to the target equal to more than half its maximum
hit point total, one of the target's limbs (determined randomly) is gruesomely ripped from the
target's body and flies 15 feet away from the creature in a random direction. The target then takes
1 point of bleed damage per 2 caster levels you have. The bleeding can be stopped by a successful DC
15 Heal check or the application of any effect that heals hit point damage, but the limb can be
restored only by powerful healing effects such as heal or regeneration. If the damage reduces the
target's hit points to below 0, all of its limbs are affected in this fashion.

Creatures without discernible anatomy or limbs are unaffected by rend body.

### Rend Body II

**Sources:** Psychic Anthology pg 10

This spell functions as per [rend body I](ref/spell/rend-body-1), but the target takes 1d8 points of
damage per caster level you have (maximum 10d8). This spell can be undercast.

### Rend Body III

**Sources:** Psychic Anthology pg 10

This spell functions as per rend body I, but the target takes 1d8 points of damage per caster level
you have (maximum 15d8), and if a limb is ripped from its body, the target is sickened for as long
as the bleed damage persists. This spell can be undercast.

### Rend Body IV

**Sources:** Psychic Anthology pg 10

This functions as per rend body III, but the target takes 1d8 points of damage per caster level
(maximum 20d8), and one of the target's limbs is ripped off if the amount of damage dealt is greater
than 1/4 of its maximum hit point total. This spell can be undercast.
