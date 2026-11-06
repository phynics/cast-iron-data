+++
id = "ref/spell/antitoxin-touch"
kind = "spell"
title = "Antitoxin Touch"
source_ids = ["potions-and-poisons"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "antitoxin_touch", path = "json/spells.json" },
]

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Alchemist", level = 1 },
  { class = "Druid", level = 1 },
  { class = "Hunter", level = 1 },
  { class = "Investigator", level = 1 },
  { class = "Ranger", level = 1 },
  { class = "Shaman", level = 1 },
  { class = "Witch", level = 1 },
]
casting_time = "1 standard action"
components = "V, S, M (a small drop of antitoxin)"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "1 round/level"
saving_throw = "Fortitude negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 1: Alchemist, Druid, Hunter, Investigator, Ranger, Shaman, Witch
Casting time: 1 standard action
Components: V, S, M (a small drop of antitoxin)
Range: touch
Duration: 1 round/level
Saving throw: Fortitude negates (harmless)
Spell resistance: yes (harmless)
Target: creature touched
:::

**Sources:** Potions and Poisons pg 11

The target's skin secretes a small amount of venom-resistant oils for the spell's duration. The
target cannot accidentally poison itself while applying poison. Additionally, the target does not
risk exposure to a creature's poison when attempting to [milk venom](ref/rule/harvesting-poisons).
