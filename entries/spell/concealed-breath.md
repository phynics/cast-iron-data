+++
id = "ref/spell/concealed-breath"
kind = "spell"
title = "Concealed Breath"
aon = "SpellDisplay.aspx?ItemName=Concealed%20Breath"
source_ids = ["heroes-of-the-darklands"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "concealed_breath", path = "json/spells12.json" },
]
[[sources]]
publication = "heroes-of-the-darklands"
page = "14"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Alchemist", level = 4 },
  { class = "Arcanist", level = 4 },
  { class = "Cleric", level = 4 },
  { class = "Druid", level = 4 },
  { class = "Hunter", level = 4 },
  { class = "Investigator", level = 4 },
  { class = "Oracle", level = 4 },
  { class = "Shaman", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Summoner", level = 4 },
  { class = "Unchained Summoner", level = 4 },
  { class = "Warpriest", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "S, M/DF (a palm-sized stone)"
range = "touch"
effects = [
  { label = "Target", value = "living creature touched" },
]
duration = "1 hour/level; see text"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 4: Alchemist, Arcanist, Cleric, Druid, Hunter, Investigator, Oracle, Shaman, Sorcerer, Summoner, Unchained Summoner, Warpriest, Wizard
Casting time: 1 standard action
Components: S, M/DF (a palm-sized stone)
Range: touch
Duration: 1 hour/level; see text
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
Target: living creature touched
:::

This spell allows affected creatures to [hold their breath](ref/misc/hold-your-breath) freely
without negative effects or risk of [suffocation](ref/rule/suffocation). Divide the duration evenly
among all creatures touched. A creature that doesn't need to breathe because of this spell is not at
risk of drowning and is immune to effects that require breathing, such as inhaled poisons. This does
not grant immunity to cloud or gas attacks that don't require breathing. While a creature is holding
its breath, it can't speak or cast spells with a verbal component (unless it's using
[Silent Spell](ref/feat/silent-spell)). This spell does not prevent a creature from breathing
normally; it just removes the need for the creature to breathe.
