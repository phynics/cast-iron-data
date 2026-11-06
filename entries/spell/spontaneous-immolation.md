+++
id = "ref/spell/spontaneous-immolation"
kind = "spell"
title = "Spontaneous Immolation"
source_ids = ["ultimate-combat", "orcs-of-golarion"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "spontaneous_immolation", path = "json/spells9.json" },
]

[fields]
kind = "spell"
school = "evocation"
descriptors = ["fire"]
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Psychic", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, M (pinch of saltpeter)"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "instantaneous"
saving_throw = "Fortitude half and Reflex (see description)"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 2: Arcanist, Psychic, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M (pinch of saltpeter)
Range: medium (100 ft. + 10 ft./level)
Duration: instantaneous
Saving throw: Fortitude half and Reflex (see description)
Spell resistance: yes
Target: one creature
Descriptors: fire
:::

**Sources:** Ultimate Combat pg 245, Orcs of Golarion pg 28

You point your finger at a creature, causing it to spontaneously burst into flame. The target takes
3d6 points of fire damage and catches on fire. A successful Fortitude save reduces this damage by
half and prevents the target from catching on fire. Each round on your turn, a burning target can
attempt a new save to extinguish the flames (DC equal to the DC of the spell); otherwise it takes
another 1d6 fire damage.
