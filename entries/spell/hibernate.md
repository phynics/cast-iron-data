+++
id = "ref/spell/hibernate"
kind = "spell"
title = "Hibernate"
source_ids = ["faction-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "hibernate", path = "json/spells5.json" },
]

[fields]
kind = "spell"
school = "necromancy"
levels = [
  { class = "Druid", level = 1 },
  { class = "Hunter", level = 1 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "1 minute/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 1: Druid, Hunter
Casting time: 1 standard action
Components: V, S, DF
Range: touch
Duration: 1 minute/level (D)
Saving throw: none
Spell resistance: no
Target: creature touched
:::

**Sources:** Faction Guide pg 61

You place a willing subject into a cataleptic state. It remains aware of its surroundings but is
paralyzed, appearing dead unless observers make a DC 20 Heal check. Hibernate delays the effects of
poison, disease, and bleed effects for the spell's duration, and half of any hit point damage
suffered by the subject is converted to nonlethal damage.

This spell originated with the Green Faith, but has spread to all other druidic religions.
