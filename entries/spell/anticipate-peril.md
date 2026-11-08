+++
id = "ref/spell/anticipate-peril"
kind = "spell"
title = "Anticipate Peril"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "anticipate_peril", path = "json/spells.json" },
]

[fields]
kind = "spell"
school = "divination"
levels = [
  { class = "Alchemist", level = 1 },
  { class = "Arcanist", level = 1 },
  { class = "Bard", level = 1 },
  { class = "Hunter", level = 1 },
  { class = "Investigator", level = 1 },
  { class = "Medium", level = 1 },
  { class = "Mesmerist", level = 1 },
  { class = "Occultist", level = 1 },
  { class = "Psychic", level = 1 },
  { class = "Ranger", level = 1 },
  { class = "Skald", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Spiritualist", level = 1 },
  { class = "Wizard", level = 1 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "1 minute/level or until activated"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 1: Alchemist, Arcanist, Bard, Hunter, Investigator, Medium, Mesmerist, Occultist, Psychic, Ranger, Skald, Sorcerer, Spiritualist, Wizard
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: 1 minute/level or until activated
Saving throw: Will negates
Spell resistance: yes
Target: creature touched
:::

**Sources:** Ultimate Magic pg 206

A creature affected by anticipate peril gains a preternatural sense of danger. The first time during
this spell's duration that the target has to make an initiative check, the creature adds an insight
bonus on that initiative check equal to the spell's caster level (maximum +5). Once this bonus
applies, the effects of the spell end.
