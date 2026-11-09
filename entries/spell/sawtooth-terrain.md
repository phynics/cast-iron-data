+++
id = "ref/spell/sawtooth-terrain"
kind = "spell"
title = "Sawtooth Terrain"
source_ids = ["adventurers-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "sawtooth_terrain", path = "json/spells8.json" },
]
[[sources]]
publication = "adventurers-guide"
page = "161"

[fields]
kind = "spell"
school = "transmutation"
descriptors = ["earth"]
levels = [
  { class = "Arcanist", level = 5 },
  { class = "Cleric", level = 5 },
  { class = "Druid", level = 5 },
  { class = "Hunter", level = 5 },
  { class = "Oracle", level = 5 },
  { class = "Sorcerer", level = 5 },
  { class = "Warpriest", level = 5 },
  { class = "Witch", level = 5 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 round"
components = "V, S, DF"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Effect", value = "one 10-foot square of difficult and damaging terrain" },
]
duration = "1 round/level"
saving_throw = "Reflex negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 5: Arcanist, Cleric, Druid, Hunter, Oracle, Sorcerer, Warpriest, Witch, Wizard
Casting time: 1 round
Components: V, S, DF
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level
Saving throw: Reflex negates
Spell resistance: yes
Effect: one 10-foot square of difficult and damaging terrain
Descriptors: earth
:::

This spell targets an area of earth, metal, stone, or wood, causing long, serrated blades to shoot
out from random points within the area of effect. Any creature in the area when the spell is first
cast must attempt a Reflex save to avoid taking 3d8 points of piercing damage from the blades and an
additional 2d6 points of bleed damage. A creature that fails the save also has its speed reduced by
half for 24 hours or until the injured creature benefits from a "cure" spell (which restores lost
hit points as normal). Another creature can remove the penalty by succeeding on a Heal check against
the spell's save DC as a standard action.

The lashing limbs remain active in the area for the remainder of the spell's duration, during which
time the area is treated as difficult terrain, and any creature that moves into or through the area
takes 1d8 points of piercing damage. The transformed area can be located on any visible surface
within range, including floors, walls, doors, ceilings, or other generally flat surfaces.
