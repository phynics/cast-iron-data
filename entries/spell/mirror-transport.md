+++
id = "ref/spell/mirror-transport"
kind = "spell"
title = "Mirror Transport"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "mirror_transport", path = "json/spells14.json" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Occultist", level = 4 },
  { class = "Psychic", level = 4 },
  { class = "Red Mantis Assassin", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Spiritualist", level = 4 },
  { class = "Witch", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S, M (a glass or metal marble and a twisted loop of parchment)"
range = "touch"
effects = [
  { label = "Target", value = "one mirror" },
]
duration = "1 hour/level (D)"
saving_throw = "yes (object)"
spell_resistance = "yes (object)"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 4: Arcanist, Occultist, Psychic, Red Mantis Assassin, Sorcerer, Spiritualist, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M (a glass or metal marble and a twisted loop of parchment)
Range: touch
Duration: 1 hour/level (D)
Saving throw: yes (object)
Spell resistance: yes (object)
Target: one mirror
:::

**Sources:** Advanced Class Guide pg 188

This spell functions as [mirror hideaway](ref/spell/mirror-hideaway), except any creature that
enters the target mirror can spend a swift action to exit through another mirror within 500 feet as
if using dimension door; this is a one-way transport. The creature can exit through a mirror only if
it could fit through an opening the same size as the mirror. Each transport through the target
mirror reduces the spell's duration by 1 hour.
