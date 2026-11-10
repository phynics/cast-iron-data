+++
id = "ref/spell/water-shield"
kind = "spell"
title = "Water Shield"
aon = "SpellDisplay.aspx?ItemName=Water%20Shield"
source_ids = ["pathfinder-24-the-final-wish"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "water_shield", path = "json/spells11.json" },
]
[[sources]]
publication = "pathfinder-24-the-final-wish"
page = "61"

[fields]
kind = "spell"
school = "evocation"
descriptors = ["acid", "water"]
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Cleric", level = 4 },
  { class = "Druid", level = 3 },
  { class = "Hunter", level = 3 },
  { class = "Oracle", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Warpriest", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S, M/DF (1 cup of water)"
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
Level: 3: Druid, Hunter\
4: Arcanist, Cleric, Oracle, Sorcerer, Warpriest, Wizard
Casting time: 1 standard action
Components: V, S, M/DF (1 cup of water)
Range: personal
Duration: 1 round/level (D)
Saving throw: none
Spell resistance: no
Target: you
Descriptors: acid, water
:::

This spell surrounds you in a spout of clear acid that aids in deflecting attacks and damages
creatures that attack you in melee. The constantly upward-rushing waters grant you a measure of
protecting, shielding you so you only take half damage from acid and fire-based attacks. If such an
attack allows a Reflex save for half damage, you take no damage on a successful save.

Any creature striking you with its body or a handheld weapon deals normal damage, but at the same
time the attacker takes 1d6 points of acid damage + 1 point per 2 caster levels (maximum +10). If
the attacker has [spell resistance](ref/rule/spell-resistance), it applies to this effect. Creatures
wielding weapons with exceptional reach are not subject to this damage if they attack you.
