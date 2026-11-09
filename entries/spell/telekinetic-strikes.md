+++
id = "ref/spell/telekinetic-strikes"
kind = "spell"
title = "Telekinetic Strikes"
source_ids = ["psychic-anthology"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "telekinetic_strikes", path = "json/spells10.json" },
]
[[sources]]
publication = "psychic-anthology"
page = "11"

[fields]
kind = "spell"
school = "evocation"
descriptors = ["force"]
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Magus", level = 2 },
  { class = "Psychic", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "1 minute/level"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 2: Arcanist, Magus, Psychic, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: 1 minute/level
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
Target: one creature
Descriptors: force
:::

The touched creature's limbs are charged with telekinetic force. For the duration of the spell, the
target's unarmed attacks or natural weapons deal an additional 1d4 points of force damage on each
successful unarmed melee attack.
