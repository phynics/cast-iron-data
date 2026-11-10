+++
id = "ref/spell/profane-nimbus"
kind = "spell"
title = "Profane Nimbus"
source_ids = ["horror-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "profane_nimbus", path = "json/spells15.json" },
]
[[sources]]
publication = "horror-adventures"
page = "125"

[fields]
kind = "spell"
school = "evocation"
descriptors = ["evil"]
levels = [
  { class = "Antipaladin", level = 4 },
  { class = "Cleric", level = 5 },
  { class = "Inquisitor", level = 5 },
  { class = "Oracle", level = 5 },
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
Level: 4: Antipaladin\
5: Cleric, Inquisitor, Oracle, Warpriest
Casting time: 1 standard action
Components: V, S, DF
Range: personal
Duration: 1 round/level (D)
Saving throw: none
Spell resistance: no
Target: you
Descriptors: evil
:::

You are surrounded by a nimbus of shadow shaped like your god's unholy symbol or a symbol of your
faith. Any good creature striking you with unarmed strikes, natural weapons, or a handheld weapon
deals normal damage, but at the same time, the attacker takes 1d6 points of damage + 1 point per
caster level (maximum +15). Creatures wielding melee weapons with reach are not subject to this
damage if they attack you. [Spell resistance](ref/rule/spell-resistance) applies against this
damage. You also take half damage from magical attacks with the good descriptor. If such an attack
allows a Reflex save for half damage, you take no damage on a successful saving throw.
