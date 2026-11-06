+++
id = "ref/spell/dread-bolt"
kind = "spell"
title = "Dread Bolt"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "dread_bolt", path = "json/spells13.json" },
]

[fields]
kind = "spell"
school = "evocation"
descriptors = ["evil"]
levels = [
  { class = "Cleric", level = 2 },
  { class = "Oracle", level = 2 },
  { class = "Warpriest", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Effect", value = "arrow-shaped projectile of evil energy" },
]
duration = "instantaneous (1d4 rounds)"
saving_throw = "Will partial (see text)"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 2: Cleric, Oracle, Warpriest
Casting time: 1 standard action
Components: V, S, DF
Range: close (25 ft. + 5 ft./2 levels)
Duration: instantaneous (1d4 rounds)
Saving throw: Will partial (see text)
Spell resistance: yes
Effect: arrow-shaped projectile of evil energy
Descriptors: evil
:::

**Sources:** Ultimate Magic pg 217

You unleash a crackling missile of darkness from your unholy symbol at any one target in range as a
ranged touch attack.

A good creature struck by dread bolt takes 1d8 points of damage per two caster levels (maximum 5d8).
A good outsider instead takes 1d6 points of damage per caster level (maximum 10d6) and is sickened
for 1 round. A successful Will save reduces the damage to half and negates the sickened effect. This
spell deals only half damage to creatures that are neither good nor evil, and they are not sickened.
The bolt has no effect on evil creatures.
