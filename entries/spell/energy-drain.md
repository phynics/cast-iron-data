+++
id = "ref/spell/energy-drain"
kind = "spell"
title = "Energy Drain"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "energy_drain", path = "json/spells4.json" },
]

[fields]
kind = "spell"
school = "necromancy"
levels = [
  { class = "Arcanist", level = 9 },
  { class = "Cleric", level = 9 },
  { class = "Oracle", level = 9 },
  { class = "Shaman", level = 9 },
  { class = "Sorcerer", level = 9 },
  { class = "Wizard", level = 9 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Effect", value = "ray of negative energy" },
]
duration = "instantaneous"
saving_throw = "Fortitude partial; see text for enervation"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 9: Arcanist, Cleric, Oracle, Shaman, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: instantaneous
Saving throw: Fortitude partial; see text for enervation
Spell resistance: yes
Effect: ray of negative energy
:::

**Sources:** PRPG Core Rulebook pg 277

This spell functions like enervation, except that the creature struck gains 2d4 temporary negative
levels. Twenty-four hours after gaining them, the subject must make a Fortitude saving throw (DC =
energy drain spell's save DC) for each negative level. If the save succeeds, that negative level is
removed. If it fails, that negative level becomes permanent.

An undead creature struck by the ray gains 2d4 × 5 temporary hit points for 1 hour.
