+++
id = "ref/spell/shadowfade"
kind = "spell"
title = "Shadowfade"
source_ids = ["heroes-of-the-darklands"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "shadowfade", path = "json/spells15.json" },
]
[[sources]]
publication = "heroes-of-the-darklands"
page = "9"

[fields]
kind = "spell"
school = "illusion"
subschools = ["Shadow"]
levels = [
  { class = "Arcanist", level = 1 },
  { class = "Bard", level = 1 },
  { class = "Inquisitor", level = 1 },
  { class = "Mesmerist", level = 1 },
  { class = "Skald", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Summoner", level = 1 },
  { class = "Unchained Summoner", level = 1 },
  { class = "Wizard", level = 1 },
]
casting_time = "1 standard action"
components = "V, S, M (a blindfold)"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "1 minute/level (D)"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 1: Arcanist, Bard, Inquisitor, Mesmerist, Skald, Sorcerer, Summoner, Unchained Summoner, Wizard
Casting time: 1 standard action
Components: V, S, M (a blindfold)
Range: touch
Duration: 1 minute/level (D)
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
Target: creature touched
Subschool: Shadow
:::

In areas of darkness, the target of shadowfade is invisible to creatures using
[darkvision](ref/rule/darkvision) to see. In areas of dim light, the target gains
[concealment](ref/rule/concealment) against creatures using darkvision. This spell has no effect in
areas of normal light or brighter, and is automatically dispelled if the target enters an area of
bright light or takes a hostile action.
