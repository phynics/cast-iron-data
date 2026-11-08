+++
id = "ref/spell/delay-poison-communal"
kind = "spell"
title = "Communal Delay Poison"
source_ids = ["core-rulebook", "ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "delay_poison_communal", path = "json/spells3.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/delay-poison" },
]

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Healing"]
levels = [
  { class = "Adept", level = 2 },
  { class = "Alchemist", level = 2 },
  { class = "Bard", level = 2 },
  { class = "Cleric", level = 2 },
  { class = "Druid", level = 2 },
  { class = "Hunter", level = 1 },
  { class = "Inquisitor", level = 2 },
  { class = "Investigator", level = 2 },
  { class = "Mesmerist", level = 2 },
  { class = "Occultist", level = 2 },
  { class = "Oracle", level = 2 },
  { class = "Paladin", level = 2 },
  { class = "Ranger", level = 1 },
  { class = "Shaman", level = 2 },
  { class = "Skald", level = 2 },
  { class = "Warpriest", level = 2 },
  { class = "Witch", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "1 hour/level"
saving_throw = "Fortitude negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 1: Hunter, Ranger\
2: Adept, Alchemist, Bard, Cleric, Druid, Inquisitor, Investigator, Mesmerist, Occultist, Oracle, Paladin, Shaman, Skald, Warpriest, Witch
Casting time: 1 standard action
Components: V, S, DF
Range: touch
Duration: 1 hour/level
Saving throw: Fortitude negates (harmless)
Spell resistance: yes (harmless)
Target: creature touched
Subschool: Healing
:::

## Delay Poison

**Sources:** PRPG Core Rulebook pg 265

The subject becomes temporarily immune to poison. Any poison in its system or any poison to which it
is exposed during the spell's duration does not affect the subject until the spell's duration has
expired. Delay poison does not cure any damage that poison may have already done.

### Communal Delay Poison

**Sources:** Ultimate Combat pg 227

This spell functions like [delay poison](ref/spell/delay-poison), except you divide the duration in
1-hour intervals among the creatures touched.
