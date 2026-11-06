+++
id = "ref/spell/unholy-ward"
kind = "spell"
title = "Unholy Ward"
source_ids = ["agents-of-evil"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "unholy_ward", path = "json/spells11.json" },
]

[fields]
kind = "spell"
school = "abjuration"
descriptors = ["evil"]
levels = [
  { class = "Antipaladin", level = 3 },
  { class = "Arcanist", level = 4 },
  { class = "Cleric", level = 4 },
  { class = "Inquisitor", level = 3 },
  { class = "Oracle", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Warpriest", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "10 minutes/level (D)"
saving_throw = "Fortitude negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 3: Antipaladin, Inquisitor\
4: Arcanist, Cleric, Oracle, Sorcerer, Warpriest, Wizard
Casting time: 1 standard action
Components: V, S, DF
Range: personal
Duration: 10 minutes/level (D)
Saving throw: Fortitude negates (harmless)
Spell resistance: yes (harmless)
Target: you
Descriptors: evil
:::

**Sources:** Agents of Evil pg 19

This spell grants you resistance to the holy powers of good-aligned deities and their servants. You
resist 10 points of damage from holy sources (divine power damage from flame strike, additional
damage from smite evil, channeled positive energy, etc.), provided they originate from a
good-aligned source or a servant of a good-aligned god. You ignore a maximum of 10 points of damage
per caster level, at which point the spell ends.
