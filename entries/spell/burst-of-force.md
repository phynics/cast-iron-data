+++
id = "ref/spell/burst-of-force"
kind = "spell"
title = "Burst of Force"
source_ids = ["psychic-anthology"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "burst_of_force", path = "json/spells2.json" },
]
[[sources]]
publication = "psychic-anthology"
page = "10"

[fields]
kind = "spell"
school = "evocation"
descriptors = ["force"]
levels = [
  { class = "Arcanist", level = 5 },
  { class = "Psychic", level = 5 },
  { class = "Sorcerer", level = 5 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 standard action"
components = "V"
range = "personal"
effects = [
  { label = "Area", value = "20-ft.-radius burst centered on you" },
]
duration = "instantaneous"
saving_throw = "Fortitude half (see text)"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 5: Arcanist, Psychic, Sorcerer, Wizard
Casting time: 1 standard action
Components: V
Range: personal
Duration: instantaneous
Saving throw: Fortitude half (see text)
Spell resistance: yes
Area: 20-ft.-radius burst centered on you
Descriptors: force
:::

With a burst of telekinetic force, you deal 1d6 points of force damage per caster level (maximum
15d6 points of damage) to all other creatures in the affected area. A successful Fortitude save
reduces the damage taken by half. A creature that fails its Fortitude save must also succeed at a
Reflex save or be knocked prone.
