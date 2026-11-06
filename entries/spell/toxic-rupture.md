+++
id = "ref/spell/toxic-rupture"
kind = "spell"
title = "Toxic Rupture"
source_ids = ["dirty-tactics-toolbox"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "toxic_rupture", path = "json/spells10.json" },
]

[fields]
kind = "spell"
school = "necromancy"
descriptors = ["poison"]
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Druid", level = 3 },
  { class = "Hunter", level = 3 },
  { class = "Shaman", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Witch", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, M/DF (a viper's fang)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one poisonous creature" },
]
duration = "instantaneous"
saving_throw = "Fortitude negates see text"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 3: Arcanist, Druid, Hunter, Shaman, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M/DF (a viper's fang)
Range: close (25 ft. + 5 ft./2 levels)
Duration: instantaneous
Saving throw: Fortitude negates see text
Spell resistance: yes
Target: one poisonous creature
Descriptors: poison
:::

**Sources:** Dirty Tactics Toolbox pg 29

With a squeezing hand gesture, you cause internal bleeding in the target creature's venom glands or
similar organs. The target must attempt a saving throw against its own poison using the DC for this
spell. If it fails, the creature is poisoned and suffers the full effect of its poison. Any
subsequent saving throws that the target must attempt against the poison use the normal DC for the
poison rather than this spell's DC.
