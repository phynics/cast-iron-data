+++
id = "ref/spell/obscure-poison"
kind = "spell"
title = "Obscure Poison"
source_ids = ["ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "obscure_poison", path = "json/spells7.json" },
]

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Alchemist", level = 1 },
  { class = "Antipaladin", level = 1 },
  { class = "Arcanist", level = 1 },
  { class = "Bard", level = 1 },
  { class = "Cleric", level = 1 },
  { class = "Druid", level = 1 },
  { class = "Hunter", level = 1 },
  { class = "Investigator", level = 1 },
  { class = "Mesmerist", level = 1 },
  { class = "Oracle", level = 1 },
  { class = "Shaman", level = 1 },
  { class = "Skald", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Warpriest", level = 1 },
  { class = "Witch", level = 1 },
  { class = "Wizard", level = 1 },
]
casting_time = "1 standard action"
components = "S, M (herbs used in antitoxin worth 10 gp)"
range = "touch"
effects = [
  { label = "Target", value = "one dose of poison or one venomous creature touched" },
]
duration = "1 hour/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 1: Alchemist, Antipaladin, Arcanist, Bard, Cleric, Druid, Hunter, Investigator, Mesmerist, Oracle, Shaman, Skald, Sorcerer, Warpriest, Witch, Wizard
Casting time: 1 standard action
Components: S, M (herbs used in antitoxin worth 10 gp)
Range: touch
Duration: 1 hour/level
Saving throw: none
Spell resistance: no
Target: one dose of poison or one venomous creature touched
:::

**Sources:** Ultimate Intrigue pg 220

You make the touched poison difficult to detect or identify. Detect poison and similar effects
detect an obscured poison only with a successful caster level check against a DC equal to 15 + your
caster level (rolled secretly by the GM). Even if the poison is detected, the DC of Craft (alchemy)
or Wisdom checks to identify the poison is increased by 10.

If cast upon a venomous creature, obscure poison disguises all of the creature's natural poisons in
the same way.
