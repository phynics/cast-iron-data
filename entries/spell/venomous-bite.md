+++
id = "ref/spell/venomous-bite"
kind = "spell"
title = "Venomous Bite"
source_ids = ["dirty-tactics-toolbox"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "venomous_bite", path = "json/spells11.json" },
]

[fields]
kind = "spell"
school = "transmutation"
descriptors = ["poison"]
levels = [
  { class = "Alchemist", level = 2 },
  { class = "Druid", level = 2 },
  { class = "Hunter", level = 2 },
  { class = "Investigator", level = 2 },
  { class = "Ranger", level = 2 },
  { class = "Shaman", level = 2 },
  { class = "Summoner", level = 2 },
  { class = "Witch", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, DF, M (a vial of injury poison worth at least 75 gp)"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "1 round/level (D)"
saving_throw = "Fortitude negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 2: Alchemist, Druid, Hunter, Investigator, Ranger, Shaman, Summoner, Witch
Casting time: 1 standard action
Components: V, S, DF, M (a vial of injury poison worth at least 75 gp)
Range: touch
Duration: 1 round/level (D)
Saving throw: Fortitude negates (harmless)
Spell resistance: yes (harmless)
Target: creature touched
Descriptors: poison
:::

**Sources:** Dirty Tactics Toolbox pg 29

When you touch the poison vial against the target creature and cast this spell, the vial drains and
the target's teeth become envenomed with the same poison. The creature gains the use of 1 dose of
the poison for every 5 caster levels you possess (maximum 4 doses). The creature gains immunity to
that poison while this spell is in effect. The poison retains its normal properties, and this spell
does not alter the DC to resist or cure the poison.

Each successful bite attack counts as an expended dose. When all the poison is used, the spell ends.
If the target creature doesn't have a bite attack, or if the target's bite attack is already
poisonous, the spell has no effect. If the target has multiple heads, the spell affects only one
bite attack.

When this spell ends, any unused poison is harmlessly expelled from the target's mouth and cannot be
used again.
