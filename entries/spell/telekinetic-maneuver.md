+++
id = "ref/spell/telekinetic-maneuver"
kind = "spell"
title = "Telekinetic Maneuver"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "telekinetic_maneuver", path = "json/spells10.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/telekinesis" },
]
[[sources]]
publication = "occult-adventures"
page = "188"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Magus", level = 4 },
  { class = "Psychic", level = 3 },
  { class = "Sorcerer", level = 4 },
  { class = "Spiritualist", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "concentration (up to 1 round/level)"
saving_throw = "none"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 3: Psychic\
4: Arcanist, Magus, Sorcerer, Spiritualist, Wizard
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: concentration (up to 1 round/level)
Saving throw: none
Spell resistance: yes
Target: one creature
:::

This spell functions as [telekinesis](ref/spell/telekinesis), but it can be used only to perform a
bull rush, disarm, drag, grapple (including pin), reposition, steal, or trip combat maneuver.
