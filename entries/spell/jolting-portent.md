+++
id = "ref/spell/jolting-portent"
kind = "spell"
title = "Jolting Portent"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "jolting_portent", path = "json/spells6.json" },
]
[[sources]]
publication = "ultimate-combat"
page = "232"

[fields]
kind = "spell"
school = "evocation"
descriptors = ["electricity"]
levels = [
  { class = "Cleric", level = 7 },
  { class = "Oracle", level = 7 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "1 round/level (d) see text"
saving_throw = "none"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 7: Cleric, Oracle
Casting time: 1 standard action
Components: V, S, DF
Range: medium (100 ft. + 10 ft./level)
Duration: 1 round/level (d) see text
Saving throw: none
Spell resistance: yes
Target: one creature
Descriptors: electricity
:::

The creature you designate is surrounded by a glowing red aura of vengeful fate. Once per round when
the target makes an attack or casts a spell, it must succeed at a Fortitude saving throw with a DC =
10 + 1/2 caster level + Charisma (in the case of oracles) or Wisdom (in the case of clerics). If the
target fails the saving throw, it takes 4d6 + your Charisma modifier (in the case of oracles) or
Wisdom modifier (in the case of clerics) electricity damage. It takes no damage on a successful
saving throw. You can dismiss this spell as an immediate action when its subject confirms a critical
hit to negate the critical hit and daze the creature for 1 round. The attack still hits its target
and deals normal damage. The effects of the daze occur after the attack.
