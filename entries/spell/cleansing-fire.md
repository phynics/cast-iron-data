+++
id = "ref/spell/cleansing-fire"
kind = "spell"
title = "Cleansing Fire"
source_ids = ["adventurers-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "cleansing_fire", path = "json/spells2.json" },
]

[fields]
kind = "spell"
school = "evocation"
descriptors = ["fire", "good"]
levels = [
  { class = "Cleric", level = 5 },
  { class = "Inquisitor", level = 4 },
  { class = "Oracle", level = 5 },
  { class = "Paladin", level = 4 },
  { class = "Warpriest", level = 5 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "touch"
effects = [
  { label = "Area", value = "30-ft. rdius emanating from the touched point" },
]
duration = "concentration, up to 1 round/level"
saving_throw = "none"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 4: Inquisitor, Paladin\
5: Cleric, Oracle, Warpriest
Casting time: 1 standard action
Components: V, S, DF
Range: touch
Duration: concentration, up to 1 round/level
Saving throw: none
Spell resistance: yes
Area: 30-ft. rdius emanating from the touched point
Descriptors: fire, good
:::

**Sources:** Adventurer's Guide pg 17

A ring of fire surrounds the area affected by the spell. The flames radiate heat, but not enough to
damage adjacent creatures. The flames deal 2d6 points of fire damage to any creatures that pass
through them (or 4d6 points of damage to undead creatures). If you manifest a portion of the ring in
a square that contains a creature, that creature takes damage as if it passed through the ring.

The ring of flames attempts to dispel all ongoing spell effects with the evil descriptor within it,
targeting each spell effect once per round as per [dispel magic](ref/spell/dispel-magic). Any
attempt to cast a spell with the evil descriptor inside the ring of flames is targeted by a dispel
magic affect that attempts to counterspell the evil spell.
