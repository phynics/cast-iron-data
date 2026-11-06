+++
id = "ref/spell/tongues-communal"
kind = "spell"
title = "Communal Tongues"
source_ids = ["core-rulebook", "ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "tongues_communal", path = "json/spells10.json" },
]

[fields]
kind = "spell"
school = "divination"
levels = [
  { class = "Adept", level = 3 },
  { class = "Alchemist", level = 3 },
  { class = "Arcanist", level = 3 },
  { class = "Bard", level = 2 },
  { class = "Cleric", level = 4 },
  { class = "Inquisitor", level = 2 },
  { class = "Investigator", level = 3 },
  { class = "Medium", level = 2 },
  { class = "Mesmerist", level = 2 },
  { class = "Oracle", level = 4 },
  { class = "Psychic", level = 3 },
  { class = "Shaman", level = 4 },
  { class = "Skald", level = 2 },
  { class = "Sorcerer", level = 3 },
  { class = "Spiritualist", level = 3 },
  { class = "Summoner", level = 3 },
  { class = "Unchained Summoner", level = 3 },
  { class = "Warpriest", level = 4 },
  { class = "Witch", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, M/DF (a clay model of a ziggurat)"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "10 minutes/level"
saving_throw = "Will negates (harmless)"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 2: Bard, Inquisitor, Medium, Mesmerist, Skald\
3: Adept, Alchemist, Arcanist, Investigator, Psychic, Sorcerer, Spiritualist, Summoner, Unchained Summoner, Witch, Wizard\
4: Cleric, Oracle, Shaman, Warpriest
Casting time: 1 standard action
Components: V, M/DF (a clay model of a ziggurat)
Range: touch
Duration: 10 minutes/level
Saving throw: Will negates (harmless)
Spell resistance: no
Target: creature touched
:::

## Tongues

**Sources:** PRPG Core Rulebook pg 360

This spell grants the creature touched the ability to speak and understand the language of any
intelligent creature, whether it is a racial tongue or a regional dialect. The subject can speak
only one language at a time, although it may be able to understand several languages. Tongues does
not enable the subject to speak with creatures who don't speak. The subject can make itself
understood as far as its voice carries. This spell does not predispose any creature addressed toward
the subject in any way.

Tongues can be made permanent with a [permanency](ref/spell/permanency) spell.

### Communal Tongues

**Sources:** Ultimate Combat pg 248

This spell functions like tongues, except you divide the duration in 10-minute intervals among the
creatures touched.
