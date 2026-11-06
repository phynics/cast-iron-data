+++
id = "ref/spell/protection-from-natural-attacks"
kind = "spell"
title = "Protection from Natural Attacks"
source_ids = ["monster-hunters-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "protection_from_natural_attacks", path = "json/spells15.json" },
]

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Alchemist", level = 3 },
  { class = "Druid", level = 4 },
  { class = "Hunter", level = 2 },
  { class = "Investigator", level = 3 },
  { class = "Psychic", level = 4 },
  { class = "Ranger", level = 2 },
  { class = "Shaman", level = 4 },
  { class = "Spiritualist", level = 3 },
  { class = "Summoner", level = 3 },
  { class = "Unchained Summoner", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, M/DF (a scale from a lizard)"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "1 minute/level"
saving_throw = "Fortitude negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 2: Hunter, Ranger\
3: Alchemist, Investigator, Spiritualist, Summoner, Unchained Summoner\
4: Druid, Psychic, Shaman
Casting time: 1 standard action
Components: V, S, M/DF (a scale from a lizard)
Range: touch
Duration: 1 minute/level
Saving throw: Fortitude negates (harmless)
Spell resistance: yes (harmless)
Target: creature touched
:::

**Sources:** Monster Hunter's Handbook pg 30

Upon casting this spell, select one type of natural attack from the following: bite, claw, gore,
hoof, pincers, slam, sting, swarm, tail slap, talon, tentacle, or wing. For the duration of the
spell, the target gains DR 5/- against all attacks from natural weapons of the selected type.
