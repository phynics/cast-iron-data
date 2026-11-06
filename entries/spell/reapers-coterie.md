+++
id = "ref/spell/reapers-coterie"
kind = "spell"
title = "Reaper's Coterie"
source_ids = ["melee-tactics-toolbox"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "reapers_coterie", path = "json/spells8.json" },
]

[fields]
kind = "spell"
school = "necromancy"
descriptors = ["evil"]
levels = [
  { class = "Antipaladin", level = 2 },
  { class = "Bloodrager", level = 2 },
  { class = "Cleric", level = 3 },
  { class = "Inquisitor", level = 3 },
  { class = "Oracle", level = 3 },
  { class = "Warpriest", level = 3 },
  { class = "Witch", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "touch"
effects = [
  { label = "Target", value = "weapon touched" },
]
duration = "1 round/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 2: Antipaladin, Bloodrager\
3: Cleric, Inquisitor, Oracle, Warpriest, Witch
Casting time: 1 standard action
Components: V, S, DF
Range: touch
Duration: 1 round/level
Saving throw: none
Spell resistance: no
Target: weapon touched
Descriptors: evil
:::

**Sources:** Melee Tactics Toolbox pg 31

The target weapon becomes a reservoir of spiritual energy, fueling its destructive power by drawing
in a tiny fragment of the essence of each creature it is used to defeat. When the targeted weapon is
used to reduce a living creature to 0 or fewer hit points, it gains a +1 profane bonus on damage
rolls. This bonus increases by 1 for each creature reduced to 0 hit points or fewer with that
weapon, up to a maximum bonus equal to 1/2 your caster level.
