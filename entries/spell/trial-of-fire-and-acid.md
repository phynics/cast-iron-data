+++
id = "ref/spell/trial-of-fire-and-acid"
kind = "spell"
title = "Trial of Fire and Acid"
source_ids = ["monster-codex"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "trial_of_fire_and_acid", path = "json/spells10.json" },
]
[[sources]]
publication = "monster-codex"
page = "225"

[fields]
kind = "spell"
school = "evocation"
descriptors = ["acid", "fire"]
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Bloodrager", level = 3 },
  { class = "Cleric", level = 3 },
  { class = "Magus", level = 3 },
  { class = "Oracle", level = 3 },
  { class = "Shaman", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Warpriest", level = 3 },
  { class = "Witch", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "1 round/level"
saving_throw = "Fortitude half (see text)"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 3: Arcanist, Bloodrager, Cleric, Magus, Oracle, Shaman, Sorcerer, Warpriest, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: 1 round/level
Saving throw: Fortitude half (see text)
Spell resistance: no
Target: creature touched
Descriptors: acid, fire
:::

The target creature is covered in burning acid that deals 1d6 points of acid damage and 1d6 points
of fire damage each round. The subject can attempt a Fortitude saving throw each round to reduce the
damage by half. Dousing the target in water ends the effect (both the acid and the fire), but
rolling on the ground does not extinguish the fire or affect the acid.
