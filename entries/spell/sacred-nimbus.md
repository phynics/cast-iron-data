+++
id = "ref/spell/sacred-nimbus"
kind = "spell"
title = "Sacred Nimbus"
source_ids = ["horror-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "sacred_nimbus", path = "json/spells8.json" },
]

[fields]
kind = "spell"
school = "evocation"
descriptors = ["good"]
levels = [
  { class = "Cleric", level = 5 },
  { class = "Inquisitor", level = 5 },
  { class = "Oracle", level = 5 },
  { class = "Paladin", level = 4 },
  { class = "Warpriest", level = 5 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 round/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 4: Paladin\
5: Cleric, Inquisitor, Oracle, Warpriest
Casting time: 1 standard action
Components: V, S, DF
Range: personal
Duration: 1 round/level (D)
Saving throw: none
Spell resistance: no
Target: you
Descriptors: good
:::

**Sources:** Horror Adventures pg 126

You are surrounded by a nimbus of golden light shaped like your god's holy symbol or a symbol of
your faith. Any evil creature striking you with unarmed strikes, natural weapons, or a handheld
weapon deals normal damage, but at the same time, the attacker takes 1d6 points of damage + 1 point
per caster level (maximum +15). Creatures wielding melee weapons with reach are not subject to this
damage if they attack you. [Spell resistance](ref/rule/spell-resistance) applies against this
damage. You also take half damage from magical attacks with the evil descriptor. If such an attack
allows a Reflex save for half damage, you take no damage on a successful saving throw.
