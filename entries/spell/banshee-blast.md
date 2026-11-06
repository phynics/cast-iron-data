+++
id = "ref/spell/banshee-blast"
kind = "spell"
title = "Banshee Blast"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "banshee_blast", path = "json/spells12.json" },
]

[fields]
kind = "spell"
school = "necromancy"
descriptors = ["death", "fear", "mind-affecting", "sonic"]
levels = [
  { class = "Arcanist", level = 6 },
  { class = "Sorcerer", level = 6 },
  { class = "Spiritualist", level = 6 },
  { class = "Witch", level = 6 },
  { class = "Wizard", level = 6 },
]
casting_time = "1 standard action"
components = "V, S"
range = "30 ft."
effects = [
  { label = "Area", value = "cone-shaped burst" },
]
duration = "instantaneous and 1 round/level (see text)"
saving_throw = "Reflex half and Will negates (see text)"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 6: Arcanist, Sorcerer, Spiritualist, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: 30 ft.
Duration: instantaneous and 1 round/level (see text)
Saving throw: Reflex half and Will negates (see text)
Spell resistance: yes
Area: cone-shaped burst
Descriptors: death, fear, mind-affecting, sonic
:::

**Sources:** Advanced Class Guide pg 174

You create a cone of spectral energy resembling screaming elven ghosts that deals 1d4 points of
damage per caster level (maximum 15d4); a successful Reflex save halves this damage. Any creature
that fails its Reflex save must succeed at a Will save or become panicked for 1 round/level.
