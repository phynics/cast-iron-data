+++
id = "ref/spell/disintegrate"
kind = "spell"
title = "Disintegrate"
source_ids = ["core-rulebook", "mythic-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "disintegrate", path = "json/spells13.json" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Arcanist", level = 6 },
  { class = "Magus", level = 6 },
  { class = "Occultist", level = 6 },
  { class = "Psychic", level = 6 },
  { class = "Sorcerer", level = 6 },
  { class = "Spiritualist", level = 6 },
  { class = "Wizard", level = 6 },
]
casting_time = "1 standard action"
components = "V, S, M/DF (a lodestone and a pinch of dust)"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Effect", value = "ray" },
]
duration = "instantaneous"
saving_throw = "Fortitude partial (object)"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 6: Arcanist, Magus, Occultist, Psychic, Sorcerer, Spiritualist, Wizard
Casting time: 1 standard action
Components: V, S, M/DF (a lodestone and a pinch of dust)
Range: medium (100 ft. + 10 ft./level)
Duration: instantaneous
Saving throw: Fortitude partial (object)
Spell resistance: yes
Effect: ray
:::

**Sources:** PRPG Core Rulebook pg 271

A thin, green ray springs from your pointing finger. You must make a successful ranged touch attack
to hit. Any creature struck by the ray takes 2d6 points of damage per caster level (to a maximum of
40d6). Any creature reduced to 0 or fewer hit points by this spell is entirely disintegrated,
leaving behind only a trace of fine dust. A disintegrated creature's equipment is unaffected.

When used against an object, the ray simply disintegrates as much as a 10-foot cube of nonliving
matter. Thus, the spell disintegrates only part of any very large object or structure targeted. The
ray affects even objects constructed entirely of force, such as forceful hand or a wall of force,
but not magical effects such as a [globe of invulnerability](ref/spell/globe-of-invulnerability) or
an [antimagic field](ref/spell/antimagic-field).

A creature or object that makes a successful Fortitude save is partially affected, taking only 5d6
points of damage. If this damage reduces the creature or object to 0 or fewer hit points, it is
entirely disintegrated.

Only the first creature or object struck can be affected; that is, the ray affects only one target
per casting.

### Mythic Disintegrate

**Sources:** Mythic Adventures pg 91\
The damage dealt increases to 3d6 points of damage per caster level (maximum 60d6) plus 1d4 points
of Constitution damage.

A creature that succeeds at its saving throw takes 5d8 points of damage plus 1 point of Constitution
damage. A creature whose Constitution score is reduced to 0 by this spell is entirely disintegrated.

_Augmented (7th):_ If you expend two uses of mythic power, you fire two rays.

Alternatively, you may fire only one ray, but if the target is a non-mythic creature and it fails
its saving throw, it's automatically disintegrated regardless of its current hp.
