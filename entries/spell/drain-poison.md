+++
id = "ref/spell/drain-poison"
kind = "spell"
title = "Drain Poison"
source_ids = ["dirty-tactics-toolbox"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "drain_poison", path = "json/spells13.json" },
]

[fields]
kind = "spell"
school = "transmutation"
descriptors = ["poison"]
levels = [
  { class = "Alchemist", level = 3 },
  { class = "Antipaladin", level = 3 },
  { class = "Cleric", level = 3 },
  { class = "Druid", level = 3 },
  { class = "Hunter", level = 3 },
  { class = "Investigator", level = 3 },
  { class = "Oracle", level = 3 },
  { class = "Ranger", level = 3 },
  { class = "Warpriest", level = 3 },
  { class = "Witch", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, M/DF (the fang of a poisonous creature)"
range = "touch"
effects = [
  { label = "Target", value = "one weapon or a single piece of ammunition" },
]
duration = "24 hours"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 3: Alchemist, Antipaladin, Cleric, Druid, Hunter, Investigator, Oracle, Ranger, Warpriest, Witch
Casting time: 1 standard action
Components: V, S, M/DF (the fang of a poisonous creature)
Range: touch
Duration: 24 hours
Saving throw: none
Spell resistance: no
Target: one weapon or a single piece of ammunition
Descriptors: poison
:::

**Sources:** Dirty Tactics Toolbox pg 28

By touching a weapon against the fang of a poisonous creature and casting this spell, you drain 1
dose of the creature's poison, which is magically applied to your weapon without risk of poisoning
yourself. The poison remains on the weapon until either it strikes a creature, you touch the weapon,
or you wipe off the poison. It otherwise functions exactly like a dose of a manufactured poison
applied to a weapon. You can use this spell with natural as well as manufactured weapons. This spell
does not prevent you from exposing yourself to the poison if you roll a natural 1 on an attack roll
while the poison is applied to your weapon.

The spell has no effect if the creature whose fang is touched is a summoned creature, if it has been
dead for more than 1 minute, or if its poison has already been extracted from it.
