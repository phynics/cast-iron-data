+++
id = "ref/spell/pox-pustules"
kind = "spell"
title = "Pox Pustules"
source_ids = ["advanced-players-guide", "mythic-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "pox_pustules", path = "json/spells14.json" },
]

[fields]
kind = "spell"
school = "necromancy"
descriptors = ["disease"]
levels = [
  { class = "Druid", level = 2 },
  { class = "Hunter", level = 2 },
  { class = "Witch", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, M (leaves from a toxic plant)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "1 minute/level"
saving_throw = "Fortitude negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 2: Druid, Hunter, Witch
Casting time: 1 standard action
Components: V, S, M (leaves from a toxic plant)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 minute/level
Saving throw: Fortitude negates
Spell resistance: yes
Target: one creature
Descriptors: disease
:::

**Sources:** Advanced Player's Guide pg 236

You inflict a painful, itching rash on the target creature. The target is sickened and takes a -4
penalty to Dexterity (this penalty cannot lower Dexterity below 0). The target can spend a move
action scratching furiously at the rash to remove the sickened condition (but not the Dexterity
penalty) until the start of its next turn.

### Mythic Pox Pustules

**Sources:** Mythic Adventures pg 104\
The Dexterity penalty increases to -6. The target takes 1 point of bleed damage each round. If the
target spends a move action scratching, increase its bleed damage each round by 1. If the bleeding
is stopped, scratching causes it to start again at 1 point of bleed per round.
