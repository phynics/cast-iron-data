+++
id = "ref/spell/incendiary-runes"
kind = "spell"
title = "Incendiary Runes"
aon = "SpellDisplay.aspx?ItemName=Incendiary%20Runes"
source_ids = ["black-markets"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "incendiary_runes", path = "json/spells14.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/explosive-runes" },
]
[[sources]]
publication = "black-markets"
page = "31"

[fields]
kind = "spell"
school = "abjuration"
descriptors = ["fire"]
levels = [
  { class = "Arcanist", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Wizard", level = 1 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "one touched object weighing no more than 10 lbs." },
]
duration = "permanent until discharged (D)"
saving_throw = "Reflex partial"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 1: Arcanist, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: permanent until discharged (D)
Saving throw: Reflex partial
Spell resistance: yes
Target: one touched object weighing no more than 10 lbs.
Descriptors: fire
:::

This spell functions as [explosive runes](ref/spell/explosive-runes), except it creates a small
surge of flames rather than an explosion of force. The runes automatically deal 1d6 points of fire
damage to any creatures and objects in adjacent squares, and those creatures and objects catch fire
unless they succeed at Reflex saves.
