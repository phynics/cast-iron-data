+++
id = "ref/spell/spell-immunity"
kind = "spell"
title = "Spell Immunity"
source_ids = ["core-rulebook", "ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "spell_immunity", path = "json/spells9.json" },
]
[[sources]]
publication = "core-rulebook"
page = "346"

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Alchemist", level = 4 },
  { class = "Cleric", level = 4 },
  { class = "Inquisitor", level = 4 },
  { class = "Investigator", level = 4 },
  { class = "Occultist", level = 4 },
  { class = "Oracle", level = 4 },
  { class = "Psychic", level = 4 },
  { class = "Spiritualist", level = 4 },
  { class = "Warpriest", level = 4 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "10 minutes/level"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 4: Alchemist, Cleric, Inquisitor, Investigator, Occultist, Oracle, Psychic, Spiritualist, Warpriest
Casting time: 1 standard action
Components: V, S, DF
Range: touch
Duration: 10 minutes/level
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
Target: creature touched
:::

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
