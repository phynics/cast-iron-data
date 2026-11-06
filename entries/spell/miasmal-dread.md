+++
id = "ref/spell/miasmal-dread"
kind = "spell"
title = "Miasmal Dread"
source_ids = ["inner-sea-races"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "miasmal_dread", path = "json/spells14.json" },
]

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["fear", "mind-affecting"]
levels = [
  { class = "Antipaladin", level = 2 },
  { class = "Bloodrager", level = 2 },
  { class = "Bard", level = 2 },
  { class = "Inquisitor", level = 3 },
  { class = "Skald", level = 2 },
]
casting_time = "1 standard action"
components = "V, S"
range = "30 ft."
effects = [
  { label = "Area", value = "cone-shaped burst" },
]
duration = "instantaneous"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 2: Antipaladin, Bloodrager, Bard, Skald\
3: Inquisitor
Casting time: 1 standard action
Components: V, S
Range: 30 ft.
Duration: instantaneous
Saving throw: none
Spell resistance: no
Area: cone-shaped burst
Subschool: Compulsion
Descriptors: fear, mind-affecting
:::

**Sources:** Inner Sea Races pg 221

> _The following spell is available to the indicated race or ethnicity:
> [Half-Orc](ref/race/half-orc)_

A cloud of sickly green mist pours from your mouth and coalesces around creatures in the cone.
Attempt a single [Intimidate](ref/skill/intimidate) check to demoralize as part of casting the
spell, comparing the result against the DC to Intimidate each foe within the area. You demoralize
all foes whose DC you meet or exceed.
