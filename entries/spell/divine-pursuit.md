+++
id = "ref/spell/divine-pursuit"
kind = "spell"
title = "Divine Pursuit"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "divine_pursuit", path = "json/spells13.json" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Inquisitor", level = 5 },
]
casting_time = "1 standard action"
components = "V, S"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 minute/level; see text"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 5: Inquisitor
Casting time: 1 standard action
Components: V, S
Range: personal
Duration: 1 minute/level; see text
Saving throw: none
Spell resistance: no
Target: you
:::

**Sources:** Ultimate Magic pg 217

Select one creature within 60 feet that you have damaged. If that creature has a burrow, climb, fly,
or swim speed, you gain that form of movement for the duration of the spell at the same speed and
maneuverability as the selected creature. If this gives you the burrow or swim speed, you can
breathe while burrowing or swimming. If the creature moves 1,000 feet or more from you, the spell
ends. If the creature has more than one of these types of movement, you select one from the types
available to the creature.
