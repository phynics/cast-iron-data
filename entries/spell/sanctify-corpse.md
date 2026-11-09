+++
id = "ref/spell/sanctify-corpse"
kind = "spell"
title = "Sanctify Corpse"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "sanctify_corpse", path = "json/spells8.json" },
]
[[sources]]
publication = "ultimate-magic"
page = "236"

[fields]
kind = "spell"
school = "evocation"
descriptors = ["good"]
levels = [
  { class = "Cleric", level = 1 },
  { class = "Inquisitor", level = 1 },
  { class = "Oracle", level = 1 },
  { class = "Paladin", level = 1 },
  { class = "Spiritualist", level = 1 },
  { class = "Warpriest", level = 1 },
  { class = "Witch", level = 1 },
]
casting_time = "1 standard action"
components = "V, S, DF, M (a pinch of silver dust)"
range = "touch"
effects = [
  { label = "Area", value = "corpse touched" },
]
duration = "24 hours"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 1: Cleric, Inquisitor, Oracle, Paladin, Spiritualist, Warpriest, Witch
Casting time: 1 standard action
Components: V, S, DF, M (a pinch of silver dust)
Range: touch
Duration: 24 hours
Saving throw: none
Spell resistance: no
Area: corpse touched
Descriptors: good
:::

This spell blesses a corpse with positive energy, preventing it from being turned into an undead
creature. Attempts to raise the corpse as an undead automatically fail. If the corpse is of a person
slain by a creature that creates undead out of its slain foes (such as a shadow, vampire, or
wraith), that effect is delayed until the end of this spell. It is possible to protect a corpse for
an extended time by casting this spell each day.

Sanctify corpse can be made permanent with a [permanency](ref/spell/permanency) spell by a caster of
9th level or higher for the cost of 500 gp.
