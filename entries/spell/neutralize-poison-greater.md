+++
id = "ref/spell/neutralize-poison-greater"
kind = "spell"
title = "Greater Neutralize Poison"
source_ids = ["core-rulebook", "dirty-tactics-toolbox"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "neutralize_poison_greater", path = "json/spells7.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/neutralize-poison" },
]
[[sources]]
publication = "dirty-tactics-toolbox"
page = "28"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Healing"]
levels = [
  { class = "Alchemist", level = 6 },
  { class = "Bard", level = 6 },
  { class = "Cleric", level = 6 },
  { class = "Druid", level = 5 },
  { class = "Hunter", level = 5 },
  { class = "Inquisitor", level = 6 },
  { class = "Investigator", level = 6 },
  { class = "Oracle", level = 6 },
  { class = "Skald", level = 6 },
  { class = "Warpriest", level = 6 },
  { class = "Witch", level = 6 },
]
casting_time = "1 standard action"
components = "V, S, M/DF (a lump of charcoal)"
range = "touch"
effects = [
  { label = "Target", value = "creature or object of up to 1 cu. ft./level touched" },
]
duration = "instantaneous or 1 hour/level (D)"
saving_throw = "Will negates (harmless) (object)"
spell_resistance = "yes (harmless) (object)"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 5: Druid, Hunter\
6: Alchemist, Bard, Cleric, Inquisitor, Investigator, Oracle, Skald, Warpriest, Witch
Casting time: 1 standard action
Components: V, S, M/DF (a lump of charcoal)
Range: touch
Target: creature or object of up to 1 cu. ft./level touched
Duration: instantaneous or 1 hour/level (D)
Saving throw: Will negates (harmless) (object)
Spell resistance: yes (harmless) (object)
Subschool: Healing
:::

### Greater Neutralize Poison

This spell functions as [neutralize poison](ref/spell/neutralize-poison), except as noted here. You
automatically succeed at all caster level checks to neutralize any poisons affecting the target
creature. The spell also reverses all instantaneous or permanent effects caused by poisons, such as
temporary ability damage or permanent ability drain (it does not heal ability drain caused by
anything other than poison, however). If you use the spell to neutralize the poison in a poisonous
creature or object, the duration is 1 hour per level rather than 10 minutes per level. If the spell
is cast on a creature, the creature can negate the effect by succeeding at a Will saving throw.
