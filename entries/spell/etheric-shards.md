+++
id = "ref/spell/etheric-shards"
kind = "spell"
title = "Etheric Shards"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "etheric_shards", path = "json/spells4.json" },
]

[fields]
kind = "spell"
school = "evocation"
descriptors = ["force"]
levels = [
  { class = "Occultist", level = 4 },
  { class = "Psychic", level = 5 },
  { class = "Spiritualist", level = 4 },
]
casting_time = "1 standard action"
components = "S, M (broken glass)"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Area", value = "one 10-ft. cube/level" },
]
duration = "1 hour/level (D)"
saving_throw = "Reflex partial or Reflex negates (see text)"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 4: Occultist, Spiritualist\
5: Psychic
Casting time: 1 standard action
Components: S, M (broken glass)
Range: medium (100 ft. + 10 ft./level)
Duration: 1 hour/level (D)
Saving throw: Reflex partial or Reflex negates (see text)
Spell resistance: no
Area: one 10-ft. cube/level
Descriptors: force
:::

**Sources:** Occult Adventures pg 171

You harden interpenetrated ethereal substance into deadly transdimensional razors that are invisible
to normal sight. Movement through an area of etheric shards is halved, even for incorporeal
creatures, and creatures entering a 5-foot cube filled with etheric shards take 1d8 points of
piercing and slashing damage and must succeed at a Reflex save or take 1 point of bleed damage. This
bleed damage stacks with itself and other sources of bleed damage. A creature standing within an
area of etheric shards takes no damage as long as it remains completely motionless, but even the
minor movements involved in attacking or defending in combat force a stationary creature to attempt
a Reflex save. If a stationary creature succeeds at this save, it avoids damage completely for that
round, but if it fails, it takes hit point damage and bleed damage as though it had moved through
the square.

A creature forcibly moved through an area of etheric shards, such as by a bull rush or drag combat
maneuver, takes a -4 penalty on its saving throw, but a creature able to see invisible or ethereal
objects gains a +4 bonus, and damage to it is completely negated on a successful Reflex save.

Etheric shards are considered a magical trap, and a creature with trapfinding can use Perception to
find them. The DC of this check is equal to 25 + the spell's level. Etheric shards can't be disabled
with the Disable Device skill.
