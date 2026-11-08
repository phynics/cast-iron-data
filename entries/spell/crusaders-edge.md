+++
id = "ref/spell/crusaders-edge"
kind = "spell"
title = "Crusader's Edge"
source_ids = ["inner-sea-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "crusaders_edge", path = "json/spells3.json" },
]

[fields]
kind = "spell"
school = "transmutation"
descriptors = ["good"]
levels = [
  { class = "Cleric", level = 4 },
  { class = "Inquisitor", level = 4 },
  { class = "Oracle", level = 4 },
  { class = "Paladin", level = 4 },
  { class = "Warpriest", level = 4 },
]
casting_time = "1 standard action"
components = "V, S, M (dried blood from an evil outsider, sprinkled on the weapon)"
range = "touch"
effects = [
  { label = "Target", value = "melee weapon touched" },
]
duration = "1 minute/level"
saving_throw = "Fortitude negates"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 4: Cleric, Inquisitor, Oracle, Paladin, Warpriest
Casting time: 1 standard action
Components: V, S, M (dried blood from an evil outsider, sprinkled on the weapon)
Range: touch
Duration: 1 minute/level
Saving throw: Fortitude negates
Spell resistance: no
Target: melee weapon touched
Descriptors: good
:::

**Sources:** Inner Sea Magic pg 53

This spell was created by the paladins of the Mendevian Crusades, and co-opted by inquisitors and
rangers dedicated to tracking and fighting demons, devils, and other evil extraplanar creatures.

When you cast this spell on a melee weapon you imbue it with a powerful holy energy, granting the
weapon the bane weapon quality against evil outsiders. Furthermore, whenever you score a successful
critical hit against an outsider with the evil subtype, you not only deal normal critical damage
with the weapon but also nauseate the outsider for 1d3 rounds - the outsider can reduce this
nauseated condition to sickened for 1 round with a successful Fortitude save.
