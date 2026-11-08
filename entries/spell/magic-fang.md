+++
id = "ref/spell/magic-fang"
kind = "spell"
title = "Magic Fang"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "magic_fang", path = "json/spells6.json" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Druid", level = 1 },
  { class = "Hunter", level = 1 },
  { class = "Ranger", level = 1 },
  { class = "Spiritualist", level = 1 },
  { class = "Summoner", level = 1 },
  { class = "Unchained Summoner", level = 1 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "touch"
effects = [
  { label = "Target", value = "living creature touched" },
]
duration = "1 minute/level"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 1: Druid, Hunter, Ranger, Spiritualist, Summoner, Unchained Summoner
Casting time: 1 standard action
Components: V, S, DF
Range: touch
Duration: 1 minute/level
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
Target: living creature touched
:::

**Sources:** PRPG Core Rulebook pg 308

Magic fang gives one natural weapon or unarmed strike of the subject a +1 enhancement bonus on
attack and damage rolls. The spell can affect a slam attack, fist, bite, or other natural weapon.
The spell does not change an unarmed strike's damage from nonlethal damage to lethal damage.

Magic fang can be made permanent with a [permanency](ref/spell/permanency) spell.
