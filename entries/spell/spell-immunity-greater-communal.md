+++
id = "ref/spell/spell-immunity-greater-communal"
kind = "spell"
title = "Greater Communal Spell Immunity"
source_ids = ["core-rulebook", "ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "spell_immunity_greater_communal", path = "json/spells9.json" },
]

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Cleric", level = 9 },
  { class = "Oracle", level = 9 },
  { class = "Psychic", level = 9 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "touch"
effects = [
  { label = "Target", value = "creatures touched" },
]
duration = "10 minutes/level"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 9: Cleric, Oracle, Psychic
Casting time: 1 standard action
Components: V, S, DF
Range: touch
Target: creatures touched
Duration: 10 minutes/level
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
:::

## Spell Immunity

**Sources:** PRPG Core Rulebook pg 346

The warded creature is immune to the effects of one specified spell for every four levels you have.
The spells must be of 4th level or lower. The warded creature effectively has unbeatable
[spell resistance](ref/rule/spell-resistance) regarding the specified spell or spells. Naturally,
that immunity doesn't protect a creature from spells for which spell resistance doesn't apply. Spell
immunity protects against spells, spell-like effects of magic items, and innate
[spell-like abilities](ref/umr/spell-like-abilities) of creatures. It does not protect against
supernatural or extraordinary abilities, such as breath weapons or gaze attacks.

Only a particular spell can be protected against, not a certain domain or school of spells or a
group of spells that are similar in effect. A creature can have only one spell immunity or greater
spell immunity spell in effect on it at a time.

### Communal Spell Immunity

**Sources:** Ultimate Combat pg 244

This spell functions like spell immunity, except you divide the duration in 10-minute intervals
among the creatures touched.

### Greater Spell Immunity

**Sources:** PRPG Core Rulebook pg 347

This spell functions like spell immunity, except the immunity applies to spells of 8th level or
lower. A creature can have only one spell immunity or greater spell immunity spell in effect on it
at a time.

### Greater Communal Spell Immunity

**Sources:** Ultimate Combat pg 245

This spell functions like greater spell immunity, except you divide the duration among the creatures
in 10-minute intervals among the creatures touched.
