+++
id = "ref/spell/spellcrash"
kind = "spell"
title = "Spellcrash"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "spellcrash", path = "json/spells9.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/spellcrash-lesser" },
]

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Cleric", level = 4 },
  { class = "Oracle", level = 4 },
  { class = "Psychic", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Warpriest", level = 4 },
  { class = "Witch", level = 4 },
  { class = "Wizard", level = 4 },
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
Level: 4: Arcanist, Cleric, Oracle, Psychic, Sorcerer, Warpriest, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: medium (100 ft. + 10 ft./level)
Duration: 1 round/level
Saving throw: Will negates; see text
Spell resistance: yes
Target: one creature
:::

### Spellcrash

**Sources:** Advanced Class Guide pg 193

This spell functions as [lesser spellcrash](ref/spell/spellcrash-lesser), except that it affects
5th-level or lower prepared spells or spell slots.
