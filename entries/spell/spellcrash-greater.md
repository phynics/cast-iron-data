+++
id = "ref/spell/spellcrash-greater"
kind = "spell"
title = "Greater Spellcrash"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "spellcrash_greater", path = "json/spells9.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/spellcrash-lesser" },
]

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Arcanist", level = 8 },
  { class = "Cleric", level = 8 },
  { class = "Oracle", level = 8 },
  { class = "Sorcerer", level = 8 },
  { class = "Witch", level = 8 },
  { class = "Wizard", level = 8 },
]
casting_time = "1 standard action"
components = "V, S"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "1 round/level"
saving_throw = "Will negates; see text"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 8: Arcanist, Cleric, Oracle, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: medium (100 ft. + 10 ft./level)
Target: one creature
Duration: 1 round/level
Saving throw: Will negates; see text
Spell resistance: yes
:::

### Greater Spellcrash

**Sources:** Advanced Class Guide pg 194

This spell functions as [lesser spellcrash](ref/spell/spellcrash-lesser), except that it affects
7th-level or lower prepared spells or spell slots.
